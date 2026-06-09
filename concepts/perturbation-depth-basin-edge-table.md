---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [perturbation, attractors, basins, manifolds, evidence, formal-scouts]
sources:
  - /tmp/perturbation_depth_group_table_20260518.json
---

# Perturbation-Depth Basin-Edge Table

## Purpose
This page extracts the perturbation-depth rows behind [[attractor-basin-row-level-evidence-ledger]].

It gives the wiki a concrete basin-edge support surface: not a final basin proof, but a local table of how manifold-on and manifold-off perturbation rows behave by loop class and perception.

## Evidence boundary
Source result:
- `system_v5/ops/formal_scouts/results/stage_record_true_perturbation_depth_probe_results.json`

Extraction artifact:
- `/tmp/perturbation_depth_group_table_20260518.json`

Status:
- classification: `formal_scout`
- all_pass: `True`
- promotion_allowed: `False`

Claim ceiling:
> Formal scout only: tests local rank-repair perturbation depth for the source-native science-method stage-record row. It does not admit global manifold requirement, final FEP, final Axis0, deep-basin promotion, Holodeck, physics, cognition, world-model, architecture, or canonical claims.

## Grouped perturbation table

| Loop class | Perception | Rows | Epsilons | Avg manifold-on repair delta | Avg manifold-off repair delta | Avg manifold-step KL | Avg off-manifold KL | On ranks | Off ranks |
|---|---|---:|---|---:|---:|---:|---:|---|---|
| inner | Se | 40 | [0.05, 0.15, 0.3, 0.45] | 0.866447 | 0 | 0.338428 | 0 | [1] | [2] |


## Reading rule
This table supports local basin-edge language only.

Safe reading:
- manifold-on rows show a nonzero repair/perturbation effect under the local stage-record setup;
- manifold-off rows give a contrast surface;
- loop/perception grouping helps preserve differences rather than collapsing all perturbations into one number.

Unsafe reading:
- this proves a global attractor basin;
- this admits final FEP, Axis0, Holodeck, cognition, or world-model claims;
- this proves the manifold requirement generally.

## Anti-teleology connection
The table is useful because it shows selection pressure as a family of local perturbation responses.

It supports sentences like:
- a basin edge is a perturbation-sensitive boundary, not a final goal;
- viable continuations can be locally tested by perturbing the support;
- the present is selected by what remains repairable under continuation pressure.

## Next work
- Link these groups to the corresponding stage-record row names and source docs.
- Compare with the 33-case classifier table to see which labels correspond to strong perturbation separation.
- Add a small visualization or summary if a future wiki pass builds diagrams.

## Related pages
- [[basin-stability-and-viability-support]]
- [[attractor-basin-row-level-evidence-ledger]]
- [[attractor-basin-classifier-case-table]]
- [[attractor-basin-result-surface-ledger]]
- [[anti-teleology-future-option-selection]]
- [[systems-philosophy-attractor-basin-inversion]]
- [[sim-math-geometry-result-surface-router]]
