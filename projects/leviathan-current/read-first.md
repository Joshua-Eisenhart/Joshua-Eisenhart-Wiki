---
title: Leviathan Current Read First
created: 2026-06-17
updated: 2026-06-17
type: read-first
status: active scaffold
claim_ceiling: routing note; not full conceptual synthesis
---

# Read First — Leviathan Current

## Why this project exists

Josh needs a wiki that can understand current Leviathan: what it is, what it can do, what it intends to do, what it could do, and how much of Josh's constraint doctrine is inside it.

This project exists because the repo is high-entropy: thousands of docs/code files, active submodules, source chats/transcripts, older LevOS/Leviathan material, and architecture that is partly ahead of implementation.

## First working definition

Observed from the current repo docs, Lev / Leviathan is a universal agent-human runtime. It turns intent into constrained, routed, auditable execution across surfaces.

Plain version:

```text
Lev is not just chat. It is a runtime where agents act through surfaces, under policy, with graph memory, receipts, leases, and event traces.
```

Current repo docs keep these planes separate:

- **FlowMind** — control and policy declarations.
- **Orchestration** — scheduling, worker coordination, execution strategy.
- **Graph** — state, knowledge, memory, traversal, lineage.
- **Event Bus** — canonical `LevEvent` spine, replay, audit.
- **Exec / Poly / Daemon** — execution SDK, bindings, process/runtime surfaces.
- **AgentPing** — human-loop surfaces.
- **AgentLease** — scoped authority and accountability, still partly product/roadmap depending on surface.

## The Josh / JP boundary

- Josh / Joshua Eisenhart: Codex Ratchet dev; supplied or shaped root constraints and the broader constraint-admissibility frame.
- JP Smith: Lev / LevOS developer; owns the Leviathan repo and runtime implementation lane.
- Leviathan contains many Josh ideas, but repo-current Lev is not the same object as Codex Ratchet.

Safe bridge statement:

```text
Codex Ratchet works on the mathematical/proof/admissibility kernel. Leviathan applies related constraint structure as a running agent-human runtime.
```

Do not collapse one into the other. Use the bridge as a map, not as proof.

## Constraint map

The wiki bridge currently maps Lev's five listed kernel constraints to two roots plus derived consequences:

- `C1 Finitude` ↔ `F01` root.
- `C2 Non-commutation` ↔ `N01` root.
- `C3 Nominalized reality` — derived from finitude / nominalist doctrine.
- `C4 Ratchet` — derived from finitude + non-commutation.
- `C5 Locality` — derived from finitude / probe-relative scope.

Use this map as doctrine alignment, not as implementation proof. For repo truth, read current Lev docs and code.

## Read order for future agents

1. This file.
2. `README.md` in this folder.
3. `/Users/joshuaeisenhart/GitHub/leviathan/docs/README.md`.
4. `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md`.
5. `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md`.
6. `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`.
7. `source-inventory-2026-06-17.md` here.
8. `bounded-ingestion-plan.md` here.
9. Existing `projects/levos/*.md` pages for prior idea intake.
10. Chat/transcript candidates only after provenance classification.

## Current status

- Repo checked at `/Users/joshuaeisenhart/GitHub/leviathan`.
- Remote checked: `https://github.com/lev-os/leviathan`.
- HEAD checked during initial inventory: `a661ecbf410469becd7b89c3bfc5ee215721ae34`.
- Dirty worktree observed: submodule changes and deleted `docs/vernacular.md`. This wiki pass did not mutate the repo.
- First inventory written: `source-inventory-2026-06-17.md` plus JSON sidecar.

## Do not

- Do not treat chat transcripts as implementation proof.
- Do not treat old LevOS product pages as current repo truth.
- Do not say `implemented`, `enterprise-ready`, or `canonical` unless current docs/code/tests earn that exact rung.
- Do not flatten Josh's root constraints into generic startup/product language.
- Do not flatten JP's runtime implementation work into Codex Ratchet math/proof work.
