---
title: Research Index Compression Terms
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, compression]
sources:
  - raw/articles/new-docs/05_research_index.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Research Index: Compression Terms

## Overview
Searchable research index for compression and spectral terms used in the system. Maps each term to its role in the density-matrix / operator framework.

## Key Terms and Their Density-Matrix Roles

### SVD (Singular Value Decomposition)
Factorizes a matrix into U * Sigma * V^dagger. In the system: low-rank factorization of a correlation operator. Basis for PCA, Schmidt decomposition, and spectral truncation.

### PCA / Quantum PCA
Classical: eigendecomposition of covariance matrix, keep top-k. Quantum: phase-estimation-style spectral extraction from density operator. See [[pca-qpca-alignment]].

### Schmidt Decomposition
Bipartite factorization of a pure state: |psi> = sum_k sqrt(lambda_k) |a_k> |b_k>. In the system: bipartite PCA of a pure joint state. Schmidt coefficients = entanglement spectrum.

### Spectral Truncation
Keeping only the dominant eigenmodes of an operator. In the system: compression of density matrices or covariance operators. The retained subspace is the "principal" structure.

### Low-Rank Approximation
Approximating a matrix/operator by one with fewer non-zero singular values. In the system: controlled information loss. The rank-k approximation preserves the k most distinguishable modes.

### Coarse-Graining
Collapsing fine-grained states into fewer observed classes. In the system: projection onto a subalgebra of observables. Reduces distinguishability. Connected to [[constraint-on-distinguishability-formal-reference]].

### Quantum Fisher Information
Measures sensitivity of a quantum state to parameter changes. Related to the Fubini-Study metric on pure-state space. In the system: part of the admissible geometry family.

### Entanglement Spectrum
Schmidt coefficients of a bipartite pure state. In the system: spectral structure of the joint state rho_AB. See [[constraint-on-distinguishability-full-math]] for how it connects to entropy.

## Related pages
- [[pca-qpca-alignment]]
- [[cross-domain-equivalence-map]]
- [[compression-math-density-matrix]]
- [[constraint-on-distinguishability-full-math]]
