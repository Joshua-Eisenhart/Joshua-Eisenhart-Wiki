#!/usr/bin/env python3
"""Bounded Claude child fanout with one parent-readable receipt.

Jobs are intentionally small. This wrapper exists so a Codex parent can launch
several Claude children without one slow child holding the whole route open.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import signal
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BRIDGE = SCRIPT_DIR / "claude_bridge.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run bounded Claude child fanout.")
    parser.add_argument("--jobs-file", help="JSON file containing a list of {id,prompt} jobs")
    parser.add_argument("--jobs-json", help="Inline JSON list of {id,prompt} jobs")
    parser.add_argument("--model", default="sonnet", help="Bridge model alias or full Claude model")
    parser.add_argument("--effort", default="high", help="Claude effort")
    parser.add_argument("--budget", type=float, default=1.0, help="Budget per child")
    parser.add_argument("--timeout-sec", type=float, default=20.0, help="Timeout per child")
    parser.add_argument("--max-concurrency", type=int, default=4, help="Maximum simultaneous children")
    parser.add_argument("--cwd", default=os.getcwd(), help="Working directory for child calls")
    parser.add_argument("--out-dir", default="/tmp/codex_claude_child_fanout", help="Receipt directory")
    parser.add_argument("--name", default="claude-child-fanout", help="Run name")
    parser.add_argument("--tools", default="", help="Optional tools for every child; default is no tools")
    parser.add_argument("--stop-after-completed", type=int, default=0, help="Stop once this many children complete; 0 drains all children")
    parser.add_argument("--global-timeout-sec", type=float, default=0.0, help="Whole fanout timeout; 0 disables")
    parser.add_argument("--terminate-grace-sec", type=float, default=2.0, help="Grace period before killing stopped child process groups")
    parser.add_argument("--global-max-active", type=int, default=0, help="Cross-process child start limit for this model; 0 disables")
    parser.add_argument("--global-slot-dir", default="/tmp/codex_claude_child_fanout_slots", help="Directory for cross-process child slots")
    parser.add_argument("--global-slot-stale-sec", type=float, default=600.0, help="Remove slot dirs older than this many seconds")
    return parser.parse_args()


def load_jobs(args: argparse.Namespace) -> list[dict[str, str]]:
    if bool(args.jobs_file) == bool(args.jobs_json):
        raise SystemExit("Use exactly one of --jobs-file or --jobs-json.")
    if args.jobs_file:
        jobs = json.loads(Path(args.jobs_file).read_text(encoding="utf-8"))
    else:
        jobs = json.loads(args.jobs_json)
    if not isinstance(jobs, list) or not jobs:
        raise SystemExit("Jobs must be a non-empty JSON list.")
    normalized = []
    for idx, job in enumerate(jobs, start=1):
        if not isinstance(job, dict):
            raise SystemExit(f"Job {idx} is not an object.")
        job_id = str(job.get("id") or f"child-{idx}")
        prompt = str(job.get("prompt") or "").strip()
        if not prompt:
            raise SystemExit(f"Job {job_id} has an empty prompt.")
        normalized.append({"id": job_id, "prompt": prompt})
    return normalized


def build_child_command(job: dict[str, str], args: argparse.Namespace, child_dir: Path) -> list[str]:
    child_out = child_dir / job["id"]
    child_out.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable,
        str(BRIDGE),
        "--model",
        args.model,
        "--effort",
        args.effort,
        "--budget",
        str(args.budget),
        "--timeout-sec",
        str(args.timeout_sec),
        "--cwd",
        args.cwd,
        "--out-dir",
        str(child_out),
        "--name",
        job["id"],
        "--prompt",
        job["prompt"],
    ]
    if args.tools:
        command.extend(["--tools", args.tools])
    return command


def child_result(
    job: dict[str, str],
    started_at: datetime,
    completed_at: datetime,
    raw: str,
    returncode: int,
    wrapper_timed_out: bool,
) -> dict:
    parsed_receipt = {}
    try:
        parsed_receipt = json.loads(raw)
    except json.JSONDecodeError:
        pass
    bridge_timed_out = bool(parsed_receipt.get("timed_out"))
    status = "completed" if returncode == 0 and not bridge_timed_out and not wrapper_timed_out else "timed_out" if returncode == 124 or bridge_timed_out or wrapper_timed_out else "failed"
    return {
        "id": job["id"],
        "status": status,
        "returncode": returncode,
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_ms": int((completed_at - started_at).total_seconds() * 1000),
        "bridge_receipt_path": parsed_receipt.get("receipt_path"),
        "bridge_output_path": parsed_receipt.get("output_path"),
        "model": parsed_receipt.get("model"),
        "cost_usd": (parsed_receipt.get("parsed") or {}).get("total_cost_usd"),
        "result_preview": (parsed_receipt.get("parsed") or {}).get("result_preview", "")[:800],
        "raw_preview": raw[:800],
    }


def synthetic_child_result(job: dict[str, str], status: str, reason: str, started_at: datetime | None = None) -> dict:
    now = datetime.now(timezone.utc)
    return {
        "id": job["id"],
        "status": status,
        "returncode": 124 if status in {"timed_out", "abandoned"} else None,
        "started_at": started_at.isoformat() if started_at else None,
        "completed_at": now.isoformat(),
        "duration_ms": int((now - started_at).total_seconds() * 1000) if started_at else 0,
        "bridge_receipt_path": None,
        "bridge_output_path": None,
        "model": None,
        "cost_usd": None,
        "result_preview": "",
        "raw_preview": reason,
    }


def slugify_token(text: str) -> str:
    return "".join(char if char.isalnum() or char in {"-", "_"} else "-" for char in text)[:80] or "model"


def pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def slot_is_stale(slot: Path, stale_sec: float) -> bool:
    owner = slot / "owner.json"
    now = time.time()
    try:
        age = now - slot.stat().st_mtime
    except FileNotFoundError:
        return False
    if age > stale_sec:
        return True
    if not owner.exists():
        return age > 60
    try:
        data = json.loads(owner.read_text(encoding="utf-8", errors="replace"))
        pid = int(data.get("pid") or 0)
    except Exception:
        return age > 60
    return bool(pid and not pid_alive(pid))


def acquire_global_slot(args: argparse.Namespace, child_id: str, *, block: bool) -> Path | None:
    if args.global_max_active <= 0:
        return None
    root = Path(args.global_slot_dir) / slugify_token(args.model)
    root.mkdir(parents=True, exist_ok=True)
    while True:
        for idx in range(args.global_max_active):
            slot = root / f"slot-{idx}"
            try:
                slot.mkdir()
            except FileExistsError:
                if slot_is_stale(slot, args.global_slot_stale_sec):
                    shutil.rmtree(slot, ignore_errors=True)
                    try:
                        slot.mkdir()
                    except FileExistsError:
                        continue
                else:
                    continue
            owner = {
                "pid": os.getpid(),
                "child_id": child_id,
                "acquired_at": datetime.now(timezone.utc).isoformat(),
            }
            (slot / "owner.json").write_text(json.dumps(owner, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            return slot
        if not block:
            return None
        time.sleep(0.2)


def release_global_slot(slot: Path | None) -> None:
    if slot is not None:
        shutil.rmtree(slot, ignore_errors=True)


def terminate_process_group(process: subprocess.Popen[str], grace_sec: float) -> None:
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    except Exception:
        process.terminate()
    try:
        process.wait(timeout=max(0.1, grace_sec))
        return
    except subprocess.TimeoutExpired:
        pass
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        return
    except Exception:
        process.kill()


def run_child(job: dict[str, str], args: argparse.Namespace, child_dir: Path) -> dict:
    command = build_child_command(job, args, child_dir)
    slot = acquire_global_slot(args, job["id"], block=True)

    started_at = datetime.now(timezone.utc)
    try:
        completed = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=args.timeout_sec + 10,
        )
        raw = completed.stdout
        returncode = completed.returncode
        wrapper_timed_out = False
    except subprocess.TimeoutExpired as exc:
        raw = exc.stdout or ""
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8", errors="replace")
        returncode = 124
        wrapper_timed_out = True
    finally:
        release_global_slot(slot)

    completed_at = datetime.now(timezone.utc)
    return child_result(job, started_at, completed_at, raw, returncode, wrapper_timed_out)


def run_children_managed(jobs: list[dict[str, str]], args: argparse.Namespace, child_dir: Path, max_workers: int) -> tuple[list[dict], str]:
    """Run children with early-stop support and real process-group cleanup."""
    stop_after = args.stop_after_completed if args.stop_after_completed > 0 else 0
    deadline = time.monotonic() + args.global_timeout_sec if args.global_timeout_sec and args.global_timeout_sec > 0 else None
    pending = list(jobs)
    active: dict[subprocess.Popen[str], dict] = {}
    children: list[dict] = []
    stop_reason = "drained"

    def completed_count() -> int:
        return sum(1 for child in children if child["status"] == "completed")

    def should_stop_launching() -> bool:
        if stop_after and completed_count() >= stop_after:
            return True
        if deadline and time.monotonic() >= deadline:
            return True
        return False

    def launch_available() -> None:
        while pending and len(active) < max_workers and not should_stop_launching():
            job = pending.pop(0)
            slot = acquire_global_slot(args, job["id"], block=False)
            if args.global_max_active > 0 and slot is None:
                pending.insert(0, job)
                return
            command = build_child_command(job, args, child_dir)
            child_out = child_dir / job["id"]
            child_out.mkdir(parents=True, exist_ok=True)
            stdout_path = child_out / "fanout_wrapper_stdout.json"
            stdout_handle = stdout_path.open("w", encoding="utf-8", errors="replace")
            started_at = datetime.now(timezone.utc)
            process = subprocess.Popen(
                command,
                text=True,
                stdout=stdout_handle,
                stderr=subprocess.STDOUT,
                cwd=args.cwd,
                start_new_session=True,
            )
            active[process] = {
                "job": job,
                "started_at": started_at,
                "stdout_path": stdout_path,
                "stdout_handle": stdout_handle,
                "slot": slot,
            }

    launch_available()
    while active or pending:
        for process, meta in list(active.items()):
            if process.poll() is None:
                continue
            meta["stdout_handle"].close()
            release_global_slot(meta.get("slot"))
            raw = meta["stdout_path"].read_text(encoding="utf-8", errors="replace") if meta["stdout_path"].exists() else ""
            children.append(child_result(meta["job"], meta["started_at"], datetime.now(timezone.utc), raw, process.returncode, False))
            active.pop(process, None)

        if stop_after and completed_count() >= stop_after:
            stop_reason = "stop_after_completed"
            break
        if deadline and time.monotonic() >= deadline:
            stop_reason = "global_timeout"
            break

        launch_available()
        if not active and not pending:
            break
        time.sleep(0.1)

    if stop_reason != "drained":
        for process, meta in list(active.items()):
            terminate_process_group(process, args.terminate_grace_sec)
            meta["stdout_handle"].close()
            release_global_slot(meta.get("slot"))
            raw = meta["stdout_path"].read_text(encoding="utf-8", errors="replace") if meta["stdout_path"].exists() else ""
            child = child_result(meta["job"], meta["started_at"], datetime.now(timezone.utc), raw, process.returncode or 124, True)
            if stop_reason == "stop_after_completed":
                child["status"] = "abandoned"
                child["raw_preview"] = raw[:800] or stop_reason
            children.append(child)
            active.pop(process, None)
        for job in pending:
            children.append(synthetic_child_result(job, "not_launched", stop_reason))

    return children, stop_reason


def main() -> int:
    args = parse_args()
    jobs = load_jobs(args)
    max_workers = max(1, min(args.max_concurrency, len(jobs)))
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = Path(args.out_dir) / f"{timestamp}-{args.name}"
    child_dir = run_dir / "children"
    child_dir.mkdir(parents=True, exist_ok=True)

    started_at = datetime.now(timezone.utc)
    if args.stop_after_completed > 0 or args.global_timeout_sec > 0:
        children, stop_reason = run_children_managed(jobs, args, child_dir, max_workers)
    else:
        stop_reason = "drained"
        children = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(run_child, job, args, child_dir) for job in jobs]
            for future in concurrent.futures.as_completed(futures):
                children.append(future.result())
    completed_at = datetime.now(timezone.utc)

    counts = {
        "completed": sum(1 for child in children if child["status"] == "completed"),
        "failed": sum(1 for child in children if child["status"] == "failed"),
        "timed_out": sum(1 for child in children if child["status"] == "timed_out"),
        "abandoned": sum(1 for child in children if child["status"] == "abandoned"),
        "not_launched": sum(1 for child in children if child["status"] == "not_launched"),
        "total": len(children),
    }
    receipt = {
        "route": args.name,
        "status": "completed" if counts["completed"] == len(jobs) else "partial" if counts["completed"] else "failed",
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_ms": int((completed_at - started_at).total_seconds() * 1000),
        "model": args.model,
        "effort": args.effort,
        "timeout_sec": args.timeout_sec,
        "global_timeout_sec": args.global_timeout_sec,
        "max_concurrency": max_workers,
        "stop_after_completed": args.stop_after_completed,
        "stop_reason": stop_reason,
        "counts": counts,
        "children": sorted(children, key=lambda child: child["id"]),
    }
    receipt_path = run_dir / "fanout_receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    receipt["receipt_path"] = str(receipt_path)
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if counts["completed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
