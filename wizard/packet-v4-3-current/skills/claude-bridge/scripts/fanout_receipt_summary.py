#!/usr/bin/env python3
"""Summarize Claude/Gemini fanout receipts without hand-reading logs."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


DEFAULT_ROOTS = [
    Path("/tmp/codex_claude_child_fanout"),
    Path("/tmp/codex_gemini_child_fanout"),
]
STATUS_KEYS = ["completed", "failed", "timed_out", "abandoned", "not_launched", "total"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize fanout_receipt.json files.")
    parser.add_argument("paths", nargs="*", help="Receipt files or directories. Defaults to known /tmp fanout roots.")
    parser.add_argument("--route-prefix", action="append", default=[], help="Only include routes with this prefix. Repeatable.")
    parser.add_argument("--since-min", type=float, default=0.0, help="Only include receipts completed in the last N minutes.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON instead of concise text.")
    parser.add_argument("--show-routes", action="store_true", help="Include one line per route in text output.")
    return parser.parse_args()


def parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def receipt_paths(paths: list[str]) -> list[Path]:
    roots = [Path(path).expanduser() for path in paths] if paths else DEFAULT_ROOTS
    found: list[Path] = []
    for root in roots:
        if root.is_file():
            found.append(root)
        elif root.is_dir():
            found.extend(root.rglob("fanout_receipt.json"))
    return sorted(set(found), key=lambda path: str(path))


def load_receipt(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"path": str(path), "load_error": str(exc)}
    if isinstance(data, dict):
        data.setdefault("receipt_path", str(path))
        return data
    return {"path": str(path), "load_error": "receipt root is not an object"}


def include_receipt(receipt: dict[str, Any], args: argparse.Namespace, cutoff: datetime | None) -> bool:
    route = str(receipt.get("route") or "")
    if args.route_prefix and not any(route.startswith(prefix) for prefix in args.route_prefix):
        return False
    if cutoff:
        completed_at = parse_dt(receipt.get("completed_at"))
        if not completed_at or completed_at < cutoff:
            return False
    return True


def child_counts(receipt: dict[str, Any]) -> Counter[str]:
    counts = Counter()
    raw_counts = receipt.get("counts")
    if isinstance(raw_counts, dict):
        for key in STATUS_KEYS:
            value = raw_counts.get(key, 0)
            if isinstance(value, int):
                counts[key] += value
    if counts:
        return counts
    children = receipt.get("children")
    if isinstance(children, list):
        for child in children:
            if isinstance(child, dict):
                counts[str(child.get("status") or "unknown")] += 1
        counts["total"] = len(children)
    return counts


def summarize(receipts: list[dict[str, Any]]) -> dict[str, Any]:
    aggregate = Counter()
    model_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    route_rows: list[dict[str, Any]] = []
    by_prefix: dict[str, Counter[str]] = defaultdict(Counter)
    durations: list[int] = []

    for receipt in receipts:
        counts = child_counts(receipt)
        aggregate.update(counts)
        route = str(receipt.get("route") or "unknown")
        prefix = route.split("-", 1)[0] if "-" in route else route
        by_prefix[prefix].update(counts)
        model_counts[str(receipt.get("model") or "unknown")] += 1
        status_counts[str(receipt.get("status") or "unknown")] += 1
        duration = receipt.get("duration_ms")
        if isinstance(duration, int):
            durations.append(duration)
        route_rows.append(
            {
                "route": route,
                "status": receipt.get("status"),
                "model": receipt.get("model"),
                "duration_ms": duration,
                "counts": {key: counts.get(key, 0) for key in STATUS_KEYS},
                "receipt_path": receipt.get("receipt_path"),
            }
        )

    return {
        "parent_receipts": len(receipts),
        "child_counts": {key: aggregate.get(key, 0) for key in STATUS_KEYS},
        "parent_statuses": dict(sorted(status_counts.items())),
        "models": dict(sorted(model_counts.items())),
        "duration_ms": {
            "min": min(durations) if durations else None,
            "max": max(durations) if durations else None,
            "avg": int(sum(durations) / len(durations)) if durations else None,
        },
        "by_prefix": {
            prefix: {key: counts.get(key, 0) for key in STATUS_KEYS}
            for prefix, counts in sorted(by_prefix.items())
        },
        "routes": sorted(route_rows, key=lambda row: str(row["route"])),
    }


def print_text(summary: dict[str, Any], *, show_routes: bool) -> None:
    counts = summary["child_counts"]
    duration = summary["duration_ms"]
    print(
        "fanout receipts: "
        f"parents={summary['parent_receipts']} "
        f"children={counts['completed']}/{counts['total']} completed "
        f"failed={counts['failed']} timed_out={counts['timed_out']} "
        f"abandoned={counts['abandoned']} not_launched={counts['not_launched']}"
    )
    print(
        "durations_ms: "
        f"min={duration['min']} avg={duration['avg']} max={duration['max']}"
    )
    print("models: " + ", ".join(f"{model}={count}" for model, count in summary["models"].items()))
    if summary["by_prefix"]:
        print("prefixes:")
        for prefix, prefix_counts in summary["by_prefix"].items():
            print(
                f"  {prefix}: {prefix_counts['completed']}/{prefix_counts['total']} completed, "
                f"timed_out={prefix_counts['timed_out']}, abandoned={prefix_counts['abandoned']}, "
                f"not_launched={prefix_counts['not_launched']}"
            )
    if show_routes:
        print("routes:")
        for row in summary["routes"]:
            counts = row["counts"]
            print(
                f"  {row['route']}: {row['model']} {row['status']} "
                f"{counts['completed']}/{counts['total']} completed, "
                f"timed_out={counts['timed_out']}, abandoned={counts['abandoned']}, "
                f"not_launched={counts['not_launched']}"
            )


def main() -> int:
    args = parse_args()
    cutoff = None
    if args.since_min > 0:
        cutoff = datetime.now(timezone.utc) - timedelta(minutes=args.since_min)

    receipts: list[dict[str, Any]] = []
    load_errors: list[dict[str, Any]] = []
    for path in receipt_paths(args.paths):
        receipt = load_receipt(path)
        if not receipt:
            continue
        if "load_error" in receipt:
            load_errors.append(receipt)
            continue
        if include_receipt(receipt, args, cutoff):
            receipts.append(receipt)

    summary = summarize(receipts)
    if load_errors:
        summary["load_errors"] = load_errors

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print_text(summary, show_routes=args.show_routes)
        if load_errors:
            print(f"load_errors={len(load_errors)}", file=sys.stderr)
    return 0 if receipts else 1


if __name__ == "__main__":
    raise SystemExit(main())
