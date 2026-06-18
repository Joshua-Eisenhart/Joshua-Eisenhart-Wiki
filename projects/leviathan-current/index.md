---
title: Leviathan Current Content Index
created: 2026-06-18
updated: 2026-06-18
type: project-index
status: active
claim_ceiling: content map and reading order; not implementation proof
---

# Leviathan Current Content Index

This is the human-facing entrypoint for the current `lev-os/leviathan` wiki work.

The content exists under `projects/leviathan-current/`. The strongest pages are source-grounded maps and explanations; the receipt pages are there to show what was read, what was blocked, and what was not proven.

## Current reset point

Start with the clean-current audit before reading older Packet 2 runtime pages:

1. [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]] — current clean snapshot audit at `c90ec8499c83db3d17f6132ec734698a8de2dbce`.
2. [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]] — what older wiki pages still say that is now historical damaged-checkout evidence, not current upstream truth.
3. [[projects/leviathan-current/concept-atlas-current-2026-06-18]] — current concept atlas with aliases, evidence levels, wiki targets, and claim ceilings.
4. [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]] — contradictions/blockers that should not be smoothed into a single verdict.
5. [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]] — clean-clone command proof audit that splits the `ROADMAP.md` vs `mvp.md` conflict.
6. [[projects/leviathan-current/read-order-by-intent-2026-06-18]] — safer read order by task/persona for a massive mixed repo.
7. [[projects/leviathan-current/wizard-swarm-current-wiki-receipt-2026-06-18]] — route/worker/verification receipt for the first current rebuild pass.

## Start here

1. [[projects/leviathan-current/what-is-leviathan]] — plain-English explanation of what Lev / Leviathan is.
2. [[projects/leviathan-current/current-state-and-roadmap]] — current status, strengths, gaps, and roadmap.
3. [[projects/leviathan-current/architecture-planes-and-ownership]] — FlowMind, Orchestration, Graph, Event Bus, Exec, Poly, Daemon, AgentPing ownership map.
4. [[projects/leviathan-current/contract-surface-map]] — specs and contract surfaces, with drift preserved.
5. [[projects/leviathan-current/runtime-module-map-full-2026-06-18]] — older full runtime/module map. Read through the drift audit above because its conflict-marker language is now historical.

## Runtime maps

- [[projects/leviathan-current/flowmind-control-plane]]
- [[projects/leviathan-current/graph-state-knowledge-plane]]
- [[projects/leviathan-current/event-bus-causality-plane]]
- [[projects/leviathan-current/orchestration-execution-plane]]
- [[projects/leviathan-current/exec-poly-daemon-boundary]]
- [[projects/leviathan-current/plugin-ownership-map]]
- [[projects/leviathan-current/runtime-build-test-surface-map-2026-06-18]]

Starter/earlier maps:

- [[projects/leviathan-current/runtime-module-map-start]]
- [[projects/leviathan-current/flowmind-control-plane-start]]
- [[projects/leviathan-current/event-graph-orchestration-start]]

## Product and human-loop surfaces

- [[projects/leviathan-current/agentping-human-loop-surfaces]]
- [[projects/leviathan-current/agentlease-scoped-authority]]

## Josh / JP / constraint boundary

- [[projects/leviathan-current/josh-root-constraints-in-leviathan]]
- [[projects/leviathan-current/lev-five-constraints-vs-f01-n01]]
- [[projects/leviathan-current/codex-ratchet-vs-leviathan-boundary]]
- [[projects/leviathan-current/provenance-ledger-josh-jp-pass-1-2026-06-18]]
- [[projects/leviathan-current/josh-contribution-signal-radar]]
- [[projects/leviathan-current/josh-contribution-signal-index-2026-06-17]]

## Chat and provenance processing

- [[projects/leviathan-current/chat-evidence-promotion-protocol]]
- [[projects/leviathan-current/chat-tranche-1-processing-2026-06-18]]
- [[projects/leviathan-current/chat-provenance-queue-2026-06-17]]

## Assessment and research pages

- [[projects/leviathan-current/research-connection-map-start]]
- [[projects/leviathan-current/doing-well-failing-promising-start]]
- [[projects/leviathan-current/concept-map-start]]
- [[projects/leviathan-current/concept-atlas-current-2026-06-18]]
- [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]]
- [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]]
- [[projects/leviathan-current/read-order-by-intent-2026-06-18]]

## Control, plans, and receipts

- [[projects/leviathan-current/read-first]]
- [[projects/leviathan-current/README]]
- [[projects/leviathan-current/bounded-ingestion-plan]]
- [[projects/leviathan-current/source-inventory-2026-06-17]]
- [[projects/leviathan-current/worker-swarm-plan-2026-06-17]]
- [[projects/leviathan-current/wiki-swarm-launch-receipt-2026-06-18]]
- [[projects/leviathan-current/ratchet-working-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-1-processing-receipt-2026-06-17]]
- [[projects/leviathan-current/packet-2-runtime-map-receipt-2026-06-17]]
- [[projects/leviathan-current/packet-2-full-runtime-map-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-3-product-surfaces-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-4-provenance-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-4-constraint-boundary-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-5-chat-tranche-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-6-concept-atlas-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-7-clean-clone-proof-audit-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-8-wizard-mass-swarm-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-9-external-upgrade-report-intake-2026-06-18]]

## Source mode

New wiki work reads `https://github.com/lev-os/leviathan` plus raw/API URLs first. If that is too limited, use a clean fresh clone from `https://github.com/lev-os/leviathan.git`, record the remote URL, commit SHA, and clean status, and keep it read-only unless Josh explicitly assigns a repo patch.

Current clean-clone baseline for this index: `/tmp/leviathan-wiki-src-20260618` at `c90ec8499c83db3d17f6132ec734698a8de2dbce`, clean status. The damaged `/Users/joshuaeisenhart/GitHub/leviathan` checkout is historical only.
