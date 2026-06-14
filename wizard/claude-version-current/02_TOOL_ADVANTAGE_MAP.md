---
title: Claude Code Wizard Tool Advantage Map
type: tool_map
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
---

# Tool Advantage Map

This system's Wizard is built around Claude Code's tools, not Hermes's `delegate_task`/`cronjob`/gateway surfaces and not Codex's process machinery. Same Wizard idea, native bindings.

## Core Claude Code advantages

| Claude Code surface | Wizard job | Truth boundary |
|---|---|---|
| `Skill` tool + `.claude/skills/` | load procedures (wizard, wizard-council, wizard-v43, sim-wizard, three-engine-sim, premortem) | a skill is procedure, not proof a run happened |
| `Agent` tool (subagents) | bounded parallel fan-out: sim-runners (julia/jax/pytorch), fresh-audit-runner, voice-* council, council-collapse-auditor, fabrication-auditor | only the returned final message/receipt counts; a builder's verdict on its own work is never evidence |
| `~/.claude/projects/<proj>/memory/` (MEMORY.md + files) | durable owner-curated doctrine | Claude reads, rarely writes; recall is not current execution |
| `~/wiki/claude-memory/` (sessions/doctrine/INDEX) | Claude-owned cross-thread working memory + handoff | read on entry, write on exit; a session summary is not current file state |
| `Read`/`Grep`/`Glob` | grounded file reads + inventory | reading proves content only at read time |
| `Edit`/`Write` | grounded file mutation | a write must be read back to prove it landed |
| `Bash` (+ `run_in_background`) | commands, tests, sims, readiness checks | exit 0 / process alive is not task done; read the result |
| `Monitor` / `TaskList` / `TaskOutput` / `TaskStop` | track and assert background/agent state | assert from notification/TaskOutput/result-JSON, never from `ps`/mtime |
| `CronCreate` + `/loop` + `/schedule` skills | scheduled or recurring autonomous work | cron fires fresh context; the prompt must be self-contained |
| `WebFetch` / `WebSearch` | current research and source pull | web facts need fresh receipts |
| `ToolSearch` (deferred tools / MCP) | dynamic external tool surfaces | tool name + availability must be fetched before use |
| `AskUserQuestion` | resolve a genuine owner-only fork | use only for decisions not tool-recoverable; not for determinable work |

## Authority surfaces (the Claude analog to HERMES.md/SOUL.md/hermes-current)

1. current user request
2. `~/.claude/CLAUDE.md` — global control law + output discipline
3. `<repo>/CLAUDE.md` — project law (Codex Ratchet: read-first docs, gates, ceilings); `AGENTS.md` is Codex authority, Claude reads as reference
4. `~/wiki/claude-memory/` — Claude-owned frame + working memory + handoff
5. `.claude/skills/` — executable procedures
6. project/local gates + result JSONs — local evidence rules

This folder is below those until explicitly adopted.

## Recommended route mapping

- direct answer -> controller-local plus `Read`/`Grep`/`Bash`/web reads as needed
- critique / falsifier / premortem -> `Agent` (voice-popper, premortem-agent, falsifier-agent) only when separable and it changes the move
- council -> `Agent` fan-out of `voice-*` + `council-collapse-auditor`, run in one message for parallelism
- sim work -> the sim-runner agents + the per-engine skills; fresh-audit-runner for closure (builder never audits own work)
- follow-up scout -> `Agent` (Explore/scout-runner), marked scout, not chosen execution
- durable watch -> `CronCreate` / `/loop` only after explicit scope

## Tool-first rule

If a state is checkable with a tool, check it. current file -> `Read`; inventory -> `Grep`/`Glob`; counts/arithmetic -> `Bash`; agent/background state -> `TaskOutput`/`Monitor`; web facts -> `WebFetch`.

## Anti-theater rule

Do not claim a Wizard lane just because the toolset exists. A toolset is capability, not execution. A subagent's parent-reported summary is not proof of its child work until the artifact is controller-visible.
