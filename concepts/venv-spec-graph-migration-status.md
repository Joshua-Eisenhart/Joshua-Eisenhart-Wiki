---
title: Venv Spec Graph Migration Status
created: 2026-04-07
updated: 2026-05-21
type: concept
tags: [implementation, validation, system, planning]
sources:
  - raw/articles/new-docs/VENV_MIGRATION_STATUS.md
  - raw/articles/new-docs/TOOLING_STATUS.md
  - raw/articles/new-docs/15_stack_authority_and_capability_index.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/VENV_MIGRATION_STATUS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/TOOLING_STATUS.md
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/process-contract-mirror-index.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/tool-function-receipt-status.md
framing: duplicate_historical_stub
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Venv Spec Graph Migration Status

## Overview
The `.venv_spec_graph` migration is complete and deletion-ready pending confirmation.

Status boundary: this page preserves an April cleanup conclusion and duplicates [[venv-migration-status]]. It is not live deletion authorization. A 2026-05-21 local check found `.venv_spec_graph` absent in both repo and home locations; still reverify local shell aliases, launchd/plist references, repo interpreter settings, and current process contracts before acting on cleanup claims.

## Main points
- All tier-1/tier-2 runtime skills migrated to the canonical interpreter.
- No live runtime blockers remain.
- Remaining references are historical or documentation-only.
- The largest remaining action is owner confirmation before deletion.

## Why it matters
This page tracks a concrete cleanup boundary in the stack and points to what is safe to delete versus what is still legacy reference material.

## Related pages
- [[tooling-status]]
- [[stack-authority-and-capability-index]]
- [[system-architecture-reference]]
- [[agent-workflow-and-boot-architecture]]
- [[research-inventory-and-foundations]]
