---
title: Compression To Density Matrix Map
created: 2026-04-07
updated: 2026-04-08
type: summary
framing: archived_source_snapshot
tags: [reference, research, validation]
sources:
  - raw/articles/new-docs/02_compression_to_density_matrix_map.md
---

Archived source-bundle snapshot. Any current/canonical/proven language here is
a source-bundle label, not current repo proof, maturity, or promotion.

# Compression Mathematics to Density-Matrix Map

## Overview
Canonical mapping from compression families to density-matrix form. This is the translation table: what each compression method looks like when rewritten in the system's native operator language.

## Canonical Mapping

| Compression family | Density-matrix form |
|---|---|
| PCA | spectral decomposition of covariance |
| QPCA | dominant eigenmodes of operator |
| SVD | operator low-rank factorization |
| Schmidt decomposition | singular modes of bipartite amplitude |
| low-rank approximation | PSD low-rank approximation |
| spectral truncation | eigenvalue thresholding |
| coarse-graining | projection to reduced operator algebra |
| entanglement compression | truncation in Schmidt basis |

## Safe Compression Pattern

A compression method is system-compatible when it can be written as: (1) build operator, (2) diagonalize or factorize, (3) keep leading modes, (4) reconstruct valid density operator, (5) renormalize and enforce positivity.

## Geometry-Friendly Operators

Most natural compression within the geometry stack: covariance operator of Bloch/correlation data, joint density matrix of two subsystems, correlation tensor C_ij, entanglement spectrum, reduced density matrices from partial traces.

## What to Avoid

- Compression with no spectral interpretation
- Lossy transforms that break positivity or trace normalization
- Ad hoc coordinates that cannot be mapped back to observables

## Rule of Thumb
If the compression target can be represented as a principal subspace, Schmidt basis, or low-rank density operator, then it belongs in this system.

## How it connects
This is the practical translation layer for [[01-pca-qpca-alignment]] and [[system-math-alignment]]. See [[mass-equivalence-engine]] for the deeper equivalence classes.

## Open questions
- Whether entanglement compression should be treated as a separate family or a special case of Schmidt truncation.
