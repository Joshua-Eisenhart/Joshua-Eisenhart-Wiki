---
title: Hermes Wizard Read First
type: read_first
runtime: hermes
created: 2026-05-04
updated: 2026-05-04
---

# Read First

This folder adapts the Wizard idea to Hermes.

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
5. render through Hermes's normal scaffold.

## Maintenance extension

When the user asks Wizard to maintain Hermes, memories, skills, subagents, or the wiki, use `16_HERMES_WIZARD_MAINTENANCE_GOVERNOR.md` after this front door and the runtime contract.

That maintenance role is coordination, not replacement: Wizard inventories, routes, patches, verifies, logs, and queues bounded tranches while preserving the normal authority split among `HERMES.md`, `SOUL.md`, `hermes-current/`, skills, memory tooling, cron/background routes, and verified worker receipts.
