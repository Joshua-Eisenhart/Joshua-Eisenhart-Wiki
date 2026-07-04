---
last_updated: 2026-04-17
type: memory_namespace
owner: claude_threads
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Claude Memory — wiki-resident working memory for Claude threads

Parallel to, not replacing:
- `~/.claude/projects/<proj>/memory/` — global durable doctrine (owner-curated; Claude reads, rarely writes)
- `~/wiki/projects/<proj>/_steward_*`, `~/wiki/hermes-current/hermes-memory-offload.md`, `~/wiki/entities/hermes.md` — Hermes-owned surfaces (Claude reads, does NOT write)

**This namespace is Claude-owned.** Hermes can read it; Hermes does not modify it. Claude threads do not modify Hermes surfaces.

## Three layers

### `sessions/` — per-session working memory

One file per Claude thread-session. Ephemeral-but-persistent: written during the session, read by future sessions or other Claude threads for context transfer.

Filename: `YYYY-MM-DD_<thread-role>_<short-topic>.md`
Examples:
- `2026-04-17_opus-orchestration_fleet-architecture.md`
- `2026-04-17_wiki-claude_harness-upgrade.md`
- `2026-04-17_sim-claude_type-engine-work.md`

### `doctrine/` — promoted cross-session insights

When a session produces durable insight (not project-state, not session-bound), it gets a sibling entry here. Promotion is manual (owner or Opus decides). Doctrine entries are short (≤400 words), stable, cross-referenced.

### `INDEX.md` — live table of contents

One-line entry per session + doctrine file. Mirrors the pattern of `memory/MEMORY.md`. Updated per-write.

## Session file schema

Every file in `sessions/` has this YAML frontmatter:

```yaml
---
session_id: <date-thread-topic>
thread_role: opus_orchestrator | wiki_claude | sim_claude | other
entered_at: <ISO>
exited_at: <ISO or "open">
task_summary: <one sentence>
sources_read: [list of file paths]
artifacts_produced: [list of file paths or commit shas]
blockers_raised: [list]
doctrine_candidates: [list of claims worth promoting to doctrine/]
---
```

Body sections (fixed order):
1. **What I was asked** — the actual task
2. **What I read first** — harness primers + source files (prove the read)
3. **What I produced** — concrete artifacts with paths/shas
4. **What I learned that outlasts this session** — durable insights (promotion candidates)
5. **Open questions** — unresolved for next session
6. **Handoff** — next thread should know...

Language discipline per `harness/03_language_discipline.md` applies. Banned verbs grep-checked on write.

## Rules

1. **One writer per file.** If a session is open, other threads read but do not edit. Conflicting writes are lost.
2. **Write on exit, always.** Even if the session was trivial, write a stub. Silence = lost context.
3. **Cite the harness primer order actually read** — proves salience alignment (counteracts fresh-terminal fabrication per `memory/feedback_sub_agent_fabrication_incident.md`).
4. **Never modify Hermes surfaces.** `_steward_*`, `hermes-memory-offload.md`, `entities/hermes.md` are read-only to Claude.
5. **Never edit `~/.claude/projects/<proj>/memory/` files from here.** That layer is owner-curated durable doctrine. Propose additions via `doctrine_candidates:` frontmatter; owner or Opus promotes.
6. **Digestion cadence:** Opus (or a dedicated digestion Claude) reviews `sessions/` weekly, promotes doctrine, updates `INDEX.md`.

## Read-on-entry

Any Claude thread starting work in this project reads:
1. `~/wiki/wizard/00-read-first.md` and `~/wiki/wizard/AGENTS.md` (active Wizard harness alignment)
2. `~/wiki/claude-memory/INDEX.md` (what's already known)
3. Any `sessions/` files relevant to the current task
4. `~/.claude/projects/<proj>/memory/MEMORY.md` (durable doctrine)

Prompt wrapper for fresh Claude terminals should force step 1 + 2 before any writing.

Nominalist-CS support material now lives under `~/wiki/wizard/harness-consolidated/`. Do not boot directly from the old `~/wiki/harness/` tree unless the task explicitly targets legacy provenance.

## Relation to Hermes

Hermes writes its own session state to `_steward_log.md` in project dirs. That's the Hermes working memory. This Claude namespace is parallel — same concept, different owner. Cross-reading is encouraged; cross-writing is forbidden.
