---
title: Spinor Memory and Attractor Basin Digger — integrated design
created: 2026-06-21
updated: 2026-06-21
type: architecture
status: current-research-overlay
claim_ceiling: JSON-first oriented memory and basin classifier design; no quantum memory; no proof authority
tags: [spinor-memory, attractor-basin-digger, research-ratchet, project-state, gates]
---

# Spinor Memory and Attractor Basin Digger — integrated design

## One sentence

**Spinor Memory stores the orientation of a project claim under ordered gates; Attractor Basin Digger decides whether the next graph patch keeps that claim inside the right project basin.**

They go together because long-horizon project failure is not merely fact loss. It is basin loss:

```text
model forgot the active object
model forgot the frontier
model forgot the claim ceiling
model collapsed proposal into proof
model drifted to UI/demo/marketing instead of gate-deepening
model retrieved a similar note with the wrong lifecycle state
```

## Spinor Memory

A Spinor Memory cell is not a vector embedding. It is a finite project-state object:

```json
{
  "kind": "SpinorMemoryCell",
  "object_id": "research-ratchet",
  "basin_id": "lev-native-project-harness",
  "claim_text": "Spinor memory stores project claims as oriented state under gates.",
  "claim_ceiling": "design proposal",
  "orientation": {
    "left": "source_owner_provenance",
    "right": "host_eval_admission",
    "chirality": "authority_chain"
  },
  "operator_trace": ["source_bind", "owner_approve", "host_request"],
  "allowed_next_ops": ["observe_effect", "eval_measure", "seal_receipt"],
  "blocked_ops": ["canon_promote", "proof_from_llm_prose"],
  "receipt_refs": []
}
```

The key invariant:

```text
same claim text + different operator_trace = different memory state
```

## Attractor Basin Digger

Attractor Basin Digger takes a proposed next move and classifies it relative to the active basin:

```text
basin_deepening
basin_leakage
basin_split
basin_kill
insufficient_evidence
```

It should inspect active object, frontier, invariant basis, claim ceiling, operator trace, receipt lineage, graveyard collisions, leakage edges, and next allowed gates.

## Why vectors are not enough

A vector index can retrieve related content. It cannot, by itself, tell whether the retrieved item is proposal-only, approved but not host-consumed, host-consumed but not effect-observed, verified with trust root, scratch diagnostic, graveyarded, or canon-promoted.

Vector retrieval stays useful as candidate generation. Spinor Memory is the state-valid filter/reranker above it.

```text
vector recall: what is semantically close?
spinor memory: what is the oriented project state?
basin digger: does the next patch deepen or leak?
ClaimGate/Effect/Eval: what is actually admitted?
```

## Diggers as operators

| Digger | Operator role | Output |
| --- | --- | --- |
| Axiom Digger | Finds invariant basis / conserved commitments. | `axiom_basis` |
| Constraint Digger | Finds forbidden regions / annihilators. | `constraint_basis`, `blocked_ops` |
| Gate Digger | Finds tests/admissibility projectors. | `gate_basis`, `required_receipts` |
| Attractor Basin Digger | Finds stable basin, leaks, splits, kill edges. | `basin_classification`, `next_allowed_moves` |

## Basin invariants for the current project

- Proposal is not promotion.
- Owner approval is not host admission.
- Host consumption requires request/receipt binding.
- Enforcing scope requires trust-root verified owner and host authority.
- ACT must produce ObservedEffect before semantic proof counts.
- Eval measures; LLMs may witness but never self-grade.
- Graph/UI/dashboard/vector-memory projections are not authority.
- Codex sims remain scratch/diagnostic until gates, receipts, and audits promote them.
- Old docs and old sims are mine/fuel, not roadmap or status.

## Integration pattern

```text
ColdStartPacket
  -> active SpinorMemoryCell set
  -> AttractorBasinMap
  -> FlowMind policy
  -> GraphPatchProposal
  -> admission
  -> effect/eval/receipt
  -> successor SpinorMemoryCell
  -> updated basin map
```

## Failure modes this should catch

- `docs_green_as_proof`
- `dashboard_green_as_proof`
- `fixture_authority_overclaim`
- `owner_approval_without_host_receipt`
- `host_consume_before_owner_approve`
- `promote_frontier_before_effect_eval_receipt`
- `massrun_expansion_as_admission_power`
- `vector_retrieval_as_project_understanding`
- `physics/bridge/Axis0 claims before M(C)/carrier gates`
- `spinor_memory_claimed_as_proof_authority`
