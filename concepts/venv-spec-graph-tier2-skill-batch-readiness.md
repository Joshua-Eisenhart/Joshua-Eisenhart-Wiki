---
title: Venv Spec Graph Tier2 Skill Batch Readiness
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, system, tooling, planning]
sources:
  - raw/articles/new-docs/archive_old/VENV_SPEC_GRAPH_TIER2_SKILL_BATCH_READINESS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/archive_old/VENV_SPEC_GRAPH_TIER2_SKILL_BATCH_READINESS.md
framing: legacy_cleanup_snapshot
priming: false
---

# .venv_spec_graph Tier-2 Skill Batch Readiness

## Overview
Readiness assessment for migrating tier-2 skills from .venv_spec_graph to canonical interpreter. Superseded by [[venv-migration-status]] which confirms ALL skills (tier-1 and tier-2) are migrated.

Status boundary: this is an April readiness assessment. It is useful provenance, not current runtime or deletion authority. Current runtime constants no longer have to preserve this exact interpreter string; verify against the repo before citing runtime state.

## Tier-2 Skills (now migrated)
- clifford_edge_semantics_audit.py: migrated to /opt/homebrew/bin/python3
- toponetx_projection_adapter_audit.py: migrated
- pyg_heterograph_projection_audit.py: migrated

## Original Assessment
Each skill needed: import audit (what depends on .venv_spec_graph), path replacement (PREFERRED_INTERPRETER constant), test run under canonical interpreter, validation of output correctness.

## Current Status
All assessments completed. All skills confirmed working under canonical interpreter. Migration is COMPLETE. No remaining tier-2 blockers for .venv_spec_graph deletion.

## Related pages
- [[venv-migration-status]]
- [[tooling-status]]
- [[venv-spec-graph-post-migration-validation]]
