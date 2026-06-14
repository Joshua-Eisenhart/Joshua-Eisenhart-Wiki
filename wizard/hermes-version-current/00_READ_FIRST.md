---
title: Hermes Wizard Read First
type: read_first
runtime: hermes
created: 2026-05-04
updated: 2026-05-04
---

# Read First

This folder adapts the Wizard idea to Hermes.

## Current version boundary

Current Hermes Wizard binding is **v4.3**. v4.3 is the required current-task object-preservation gate for object-bearing work; legacy v4.2 packet references are provenance; do not run v4.2 as current. Do not say “current Wizard is v4.2” without the v4.3 gate, and do not call a v4.3 validator example/selftest a real task run.

## Always-on adaptive rule

Hermes Wizard runs every prompt and every prompt uses Wizard/Hermes formatting with a compact header. The depth is adaptive: ambient mode checks context continuity, memory/offload, skill maintenance, route truth, stale-context risk, and next-action/failure/follow-up shape; full councils, visible voices, and worker waves are escalations only when requested or warranted. Wizard output is human synthesis, not logs; headers exist to reduce cognitive load.

Context must be reinjected, not loaded once: parent/child/subagent routes receive the current context pack plus relevant MMM/saliency slices before task rules, and long or multi-wave work refreshes at TTL/checkpoints.

Main-agent MMM load comes first: before ordinary Wizard synthesis, load the active main MMM saliency body (`COMPACT_MMM_v4_3.md` by default with MMM index/L0). For high-context runs, load `FULL_MMM_v4_3.md` or the relevant/all mini-MMM set and compact it into the main agent. Worker preload never replaces this main-agent load.

## Authority boundary

For live Hermes behavior:

1. current user request
2. `~/.hermes/HERMES.md` — control law and output scaffold
3. `~/.hermes/SOUL.md` — body voice and anti-collapse method
4. `~/wiki/hermes-current/` — long-form Hermes frame and provenance routing
5. skills — executable procedures
6. project/local docs — local gates and evidence rules

This folder is below those until explicitly adopted.

## Why this exists

The general Wizard packet is portable. Portable does not mean native.

Hermes needs a version that uses Hermes's own surfaces:

- `skill_view` / `skills_list` / `skill_manage`
- `memory` and `session_search`
- `delegate_task`
- `cronjob`
- file/search/patch/write tools
- terminal/process tools
- web/browser/MCP/gateway surfaces
- profile-scoped config, sessions, memory, and skills
- Hermes answer scaffold and SOUL voice stack
- maintenance governance for Hermes memory, skills, wiki, and subagent ledgers through existing Hermes tools and skills

## Load rule

Do not load `../packet-v4-1-current/` as Hermes authority by default.
Use it as a source to mine mechanisms.

Do not load Codex Ratchet's AGENTS/process docs as Hermes authority by default.
Use them to import proven mechanisms with boundaries.

For explicit Wizard/current-Wizard/object-bearing work, load `15_HERMES_WIZARD_V4_3_OBJECT_PRESERVATION.md` and keep current routing under v4.3. Legacy v4.2 packet surfaces are provenance only unless the user explicitly asks for historical audit.

## Working rule

A Hermes Wizard run is valid only when each visible route has one of:

- a current Hermes tool receipt;
- a current `delegate_task` receipt;
- a current background/cron/process receipt;
- an explicit blocked/deferred/not-run status;
- or a clear statement that it remained controller-local and was not worker proof.

## Smallest useful version

The smallest Hermes Wizard is:

1. choose a bounded move;
2. pressure-test it;
3. compile a next action with success and stop checks;
4. use Hermes tools/workers only where they change the answer;
5. render through the Wizard/Hermes headered scaffold, not a log dump.

## Maintenance extension

When the user asks Wizard to maintain Hermes, memories, skills, subagents, or the wiki, use `16_HERMES_WIZARD_MAINTENANCE_GOVERNOR.md` after this front door and the runtime contract.

That maintenance role is coordination, not replacement: Wizard inventories, routes, patches, verifies, logs, and queues bounded tranches while preserving the normal authority split among `HERMES.md`, `SOUL.md`, `hermes-current/`, skills, memory tooling, cron/background routes, and verified worker receipts.
