---
title: CR / Lev merge project plan
created: 2026-07-02
type: gated-project-plan
status: active merge program
claim_ceiling: gated integration plan for CR evidence flowing through Lev surfaces; not completion proof, not release certification, and not promotion of pending scouts or legos
tags: [lev, codex-ratchet, merge, sim-witness, admissibility, graph]
sources:
  - projects/leviathan-current/LEV_CR_INTEGRATION_STATE_2026-07-02.md
  - projects/leviathan-current/GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md
  - projects/leviathan-current/MESH_NODE_PROTOCOL_V0_2026-07-02.md
---

# CR / Lev Merge Project Plan - 2026-07-02

This is the gated merge program for Codex Ratchet evidence entering Lev through adapters, witness packs, guarded runners, and graph residency. Order matters: later milestones consume receipts from earlier milestones instead of bypassing them.

## Status ladder

Milestone language is bounded by receipts:

```text
not-started < in-flight < schema-shaped < runs < passes fresh local rerun < admitted by declared gate < landed upstream < canonical by process
```

The current program is `active merge program`. Individual milestones below carry their own blocker and receipt criterion.

## Related

- [Lev / CR Integration State](./LEV_CR_INTEGRATION_STATE_2026-07-02.md)
- [Gate Doctrine: Admissibility, Not Quality](./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md)
- [Mesh Node Protocol v0](./MESH_NODE_PROTOCOL_V0_2026-07-02.md)
- [Relevant Docs Index](./RELEVANT_DOCS_INDEX_2026-07-02.md)
- [Leviathan Claim Ceilings](./leviathan-claim-ceilings-2026-06-19.md)

## Gated order

| Milestone | Scope | Current status | Blocker | Receipt criterion |
|---|---|---|---|---|
| M0 evidence catalog | Inventory CR evidence estate: result files, schemas, engine legs, negative controls, source commits, generated receipts, and battery eligibility. | in-flight | Catalog must distinguish full v1 legs from sparse drafts and must preserve source/provenance addresses. | Catalog file or receipt set lists each candidate with schema id, source commit/address, engine, `negative_tests` status, freshness, and eligibility verdict. |
| M1 corpus schema conformance | Make corpus artifacts conform to intake schemas before they touch batteries. v1 legs are done for v7 core plus 6 drafts. Legos/scouts remain pending JP's `FORMAL_SCOUT_RESULT_v1` and `LEGO_RESULT_v1` schemas. | partially schema-shaped | Scout and lego schemas are not landed; sparse drafts still need full-leg reruns where required. | Adapter validation passes for v7 core and six drafts; later, scout/lego samples validate against JP's schemas with malformed/sparse fixtures rejected. |
| M2 corpus flow | Drive catalog-selected artifacts through adapters in batches so the battery-eligible set grows by receipt, not hand selection. | planned after M0/M1 receipts | Needs catalog fields stable enough to select eligible batches and route non-eligible artifacts to rerun/fix queues. | Batch run emits per-artifact adapter verdicts, rejected-candidate reasons, content addresses, and an updated eligible set. |
| M3 gates-as-packs | Re-express general CR harness gates as Lev evaluator/witness packs where the gate is not CR-specific private machinery. | planned | Need a boundary split between general admission logic and CR-only witness family details. | At least one general gate pack lands with tests, negative controls, and claim-language ceiling; CR-specific residue remains fenced. |
| M4 run-side integration | Let `lev exec` dispatch the CR guarded runner. The deep host-executed pattern exists from pilots; this milestone makes it a guarded program path. | planned with pilot precedent | Needs stable runner invocation, declared permissions, source-hash-pinned carriers, and fail-closed host execution semantics. | `lev exec` receipt shows CR guarded runner invoked on host, source hashes checked, negative controls executed, adapter consumed output, and failures reported without hand edits. |
| M5 graph residency | Represent CR registry rows as Lev world-model nodes while preserving labels, claim ceilings, evidence refs, addresses, and status rungs. | planned | Needs schema mapping that does not flatten CR labels into broad accepted/green language. | Graph events/rows show CR registry entries with preserved labels and evidence refs; query can recover source address, gate verdict, claim ceiling, and current rung. |
| M6 bridge/flow: QIT surprise evidence | Route the QIT bridge `surprise_bits` stream as EVIDENCE into Lev's existing G3 `SurprisePredictor` port. | planned after upstream rehoming stabilizes paths | `core/reconciler` already ships the G3 `SurprisePredictor` port and documents it as wrapping an FEP-surprisal seam; the bridge must feed that port rather than creating a new edge. | Receipt shows `surprise_bits` content/provenance entering the existing `SurprisePredictor` evidence path, with adapter rejection for malformed, stale, or verdict-shaped surprise evidence. |

