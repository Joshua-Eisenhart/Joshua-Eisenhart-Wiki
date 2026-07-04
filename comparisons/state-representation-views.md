---
title: State Representation Views
created: 2026-04-07
updated: 2026-04-07
type: comparison
framing: current
tags: [comparison, validation, research, simulation]
sources:
  - raw/articles/new-docs/11_mass_equivalence_engine.md
  - raw/articles/new-docs/08_aligned_sim_backlog_and_build_order.md
  - raw/articles/new-docs/10_cross_domain_equivalence_map.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# State Representation Views

## What is being compared
Different ways to represent the same underlying state on the L0 carrier.

## Comparison
| View | What it preserves | Main loss mode | Best use |
|---|---|---|---|
| Density matrix | positivity, trace, correlations | can hide basis-specific phase detail | base carrier language |
| Bloch / coherence vector | geometric intuition, operator coordinates | less direct for some mixed-state structure | extensible bridge view |
| Purification | full pure-state structure on larger space | introduces non-uniqueness by environment | exact lifting |
| Spectrum / eigenvalues | mixedness ordering, dominant modes | phase and orientation are lost | compression / ranking |
| Stokes-style coordinates | compact parameterization | representation-dependent | visualization |

## Verdict
No single representation is universally best. The right view depends on the probe, geometry, and question.

The strongest bridge candidate in the current stack is the coherence-vector style representation because it preserves more structure than spectrum-only summaries while staying close to the density-operator language.

## Related pages
- [[constraint-on-distinguishability]]
- [[mass-equivalence-engine]]
- [[compression-to-density-matrix-map]]
- [[aligned-sim-backlog-and-build-order]]
- [[pca-qpca-density-matrix-view]]
- [[research-inventory-and-foundational-findings]]
- [[sim-session-index]]
