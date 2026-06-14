---
title: Claude Code Wizard Version
created: 2026-06-13
updated: 2026-06-13
type: runtime_design
runtime: claude_code
framing: current-proposed
---

# Claude Code Wizard Version

This folder is Claude Code's own native adaptation of `../packet-v4-3-current/`. It can reference `../hermes-version-current/`, but Hermes is a reference adapter, not Claude authority.

It is not a copy of `../packet-v4-2-current/`. It is not a replacement for `~/.claude/CLAUDE.md`, the project `CLAUDE.md`/`AGENTS.md`, the skills, or `~/wiki/claude-memory/`. It is a low-coupling adaptation/proof folder binding Wizard mechanisms to this system's strengths:

- subagent fan-out via the `Agent` tool (sim-runners, voice-* council, fresh-audit-runner, premortem/falsifier)
- the `Skill` tool + `.claude/skills/` procedures
- `~/.claude/projects/<proj>/memory/` durable doctrine + `~/wiki/claude-memory/` working memory and cross-thread handoff
- grounded file/exec tools (`Read`/`Grep`/`Edit`/`Write`/`Bash`/`Monitor`/`TaskOutput`)
- `CronCreate` + `/loop` + `/schedule` for durable/recurring work
- bottom-line-first plain output discipline with honest status labels

## Core claim (shared with Hermes)

A general Wizard packet cannot run a system by itself. A system must make a native version that binds the general mechanisms to its own tools, state, failure modes, and output discipline. Hermes did that in `hermes-version-current/`; this folder does it for Claude Code.

## The key difference from Hermes: opt-in, not always-on

Hermes Wizard runs every prompt. **This system's Wizard is opt-in** (`~/.claude/CLAUDE.md`): plain answers by default; Wizard/voices/council/follow-up fire only when the user asks. This folder governs only when Wizard is invoked.

## Current status

`built-not-yet-adopted`: created 2026-06-13 by re-tooling the Hermes adaptation against the shared `../packet-v4-3-current/` core. Binding is **v4.3**. Not yet wired into the `.claude/skills/wizard*` skills as their reference; that is the adoption step.

## Read order

Before this adapter, load the shared v4.3 core and MMM:

- `../packet-v4-3-current/README.md`
- `../packet-v4-3-current/00_READ_FIRST.md`
- `../packet-v4-3-current/mmm/COMPACT_MMM_v4_3.md` plus `../packet-v4-3-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md`, or `../packet-v4-3-current/mmm/FULL_MMM_v4_3.md` when context allows
- `../packet-v4-3-current/WIZARD_v4_3.md`

Then load Claude-native files:

1. `00_READ_FIRST.md`
2. `01_RUNTIME_CONTRACT.md`
3. `02_TOOL_ADVANTAGE_MAP.md`
4. `16_CLAUDE_WIZARD_MAINTENANCE_GOVERNOR.md`
5. `schemas/` + `conformance/` + `templates/` (imported from Hermes; re-tool to Claude action-classes on first use)

## Provenance

Referenced and adapted from `../hermes-version-current/` (00/01/02/16 + README) on 2026-06-13. Hermes-specific surfaces (`delegate_task`, `cronjob`/gateway, `HERMES.md`/`SOUL.md`, `hermes-current/`) were mapped to Claude Code equivalents in `02_TOOL_ADVANTAGE_MAP.md`. `schemas/`, `conformance/`, `templates/` were copied as-is and still carry Hermes naming/logic — flagged for re-tooling.

## What's still open (adoption)

- Wire this folder in as the reference for `.claude/skills/wizard`, `wizard-council`, `wizard-v43`, `sim-wizard`, `claude-wizard-loop-engineering`; version-bind the untagged skills to v4.3; confirm `wizard-council` v4.2 is intended.
- Re-tool the imported `schemas/`/`conformance/` python validators from Hermes action-classes to Claude action-classes.
- Revive the `~/wiki/claude-memory/` read-on-entry / write-on-exit loop (dead since 2026-04-17).
