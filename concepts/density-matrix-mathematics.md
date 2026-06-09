---
title: Density Matrix Mathematics
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, geometry, research, architecture]
sources:
  - raw/articles/new-docs/new content/density_matrix_mathematics.md
  - raw/articles/new-docs/new content/compression_math_density_matrix.md
  - raw/articles/new-docs/02_compression_to_density_matrix_map.md
framing: mixed
---

# Density Matrix Mathematics

## Overview
This page collects the formal structure of density matrices, spectral decomposition, Bloch-ball geometry, two-qubit correlation tensors, and purification.

## Formal Definition
A density matrix rho on Hilbert space H of dimension d is a linear operator satisfying three conditions: Hermiticity (rho = rho^dagger), positivity (all eigenvalues >= 0), and unit trace (Tr(rho) = 1). The set D(C^d) of all density matrices forms a convex body of real dimension d^2 - 1. Pure states are rank-1 projectors satisfying rho^2 = rho — these are the extreme points. Mixed states satisfy rho^2 =/= rho, equivalently Tr(rho^2) < 1. (from density_matrix_mathematics.md)

## Purity and Entropy
Purity gamma = Tr(rho^2) ranges from 1/d (maximally mixed) to 1 (pure). For single qubits, purity relates to the Bloch vector: Tr(rho^2) = (1 + |r|^2)/2. Von Neumann entropy S(rho) = -Tr(rho log rho) is the canonical entropy measure — zero for pure states, maximal for maximally mixed states. (from density_matrix_mathematics.md)

## Bloch Ball Geometry (Single Qubit)
Any 2x2 density matrix decomposes as rho = (I + r.sigma)/2 where r in R^3 is the Bloch vector and sigma are the [[formal-constraints-and-geometry|Pauli matrices]]. The Bloch ball B^3 = {|r| <= 1} is the complete state space: surface (|r|=1) for pure states, interior for mixed states, center (r=0) for maximally mixed. Eigenvalues are lambda_pm = (1 +/- |r|)/2. (from density_matrix_mathematics.md)

## Two-Qubit Structure (C^4)
General 2-qubit density matrices decompose in the Pauli product basis: rho = (1/4)(I_4 + a.sigma tensor I + I tensor b.sigma + sum T_{ij} sigma_i tensor sigma_j). This gives 15 real parameters (3+3+9 with trace constraint). The correlation tensor T captures all correlations between subsystems; its SVD determines canonical forms via local unitary equivalence. (from density_matrix_mathematics.md)

## Quantum Steering Ellipsoid
For 2-qubit states, the set of Bloch vectors Bob's qubit can be steered to by Alice's measurements forms an ellipsoid in Bob's Bloch ball (Jevtic, Pusey, Rudolph, Jennings 2014). Entanglement increases ellipsoid volume — maximal for [[entanglement-theory|Bell states]] where the ellipsoid fills the entire Bloch sphere. This connects to [[quantum-information-measures]] via steering-based entanglement criteria. (from density_matrix_mathematics.md)

## Purification Theorem
Every mixed state rho_A can be realized as the partial trace of a pure state on a larger system. Given spectral decomposition rho_A = sum lambda_i |a_i><a_i|, purification is |Psi> = sum sqrt(lambda_i) |a_i> tensor |b_i>. Purifications are unique up to unitary freedom on the auxiliary system — a foundational result for [[quantum-information-measures]] and information-disturbance tradeoffs. (from density_matrix_mathematics.md)

## Spectral Decomposition and Functional Calculus
Every density matrix admits rho = sum lambda_i |i><i| where the spectrum (lambda_1, ..., lambda_d) lives in the probability simplex Delta_{d-1}. For C^2, there is one free parameter (lambda_1 in [0,1]); for C^4 (two qubits), three independent eigenvalues. The functional calculus f(rho) = sum f(lambda_i)|i><i| powers all entropy computations: log(rho) for von Neumann entropy, rho^alpha for Renyi entropy, and sqrt(rho) for fidelity. The convention 0 log 0 = 0 (by continuity) handles rank-deficient density matrices. (from density_matrix_mathematics.md)

## Majorization and Unitary Orbits
Two density matrices are unitarily equivalent iff they share the same spectrum. Majorization provides a partial order on spectra: lambda majorizes mu when partial sums of sorted eigenvalues dominate. The maximally mixed state (1/d,...,1/d) is majorized by all others -- it is the "most mixed" state. This partial order underlies Nielsen's theorem for LOCC convertibility of entangled states and Schur's theorem that unital channels always increase mixedness. (from density_matrix_mathematics.md, spectral_decomposition_theory.md)

## Two-Qubit Correlation Tensor and Positivity
A 2-qubit density matrix decomposes as rho = (1/4)(I_4 + a.sigma tensor I + I tensor b.sigma + sum T_{ij} sigma_i tensor sigma_j) with 15 real parameters. The correlation tensor T captures all inter-subsystem correlations. Bell states have a=b=0 and T=diag(+/-1,+/-1,+/-1) with det(T)=-1. Werner states rho_W = (1-p)I/4 + p|Phi+><Phi+| are entangled iff p>1/3 and violate Bell inequality iff p>1/sqrt(2). (from density_matrix_mathematics.md)

## Purification and Unitary Freedom
Every mixed state rho_A = sum lambda_i|a_i><a_i| can be purified as |Psi> = sum sqrt(lambda_i)|a_i>|b_i> on a larger system. Purifications of the same state are related by unitaries on the auxiliary system: |Phi> = (I_A tensor U_B)|Psi>. This unitary freedom in purifications is equivalent to the Hughston-Jozsa-Wootters mixture theorem for decompositions of mixed states. (from density_matrix_mathematics.md)

## Partial Transpose and Entanglement Detection
The partial transpose w.r.t. B swaps indices: rho^{T_B}_{ij,kl} = rho_{ij,lk}. In terms of (a,b,T), partial transpose maps the sigma_y component of T to -T_2. For 2x2 and 2x3 systems, PPT (positive partial transpose) is necessary and sufficient for separability (Peres-Horodecki). In higher dimensions, PPT entangled states ("bound entanglement") exist. (from density_matrix_mathematics.md, entanglement_theory.md)

## Related pages
- [[compression-to-density-matrix-map]]
- [[quantum-information-measures]]
- [[entanglement-theory]]
- [[pca-qpca-density-matrix-view]]
- [[spectral-decomposition-theory]]
- [[schmidt-decomposition-bipartite]]
- [[svd-and-low-rank-approximation]]
- [[quantum-computing-applications]]
- [[density-matrices-across-fields]]
- [[ai-ml-density-matrix-connections]]
- [[clifford-algebra-qit]]
- [[berry-phase-and-holonomy]]
- [[distance-metrics-state-space]]
