"""
z3 encoding of the sim-claim tool-manifest completeness predicate.

Harness surface encoded: 31_admission_surface.md Class II.2 —
"tool-manifest completeness. Trivially boolean-encodable; not wired in
because current encodings target harness-edit claims, not sim claims."

This is the sim-claim side of the L-proof ratchet, distinct from the
harness-edit side (status-ladder / pre-emit / bounded-work / gate-ordering /
closeout). It answers: under what conditions is a sim's tool-manifest
admissible as evidence for a canonical claim?

Sim-claim fields (per SIM_TEMPLATE.py + ENFORCEMENT_AND_PROCESS_RULES.md):
    classification_set                 — `classification` assignment present
    classification_is_canonical        — `classification == "canonical"`
    classification_is_classical        — `classification == "classical_baseline"`
    tool_manifest_present              — TOOL_MANIFEST dict assignment present
    every_tool_has_tried               — every tool row has `tried` field
    every_tool_has_used                — every tool row has `used` field
    every_tool_has_nonempty_reason     — every tool row has non-empty `reason`
    tool_integration_depth_present     — TOOL_INTEGRATION_DEPTH assignment present
    at_least_one_tool_load_bearing     — some tool declared load_bearing
    load_bearing_tool_marked_used      — the load-bearing tool has used==True
    load_bearing_tool_is_non_numeric   — the load-bearing tool is NOT pytorch/numpy

Admissibility:
    sim_manifest_admitted(S) =
        classification_set AND
        tool_manifest_present AND tool_integration_depth_present AND
        every_tool_has_tried AND every_tool_has_used AND
        every_tool_has_nonempty_reason AND
        (classification_is_classical OR
         (classification_is_canonical AND
          at_least_one_tool_load_bearing AND
          load_bearing_tool_marked_used AND
          load_bearing_tool_is_non_numeric))

Key constraint: a canonical classification requires at least one
load-bearing tool outside the numeric baseline that is actually used.
A classical_baseline classification does not require load-bearing tool
integration — classical work is legitimate as non-canonical evidence.

Empty-reason and missing-field cases are UNSAT regardless of classification:
every tool row must document the attempt, even if that attempt was "not
tried — not applicable here."
"""

from z3 import Bool, Solver, And, Or, Not, Implies, sat, unsat


def sim_manifest_predicate(
    classification_set,
    classification_is_canonical,
    classification_is_classical,
    tool_manifest_present,
    every_tool_has_tried,
    every_tool_has_used,
    every_tool_has_nonempty_reason,
    tool_integration_depth_present,
    at_least_one_tool_load_bearing,
    load_bearing_tool_marked_used,
    load_bearing_tool_is_non_numeric,
):
    # Classical branch: structural completeness only
    classical_branch = And(
        classification_set,
        classification_is_classical,
        tool_manifest_present,
        tool_integration_depth_present,
        every_tool_has_tried,
        every_tool_has_used,
        every_tool_has_nonempty_reason,
    )
    # Canonical branch: structural completeness + at-least-one load-bearing
    # non-numeric tool that is actually used
    canonical_branch = And(
        classification_set,
        classification_is_canonical,
        tool_manifest_present,
        tool_integration_depth_present,
        every_tool_has_tried,
        every_tool_has_used,
        every_tool_has_nonempty_reason,
        at_least_one_tool_load_bearing,
        load_bearing_tool_marked_used,
        load_bearing_tool_is_non_numeric,
    )
    # The two classification branches are disjoint — enforce exclusivity
    exclusive_class = Not(And(classification_is_canonical, classification_is_classical))
    return And(Or(classical_branch, canonical_branch), exclusive_class)


def check(record):
    s = Solver()
    flags = {k: Bool(k) for k in [
        "classification_set",
        "classification_is_canonical",
        "classification_is_classical",
        "tool_manifest_present",
        "every_tool_has_tried",
        "every_tool_has_used",
        "every_tool_has_nonempty_reason",
        "tool_integration_depth_present",
        "at_least_one_tool_load_bearing",
        "load_bearing_tool_marked_used",
        "load_bearing_tool_is_non_numeric",
    ]}
    for k, v in record.items():
        s.add(flags[k] == v)
    s.add(sim_manifest_predicate(**flags))
    return s.check()