## Milestone details

### M0 evidence catalog

Goal: create the routing spine. The catalog decides what can be attempted, what must rerun, and what is inadmissible until repaired.

Receipt criterion: every row has enough provenance for a receiving node to re-fetch or rerun, and every eligibility claim is bounded to an adapter/gate reason.

### M1 corpus schema conformance

Goal: prevent corpus flow from becoming string-shape optimism. v1 engine legs for v7 core plus six drafts are the first conforming set. Legos and scouts wait for JP's `FORMAL_SCOUT_RESULT_v1` and `LEGO_RESULT_v1` schemas.

Receipt criterion: conforming examples and hostile malformed examples both exist, and the adapter refuses sparse/self-graded inputs.

### M2 corpus flow

Goal: turn catalog rows into deterministic adapter batches. The battery-eligible set grows only when artifacts pass the declared shape, provenance, freshness, and falsifier requirements.

Receipt criterion: the batch receipt is content-addressed and shows both admitted and rejected cases.

### M3 gates-as-packs

Goal: package general CR gate logic as Lev evaluator/witness packs so it can be run by Lev's gate machinery without importing CR authority wholesale.

Receipt criterion: packs carry their own tests, negative controls, and claim ceilings. The pack says what it admits; it does not certify broad CR quality.

### M4 run-side integration

Goal: make CR guarded execution a Lev-dispatchable workload. The existing deep host-executed pilot pattern is precedent, not completion.

Receipt criterion: a `lev exec` run invokes the guarded runner, checks source hashes, executes falsifiers, emits provider evidence, and fails closed on malformed output.

### M5 graph residency

Goal: give admitted CR registry rows world-model residency without losing their original epistemic labels.

Receipt criterion: graph queries can distinguish `draft`, `battery-eligible`, `admitted by declared gate`, `landed upstream`, and any stronger process status without collapsing them.

### M6 bridge/flow: QIT surprise evidence

Goal: connect QIT bridge surprise evidence to the existing Lev reconciler surface. `core/reconciler` already includes the G3 `SurprisePredictor` port, explicitly documented as wrapping an FEP-surprisal seam, so `surprise_bits` arrives as EVIDENCE feeding that port. This is routing into an existing port, not a new bridge edge or a second surprise abstraction.

Receipt criterion: a bridge/flow receipt identifies the `surprise_bits` source address, schema or stream version, adapter verdict, and the receiving `SurprisePredictor` port path; hostile fixtures for sparse, stale, or verdict-shaped surprise evidence fail closed.

## Patch-flow hold

Patch work holds until JP's upstream rehoming push lands. JP is moving more upstream paths, so any patch series prepared before that push is staging context only until paths, imports, and receipt anchors are refreshed against the receiving tree.

## Cross-cutting rules

- No milestone may promote a claim above the receipt rung it earned.
- No adapter may consume `all_pass`, `promotion_allowed`, or `formal_admission_allowed` as provider evidence.
- No sparse draft becomes eligible by catalog inclusion alone.
- No scout or lego enters flow until the relevant JP schema exists and hostile fixtures fail.
- No graph row may erase provenance, negative-test status, source address, or claim ceiling.
- No patch-flow claim may advance while JP's upstream rehoming push is pending; refreshed paths and receipt anchors are required before dry-run, apply, or integration language.

## Claim ceiling

This plan is an integration route and blocker ledger. It may be used to coordinate merge work and ask for receipts. It may not be cited as proof that M1-M5 are complete, that CR corpus results are canonical, or that Lev release readiness has increased beyond the exact receipts produced by each milestone.
