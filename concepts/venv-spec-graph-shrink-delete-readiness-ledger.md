---
title: Venv Spec Graph Shrink Delete Readiness Ledger
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, system, tooling, planning]
sources:
  - raw/articles/new-docs/archive_old/VENV_SPEC_GRAPH_SHRINK_DELETE_READINESS_LEDGER.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/archive_old/VENV_SPEC_GRAPH_SHRINK_DELETE_READINESS_LEDGER.md
framing: legacy_cleanup_snapshot
priming: false
---

# .venv_spec_graph Shrink/Delete Readiness Ledger

## Overview
Readiness ledger for shrinking or deleting .venv_spec_graph. Superseded by [[venv-migration-status]] which confirms migration is complete.

Status boundary: this ledger is historical. The unchecked owner-confirmation and deletion items remain non-authorizing until a fresh local reverify is run. A 2026-05-21 local check found `.venv_spec_graph` absent in both repo and home locations.

## Historical Readiness Checklist
- [x] All tier-1 skills migrated to canonical interpreter
- [x] All tier-2 skills migrated to canonical interpreter
- [x] No runtime execution paths reference .venv_spec_graph/bin/python
- [x] Two dead-code constants identified (cosmetic, not blockers)
- [x] Defensive exclusion filters in place (correct behavior)
- [ ] Owner confirms no external shell aliases reference it
- [ ] Owner confirms no launchd plists reference it
- [ ] Delete directory

## Size
.venv_spec_graph is ~1GB. This is the largest single cleanup target inside the repo.

## Historical Post-Deletion Notes
1. Remove two dead-code constants (optional, cosmetic)
2. Archive 4 VENV_SPEC_GRAPH planning docs
3. Update any remaining planning docs that reference migration as in-progress

## Related pages
- [[venv-migration-status]]
- [[tooling-status]]
- [[python-repo-skills-inventory-and-cleanup-plan]]