def main():
    tests = [
        {
            "label": "positive: canonical sim with load-bearing non-numeric tool (e.g. z3/sympy/clifford)",
            "record": {
                "classification_set": True,
                "classification_is_canonical": True,
                "classification_is_classical": False,
                "tool_manifest_present": True,
                "every_tool_has_tried": True,
                "every_tool_has_used": True,
                "every_tool_has_nonempty_reason": True,
                "tool_integration_depth_present": True,
                "at_least_one_tool_load_bearing": True,
                "load_bearing_tool_marked_used": True,
                "load_bearing_tool_is_non_numeric": True,
            },
            "expected": sat,
        },
        {
            "label": "positive: classical_baseline sim with no load-bearing tool (legit)",
            # every_tool_has_{tried,used} are field-presence flags (every tool row
            # has the `tried`/`used` key present), not value-of-field. A classical
            # baseline where no tool is actually used still has `"used": False`
            # as a key in every tool row — so every_tool_has_used remains True.
            "record": {
                "classification_set": True,
                "classification_is_canonical": False,
                "classification_is_classical": True,
                "tool_manifest_present": True,
                "every_tool_has_tried": True,
                "every_tool_has_used": True,
                "every_tool_has_nonempty_reason": True,
                "tool_integration_depth_present": True,
                "at_least_one_tool_load_bearing": False,
                "load_bearing_tool_marked_used": False,
                "load_bearing_tool_is_non_numeric": False,
            },
            "expected": sat,
        },
        {
            "label": "negative: canonical claim but no load-bearing tool (unearned canonical)",
            "record": {
                "classification_set": True,
                "classification_is_canonical": True,
                "classification_is_classical": False,
                "tool_manifest_present": True,
                "every_tool_has_tried": True,
                "every_tool_has_used": True,
                "every_tool_has_nonempty_reason": True,
                "tool_integration_depth_present": True,
                "at_least_one_tool_load_bearing": False,
                "load_bearing_tool_marked_used": False,
                "load_bearing_tool_is_non_numeric": False,
            },
            "expected": unsat,
        },
        {
            "label": "negative: canonical with load-bearing declared but tool not used (declared-but-unused)",
            "record": {
                "classification_set": True,
                "classification_is_canonical": True,
                "classification_is_classical": False,
                "tool_manifest_present": True,
                "every_tool_has_tried": True,
                "every_tool_has_used": True,
                "every_tool_has_nonempty_reason": True,
                "tool_integration_depth_present": True,
                "at_least_one_tool_load_bearing": True,
                "load_bearing_tool_marked_used": False,
                "load_bearing_tool_is_non_numeric": True,
            },
            "expected": unsat,
        },
        {
            "label": "negative: canonical with only pytorch/numpy load-bearing (numeric-baseline pretending canonical)",
            "record": {
                "classification_set": True,
                "classification_is_canonical": True,
                "classification_is_classical": False,
                "tool_manifest_present": True,
                "every_tool_has_tried": True,
                "every_tool_has_used": True,
                "every_tool_has_nonempty_reason": True,
                "tool_integration_depth_present": True,
                "at_least_one_tool_load_bearing": True,
                "load_bearing_tool_marked_used": True,
                "load_bearing_tool_is_non_numeric": False,
            },
            "expected": unsat,
        },
        {
            "label": "negative: empty reason on some tool row (unjustified skip)",
            "record": {
                "classification_set": True,
                "classification_is_canonical": True,
                "classification_is_classical": False,
                "tool_manifest_present": True,
                "every_tool_has_tried": True,
                "every_tool_has_used": True,
                "every_tool_has_nonempty_reason": False,
                "tool_integration_depth_present": True,
                "at_least_one_tool_load_bearing": True,
                "load_bearing_tool_marked_used": True,
                "load_bearing_tool_is_non_numeric": True,
            },
            "expected": unsat,
        },
        {
            "label": "negative: no classification set (malformed probe)",
            "record": {
                "classification_set": False,
                "classification_is_canonical": False,
                "classification_is_classical": False,
                "tool_manifest_present": True,
                "every_tool_has_tried": True,
                "every_tool_has_used": True,
                "every_tool_has_nonempty_reason": True,
                "tool_integration_depth_present": True,
                "at_least_one_tool_load_bearing": True,
                "load_bearing_tool_marked_used": True,
                "load_bearing_tool_is_non_numeric": True,
            },
            "expected": unsat,
        },
        {
            "label": "negative: TOOL_MANIFEST missing (no tool declaration at all)",
            "record": {
                "classification_set": True,
                "classification_is_canonical": False,
                "classification_is_classical": True,
                "tool_manifest_present": False,
                "every_tool_has_tried": False,
                "every_tool_has_used": False,
                "every_tool_has_nonempty_reason": False,
                "tool_integration_depth_present": False,
                "at_least_one_tool_load_bearing": False,
                "load_bearing_tool_marked_used": False,
                "load_bearing_tool_is_non_numeric": False,
            },
            "expected": unsat,
        },
        {
            "label": "boundary: both canonical AND classical set (classifier collision)",
            "record": {
                "classification_set": True,
                "classification_is_canonical": True,
                "classification_is_classical": True,
                "tool_manifest_present": True,
                "every_tool_has_tried": True,
                "every_tool_has_used": True,
                "every_tool_has_nonempty_reason": True,
                "tool_integration_depth_present": True,
                "at_least_one_tool_load_bearing": True,
                "load_bearing_tool_marked_used": True,
                "load_bearing_tool_is_non_numeric": True,
            },
            "expected": unsat,
        },
    ]

    all_ok = True
    for t in tests:
        result = check(t["record"])
        ok = result == t["expected"]
        all_ok = all_ok and ok
        print(f"[{'OK' if ok else 'FAIL'}] {t['label']}\n        expected={t['expected']}, got={result}")

    print()
    print("all tests passed" if all_ok else "one or more tests failed")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
