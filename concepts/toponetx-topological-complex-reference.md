---
title: Toponetx Topological Complex Reference
created: 2026-04-13
updated: 2026-05-18
type: concept
tags: [concept, research, tooling, topology, geometry, mathematics]
sources:
  - raw/articles/new-docs/TOOLING_STATUS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/toponetx_capability_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_toponetx_cell_incidence_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_toponetx_hodge_laplacian_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_xgi_toponetx_higher_order_incidence_micro_results.json
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# TopoNetX Topological Complex Reference

## Overview
Current topology-carrier routing across XGI / TopoNetX / GUDHI lives at [[topology-carrier-tool-lane]].

TopoNetX is the stack's explicit topological-complex tool. It extends beyond plain graphs into cell/simplicial-complex-style representations, especially when incidence between nodes, edges, faces, and higher cells is the object under test.

Use TopoNetX when the support question is not just pairwise graph reachability and not just hyperedge membership, but a cell/rank/higher-order incidence structure.

## Evidence boundary
This page is a wiki/tool reference. It cites repo artifacts to anchor the role, but it does not promote results.

Observed repo anchors:
- `toponetx_capability_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: finite sim_toponetx_capability lego receipt only`, and `toponetx: load_bearing`.
- `sim_toponetx_cell_incidence_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_function_micro_only`, and `toponetx: load_bearing` with NumPy supportive.
- `sim_toponetx_hodge_laplacian_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_function_micro_only`, and `toponetx: load_bearing`.
- `sim_integration_xgi_toponetx_higher_order_incidence_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_integration_micro_only`, and load-bearing XGI plus TopoNetX roles.
- Representative nested-torus cell-incidence artifacts report `classification: tool_lego_fit_probe`, `promotion_allowed: false`, and load-bearing TopoNetX plus z3 roles.

Safe claim: TopoNetX has artifacted capability, cell-incidence, Hodge-Laplacian, XGI-integration, and tool-lego-fit roles.

Unsafe claim: TopoNetX evidence by itself admits bridge, axis, GStack, QIT, nonclassical, full topology, manifold, or target-system claims.

## Best-fit jobs in this stack
- cell-complex and higher-topology carriers;
- cell incidence, rank-2 incidence, and boundary-style structure;
- Hodge-Laplacian micro checks when the question is cell-complex algebra rather than persistence;
- topological state-class binding where graph edges are too thin;
- explicit support-space models beyond pairwise graphs;
- integration with [[xgi-hypergraph-reference]] when hyperedges need cell/rank comparison.

## Bad-fit jobs
Do not use TopoNetX to:
- replace XGI when named hyperedge membership is the real object;
- replace GUDHI when persistence, filtration, or lifespan across scale is the real object;
- replace rustworkx when ordinary graph reachability/cycle algorithms are enough;
- infer physical/topological ontology from a cell-complex fixture alone;
- promote a cell-incidence micro into a bridge or axis claim.

## Good TopoNetX receipt shape
A useful TopoNetX receipt should name:
1. the complex type and rank/cell objects under test;
2. the operation: cell incidence, boundary/incidence matrix, Hodge Laplacian, rank comparison, or XGI-to-cell mapping;
3. the observable: incidence shape, nonzero pattern, rank, Laplacian value, or matched/mismatched higher-order relation;
4. the negative control: missing cell, wrong rank, pairwise projection, XGI mismatch, or disconnected/degenerate complex;
5. the claim ceiling: capability, tool-function micro, tool-integration micro, tool-lego fit, or stronger only if earned.

Pass condition: the TopoNetX operation preserves or exposes the intended cell/higher-order incidence relation under the active constraint.

Fail condition: the result survives as an ordinary graph/hypergraph projection, the negative control also passes, or the complex fixture merely renames the intended topology.

## Current role in the tool program
TopoNetX is the cell-complex bridge between graph/hypergraph carriers and persistent topology. It connects naturally to:
- [[xgi-hypergraph-reference]] for hyperedge membership and higher-arity incidence;
- [[gudhi-persistent-topology-reference]] when the question becomes filtration/persistence;
- [[rustworkx-graph-algorithms-reference]] when pairwise graph algorithms are sufficient;
- [[smt-formal-falsifier-lane]] when finite readout/order predicates need symbolic support;
- [[repo-tool-use-router]] for mention/import/supportive/load-bearing/promotion separation.

## Why it matters here
If the project is support-first, the support cannot always be reduced to a graph. TopoNetX gives a richer carrier family for testing when the live object is cell/rank/incidence structure rather than a list of pairwise edges.

Its strongest wiki role is to keep higher-topology support claims from collapsing into either graph convenience or vague topology language.

## How it connects
- [[topology-carrier-tool-lane]]
- [[repo-tool-use-router]]
- [[tooling-status]]
- [[current-tool-status-installed-vs-missing-vs-not-wired]]
- [[tool-capability-sim-program]]
- [[sim-run-catalogue-and-result-family-router]]
- [[geometry-ingredient-map]]
- [[support-spaces-and-process-classification]]
- [[actual-lego-registry]]
- [[xgi-hypergraph-reference]]
- [[gudhi-persistent-topology-reference]]
- [[rustworkx-graph-algorithms-reference]]
- [[smt-formal-falsifier-lane]]

## Row-level receipts
- [[xgi-toponetx-higher-order-incidence-row]] — first ingested XGI/TopoNetX integration row; preserves `tool_integration_micro_only`, parent receipt gates, shared-pair incidence, and fake-pair/empty-fixture controls.

## Next bounded wiki work
A good next TopoNetX tranche would turn a separate Hodge-Laplacian or cell-incidence row into a row-level ledger, preserving `classification`, `promotion_allowed`, `claim_ceiling`, `tool_manifest`, and the negative control.
