---
title: PCA QPCA Alignment
created: 2026-04-07
updated: 2026-04-08
type: summary
framing: current
tags: [reference, research, validation]
sources:
  - raw/articles/new-docs/01_pca_qpca_alignment.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# PCA, Quantum PCA, and the Density-Matrix View

## Overview
A large class of compression methods can be expressed as selecting dominant modes of a matrix or operator. In this system, those operators are naturally represented as density matrices, correlation matrices, or covariance operators. This page maps the shared structure.

## Classical PCA

PCA is a linear method: center the data, compute covariance matrix, diagonalize, keep eigenvectors with largest eigenvalues. Eigenvectors = principal directions. Eigenvalues = variance carried by each direction. Truncation to top-k components = compression.

## Quantum PCA

QPCA is the quantum-algorithm version: quantum-access model for a density operator, extraction of dominant eigenvalues/eigenvectors or principal subspaces, phase-estimation-style readout. Important caveat: QPCA depends on strong state-preparation and access assumptions; speedups are tied to those assumptions.

## Density-Matrix Translation

In this system, compression should be rewritten as: spectral truncation of a density matrix, low-rank approximation of a correlation tensor, Schmidt-mode truncation of a bipartite state, or projection onto the dominant eigenspace. This gives physically meaningful representation: trace 1 preserved, positivity enforced, principal modes interpretable.

## Natural Equivalences

- PCA to covariance eigendecomposition
- SVD to low-rank factorization
- Schmidt decomposition to bipartite PCA of a pure state
- QPCA to quantum-access spectral extraction
- entanglement spectrum to spectral compression of joint states
- coarse-graining to projection onto dominant modes

## System Implication
If a proposed compression method can be rewritten as a dominant-subspace operator, it is likely admissible in the system math. If it cannot be phrased in spectral/operator language, it is probably only a heuristic wrapper.

## How it connects
This feeds into [[compression-to-density-matrix-map]] and [[system-math-alignment]]. See [[quantum-information-measures]] for the information-theoretic framing and [[pca-qpca-density-matrix-view]] for the structural view.

## Open questions
- Whether QPCA's speedup assumptions can be relaxed for the system's use case.
- Whether the equivalence between PCA/SVD/Schmidt is exact or approximate in the system's carrier.
