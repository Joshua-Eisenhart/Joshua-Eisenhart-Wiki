"""
z3 encoding of the harness status ladder admissibility predicate.

Harness surface encoded: 04_status_label_hierarchy.md + ENFORCEMENT_AND_PROCESS_RULES.md Rule 12.

Ladder (strict, non-inflatable):
    exists < runs < passes_local_rerun < canonical_by_process

Admissibility predicate for a claimed label L under a cited-evidence set E:
    claim L is admissible iff E contains evidence for L and for every L' < L.

Inflation (claim L while only E contains L' < L without L-evidence) is UNSAT under this predicate.
This is a structural impossibility proof, not a stylistic prohibition.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/z3_status_ladder_admissibility.py

Exit 0 iff all three tests hit their expected SAT/UNSAT outcomes.
"""

from z3 import Bool, Int, Solver, And, Or, sat, unsat, Implies


L_EXISTS = 0
L_RUNS = 1
L_PASSES = 2
L_CANONICAL = 3
LABEL_NAMES = {
    L_EXISTS: "exists",
    L_RUNS: "runs",
    L_PASSES: "passes local rerun",
    L_CANONICAL: "canonical by process",
}


def admissibility_predicate(claim, e_exists, e_runs, e_passes, e_canonical):
    """
    Admissible iff the claimed label has evidence AND all lower labels have evidence.
    Encodes the non-inflation rule: higher label requires all lower labels witnessed.
    """
    return Or(
        And(claim == L_EXISTS, e_exists),
        And(claim == L_RUNS, e_runs, e_exists),
        And(claim == L_PASSES, e_passes, e_runs, e_exists),
        And(claim == L_CANONICAL, e_canonical, e_passes, e_runs, e_exists),
    )


def run_admissibility_check(claim_value, evidence):
    """
    claim_value: int in {0,1,2,3}
    evidence: dict with keys exists/runs/passes/canonical -> bool

    Returns z3 check result: sat or unsat.
    """
    s = Solver()
    claim = Int("claim")
    e_exists = Bool("e_exists")
    e_runs = Bool("e_runs")
    e_passes = Bool("e_passes")
    e_canonical = Bool("e_canonical")

    s.add(claim == claim_value)
    s.add(e_exists == evidence["exists"])
    s.add(e_runs == evidence["runs"])
    s.add(e_passes == evidence["passes"])
    s.add(e_canonical == evidence["canonical"])

    s.add(admissibility_predicate(claim, e_exists, e_runs, e_passes, e_canonical))

    return s.check()


def main():
    results = []

    test_positive = {
        "label": "positive: claim 'exists' with evidence for exists",
        "claim": L_EXISTS,
        "evidence": {"exists": True, "runs": False, "passes": False, "canonical": False},
        "expected": sat,
    }

    test_inflation = {
        "label": "negative (inflation): claim 'canonical' with only 'runs' evidence",
        "claim": L_CANONICAL,
        "evidence": {"exists": True, "runs": True, "passes": False, "canonical": False},
        "expected": unsat,
    }

    test_skip_label = {
        "label": "boundary (skip-label): claim 'runs' without 'exists' evidence",
        "claim": L_RUNS,
        "evidence": {"exists": False, "runs": True, "passes": False, "canonical": False},
        "expected": unsat,
    }

    for t in (test_positive, test_inflation, test_skip_label):
        result = run_admissibility_check(t["claim"], t["evidence"])
        ok = result == t["expected"]
        results.append((t["label"], t["expected"], result, ok))
        status = "OK" if ok else "FAIL"
        print(
            f"[{status}] {t['label']}"
            f"\n        expected={t['expected']}, got={result}"
        )

    all_ok = all(r[3] for r in results)
    print()
    print("all tests passed" if all_ok else "one or more tests failed")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
