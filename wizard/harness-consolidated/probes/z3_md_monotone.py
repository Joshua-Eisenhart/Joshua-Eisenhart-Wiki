"""
z3 encoding of the Manifold Depth (MD) monotone conjecture.

Harness surface encoded: 21_mimetic_meme_manifold.md (MD composite metric) +
30_z3_harness_formalization.md (Phase 6 deliverable).

MD composite metric:
    MD = 0.4 * (1 - D_correction) + 0.3 * D_drift + 0.3 * D_completion

where D_correction ∈ [0,1] (higher = more correction needed, so (1-D_correction)
is the "non-correction depth"), D_drift ∈ [0,1] (higher = more drift-resistant),
D_completion ∈ [0,1] (higher = more biased toward shaped completions).

Conjectures under test:

  Conj-A (pure-addition monotone) — if an edit only reduces D_correction, or only
    raises D_drift, or only raises D_completion, and never degrades any axis, then
    MD_post >= MD_pre. EXPECTED: UNSAT for any counterexample (structurally true).

  Conj-B (mixed-edit monotone) — monotone even when one axis degrades while another
    improves. EXPECTED: SAT counterexample (mixed edits can reduce MD when the
    degraded axis sits on the higher-weighted term).

  Conj-C (correction-weight counterexample) — specific failure: raising D_correction
    by ε while raising D_drift by ε' with ε' < (0.4/0.3)·ε must cause MD decrease.
    EXPECTED: SAT witness at the boundary.

Conj-A UNSAT is the structural guarantee; Conj-B SAT shows why mixed edits cannot be
admitted without checking the composite — the harness cannot coast on any single axis.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/z3_md_monotone.py
"""

from z3 import Real, Solver, And, Or, sat, unsat, Not, RealVal


W_CORR = RealVal("0.4")
W_DRIFT = RealVal("0.3")
W_COMP = RealVal("0.3")


def md_expr(d_correction, d_drift, d_completion):
    """MD = 0.4 * (1 - D_correction) + 0.3 * D_drift + 0.3 * D_completion"""
    return W_CORR * (RealVal(1) - d_correction) + W_DRIFT * d_drift + W_COMP * d_completion


def bounded(x):
    return And(x >= 0, x <= 1)


# ----- Conjecture A: pure-addition monotone ---------------------------------

def conj_a_counterexample():
    """
    Probe for: a pure-addition edit with MD_post < MD_pre.
    Pure addition = (D_correction_post <= pre) AND (D_drift_post >= pre) AND (D_completion_post >= pre).
    If this search is UNSAT, Conj-A holds structurally.
    """
    s = Solver()
    dc0, dd0, dx0 = Real("dc0"), Real("dd0"), Real("dx0")
    dc1, dd1, dx1 = Real("dc1"), Real("dd1"), Real("dx1")

    for v in (dc0, dd0, dx0, dc1, dd1, dx1):
        s.add(bounded(v))

    s.add(dc1 <= dc0)
    s.add(dd1 >= dd0)
    s.add(dx1 >= dx0)

    md0 = md_expr(dc0, dd0, dx0)
    md1 = md_expr(dc1, dd1, dx1)

    s.add(md1 < md0)
    return s.check()


# ----- Conjecture B: mixed-edit monotone ------------------------------------

def conj_b_counterexample():
    """
    Probe for: a mixed edit where MD_post < MD_pre.
    Mixed = at least one axis improves AND at least one axis degrades.
    If SAT, Conj-B is false — monotone fails under mixed edits.
    """
    s = Solver()
    dc0, dd0, dx0 = Real("dc0"), Real("dd0"), Real("dx0")
    dc1, dd1, dx1 = Real("dc1"), Real("dd1"), Real("dx1")

    for v in (dc0, dd0, dx0, dc1, dd1, dx1):
        s.add(bounded(v))

    corr_improved = dc1 < dc0
    drift_improved = dd1 > dd0
    comp_improved = dx1 > dx0
    corr_degraded = dc1 > dc0
    drift_degraded = dd1 < dd0
    comp_degraded = dx1 < dx0

    any_improved = Or(corr_improved, drift_improved, comp_improved)
    any_degraded = Or(corr_degraded, drift_degraded, comp_degraded)
    s.add(any_improved)
    s.add(any_degraded)

    md0 = md_expr(dc0, dd0, dx0)
    md1 = md_expr(dc1, dd1, dx1)
    s.add(md1 < md0)

    return s.check(), s


# ----- Conjecture C: specific correction-weight counterexample --------------

def conj_c_specific_witness():
    """
    Probe for: concrete witness where correction degrades by ε while drift rises by
    ε' with ε' < (0.4/0.3)·ε, forcing MD_post < MD_pre.
    Closes the door on "but I added drift-resistance" as a universal excuse.
    """
    s = Solver()
    dc0 = RealVal("0.1")
    dd0 = RealVal("0.5")
    dx0 = RealVal("0.5")

    eps = Real("eps")
    eps_prime = Real("eps_prime")
    s.add(eps > 0, eps <= RealVal("0.2"))
    s.add(eps_prime > 0, eps_prime <= RealVal("0.2"))

    s.add(RealVal("0.3") * eps_prime < RealVal("0.4") * eps)

    dc1 = dc0 + eps
    dd1 = dd0 + eps_prime
    dx1 = dx0

    s.add(bounded(dc1))
    s.add(bounded(dd1))

    md0 = md_expr(dc0, dd0, dx0)
    md1 = md_expr(dc1, dd1, dx1)
    s.add(md1 < md0)

    return s.check(), s


# ----- driver ---------------------------------------------------------------

def main():
    results = []

    ra = conj_a_counterexample()
    ok_a = ra == unsat
    results.append(("Conj-A (pure-addition monotone)", "UNSAT", str(ra), ok_a))
    print(f"[{'OK' if ok_a else 'FAIL'}] Conj-A: pure-addition monotone  expected=UNSAT got={ra}")

    rb, sb = conj_b_counterexample()
    ok_b = rb == sat
    results.append(("Conj-B (mixed-edit monotone)", "SAT", str(rb), ok_b))
    print(f"[{'OK' if ok_b else 'FAIL'}] Conj-B: mixed-edit counterexample  expected=SAT got={rb}")
    if rb == sat:
        m = sb.model()
        vals = {str(d): str(m[d]) for d in m.decls()}
        print(f"        witness: {vals}")

    rc, sc = conj_c_specific_witness()
    ok_c = rc == sat
    results.append(("Conj-C (correction-weight witness)", "SAT", str(rc), ok_c))
    print(f"[{'OK' if ok_c else 'FAIL'}] Conj-C: correction-weight witness  expected=SAT got={rc}")
    if rc == sat:
        m = sc.model()
        vals = {str(d): str(m[d]) for d in m.decls()}
        print(f"        witness: {vals}")

    all_ok = all(x[3] for x in results)
    print()
    print(
        "All three conjecture outcomes as expected: Conj-A UNSAT (monotone holds under pure addition),\n"
        "Conj-B SAT (mixed edits can degrade MD — weights matter), Conj-C SAT (explicit boundary witness)."
        if all_ok else "one or more conjecture probes produced an unexpected outcome"
    )
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
