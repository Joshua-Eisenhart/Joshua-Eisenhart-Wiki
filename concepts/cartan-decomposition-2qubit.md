---
title: Cartan Decomposition 2 Qubit
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, geometry, research, architecture]
sources:
  - raw/articles/new-docs/new content/cartan_decomposition_2qubit.md
  - raw/articles/new-docs/new content/operator_algebras_and_representation.md
  - raw/articles/new-docs/new content/entanglement_theory.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Cartan Decomposition 2 Qubit

## Overview
This page covers the KAK decomposition of SU(4), the Weyl chamber, special two-qubit gates, Makhlin invariants, entangling power, and perfect entanglers.

## Main points
- Every two-qubit gate can be decomposed into local unitaries and a canonical nonlocal core.
- The Weyl chamber gives a canonical parameter region for two-qubit entangling strength.
- CNOT, iSWAP, SWAP, and sqrt(SWAP) sit at distinguished chamber points.
- Local equivalence classes are tracked by invariant quantities rather than raw matrices.

## Why it matters
This is the canonical two-qubit gate geometry page for the wiki’s operator and entanglement layers.

## KAK Decomposition and Weyl Chamber
Every U in SU(4) decomposes as U = k_1 . exp(i(c_1 sigma_x tensor sigma_x + c_2 sigma_y tensor sigma_y + c_3 sigma_z tensor sigma_z)) . k_2 where k_1,k_2 are local unitaries. The Weyl chamber is pi/4 >= c_1 >= c_2 >= |c_3| >= 0 with c_1+c_2<=pi/2 at boundary c_3=0. Vertices: O=(0,0,0) identity, A_1=(pi/4,0,0) CNOT, A_2=(pi/4,pi/4,0) iSWAP, A_3=(pi/4,pi/4,pi/4) SWAP. The non-local part A(c_1,c_2,c_3) is diagonal in the Bell basis. (from cartan_decomposition_2qubit.md)

## Special Gates and Entangling Power
CNOT at (pi/4,0,0): entangling power e_p=2/9. iSWAP at (pi/4,pi/4,0): e_p=2/9 (same as CNOT). SWAP at (pi/4,pi/4,pi/4): e_p=0 (moves entanglement, doesn't create it). sqrt(SWAP) at (pi/8,pi/8,pi/8): e_p=1/9. Haar-random gates have e_p=2/9 (maximum). The B gate at (pi/4,pi/8,0) can construct any two-qubit gate with at most 2 applications + local unitaries. (from cartan_decomposition_2qubit.md)

## Makhlin Invariants and Local Equivalence
G_1 = Tr(M)^2/(16 det(U)) and G_2 = (Tr(M)^2-Tr(M^2))/(4 det(U)) where M=U^T(sigma_y tensor sigma_y)U(sigma_y tensor sigma_y). Two gates are locally equivalent iff G_1 and G_2 match. Identity: G_1=1,G_2=3. CNOT: G_1=0,G_2=1. SWAP: G_1=1,G_2=-3. Extraction algorithm: transform to magic basis, compute M=U_B^T U_B, diagonalize, solve for c_1,c_2,c_3. Cost O(1). (from cartan_decomposition_2qubit.md)

## Perfect Entanglers and Circuit Compilation
U is a perfect entangler if it can produce a maximally entangled state from some product input. Condition: c_1+c_2>=pi/4. Perfect entanglers occupy 84.19% of Weyl chamber volume. Circuit compilation: 0 CNOTs at (0,0,0), 1 CNOT at (c_1,0,0) with c_1=pi/4, 2 CNOTs at (c_1,c_2,0), 3 CNOTs for general points. The cross-resonance gate in superconducting qubits is locally equivalent to CNOT (both at (pi/4,0,0)). (from cartan_decomposition_2qubit.md)

## Related pages
- [[operator-algebras-and-representation]]
- [[entanglement-theory]]
- [[density-matrix-mathematics]]
- [[quantum-computing-applications]]
- [[cptp-maps-and-channels]]
