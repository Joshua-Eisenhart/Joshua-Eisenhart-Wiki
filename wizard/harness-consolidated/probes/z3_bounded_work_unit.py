"""
z3 encoding of the bounded-work unit admissibility predicate.

Harness surface encoded: 28_bounded_work.md.

Work-unit fields:
    scope_declared              — Scope names a single bounded claim/action
    scope_is_singular           — scope_declared AND it is one unit (not "refactor the harness")
    action_in_scope             — the action taken lies inside Scope
    action_in_out_of_scope      — the action taken hits an Out-of-scope entry (skip-ahead)
    bound_exit_cited            — result-file path or named refusal recorded
    out_of_scope_enumerated     — Out-of-scope list is present (names adjacent skip-ahead targets)

Admissibility:
    work_admitted(W) =
        scope_declared AND scope_is_singular AND
        action_in_scope AND (NOT action_in_out_of_scope) AND
        bound_exit_cited AND out_of_scope_enumerated

Skip-ahead (action in Out-of-scope) is UNSAT. Missing bound-exit is UNSAT.
"""

from z3 import Bool, Solver, And, Not, sat, unsat


def work_unit_predicate(
    scope_declared,
    scope_is_singular,
    action_in_scope,
    action_in_out_of_scope,
    bound_exit_cited,
    out_of_scope_enumerated,
):
    return And(
        scope_declared,
        scope_is_singular,
        action_in_scope,
        Not(action_in_out_of_scope),
        bound_exit_cited,
        out_of_scope_enumerated,
    )


def check(record):
    s = Solver()
    flags = {k: Bool(k) for k in [
        "scope_declared", "scope_is_singular",
        "action_in_scope", "action_in_out_of_scope",
        "bound_exit_cited", "out_of_scope_enumerated",
    ]}
    for k, v in record.items():
        s.add(flags[k] == v)
    s.add(work_unit_predicate(**flags))
    return s.check()


def main():
    tests = [
        {
            "label": "positive: well-formed bounded work unit",
            "record": {
                "scope_declared": True, "scope_is_singular": True,
                "action_in_scope": True, "action_in_out_of_scope": False,
                "bound_exit_cited": True, "out_of_scope_enumerated": True,
            },
            "expected": sat,
        },
        {
            "label": "negative (skip-ahead): action hits Out-of-scope entry",
            "record": {
                "scope_declared": True, "scope_is_singular": True,
                "action_in_scope": True, "action_in_out_of_scope": True,
                "bound_exit_cited": True, "out_of_scope_enumerated": True,
            },
            "expected": unsat,
        },
        {
            "label": "negative (no bound): bound exit not cited",
            "record": {
                "scope_declared": True, "scope_is_singular": True,
                "action_in_scope": True, "action_in_out_of_scope": False,
                "bound_exit_cited": False, "out_of_scope_enumerated": True,
            },
            "expected": unsat,
        },
        {
            "label": "boundary (implicit bound): scope not declared",
            "record": {
                "scope_declared": False, "scope_is_singular": False,
                "action_in_scope": True, "action_in_out_of_scope": False,
                "bound_exit_cited": True, "out_of_scope_enumerated": True,
            },
            "expected": unsat,
        },
        {
            "label": "boundary (bound-creep): scope declared but not singular",
            "record": {
                "scope_declared": True, "scope_is_singular": False,
                "action_in_scope": True, "action_in_out_of_scope": False,
                "bound_exit_cited": True, "out_of_scope_enumerated": True,
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
