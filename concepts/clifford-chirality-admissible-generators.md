---
title: Chirality-Admissible Cl(3) Generators
created: 2026-04-15
updated: 2026-05-21
type: concept
tags: [clifford, weyl, chirality, coupling, z2, constraints, simulation]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_clifford_chirality_admissible_generators.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_mera_clifford_pairwise_coupling.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_mera_clifford_weyl_triple_coexistence.py
prior_commit_refs:
  - sim_clifford_chirality_admissible_generators commit 38947c771
  - sim_mera_clifford_pairwise_coupling commit 22b9f7abe
  - sim_mera_clifford_weyl_triple_coexistence commit 946742575
framing: source_present_result_unverified_snapshot
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Chirality-Admissible Cl(3) Generators

## Core claim

Not all Cl(3) generators preserve the Weyl chirality observable γ = Z⊗Z. Only generators
whose commutator [G, γ] = 0 are **chirality-admissible** — they can participate in
Clifford-coupled evolution without breaking the chiral symmetry of the Weyl shell.

**Status**: source-present / result-unverified in this 2026-05-21 audit. The source scripts are present, but no exact current result receipt was linked here; current repo proposal/index surfaces still require review before this becomes an earned controller status. This remains NOT a bridge proof.

Repo-status boundary: the algebraic partition below is useful as a candidate generator rule. Do not promote it above source-present or source-cited without an exact current result path, rerun receipt, tool manifest, and controller-admitted classification.

---

## Admissible vs inadmissible partition (2-qubit generators)

| Generator | [G, Z⊗Z] | Status |
|---|---|---|
| XX | 0 | **admissible** |
| XY | 0 | **admissible** |
| YX | 0 | **admissible** |
| YY | 0 | **admissible** |
| ZZ | 0 | **admissible** |
| ZI | 0 | **admissible** |
| IZ | 0 | **admissible** |
| II | 0 | **admissible** (trivial) |
| XZ | ≠ 0 | **inadmissible** |
| ZX | ≠ 0 | **inadmissible** |
| YZ | ≠ 0 | **inadmissible** |
| ZY | ≠ 0 | **inadmissible** |
| XI | ≠ 0 | **inadmissible** |
| IX | ≠ 0 | **inadmissible** |
| YI | ≠ 0 | **inadmissible** |
| IY | ≠ 0 | **inadmissible** |

**8 admissible / 8 inadmissible** — a clean Z₂ split.

---

## Pattern

Standard math for the selected 2-qubit Pauli-string fixture: a Pauli string commutes with Z⊗Z iff it has an even number of X/Y factors. Repo label: this page calls those strings chirality-admissible for this fixture only.

Three useful structure classes emerge:

1. **Even-subalgebra two-qubit products** (XX, XY, YX, YY): both qubits have non-trivial Pauli,
   and the product of Paulis commutes with Z⊗Z because Z commutes with X and Y's combined parity
   is even.

2. **Z-diagonal elements** (ZZ, ZI, IZ): Z commutes with Z trivially.

3. **Inadmissible**: any generator that acts with a single Pauli on one qubit (XI, IX, YI, IY)
   or mixes Z on one qubit with X/Y on the other (XZ, ZX, YZ, ZY).

**Why**: γ = Z⊗Z is the chirality observable. Its eigenspaces (L and R chirality) are the ±1
eigenstates of Z⊗Z. A generator commutes with γ iff it maps each chirality eigenspace to itself.
Single-qubit X/Y generators flip the Z-eigenvalue on that qubit → break chirality.

---

## z3 UNSAT (structural)

The source-level structural claim is that it is impossible for a nonzero matrix to simultaneously commute AND anti-commute with Z.
`{G, Z} = 0 ∧ [G, Z] = 0 ∧ G ≠ 0` → UNSAT (integer arithmetic, 2×2 matrices).

For the selected Pauli-string basis, no nonzero basis element is both commuting and anti-commuting with Z. Arbitrary linear combinations require decomposition/projection; do not state a global binary partition without a current receipt.

---

## Coupling program implication

For the historical 2-qubit Weyl-shell fixture with γ = Z⊗Z, Clifford rotors should be built from the commuting generator set if the goal is to preserve that fixture's Weyl chirality H = log(2) across MERA layers.

The emergence observable Q_MCW = I_c × H_clifford × H_chirality depends on H_chirality surviving
the Clifford rotation. Claims that an inadmissible generator forces H_chirality → 0, destroys chirality, or collapses Q_MCW require the exact fixture and receipt; do not generalize them to higher Clifford algebras or future coupling programs.

**Candidate operational rule**: When constructing Cl(3) rotors for any future coupling program that
includes a Weyl shell, restrict to {XX, XY, YX, YY, ZZ, ZI, IZ} generators.

---

## Anti-smoothing caveat

- Pattern is for 2-qubit Cl(3) representations only; 3-qubit case not yet confirmed
- The block-diagonal rotation generator used in early Steps 2-3 sims was inadmissible —
  the coupling was valid only after restricting to chirality-preserving subspace
- Extension to higher Clifford algebras (Cl(6), Cl(9)) is open

---

## Related pages

- [[shell-local-to-coupled-program]] — larger coupling-program status surface and where this constraint fits in the shell-local → coupled lane
- [[pauli-on-weyl-loop-interaction]] — nearest existing Weyl/chirality interaction page in the live wiki
- [[clifford-geometric-algebra-reference]] — Cl(3) basis and rotor structure
- [[universal-q-product-form]] — cross-program product-form witness language used in recent coupling pages
