---
title: Josh Root Constraints in Leviathan
created: 2026-06-18
updated: 2026-06-18
type: contribution-boundary-map
status: candidate/controller-verification-required
claim_ceiling: source-backed wiki synthesis only; not authorship proof, not implementation proof, not Codex Ratchet proof imported into Leviathan
---

# Josh Root Constraints in Leviathan

## Purpose

This page records the bounded Packet 4 answer to one question: where do Josh/root-constraint ideas appear in current Leviathan without collapsing Leviathan into Codex Ratchet or collapsing JP/Lev-dev runtime work into Josh's proof/admissibility lane?

The safe answer is:

```text
Current Leviathan docs explicitly attribute to Josh the identification of an ontological + operational constraint unification. Current Leviathan repo surfaces encode matching constraint vocabulary in FlowMind/System FlowMind and kernel surfaces. That supports a Josh/root-constraint contribution map, but it does not prove Josh authored the implementation and it does not turn Leviathan into Codex Ratchet.
```

## Three layers that must stay separate

| Layer | What it means here | Safe source classes | Do not promote to |
|---|---|---|---|
| Repo-current implementation/contracts | What the current repo files, specs, configs, and code say exists now. | `docs/specs/**`, `docs/ARCHITECTURE.md`, `docs/ROADMAP.md`, `core/flowmind/**`, `crates/lev-kernel/**` | Full runtime health unless tests/smokes verify it. |
| JP/Lev-dev intent | Lev's product/runtime direction and FlowMind/engine-builder design lane. | `docs/NORTH_STAR.md`, `docs/design/**`, roadmap language, handoffs marked as provenance | Josh authorship or Codex Ratchet proof. |
| Josh/root-constraint contribution | Finitude, non-commutation, nominalized reality, ratchet, locality, and the constraint/admissibility frame attributed to or aligned with Josh's ratchet work. | Explicit Josh passages; FlowMind Ratchet Harness design docs; provenance ledger; current constraint surfaces | Repo implementation proof, maintainer acceptance, or identity with Codex Ratchet. |

## Strongest explicit Josh contribution signal

The strongest current-repo attribution remains `docs/NORTH_STAR.md:190-200`:

- **Observed support:** `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md:190-200` says the constraint manifold as declarations enables evidence-driven evolution, deterministic replay, and an explicit LLM/kernel boundary, then states: “This is what Josh identified: two orthogonal constraint systems — ontological (ratchet, finitude, non-commutation) and operational (ABAC, leases, containment) — unified in a single declarative substrate.”
- **Claim ceiling:** explicit attribution to Josh for identifying/unifying the conceptual constraint structure; not proof that Josh wrote the current code.
- **Layer:** Josh/root-constraint contribution plus JP/Lev-dev intent, because it is in a current Lev North Star doc.

Safe wording:

```text
Current Leviathan docs explicitly attribute to Josh the identification of the ontological/operational constraint unification: ratchet, finitude, and non-commutation joined with ABAC, leases, and containment in one declarative substrate.
```

## Current Leviathan surfaces that carry the constraint frame

| Constraint-frame piece | Leviathan expression | Strongest source paths | Support label | Guardrail |
|---|---|---|---|---|
| Finitude root | C1 / `F01_FINITUDE`; finite explicit encoding; execution bounds. | `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:36-47`; `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts:58-123` | observed config + observed code | Supports current C1/F01 validator surface; not universal enforcement through every runtime path. |
| Non-commutation root | C2 / `N01_NONCOMMUTATION`; explicit dependency DAG; no cycles; order-sensitive composition. | `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:49-59`; `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts:130-248` | observed config + observed code | Supports C2/N01 native validator; not proof all FlowMind execution paths call it. |
| Nominalized reality | C3 governance assumption; validated canonical YAML; checksum/canonical form. | `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:65-79`; `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/schemas/system-flowmind.schema.yaml:313-357` | observed config + schema | Mark as governance/derived/aligned unless later repo source proves independent root status. |
| Ratchet | C4 governance assumption; append-only/audit/compensation; separate ratchet admission contract. | `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:81-94`; `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/ratchet-admission.flow.yaml:19-24`; `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs:29-43` | observed config + observed Rust code | Do not import Codex Ratchet proof/sim results as Lev implementation proof. Current Rust admission is simpler than the rich 7-stage contract. |
| Locality | C5 governance assumption; explicit scope; no omniscience/ambient authority. | `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:96-109`; `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/manifold.rs:20-23` | observed config + observed Rust enum | Mark as governance/derived/aligned unless implementation source proves independent root status. |
| Constraint manifold | Boot priority 0 System FlowMind declaration plus TS native evaluator. | `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:5-15`; `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts:1-12` | observed config + code | Good evidence for a repo surface, not a complete boot-path verification. |
| Ratchet harness bridge | FlowMind as socket; Josh's ratchet as chip; binding contract. | `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-system.md:35-47`; `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-ratchet.md:27-36` | design/provenance | Strong boundary/provenance language; not proof of full Josh system port. |

