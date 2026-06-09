---
title: General-N Q-Product Zero Theorem
created: 2026-04-15
updated: 2026-04-24
type: concept
tags: [coupling, invariant, product-form, n-shell, z3, sympy, simulation]
sources:
  - universal-q-product-form.md
  - sim_general_n_product_zero_theorem.py
framing: current
---

# General-N Q-Product Zero Theorem

Current concept note, not a promotion surface. The algebraic zero-product claim
is bounded to the named symbolic/SMT fixtures; it does not close a
nonclassical campaign, bridge lane, or canonical theorem claim.

## Statement

For any N shells with entropy-like quantities H_1, ..., H_N and mutual information MI:

> **Q_N = MI × H_1 × H_2 × ... × H_N = 0 iff any factor = 0**

Equivalently: Q_N ≠ 0 only when ALL of MI, H_1, ..., H_N are simultaneously nonzero.

## Proof Forms

- **sympy (algebraic)**: symbolic product a_1 × a_2 × ... × a_N with any a_i = 0 → product = 0. Checked for N=2..10 in `sim_general_n_product_zero_theorem.py` (commit 44016d118).
- **z3 (structural)**: UNSAT for "any_factor=0 AND Q>0" — structural impossibility, not probabilistic.

## Numerical Confirmation (N=3..10)

| N | Program | Q at all-active | Sub-combos tested | Commit |
|---|---|---|---|---|
| 3 | 18 triple programs (see universal-q-product-form.md) | various > 0 | all pairs = 0 | multiple |
| 5 | Weyl×Hopf×Gerbe×Dirac×MERA | Q_5 > 0 | 30 sub-4-shell combos = 0 | 97fdc870 |
| 6 | Sextuple | Q_6 > 0 | 62 sub-sextuple combos = 0 | b735bf9a5 |
| 7 | Septuple | Q_7 = 0.1315 | all sub-6 = 0 | c61fe48d8 |
| 8 | Octuple | Q_8 = 1.52 | all sub-7 = 0 | 246c48aaa |
| 9 | Nonuple | Q_9 = 1.67 | all sub-8 = 0 | d95e1ba14 |
| 10 | Decuple (all shells) | Q_10 = 0.4444 | all sub-9 = 0 | 428476a80 |

Note: Q is non-monotone in N (Q_10 < Q_9) — the value of the full-product is not a monotone function of shell count. This is structural: each new shell's H_i multiplies in, and H_i < 1 can decrease Q even while the zero-in-subshell property is preserved.

## What This Is (Nominalist Reading)

This is a probe-relative indistinguishability result, not a theorem about entanglement:

- Q = 0 in any subshell = "the probe cannot detect joint structure unless ALL shells simultaneously contribute"
- The product form is the minimal encoding: any absent shell collapses the witness
- Q > 0 at all-active = "joint structure is detectable only when the full constraint surface is activated"

The general-N fixture says this property scales across the checked symbolic shell counts and the stated product form; it is not an artifact of triples.

## Open Questions

1. ~~Is Q non-monotone in N in general?~~ **RESOLVED 2026-04-15** (commit 9b46c92b2, sim_q_nonmonotonicity_in_n_sweep): Q_{N+1} > Q_N iff H_{N+1} > 1; Q_{N+1} < Q_N iff H_{N+1} < 1. Non-monotonicity is purely value-driven. Q_10 < Q_9 because H_10 < 1 (value accident). The only structural N-invariant is zero-collapse. Analytic check: frac_increase=0.654 ≈ 68.4% (fraction of Uniform(0.1,3.0) exceeding 1.0 — consistent).
2. Does the theorem extend to continuous-N (e.g., fractional shell weights)?
3. What is the relationship between Q_N and the Xi bridge object at arbitrary N?

## Related Pages

- [[universal-q-product-form]] — cross-program evidence for the triple/quad case
- [[shell-local-to-coupled-program]] — N-shell programs in context
