---
title: Schmidt Decomposition Bipartite
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, geometry, research, validation]
sources:
  - raw/articles/new-docs/new content/schmidt_decomposition_bipartite.md
  - raw/articles/new-docs/new content/entanglement_theory.md
  - raw/articles/new-docs/new content/density_matrix_mathematics.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Schmidt Decomposition Bipartite

## Overview
This page covers the Schmidt decomposition, Schmidt rank, operator Schmidt structure, and Schmidt number for mixed states.

## Main points
- Every bipartite pure state decomposes into orthonormal pairs with unique coefficients.
- Schmidt rank is a direct entanglement witness for pure states.
- Reduced density matrices share the same nonzero eigenvalues as the Schmidt coefficients squared.
- The decomposition ties directly to SVD and entanglement entropy.

## Why it matters
This is the clean bipartite entanglement primitive that connects density matrices to tensor structure.

## Construction via SVD
Expand |psi>=sum C_{jk}|j>|k>. The SVD C=U Sigma V* gives Schmidt coefficients alpha_i=sigma_i, Schmidt bases |i_A>=sum U_{ji}|j>, |i_B>=sum V_{ki}*|k>. Schmidt rank = rank(C) = number of nonzero singular values. For 2-qubit |psi>=a|00>+b|01>+c|10>+d|11>, concurrence C=2|det C|=2 alpha_1 alpha_2, parametrized as sin(2 theta) with theta in [0,pi/4]. Entanglement entropy S=H_2(cos^2 theta) monotonically increases from 0 to log 2. (from schmidt_decomposition_bipartite.md)

## Entanglement from Schmidt Coefficients
rho_A = Tr_B(|psi><psi|) = sum alpha_i^2|i_A><i_A|, so Schmidt coefficients squared are the eigenvalues of the reduced state. rho_A = CC* and rho_B = C*C share the same nonzero eigenvalues. Von Neumann entanglement entropy S = -sum alpha_i^2 log(alpha_i^2). Renyi versions: S_0=log(Schmidt rank), S_2=-log(sum alpha_i^4)=-log(purity), S_inf=-log(alpha_max^2). Bounds: 0<=S<=log(min(m,n)). LOCC convertibility: alpha^2(psi)<|alpha^2(phi) iff |psi>->|phi> by LOCC. (from schmidt_decomposition_bipartite.md)

## Operator-Schmidt Decomposition
Any operator M on H_A tensor H_B decomposes as M = sum s_i A_i tensor B_i with orthonormal {A_i},{B_i} under Hilbert-Schmidt inner product. For 2-qubit density matrices, the operator-Schmidt coefficients come from SVD of the correlation tensor T_{ij}. Operator-Schmidt rank = 1 iff product operator; for unitary gates, it relates to entangling power. (from schmidt_decomposition_bipartite.md)

## Schmidt Number for Mixed States
SN(rho) = min_decompositions max_{|psi_k>} (Schmidt rank of |psi_k>) (Terhal-Horodecki). SN=1 iff separable. Schmidt-number-k witnesses W satisfy Tr(W sigma)>=0 for all sigma with SN<=k but Tr(W rho)<0 for some rho with SN>k. The Schmidt number quantifies "effective dimensionality" of entanglement. SN is an entanglement monotone non-increasing under LOCC. (from schmidt_decomposition_bipartite.md)

## Multi-Party Generalization and MPS
No Schmidt decomposition exists for 3+ parties (counterexample: W state). SLOCC classification replaces it: 6 classes for 3 qubits (Dur-Vidal-Cirac). Computing tensor rank is NP-hard. Truncated Schmidt decomposition keeps top-k coefficients, error D<=2sqrt(1-sum_{i=1}^k alpha_i^2). Repeated Schmidt decompositions across bipartitions give Matrix Product States with bond dimension chi = max Schmidt rank -- the most efficient representation for bounded-entanglement states. (from schmidt_decomposition_bipartite.md)

## Related pages
- [[entanglement-theory]]
- [[density-matrix-mathematics]]
- [[svd-and-low-rank-approximation]]
- [[quantum-information-measures]]
- [[spectral-decomposition-theory]]
- [[quantum-computing-applications]]
