---
title: Gudhi Persistent Topology Reference
created: 2026-04-13
updated: 2026-05-18
type: concept
tags: [concept, research, tooling, topology, geometry, mathematics]
sources:
  - raw/articles/new-docs/TOOLING_STATUS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gudhi_capability_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gudhi_simplex_persistence_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gudhi_alpha_complex_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gudhi_rips_point_cloud_micro_results.json
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# GUDHI Persistent Topology Reference

## Overview
Current topology-carrier routing across XGI / TopoNetX / GUDHI lives at [[topology-carrier-tool-lane]].

GUDHI is the persistence / topological-data-analysis layer in the stack. It is useful when the project wants topological pressure that survives scale changes, filtrations, simplex choices, or point-cloud constructions.

Use GUDHI when the live question is not merely whether a topological feature exists, but whether it persists under a filtration or construction rule.

## Evidence boundary
This page is a wiki/tool reference. It cites repo artifacts to anchor the role, but it does not promote results.

Observed repo anchors:
- `sim_gudhi_capability_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: finite sim_gudhi_capability tool-capability receipt only`, and `gudhi: load_bearing`.
- `sim_gudhi_simplex_persistence_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: finite sim_gudhi_simplex_persistence_micro lego receipt only`, and `gudhi: load_bearing`.
- `sim_gudhi_alpha_complex_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_function_micro_only`, and `gudhi: load_bearing`.
- `sim_gudhi_rips_point_cloud_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_function_micro_only`, and `gudhi: load_bearing`.
- Representative nested-torus filled-cycle artifacts report `classification: tool_lego_fit_probe`, `promotion_allowed: false`, and load-bearing GUDHI plus z3 roles.

Safe claim: GUDHI has artifacted capability, simplex persistence, alpha-complex, Rips point-cloud, and tool-lego-fit roles.

Unsafe claim: GUDHI evidence by itself admits bridge, axis, GStack, QIT, nonclassical, final topology, manifold, or target-system claims.

## Best-fit jobs in this stack
- persistence geometry and topological data analysis;
- simplex persistence and filtration checks;
- alpha-complex and Rips-complex point-cloud witnesses;
- topological pressure on geometry ratchets across scale;
- cycle/filling questions where lifespan under filtration matters;
- support for geometry/topology claims after graph or cell-complex witnesses have identified a candidate carrier.

## Bad-fit jobs
Do not use GUDHI to:
- replace XGI when the question is hyperedge membership;
- replace TopoNetX when the question is cell/rank incidence rather than persistence;
- replace rustworkx when ordinary graph path/cycle algorithms are the right object;
- treat a persistence diagram as ontology closure;
- promote a persistent feature into a bridge or axis claim without the current result contracts.

## Good GUDHI receipt shape
A useful GUDHI receipt should name:
1. the construction: simplex tree, Rips complex, alpha complex, filtration, or persistence computation;
2. the input carrier: point cloud, cycle, simplex set, nested-torus fixture, or geometry-derived sample;
3. the observable: Betti number, persistence pair, barcode/lifetime, filled cycle, or filtration threshold;
4. the negative control: filled vs unfilled cycle, shuffled points, degenerate simplex, wrong filtration, or graph-only witness;
5. the claim ceiling: capability, tool-function micro, tool-lego fit, or stronger only if earned.

Pass condition: the GUDHI operation exposes a topological feature whose persistence/lifetime is relevant under the active constraint.

Fail condition: the result disappears under the intended filtration, survives only as a construction artifact, or is equally present in the negative control.

## Current role in the tool program
GUDHI is the persistence witness lane. It connects naturally to:
- [[toponetx-topological-complex-reference]] when cell/rank incidence should be built before persistence;
- [[xgi-hypergraph-reference]] when a higher-arity relation needs a carrier before TDA;
- [[rustworkx-graph-algorithms-reference]] when cycles and components first need pairwise graph witnesses;
- [[geomstats-manifold-geometry-reference]] when manifold samples become point-cloud or filtration inputs;
- [[repo-tool-use-router]] for separating mention/import/supportive/load-bearing/promoted status.

## Why it matters here
The project often wants to know not only whether a topological feature exists, but whether it persists under filtration or scale. GUDHI is the right public reference surface for that tool family.

Its strongest wiki role is to stop topology language from becoming decorative: if persistence matters, the page should route toward an explicit filtration, an observable lifetime, and a negative control.

## How it connects
- [[topology-carrier-tool-lane]]
- [[repo-tool-use-router]]
- [[tooling-status]]
- [[current-tool-status-installed-vs-missing-vs-not-wired]]
- [[tool-capability-sim-program]]
- [[sim-run-catalogue-and-result-family-router]]
- [[geometry-ingredient-map]]
- [[support-spaces-and-process-classification]]
- [[toponetx-topological-complex-reference]]
- [[xgi-hypergraph-reference]]
- [[rustworkx-graph-algorithms-reference]]
- [[geomstats-manifold-geometry-reference]]

## Row-level receipts
- [[gudhi-rips-point-cloud-persistence-row]] — first ingested GUDHI Rips point-cloud persistence row; preserves `tool_function_micro_only`, H1 birth/death observable, filled-triangle negative control, and side-threshold/singleton boundaries.

## Next bounded wiki work
A good next GUDHI tranche would process a separate AlphaComplex, simplex-persistence, or nested-torus filled-cycle row only if it names a distinct GUDHI function/API surface.
