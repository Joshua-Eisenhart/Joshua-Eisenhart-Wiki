---
title: Source Notes Index
created: 2026-04-07
updated: 2026-04-08
type: summary
framing: current
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/03_source_notes.md
---

# Source Notes

## Overview
Source-derived anchors used for the research synthesis. These are the provenance notes for PCA, QPCA, and related spectral math. Not canonical themselves, but feed the canonical numbered docs.

## PCA Sources

Wikipedia: PCA is a linear dimensionality-reduction method. It finds orthogonal directions of maximal variance. Principal directions are eigenvectors of the covariance matrix. Corresponding eigenvalues measure variance along those directions.

## Quantum PCA Sources

arXiv search for "quantum principal component analysis Lloyd":
- classic paper: arXiv:1307.0401 — Lloyd, Mohseni, Rebentrost
- arXiv:1903.03999 — Improved Algorithm for QPCA
- arXiv:1811.00414 — QPCA only achieves exponential speedup because of state preparation assumptions
- arXiv:2104.02476 — Resonant QPCA

## Alignment Takeaway

The central shared structure is spectral extraction: covariance eigenvectors in PCA, principal subspaces in QPCA, Schmidt modes in bipartite states, low-rank truncation in density-matrix compression.

## Status

- source-note: yes
- canonical: no
- use for doc synthesis: yes
- use for runtime implementation directly: no

## How it connects
These sources feed [[01-pca-qpca-alignment]], [[02-compression-to-density-matrix-map]], and [[research-index]]. See [[source-notes]] for the broader provenance catalog.

## Open questions
- Whether additional QPCA papers beyond the Lloyd et al. cluster should be incorporated.
