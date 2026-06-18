---
title: Leviathan Current Wiki Project
created: 2026-06-17
updated: 2026-06-17
type: project-front-door
status: active scaffold / early intake
claim_ceiling: wiki routing and current-repo orientation; not full synthesis, not implementation proof, not maintainer acceptance
sources:
  - /Users/joshuaeisenhart/GitHub/leviathan/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md
  - /Users/joshuaeisenhart/wiki/wizard/harness-consolidated/14_leviathan_os_constraint_map.md
  - /Users/joshuaeisenhart/wiki/projects/levos/levos-dev-handoff-product-and-runtime-2026-06-15.md
  - /Users/joshuaeisenhart/wiki/projects/leviathan-current/source-inventory-2026-06-17.md
tags:
  - leviathan
  - lev-os
  - levos
  - runtime
  - wiki-project
---

# Leviathan Current Wiki Project

## Purpose

This folder is the current wiki project for understanding `lev-os/leviathan` as it exists on disk now.

It should answer four questions without forcing Josh to re-explain the project:

1. What is Lev / Leviathan?
2. What currently exists in the repo?
3. What is intended but not yet landed?
4. How do Josh's root constraints and JP Smith's Lev runtime architecture relate without collapsing into one another?

## Current bottom line

Observed from current repo docs: Lev is an open runtime for agent-human systems: agents act through real surfaces, under explicit policy, graph memory, auditable events, execution boundaries, and human approval surfaces.

The active repo docs describe the foundation as real but still being hardened. They explicitly say the universal context graph is not fully landed, the system is not enterprise-ready, and architecture is ahead of some implementation areas.

## Current repo authority order

For this project, read current repo sources before chat-derived or legacy material:

1. `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/` — normative contracts.
2. `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md` — canonical topology and ownership boundaries.
3. `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md` — current execution state.
4. `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md` and root `README.md` — vision and product frame.
5. `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/` — rationale and deeper design reference.
6. `/Users/joshuaeisenhart/GitHub/leviathan/docs/_inbox/`, `_archive/`, chats, transcripts, and older LevOS wiki notes — source material / provenance, not current implementation truth by default.

## Key current source artifacts

### Front door / control

- `read-first.md` — project boot note for future agents.
- `source-inventory-2026-06-17.md` — first repo inventory; 12,699 files excluding common build/cache dirs; 4,848 Markdown/MDX files; 250 chat/transcript/Josh-JP routing candidates captured in the JSON sidecar.
- `source-inventory-2026-06-17.json` — full machine-readable inventory sidecar.
- `bounded-ingestion-plan.md` — finite packet plan for turning the repo into wiki pages.
- `worker-swarm-plan-2026-06-17.md` — first bounded worker-wave plan.
- `concept-map-start.md` — first current concept map with strict claim ceilings.

### Packet 1 — current authority docs

- `what-is-leviathan.md` — plain-English current-authority synthesis.
- `current-state-and-roadmap.md` — status/roadmap synthesis with open gaps preserved.
- `architecture-planes-and-ownership.md` — four-plane/runtime ownership map.
- `contract-surface-map.md` — normative specs/contract map plus drift findings.
- `packet-1-processing-receipt-2026-06-17.md` — bounded processing receipt for this tranche.

### Packet 2 — runtime/module map

- `runtime-module-map-start.md` — package/workspace and core module starter map.
- `flowmind-control-plane-start.md` — FlowMind control-plane starter map.
- `event-graph-orchestration-start.md` — Event Bus / Graph / Orchestration starter map.
- `flowmind-control-plane.md` — FlowMind source/package control-plane map.
- `graph-state-knowledge-plane.md` — Graph state/knowledge ownership map.
- `event-bus-causality-plane.md` — Event Bus causality spine map; runtime health blocked by conflict markers.
- `orchestration-execution-plane.md` — Orchestration DAG/loop/queue execution-plane map.
- `exec-poly-daemon-boundary.md` — Exec / Poly / Daemon ownership split.
- `plugin-ownership-map.md` — plugin inventory, registration, and ownership map.
- `packet-2-runtime-map-receipt-2026-06-17.md` — bounded receipt and verification notes for this tranche.

### Contribution / provenance / research / assessment starters

- `josh-contribution-signal-radar.md` — grounded starter radar for Josh's constraint contributions in docs/code.
- `josh-contribution-signal-index-2026-06-17.md` — broader controller-generated signal index after contribution-worker route failure.
- `chat-provenance-queue-2026-06-17.md` — classified queue for 250 chat/transcript/handoff candidates.
- `research-connection-map-start.md` — starter map of research-connected repo surfaces.
- `doing-well-failing-promising-start.md` — first assessment of strengths, failures, promise, and falsifiers.

## Existing related wiki surfaces

- `projects/levos/levos-gpt-webui-idea-ledger-2026-06-15.md` — processed GPT WebUI ideas; useful, not repo-current proof.
- `projects/levos/levos-dev-handoff-product-and-runtime-2026-06-15.md` — product/runtime framing; useful as a handoff draft, not repo contract.
- `projects/levos/levos-gpt-webui-representation-audit-2026-06-15.md` — coverage ledger for earlier idea intake.
- `wizard/harness-consolidated/14_leviathan_os_constraint_map.md` — constraint bridge between Lev terms and Josh/Codex Ratchet terms.

## Claim discipline

Do not say the wiki fully understands Leviathan yet. Current status is: scaffold exists, first inventory exists, Packet 1 current-authority synthesis pages exist, and Packet 2 source-map pages exist. Runtime verification remains open because Event Bus has unresolved conflict markers and Packet 2 did not run package tests/typechecks.

The live synthesis must keep three layers separate:

- **repo-current implementation and contracts** — what files and tests say now;
- **JP/Lev-dev intent** — what the Lev docs and chat/source material say the system is trying to become;
- **Josh/root-constraint contribution** — finitude, non-commutation, nominalist reality, ratchet, locality, and the broader constraint/admissibility doctrine.
