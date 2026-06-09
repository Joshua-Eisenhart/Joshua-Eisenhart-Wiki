---
title: Classical vs Quantum Compression
created: 2026-04-07
updated: 2026-04-13
type: comparison
framing: current
tags: [comparison, research, validation, reference]
sources:
  - raw/articles/new-docs/new content/compression_math_density_matrix.md
  - raw/articles/new-docs/02_compression_to_density_matrix_map.md
  - raw/articles/new-docs/new content/quantum_computing_applications.md
---

# Classical vs Quantum Compression

## What is being compared
This page compares the classical rate-distortion/PCA picture with the quantum rate-distortion/Schumacher picture.

## Comparison
| Dimension | Classical compression | Quantum compression |
|---|---|---|
| Carrier | probability distribution / covariance | density matrix |
| Optimal structure | reverse water-filling / low-rank covariance truncation | typical subspace / spectral truncation |
| Distortion | average reconstruction loss | fidelity / entanglement fidelity |
| Information measure | Shannon entropy, mutual information | von Neumann entropy, coherent information |
| Exactness | exact for classical source models | exact for quantum source models |

## Synthesis
Both families reduce to spectral retention on a carrier. The difference is which carrier is admissible and which distortion witness is used.

The thread-level correction is that the classical side should not be treated as outside the larger system. Classical/numpy realizations are baseline occupants of the same wider manifold and serve as comparison/control surfaces for richer QIT or constraint-stack realizations of the same bounded object when such twin realizations exist. See [[support-first-constraint-manifold-dependency-chain]].

## Related pages
- [[compression-mathematics-and-density-matrix]]
- [[compression-to-density-matrix-map]]
- [[quantum-computing-applications]]
- [[pca-qpca-density-matrix-view]]
