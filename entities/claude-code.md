---
title: Claude Code
created: 2026-04-10
updated: 2026-04-10
type: entity
tags: [entity, workflow, multi-agent, tooling]
sources:
  - raw/articles/new-docs/AGENT_WORKFLOW_AND_BOOT_ARCHITECTURE.md
  - raw/articles/new-docs/archive_old/CLAUDE_BATCH_HANDOFF_PROCESS.md
  - raw/articles/new-docs/archive_old/CLAUDE_CODE_DANGEROUS_MODE_POLICY.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Claude Code

## Overview
Claude Code is the worker-terminal execution surface in this wiki. It runs one bounded handoff at a time under a declared boot, produces repo artifacts, and returns review notes for controller audit.

## Key facts
- Claude Code is used for A1 recon, A0 compiler, B ratchet, and SIM discipline boots.
- The worker contract is one handoff per terminal, not one mega-prompt for many tasks.
- Dangerous mode is treated as a bounded execution contract, not a blank check.

## Relationships
- Primary workflow: [[agent-workflow-and-boot-architecture]]
- Batch handoff discipline: [[claude-batch-handoff-process]]
- Dangerous mode policy: [[claude-code-dangerous-mode-policy]]
- Boot prompts: [[boot-prompt-templates]]
- Controller side counterpart: [[hermes]]
- Repo-mediated orchestration: [[repo-mediated-multi-agent-workflow]]

## Notes
Use this page when the question is about the Claude Code role itself. Use the linked workflow pages for the detailed operating rules.
