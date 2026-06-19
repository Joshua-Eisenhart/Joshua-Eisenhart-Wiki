---
title: Tool Function Fanout Bank
created: 2026-06-19
type: tool-router
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, tools, fanout]
sources:
  - Codex-Ratchet/system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md
  - Codex-Ratchet/system_v5/ops/SIM_FULL_WIZARD_PARALLEL_RUNBOOK.md
  - Codex-Ratchet/system_v5/docs/TOOLING_STATUS.md
---


# Tool Function Fanout Bank — 2026-06-19

## Tool rows

| Layer | Tool | Expected role |
|---|---|---|
| proof | z3 | UNSAT impossibility, constraint logic |
| proof | cvc5 | cross-check z3, SyGuS/admissible-operator search |
| symbolic | sympy | symbolic algebra, derivations |
| geometry | clifford | geometric product, spinor/rotor claims |
| geometry | geomstats | manifold metrics, geodesics, curvature |
| geometry | e3nn | equivariant computation where symmetry-native PyTorch matters |
| graph | rustworkx | DAGs, dependency/routing/causal-order workloads |
| graph | XGI | hypergraphs and multi-way structure |
| topology | TopoNetX | cell-complex topology |
| topology | GUDHI | persistent homology and filtrations |
| computation | PyG | graph-native differentiable/message passing |
| computation | PyTorch/autograd | core differentiable substrate |

## Packet shape

```yaml
tool:
function_or_api_surface:
tiny_claim:
minimal_fixture_or_lego_target:
positive_case:
negative_case:
boundary_case:
demotion_condition:
out_of_scope:
ledger_loopback:
```

## Current wiki need

Add pages that describe exact function/API surfaces, not just tools. Tool presence is no longer enough; load-bearing usage is the gate.
