#!/usr/bin/env python3
"""Small Claude Code bridge for Codex skills.

Runs `claude -p` with budget caps, captures raw output, and writes a receipt.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


MODEL_ALIASES = {
    "opus": "claude-opus-4-7",
    "sonnet": "claude-sonnet-4-6",
    "haiku": "claude-haiku-4-5-20251001",
}


def slugify(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", text.strip().lower()).strip("-")
    return text[:48] or "claude-bridge"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Claude Code from Codex with receipts.")
    parser.add_argument("--model", default="opus", help="opus, sonnet, haiku, or full Claude model name")
    parser.add_argument("--prompt", help="Prompt text")
    parser.add_argument("--prompt-file", help="Read prompt from file")
    parser.add_argument("--budget", type=float, default=2.0, help="Max budget in USD")
    parser.add_argument("--effort", default="", help="Optional Claude effort, for example low, medium, or high")
    parser.add_argument("--timeout-sec", type=float, default=0.0, help="Wall-clock timeout for the Claude process; 0 disables")
    parser.add_argument("--stream", action="store_true", help="Use stream-json --verbose output")
    parser.add_argument("--tools", default="", help="Comma-separated Claude tools to allow")
    parser.add_argument("--cwd", default=os.getcwd(), help="Working directory for Claude")
    parser.add_argument("--out-dir", default="/tmp/codex_claude_bridge", help="Directory for prompt/output/receipt")
    parser.add_argument("--name", default="", help="Optional run name")
    return parser.parse_args()


def load_prompt(args: argparse.Namespace) -> str:
    if args.prompt and args.prompt_file:
        raise SystemExit("Use --prompt or --prompt-file, not both.")
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8")
    if args.prompt:
        return args.prompt
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("Provide --prompt, --prompt-file, or stdin.")


def summarize_stream(path: Path) -> dict:
    summary = {
        "json_lines": 0,
        "agent_tool_calls": 0,
        "task_started": 0,
        "task_completed": 0,
        "rate_limit_events": 0,
        "models": [],
        "result_subtype": None,
        "is_error": None,
        "total_cost_usd": None,
    }
    models = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        summary["json_lines"] += 1
        if event.get("type") == "rate_limit_event":
            summary["rate_limit_events"] += 1
        if event.get("type") == "system" and event.get("subtype") == "task_started":
            summary["task_started"] += 1
        if (
            event.get("type") == "system"
            and event.get("subtype") == "task_notification"
            and event.get("status") == "completed"
        ):
            summary["task_completed"] += 1
        message = event.get("message") or {}
        for content in message.get("content") or []:
            if content.get("type") == "tool_use" and content.get("name") == "Agent":
                summary["agent_tool_calls"] += 1
        if event.get("type") == "result":
            summary["result_subtype"] = event.get("subtype")
            summary["is_error"] = event.get("is_error")
            summary["total_cost_usd"] = event.get("total_cost_usd")
            models.update((event.get("modelUsage") or {}).keys())
    summary["models"] = sorted(models)
    return summary


def summarize_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError:
        return {"parse_error": True}
    return {
        "result_subtype": data.get("subtype"),
        "is_error": data.get("is_error"),
        "total_cost_usd": data.get("total_cost_usd"),
        "duration_ms": data.get("duration_ms"),
        "models": sorted((data.get("modelUsage") or {}).keys()),
        "result_preview": str(data.get("result", ""))[:1000],
    }


def main() -> int:
    args = parse_args()
    prompt = load_prompt(args).strip()
    if not prompt:
        raise SystemExit("Prompt is empty.")

    model = MODEL_ALIASES.get(args.model, args.model)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    digest = hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:12]
    run_name = slugify(args.name or prompt[:80])
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    stem = out_dir / f"{timestamp}-{run_name}-{digest}"
    prompt_path = stem.with_suffix(".prompt.txt")
    output_path = stem.with_suffix(".stream.jsonl" if args.stream else ".json")
    receipt_path = stem.with_suffix(".receipt.json")
    prompt_path.write_text(prompt + "\n", encoding="utf-8")

    command = [
        "claude",
        "-p",
        "--model",
        model,
        "--output-format",
        "stream-json" if args.stream else "json",
        "--no-session-persistence",
        "--max-budget-usd",
        str(args.budget),
    ]
    if args.stream:
        command.append("--verbose")
    if args.effort:
        command.extend(["--effort", args.effort])
    if args.tools:
        command.extend(["--allowedTools", args.tools])

    timed_out = False
    timeout_sec = args.timeout_sec if args.timeout_sec and args.timeout_sec > 0 else None
    try:
        completed = subprocess.run(
            command,
            input=prompt,
            text=True,
            cwd=args.cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=timeout_sec,
        )
        stdout = completed.stdout
        returncode = completed.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        stdout = exc.stdout or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        stdout += f"\n[TIMEOUT after {args.timeout_sec}s]\n"
        returncode = 124

    output_path.write_text(stdout, encoding="utf-8", errors="replace")

    parsed = summarize_stream(output_path) if args.stream else summarize_json(output_path)
    if timed_out:
        parsed["timed_out"] = True
        parsed["timeout_sec"] = args.timeout_sec
    receipt = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "command": command,
        "cwd": args.cwd,
        "model": model,
        "returncode": returncode,
        "prompt_path": str(prompt_path),
        "output_path": str(output_path),
        "receipt_path": str(receipt_path),
        "stream": args.stream,
        "timed_out": timed_out,
        "timeout_sec": args.timeout_sec,
        "parsed": parsed,
    }
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(receipt, indent=2, sort_keys=True))
    return returncode


if __name__ == "__main__":
    raise SystemExit(main())
