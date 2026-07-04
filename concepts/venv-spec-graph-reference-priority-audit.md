---
title: Venv Spec Graph Reference Priority Audit
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, system, tooling, audit]
sources:
  - raw/articles/new-docs/archive_old/VENV_SPEC_GRAPH_REFERENCE_PRIORITY_AUDIT.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/archive_old/VENV_SPEC_GRAPH_REFERENCE_PRIORITY_AUDIT.md
framing: legacy_cleanup_snapshot
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# .venv_spec_graph Reference Priority Audit

## Overview
Audit of all remaining .venv_spec_graph references categorized by priority for cleanup. Superseded by [[venv-migration-status]] which has the complete status.

Status boundary: this is a historical reference-priority audit. Treat the cleanup categories as April evidence, not as current permission to delete or archive without fresh reverify. A 2026-05-21 local check found `.venv_spec_graph` absent in both repo and home locations.

## Priority Classes

### Runtime blockers (MUST fix before deletion)
None remaining. All 5 tier-1/tier-2 skills migrated. Two dead-code constants are cosmetic only.

### Structural references (SHOULD fix for clean codebase)
Defensive exclusion filters in multi_repo_ingestor.py and full_stack_ingestion_manifest.json -- these are correct and should remain.

### Historical records (DO NOT patch)
Frozen audit logs (~12), Antigravity prompt batches (~4), legacy docs (core_docs/, system_v5/), frozen sim results. These are provenance records. Patching them would destroy historical accuracy.

### Planning docs (CAN archive)
VENV_SPEC_GRAPH_SHRINK_DELETE_READINESS_LEDGER.md, VENV_SPEC_GRAPH_REFERENCE_PRIORITY_AUDIT.md, VENV_SPEC_GRAPH_TIER2_SKILL_BATCH_READINESS.md, CURRENT_TOOL_STATUS__*.md. Can be archived after deletion.

## Historical Recommendation
1. Confirm no shell aliases reference .venv_spec_graph
2. Delete .venv_spec_graph/ (~1GB)
3. Archive the 4 venv-specific planning docs
4. Leave historical records untouched

## Related pages
- [[venv-migration-status]]
- [[tooling-status]]
- [[python-repo-skills-inventory-and-cleanup-plan]]
