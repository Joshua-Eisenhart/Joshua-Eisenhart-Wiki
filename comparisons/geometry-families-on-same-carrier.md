---
title: Geometry Families on the Same Carrier
created: 2026-04-07
updated: 2026-04-15
type: comparison
framing: current
tags: [comparison, geometry, validation, simulation]
sources:
  - raw/articles/new-docs/05_research_index.md
  - raw/articles/new-docs/07_model_math_geometry_sim_plan.md
  - raw/articles/new-docs/10_cross_domain_equivalence_map.md
  - raw/articles/new-docs/CONSTRAINT_ON_DISTINGUISHABILITY_FULL_MATH.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Geometry Families on the Same Carrier

## Role in the live wiki cluster
- Strongest use: compact comparison page for which geometry families survive or fail when they are all tested against the same admissible carrier.
- Weak use: first-stop authority page for current repo truth, geometry build order, or rerun-backed status claims.
- Authority boundary: comparison/router page that helps readers separate geometry options on one shared carrier; it does not replace the current front door, the repo-current controller docs, or the narrower formal/reference pages that define each family in more detail.

## Recommended reading order
1. `hermes-current/read-first.md` and the rest of the `hermes-current/` spine
2. `projects/codex-ratchet/read-first.md` when the task is Codex Ratchet or repo-facing
3. `constraint-on-distinguishability.md` and `constraint-surface-and-process.md` for the shared admissible-carrier frame
4. `information-geometry-reference.md`, `berry-phase-and-holonomy.md`, or other narrower geometry pages for family-specific detail
5. this page when the question is specifically how the geometry candidates compare on the same carrier without widening into a larger omnibus summary

## What is being compared
Geometry candidates that act on the same admissible state carrier.

## Comparison
| Geometry family | Strength | Failure mode | Current status |
|---|---|---|---|
| Trace distance | operational distinguishability | can be too coarse for curvature | survives |
| Fidelity / Bures | information-geometric sensitivity | not a full metric in every convenience sense | survives |
| Fubini-Study | pure-state projective geometry | only applies cleanly on pure states | survives on pure rays |
| QFI / QGT | local sensitivity and curvature | needs admissible carrier and probe | survives |
| Berry phase / holonomy | transport / curvature witness | collapses under real-only or commutative reduction | survives |
| Hilbert-Schmidt alone | easy to compute | too flat to be the sole geometry | insufficient |

## Verdict
The admissible geometry is not flat or one-dimensional. The current stack favors curved, complex, probe-relative geometry tied to the same carrier used for state and operator structure.

## Related pages
- [[constraint-on-distinguishability]]
- [[constraint-surface-and-process]]
- [[mass-equivalence-engine]]
- [[aligned-sim-backlog-and-build-order]]
- [[system-architecture-reference]]
- [[research-inventory-and-foundational-findings]]
