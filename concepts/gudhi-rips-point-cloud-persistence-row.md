---
title: GUDHI Rips Point Cloud Persistence Row
created: 2026-05-18
updated: 2026-05-18
type: concept
tags: [simulation, tooling, topology, evidence]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gudhi_rips_point_cloud_micro_results.json
framing: current
---

# GUDHI Rips Point Cloud Persistence Row

## Purpose
This page is a row-level wiki ingestion from [[tool-function-receipt-matrix-router]]. It turns one exact GUDHI receipt into a human-readable wiki routing surface.

The row is:
- `system_v4/probes/a2_state/sim_results/sim_gudhi_rips_point_cloud_micro_results.json`

## Status boundary
This is row-level routing, not result promotion.

The receipt says:
- `classification`: `canonical`
- `all_pass`: `true`
- `claim_ceiling`: `tool_function_micro_only`

Safe claim: this row witnesses one bounded GUDHI RipsComplex point-cloud persistence micro: a square point cloud has one finite H1 interval born at side length `1.0` and killed at diagonal length `sqrt(2)`.

Unsafe claim: this row does not admit manually inserted SimplexTree coverage, AlphaComplex/CubicalComplex coverage, persistent cohomology, TopoNetX cross-checks, lego promotion, tool-tool coupling, Hopf, bridge, axis-level topology, or whole-GUDHI-library claims.

## Tool roles
| Tool | Integration depth | Role in this row |
|---|---|---|
| GUDHI | load-bearing | `RipsComplex` builds the point-cloud filtration, `create_simplex_tree` materializes simplices, and persistence reports H1 birth/death verdicts |
| PyTorch / PyG / z3 / cvc5 / SymPy / Clifford / Geomstats / e3nn / rustworkx / XGI / TopoNetX | not used | explicitly out of scope for this micro row |

## Observable
The main observable is the H1 persistence interval for the square point cloud:
- expected birth: `1.0`
- expected death: `1.4142135623730951`
- longest H1 lifetime: `0.41421356237309515`

The receipt states: the square's side edges create a 1-cycle at filtration `1.0`; diagonals enter at `sqrt(2)`, creating triangles that kill it.

## Positive checks
The row preserves two positive checks:
- `square_rips_has_one_finite_h1_bar`: one H1 interval born at side length and killed at diagonal threshold.
- `square_rips_contains_triangles_at_killing_threshold`: 2-simplices exist once diagonals enter the Rips filtration.

The square fixture reports simplex counts:
- vertices: `4`
- edges: `6`
- 2-simplices: `4`

## Negative and boundary controls
Negative controls that must exclude false topology:
- equilateral triangle is filled at threshold and has no positive-length H1 interval;
- the three-point triangle materializes exactly one 2-simplex.

Boundary controls that must preserve semantics:
- side-threshold square has only vertices and side edges before diagonals;
- singleton has finite filtration values and no H1.

## Demotion condition
Demote this row if:
- GUDHI cannot build the tiny point-cloud simplex tree;
- square H1 is not born at side length `1.0` and killed at diagonal length `sqrt(2)`;
- the filled three-point triangle reports a positive-length H1 bar;
- finite singleton or boundary filtrations cannot be reported.

## Surviving alternatives
The receipt keeps these alternatives open:
- other point-cloud filtrations may survive;
- manual SimplexTree persistence remains a separate GUDHI surface and is not retested here.

## Relation to tool pages
- [[gudhi-persistent-topology-reference]] should use this as the first concrete Rips point-cloud persistence row.
- [[tool-function-receipt-matrix-router]] should keep this as a row-level example, not a family-wide promotion.
- [[topology-carrier-tool-lane]] should treat it as a persistence witness, not a graph, hypergraph, or cell-complex witness.

## Related pages
- [[tool-function-receipt-matrix-router]]
- [[gudhi-persistent-topology-reference]]
- [[topology-carrier-tool-lane]]
- [[toponetx-topological-complex-reference]]
- [[xgi-hypergraph-reference]]
- [[rustworkx-graph-algorithms-reference]]
- [[geomstats-manifold-geometry-reference]]
- [[repo-tool-use-router]]
- [[sim-run-catalogue-and-result-family-router]]
