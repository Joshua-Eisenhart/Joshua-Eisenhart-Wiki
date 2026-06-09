---
title: Rustworkx Graph Algorithms Reference
created: 2026-04-13
updated: 2026-05-18
type: concept
tags: [concept, research, tooling, graph, mathematics, systems]
sources:
  - raw/articles/new-docs/TOOLING_STATUS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/rustworkx_capability_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_rustworkx_dag_reachability_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_rustworkx_cycle_basis_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_fiber_base_loop_orientation_nodes_503_rustworkx_isolated_control_gap_survivor_classes_results.json
framing: current
---

# Rustworkx Graph Algorithms Reference

## Overview
rustworkx is the fast graph-kernel / DAG tool in the stack. It is the graph-side counterpart to proof and topology tools when the question is about dependency structure, routing, reachability, cycle structure, or graph algorithms rather than symbolic identities or higher-order carriers.

Use rustworkx when pairwise graph structure is the right carrier. Do not use it to flatten hypergraph, cell-complex, persistence, manifold, or algebraic questions into ordinary edges.

## Evidence boundary
This is a wiki/tool reference. It cites repo artifacts to anchor the tool role, but it does not promote results.

Observed repo anchors:
- `rustworkx_capability_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: finite sim_rustworkx_capability lego receipt only`, and `rustworkx: load_bearing` with NetworkX only supportive.
- `sim_rustworkx_dag_reachability_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_lego_fit_probe_only`, and `rustworkx: load_bearing` for graph reachability.
- `sim_rustworkx_cycle_basis_micro_results.json` reports `classification: canonical`, `all_pass: true`, and `rustworkx: load_bearing` for cycle-basis behavior.
- `sim_fiber_base_loop_orientation_nodes_503_rustworkx_isolated_control_gap_survivor_classes_results.json` reports `classification: tool_lego_fit_probe`, `all_pass: true`, `promotion_allowed: false`, and load-bearing rustworkx plus z3 roles.

Safe claim: rustworkx has artifacted capability, DAG reachability, cycle-basis, and tool-lego-fit roles in the repo.

Unsafe claim: rustworkx evidence by itself admits bridge, axis, GStack, QIT, nonclassical, full topology, or target-system claims.

## Best-fit jobs in this stack
- dependency DAGs and queue graph structure;
- routing, reachability, path, and endpoint analysis;
- cycle-basis and graph reduction checks;
- fast pairwise graph operations where NetworkX-style ergonomics are too slow or not precise enough for the receipt;
- graph-side support for seam, bridge, maintenance, or dependency reasoning;
- finite graph controls paired with [[smt-formal-falsifier-lane]] when a readout/order predicate also needs a symbolic witness.

## Bad-fit jobs
Do not use rustworkx to:
- replace XGI when the relation is genuinely higher-arity or hyperedge-based;
- replace TopoNetX or GUDHI when the question is cell-complex, simplicial, or persistent topology;
- replace PyG/e3nn when the question is learned/equivariant message passing;
- treat reachability as proof of a physical or ontology-level bridge;
- promote graph convenience into graph necessity.

## Good rustworkx receipt shape
A useful rustworkx receipt should name:
1. the graph fixture: directed graph, DAG, cycle graph, dependency graph, or pairwise support graph;
2. the operation: reachability, shortest/path query, topological order, cycle basis, connected components, reduction, or cut/path comparison;
3. the observable: reachable endpoint, path existence/length, cycle set, order, component, or reduction result;
4. the negative control: isolated node, reversed edge, broken orientation, disconnected component, or hand-enumerated baseline;
5. the claim ceiling: capability, graph micro, tool-lego fit, classical baseline, or stronger only if a current process earned it.

Pass condition: the rustworkx operation exposes the intended pairwise graph/dependency relation under the active constraint.

Fail condition: the result survives a disconnected/reversed/isolated control, depends on an accidental graph encoding, or erases a needed higher-order/topological/algebraic structure.

## Current role in the tool program
rustworkx is strongest as a pairwise graph and dependency witness. It connects naturally to:
- [[xgi-hypergraph-reference]] when pairwise edges are too thin and hyperedges are needed;
- [[toponetx-topological-complex-reference]] when a graph relation should become a cell/simplicial complex relation;
- [[gudhi-persistent-topology-reference]] when cycle or component structure becomes persistence/filtration evidence;
- [[pytorch-geometric-reference]] when graph structure becomes differentiable message passing;
- [[smt-formal-falsifier-lane]] when finite order/readout constraints need symbolic exclusion;
- [[repo-tool-use-router]] for separating mention/import/supportive/load-bearing/promoted status.

When a result uses rustworkx, future wiki tranches should classify it as `mentioned`, `imported`, `supportive`, `load_bearing`, `capability`, `graph_micro`, `cycle_micro`, `tool_lego_fit_probe`, `classical_baseline`, or stronger only if the process earned it.

## Why it matters here
The project keeps producing graph-shaped structures:
- queue/dependency surfaces;
- state-class/topology bindings;
- shell and interaction graphs;
- support/coupling structures;
- seam and bridge candidates that need pairwise graph controls before stronger topology or algebra is invoked.

rustworkx provides a stronger algorithmic graph layer for those tasks, but the wiki should keep its role bounded: pairwise graph witness first, broader carrier evidence only after the right higher-order/topology tools also carry the claim.

## How it connects
- [[repo-tool-use-router]]
- [[tooling-status]]
- [[current-tool-status-installed-vs-missing-vs-not-wired]]
- [[tool-capability-sim-program]]
- [[sim-run-catalogue-and-result-family-router]]
- [[support-spaces-and-process-classification]]
- [[graph-driven-intent-runtime]]
- [[xgi-hypergraph-reference]]
- [[toponetx-topological-complex-reference]]
- [[gudhi-persistent-topology-reference]]
- [[pytorch-geometric-reference]]
- [[smt-formal-falsifier-lane]]
- [[controller-prompt-rules]]

## Row-level receipts
- [[rustworkx-dag-reachability-row]] — first ingested rustworkx DAG reachability row; preserves `tool_lego_fit_probe_only`, BFS baseline comparison, reverse/isolated exclusions, and empty/singleton/cycle-blocked boundaries.

## Next bounded wiki work
A good next rustworkx tranche would process a separate cycle-basis or graph-reduction row only if it names a distinct rustworkx function/API surface. Do not widen from rustworkx into all graph/topology/carrier tools in one pass.
