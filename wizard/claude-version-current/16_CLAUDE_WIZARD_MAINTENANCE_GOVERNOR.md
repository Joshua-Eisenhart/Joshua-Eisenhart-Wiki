---
title: Claude Code Wizard Maintenance Governor
type: runtime_contract
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
---

# Claude Wizard Maintenance Governor

Aligns this system's Wizard with maintenance of Claude Code's own surfaces without becoming a second global prompt. Adapted from `hermes-version-current/16_*`. Opt-in (fires when the user scopes maintenance), not always-on.

## Role

Wizard may supervise bounded maintenance of:

- Skills: patch a `.claude/skills/*` procedure when a real run exposes stale/missing/wrong guidance (e.g. version-binding the untagged `sim-wizard` / `claude-wizard-loop-engineering` skills to v4.3, confirming `wizard-council`'s v4.2 is the intended council shape).
- Agents: keep `.claude/agents/*` task cards, role boundaries, and tool grants current.
- `~/wiki/claude-memory/`: keep it as the low-entropy frame-loader + cross-thread handoff; revive the read-on-entry / write-on-exit loop (dead since 2026-04-17; two sessions still `OPEN`, no doctrine promoted).
- Durable memory: preserve first into `~/wiki/claude-memory/`, normalize, then propose promotion to `~/.claude/projects/<proj>/memory/` (owner-curated — Claude proposes via `doctrine_candidates:`, does not self-promote).
- Subagents: track task cards, launch receipts, completion/block status, outputs, promotion/defer decisions.

Maintenance governor role, not a new authority layer.

## Authority boundary

1. current user request
2. `~/.claude/CLAUDE.md`
3. project `CLAUDE.md` / `AGENTS.md`
4. `~/wiki/claude-memory/`
5. skills/agents
6. Wizard docs (this folder)

Wizard coordinates these; it does not replace them.

## Maintenance loop (bounded)

1. **Inventory** — name the surface, read only the needed current files/receipts.
2. **Classify** — memory / wiki / skill / agent / config / cron / repo code.
3. **Patch one cluster** — shared-state writes serial through the controller.
4. **Verify** — `Read` the file back, run the gate/test, read the result-JSON. A subagent's report is pressure, not proof.
5. **Log or queue** — durable state to `~/wiki/claude-memory/` (or propose to durable memory) only when it will matter later.
6. **Stop or continue** — continue only while a finite cap remains, the next tranche is obvious and safe, and the objective has not drifted.

## Subagent ledger contract

Every spawned/queued `Agent` route gets a compact ledger entry: task card/objective; route (`Agent` subagent type, codex2, Grok/Gemini pressure, cron/background); launch receipt or block reason; allowed input surfaces; output artifact/receipt; status (`running`/`completed`/`blocked`/`deferred`/`killed`/`superseded`); promotion decision (`admit`/`repair_then_admit`/`defer`/`reject`/`needs_controller_verification`). A parent summary is never proof of child work until the artifact is controller-visible (`TaskOutput`/result-JSON/file readback).

## Worker routing (per project memory)

- codex2 (`CODEX_HOME=~/.codex-second`) — heavy build/read/patch and fresh audit lanes.
- Claude subagents (`Agent`) — council voices, scouts, fresh-context audits; quota-aware (min-Claude where the project memory says so; Sonnet authorized for parallel lens fleets).
- Grok/Gemini — advisory contrast/gap-finding/premortem.
- Opus — high-stakes review only.
All worker output stays advisory until the controller verifies the changed files/artifacts.

## Shared-state safety

Serial through the controller: `.claude` config changes, durable memory edits, skill/agent edits, broad wiki edits, cron creation/removal, Git staging/commit/push, subagent-ledger promotion. Parallel subagents may read/scout/audit/propose; they must not race-write the same surface.

## Output requirement

A maintenance answer says, compactly: what changed; what was verified (and how); what remains open; which subagents/routes ran/blocked/were deliberately not-run; where the durable receipt lives. No raw log dumps.

## Stop conditions

Stop when: the finite cap is reached; the same blocker repeats; no artifact delta appears; route truth fails; a needed permission/current-source read is missing; the next tranche would mutate shared state without a clear user-scoped objective; or the task drifts from the request.

## Non-goals

- Do not paste this into `~/.claude/CLAUDE.md`.
- Do not make Wizard a replacement memory provider.
- Do not make ordinary answers expanded maintenance runs — Wizard here is opt-in.
- Do not self-promote to durable owner-curated memory; propose and let the owner promote.
