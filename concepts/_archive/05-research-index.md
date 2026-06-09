---
title: Research Index
created: 2026-04-07
updated: 2026-04-08
type: summary
framing: current
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/05_research_index.md
---

# Research Index — Compression and Systems Math

## Overview
Searchable index linking the research terms that now belong in the systems-math layer. All of these express the same basic move: find dominant modes of an operator, keep the strongest modes, compress the rest.

## Core Terms

- Principal component analysis (PCA)
- Quantum principal component analysis (QPCA)
- Singular value decomposition (SVD)
- Schmidt decomposition
- covariance matrix / covariance operator
- density matrix / density operator
- low-rank approximation
- entanglement spectrum
- principal subspace

## What This Means for the Engine

The engine already supports the operator vocabulary needed for this family: partial traces, correlation tensors, joint density matrices, spectral checks, entanglement measures, graph/topology gates. The research question is not whether compression mathematics belongs here. The question is which spectral form best matches the runtime object.

## Current Best Alignment

- PCA for classical covariance structure
- QPCA for quantum-access spectral extraction
- Schmidt decomposition for bipartite pure states
- low-rank density operators for mixed-state compression

## Promotion Rule

A new compression method belongs here if it can be stated as a principal-subspace / spectral-truncation / low-rank operator problem.

## How it connects
This index points to [[01-pca-qpca-alignment]], [[02-compression-to-density-matrix-map]], [[04-system-math-alignment]], and [[compression-mathematics-and-density-matrix]].

## Open questions
- Whether "best matches the runtime object" should be determined by sim or by theoretical alignment.
