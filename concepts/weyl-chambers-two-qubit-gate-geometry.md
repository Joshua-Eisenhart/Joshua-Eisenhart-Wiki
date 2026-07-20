---
title: Weyl chambers — two-qubit gate geometry and density-matrix spectral strata
created: 2026-07-19
type: concept
tags: [weyl-chamber, two-qubit-gates, entanglement, density-matrix, uhlmann-phase, literature]
sources:
  - Zhang, Vala, Sastry, Whaley, "Geometric theory of nonlocal two-qubit operations", Phys. Rev. A 67, 042313 (2003); arXiv:quant-ph/0209120
  - Watts, O'Connor, Vala, "Characterizing the geometrical edges of nonlocal two-qubit gates", Phys. Rev. A 79, 052339 (2009); arXiv:0902.4124
  - Kuś, Życzkowski and related, "Geometry of entangled states" literature; arXiv:quant-ph/0006068
  - Uhlmann-Berry correspondence literature, e.g. arXiv:2208.07001; "Purification of Lindblad dynamics, geometry of mixed states and geometric phases", arXiv:1508.02279
framing: literature-only
status: research-note
---

# Weyl chambers — two-qubit gate geometry and density-matrix spectral strata

This page reports what the published literature says about two distinct
uses of the term "Weyl chamber" in quantum information. It does not connect
either use to the Codex-Ratchet model — that mapping, entirely hypothesis,
lives in [[projects/codex-ratchet/weyl-chamber-otto-attachment-hypotheses-2026-07-19]].

There are two separate literatures here, both real, both called "Weyl
chamber," and they are not the same object. Keep them apart.

## 1. The two-qubit gate Weyl chamber

Source: Zhang, Vala, Sastry, Whaley, Phys. Rev. A 67, 042313 (2003),
arXiv:quant-ph/0209120.

Any two-qubit unitary can be written, via the Cartan (KAK) decomposition of
`su(4)`, as

```
U = k1 . exp(i(c1 XX + c2 YY + c3 ZZ)) . k2
```

where `k1, k2` are local (single-qubit) unitaries and `(c1, c2, c3)` are the
non-local part. The paper's central result: the geometric structure of the
non-local part is a 3-torus, and because different points on that torus can
give locally-equivalent gates, applying Weyl group symmetry collapses the
torus onto a tetrahedron. Local equivalence classes of two-qubit gates
correspond one-to-one with points in that tetrahedron (except on its base).
This tetrahedron is the two-qubit "Weyl chamber."

Named landmarks inside the chamber (identity at the origin, CNOT and
related controlled gates, SWAP and its powers, the double-CNOT gate) sit at
specific vertices and edges — the paper and follow-on work give exact
coordinates, but the citable claim here is the qualitative structure, not
transcribed numbers this pass did not independently verify against the PDF.

Watts, O'Connor, Vala, Phys. Rev. A 79, 052339 (2009), arXiv:0902.4124,
characterize the region of the chamber occupied by "perfect entanglers" —
gates able to map some product state to a maximally entangled state — as a
polyhedron with 6 vertices, 11 edges, and 7 faces, all edges corresponding
to single-parameter gate families, entangling power computable along each
edge. The B-gate (a specific perfect entangler used for efficient two-qubit
circuit synthesis) has its own sub-region inside this polyhedron, and gate
sequences built from repeated B-gate applications trace out nested
hexahedra inside the chamber (arXiv:2601.13983, construction results using
B-gate symmetries).

Status: `exists` as literature, cited directly, not independently
re-derived or re-run inside Codex-Ratchet.

## 2. The eigenvalue-ordering Weyl chamber for density-matrix spectra

Source: the "geometry of entangled states" literature (e.g.
arXiv:quant-ph/0006068 and related Życzkowski/Bengtsson-school work), and
the flag-manifold stratification of Hermitian-matrix space.

This is a different chamber. The space of `N x N` density matrices
decomposes, via spectral decomposition `rho = U D U^dagger`, into an
ordered simplex of eigenvalues (`lambda_1 >= lambda_2 >= ... >= lambda_N`,
`sum lambda_i = 1`) crossed with a unitary orbit. The ordered-eigenvalue
simplex is again called a Weyl chamber, by analogy with the same
representation-theoretic construction (ordering the weights of a
representation modulo the Weyl group of `U(N)`).

The walls of this simplex are where two or more eigenvalues coincide —
spectral degeneracy. Away from the walls (all eigenvalues distinct), the
unitary orbit fiber over a point in the chamber is the full flag manifold
`U(N)/U(1)^N`. On a wall of degeneracy type `(k_1, k_2, ...)` (eigenvalues
grouped into blocks of those sizes), the stability subgroup grows — for
example a two-fold degeneracy in a two-qubit system leaves a stabilizer of
`U(2) x U(1) x U(1)` rather than `U(1)^4` — so the fiber becomes a smaller
partial flag manifold (a Grassmannian in the simplest case), and the orbit
dimension over that point drops. The number of distinct strata equals the
number of integer partitions of `N`.

This stratification is where the two literatures make genuine physical
contact with dynamics: crossing or passing near a wall means passing
through or near a spectral degeneracy, and that is exactly the setting for

- Landau-Zener physics (finite-time passage through or near a level
  crossing produces diabatic transitions — "quantum friction" in the
  thermodynamic-cycle literature below), and
- geometric phase around the degeneracy — for pure states this is the
  Berry phase; for the mixed states native to this project, the relevant
  object is the **Uhlmann phase**, defined via the purification `rho =
  W W^dagger` (the decomposition is not unique: any `W = sqrt(rho) . V`
  with `V` unitary also purifies `rho`), transported via Uhlmann's
  parallel-transport condition `W^dagger dW` Hermitian. The Uhlmann phase
  generalizes the Berry phase to finite-temperature, mixed-state cycles,
  and — unlike the Berry phase — it can undergo topological transitions as
  temperature or a control parameter is varied (arXiv:2103.00080,
  "Topological Uhlmann phase transitions for a spin-j particle in a
  magnetic field"; arXiv:2208.07001 on the Uhlmann-Berry correspondence;
  arXiv:1508.02279 on purification of Lindblad dynamics and mixed-state
  geometric phases).

Status: `exists` as literature, cited directly. The PDF fetches this pass
attempted could not be parsed to pull exact stratum-dimension tables or
Uhlmann-phase formulas verbatim; the qualitative structure above is
supported across the cited sources and is standard in this sub-field, but
any exact numeric coefficient should be re-checked against a primary
source before being treated as load-bearing.

## What genuinely happens at a wall crossing

Two distinct physical readouts, not to be conflated:

1. **Dynamical (Landau-Zener):** a finite-time sweep of a control parameter
   through or near a degeneracy produces diabatic (non-adiabatic)
   population transfer. In a driven cycle this shows up as irreversible
   work loss — "quantum friction" (see the Otto-cycle page).
2. **Geometric (Uhlmann/Berry):** transport around a degeneracy, even
   infinitely slowly, accumulates a phase (pure-state case: Berry;
   mixed-state case: Uhlmann) that depends only on the loop taken, not the
   rate.

Both are real, well-established, and distinct from each other. Neither
literature (gate-Weyl-chamber, spectral-Weyl-chamber) discusses the other's
chamber; they share only the name and the underlying group-theoretic
construction (ordering weights modulo a Weyl group).
