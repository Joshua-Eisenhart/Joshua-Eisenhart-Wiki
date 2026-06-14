---
title: Wizard v4.3 Adapter Guide
created: 2026-06-13
updated: 2026-06-13
packet: v4.3
type: adapter_guide
---

# Adapter Guide

All Wizard adapters live under `~/wiki/wizard/` as sibling folders:

- `<llm>-version-current/`

Examples:

- `hermes-version-current/`
- `claude-version-current/`
- `codex-version-current/`

## Adapter minimum contents

Each adapter should have:

- `README.md`
- `00_READ_FIRST.md`
- `01_RUNTIME_CONTRACT.md`
- a tool/route map for the runtime
- optional maintenance governor if that runtime maintains memory/skills/wiki/session ledgers
- schemas/templates only after names and action classes are retuned to that runtime

## Copying rule

Copying is allowed. Adoption is not automatic.

If Claude copies Hermes files, those files are Claude source material until every Hermes-specific item is retooled or explicitly marked source-only:

- `HERMES.md` / `SOUL.md`
- `delegate_task`
- Hermes `cronjob`, gateway, profile memory, Hermes session DB
- Hermes-specific schemas and validator names

The same applies in every direction.
