---
title: SVD and Low Rank Approximation
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, geometry, research, architecture]
sources:
  - raw/articles/new-docs/new content/svd_and_low_rank_approximation.md
  - raw/articles/new-docs/new content/schmidt_decomposition_bipartite.md
  - raw/articles/new-docs/new content/density_matrix_mathematics.md
framing: mixed
---

# SVD and Low Rank Approximation

## Overview
This page covers singular value decomposition, matrix norms, Eckart-Young truncation, low-rank density-matrix approximation, and correlation-tensor SVD.

## Main points
- SVD is the universal factorization for matrices.
- Truncated SVD gives the best low-rank approximation in standard norms.
- Density matrices inherit spectral truncation logic, but trace-one constraints require care.
- Correlation tensors for two-qubit states can be analyzed by SVD.

## Why it matters
This is the numerical and compression-side companion to the density-matrix and Schmidt pages.

## Schatten Norms and Trace Distance
The Schatten p-norms ||A||_p = (sum sigma_i^p)^{1/p} unify operator norm (p=inf), Frobenius (p=2), and nuclear/trace norm (p=1). For density matrices: ||rho||_1=1 always, ||rho||_F=sqrt(purity), ||rho||_op=lambda_max. Trace distance D(rho,sigma)=(1/2)||rho-sigma||_1 uses eigenvalues of the Hermitian difference. The dual relationship ||A||_* = max_{||B||_op<=1}|Tr(B*A)| connects nuclear and operator norms. (from svd_and_low_rank_approximation.md)

## Eckart-Young and Density Matrix Truncation
The best rank-k approximation is the truncated SVD A_k = sum_{i=1}^k sigma_i|u_i><v_i| in both operator and Frobenius norms. For density matrices, naive truncation rho_k^raw = sum_{i=1}^k lambda_i|i><i| loses trace. Trace renormalization rho_k = rho_k^raw/Tr(rho_k^raw) gives a valid density matrix but not the trace-distance optimum. The Ky Fan solution keeps top k-1 eigenvalues and lumps remaining probability into the k-th: D(rho,sigma_opt) = sum_{i=k+1}^r lambda_i. (from svd_and_low_rank_approximation.md)

## Correlation Tensor SVD and Bell-Diagonal States
For 2-qubit states, T=O_1 diag(t_1,t_2,t_3) O_2^T where O_1,O_2 encode local unitary freedom. Bell-diagonal states (a=b=0) have eigenvalues lambda_i = (1 +/- t_1 +/- t_2 +/- t_3)/4 forming a tetrahedron in (t_1,t_2,t_3) space. Separability: |t_1|+|t_2|+|t_3|<=1 (inscribed octahedron). The PPT criterion flips t_2's sign. Realignment criterion ||R(rho)||_1>1 implies entanglement via singular values of the realignment map. (from svd_and_low_rank_approximation.md)

## Nuclear Norm and Quantum Tomography
Nuclear norm minimization min||X||_* s.t. Tr(M_i X)=m_i, X>=0 is the convex relaxation of rank minimization for state tomography. The nuclear norm penalty encourages low-rank solutions since physical density matrices are often approximately low-rank. Choi matrix rank equals Kraus rank (number of nonzero eigenvalues of J(E)). Randomized SVD achieves O(n^2(k+p)) cost instead of O(n^3) for large density matrices -- enabling efficient tomography when rho is approximately rank-k. (from svd_and_low_rank_approximation.md)

## SVD as Unifying Framework
SVD connects: Schmidt decomposition (SVD of coefficient matrix C), reduced density matrices (rho_A=CC*, rho_B=C*C), entanglement measures (functions of singular values), low-rank approximation (truncated SVD = MPS truncation), and channel decomposition (SVD of Choi matrix -> Kraus operators). Key chain: singular values of C = Schmidt coefficients alpha_i; alpha_i^2 = eigenvalues of rho_A; S(rho_A) = H(alpha^2); rank(C) = Schmidt rank = entanglement dimensionality. (from svd_and_low_rank_approximation.md)

## Related pages
- [[density-matrix-mathematics]]
- [[schmidt-decomposition-bipartite]]
- [[compression-to-density-matrix-map]]
- [[pca-qpca-density-matrix-view]]
- [[spectral-decomposition-theory]]
- [[quantum-information-measures]]
- [[distance-metrics-state-space]]
