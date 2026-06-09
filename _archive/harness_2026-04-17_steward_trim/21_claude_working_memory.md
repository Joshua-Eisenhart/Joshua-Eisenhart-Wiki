last_updated: 2026-04-17

# Claude Working Memory Protocol

Claude threads write session memory to `~/wiki/claude-memory/`. This is parallel to, and independent from, Hermes memory surfaces.

## Three memory surfaces Claude threads interact with

| Surface | Path | Claude role |
|---|---|---|
| Durable doctrine | `~/.claude/projects/<proj>/memory/` | Read on entry. Write only if owner-instructed. |
| Working memory | `~/wiki/claude-memory/sessions/` | Write on exit. Read siblings on entry. |
| Hermes surfaces | `~/wiki/projects/<proj>/_steward_*`, `~/wiki/current/hermes-memory-offload.md`, `~/wiki/entities/hermes.md` | Read only. Never write. |

## Read-on-entry order

Every Claude thread starting work:

1. `~/wiki/harness/00_READ_FIRST.md` (salience alignment)
2. `~/wiki/claude-memory/INDEX.md` (what sibling sessions know)
3. Any relevant open session files in `~/wiki/claude-memory/sessions/`
4. `~/.claude/projects/<proj>/memory/MEMORY.md` (durable doctrine)
5. Project-specific `projects/<proj>/read-first.md`

Step 1 is non-negotiable. Without it, salience drift is near-certain per `08_anti_patterns.md`.

## Write-on-exit protocol

Every session writes a file at `~/wiki/claude-memory/sessions/YYYY-MM-DD_<thread-role>_<topic>.md`.

Thread roles: `opus_orchestrator` | `wiki_claude` | `sim_claude` | `audit_claude` | `other`.

Required frontmatter (see `~/wiki/claude-memory/README.md` for full schema):
`session_id`, `thread_role`, `entered_at`, `exited_at`, `task_summary`, `sources_read`, `artifacts_produced`, `blockers_raised`, `doctrine_candidates`.

Required body sections in order: asked / read / produced / learned / open questions / handoff.

## Language discipline

Same banned-verb rule as elsewhere in harness. Grep before commit. Session files are readable by fresh threads — drift here contaminates future sessions.

## Separation from Hermes memory

Hermes writes its own session state to `_steward_log.md` and related files. That system has internal tooling Claude should not disrupt. Hermes is the owner of its surfaces. Claude reads them for cross-reference only.

Conversely, Hermes reads Claude session files for context but does not modify them. Cross-visible, single-writer.

## Digestion

Working memory grows. Periodically (Opus weekly or owner-triggered):
- Review `sessions/` entries
- Promote cross-session durable insights from `doctrine_candidates:` frontmatter to `doctrine/<topic>.md` files
- Update `INDEX.md`
- Archive superseded sessions to `sessions/_archive/` if >30 days old

Doctrine files are short (≤400 words), stable, cross-linked.

## Anti-patterns

- Writing session memory into `~/.claude/projects/<proj>/memory/` directly — that's owner-curated durable doctrine. Propose instead.
- Editing `_steward_*.md` or other Hermes surfaces — violation of ownership.
- Skipping write-on-exit because "the session was trivial" — silence loses the context. Write a stub.
- Citing harness primers in `sources_read` without actually reading them — testimony without evidence; falsified by `feedback_sub_agent_fabrication_incident.md`.

## Why this exists

LLM threads are amnestic by default. Salience drifts. Without a wiki-resident working-memory layer, every Claude thread re-derives context from scratch and invents plausible structure (see `feedback_sub_agent_fabrication_incident.md`).

With this protocol, session N+1 inherits session N's conclusions, cites sources, and extends rather than re-constructs. The harness aligns entry; the memory protocol preserves exit.

Cross-linked:
- `~/wiki/claude-memory/README.md` — full schema + rules
- `08_anti_patterns.md` — failures this protocol mitigates
- `13_mandatory_pushback.md` — refuse to write if sources cannot be cited
- `~/.claude/projects/<proj>/memory/feedback_sub_agent_fabrication_incident.md` — the incident that motivated formalization
