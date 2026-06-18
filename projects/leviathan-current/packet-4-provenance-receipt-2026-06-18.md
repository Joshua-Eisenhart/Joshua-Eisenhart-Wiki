---
title: Packet 4 Provenance Receipt — Josh / JP Ledger Pass 1
created: 2026-06-18
type: processing-receipt
status: complete
claim_ceiling: process receipt; not provenance synthesis beyond linked ledger
repo_root: /Users/joshuaeisenhart/GitHub/leviathan
repo_head_checked: a661ecbf410469becd7b89c3bfc5ee215721ae34
---

# Packet 4 Provenance Receipt — Josh / JP Ledger Pass 1

## Task

Create a quote/source-level provenance ledger for Josh / Joshua Eisenhart and JP Smith in current LevOS / Leviathan, matched to repo-current surfaces, with support levels and overclaim guards.

## Files created

- `provenance-ledger-josh-jp-pass-1-2026-06-18.md`
- `packet-4-provenance-receipt-2026-06-18.md` (this receipt)

No files under `/Users/joshuaeisenhart/GitHub/leviathan` were edited.

## Required project files read

- `read-first.md`
- `README.md`
- `josh-contribution-signal-radar.md`
- `josh-contribution-signal-index-2026-06-17.md`
- `model-pressure/fusion-glm-wiki-direction-2026-06-18.md`

Additional current wiki context read:

- `chat-provenance-queue-2026-06-17.md`
- `source-inventory-2026-06-17.md`
- `contract-surface-map.md`
- `runtime-module-map-start.md`
- `flowmind-control-plane.md`

## Repo sources read / sampled

Primary current docs and design/provenance surfaces:

- `/Users/joshuaeisenhart/GitHub/leviathan/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/design-flowmind.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-system.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-ratchet.md`

Current code/config surfaces:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/ratchet-admission.flow.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/scheduler.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/manifold.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs`

Chat/session-provenance surface:

- `/Users/joshuaeisenhart/GitHub/leviathan/.lev/pm/handoffs/20260220-flowmind-ratchet-harness.md`

## Verification / repo status check

Read-only command run:

```text
git -C /Users/joshuaeisenhart/GitHub/leviathan rev-parse HEAD
```

Returned:

```text
a661ecbf410469becd7b89c3bfc5ee215721ae34
```

Read-only status check showed pre-existing non-clean state:

```text
 m apps/nanoclaw
 m community/agentguard
 m community/agentping
 m community/lev-content
 D docs/vernacular.md
 M plugins/prompt-stack/vendors/jeffreysprompts.com
```

This packet did not touch those repo paths.

## What the ledger accomplished

The ledger created 35 rows with the required fields:

- source path;
- quote or exact phrase;
- actor attribution if present;
- concept;
- current repo surface it maps to;
- support level;
- overclaim guard.

The rows separate:

1. **Explicit Josh attribution** — especially `docs/NORTH_STAR.md:190-200`, which says Josh identified the ontological/operational constraint-system unification.
2. **Explicit Josh/JP role-boundary design language** — especially `docs/design/proposal-flowmind-system.md` and `docs/design/proposal-flowmind-ratchet.md` where Josh is named as constraint scientist/spec lane and JP as engine builder/runtime lane.
3. **Current repo surfaces** — FlowMind package, System FlowMind YAML declarations, C1/C2 TypeScript validator, Rust `lev-kernel` manifold/ratchet, Exec SDK, Orchestration scheduler, Architecture/Roadmap ownership/current-state docs.
4. **Chat/handoff claims** — `.lev/pm/handoffs/20260220-flowmind-ratchet-harness.md` retained as provenance only, never as current repo truth.
5. **Model-pressure influence** — included only as methodology pressure, not evidence for contribution claims.

## Main findings

- The strongest Josh evidence is an explicit current-doc attribution in `docs/NORTH_STAR.md`: Josh identified the unification of ontological constraints (`ratchet`, `finitude`, `non-commutation`) with operational constraints (`ABAC`, `leases`, `containment`) in a declarative substrate.
- The strongest Josh/JP boundary evidence is in current design docs: Josh is framed as **Constraint Scientist** / spec lane; JP is framed as **Engine Builder** / FlowMind engine lane.
- Current repo surfaces do encode the same constraint vocabulary: C1/C2 as root axioms, C3-C5 as governance assumptions, ratchet admission, FlowMind System FlowMinds, Rust kernel constraint kinds, and forward-only ratchet admission.
- The implementation surface is uneven by claim tier: some pieces are code/config-present, while richer ratchet-admission language remains contract/design relative to the simpler Rust `RatchetAdmission` implementation.
- JP-specific current-code authorship is not directly proven by most current files; the safe claim is that design/provenance docs attribute the engine-builder role to JP, while repo-current code/docs expose the runtime surfaces matching that lane.

## Guardrails preserved

- Did not promote chat/handoff claims to repo truth.
- Did not treat old/legacy docs as current authority.
- Did not say Josh authored the repo implementation.
- Did not collapse Leviathan into Codex Ratchet.
- Did not collapse JP's runtime implementation lane into Josh's math/proof/admissibility lane.
- Did not claim full ratchet implementation; preserved contract-vs-implementation caveats.
- Did not edit the Leviathan repo.

## Issues / limitations

- `josh-contribution-signal-index-2026-06-17.md` has very long lines; it had to be read in chunks.
- `josh-flowmind-spec.zip` and raw Josh ratchet source files were not opened in this pass; rows that mention them are sourced only from repo design/handoff claims and marked with guards.
- No package tests, typechecks, or runtime smoke tests were run; this was a wiki provenance pass, not a runtime-verification packet.
- Repo worktree was already dirty when checked; no attempt was made to clean or modify it.

## Next recommended packet

Create a focused `josh-jp-provenance-boundary.md` only after either:

1. direct owner confirmation, or
2. a bounded source-owner pass over the raw Josh ratchet archive / `josh-flowmind-spec.zip`, with each raw-source citation separately classified.

Until then, cite the new ledger for guarded provenance rows and cite repo-current docs/code for runtime truth.
