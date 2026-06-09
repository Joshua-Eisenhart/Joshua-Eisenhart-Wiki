#!/usr/bin/env python3
"""Validate a Hermes-native Wizard v4.1 wide-council PARTIAL fixture.

This validator is intentionally stricter than validate_hermes_wizard_run.py.
It does not prove full v4.1 or Codex Max Assembly. It verifies that a run claiming
wide-council work does not hide the member/child obligations or promote
parent-reported child evidence to raw verified proof.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

REQUIRED_FILES = [
    "run-plan.md",
    "decision-wide-receipt.md",
    "failure-wide-receipt.md",
    "followup-wide-receipt.md",
    "final-render.md",
]

REQUIRED_NEEDLES = {
    "decision-wide-receipt.md": [
        "mode: REAL_ATTEMPT_PARTIAL",
        "wave: Decision",
        "selected_member_obligation:",
        "expected: 7",
        "completed: 7",
        "child_subchild_obligation:",
        "expected: 14",
        "nested_visibility: reported_by_parent",
        "### Strategy",
        "### Systems",
        "### Factory",
        "### Hume/evidence",
        "### Feynman/testability",
        "### Zhuangzi/alternatives",
        "### Outside evaluator",
    ],
    "failure-wide-receipt.md": [
        "mode: REAL_ATTEMPT_PARTIAL",
        "wave: Failure",
        "input_receipts: decision-wide-receipt.md",
        "expected: 6",
        "completed: 6",
        "verdict: harden_then_execute",
        "### Popper/falsifier",
        "### Pushback/boundary",
        "### Premortem",
        "### Black/Red Hat",
        "### Calibration",
        "### Receipt audit",
    ],
    "followup-wide-receipt.md": [
        "mode: REAL_ATTEMPT_PARTIAL",
        "wave: Follow-Up",
        "decision-wide-receipt.md",
        "failure-wide-receipt.md",
        "expected: 7",
        "completed: 7",
        "### Direct option maker",
        "### Alternative/Reframe maker",
        "### Wildcard maker",
        "### All-C composition",
        "### Compile gate",
        "gate_verdict: FAIL on consumed receipts alone",
        "### Orwell wording",
        "### Factory/Strategy handoff",
        "Prompt-ready options prepared",
    ],
    "final-render.md": [
        "REAL_ATTEMPT_PARTIAL",
        "Decision 7/7",
        "Failure 6/6",
        "Follow-Up 7/7",
        "parent-reported",
        "not full v4.1",
        "Follow-up — pick a number",
        "Proof strip",
    ],
}

BANNED_IN_FINAL = [
    "REAL_ATTEMPT_FULL",
    "FULL | waves",
    "full v4.1 coverage proved",
    "raw child evidence verified",
    "raw child/subchild proof verified",
    "one-parent-per-council proves v4.1",
]

EVIDENCE_TIER_NEEDLES = [
    "parent_reported",
    "controller_visible",
    "artifact_verified",
    "test_passed",
]

GRAPH_NEEDLES = [
    "node",
    "edge",
    "DAG",
    "cycle",
    "future",
]

NEGATIVE_NEEDLES = [
    "one-parent",
    "missing",
    "wrong-parent",
    "hidden",
    "orphan",
    "cycle",
    "future",
    "collapsed alternatives",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir
    findings: list[str] = []

    if not run_dir.is_dir():
        findings.append(f"missing run dir: {run_dir}")
        print_findings(findings)
        return 1

    for name in REQUIRED_FILES:
        if not (run_dir / name).exists():
            findings.append(f"missing required file: {name}")

    for name, needles in REQUIRED_NEEDLES.items():
        path = run_dir / name
        if not path.exists():
            continue
        text = read(path)
        for needle in needles:
            if needle not in text:
                findings.append(f"{name} missing {needle!r}")

    final_path = run_dir / "final-render.md"
    if final_path.exists():
        final = read(final_path)
        for banned in BANNED_IN_FINAL:
            if banned in final:
                findings.append(f"final-render.md contains banned overclaim {banned!r}")
        for needle in EVIDENCE_TIER_NEEDLES:
            if needle not in final:
                findings.append(f"final-render.md missing evidence tier {needle!r}")
        for needle in GRAPH_NEEDLES:
            if needle not in final:
                findings.append(f"final-render.md missing graph/dependency term {needle!r}")
        for needle in NEGATIVE_NEEDLES:
            if needle not in final:
                findings.append(f"final-render.md missing negative fixture marker {needle!r}")

    # Specific overclaim guard: selected member counts must exceed one per council
    decision = read(run_dir / "decision-wide-receipt.md") if (run_dir / "decision-wide-receipt.md").exists() else ""
    failure = read(run_dir / "failure-wide-receipt.md") if (run_dir / "failure-wide-receipt.md").exists() else ""
    followup = read(run_dir / "followup-wide-receipt.md") if (run_dir / "followup-wide-receipt.md").exists() else ""
    if re.search(r"^\s*expected:\s*1\s*$", decision, re.MULTILINE) or re.search(r"^\s*expected:\s*1\s*$", failure, re.MULTILINE) or re.search(r"^\s*expected:\s*1\s*$", followup, re.MULTILINE):
        findings.append("one-parent/member expected count appears in a wide-council receipt")

    if findings:
        print_findings(findings)
        return 1
    print("PASS")
    print(f"validated_wide_partial: {run_dir}")
    return 0


def print_findings(findings: list[str]) -> None:
    print("FAIL")
    for finding in findings:
        print(f"- {finding}")


if __name__ == "__main__":
    sys.exit(main())
