---
title: Research Ratchet Missing Primitives and Open Questions
created: 2026-06-21
updated: 2026-06-21
type: design-debt-ledger
status: proposal_design_current
claim_ceiling: open design debt; not implementation canon; not runtime proof
sources:
  - /Users/joshuaeisenhart/Downloads/research_ratchet_full_wiki_ingest_pack_20260621.zip
  - research/MISSING_PRIMITIVES_AND_OPEN_QUESTIONS_20260621.md
  - research/FULL_DEEP_RESEARCH_COMPENDIUM_20260621.md
---

# Research Ratchet Missing Primitives and Open Questions

This page records the design debt surfaced by the full wiki ingest packet. It is
not a runtime state surface and does not promote any primitive into Leviathan,
ClaimGate, Codex-Ratchet, or wiki canon by itself.

## Primitive register

| Primitive | Current role | Promotion boundary |
|---|---|---|
| GraphPatch | Universal proposed update object across docs, code, sims, evals, policies, skills, and authority state. | Must be translated against current Leviathan graph/compositor surfaces before runtime use. |
| GraphPatchEnvelope | EffectEnvelope-like wrapper for graph-state mutation proposals. | Needs schema, validator, and Effect/Eval path. |
| PatchIntentRef | Source intent pointer with adapter and content hash. | Needs source binding and owner/repo provenance policy. |
| PatchClass | Classification such as doc, code, ontology, eval, sim, policy, memory, authority, or basin patch. | Needs deterministic enum and gate-specific required fields. |
| OperatorSpec | Gate/operator definition with preconditions, postconditions, noncommutes-with, and receipt requirements. | Needs tiny illegal-transition and order-sensitivity tests. |
| OperatorTrace | Ordered operator history over a proposed patch. | Must be receipt-linked; LLM prose cannot advance the trace. |
| AuthorityLattice | Lifecycle ladder from proposal to approval, request, receipt, verification, admission, canon, rejection, or graveyard. | ClaimGate receipts must control promotion-bearing transitions. |
| CapabilityLattice | Which actor, runtime, or surface may propose, apply, evaluate, or admit which operator. | Needs host policy rather than dashboard or council agreement. |
| BasinMap | Stable region, leakage edges, graveyard zones, split points, and frontier labels. | Needs deterministic classifier inputs plus evidence-backed policy. |
| BasinClassifier | Classifies proposed patches as deepen, leak, split, kill, or insufficient evidence. | Must emit reasons, blocked moves, and required evidence; not proof authority. |
| ColdStartPacket | Portable state packet for re-entering the active project basin without chat history. | Needs compiler from receipts/wiki/repo/frontier, plus freshness checks. |
| Proof-Carrying State Entry | Graph state node that carries evidence refs instead of only summaries. | Needs accepted proof/ref schema and storage boundary. |
| GraphPatchReceipt | Sealed transition record for graph patch attempts and outcomes. | Needs hash, source refs, operator trace, and admission status. |
| Vector-to-Spinor Retrieval Adapter | Vector candidate retrieval followed by state/orientation/basin filtering. | Retrieval support only; cannot decide truth or admission. |

## Open ownership questions

- Leviathan should own runtime graph state, effect/eval execution, eventing, and
  host-consumed graph patch state.
- Codex-Ratchet should own sim/proof discipline, receipt-producing micro-scouts,
  and claim ceilings for mathematical or nonclassical evidence.
- ClaimGate should own authority-chain promotion when a patch seeks admission.
- The wiki should own source/provenance, doctrine summaries, plans, and cold-start
  read models, not authoritative cell storage.

## v0 naming decision

For v0, the essential primitive is not a true Clifford/spinor database. The
essential primitive is ordered operator state:

```text
patch + gate history + receipts + claim ceiling + basin context
```

Spinor Memory is currently a JSON-first oriented project-state read model. Any
finite Clifford or geometric-algebra version is future experimental work.

## ClaimGate caution

Do not collapse these states:

```text
trust_root_configured != trust_root_required_for_enforcement
```

Any v41-style enforcement claim needs current ClaimGate repo/package receipts
before the wiki writes stronger language than reported package state.

## Sim/proof backlog

The first Codex-Ratchet-facing work should stay micro-first:

1. Define `BasinSimReceipt_v0` and `GraphPatchReceipt_v0`.
2. Build one tiny finite GraphPatch basin-classifier fixture.
3. Prove one `OperatorSpec` / `OperatorTrace` order-sensitivity or illegal-transition claim with explicit controls.
4. Link outputs through ClaimGate receipt refs before any SpinorMemory projection.

Blocked claims:

- no direct sim-to-authority mutation;
- no Spinor Memory proof authority;
- no true basin, Axis0, Xi/Phi0, physics, QIT-engine, or manifold promotion;
- no admission without explicit finite carrier or bounded state, update/operator
  rule, controls, proof tier, and receipt path.

## Related pages

- [[projects/research-ratchet/README]]
- [[projects/research-ratchet/wiki-update-intake-2026-06-21]]
- [[concepts/world-engine-graph-patch-algebra]]
- [[concepts/spinor-memory]]
- [[concepts/attractor-basin-digger]]
- [[projects/codex-ratchet/spinor-memory-sim-integration-2026-06-21]]
- [[projects/leviathan-current/research-ratchet-deep-patch-plan-2026-06-21]]
