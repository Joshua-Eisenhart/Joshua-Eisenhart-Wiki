---
title: CPTP Maps and Quantum Channels
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, architecture, research, validation]
sources:
  - raw/articles/new-docs/new content/cptp_maps_and_channels.md
  - raw/articles/new-docs/new content/density_matrix_mathematics.md
  - raw/articles/new-docs/references/DISTINGUISHABILITY_FORMAL_REFERENCE.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# CPTP Maps and Quantum Channels

## Overview
This page gathers the formalism of quantum channels: complete positivity, Kraus forms, Stinespring dilation, Choi duality, and Lindblad evolution.

## Main points
- Physical channels must be completely positive and trace preserving.
- Kraus representations and Stinespring dilations are equivalent pictures.
- The Choi matrix turns channel questions into state questions.
- Lindblad/GKSL form governs Markovian open-system dynamics.

## Why it matters
This is the channel-level counterpart to density matrices and distinguishability monotonicity.

## Kraus Representation and Stinespring Dilation
Every CPTP map E(rho) = sum A_k rho A_k^dagger with sum A_k^dagger A_k = I has minimal Kraus rank equal to the Choi rank (1 to d^2). Kraus representations are non-unique: sets {A_k} and {B_l} define the same channel iff related by a unitary mixing matrix. Stinespring dilation expresses E(rho) = Tr_E(V rho V^dagger) where V is an isometry into system+environment. The complementary channel E^c(rho) = Tr_B(V rho V^dagger) captures information leakage. Channels are degradable (environment can simulate from output) or anti-degradable (output from environment); most are neither. (from cptp_maps_and_channels.md)

## Choi-Jamiolkowski Isomorphism
The Choi matrix J(E) = (E tensor id)(|Omega><Omega|) establishes a bijection: E is CP iff J(E)>=0, TP iff Tr_B(J(E))=I_A, unital iff Tr_A(J(E))=I_B. The channel-state duality means studying quantum channels IS studying certain bipartite density matrices. The rank of J(E) equals the minimum number of Kraus operators. Recovery: E(rho) = d_A Tr_A((rho^T tensor I_B) J(E)). For unitary channels, J is rank-1. (from cptp_maps_and_channels.md)

## Lindblad/GKSL Master Equation
The most general Markovian evolution is d rho/dt = -i[H,rho] + sum gamma_k(L_k rho L_k^dagger - (1/2){L_k^dagger L_k, rho}). The GKSL theorem (1976) characterizes generators of quantum dynamical semigroups. For qubits, T1 decay uses L=sqrt(gamma)sigma_-, T2 dephasing uses L=sqrt(gamma_phi)sigma_z/2, with 1/T2 = 1/(2T1)+1/T_phi. Vectorizing rho gives a d^2-dimensional Liouvillian superoperator L_super whose eigenvalues determine the relaxation spectrum. (from cptp_maps_and_channels.md)

## Affine Bloch Map and Qubit Channel Classification
Any qubit CPTP map acts on the Bloch vector as r -> Mr + t, where M is 3x3 and t is a translation. Unital channels (t=0) map the Bloch ball to an ellipsoid centered at the origin. Pauli channels have M=diag(lambda_1,lambda_2,lambda_3) with the CP constraint that (lambda_1,lambda_2,lambda_3) lies in a tetrahedron. Amplitude damping has M=diag(sqrt(1-gamma),sqrt(1-gamma),1-gamma) and t=(0,0,gamma), compressing and shifting the ball toward |0>. (from cptp_maps_and_channels.md)

## Channel Capacities
Classical capacity C(N) uses Holevo information; quantum capacity Q(N) uses coherent information I_c = S(B)-S(AB). For degradable channels both are single-letter. Entanglement-assisted capacity C_E is always additive. Q can be superadditive: two channels with Q=0 individually can jointly have Q>0 (superactivation, Cubitt et al. 2015). Channel twirling (Haar averaging) converts any channel to depolarizing form; Pauli twirling converts to Pauli channels, practical for error characterization. (from cptp_maps_and_channels.md)

## Related pages
- [[density-matrix-mathematics]]
- [[distinguishability-formal-reference]]
- [[quantum-information-measures]]
- [[stochastic-thermodynamics-reference]]
- [[quantum-computing-applications]]
- [[quantum-fisher-information-geometry]]
- [[entanglement-theory]]
- [[distance-metrics-state-space]]
