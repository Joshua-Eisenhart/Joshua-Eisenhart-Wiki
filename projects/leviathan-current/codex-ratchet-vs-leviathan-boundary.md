---
title: Codex Ratchet vs Leviathan Boundary
created: 2026-06-18
updated: 2026-06-19
type: boundary-map
status: current-source-boundary
source_repo: lev-os/leviathan
source_snapshot: 5dd98ac4ce7afeb9e4351787179c60208de6d23f
claim_ceiling: boundary synthesis plus owner attribution correction; not Codex Ratchet proof; not Leviathan release proof; not final authorship adjudication for every code line
---

# Codex Ratchet vs Leviathan Boundary

Leviathan contains many Joshua Eisenhart ideas, but Leviathan is not Codex Ratchet.

Josh, Joshua Eisenhart, and the Codex Ratchet maker are the same person.

## One-Sentence Boundary

```text
Codex Ratchet is Joshua Eisenhart's mathematical/proof/admissibility project; Leviathan OS is JP Smith's agent-human runtime project; FlowMind ratchet-harness language is a bridge, not identity.
```

## Attribution Correction

Use this correction when reading older wiki pages:

- Codex Ratchet does not come from Leviathan OS.
- If Codex Ratchet and Leviathan converge on finitude, non-commutation, ratchet, nominalist/admissibility, QIT, or anti-hallucination structure, do not default to "Leviathan influenced Codex Ratchet."
- The safer default is Joshua-origin material entering Leviathan, independent convergence, or JP Smith's runtime architecture finding a compatible host for Joshua's constraints.
- The one explicit owner-acknowledged influence from JP/Leviathan into Joshua's side is the original Wizard idea.

## Safe Bridge Statement

```text
Codex Ratchet works on the mathematical/proof/admissibility kernel. Leviathan applies related constraint structure as a running agent-human runtime through FlowMind, orchestration, graph state, event causality, execution boundaries, and human-loop surfaces.
```

Use the bridge as a map. Do not use it as proof.

## Current Repo Evidence

### Leviathan Runtime Lane

Current repo docs frame Leviathan as an open runtime for agent-human systems. The technical architecture separates FlowMind, Orchestration, Graph, Event Bus, Exec, Poly, Daemon, UI, plugins, and human-loop surfaces.

Safe claim:

```text
Leviathan is a pre-release agent-human runtime project with real package surfaces and active hardening.
```

Unsafe claim:

```text
Leviathan is fully enterprise-ready or launch-ready.
```

### Joshua Constraint Lane

Current repo docs explicitly name Joshua's constraint role:

- `docs/design/proposal-flowmind-system.md` names Josh as "Constraint Scientist" and JP as "Engine Builder."
- `docs/design/proposal-flowmind-ratchet.md` frames Josh as constraint scientist and JP as engine builder, with FlowMind as socket and Josh's ratchet as chip.
- `docs/design/design-flowmind.md` says FlowMind hosts external constraint systems through the ratchet harness pattern, with Joshua's low-entropy ratchet as the canonical instance.

Current source also implements a narrow root-constraint validator:

- `core/eval/src/constraint-manifold.ts` defines and evaluates `F01_FINITUDE` and `N01_NONCOMMUTATION`.
- `core/flowmind/src/kernel/system-flowmind-loader.ts` binds the `constraint-manifold` System FlowMind to `createConstraintManifold` from `@lev-os/eval`.

Safe claim:

```text
Leviathan currently contains both Joshua-origin design/provenance material and a narrow implementation of F01/N01 validation in @lev-os/eval.
```

Unsafe claim:

```text
Leviathan implements all of Codex Ratchet.
```

### QIT / Engine Lane

Current repo evidence for Joshua-origin QIT/engine material:

- `docs/design/lev-qit-engine-glossary-eisenhart.md` is explicitly a Joshua Eisenhart glossary extracted from an iMessage corpus.
- `plugins/qit-engines/config.yaml` cites Joshua source lineage: iMessages, Codex Ratchet, and Josh wiki intake.
- `plugins/qit-engines/schemas/engine.schema.yaml` cites Josh Eisenhart as source for type1/type2 engine contracts.

Safe claim:

```text
Leviathan contains Joshua-origin QIT/engine vocabulary and plugin contract material.
```

Unsafe claim:

```text
The QIT engine plugin is a proven working runtime engine.
```

## Boundary Table

| Dimension | Codex Ratchet / Joshua lane | Leviathan / JP lane | Bridge surface | Do not infer |
|---|---|---|---|---|
| Project identity | Mathematical/proof/admissibility kernel. | Agent-human runtime / OS project. | FlowMind ratchet hosting. | Do not collapse one project into the other. |
| Root constraints | F01 finitude and N01 non-commutation as Joshua root terms. | C1/F01 and C2/N01 appear as System FlowMind roots and `@lev-os/eval` validators. | Constraint manifold. | Do not infer full Codex Ratchet proof import. |
| Ratchet | Proof/admissibility and monotone promotion discipline. | Runtime admission, audit, state transition, and governance vocabulary. | Ratchet admission / harness docs. | Do not call every Lev transition mathematically proven. |
| QIT/world model | Joshua-origin lawful-state/transformation research lane. | Repo has QIT glossary/config/schema and world-model product/design direction. | `plugins/qit-engines`, `core/world-model`, docs/design. | Do not call the QIT world engine product-proven. |
| Wizard | Codex Ratchet has its own Wizard lineage. | JP Smith supplied the original Wizard idea per owner correction. | Wizard concept influence. | Do not infer Codex Ratchet as Leviathan-derived. |
| Runtime implementation | Not the Leviathan runtime as a whole. | JP/Lev implementation lane: FlowMind, orchestration, graph, event bus, daemon, plugins. | Hosting/binding interfaces. | Do not erase JP's runtime authorship. |

## Do-Not-Import Rule

Codex Ratchet proof/sim/math claims do not become Leviathan implementation claims by analogy.

Allowed:

- "This Leviathan surface uses Joshua-aligned terms."
- "This Leviathan config declares C1/F01 or C2/N01."
- "This current code validates finite bounds and dependency DAGs."
- "This design doc frames FlowMind as a ratchet harness for Joshua's constraint system."
- "This QIT glossary/config/schema cites Joshua source material."

Not allowed:

- "Therefore Leviathan proves Codex Ratchet."
- "Therefore every Leviathan execution is constraint-complete."
- "Therefore Codex Ratchet simulations are implemented in Leviathan."
- "Therefore JP's runtime is just Joshua's system."
- "Therefore Codex Ratchet came from Leviathan."

## Current Source Split

At source snapshot `5dd98ac4ce7afeb9e4351787179c60208de6d23f`, the honest status is mixed:

- Root F01/N01 validator exists narrowly in `@lev-os/eval`.
- System FlowMind declarations load and are ordered.
- `system-flowmind-executor.ts` says YAML pipeline stages pass at boot in MVP because they are declarations, not runtime checks; runtime YAML rule interpretation is Phase 2+.
- `ROADMAP.md` and `mvp.md` still disagree about parts of current proof state.
- Full launch/enterprise/runtime proof is not settled by prose.

## Best Current Bridge

```text
Joshua contributed the constraint/admissibility/QIT/ratchet kernel ideas that Leviathan can host.
JP Smith contributed the Leviathan/FlowMind runtime architecture and the original Wizard idea that influenced Joshua's Wizard lineage.
Codex Ratchet remains Joshua's separate mathematical/proof/admissibility project, not a derivative of Leviathan OS.
```
