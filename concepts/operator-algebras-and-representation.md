---
title: Operator Algebras and Representation
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, geometry, research, architecture]
sources:
  - raw/articles/new-docs/new content/operator_algebras_and_representation.md
  - raw/articles/new-docs/new content/cartan_decomposition_2qubit.md
  - raw/articles/new-docs/references/FIBER_BUNDLES_AND_SPIN_GEOMETRY_REFERENCE.md
framing: mixed
---

# Operator Algebras and Representation

## Overview
This page covers the su(2) algebra, Clebsch-Gordan decomposition, su(4) structure, Killing form, and Casimir operators in the quantum-information setting.

## Main points
- su(2) is the basic angular-momentum algebra with familiar spin-j representations.
- Tensor products decompose by Clebsch-Gordan rules.
- Two-qubit operator space naturally organizes into local and nonlocal generators.
- Representation theory supplies the symmetry language behind the gate and state decompositions.

## Why it matters
This is the algebraic symmetry layer beneath the spin, gate, and density-matrix pages.

## Two-Qubit System: Singlet and Triplet
1/2 (x) 1/2 = 0 (+) 1 (singlet + triplet). The singlet |0,0>=(|01>-|10>)/sqrt(2) is maximally entangled (S=log2) and the unique SU(2)-invariant state. The SWAP operator P_{12} = (1/2)(I tensor I + sigma_x tensor sigma_x + sigma_y tensor sigma_y + sigma_z tensor sigma_z) has eigenvalue +1 on the triplet (symmetric) and -1 on the singlet (antisymmetric). Bell states are superpositions of singlet and triplet: |Psi-> = singlet, |Psi+> = |1,0> triplet, |Phi+/-> = (|1,1> +/- |1,-1>)/sqrt(2). (from operator_algebras_and_representation.md)

## su(4) Structure and Cartan Subalgebra
su(4) has 15 generators: 3 local on A (sigma_i tensor I), 3 local on B (I tensor sigma_j), 9 nonlocal (sigma_i tensor sigma_j). The local subalgebra su(2)_A (+) su(2)_B is Type I+II. The Cartan decomposition su(4) = k + p has k = local subalgebra (dim 6) and p = nonlocal (dim 9), with [p,p] subset k. The Killing form K(X,Y) = 2n Tr(XY) for su(n) provides the natural metric on Hamiltonian parameter space. (from operator_algebras_and_representation.md, cartan_decomposition_2qubit.md)

## Casimir Operators and Entanglement Witness
J^2_total = J_A^2 + J_B^2 + 2 J_A.J_B. For two qubits: J_A.J_B = (J^2_total - 3/2)/2. Singlet: J_A.J_B = -3/4 (maximally anti-correlated, maximally entangled). Triplet: J_A.J_B = 1/4. The expectation value of J_A.J_B is thus an entanglement witness. The total spin Casimir eigenvalue c_2 = 0 on singlet, 2 on triplet. (from operator_algebras_and_representation.md)

## Jordan Algebra and Operator Product Decomposition
The Jordan product A o B = (AB+BA)/2 is commutative and produces Hermitian results. The full operator product splits: AB = (A o B) + (1/2)[A,B]. The Jordan part governs measurement statistics (<A o B> = Re(<AB>)), the Lie bracket governs dynamics (d/dt A = (i/hbar)[H,A]). The JBW algebra of density matrices under the Jordan product has the state space as its positive cone. Spectral theory in Jordan algebras uses orthogonal idempotents (e_i o e_j = delta_{ij} e_i). (from operator_algebras_and_representation.md)

## Schur-Weyl Duality and Tensor Networks
(C^d)^{(x)n} = sum_lambda V_lambda (x) S_lambda where lambda ranges over Young diagrams. Permutation-invariant states live in the symmetric subspace (dimension n+1 for n qubits). MPS: chain of tensors, bond dimension = Schmidt rank across each cut. The Pauli transfer matrix representation M = sum m_{mu nu}(sigma_mu tensor sigma_nu)/4 with m_{mu nu} = Tr(M sigma_mu tensor sigma_nu) is fundamental to quantum process tomography. (from operator_algebras_and_representation.md)

## Related pages
- [[fiber-bundles-and-spin-geometry]]
- [[cartan-decomposition-2qubit]]
- [[density-matrix-mathematics]]
- [[schmidt-decomposition-bipartite]]
- [[clifford-algebra-qit]]
- [[berry-phase-and-holonomy]]
- [[entanglement-theory]]
