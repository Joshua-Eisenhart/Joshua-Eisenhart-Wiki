---
title: E3nn Equivariant Geometry Reference
created: 2026-04-13
updated: 2026-05-18
type: concept
tags: [concept, research, tooling, geometry, simulation, quantum]
sources:
  - raw/articles/new-docs/TOOLING_STATUS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/e3nn_capability_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_e3nn_irreps_tensor_product_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_e3nn_pyg_equivariance_under_mp_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/formal_scouts/results/e3nn_equivariant_constraint_manifold_geometric_feature_probe_results.json
framing: current
---

# e3nn Equivariant Geometry Reference

## Overview
e3nn is the E(3)/SO(3)-equivariant neural-network and representation-tool layer in the stack. It belongs to the geometry/tooling lane, but it is not just “a neural net library.” Its useful role is narrower: test whether declared irreps, tensor products, spherical harmonics, and equivariant feature maps preserve the symmetry constraint a probe says it depends on.

Use e3nn when the question is about equivariant structure under rotations or Euclidean symmetries. Do not use it as generic tensor numerics; PyTorch already covers that.

## Evidence boundary
This is a wiki/tool reference. It cites repo artifacts to anchor the role, but it does not promote results.

Observed repo anchors:
- `e3nn_capability_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: finite sim_e3nn_capability lego receipt only`, and `e3nn: load_bearing` with PyTorch as backend.
- `sim_e3nn_irreps_tensor_product_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_function_micro_only`, and `e3nn: load_bearing` for `o3.Irreps` / tensor-product dimension behavior.
- `sim_integration_e3nn_pyg_equivariance_under_mp_micro_results.json` reports `classification: canonical`, `all_pass: true`, `claim_ceiling: tool_integration_micro_only`, and load-bearing `e3nn` plus `pyg` for equivariant message passing on a tiny graph.
- `e3nn_equivariant_constraint_manifold_geometric_feature_probe_results.json` reports `classification: formal_scout`, `promotion_allowed: false`, `all_pass: 7/7`, and load-bearing e3nn/PyTorch/z3 roles.

Safe claim: e3nn has artifacted capability, function-micro, integration-micro, and formal-scout roles in the repo.

Unsafe claim: e3nn evidence by itself admits a final neural architecture, target-system model, manifold ontology, physics claim, bridge claim, or axis claim.

## Best-fit jobs in this stack
- checking `o3.Irreps` declarations and dimensions;
- testing tensor-product compatibility under declared irreps;
- checking whether a feature map commutes with SO(3)/E(3) actions;
- pairing vector irreps with PyG message passing when graph aggregation must preserve rotation action;
- comparing equivariant classifiers against plain MLP baselines as a scout-level witness;
- testing whether geometry/manifold features actually need symmetry-aware representation rather than generic tensor computation.

## Bad-fit jobs
Do not use e3nn to:
- replace full tensor, chirality, correlation, or density structure with a learned toy;
- treat classifier success as proof of an ontology or axis;
- promote a formal scout to canon because the equivariant model beat a baseline;
- hide carrier mismatch by forcing every geometry question into SO(3)/E(3) language;
- substitute neural-network training for exact algebra, SMT falsifiers, or topology witnesses.

## Good e3nn receipt shape
A useful e3nn receipt should name:
1. the irrep declaration, tensor-product layer, spherical harmonic, or equivariant feature map under test;
2. the group action or rotation matrix used;
3. the observable: output width, equivariance error, classifier contrast, commutation check, or representation mismatch;
4. the negative control: wrong feature width, broken equivariance, permuted labels, plain MLP baseline, or incompatible irrep fixture;
5. the claim ceiling: capability, tool-function micro, tool-integration micro, formal scout, or stronger only if a current process earned it.

Pass condition: the e3nn operation preserves or exposes the intended symmetry constraint under the stated probe.

Fail condition: the same result is achieved without equivariant structure, breaks under rotation/action checks, or only works by reducing away the structure the probe was supposed to preserve.

## Current role in the tool program
e3nn is strongest as a symmetry-preservation witness. It connects naturally to:
- [[pytorch-geometric-reference]] when equivariant graph/message-passing behavior is the target;
- [[geomstats-manifold-geometry-reference]] when manifold features need a symmetry-aware representation witness;
- [[clifford-geometric-algebra-reference]] when chirality/spin/orientation claims need algebraic checks alongside representation checks;
- [[smt-formal-falsifier-lane]] when a symbolic exclusion or countermodel is needed after the equivariant feature result;
- [[repo-tool-use-router]] for separating mention/import/supportive/load-bearing/promoted status.

When a result uses e3nn, future wiki tranches should classify the use as `mentioned`, `imported`, `supportive`, `load_bearing`, `tool_function_micro`, `tool_integration_micro`, `formal_scout`, or stronger only if the process earned it.

## Why it matters here
Some project claims are not just about geometry existing; they are about which distinctions survive transformations. e3nn is useful when that transformation is a rotation or Euclidean symmetry action and the candidate witness must carry typed representation structure rather than an unconstrained tensor.

Its strongest wiki role is to keep symmetry language honest: if a page says a feature or operator is equivariant, the wiki should route future agents toward an e3nn-style operation, a negative control, and a claim ceiling.

## Honesty fence
Older tooling notes correctly warned that e3nn usage was weak or exploratory in some audits. The current repo has stronger artifacted anchors now, but the boundary remains: e3nn can be load-bearing for a bounded tool/function/integration/formal-scout claim without becoming evidence for a final system architecture.

## How it connects
- [[repo-tool-use-router]]
- [[tooling-status]]
- [[current-tool-status-installed-vs-missing-vs-not-wired]]
- [[tool-capability-sim-program]]
- [[sim-run-catalogue-and-result-family-router]]
- [[pytorch-geometric-reference]]
- [[geomstats-manifold-geometry-reference]]
- [[clifford-geometric-algebra-reference]]
- [[smt-formal-falsifier-lane]]
- [[geometry-ingredient-map]]

## Row-level receipts
- [[e3nn-pyg-equivariance-message-passing-row]] — first ingested e3nn/PyG integration row; preserves `tool_integration_micro_only`, parent receipt gates, negative controls, and boundary fixtures.

## Next bounded wiki work
A good next e3nn tranche would process a second row only if it names a distinct e3nn function/API surface. Do not widen from this page into all equivariant learning or all graph-neural tools in one pass.
