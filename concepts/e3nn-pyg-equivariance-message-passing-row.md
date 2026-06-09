---
title: e3nn PyG Equivariance Message Passing Row
created: 2026-05-18
updated: 2026-05-18
type: concept
tags: [simulation, tooling, graph, geometry, evidence]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_e3nn_pyg_equivariance_under_mp_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_e3nn_irreps_tensor_product_micro_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_pyg_message_passing_autograd_micro_results.json
framing: current
---

# e3nn PyG Equivariance Message Passing Row

## Purpose
This page is the first row-level wiki ingestion from [[tool-function-receipt-matrix-router]]. It turns one exact receipt row into a human-readable wiki routing surface.

The row is:
- `system_v4/probes/a2_state/sim_results/sim_integration_e3nn_pyg_equivariance_under_mp_micro_results.json`

## Status boundary
This is row-level routing, not result promotion.

The receipt says:
- `classification`: `canonical`
- `all_pass`: `true`
- `claim_ceiling`: `tool_integration_micro_only`

Safe claim: this row witnesses one bounded e3nn/PyG integration micro: PyG additive directed message passing commutes with a shared e3nn SO(3) vector-irrep action on a tiny directed vector-feature graph.

Unsafe claim: this row does not admit learned GNN equivariance, e3nn convolution, graph/operator lego promotion, bridge, axis, broader graph dynamics, target-system claims, or broad e3nn/PyG compatibility.

## Parent receipt gate
The row explicitly depends on two prior function receipts:

| Parent tool | Parent receipt | Observed status in row |
|---|---|---|
| e3nn | `sim_e3nn_irreps_tensor_product_micro_results.json` | exists, source exists, `all_pass: true`, `classification: canonical`, load-bearing, fresh for source |
| PyG | `sim_pyg_message_passing_autograd_micro_results.json` | exists, source exists, `all_pass: true`, `classification: canonical`, load-bearing, fresh for source |

If either parent receipt becomes missing, stale, noncanonical, not all-pass, or not load-bearing, this row demotes.

## Tool roles
| Tool | Integration depth | Role in this row |
|---|---|---|
| PyTorch | supportive | tensors carry the e3nn/PyG feature fixtures and numeric equality checks |
| PyG | load-bearing | `MessagePassing.propagate` supplies the directed additive aggregation that must commute with the shared irrep action |
| e3nn | load-bearing | `o3.Irreps` and `D_from_matrix` supply the SO(3) vector representation used in the equivariance pass/fail check |
| z3 / cvc5 / SymPy / Clifford / Geomstats / rustworkx / XGI / TopoNetX / GUDHI | not used | explicitly out of scope for this micro row |

## Operation sequence
The row preserves this operation sequence:
1. Load and check the prior e3nn irrep tensor-product function receipt.
2. Load and check the prior PyG MessagePassing autograd function receipt.
3. Construct a three-node directed vector-feature graph with e3nn `1o` feature width.
4. Compute the e3nn SO(3) vector representation matrix from a bounded rotation.
5. Run PyG additive MessagePassing before and after applying the shared irrep action.
6. Compare rotate-then-message against message-then-rotate equivariance residual.
7. Run negative fixtures for fixed unrotated bias, wrong output representation, and malformed feature width.
8. Run boundary fixtures for isolated-node zero vector output and zero-batch vector-width preservation.

## Observable
The primary observable is the max absolute difference between the two paths:
- rotate then message;
- message then rotate.

The row reports:
- `max_equivariance_error`: `2.220446049250313e-16`
- `tolerance`: `1e-05`
- `e3nn_irrep`: `1x1o`
- edge semantics: `edge_index[0]` source vectors add into `edge_index[1]` targets

## Negative and boundary controls
Negative controls that must fail or raise:
- fixed unrotated bias breaks equivariance;
- wrong output representation is excluded;
- malformed feature width is rejected.

Boundary controls that must preserve semantics:
- isolated node receives zero vector;
- zero-node batch preserves vector width.

## Demotion condition
Demote this row if:
- either parent receipt is missing, noncanonical, not all-pass, not load-bearing, or stale relative to its source;
- PyG additive aggregation does not commute with the e3nn vector irrep action;
- biased or wrong-representation paths pass;
- malformed feature widths are silently accepted.

## Relation to tool pages
- [[e3nn-equivariant-geometry-reference]] should use this as the first concrete e3nn/PyG integration row.
- [[pytorch-geometric-reference]] should use this as the first concrete equivariant-message-passing row.
- [[tool-function-receipt-matrix-router]] should keep this as a row-level example, not a family-wide promotion.

## Related pages
- [[tool-function-receipt-matrix-router]]
- [[e3nn-equivariant-geometry-reference]]
- [[pytorch-geometric-reference]]
- [[repo-tool-use-router]]
- [[sim-run-catalogue-and-result-family-router]]
- [[tool-capability-sim-program]]
- [[rustworkx-graph-algorithms-reference]]
- [[xgi-hypergraph-reference]]
