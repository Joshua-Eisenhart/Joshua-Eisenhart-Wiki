#!/usr/bin/env python3
"""Validate a bounded Hermes-native Wizard run directory.

This is intentionally small. It does not prove scientific truth or Codex v4.1
conformance. It checks that a Hermes Wizard minimal run did not fake the basic
topology: Decision -> Failure -> Follow-Up -> Final, with explicit visibility
boundaries and a corrected `REAL_ATTEMPT_PARTIAL` label. Full v4.1 LLM council
coverage requires a stricter future validator for wide parent/member and
child/subchild fanout.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

REQUIRED = {
    "decision-receipt.md": ["wave: Decision", "member_routes", "nested_visibility"],
    "failure-receipt.md": ["wave: Failure", "input_receipts: decision-receipt.md", "nested_visibility"],
    "followup-receipt.md": ["wave: Follow-Up", "decision-receipt.md", "failure-receipt.md", "nested_visibility"],
    "final-render.md": ["🧙", "REAL_ATTEMPT_PARTIAL", "🧠 Decision", "🛡️ Failure", "🧭 Follow-Up", "✅ Compiled move", "reported_by_parent", "wide LLM council coverage", "does not prove full v4.1"],
}

BANNED_UNLESS_QUALIFIED = [
    "FULL Wizard",
    "raw nested transcript verified",
    "gpt-5.5 low verified",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir
    findings: list[str] = []
    if not run_dir.is_dir():
        findings.append(f"missing run dir: {run_dir}")
    for name, needles in REQUIRED.items():
        path = run_dir / name
        if not path.exists():
            findings.append(f"missing {name}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                findings.append(f"{name} missing {needle!r}")
        for banned in BANNED_UNLESS_QUALIFIED:
            if banned in text:
                findings.append(f"{name} contains overclaim phrase {banned!r}")
    if findings:
        print("FAIL")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("PASS")
    print(f"validated: {run_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
