---
title: XGI Hypergraph Reference
created: 2026-04-13
updated: 2026-05-18
type: concept
tags: [concept, research, tooling, graph, topology, mathematics]
sources:
  - raw/articles/new-docs/TOOLING_STATUS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/xgi_capability_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_xgi_hypergraph_incidence_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_xgi_toponetx_higher_order_incidence_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/xgi_hopf_receipt_hyperedge_incidence_results.json
framing: current
---

# XGI Hypergraph Reference

## Overview
Current topology-carrier routing across XGI / TopoNetX / GUDHI lives at [[topology-carrier-tool-lane]].

XGI is the hypergraph tool in the stack. It matters when pairwise graph edges are too thin and the real structure is higher-arity: shared shells, receipt groups, multi-way carrier constraints, or hyperedges that should not be flattened into ordinary graph edges.

In wiki terms, XGI is a resistance-to-flattening tool. It asks whether a relation genuinely needs an n-ary carrier rather than a pairwise graph projection.

## Evidence boundary
This is a wiki/tool reference. It cites repo artifacts to anchor the tool role, but it does not promote results.

Observed repo anchors:
- `xgi_capability_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: finite sim_xgi_capability lego receipt only`, and `xgi: load_bearing`.
- `sim_xgi_hypergraph_incidence_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: finite sim_xgi_hypergraph_incidence_micro lego receipt only`, and `xgi: load_bearing`.
- `sim_integration_xgi_toponetx_higher_order_incidence_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_integration_micro_only`, and load-bearing XGI plus TopoNetX roles.
- `xgi_hopf_receipt_hyperedge_incidence_results.json` reports `classification: classical_baseline`, `all_pass: true`, `promotion_allowed: false`, and `xgi: load_bearing` over Hopf receipt dependency groups.
- `sim_nested_torus_shared_hyperedge_width_457_xgi_unshared_incidence_gap_survivor_classes_results.json` reports `classification: tool_lego_fit_probe`, `all_pass: true`, `promotion_allowed: false`, and load-bearing XGI plus z3 roles.

Safe claim: XGI has artifacted capability, incidence-micro, TopoNetX integration-micro, classical-baseline, and tool-lego-fit roles.

Unsafe claim: XGI evidence by itself admits a bridge, axis, GStack, QIT, nonclassical, full geometric-constraint-manifold, or target-system claim.

## Best-fit jobs in this stack
- hypergraph and higher-arity interaction structure;
- named hyperedges, node memberships, edge memberships, and incidence matrices;
- shell/hyperedge organization where the relation has more than two participants;
- multi-way coupling surfaces that should not be represented as pairwise graph edges;
- shared vs unshared incidence controls for survivor-class probes;
- pairing with [[toponetx-topological-complex-reference]] when hyperedge incidence needs a cell-complex/rank-2 comparison.

## Bad-fit jobs
Do not use XGI to:
- pretend every topology question is a hypergraph question;
- replace simplicial/cell-complex or persistence tools when those are the actual carrier;
- promote receipt-grouping or dependency hyperedges into physical independence claims;
- collapse path/reachability questions that belong to [[rustworkx-graph-algorithms-reference]] into hypergraph language;
- infer QIT, bridge, axis, or manifold conclusions from hyperedge incidence alone.

## Good XGI receipt shape
A useful XGI receipt should name:
1. the hypergraph fixture and the hyperedges used;
2. the operation: membership, incidence matrix, connected component, shared-incidence comparison, or hyperedge intersection;
3. the observable: node/edge membership, incidence rank/shape, connected group, shared-vs-unshared contrast, or survivor-class difference;
4. the negative control: pairwise projection, unshared incidence, missing hyperedge, wrong membership, or TopoNetX mismatch;
5. the claim ceiling: capability, hypergraph-incidence micro, integration micro, classical baseline, tool-lego fit, or stronger only if a current process earned it.

Pass condition: XGI preserves or exposes a higher-arity relation that a pairwise graph projection would lose under the active constraint.

Fail condition: the same result survives under pairwise edges, the negative control also passes, or the hypergraph representation merely renames a graph relation.

## Current role in the tool program
XGI is strongest as a higher-arity carrier witness. It connects naturally to:
- [[toponetx-topological-complex-reference]] for cell-complex and higher-order incidence comparison;
- [[gudhi-persistent-topology-reference]] when the question becomes persistence or filtration rather than hyperedge membership;
- [[rustworkx-graph-algorithms-reference]] when pairwise path, cut, reachability, or DAG structure is the right carrier;
- [[smt-formal-falsifier-lane]] when a finite order or readout predicate needs a symbolic witness alongside incidence;
- [[repo-tool-use-router]] for separating mention/import/supportive/load-bearing/promoted status.

When a result uses XGI, future wiki tranches should classify it as `mentioned`, `imported`, `supportive`, `load_bearing`, `capability`, `incidence_micro`, `tool_integration_micro`, `classical_baseline`, `tool_lego_fit_probe`, or stronger only if the current process earned it.

## Why it matters here
The project does not want to collapse all structure into binary edges when the real object may be n-ary or hypergraph-like. XGI is the main public tool surface for resisting that flattening.

Its strongest wiki role is to keep carrier language honest: if a page names shared shells, multi-way coupling, or higher-arity support, future agents should ask whether an XGI-style hyperedge/incidence operation is the right witness.

## How it connects
- [[topology-carrier-tool-lane]]
- [[repo-tool-use-router]]
- [[tooling-status]]
- [[current-tool-status-installed-vs-missing-vs-not-wired]]
- [[tool-capability-sim-program]]
- [[sim-run-catalogue-and-result-family-router]]
- [[support-spaces-and-process-classification]]
- [[geometry-ingredient-map]]
- [[toponetx-topological-complex-reference]]
- [[gudhi-persistent-topology-reference]]
- [[rustworkx-graph-algorithms-reference]]
- [[smt-formal-falsifier-lane]]
- [[controller-prompt-rules]]

## Row-level receipts
- [[xgi-toponetx-higher-order-incidence-row]] — first ingested XGI/TopoNetX integration row; preserves `tool_integration_micro_only`, parent receipt gates, fake-pair/omitted-vertex controls, and empty-fixture boundaries.

## Next bounded wiki work
A good next XGI tranche would process a separate hypergraph-incidence or survivor-class row only if it names a distinct XGI function/API surface. Do not widen from XGI into all graph/topology/carrier tools in one pass.
