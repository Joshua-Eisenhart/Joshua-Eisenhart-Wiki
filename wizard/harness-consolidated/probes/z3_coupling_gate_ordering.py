"""
z3 encoding of the coupling-program gate ordering admissibility predicate.

Harness surface encoded: 06_coupling_program_order.md.

Steps 1–6 with strict admission ordering:
    1. Shell-local lego sims
    2. Pairwise coupling (requires step 1 result file for both shells)
    3. Multi-shell coexistence (requires step 2 result)
    4. Topology-variant reruns (requires steps 1-3 closed)
    5. Emergence tests (requires step 4 closed)
    6. Bridge claims: rho_AB, Xi, Phi0, Axis 0 (requires steps 1-5 closed)

For a claim to admit step N, result-file evidence for all steps ≤ N must be cited.
Admitting step N without cited evidence for step N-1 is the primary skip-ahead / narrative-substitution failure — UNSAT under this encoding.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/z3_coupling_gate_ordering.py
"""

from z3 import Bool, Int, Solver, And, Or, Not, Implies, sat, unsat


# Outcome reasons (Class II.3 fix per 31_admission_surface.md, audit 2026-04-18):
# distinguishes malformed-claim UNSAT (step outside 1..6) from inadmissible-under-
# ordering UNSAT (step within 1..6 but missing prior-step evidence). Without this
# distinction, a malformed claim like step=7 passes as UNSAT for the "right
# verdict, wrong reason" failure mode.
ADMITTED = "admitted"
INADMISSIBLE = "inadmissible_under_order"
MALFORMED = "malformed_claim"


def malformed_predicate(claimed_step):
    """Step number is outside the valid 1..6 range defined by 06_coupling_program_order.md."""
    return Or(claimed_step < 1, claimed_step > 6)


def gate_ordering_predicate(
    claimed_step,
    evidence_step1,
    evidence_step2,
    evidence_step3,
    evidence_step4,
    evidence_step5,
    evidence_step6,
):
    """
    Admissible iff for the claimed step N, all steps M <= N have cited evidence.
    """
    return Or(
        And(claimed_step == 1, evidence_step1),
        And(claimed_step == 2, evidence_step1, evidence_step2),
        And(claimed_step == 3, evidence_step1, evidence_step2, evidence_step3),
        And(claimed_step == 4, evidence_step1, evidence_step2, evidence_step3, evidence_step4),
        And(claimed_step == 5, evidence_step1, evidence_step2, evidence_step3, evidence_step4, evidence_step5),
        And(claimed_step == 6, evidence_step1, evidence_step2, evidence_step3, evidence_step4, evidence_step5, evidence_step6),
    )


def check(claimed_step_value, evidence):
    """Backward-compatible: returns sat/unsat. Use check_with_reason() for the
    malformed-vs-inadmissible distinction."""
    s = Solver()
    claim = Int("claimed_step")
    flags = {f"evidence_step{i}": Bool(f"evidence_step{i}") for i in range(1, 7)}

    s.add(claim == claimed_step_value)
    s.add(claim >= 1, claim <= 6)
    for i in range(1, 7):
        s.add(flags[f"evidence_step{i}"] == evidence[f"step{i}"])

    s.add(gate_ordering_predicate(claim, *(flags[f"evidence_step{i}"] for i in range(1, 7))))
    return s.check()


def check_with_reason(claimed_step_value, evidence):
    """
    Returns (verdict, reason). Verdict is sat/unsat from z3; reason is one of
    ADMITTED / INADMISSIBLE / MALFORMED. Distinguishes the two UNSAT classes
    so a malformed claim is not silently equivalent to an inadmissible one.

    Encoding: malformed_predicate is checked SAT-side under z3 first
    (claim outside 1..6 makes malformed_predicate satisfiable). If malformed,
    the gate predicate is not consulted — the claim is structurally void.
    """
    s_mal = Solver()
    c_mal = Int("claim_malformed_check")
    s_mal.add(c_mal == claimed_step_value)
    s_mal.add(malformed_predicate(c_mal))
    if s_mal.check() == sat:
        return (unsat, MALFORMED)

    verdict = check(claimed_step_value, evidence)
    return (verdict, ADMITTED if verdict == sat else INADMISSIBLE)


def main():
    tests = [
        {
            "label": "positive: claim step 2 admitted with step 1 + step 2 evidence",
            "claim": 2,
            "evidence": {"step1": True, "step2": True, "step3": False, "step4": False, "step5": False, "step6": False},
            "expected": sat,
            "expected_reason": ADMITTED,
        },
        {
            "label": "negative (narrative substitution): claim step 6 admitted with only step 1 evidence",
            "claim": 6,
            "evidence": {"step1": True, "step2": False, "step3": False, "step4": False, "step5": False, "step6": False},
            "expected": unsat,
            "expected_reason": INADMISSIBLE,
        },
        {
            "label": "negative (skip-step): claim step 3 with step 1 + step 3 but no step 2",
            "claim": 3,
            "evidence": {"step1": True, "step2": False, "step3": True, "step4": False, "step5": False, "step6": False},
            "expected": unsat,
            "expected_reason": INADMISSIBLE,
        },
        {
            "label": "positive: claim step 6 admitted with all 1-6 evidence cited",
            "claim": 6,
            "evidence": {"step1": True, "step2": True, "step3": True, "step4": True, "step5": True, "step6": True},
            "expected": sat,
            "expected_reason": ADMITTED,
        },
        {
            "label": "boundary: claim step 1 admitted with only step 1 evidence (earliest admissible)",
            "claim": 1,
            "evidence": {"step1": True, "step2": False, "step3": False, "step4": False, "step5": False, "step6": False},
            "expected": sat,
            "expected_reason": ADMITTED,
        },
        {
            "label": "malformed: claim step 0 (below valid 1..6 range)",
            "claim": 0,
            "evidence": {"step1": True, "step2": True, "step3": True, "step4": True, "step5": True, "step6": True},
            "expected": unsat,
            "expected_reason": MALFORMED,
        },
        {
            "label": "malformed: claim step 7 (above valid 1..6 range)",
            "claim": 7,
            "evidence": {"step1": True, "step2": True, "step3": True, "step4": True, "step5": True, "step6": True},
            "expected": unsat,
            "expected_reason": MALFORMED,
        },
        {
            "label": "malformed: claim step -1 (negative)",
            "claim": -1,
            "evidence": {"step1": True, "step2": True, "step3": True, "step4": True, "step5": True, "step6": True},
            "expected": unsat,
            "expected_reason": MALFORMED,
        },
    ]

    all_ok = True
    for t in tests:
        verdict, reason = check_with_reason(t["claim"], t["evidence"])
        ok = (verdict == t["expected"]) and (reason == t["expected_reason"])
        all_ok = all_ok and ok
        print(f"[{'OK' if ok else 'FAIL'}] {t['label']}\n        expected={t['expected']}/{t['expected_reason']}, got={verdict}/{reason}")

    print()
    print("all tests passed" if all_ok else "one or more tests failed")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
