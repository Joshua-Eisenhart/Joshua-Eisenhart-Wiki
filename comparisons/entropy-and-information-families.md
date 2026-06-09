---
title: Entropy and Information Families
created: 2026-04-07
updated: 2026-04-07
type: comparison
framing: current
tags: [comparison, simulation, validation, research]
sources:
  - raw/articles/new-docs/05_research_index.md
  - raw/articles/new-docs/10_cross_domain_equivalence_map.md
  - raw/articles/new-docs/11_mass_equivalence_engine.md
  - raw/articles/new-docs/08_aligned_sim_backlog_and_build_order.md
---

# Entropy and Information Families

## What is being compared
The entropy and information measures under consideration for the same underlying carrier and probe structure.

## Comparison
| Family | What it measures | Main caveat | Current role |
|---|---|---|---|
| Shannon | classical uncertainty | basis-dependent if naively diagonalized | useful but not foundational |
| von Neumann | mixedness of density operators | needs the correct operator carrier | core admissible quantum entropy |
| Rényi | family of spectral sensitivities | parameter choice matters | useful sweep family |
| Tsallis | nonextensive spectrum-sensitive uncertainty | interpretation depends on context | candidate family |
| Min / max entropy | one-shot extremal behavior | task-specific, not universal | edge-case diagnostics |
| Mutual information | total correlation | not a substitute for geometry | core correlation measure |
| Conditional entropy | reduction under conditioning | can be subtle in quantum settings | bridge diagnostic |
| Coherent information | signed cut quantity / transmission-relevant quantity | only meaningful on proper joint structure | load-bearing bridge quantity |
| Entanglement entropy | bipartite quantum correlation | depends on bipartition and reduction | important but not universal |

## Verdict
Entropy is important, but it is not first. It becomes decisive only after the carrier, probe, operator, and geometry layers are admitted.

## Related pages
- [[constraint-on-distinguishability]]
- [[mass-equivalence-engine]]
- [[compression-to-density-matrix-map]]
- [[aligned-sim-backlog-and-build-order]]
- [[entropy-sweep-protocol]]
- [[axis-and-entropy-reference]]
- [[tier-status]]
- [[quantum-information-measures]]
- [[density-matrix-mathematics]]
