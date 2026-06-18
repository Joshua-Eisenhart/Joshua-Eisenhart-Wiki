---
title: Lev Five Constraints vs F01 N01
type: constraint-map
created: 2026-06-18
updated: 2026-06-18
status: candidate/controller-verification-required
claim_ceiling: source-backed constraint-tier map; not formal derivation proof, not full runtime verification, not Codex Ratchet implementation proof
---

# Lev Five Constraints vs F01/N01

## Bottom line

Current Leviathan sources carry two overlapping views:

1. **North Star view:** Lev lists five kernel constraints: C1 Finitude, C2 Non-Commutation, C3 Nominalized Reality, C4 Ratchet, C5 Locality. Source: `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md:119-129`.
2. **FlowMind/kernel tiering view:** C1/F01 and C2/N01 are root axioms; C3-C5 are governance assumptions with derivation paths tracked for future promotion. Sources: `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:5-7`, `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts:1-12`, `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/schemas/system-flowmind.schema.yaml:276-357`.

This page preserves both without smoothing them into a stronger claim. For Josh/root-constraint mapping, treat **C1/F01** and **C2/N01** as the supported root pair. Treat **C3/C4/C5** as derived/aligned governance constraints unless a later repo source proves them as independent root axioms.

## Mapping table

| Lev constraint | Root/derived treatment for this wiki | F01/N01 relation | Leviathan repo support | Support label | Guardrail |
|---|---|---|---|---|---|
| C1 — Finitude | Root where current FlowMind sources support it. | Directly maps to `F01_FINITUDE`. | `core/flowmind/system/constraint-manifold.flow.yaml:36-47`; `core/flowmind/src/kernel/constraint-manifold.ts:58-123`; `docs/design/proposal-flowmind-system.md:123-135` | observed config + observed code + design | Good evidence for native validator surface; not proof every runtime path invokes it. |
| C2 — Non-Commutation | Root where current FlowMind sources support it. | Directly maps to `N01_NONCOMMUTATION`. | `core/flowmind/system/constraint-manifold.flow.yaml:49-59`; `core/flowmind/src/kernel/constraint-manifold.ts:130-248`; `docs/design/proposal-flowmind-system.md:136-146` | observed config + observed code + design | Good evidence for DAG/order validator surface; not proof every planner/orchestrator route uses it. |
| C3 — Nominalized Reality | Derived/aligned governance assumption. | Aligned with F01/N01 through finite named/canonical artifacts and order-dependent naming, but not a root in current FlowMind tiering. | `core/flowmind/system/constraint-manifold.flow.yaml:65-79`; `docs/design/proposal-flowmind-system.md:148-163`; `core/flowmind/schemas/system-flowmind.schema.yaml:313-357` | observed config + design + schema | North Star lists it as kernel DNA, but FlowMind tiering says governance/assumed; do not call it independent root. |
| C4 — Ratchet | Derived/aligned governance assumption plus separate ratchet-admission contract. | Aligned with F01+N01 through bounded state space + path-dependent selection; also implemented partly as admission irreversibility. | `core/flowmind/system/constraint-manifold.flow.yaml:81-94`; `core/flowmind/system/ratchet-admission.flow.yaml:19-24, 152-160`; `crates/lev-kernel/src/ratchet.rs:29-43, 57-82` | observed config + observed Rust code | Do not import Codex Ratchet sim/math proof as Lev proof. Rust admission checks evidence presence and admitted IDs; it is not the whole 7-stage pipeline. |
| C5 — Locality | Derived/aligned governance assumption. | Aligned mainly with F01 through finite probe/scope bounds; also operationally aligned with scoped authority/no ambient access. | `core/flowmind/system/constraint-manifold.flow.yaml:96-109`; `docs/design/proposal-flowmind-system.md:179-193`; `crates/lev-kernel/src/manifold.rs:20-23` | observed config + design + Rust enum | Do not claim independent root status unless promoted by explicit repo evidence. |

## Why C1/F01 is a supported root mapping

`/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:36-47` declares:

- `C1_finitude`
- `id: F01_FINITUDE`
- `tier: root_axiom`
- `configurable: false`
- `derivation: null`
- finite explicit encoding, finite plan policy, and no unbounded alphabets

`/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts:58-123` implements `validateFinitude(context)` with checks for:

- execution bounds via `plan.policy.max_turns` or `plan.policy.max_time_ms`;
- explicit encodings for structures;
- positive finite sizes where sizes are declared.

Safe claim:

```text
Leviathan currently has a FlowMind/System FlowMind declaration and TypeScript validator for C1 as `F01_FINITUDE`, with finitude treated as a non-configurable root axiom in that surface.
```

## Why C2/N01 is a supported root mapping

`/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:49-59` declares:

