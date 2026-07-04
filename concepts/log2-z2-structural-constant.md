---
title: log(2) as Z₂ Structural Constant
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [rosetta, entropy, z2, group-theory, ratchet, invariant, g-tower, simulation]
sources:
  - sim_gtower_entropy_reduction_chain (commit bbbc5776)
  - sim_cl3_bivector_entropy (commit 2375ad2a)
  - sim_spectral_triple_entropy_coupling (commit 2375ad2a)
  - sim_rosetta_su2_so3_double_cover_invariant (commit 841711df)
  - sim_gtower_sp6_symplectic_entropy (commit ba53d0f2)
  - sim_tn_gtower_bond_dimension (commit 0181d1e9)
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# log(2) as Z₂ Structural Constant

## Core claim

Wherever a Z₂ group acts — binary identification, 2:1 quotient, orientation flip, symplectic doubling — the entropy cost or gain is exactly **log(2)**. This is not a coincidence: it is the only entropy consistent with a uniform distribution over 2 indistinguishable states.

**Status**: earned candidate invariant (Rosetta R4), NOT a bridge proof. Five independent sim families agree. Cross-family agreement is the Rosetta signal.

---

## Status

This page is best read as a candidate invariant/router page built from recent worker/refinery synthesis, not as a settled theorem page.

Safe current reading:
- repeated `log(2)` appearances across Z2 quotient/doubling/orientation examples are interesting and likely load-bearing
- the page is a useful crosswalk for what to test next
- the page does **not** by itself imply canon by process while the non-classical lane remains under-run

## Established instances (2026-04-15)

| Context | Map | Entropy change | Sim | Commit |
|---|---|---|---|---|
| SU(2) → SO(3) double cover | ψ ↔ −ψ (Z₂ quotient) | **+log(2)** viewed from SO(3) | `sim_gtower_entropy_reduction_chain` | bbbc5776 |
| Cl(3) bivector rotor paths | SU(2) rotor path vs SO(3) quotient | **+log(2)** (S=0 in SU(2), S=log(2) in SO(3)) | `sim_cl3_bivector_entropy` | 2375ad2a |
| Spectral triple (Connes distance) | SU(2) vs SO(3) Connes distance | **+log(2)** gap | `sim_spectral_triple_entropy_coupling` | 2375ad2a |
| Rosetta R4 cross-check | scipy orbit quotient + clifford + sympy | All three agree < 1e-10 | `sim_rosetta_su2_so3_double_cover_invariant` | 841711df |
| O(3) → SO(3) | Orientation flip removed (Z₂ det=±1) | **−log(2)** (removes 1 bit of orientation) | `sim_gtower_entropy_reduction_chain` | bbbc5776 |
| Sp(6) bond expansion from SU(3) | Symplectic doubling (Z₂ symplectic extension) | **+log(2)** = log(6)−log(3) | `sim_gtower_sp6_symplectic_entropy` + `sim_tn_gtower_bond_dimension` | ba53d0f2, 0181d1e9 |
| Z₄ doubling map on IGT 4-ring | D: x → 2x mod 4 (Z₄ → Z₂ quotient) | **log(2)** destroyed | `sim_igt_4ring_operator_family` | pending |
| Landauer erasure | 1 bit erasure (Z₂ → trivial) | **log(2)** heat release | 84 sim corpus references | — |

---

## Why log(2)?

For any Z₂ action on a set S: the orbit of each non-fixed element has size 2. Identifying the orbit collapses entropy by log(2) (two equiprobable states → one). The universal cost of a single binary identification is:

> H(uniform over 2 outcomes) = log(2)

This is invariant under: the specific group being quotiented (SU(2), O(3), Sp(6), Z₄), the topology of the space, the choice of probability measure (as long as the Z₂ action is a bijection on non-fixed points).

**The ratchet interpretation**: each Z₂ action is a one-bit ratchet step. Information irreversibly decreases by log(2) in the direction of the quotient. The reversal (cover rather than quotient) adds log(2) of epistemic cost — because the observer can no longer distinguish which pre-image they are in.

---

## Anti-smoothing caveat

The pattern is robust but NOT yet a theorem. Current status:
- `earned`: 5 independent families agree, zero counterexamples found
- `open`: no formal proof that ALL Z₂ actions produce exactly log(2) across all embedding geometries
- `open`: Z₄ doubling map → Z₂ instance not yet formally confirmed (sim pending)
- `killed`: the pattern does NOT hold for Z₃ or higher-order cyclic groups (those give log(3), log(n) respectively)

**Only Z₂ actions produce log(2). Z_n quotients produce log(n) in general.**

---

## Structural formula

For a Z₂ action on state space X (any geometry):

```
ΔS = log(|orbit|) = log(2)    for orbits of size 2 (non-fixed points)
ΔS = 0                         for fixed points of Z₂
```

For a pure bundle reduction P → P/Z₂:
- Base entropy increases by log(2) (observer sees 2 pre-images as identical)
- Total fiber entropy decreases by log(2) (Z₂ fiber structure removed)

Net change in I_c across the quotient = log(2) (the information lost by Z₂ identification is exactly 1 bit of coherent information).

---

## Connection to Axis 0

The SU(2)→SO(3) double-cover log(2) appears in the I_c gradient along the G-tower reduction chain. At the SU(2)→SO(3) step, ∂I_c/∂step = log(2). This is the only step in the G-tower where entropy INCREASES in the direction of reduction — because the Z₂ quotient creates indistinguishability rather than destroying structure.

This makes SU(2)→SO(3) the **entropy anomaly** in the G-tower: all other steps reduce entropy, but the double-cover step increases it.

---

## Candidate Rosetta links (not yet cross-checked)

| Candidate | Description |
|---|---|
| Landauer + double-cover | Landauer erasure of 1 bit = log(2) heat = same as SU(2)→SO(3) cost. Is this the same log(2) or coincidence? |
| FEP Markov blanket boundary | Crossing from external to internal costs log(2) per boundary — same Z₂ structure? |
| Berry phase holonomy winding | Equatorial Hopf loop Hol(2π) = −1: Z₂ in the fiber. Does traversal accumulate log(2) of entropy? |
| Weyl chirality L/R | L∩R = ∅ (z3 UNSAT): two chiralities form a Z₂ pair. Chirality flip entropy? |

---

## Related pages

- [[g-tower-hopf-weyl-integration]] — G-tower entropy chain, SU(2)→SO(3) anomaly
- [[axis0-current-doctrine-state-card]] — Rosetta R4 earned items
- [[shell-local-to-coupled-program]] — all 5 stages complete; bridge claims authorized
- [[berry-phase-and-holonomy]] — Hopf bundle, holonomy, Z₂ fiber structure
- [[tensor-network-axis0]] — Sp(6) bond dimension = 6 = 2×3; expansion = log(2)
