---
title: Pca Qpca Alignment
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, compression, quantum]
sources:
  - raw/articles/new-docs/01_pca_qpca_alignment.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# PCA, Quantum PCA, and the Density-Matrix View

## Overview
A large class of compression methods can be expressed as selecting dominant modes of a matrix or operator. In this system, those operators are naturally represented as density matrices, correlation matrices, or covariance operators.

## Classical PCA
Principal component analysis: centers data, computes covariance matrix, diagonalizes, keeps eigenvectors with largest eigenvalues. Eigenvectors = principal directions. Eigenvalues = variance per direction. Top-k truncation = compression.

## Quantum PCA
QPCA is the quantum-algorithm version of the same spectral idea: quantum-access model for a density operator, extraction of dominant eigenvalues/eigenvectors or principal subspaces, phase-estimation-style readout. Important caveat: not a generic magic replacement for PCA. Depends on strong state-preparation and access assumptions.

## Density-Matrix Translation
In this system, compression should usually be rewritten as: spectral truncation of a density matrix, low-rank approximation of a correlation tensor, Schmidt-mode truncation of a bipartite state, projection onto dominant eigenspace of a covariance operator. This gives physically meaningful representation: trace 1 preserved, positivity enforced, principal modes interpretable.

## Natural Equivalences
- PCA <-> covariance eigendecomposition
- SVD <-> low-rank factorization
- Schmidt decomposition <-> bipartite PCA of a pure state
- QPCA <-> quantum-access spectral extraction
- entanglement spectrum <-> spectral compression of joint states
- coarse-graining <-> projection onto dominant modes

## System Implication
If a proposed compression method can be rewritten as a dominant-subspace operator, it is likely admissible in the system math. If it cannot be phrased in spectral/operator language, it is probably only a heuristic wrapper. See [[cross-domain-equivalence-map]] for the broader equivalence context.

## Related pages
- [[cross-domain-equivalence-map]]
- [[compression-math-density-matrix]]
- [[research-index-compression-terms]]
- [[model-math-geometry-sim-plan]]
