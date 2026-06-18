---
title: Codex Ratchet vs Leviathan Boundary
created: 2026-06-18
updated: 2026-06-18
type: boundary-map
status: candidate/controller-verification-required
claim_ceiling: boundary synthesis only; not Codex Ratchet proof, not Leviathan implementation proof, not final attribution adjudication
---

# Codex Ratchet vs Leviathan Boundary

Leviathan contains many Josh ideas but is NOT Codex Ratchet.

This page is the Packet 4 non-collapse boundary. It explains how Josh/root-constraint doctrine can be mapped into current Leviathan evidence while preserving the difference between a mathematical/provenance/admissibility kernel lane and a running agent-human runtime lane.

## One-sentence boundary

```text
Codex Ratchet / Josh-root constraints are the mathematical and admissibility doctrine lane; Leviathan / LevOS is the agent-human runtime lane; FlowMind Ratchet Harness is bridge language between them, not identity.
```

## Safe bridge statement

```text
Codex Ratchet works on the mathematical/proof/admissibility kernel. Leviathan applies related constraint structure as a running agent-human runtime through FlowMind, orchestration, graph state, event causality, execution boundaries, and human-loop surfaces.
```

Use the bridge as a map. Do not use it as proof.

## Boundary table

| Dimension | Codex Ratchet / Josh-root lane | Leviathan / Lev lane | Bridge surface | What not to infer |
|---|---|---|---|---|
| Object type | Constraint doctrine, proof/admissibility kernel, ratchet semantics, F01/N01 root terms. | Open runtime for agent-human systems. | FlowMind constraint manifold and ratchet admission. | Do not infer Lev implements every Codex Ratchet proof/simulation. |
| Primary evidence in this packet | Wiki doctrine bridge and current Lev docs naming Josh/root constraints. | Current Lev repo docs, specs, code/config surfaces. | `proposal-flowmind-system.md`, `proposal-flowmind-ratchet.md`, `constraint-manifold.flow.yaml`. | Do not let doctrine bridge override repo-current implementation state. |
| Root constraints | F01 finitude and N01 non-commutation as primitive root pair in the doctrine bridge. | C1/F01 and C2/N01 as root axioms in FlowMind constraint sources. | `core/flowmind/system/constraint-manifold.flow.yaml:36-59`; `core/flowmind/src/kernel/constraint-manifold.ts:18-19`. | Do not promote C3-C5 to independent roots unless repo source does. |
| Ratchet | Mathematical/admissibility ratchet and proof discipline. | Ratchet appears as C4 governance and as admission/irreversibility surfaces. | `core/flowmind/system/ratchet-admission.flow.yaml`; `crates/lev-kernel/src/ratchet.rs`. | Do not import Codex Ratchet sim/math proof as Lev implementation proof. |
| Runtime | Not the whole Lev runtime. | FlowMind, Orchestration, Graph, Event Bus, Exec, Poly, Daemon, AgentPing/AgentLease direction. | FlowMind hosts external constraint systems via ratchet harness. | Do not collapse JP/Lev architecture into “just Josh's ideas.” |
| Attribution | Explicit Josh contribution signal for constraint unification. | JP/Lev-dev runtime implementation lane; docs frame JP as engine builder in design/provenance surfaces. | “FlowMind is the socket; ratchet is the chip.” | Do not infer current-code authorship from conceptual attribution. |

## Repo-current Leviathan identity

Leviathan's repo front door defines it as an open runtime for agent-human systems:

- `/Users/joshuaeisenhart/GitHub/leviathan/README.md:17-28` says Leviathan is not just a prompt wrapper or chat tool; it is a runtime model for agents that act through surfaces, operate under policy/control, remember/classify context, emit auditable events, and compose into ecosystems/products.
- `/Users/joshuaeisenhart/GitHub/leviathan/README.md:31-41` summarizes three core planes: FlowMind as control/policy plane, Graph as state/knowledge plane, Event Bus as causality spine.
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md:21-27` says Lev compiles and validates workflow declarations through FlowMind, executes them through Orchestration, routes/persists runtime events through Event Bus, runs bindings through Poly, and extends behavior through plugins.
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md:151-179` maps runtime ownership across FlowMind, Event Bus, Graph, Orchestration, Exec, Poly/Daemon, plugins, and UI.

Support label: **repo-current docs / architecture**. Claim ceiling: this is current stated architecture, not proof that every plane is fully production-ready.

## Current-state guardrails from repo docs

Leviathan is not finished/enterprise-proven:

- `/Users/joshuaeisenhart/GitHub/leviathan/README.md:43-63` says the foundation is real but the universal context graph is not fully landed, the system is not fully enterprise-ready, and architecture is ahead of some implementation areas.
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md:14-31` gives “honest accounting,” including 0/9 enterprise pillars enterprise-ready, security gaps, DX gaps, dependency vulnerabilities, and a docs-to-code ratio gap.
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md:91-106` says several SDLC/runtime pieces are done, but declared topology switching is partial and enforcement/budget/resource areas are planned or not wired.

Support label: **repo-current roadmap/status**. Claim ceiling: do not call Lev enterprise-ready or fully enforced.

