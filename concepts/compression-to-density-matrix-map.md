---
title: Compression Mathematics to Density-Matrix Map
created: 2026-04-07
updated: 2026-04-15
type: concept
tags: [simulation, validation, research, architecture]
sources:
  - raw/articles/new-docs/02_compression_to_density_matrix_map.md
  - raw/articles/new-docs/05_research_index.md
  - raw/articles/new-docs/08_aligned_sim_backlog_and_build_order.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Compression Mathematics to Density-Matrix Map

## Role in the live wiki cluster
- Strongest use: compact concept/router for the compression-family mapping lane when a reader needs the admissible spectral/operator rewrite pattern in one page.
- Weak use: front-door explanation of compression doctrine, or substitute for the cleaner current summary and adjacent broader concept pages.
- Authority boundary: this page is a bounded mapping surface for compression methods that survive translation into density-matrix/operator language; it does not outrank [[pca-qpca-alignment]] as the cleaner current summary, [[pca-qpca-density-matrix-view]] as the broader public concept surface, or repo-current controller docs for live truth/process claims.

## Recommended reading order
1. `hermes-current/read-first.md` and the rest of the `hermes-current/` spine for general entry behavior.
2. `projects/codex-ratchet/read-first.md` when the task is repo-bound.
3. [[pca-qpca-alignment]] for the cleaner current summary of the spectral-compression equivalence.
4. [[pca-qpca-density-matrix-view]] for the broader public concept framing.
5. this page when the question is specifically which compression families belong in the density-matrix/operator rewrite lane and what the safe inclusion rule is.

## Overview
This page captures the family of compression methods that can be expressed as operator or density-matrix problems.

## Canonical mapping
- PCA → covariance spectral decomposition
- QPCA → dominant modes of an operator or density object
- SVD → factorization into leading singular modes
- Schmidt decomposition → bipartite factorization
- Low-rank approximation → dominant spectrum retention
- Spectral truncation → eigenvalue thresholding

## Safe compression pattern
A method belongs here when it can be written as:
1. build operator
2. diagonalize or factorize
3. keep leading modes
4. reconstruct a valid density operator
5. renormalize and preserve positivity

## Guardrails
- Avoid ad hoc transforms with no spectral interpretation
- Avoid lossy reductions that break positivity or trace normalization
- Prefer principal-subspace or Schmidt-basis formulations

## Related pages
- [[mass-equivalence-engine]]
- [[constraint-on-distinguishability]]
- [[aligned-sim-backlog-and-build-order]]
- [[state-representation-views]]
- [[entropy-and-information-families]]
- [[pca-qpca-density-matrix-view]]
- [[system-math-alignment]]
- [[compression-mathematics-and-density-matrix]]
- [[new-docs-manifest]]
- [[research-index-compression-terms]]
- [[research-index]]
- [[pca-qpca-alignment]]
