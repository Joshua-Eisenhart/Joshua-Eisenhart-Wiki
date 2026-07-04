---
title: Pytorch Ratchet Build Plan
created: 2026-04-07
updated: 2026-04-10
type: concept
tags: [planning, simulation, system, architecture, implementation]
sources:
  - raw/articles/new-docs/PYTORCH_RATCHET_BUILD_PLAN.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# PyTorch Ratchet Build Plan

Historical 2026-04-10 migration-plan snapshot. Do not use this page for
current tool adoption, result counts, NumPy admissibility, or v5 status. Use
[[specs/codex-ratchet/README]] and the live `system_v5/docs` indexes first.

7-phase plan to migrate from numpy baselines to PyTorch-native ratchet architecture. Phases 1-2 complete, Phase 3 built but unvalidated.

## Architectural Model

Nested simultaneous constraint shells: S0 ⊃ S1 ⊃ S2 ⊃ ... Higher layers refine, not replace. The engine runs at the most constrained level where all active shells are simultaneously present.

## The Computational Claim

The PyTorch computational graph IS the ratchet:
- Forward pass = exploring allowed math space
- Backward pass = constraints selecting what survives
- Graph topology = constraint manifold
- Gradient = load-bearing signal
- Zero gradient = redundant noise

**Disconfirmation criteria**: gradient triviality, graph topology independence, forward sufficiency, substrate equivalence. If all four null across all 28 families, PyTorch claim is falsified.

## Axis 0: Formal Math

Axis 0 = gradient field of coherent information on shell parameter space: ∇\_η I\_c(ρ(η)). Not a scalar — a vector field.

Connections to QFI (metrological meaning), Bures metric (natural inner product), Berry curvature (geometric protection).

## Phase Status (audited 2026-04-10)

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | Classical baselines (numpy legos) | DONE — 613 sim files, 800 results |
| 2 | Constraint cascade (L0-L7, 28 families) | DONE |
| 3 | PyTorch-native modules (28 torch.nn.Module) | NOT_STARTED per registry; ~30+ sim_torch_*.py on disk, 0 formally migrated |
| 4 | Simultaneous differentiable shells | Exploratory sims only |
| 5 | Axis 0 via autograd | Gradient experiments exist, no formal field |
| 6 | Full ratchet as GNN | Exploratory sims only |
| 7 | Validation against baselines | PARTIAL — C1/C3/C4 pass; C2_graph_topology: 11/28 non-null, 17/28 null, 0/28 NOT_TESTED |

**Stale claim**: Build plan Phase 7 table previously implied 17/28 NOT_TESTED for C2_graph_topology. Actual audit shows 17/28 null and 0/28 NOT_TESTED; coverage is incomplete, but the missing status is null, not not-tested.

**Template compliance**: 45.6% of result JSONs have classification field; 41.0% have all three required fields (classification + tool_manifest + tool_integration_depth). 54.4% are legacy (pre-template).

**Missing document**: SHELL_COUPLING_PROGRAM.md referenced in LLM_CONTROLLER_CONTRACT.md does not exist as a standalone file. Coupling work is scattered across individual sims without staged progression.

## Tool Integration (12 tools)

Strong adoption: z3 (29 sims), clifford (23), toponetx (17), sympy (16).
Minimal: PyG (8), torch (11), gudhi (3).
Zero real usage: cvc5, geomstats, e3nn, rustworkx, xgi.

Planned (not installed): Lean 4, TLAPS.

## Key Findings from Phase 7

- Substrate-independent: long chains, concurrence, Lindblad agree to numerical precision
- Structural divergence in 2 scenarios: autograd vs finite-difference give different gradient structure
- "Computational graph carries content beyond the scalar" — partial evidence for ratchet claim

## Related Pages

- [[enforcement-and-process-rules]] — the 13 rules governing this build
- [[migration-registry]] — per-family migration state
- [[battery-index]] — negative test coverage
- [[axis-and-entropy-reference]] — axis stack reference
- [[constraint-surface-and-process]] — constraint manifold theory
- [[aligned-sim-backlog-and-build-order]] — build ordering
- [[shell-local-to-coupled-program]] — next sim program: coupling and emergence tests
- [[source-notes]]
- [[tooling-status]]
- [[system-architecture-reference]]
- [[pytorch-distributed-training-reference]] — scaling shell for torch-native execution
