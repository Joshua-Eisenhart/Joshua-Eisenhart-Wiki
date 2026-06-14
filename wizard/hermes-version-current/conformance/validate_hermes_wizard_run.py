#!/usr/bin/env python3
"""Validate a bounded Hermes-native Wizard run directory.

CEILING: shape + bounded semantic-guard conformance only — NOT runtime proof.
This validator checks that required run artifacts exist, that the minimal
Decision -> Failure -> Follow-Up -> Final topology is visible, and that two
known gameable holes stay closed:

1. the final render may not make an unguarded FULL/canonical/raw-proof claim;
2. blocked/deferred/superseded route classes must carry a reason in the same
   receipt, not just appear as top-level labels.

It still cannot verify that a Wizard run actually executed, that model outputs
are genuine, or that scientific claims in receipts are true. Use this as a
structural/claim-ceiling gate, not as runtime execution proof.
"""
from __future__ import annotations

import argparse
import json
import re
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

REASONED_CLASSES = {"blocked", "deferred", "superseded"}

# Guarded negative examples are allowed. Unguarded positive claims are not.
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
    "not ",
    "not `",
    "no ",
    "does not",
    "do not",
    "never",
    "without",
    "cannot",
    "can't",
    "unproved",
    "not proved",
    "not verified",
    "not canonical",
    "not full",
)


def parse_fields(text: str) -> dict[str, object]:
    """Parse simple top-level `key: value` and `key:` + list fields."""
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
    """Parse a markdown `routes:` block with `- name:`, `action_class:`, `reason:`."""
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


def validate(run_dir: Path) -> list[str]:
    findings: list[str] = []
    if not run_dir.is_dir():
        findings.append(f"missing run dir: {run_dir}")
        return findings
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
            if banned in text and not is_guarded(text, text.index(banned), text.index(banned) + len(banned)):
                findings.append(f"{name} contains unguarded overclaim phrase {banned!r}")
        if name == "final-render.md":
            check_final_claims(text, findings)
        if name.endswith("receipt.md"):
            check_reasoned_route_classes(name, text, findings)
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = validate(args.run_dir)
    if args.json:
        print(json.dumps({"ok": not findings, "findings": findings, "run_dir": str(args.run_dir)}, indent=2))
    elif findings:
        print("FAIL")
        for finding in findings:
            print(f"- {finding}")
    else:
        print("PASS (shape + bounded semantic guard, not runtime proof)")
        print(f"validated: {args.run_dir}")
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
