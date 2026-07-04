---
title: Compression Math Density Matrix
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, compression, quantum, mathematics]
sources:
  - raw/articles/new-docs/new content/compression_math_density_matrix.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Compression Mathematics and the Density Matrix

## Overview
Mathematical structures connecting data compression, dimensionality reduction, and density matrix formalism. Every section provides explicit formulas and identifies where the density matrix structure is exact versus approximate.

## Central Thesis
Compression = low-rank approximation of a density matrix. rho -> rho_k = sum_{i=1}^k lambda_i |e_i><e_i| (top-k eigenstates). Information retained: Tr(rho_k). Information lost: 1 - Tr(rho_k). The optimal k-rank approximation (Eckart-Young theorem) is spectral truncation. All of rate-distortion theory, PCA, tensor networks, and compressed sensing are variations on this theme.

## Classical Rate-Distortion Theory
Shannon's R(D) = min I(X; X_hat) subject to E[d(X, X_hat)] <= D. R(0) = H(X) for discrete sources. R(D_max) = 0. R(D) is convex, non-increasing.

## Rate-Distortion as Density Matrix Optimization
Embed source as diagonal density matrix rho_X. Encoding channel is CPTP map E. R(D) = min I(rho_X, E) subject to distortion constraint. For Gaussian sources: R(D) = (1/2) log(sigma^2/D). Optimal encoding: project onto top eigenspace until residual variance equals D (reverse water-filling).

## SVD Connection
SVD is the matrix analog of spectral decomposition. A = U Sigma V^dagger. Truncation to top-k singular values = optimal low-rank approximation. In density matrix terms: rho = U Lambda U^dagger, keep top-k eigenvalues.

## System Relevance
See [[pca-qpca-alignment]] for PCA/QPCA correspondence and [[cross-domain-equivalence-map]] for the broader equivalence picture.

## Quantum Rate-Distortion Theory
R_q(D) = min_{E: CPTP, E_d(rho,E(rho))<=D} I_c(rho,E) where I_c = S(E(rho))-S(rho,E) is coherent information. Devetak-Berger (2005): R_q(D) = min_{E: F_e>=1-D} [S(rho)-S(rho,E)]. For diagonal rho (classical embedded), R_q = R_classical. For entangled sources, R_q(D) < R_classical(D) -- quantum compression is more efficient. The quantum rate-distortion function uses coherent information rather than mutual information. (from compression_math_density_matrix.md)

## Schumacher Compression and PCA Connection
Schumacher (1995): n copies of rho compress to n S(rho) qubits via projection onto the typical subspace (eigenvalues close to average spectrum). PCA keeps top-k eigenvectors of the covariance matrix = projecting rho=Sigma/Tr(Sigma) onto the rank-k subspace maximizing retained trace. The "rate" is log k, the "distortion" is 1-sum_{i=1}^k lambda_i/Tr(Sigma). Reverse water-filling for Gaussian sources: R(D)=sum max(0,(1/2)log(lambda_i/theta)) where theta chosen so residual variance=D. (from compression_math_density_matrix.md)

## Entanglement-Assisted Compression and Superadditivity
For entangled encoder-decoder pairs, quantum rate-distortion improves beyond classical. The coherent information I_c = S(B)-S(AB) replaces mutual information. Superadditivity: Q(E tensor E') > 2Q(E) possible. This has no classical analog. The lossy compression = entropy-constrained quantization: assign codewords based on spectral structure of rho, codebook = rank-1 projectors (pure states), encoding = CPTP map from rho to low-rank approximation. (from compression_math_density_matrix.md)

## Related pages
- [[pca-qpca-alignment]]
- [[cross-domain-equivalence-map]]
- [[research-index-compression-terms]]
- [[density-matrix-mathematics]]
- [[quantum-information-measures]]
- [[svd-and-low-rank-approximation]]
