---
title: PCA, QPCA, and the Density-Matrix View
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [research, simulation, validation, architecture]
sources:
  - raw/articles/new-docs/01_pca_qpca_alignment.md
  - raw/articles/new-docs/02_compression_to_density_matrix_map.md
  - raw/articles/new-docs/03_source_notes.md
framing: mixed
---

# PCA, QPCA, and the Density-Matrix View

## Overview
This page captures the shared spectral idea behind PCA, QPCA, SVD, Schmidt decomposition, and low-rank operator approximations.

## Main points
- PCA keeps dominant covariance eigenmodes.
- QPCA is the operator/density-matrix analogue under quantum-access assumptions.
- Compression in this stack should usually be rewritten as dominant-subspace retention, low-rank factorization, or spectral truncation.
- Eigenvalue-only views are useful but lossy; they can miss phase and noncommutation.

## Why it matters
This is the bridge from classical compression to the density-operator language used throughout the wiki.

## Related pages
- [[compression-to-density-matrix-map]]
- [[state-representation-views]]
- [[system-math-alignment]]
- [[mass-equivalence-engine]]
- [[density-matrices-across-fields]]
- [[spectral-decomposition-theory]]
- [[compression-mathematics-and-density-matrix]]
- [[research-index]]
- [[pca-qpca-alignment]]
