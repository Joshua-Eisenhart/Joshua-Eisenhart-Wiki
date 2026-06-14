---
title: Wizard v4.3 Read First
created: 2026-06-13
updated: 2026-06-13
packet: v4.3
type: read_first
framing: current
---

# Wizard v4.3 Read First

Current Wizard lives here: `~/wiki/wizard/packet-v4-3-current/`.

This packet is the shared core. It does not run any LLM by itself. After reading this file, load the native adaptation for the actual runtime:

- Hermes: `../hermes-version-current/`
- Claude Code: `../claude-version-current/`
- Codex: `../codex-version-current/` when present

## Boot order

1. Read `../README.md` to identify the Wizard folder layout.
2. Read this file.
3. Read `PACKET_MANIFEST_v4_3.md`.
4. Load the v4.3 MMM: `mmm/FULL_MMM_v4_3.md`, or `mmm/COMPACT_MMM_v4_3.md` plus `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md` when context is tight.
5. Read `WIZARD_v4_3.md`.
6. Read the current LLM's native adaptation front door.
7. Load the task.

Do not boot from `packet-v4-2-current/` as current law. Use v4.2 only as legacy/provenance source material when a v4.3 or LLM-native adaptation explicitly imports a piece.

## Minimum v4.3 run truth

A Wizard claim must name its support level:

- `controller_local` — only local synthesis ran.
- `tool_run` — a concrete tool ran and returned output.
- `spawn_worker` / `spawn_subagent` — a worker/subagent returned a receipt.
- `enqueue_runner` — a background/cron/loop route was created or checked.
- `blocked`, `deferred`, `not_run`, `superseded` — the route did not execute.

A council is not a mood or a summary. It needs receipts from the runtime's actual worker/model routes, or it is controller-local discipline.

## Output shape

Wizard output is not a raw log. Use a compact header, bottom line first, short sections, and compressed receipts.

A good Wizard answer lets a tired human see:

1. what changed;
2. what was checked;
3. what is still open or blocked;
4. what exact next move is safe.

## Anti-collapse rule

Do not turn one idea into exactly one object, one sim, one route, one proof, or one refutation unless a bounded admission gate earns it. Preserve many candidate formations and record which probes excluded which formations.
