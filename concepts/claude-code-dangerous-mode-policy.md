---
title: Claude Code Dangerous Mode Policy
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/archive_old/CLAUDE_CODE_DANGEROUS_MODE_POLICY.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Claude Code Dangerous Mode Policy

## Overview
Formal policy for using Claude Code when dangerous mode / broad permissions are enabled. Every handoff becomes a high-risk execution contract. Superseded by [[agent-workflow-and-boot-architecture]] but preserves dangerous mode discipline.

## Core Rule
If Claude Code has dangerous permissions, the handoff prompt is part of the safety boundary. Vague, broad, open-ended, repo-wide mutation, and exploratory prompts without stop rules are all unsafe.

## Why This Matters
Dangerous mode raises risk of: broad unintended file changes, destructive cleanup, overreach outside task scope, architecture changes when only local fix was intended, silently mutating configs/paths/docs, deleting things that should be archived, replacing open scientific questions with implementation shortcuts.

## Required Sections for Every Dangerous-Mode Handoff
1. Goal (one bounded objective)
2. Context (only needed context)
3. Inspect first (exact files to read before acting)
4. Allowed changes (exact classes of changes permitted)
5. Non-goals (what must not be touched)
6. Required validation (exact tests/commands to run -- use full interpreter path)
7. Required outputs (what files/notes to leave behind)
8. Stop rule (when to stop instead of continuing)

## Default Forbidden Actions
No repo-wide cleanup, mass file moves, mass deletions, dependency churn, broad directory renames, architecture replacement, speculative simplification of scientific structure, changing active doctrine docs, deleting historical material.

## Quality Rules
- One task only per handoff
- Conservative by default -- smallest bounded fix
- No hidden authority -- Claude cannot decide doctrine, promotion, or scientific closure
- Respect open structure -- cannot close open branches narratively
- Auditability required -- must leave evidence for Hermes review

## Review Requirement
Every dangerous-mode handoff requires a short review note in the repo after execution: what changed, which files, what validation ran, what remains broken/open, whether task is complete or needs follow-up.

## Related pages
- [[agent-workflow-and-boot-architecture]]
- [[claude-batch-handoff-process]]
- [[boot-prompt-templates]]
