---
title: XGI TopoNetX Higher Order Incidence Row
created: 2026-05-18
updated: 2026-05-18
type: concept
tags: [simulation, tooling, topology, graph, evidence]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_xgi_toponetx_higher_order_incidence_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_xgi_hypergraph_incidence_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_toponetx_cell_incidence_micro_results.json
framing: current
---

# XGI TopoNetX Higher Order Incidence Row

## Purpose
This page is a row-level wiki ingestion from [[tool-function-receipt-matrix-router]]. It turns one exact integration receipt into a human-readable wiki routing surface.

The row is:
- `system_v4/probes/a2_state/sim_results/sim_integration_xgi_toponetx_higher_order_incidence_micro_results.json`

## Status boundary
This is row-level routing, not result promotion.

The receipt says:
- `classification`: `canonical`
- `all_pass`: `true`
- `claim_ceiling`: `tool_integration_micro_only`

Safe claim: this row witnesses one bounded XGI/TopoNetX integration micro: XGI hyperedge member sets and shared incidence agree with TopoNetX rank-2 cell vertices and boundary incidence on a tiny two-triad fixture.

Unsafe claim: this row does not admit Hodge spectral agreement, hypergraph Laplacians, higher-order dynamics, graph-cell lego promotion, bridge, axis, broad topology, whole-library equivalence, or target-system claims.

## Parent receipt gate
The row explicitly depends on two prior function receipts:

| Parent tool | Parent receipt | Observed status in row |
|---|---|---|
| XGI | `sim_xgi_hypergraph_incidence_micro_results.json` | exists, source exists, `all_pass: true`, `classification: canonical`, load-bearing, fresh for source |
| TopoNetX | `sim_toponetx_cell_incidence_micro_results.json` | exists, source exists, `all_pass: true`, `classification: canonical`, load-bearing, fresh for source |

If either parent receipt becomes missing, stale, noncanonical, not all-pass, or not load-bearing, this row demotes.

## Tool roles
| Tool | Integration depth | Role in this row |
|---|---|---|
| XGI | load-bearing | `Hypergraph`, hyperedge members, and shared incidence intersections supply one side of the higher-order fixture agreement |
| TopoNetX | load-bearing | `CellComplex`, rank-2 cells, and `incidence_matrix(2)` supply the independent cell-boundary witness |
| NumPy | supportive | densifies and inspects the TopoNetX incidence matrix without supplying the cell-complex structure |
| PyTorch / PyG / z3 / cvc5 / SymPy / Clifford / Geomstats / e3nn / rustworkx / GUDHI | not used | explicitly out of scope for this micro row |

## Operation sequence
The row preserves this operation sequence:
1. Load exact prior XGI hypergraph-incidence and TopoNetX cell-incidence receipts.
2. Construct an XGI Hypergraph with two overlapping three-node hyperedges.
3. Construct a TopoNetX CellComplex with the same two rank-2 triad cells.
4. Compare XGI hyperedge member sets against TopoNetX rank-2 cell vertex sets.
5. Compare shared-pair incidence in XGI intersection and TopoNetX rank-2 boundary incidence.
6. Run fake-pair, omitted-vertex, single-triad, and empty-fixture controls.

## Observable
The observable is higher-order incidence agreement across two tool representations:
- hyperedge member sets;
- rank-2 cell vertex sets;
- shared edge incidence count in the TopoNetX incidence matrix;
- fake-pair exclusion;
- single/empty fixture boundary counts.

The positive row checks include:
- XGI hyperedges `left = [0,1,2]`, `right = [1,2,3]` match TopoNetX rank-2 cells `[0,1,2]` and `[1,2,3]`.
- Shared pair `[1,2]` appears in both XGI intersection and TopoNetX shared-edge incidence.
- TopoNetX reports two rank-2 cells incident to the shared edge.

## Negative and boundary controls
Negative controls that must exclude false agreement:
- non-shared pair `[0,3]` must not be treated as shared incidence;
- omitted two-vertex cell `[0,1]` must not match the three-node triad.

Boundary controls that must preserve semantics:
- single triad maps to one rank-2 cell;
- empty XGI and TopoNetX fixtures fabricate no incidence.

## Demotion condition
Demote this row if:
- either parent receipt is missing, noncanonical, not all-pass, not load-bearing, or stale relative to its source;
- XGI hyperedge membership no longer matches TopoNetX rank-2 cell vertices;
- shared pair incidence is not seen by both tools;
- fake pairs, omitted vertices, or empty fixtures fabricate higher-order agreement.

## Relation to tool pages
- [[xgi-hypergraph-reference]] should use this as the first concrete XGI/TopoNetX integration row.
- [[toponetx-topological-complex-reference]] should use this as the first concrete hyperedge-to-cell incidence row.
- [[tool-function-receipt-matrix-router]] should keep this as a row-level example, not a family-wide promotion.

## Related pages
- [[tool-function-receipt-matrix-router]]
- [[xgi-hypergraph-reference]]
- [[toponetx-topological-complex-reference]]
- [[topology-carrier-tool-lane]]
- [[repo-tool-use-router]]
- [[sim-run-catalogue-and-result-family-router]]
- [[gudhi-persistent-topology-reference]]
- [[rustworkx-graph-algorithms-reference]]
