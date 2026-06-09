"""
z3 encoding of closeout-document SHAPE conformance.

Harness surface encoded: 24_closeout_templates.md (exact-N-fields rule per role)
+ Round D-prime audit finding (P2: extra `##` headings beyond Block K spec).

Lifts literal markdown shape ↔ boolean record agreement into the L-proof layer.
Where `z3_closeout_completeness.py` checks "are the required fields present and
forward_plan absent" given an OPERATOR-AUTHORED record, this file checks the
same thing given a record EXTRACTED FROM THE MARKDOWN by closeout_doc_extractor.
The two records must agree literally; any divergence (extra heading, missing
heading, ghost forward-plan heading) UNSATs.

Scope:
    - Reads a closeout doc with closeout_doc_extractor.
    - Asserts every required role field's `##` heading is present + non-empty.
    - Asserts no `##` heading matches forward-plan.
    - Asserts no `##` heading exists beyond the role's required field set
      (Round D-prime finding: appendices must be `###` or deeper).

Why this is a separate probe and not an extension of z3_closeout_completeness:
    - closeout_completeness encodes the OPERATOR's claim about the record.
    - shape_conformance encodes the DOC's literal shape against the same spec.
    - Drift between the two is the failure mode that Round D + Round D-prime
      caught (Forward plan heading; extra appendices).
    - Keeping them separate makes the drift visible: both probes can pass
      independently for the same doc, or one can fail.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/z3_closeout_shape_conformance.py
"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from z3 import Bool, Int, Solver, And, Not, sat, unsat

import z3_closeout_completeness as CO
from closeout_doc_extractor import extract_closeout_record


def shape_conformance_predicate(role, fields_present, forward_plan_present, extras_count):
    """Admissible iff every required field's heading is present AND no
    forward-plan heading exists AND no extra `##` headings exist beyond
    the role's required field set."""
    required = CO.ROLE_FIELDS[role]
    all_required = And(*[fields_present[f] for f in required])
    return And(all_required, Not(forward_plan_present), extras_count == 0)


def check_doc_shape(doc_path, role):
    """Returns (verdict, extracted_record). Verdict is sat iff the doc's
    literal shape matches the role's Block-spec exactly (required fields all
    present-and-nonempty, no forward-plan, no extra ## headings)."""
    record = extract_closeout_record(doc_path, role)

    s = Solver()
    fields_present = {f: Bool(f) for f in CO.ROLE_FIELDS[role]}
    forward_plan_present = Bool("forward_plan_present")
    extras_count = Int("extras_count")

    for f in CO.ROLE_FIELDS[role]:
        s.add(fields_present[f] == record[f])
    s.add(forward_plan_present == record["forward_plan_present"])
    s.add(extras_count == len(record["extra_top_level_headings"]))

    s.add(shape_conformance_predicate(role, fields_present, forward_plan_present, extras_count))
    return s.check(), record


# ----- self-test fixtures (positive + 3 adversarial) ------------------------

WIKI_HARNESS = Path(__file__).parent.parent


# Synthesized minimal Block K fixture used to construct adversarial variants.
# Each `## ` heading body has one non-empty line so non-emptiness check passes.
MINIMAL_BLOCK_K_OK = """\
last_updated: 2026-04-18

# Synthetic minimal Block K closeout

## Gates cited

placeholder body

## Admission decisions

placeholder body

## Narrative substitutions intercepted

placeholder body

## Worker claims verified

placeholder body

## Worker claims not verified

placeholder body

## Status label changes to registry

placeholder body

## Blocked actions

placeholder body
"""

# Adversarial variant 1: forward-plan heading present (Round D failure mode).
ADVERSARIAL_FORWARD_PLAN = MINIMAL_BLOCK_K_OK + "\n## Forward plan\n\nbad: closeout has forward plan\n"

# Adversarial variant 2: extra top-level heading (Round D-prime failure mode).
ADVERSARIAL_EXTRA_HEADING = MINIMAL_BLOCK_K_OK + "\n## Bound-exit citation\n\nbad: extra ## heading beyond Block K\n"

# Adversarial variant 3: required field missing (e.g. blocked_actions removed).
ADVERSARIAL_MISSING_FIELD = MINIMAL_BLOCK_K_OK.replace(
    "## Blocked actions\n\nplaceholder body\n", ""
)


def _temp_doc(text):
    """Write text to a temp .md file, return Path."""
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False)
    f.write(text)
    f.close()
    return Path(f.name)


TESTS = [
    {
        "label": "POSITIVE: audit_response_closeout (Block K) — current shape conforms",
        "doc": WIKI_HARNESS / "audit_response_closeout_2026_04_18.md",
        "role": "K",
        "expected": sat,
    },
    {
        "label": "POSITIVE: synthetic minimal Block K closeout — clean shape",
        "doc": _temp_doc(MINIMAL_BLOCK_K_OK),
        "role": "K",
        "expected": sat,
    },
    {
        "label": "ADVERSARIAL: forward-plan heading present — must REFUSE",
        "doc": _temp_doc(ADVERSARIAL_FORWARD_PLAN),
        "role": "K",
        "expected": unsat,
    },
    {
        "label": "ADVERSARIAL: extra top-level ## heading — must REFUSE",
        "doc": _temp_doc(ADVERSARIAL_EXTRA_HEADING),
        "role": "K",
        "expected": unsat,
    },
    {
        "label": "ADVERSARIAL: required Block K field missing — must REFUSE",
        "doc": _temp_doc(ADVERSARIAL_MISSING_FIELD),
        "role": "K",
        "expected": unsat,
    },
]


def main():
    print("== closeout shape-conformance probe (5 tests: 2 positive + 3 adversarial) ==\n")
    all_ok = True
    for t in TESTS:
        if not Path(t["doc"]).exists():
            print(f"[FAIL] {t['label']}: doc not found at {t['doc']}")
            all_ok = False
            continue
        verdict, record = check_doc_shape(t["doc"], t["role"])
        ok = verdict == t["expected"]
        all_ok = all_ok and ok
        print(f"[{'OK' if ok else 'FAIL'}] {t['label']}")
        print(f"        expected={t['expected']}, got={verdict}")
        print(f"        forward_plan_present={record['forward_plan_present']}")
        print(f"        extras={record['extra_top_level_headings']}")
        missing = [f for f in CO.ROLE_FIELDS[t['role']] if not record[f]]
        if missing:
            print(f"        missing-required-fields={missing}")
        print()

    print("all shape-conformance tests passed" if all_ok else "one or more shape-conformance tests failed")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
