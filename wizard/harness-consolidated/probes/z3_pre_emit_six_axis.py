"""
z3 encoding of the pre-emit six-axis audit predicate.

Harness surface encoded: 17_pre_emit_audit.md.

Six axes for a candidate sentence s:
    1. probe_cited            — named M if sentence uses identity/equality/equivalence
    2. constraint_cited       — named C if sentence asserts existence/behavior
    3. quotient_named         — named S/~_M if sentence collapses a set
    4. status_labeled         — exactly one of {exists, runs, passes, canonical}, no inference from lower
    5. divergence_preserved   — named surviving set, or explicit "exclusion evidence incomplete"
    6. banned_construction_absent — zero banned verbs / "the correct X" / forward-only chain

Axes 1–3 are conditionally required based on the sentence's structural features.
Axes 4–6 are always required.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/z3_pre_emit_six_axis.py

Exit 0 iff all tests hit expected SAT/UNSAT outcomes.
"""

from z3 import Bool, Solver, And, Or, Not, Implies, sat, unsat


def pre_emit_predicate(
    has_identity_claim,
    asserts_existence,
    collapses_set,
    probe_cited,
    constraint_cited,
    quotient_named,
    status_labeled,
    divergence_preserved,
    banned_construction_absent,
):
    """
    Conjunction of six axes; axes 1–3 guarded by structural features.
    """
    axis1 = Implies(has_identity_claim, probe_cited)
    axis2 = Implies(asserts_existence, constraint_cited)
    axis3 = Implies(collapses_set, quotient_named)
    axis4 = status_labeled
    axis5 = divergence_preserved
    axis6 = banned_construction_absent
    return And(axis1, axis2, axis3, axis4, axis5, axis6)


def check(sentence_record):
    s = Solver()
    flags = {k: Bool(k) for k in [
        "has_identity_claim", "asserts_existence", "collapses_set",
        "probe_cited", "constraint_cited", "quotient_named",
        "status_labeled", "divergence_preserved", "banned_construction_absent",
    ]}
    for k, v in sentence_record.items():
        s.add(flags[k] == v)
    s.add(pre_emit_predicate(**flags))
    return s.check()


def main():
    tests = [
        {
            "label": "positive: admissible sentence (identity + probe cited + all axes clean)",
            "record": {
                "has_identity_claim": True, "asserts_existence": True, "collapses_set": False,
                "probe_cited": True, "constraint_cited": True, "quotient_named": False,
                "status_labeled": True, "divergence_preserved": True, "banned_construction_absent": True,
            },
            "expected": sat,
        },
        {
            "label": "negative (axis 1): identity claim without probe family cited",
            "record": {
                "has_identity_claim": True, "asserts_existence": False, "collapses_set": False,
                "probe_cited": False, "constraint_cited": False, "quotient_named": False,
                "status_labeled": True, "divergence_preserved": True, "banned_construction_absent": True,
            },
            "expected": unsat,
        },
        {
            "label": "negative (axis 3): collapses surviving set without naming quotient",
            "record": {
                "has_identity_claim": False, "asserts_existence": False, "collapses_set": True,
                "probe_cited": False, "constraint_cited": False, "quotient_named": False,
                "status_labeled": True, "divergence_preserved": True, "banned_construction_absent": True,
            },
            "expected": unsat,
        },
        {
            "label": "negative (axis 6): banned construction present",
            "record": {
                "has_identity_claim": False, "asserts_existence": False, "collapses_set": False,
                "probe_cited": False, "constraint_cited": False, "quotient_named": False,
                "status_labeled": True, "divergence_preserved": True, "banned_construction_absent": False,
            },
            "expected": unsat,
        },
        {
            "label": "boundary: no structural features triggered, axes 4-6 clean",
            "record": {
                "has_identity_claim": False, "asserts_existence": False, "collapses_set": False,
                "probe_cited": False, "constraint_cited": False, "quotient_named": False,
                "status_labeled": True, "divergence_preserved": True, "banned_construction_absent": True,
            },
            "expected": sat,
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