## C1/C2 roots vs C3-C5 governance

Current source support is asymmetric:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:5-7` says C1 and C2 are root axioms, non-configurable and FATAL, while C3-C5 are governance assumptions with derivation tracked for promotion.
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts:1-12` says the TypeScript validator enforces C1 and C2 as the two irreducible root axioms, and says C3-C5 governance assumptions live elsewhere.
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/schemas/system-flowmind.schema.yaml:276-317` encodes the same split: root axioms are irreducible/not derived/non-configurable/FATAL, while governance rules are enforced and tracked for future promotion to `derived_canon`.

Therefore this wiki should say:

```text
In current Leviathan constraint surfaces, C1/F01 and C2/N01 are root. C3, C4, and C5 are present and important, but they should be treated as governance / derived-aligned unless a later source proves them as independent roots.
```

## Josh/JP boundary in current design docs

`/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-system.md:35-47` names Josh as “Constraint Scientist” and JP as “Engine Builder,” then says FlowMind is the socket and the ratchet is the chip. `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-ratchet.md:27-36` repeats the same role split and frames the ratchet harness as a binding contract.

Safe wording:

```text
Design/provenance docs frame Josh as the constraint/spec lane and JP as the FlowMind/engine/runtime lane. Current repo code and architecture show the runtime surfaces matching the JP/Lev lane, while explicit Josh attribution is strongest at the conceptual constraint-unification layer.
```

## What this page does not claim

- It does not claim Josh authored current Leviathan implementation files.
- It does not claim JP's runtime work is a derivative proof of Codex Ratchet.
- It does not claim Codex Ratchet simulation/math proof has been implemented inside Leviathan.
- It does not claim every Leviathan execution path currently enforces C1/C2.
- It does not claim C3/C4/C5 are independent root axioms; current source support keeps them as governance/derived-aligned unless promoted by repo evidence.

## Source index

| Source path | Lines used | Support label |
|---|---:|---|
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md` | 119-129, 190-200 | observed current doc / explicit Josh attribution |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-system.md` | 35-47, 111-197 | design/provenance / Josh-JP role split / C1-C2 vs C3-C5 tiering |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-ratchet.md` | 27-36, 79-86, 362-379 | design/provenance / boundary / implementation-status caveat |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/design-flowmind.md` | 388-416 | design reference / ratchet hosting pattern |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml` | 5-15, 36-109, 140-155 | observed System FlowMind declaration |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts` | 1-19, 58-123, 130-345 | observed TypeScript native evaluator |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/schemas/system-flowmind.schema.yaml` | 276-357 | observed schema tiering |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/ratchet-admission.flow.yaml` | 19-24, 31-44, 114-160 | observed System FlowMind ratchet-admission contract |
| `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/manifold.rs` | 11-24, 78-85 | observed Rust kernel enum/surface |
| `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs` | 29-43, 57-82, 110-141 | observed Rust ratchet admission code/tests |
| `/Users/joshuaeisenhart/wiki/projects/leviathan-current/provenance-ledger-josh-jp-pass-1-2026-06-18.md` | 34-70, 72-98 | wiki provenance ledger / guarded synthesis |
| `/Users/joshuaeisenhart/wiki/wizard/harness-consolidated/14_leviathan_os_constraint_map.md` | 11-23, 50-54 | wiki doctrine bridge; alignment only, not implementation proof |
