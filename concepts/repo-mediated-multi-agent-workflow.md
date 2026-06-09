---
title: Repo Mediated Multi Agent Workflow
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, system, workflow]
sources:
  - raw/articles/new-docs/archive_old/REPO_MEDIATED_MULTI_AGENT_WORKFLOW.md
framing: legacy
priming: false
---

# Repo-Mediated Multi-Agent Workflow

## Overview
Defines the workflow for multiple agents operating through the repo as the coordination surface. Superseded by [[agent-workflow-and-boot-architecture]] but preserves the repo-mediated coordination pattern.

## Core Pattern
Agents communicate through repo artifacts, not through direct messaging. Each agent reads from and writes to specific locations in the repo. The repo is the single source of truth for task state, results, and handoff information.

## Directory Conventions
- `.agent/handoffs/active/`: ready tasks for execution
- `.agent/handoffs/completed/`: finished tasks
- `.agent/reviews/active/`: returned review notes
- `sim_results/`: simulation result artifacts

## Agent Roles
- Hermes (A2): Orchestrator, writes handoff files, reads review notes, manages batch queues
- Claude terminals: Workers, execute one handoff per terminal, write review notes
- Audit layer: Reviews diffs and review notes after completion

## Handoff File Structure
Each handoff file specifies: goal, context, inspect first, allowed changes, non-goals, required validation, required outputs, stop rule. See [[claude-code-dangerous-mode-policy]] for dangerous mode variants.

## Benefits of Repo-Mediation
- All state is auditable (append-only history)
- No hidden agent-to-agent communication
- Hermes can inspect any terminal's work after the fact
- Multiple terminals can work in parallel without conflicts if tasks are independent
- Completed work has a clear trail for review

## Anti-Patterns
- Direct agent-to-agent messaging bypassing the repo
- Shared mutable state without version control
- Long-lived agent sessions without check-in points
- Tasks too broad for a single handoff

## Related pages
- [[agent-workflow-and-boot-architecture]]
- [[claude-batch-handoff-process]]
- [[claude-code-dangerous-mode-policy]]
- [[boot-prompt-templates]]