- `C2_non_commutation`
- `id: N01_NONCOMMUTATION`
- `tier: root_axiom`
- `configurable: false`
- `derivation: null`
- dependency DAGs, explicit order, and order-sensitive composition

`/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts:130-248` implements `validateNonCommutation(context)` with checks for:

- dependency references resolving to declared step IDs;
- duplicate step IDs as order ambiguity;
- Kahn topological sort / cycle detection.

Safe claim:

```text
Leviathan currently has a FlowMind/System FlowMind declaration and TypeScript validator for C2 as `N01_NONCOMMUTATION`, with non-commutation treated as a non-configurable root axiom in that surface.
```

## Why C3-C5 stay derived/aligned here

The decisive repo-current tiering evidence is:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:61-64` labels C3-C5 as “Governance Assumptions” and says derivation paths are tracked for future promotion.
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:65-109` gives C3-C5 `tier: governance`, `status: assumed`, and `configurable: true`.
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/schemas/system-flowmind.schema.yaml:313-357` defines `governance_assumptions` as governance rules used by the constraint manifold, with status either `assumed` or `derived_canon`, where `assumed` means enforced but not yet proven from C1+C2.
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-system.md:113-115` explicitly says Josh's Thread B bootpack starts with exactly two initial terms, `F01_FINITUDE` and `N01_NONCOMMUTATION`, and says C3-C5 are governance rules “we believe are true but haven't yet proven from C1+C2.”

Therefore the current wiki treatment is:

```text
C3, C4, and C5 are present and important in Leviathan. They are aligned with Josh's root-constraint doctrine and are enforced/declared in current System FlowMind surfaces, but current FlowMind tiering does not make them independent roots.
```

## North Star tension preserved

`/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md:119-129` says five non-negotiable kernel constraints govern every execution and calls them the system's DNA. That is a high-signal vision/current-doc statement, but it does not erase the more precise tiering in the FlowMind constraint declaration, TypeScript validator, schema, and FlowMind system proposal.

A safe synthesis is:

```text
Lev's North Star names five kernel constraints. The current FlowMind constraint surfaces split those five into two root axioms (C1/F01, C2/N01) plus three governance assumptions (C3-C5) with derivation/promotion paths.
```

## Rust kernel note

The Rust kernel currently has a five-kind enum:

- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/manifold.rs:11-24` defines `ConstraintKind::{Finitude, NonCommutation, NominalizedReality, Ratchet, Locality}`.
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/manifold.rs:78-85` describes a constraint enforcement kernel integrating policy evaluation, declaration management, and ratchet admission.
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs:29-43` defines admission irreversibility: once admitted, a declaration cannot be un-admitted/revoked.

Support label: **observed Rust code surface**. Claim ceiling: enum and simple ratchet admission are not full semantic enforcement of all five constraints.

## Wiki doctrine bridge status

`/Users/joshuaeisenhart/wiki/wizard/harness-consolidated/14_leviathan_os_constraint_map.md:11-23` maps Lev's five listed constraints to two roots plus three derived consequences:

- C1 ↔ F01 root;
- C2 ↔ N01 root;
- C3 derived from finitude / nominalist doctrine;
- C4 derived from finitude + non-commutation;
- C5 derived from finitude / probe-relative scope.

Support label: **wiki doctrine bridge / alignment**, not repo implementation proof. Use it to guide interpretation, not to override repo-current files.

## Overclaim guards

Do not say:

- “Leviathan proves Codex Ratchet.”
- “Codex Ratchet simulations are implemented in Leviathan.”
- “C3-C5 are independent roots in Leviathan.”
- “Every Leviathan execution is verified against the manifold.”
- “The 7-stage ratchet admission pipeline is fully implemented.”

Safe short form:

```text
C1/F01 and C2/N01 are the supported root pair in current FlowMind constraint sources. C3-C5 are present as declared governance constraints and doctrine-aligned derived consequences, with future promotion paths tracked in the repo.
```

## Source index

| Source path | Lines used | Support label |
|---|---:|---|
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md` | 119-129 | observed current doc / five-constraint North Star |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-system.md` | 111-197 | design/provenance / explicit two-root tiering |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml` | 5-7, 36-109, 140-155 | observed System FlowMind declaration |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts` | 1-19, 58-123, 130-248, 278-345 | observed TypeScript validator |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/schemas/system-flowmind.schema.yaml` | 276-357 | observed schema tiering |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/ratchet-admission.flow.yaml` | 19-24, 31-44, 114-160 | observed System FlowMind ratchet-admission contract |
| `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/manifold.rs` | 11-24, 78-85 | observed Rust enum/kernel surface |
| `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs` | 29-43, 57-82, 110-141 | observed Rust ratchet admission code/tests |
| `/Users/joshuaeisenhart/wiki/wizard/harness-consolidated/14_leviathan_os_constraint_map.md` | 11-23, 50-54 | wiki doctrine bridge / not implementation proof |
