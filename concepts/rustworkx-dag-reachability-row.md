---
title: Rustworkx DAG Reachability Row
created: 2026-05-18
updated: 2026-05-18
type: concept
tags: [simulation, tooling, graph, evidence]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_rustworkx_dag_reachability_micro_results.json
framing: current
---

# Rustworkx DAG Reachability Row

## Purpose
This page is a row-level wiki ingestion from [[tool-function-receipt-matrix-router]]. It turns one exact rustworkx receipt into a human-readable wiki routing surface.

The row is:
- `system_v4/probes/a2_state/sim_results/sim_rustworkx_dag_reachability_micro_results.json`

## Status boundary
This is row-level routing, not result promotion.

The receipt says:
- `classification`: `canonical`
- `all_pass`: `true`
- `claim_ceiling`: `tool_lego_fit_probe_only`

Safe claim: this row witnesses one bounded rustworkx graph reachability micro: `PyDiGraph`, `has_path`, `descendants`, and `ancestors` decide direct, transitive, absent, and cycle-blocked reachability on a tiny dependency DAG.

Unsafe claim: this row does not admit graph-cell lego promotion, hypergraph incidence, cell-complex boundary structure, bridge, axis, GStack, QIT engine, nonclassical admission, or proof of the whole rustworkx library.

## Tool roles
| Tool | Integration depth | Role in this row |
|---|---|---|
| rustworkx | load-bearing | `has_path`, `descendants`, and `ancestors` decide every reachability admission, exclusion, and boundary result |
| PyTorch / PyG / z3 / cvc5 / SymPy / Clifford / Geomstats / e3nn / XGI / TopoNetX / GUDHI | not used | explicitly out of scope for this graph-reachability micro row |

## Operation sequence
The row preserves this operation sequence:
1. Construct a checked rustworkx `PyDiGraph` over six named dependency nodes.
2. Add directed acyclic edges from source through two branch nodes, merge, and sink.
3. Query `has_path` for direct, transitive, reverse, and isolated-node reachability.
4. Query descendants and ancestors for source, sink, and boundary nodes.
5. Compare rustworkx reachability sets against a hand-written BFS baseline.
6. Run empty-graph, singleton, and cycle-blocked boundary controls.

## Observable
The observable is pairwise directed graph reachability:
- boolean `has_path` answers;
- descendant sets;
- ancestor sets;
- node counts;
- cycle rejection exception;
- equality against manual BFS reachability.

The positive row checks include:
- source reaches `admit_A`, `admit_B`, `merge`, and `sink`;
- direct source-to-`admit_A` and transitive source-to-`sink` paths exist;
- sink ancestors match manual BFS: `admit_A`, `admit_B`, `merge`, and `source`.

## Negative and boundary controls
Negative controls that must exclude false reachability:
- sink/leaf cannot reach source/ancestor;
- source cannot reach isolated node;
- sink has no descendants;
- source has no ancestors.

Boundary controls that must preserve graph semantics:
- empty graph has no descendants;
- singleton does not count as a zero-edge self-path proof;
- checked `PyDiGraph` rejects cycle insertion with `DAGWouldCycle`.

## Demotion condition
Demote this row if rustworkx `has_path`, `descendants`, or `ancestors` disagree with the hand-written BFS baseline on any positive, negative, or boundary fixture.

## Surviving alternatives
The receipt keeps these alternatives open:
- NetworkX can cross-check pairwise graph reachability as a classical baseline.
- XGI remains the better target for higher-order hyperedge incidence.

## Relation to tool pages
- [[rustworkx-graph-algorithms-reference]] should use this as the first concrete DAG reachability row.
- [[tool-function-receipt-matrix-router]] should keep this as a row-level example, not graph/topology promotion.
- [[xgi-hypergraph-reference]] and [[toponetx-topological-complex-reference]] remain the better routes when the relation is higher-order or cell-complex based.

## Related pages
- [[tool-function-receipt-matrix-router]]
- [[rustworkx-graph-algorithms-reference]]
- [[repo-tool-use-router]]
- [[sim-run-catalogue-and-result-family-router]]
- [[xgi-hypergraph-reference]]
- [[toponetx-topological-complex-reference]]
- [[gudhi-persistent-topology-reference]]
- [[pytorch-geometric-reference]]