## Josh-root contribution boundary

The strongest explicit current-doc Josh signal is:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md:190-200` states that Josh identified two orthogonal constraint systems — ontological constraints (`ratchet`, `finitude`, `non-commutation`) and operational constraints (`ABAC`, `leases`, `containment`) — unified in one declarative substrate.

Design/provenance docs provide a stronger role-boundary frame:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-system.md:35-47` names Josh as “Constraint Scientist” and JP as “Engine Builder,” says Josh built the spec, JP built the engine, and frames FlowMind as socket / ratchet as chip.
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-ratchet.md:27-36` repeats the two-person/two-system frame and says the ratchet harness is the binding contract between them.
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-ratchet.md:362-379` marks the ratchet harness component statuses as designed/gap-identified and notes review status, which prevents overclaiming implementation completion.

Support label: **explicit attribution + design/provenance**. Claim ceiling: strong contribution/provenance signal, not implementation authorship proof.

## Constraint bridge boundary

Current repo support for C1/C2 is stronger than for C3-C5 as roots:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml:5-7` says C1/C2 are root axioms and C3-C5 are governance assumptions.
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts:1-12` says the TypeScript native evaluator enforces C1/C2 as two irreducible root axioms and that C3-C5 governance assumptions live elsewhere.
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/schemas/system-flowmind.schema.yaml:276-357` distinguishes root axioms from governance assumptions, with `assumed` vs `derived_canon` status.
- `/Users/joshuaeisenhart/wiki/wizard/harness-consolidated/14_leviathan_os_constraint_map.md:11-23` maps C1/C2 to F01/N01 roots and treats C3-C5 as derived consequences; this is a wiki doctrine bridge, not repo implementation proof.

Safe short form:

```text
Leviathan's current FlowMind constraint surfaces support C1/F01 and C2/N01 as roots. C3-C5 are important Lev constraints, but this wiki marks them derived/aligned governance constraints unless current repo evidence promotes them.
```

## Do-not-import rule

Codex Ratchet proof/sim/math claims do not become Leviathan implementation claims by analogy.

Allowed:

- “This Lev surface uses the same term.”
- “This Lev config declares C1/F01 or C2/N01.”
- “This design doc frames FlowMind as a ratchet harness.”
- “This is aligned with the Josh/Codex Ratchet root-constraint doctrine.”

Not allowed:

- “Therefore Lev has proved the Codex Ratchet math.”
- “Therefore every Lev execution is constraint-complete.”
- “Therefore Codex Ratchet simulations are implemented in Lev.”
- “Therefore JP's runtime is just Codex Ratchet.”
- “Therefore Josh authored the current Lev implementation.”

## Layered safe claims

| Claim | Safe? | Why |
|---|---:|---|
| Current Lev docs explicitly attribute constraint-system unification to Josh. | Yes | Supported by `docs/NORTH_STAR.md:190-200`. |
| Current FlowMind sources declare C1/F01 and C2/N01 as root axioms. | Yes | Supported by `constraint-manifold.flow.yaml`, TS validator, schema, and design proposal. |
| Current Lev sources contain C3/C4/C5 as constraint vocabulary. | Yes | Supported by North Star, YAML governance assumptions, schema, and Rust enum. |
| C3/C4/C5 are independent roots in Lev. | No / not yet | Current FlowMind tiering marks them governance/assumed or derived-canon candidates. |
| Lev's ratchet admission is the full Codex Ratchet implementation. | No | Current System FlowMind contract is rich; Rust implementation is much simpler; no Codex proof import. |
| Leviathan is Codex Ratchet. | No | Leviathan is a runtime with multiple planes and product surfaces; bridge is not identity. |

## Source index

| Source path | Lines used | Support label |
|---|---:|---|
| `/Users/joshuaeisenhart/GitHub/leviathan/README.md` | 17-28, 31-63 | repo-current front door / status guardrail |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/README.md` | 49-59 | docs authority order |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md` | 21-27, 41-56, 89-94, 151-179 | repo-current architecture / ownership |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md` | 14-31, 91-106 | repo-current current-state guardrails |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md` | 119-129, 190-200 | current-doc constraint manifold / explicit Josh attribution |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-system.md` | 35-47, 111-197 | design/provenance / Josh-JP role split / C1-C2 tiering |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-ratchet.md` | 27-36, 79-86, 97-119, 362-379 | design/provenance / boundary / status caveat |
| `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/design-flowmind.md` | 63-72, 388-416, 420-436 | FlowMind boundary / ratchet hosting / conflict guardrails |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml` | 5-15, 36-109 | observed System FlowMind declaration |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts` | 1-19, 58-123, 130-248, 278-345 | observed TypeScript evaluator |
| `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/ratchet-admission.flow.yaml` | 19-24, 31-44, 114-160 | observed ratchet-admission contract |
| `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs` | 29-43, 57-82 | observed Rust ratchet code |
| `/Users/joshuaeisenhart/wiki/wizard/harness-consolidated/14_leviathan_os_constraint_map.md` | 11-23, 50-54 | wiki doctrine bridge / alignment only |
