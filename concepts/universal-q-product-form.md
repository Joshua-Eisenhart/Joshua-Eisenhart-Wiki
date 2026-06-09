---
title: Universal Q-Product Form — Cross-Program Invariant
created: 2026-04-15
updated: 2026-04-24
type: concept
tags: [coupling, emergence, invariant, rosetta, simulation, mutual-information, product-form]
sources:
  - 13 coupling programs (see shell-local-to-coupled-program.md)
framing: historical_candidate_invariant
---

# Universal Q-Product Form

## Discovery

Across 13 independent coupling programs, a single structural pattern has emerged without being designed in:

> **Q = MI × ∏ H_i = 0 in every subshell combination, ≠ 0 only in the full product**

where:
- **MI** = mutual information I(A:B) = S_A + S_B - S_AB from Bell state through dephasing-MERA
- **H_i** = entropy-like quantity for shell i (= 0 when that shell is inactive)
- The product ranges over all shells in the coupling program (2-3 shells + MERA)

## Status

This page should be read as a dated compact worker/refinery synthesis over coupling-program pages, not as a final theorem surface.

Safe current reading:
- the product-form pattern is a strong candidate cross-program invariant
- several recent sims and summaries report agreement on that pattern
- this is still not enough, by itself, to imply canon by process for a nonclassical bridge lane

In particular: no proper non-classical sim campaign has yet closed this family at the level the page title might otherwise suggest.

## Evidence

The dated worker/refinery synthesis reported that 13 programs passed the zero-in-subshell invariant test with z3 UNSAT as the primary proof form:

| Program | Q form | Zero-in-subshell |
|---|---|---|
| MERA×Weyl×Hopf | I_c × H_chirality × Hol_phase | ✅ z3 UNSAT |
| Gerbe×Dirac×MERA | I_c × gap_shift × DD_class | ✅ z3 UNSAT |
| MERA×Clifford×Weyl | I_c × H_clifford × H_chirality | ✅ z3 UNSAT |
| Holographic×Clifford×Weyl | I_c × H_clifford × H_chirality | ✅ z3 UNSAT |
| SpectralTriple×Weyl×MERA | I_c × H_chirality × spectral_gap | ✅ z3 UNSAT |
| Contact×Symplectic×MERA | MI × H_contact × H_symp | ✅ z3 UNSAT |
| Symplectic×Hopf×MERA | MI × H_symp × H_hopf | ✅ z3 UNSAT |
| Gerbe×SpectralTriple×Clifford | MI × H_gerbe × H_st | ✅ z3 UNSAT |
| Weyl×Gerbe×Hopf | MI × H_weyl × H_gerbe × H_hopf | ✅ z3 UNSAT |
| Dirac×Symplectic×Weyl | MI × H_dirac × H_symp × H_weyl | ✅ z3 UNSAT |
| Holographic×Gerbe×Hopf | MI × H_holo × H_gerbe × H_hopf | ✅ z3 UNSAT |
| Contact×Clifford×MERA | MI × H_contact × H_clifford | ✅ z3 UNSAT |
| SpectralTriple×Contact×Gerbe | MI × H_st × H_contact × H_gerbe | ✅ z3 UNSAT |

## What This Is (Nominalist Reading)

This is NOT a theorem about entanglement. It is a **probe-relative indistinguishability result**:

- When any shell is absent, the coupling program cannot distinguish the state from a product state with respect to that shell's H measure
- The product Q being zero = "the probe cannot detect joint structure unless all shells simultaneously contribute"
- Q ≠ 0 in the full combination = "joint structure is detectable only when all constraint surfaces are simultaneously active"

The product form is the **minimal encoding** of this: any factor zero collapses the witness.

## Structural Notes

- z3 UNSAT is the primary proof form (structural impossibility, not probabilistic)
- sympy symbolic proof: a×b×c×d with any factor=0 → product=0 (analytic companion)
- The Pearson r(MI, Q) = 1.0 exactly (Q is linear in MI when other factors are fixed) — this is NOT a correlation result, it is a mathematical identity
- Axis 0 gradient (∂MI/∂layer < 0 under dephasing) holds 20/20 seeds — MI strictly decreases under local dephasing, confirming the MERA layer direction

## Split: I_c vs MI

Programs 1-5 used **coherent information** I_c = S(A) - S(AB) (signed; measures quantum channel capacity).
Programs 6-13 used **mutual information** MI = S_A + S_B - S_AB (non-negative; measures total correlations).

Both forms satisfy the zero-in-subshell property. The switch to MI was motivated by:
- MI ≥ 0 always (I_c can be negative after dephasing)
- MI starts at 2log(2) ≈ 1.386 for Bell state (cleaner starting point)
- Local unitary dephasing provably decreases MI (data-processing inequality)

This split is **not a contradiction** — both are valid entropy-like quantities satisfying the product invariant. They probe different aspects of the same underlying structure.

## Open Questions

1. Dated reported extensions: N=5 through N=10 product-form fixtures and a `sim_general_n_product_zero_theorem.py` symbolic fixture were reported on 2026-04-15. Treat these as candidate invariant evidence, not current nonclassical campaign closure, promotion, or a canonical theorem claim.
2. Are all Q observables from different programs actually co-varying (is there a single underlying quantity)?
3. Is the product form the ONLY form satisfying zero-in-subshell, or are there non-product witnesses?
4. What is the relationship between Q (product of shell entropies) and the Xi bridge object?

## Related Pages

- [[shell-local-to-coupled-program]] — full program status table
- [[clifford-chirality-admissible-generators]] — constraint on Clifford shell participation
- [[constraint-surface-and-process]] — constraint manifold theory
