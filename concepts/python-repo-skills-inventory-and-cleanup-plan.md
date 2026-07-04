---
title: Python Repo Skills Inventory And Cleanup Plan
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, system, tooling, audit]
sources:
  - raw/articles/new-docs/archive_old/PYTHON_REPO_SKILLS_INVENTORY_AND_CLEANUP_PLAN.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Python / Repo / Skills Inventory and Cleanup Plan

## Overview
Working inventory for cleaning up the repo slowly and properly, starting with Python/tooling. Primary goal: remove redundant tooling from inside the repo, especially .venv_spec_graph, only after clean external/canonical stack is documented, installed, and verified.

## Governing Rules
- Do not delete active tooling before replacement is verified
- Do not rely on memory or shell assumptions about where packages live
- Do not mix repo cleanup with broad repo refactors
- Python/tooling cleanup comes first
- Repo location stays on Desktop for now
- Git repos remain in ~/GitHub
- Python tooling should eventually be standardized outside the repo

## Current State
Main repo: ~/Desktop/Codex Ratchet/ (~1.5GB). Biggest cleanup target: .venv_spec_graph (~1.0GB). Do NOT delete yet -- repo code still references it. Chosen clean external folder: ~/python/.

## Location Classes
- Main repo: ~/Desktop/Codex Ratchet/
- Git repos: ~/GitHub/ (hermes-agent, leviathan, pi-mono, reference, etc.)
- Separate sim workspace: ~/LevRatchet/
- User-level Python: ~/python/

## Key Repos in ~/GitHub
hermes-agent (core), hermes-agent-self-evolution (improvement), leviathan (framework), leviathan-agent-lease/agentping/agents/lev-agentfs/lev-content, pi-mono (retired), reference (external), Sofia, codex-autoresearch.

## Cleanup Policy
This is the cleanup policy doc. For the fuller machine-scope listing, see [[full-machine-python-repo-skills-inventory]]. This doc stays compact and policy-oriented.

## Related pages
- [[full-machine-python-repo-skills-inventory]]
- [[hermes-repos-and-ecosystem-classification]]
- [[venv-migration-status]]
- [[tooling-status]]
