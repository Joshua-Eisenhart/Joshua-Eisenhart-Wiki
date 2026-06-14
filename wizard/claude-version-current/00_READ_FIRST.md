---
title: Claude Code Wizard Read First
type: read_first
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
---

# Read First

This folder adapts `../packet-v4-3-current/` to Claude Code (this system), with `../hermes-version-current/` usable as a reference adapter rather than Claude authority. Same Wizard core, native bindings.

## Current version boundary

Current Wizard binding is **v4.3** via `../packet-v4-3-current/`. Before applying Claude-specific rules, load the shared v4.3 MMM: `../packet-v4-3-current/mmm/COMPACT_MMM_v4_3.md` plus `../packet-v4-3-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md`, or `../packet-v4-3-current/mmm/FULL_MMM_v4_3.md` when context allows. `../packet-v4-2-current/` is legacy/provenance/source material only; do not run it as current. A v4.3 validator example/selftest is not a real task run.

## Opt-in rule (the key difference from Hermes)

Hermes Wizard is always-on. **This system's Wizard is opt-in** — per `~/.claude/CLAUDE.md`, default answers are plain and low-cognitive-load; the Wizard, the eight voices, the council, and the follow-up apparatus fire **only when the user asks** (`/wizard`, "run the wizard", "run the council", "use the voices"). When not asked, do not emit them. This folder governs only when Wizard is invoked.

## Authority boundary

For live behavior:

1. current user request
2. `~/.claude/CLAUDE.md` — global control law + output discipline + kernel rules
3. `<repo>/CLAUDE.md` — project law; `AGENTS.md` is Codex authority (Claude reads as reference)
4. `~/wiki/claude-memory/` — Claude-owned frame, working memory, cross-thread handoff
5. `.claude/skills/` — executable procedures
6. project/local gates + result JSONs — local evidence rules

This folder is below those until explicitly adopted.

## Why this exists

The general Wizard packet is portable. Portable is not native. The harness core claim: *a general packet cannot run a system by itself; a system must bind the general mechanisms to its own tools, state, failure modes, and output discipline.* This system's tools are the Claude Code tool set (`Agent`, `Skill`, `Read`/`Grep`/`Edit`/`Write`, `Bash`, `Monitor`/`TaskOutput`, `CronCreate`, `WebFetch`, `ToolSearch`, `AskUserQuestion`) — see `02_TOOL_ADVANTAGE_MAP.md`.

## Read-on-entry / write-on-exit (wire this to claude-memory)

Any Claude thread doing Wizard work here reads, in order: (1) this file + `01_RUNTIME_CONTRACT.md` + `02_TOOL_ADVANTAGE_MAP.md`; (2) `~/wiki/claude-memory/INDEX.md`; (3) relevant `~/wiki/claude-memory/sessions/`; (4) `~/.claude/projects/<proj>/memory/MEMORY.md`. On exit, write a session file to `~/wiki/claude-memory/sessions/` (silence = lost context — this is the loop that has been dead since 2026-04-17 and must be revived).

## Working rule

A Wizard run is valid only when each visible route has: a current tool receipt; a current `Agent` receipt; a current background/cron receipt; an explicit blocked/deferred/not-run status; or a clear statement it stayed controller-local and was not subagent proof.

## Smallest useful version

1. choose a bounded move; 2. pressure-test it (premortem/falsifier); 3. compile a next action with success + stop checks; 4. use subagents/tools only where they change the answer; 5. render plain, bottom-line-first, honest status labels — not a log dump.

## Maintenance extension

When the user asks Wizard to maintain skills, agents, memory, or the wiki, use `16_CLAUDE_WIZARD_MAINTENANCE_GOVERNOR.md` after this front door and the runtime contract.

## Imported assets note

`schemas/`, `conformance/`, and `templates/` were copied from `hermes-version-current/` as reusable scaffolding and still carry Hermes naming/logic. Re-tool them to Claude Code action-classes on first real use; do not treat them as Claude-native yet.
