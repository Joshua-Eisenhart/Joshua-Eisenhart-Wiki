#!/usr/bin/env python3
"""Validate a Hermes-native Wizard v4.1 wide-council PARTIAL fixture.

CEILING: substring/shape conformance only — NOT runtime proof.
This validator checks that required strings are present in the expected files.
It cannot verify that a Wizard run actually executed, that model outputs are
genuine, or that member/child work occurred at all. A sufficiently crafted set
of markdown files will pass regardless of whether any real council work happened.
Use this as a structural gate, not as evidence of runtime execution or genuine
multi-model fanout.

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

REASONED_CLASSES = {"blocked", "deferred", "superseded"}

FINAL_OVERCLAIM_PATTERNS = [
    r"\bREAL_ATTEMPT_FULL\b",
    r"\bFULL\s+(?:Hermes\s+)?Wizard\s+run\s+completed\b",
    r"\bfull\s+v4\.1\s+coverage\s+(?:proved|verified|complete|completed)\b",
    r"\ball\s+(?:selected\s+)?routes\s+(?:are\s+)?(?:complete|completed|canonical)\b",
    r"\ball\s+selected\s+routes\s+are\s+canonical\s+by\s+process\b",
    r"\bnothing\s+remains\s+blocked\b",
    r"\bno\s+move\s+remains\s+blocked\b",
    r"\braw\s+(?:nested\s+|child/subchild\s+|child\s+)?(?:transcript|evidence|proof)\s+(?:is\s+)?verified\b",
    r"\bcanonical\s+by\s+process\b",
]

NEGATION_CUES = (
    "not ", "not `", "no ", "does not", "do not", "never", "without",
    "cannot", "can't", "unproved", "not proved", "not verified",
    "not canonical", "not full",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_fields(text: str) -> dict[str, object]:
    fields: dict[str, object] = {}
    current_list_key: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        m_item = re.match(r"^\s*-\s+(.*)$", line)
        if m_item and current_list_key is not None:
            if not isinstance(fields.get(current_list_key), list):
                fields[current_list_key] = []
            fields[current_list_key].append(m_item.group(1).strip())
            continue
        m_kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m_kv:
            key, val = m_kv.group(1), m_kv.group(2).strip()
            if val == "":
                current_list_key = key
                if not isinstance(fields.get(key), list):
                    fields[key] = []
            else:
                fields[key] = val
                current_list_key = None
        else:
            current_list_key = None
    return fields


def as_list(val: object) -> list[str]:
    if val is None:
        return []
    if isinstance(val, list):
        return [str(v).strip() for v in val if str(v).strip()]
    return [v.strip() for v in str(val).split(",") if v.strip()]


def parse_routes(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    start = None
    for i, raw in enumerate(lines):
        if re.match(r"^routes:\s*$", raw):
            start = i + 1
            break
    if start is None:
        return []
    routes: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    reason_capture = False
    reason_indent = 0
    i = start
    while i < len(lines):
        raw = lines[i]
        if raw and not raw[0].isspace() and re.match(r"^[A-Za-z_][A-Za-z0-9_]*:", raw):
            break
        m_item = re.match(r"^\s*-\s*name:\s*(.*)$", raw)
        if m_item:
            if current is not None:
                routes.append(current)
            current = {"name": m_item.group(1).strip(), "action_class": "", "reason": ""}
            reason_capture = False
            i += 1
            continue
        if current is not None:
            m_ac = re.match(r"^\s+action_class:\s*(.*)$", raw)
            if m_ac:
                current["action_class"] = m_ac.group(1).strip()
                reason_capture = False
                i += 1
                continue
            m_reason = re.match(r"^(\s+)reason:\s*(.*)$", raw)
            if m_reason:
                inline = m_reason.group(2).strip()
                if inline and inline != "|":
                    current["reason"] = inline
                    reason_capture = False
                else:
                    reason_capture = True
                    reason_indent = len(m_reason.group(1))
                i += 1
                continue
            if reason_capture:
                if raw.strip() == "":
                    i += 1
                    continue
                indent = len(raw) - len(raw.lstrip())
                if indent > reason_indent:
                    current["reason"] = (current["reason"] + " " + raw.strip()).strip()
                    i += 1
                    continue
                reason_capture = False
        i += 1
    if current is not None:
        routes.append(current)
    return routes


def is_guarded(text: str, start: int, end: int) -> bool:
    # A negation in a previous sentence must not protect a new overclaim.
    # Only treat nearby same-clause/same-line negation before the match as guard.
    prefix = text[max(0, start - 90):start].lower()
    for sep in ("\n", ".", ";", "—"):
        prefix = prefix.rsplit(sep, 1)[-1]
    return any(cue in prefix for cue in NEGATION_CUES)


def check_final_claims(text: str, findings: list[str]) -> None:
    for pattern in FINAL_OVERCLAIM_PATTERNS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            if not is_guarded(text, match.start(), match.end()):
                findings.append(
                    "final-render.md contains unguarded overclaim matching "
                    f"{pattern!r}: {match.group(0)!r}"
                )


def check_reasoned_route_classes(name: str, text: str, findings: list[str]) -> None:
    fields = parse_fields(text)
    routes = parse_routes(text)
    reasoned: set[str] = set()
    for route in routes:
        ac = str(route.get("action_class", "")).strip().lower()
        if ac in REASONED_CLASSES:
            if not str(route.get("reason", "")).strip():
                findings.append(
                    f"{name}: route {route.get('name')!r} is {ac!r} with no reason "
                    "(blocked/deferred/superseded routes must state why)"
                )
            else:
                reasoned.add(ac)
    claimed = {c.lower() for c in as_list(fields.get("route_action_classes")) if c.lower() in REASONED_CLASSES}
    top_ac = str(fields.get("action_class", "")).strip().lower()
    direct_reason = str(fields.get("reason") or fields.get("blocked_reason") or fields.get("deferred_reason") or fields.get("superseded_reason") or "").strip()
    if top_ac in REASONED_CLASSES and not direct_reason:
        claimed.add(top_ac)
    for cls in sorted(claimed - reasoned):
        findings.append(
            f"{name}: claims {cls!r} but no structured `routes:` entry in the same receipt "
            "resolves to that class with a non-empty reason"
        )


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
        if name.endswith("receipt.md"):
            check_reasoned_route_classes(name, text, findings)

    final_path = run_dir / "final-render.md"
    if final_path.exists():
        final = read(final_path)
        for banned in BANNED_IN_FINAL:
            if banned in final:
                findings.append(f"final-render.md contains banned overclaim {banned!r}")
        check_final_claims(final, findings)
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
    print("PASS (substring/shape conformance, not runtime proof)")
    print(f"validated_wide_partial: {run_dir}")
    return 0


def print_findings(findings: list[str]) -> None:
    print("FAIL")
    for finding in findings:
        print(f"- {finding}")


if __name__ == "__main__":
    sys.exit(main())
