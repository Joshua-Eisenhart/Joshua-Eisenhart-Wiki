---
title: Pytorch Geometric Reference
created: 2026-04-13
updated: 2026-05-18
type: concept
tags: [concept, research, tooling, graph, qit, simulation]
sources:
  - raw/articles/new-docs/TOOLING_STATUS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/pyg_capability_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_pyg_message_passing_autograd_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_pyg_batching_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_e3nn_pyg_equivariance_under_mp_micro_results.json
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# PyTorch Geometric Reference

## Overview
PyTorch Geometric (PyG) is the tensor-on-graphs tool in the stack. It matters because the project often needs graph structure together with tensor, chirality, correlation, or message-passing structure.

PyG should be used when the graph is not just a static carrier but a computational graph for node/edge features, batching, propagation, or differentiable graph operations. It is not a replacement for every graph/topology tool.

## Evidence boundary
This page is a wiki/tool reference. It cites repo artifacts to anchor the role, but it does not promote results.

Observed repo anchors:
- `pyg_capability_results.json` reports `classification: canonical`, `all_pass: true`, and load-bearing PyG plus PyTorch roles.
- `sim_pyg_message_passing_autograd_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_function_micro_only`, and `pyg: load_bearing` with PyTorch supportive.
- `sim_pyg_batching_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_function_micro_only`, and `pyg: load_bearing` with PyTorch supportive.
- `sim_integration_networkx_pyg_graph_roundtrip_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_tool_micro_integration_only`, and load-bearing PyG plus NetworkX roles.
- `sim_integration_e3nn_pyg_equivariance_under_mp_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_integration_micro_only`, and load-bearing PyG plus e3nn roles.

Safe claim: PyG has artifacted capability, message-passing/autograd, batching, graph-roundtrip, and e3nn-integration roles.

Unsafe claim: PyG evidence by itself admits a graph-neural architecture, QIT bridge, axis, nonclassical, target-system, or full tensor/correlation claim.

## Best-fit jobs in this stack
- tensor structure on graph carriers;
- message passing with richer state representations;
- batching and mini-batch graph fixtures;
- graph-side coupling of QIT-like objects when full tensor/correlation structure is preserved;
- PyG/NetworkX roundtrip checks when graph data needs both ergonomic graph construction and tensor-message-passing form;
- PyG/e3nn integration when vector features must preserve SO(3)-style action through message passing.

## Bad-fit jobs
Do not use PyG to:
- replace rustworkx when only reachability, paths, cycles, or DAG operations are needed;
- replace XGI when higher-arity hyperedges are load-bearing;
- replace TopoNetX/GUDHI when cell-complex or persistence structure is the claim;
- treat learned/message-passing success as proof of a physical bridge or ontology;
- reduce away full tensor, entanglement, chirality, or correlation structure just to fit a graph neural network.

## Good PyG receipt shape
A useful PyG receipt should name:
1. the graph data object and feature tensors under test;
2. the operation: message passing, batching, graph roundtrip, edge-index transformation, or integration with e3nn/NetworkX;
3. the observable: output features, gradient/autograd behavior, batch separation, equivariance error, or roundtrip equivalence;
4. the negative control: wrong edge index, broken batching, permuted features, missing edge, non-equivariant transform, or graph-only baseline;
5. the claim ceiling: capability, tool-function micro, tool-tool integration micro, or stronger only if earned.

Pass condition: PyG preserves or exposes the graph+tensor relation under the active constraint.

Fail condition: the same result survives without graph structure, loses tensor/correlation/chirality information, or only works as a graph toy.

## Current role in the tool program
PyG is the differentiable graph/tensor lane. It connects naturally to:
- [[rustworkx-graph-algorithms-reference]] for pairwise graph algorithms and dependency witnesses;
- [[xgi-hypergraph-reference]] when higher-arity relations cannot be reduced to pairwise edge indexes;
- [[toponetx-topological-complex-reference]] and [[gudhi-persistent-topology-reference]] when the graph structure should become topology rather than message passing;
- [[e3nn-equivariant-geometry-reference]] when graph features need equivariant representation structure;
- [[repo-tool-use-router]] for mention/import/supportive/load-bearing/promotion separation.

## Why it matters here
Reduced toy graph formulations are not enough where the live claim depends on full tensor, entanglement, chirality, or correlation structure. PyG is one route to keeping graph carriers and tensor computation together, provided the receipt states exactly what was preserved and what was not.

Its strongest wiki role is to keep graph-neural language honest: message passing and batching are concrete operations, not proof of the system.

## How it connects
- [[repo-tool-use-router]]
- [[tooling-status]]
- [[current-tool-status-installed-vs-missing-vs-not-wired]]
- [[tool-capability-sim-program]]
- [[sim-run-catalogue-and-result-family-router]]
- [[support-spaces-and-process-classification]]
- [[actual-lego-registry]]
- [[qit-engine-geometry-entropy-bridge]]
- [[rustworkx-graph-algorithms-reference]]
- [[xgi-hypergraph-reference]]
- [[toponetx-topological-complex-reference]]
- [[gudhi-persistent-topology-reference]]
- [[e3nn-equivariant-geometry-reference]]

## Row-level receipts
- [[e3nn-pyg-equivariance-message-passing-row]] — first ingested PyG/e3nn integration row; preserves `tool_integration_micro_only`, parent receipt gates, negative controls, feature tensors, and boundary fixtures.

## Next bounded wiki work
A good next PyG tranche would process a separate batching or NetworkX/PyG roundtrip row, preserving `classification`, `claim_ceiling`, `tool_manifest`, feature tensors, and negative controls.
