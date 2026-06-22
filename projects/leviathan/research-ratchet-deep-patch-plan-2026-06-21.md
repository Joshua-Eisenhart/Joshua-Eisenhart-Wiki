---
title: Leviathan Research Ratchet Deep Patch Plan
created: 2026-06-21
updated: 2026-06-21
type: implementation-plan
status: proposal_design_current
claim_ceiling: patch plan; not merged/runtime canon
---

# Leviathan Research Ratchet Deep Patch Plan

## Thesis

Do not patch Leviathan by merely adding a memory store.

Patch Leviathan by adding a **world-model graph patch loop** whose accepted state is event-sourced and gate-admitted.

Spinor Memory and Attractor Basin Digger are first applications of that loop.

## Existing Lev spine

Leviathan already has the needed separation:

```text
FlowMind        graph authoring, policy, evaluator/effect bindings
Orchestration   traversal, scheduling, worker dispatch
Exec            ACT through blessed ports
Effect          EffectEnvelope, ObservedEffect, EffectReceipt
Eval            measurements, discharge, GateProof, ProofBundle
Semantic Control NextTickPlan from lineage + scored facts + policy
Ledger          append-only run/action/seal refs
Graph State     state/knowledge plane
UI/Telemetry    read projections only
```

## Missing primitive: GraphPatch

Add `GraphPatch` as the shared unit across FlowMind, Effect, Eval, ClaimGate, and Graph State.

```text
GraphPatch
  patch_id
  target_graph_ref
  patch_kind
  bounded_object_id
  claim_text
  claim_ceiling
  source_refs
  intended_mutation
  required_gates
  operator_trace
  authority_state
  evidence_requirements
  rollback_or_graveyard_plan
```

## Missing primitive: WorldModelGraph

Accepted canon/code/wiki/skills/folders/flows/eval-packs should be projected into a typed graph.

```text
WorldModelGraph
  nodes: canon, code, wiki, skill, flow, eval, sim, receipt, branch, graveyard, frontier
  edges: cites, supersedes, admits, blocks, consumes, verifies, projects, splits, kills
```

## Missing primitive: BasinProjection

Attractor Basin Digger is a projection over WorldModelGraph + SpinorMemory + ReceiptLog.

```text
BasinProjection
  active_object
  center
  invariants
  frontier
  forbidden_moves
  leakage_edges
  split_tests
  next_deepening_moves
```

## Patch flow

```text
1. FlowMind proposes GraphPatch.
2. Admission gate checks scope, authority requirements, claim ceiling, topology, and basin.
3. Exec performs ACT if admitted.
4. Effect records ObservedEffect.
5. Eval measures proof obligations and emits GateProof/ProofBundle/proof.yaml refs.
6. ClaimGate records proposal/approval/request/receipt authority transition when promotion is sought.
7. Ledger seals refs.
8. SpinorMemory appends successor orientation cell.
9. AttractorBasinDigger updates basin projection and NextTickPlan features.
10. Graph State projects accepted state; UI mirrors only.
```

## Package targets

```text
core/domain/src/research-ratchet/
  graph-patch.ts
  spinor-memory-cell.ts
  attractor-basin-map.ts
  cold-start-packet.ts
  operator-spec.ts

core/graph-state/src/research-ratchet/
  spinor-store.ts
  basin-projection.ts
  patch-index.ts

core/flowmind/system/research-ratchet.flow.yaml
core/eval/suites/research-ratchet/*.eval.yaml
core/effect/policies/research-ratchet.yaml
```

## Must not do

- Do not create a second proof brain.
- Do not let Spinor Memory promote canon.
- Do not call v0 true Clifford/spinor computation.
- Do not let Wizard/council/LLM prose mutate authority state.
- Do not let dashboards, scorecards, or green UI synthesize closure.
- Do not bypass Effect: no proof before ObservedEffect.
- Do not allow enforcing gates without trust-root verified owner + host authority.

## First PR set

1. Add JSON schemas for `GraphPatch`, `SpinorMemoryCell`, `AttractorBasinMap`, `ColdStartPacket`.
2. Add pure validator package with no authority power.
3. Add FlowMind graph for Research Ratchet tick.
4. Add EvalSuite for operator-order, claim-ceiling, graveyard, and receipt-ref checks.
5. Add Effect policy requiring ObservedEffect before eval proof.
6. Add ClaimGate receipt-link adapter.
7. Add ColdStartPacket compiler.
8. Add vector-first / spinor-rerank retrieval hook.
9. Add basin classifier v0.
10. Add repo/wiki sync docs and acceptance tests.

## Acceptance tests

```text
same_text_different_trace
reject_host_consume_before_owner_approve
reject_promote_without_effect_eval_receipt
reject_enforcing_without_trust_root_verified
projection_green_not_authority
llm_verdict_not_authority
cold_start_reconstructs_frontier
basin_digger_classifies_massrun_without_admission_as_leakage
codex_ratchet_sim_mode_declared
ratcheted_mode_recomputes_induced_geometry
```
