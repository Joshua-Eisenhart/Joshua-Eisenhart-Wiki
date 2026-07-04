---
title: Claude Batch Handoff Process
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/archive_old/CLAUDE_BATCH_HANDOFF_PROCESS.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Claude Batch Handoff Process

## Overview
Defines how to prepare multiple bounded handoffs for fresh Claude Code terminals without losing safety or creating prompt sprawl. Superseded by [[agent-workflow-and-boot-architecture]] but preserves batch discipline.

## Core Rule
A batch is a queue of independent bounded handoffs, not a single mega-prompt. Each Claude terminal receives exactly one active handoff file at a time.

## Batch Directory Convention
- `.agent/handoffs/active/` for ready tasks
- `.agent/handoffs/completed/` for finished tasks
- `.agent/reviews/active/` for returned review notes

Optional naming: `claude__NN__short_task_name.md`

## Batch Eligibility Rules
Only batch tasks that are: bounded, mostly independent, low-conflict in touched files, reviewable separately. Do NOT batch tasks that mutate the same files heavily, depend on unresolved outputs from each other, or are broad cleanup/refactor tasks.

## Per-Task Requirements
Every task must include: exact interpreter/command paths for validation, allowed changes, non-goals, stop rule, required review note path.

## Launch Pattern
For each fresh Claude terminal: start in repo, give minimal prompt like "Read .agent/handoffs/active/<file>.md and execute it conservatively." Do not paste long context if repo handoff file already contains it.

## Safety Rule for Dangerous Mode
If Claude has dangerous mode: one handoff per terminal, no stacked tasks, prefer minimal-change tasks, require review note output for every task.

## Hermes Role
Write batch files, ensure tasks are independent, track which terminal got which task, inspect review notes and repo diff afterward, move completed handoffs out of active.

## Related pages
- [[agent-workflow-and-boot-architecture]]
- [[claude-code-dangerous-mode-policy]]
- [[boot-prompt-templates]]
