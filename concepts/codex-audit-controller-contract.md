---
title: Codex Audit Controller Contract
created: 2026-04-08
updated: 2026-04-08
type: concept
tags: [audit, planning, system, simulation, validation, constraints]
sources:
  - raw/articles/new-docs/CODEX_AUDIT_2026_04_08.md
framing: current
---

# Codex Audit — Controller Contract

Historical audit summary of LLM-control failures. Root cause: truth-maintenance problem, not productivity problem.

Use this page as support/history, not as the current front-door controller contract. For the live contract surface, see [[llm-controller-contract]].

## Actually Broken

- **Phase 7 overclaim**: C2\_graph\_topology not tested for all 28 families. "Survives all 4 criteria" is unsupported.
- **Controller collapse**: "passes," "exists," "verified," "canonical" treated as equivalent status.
- **Tool-depth inconsistency**: some outputs have correct `tool_integration_depth`, many don't.
- **Doc staleness**: registry stale enough to cause LLM hallucination of progress.

## Stricter Controller Contract

1. **Split prompts** into: Read Order, Non-negotiable Guardrails, Allowed Claims, Required Verification, Stop Rules.
2. **Ban absolute repo-state claims** unless citing current file/result path from this run.
3. **4 status labels only**: `exists` | `runs` | `passes local rerun` | `canonical by process`.
4. **Claim table required**: claim → file/result → local rerun or source check before any summary.
5. **Separate lanes**: foundation migration, seam proof depth, stack/nesting. Never merge into one progress claim.
6. **Hard stop**: no registry/doc status edits until code/result gate explicitly satisfied.
7. **Phase 7 completion** = C2 coverage for ALL 28 families, not partial subset.
8. **Bounded batch workers**: controller-side consolidation pass checking overclaim, stale docs, schema drift.

## Formal Version

See [[llm-controller-contract]] for the full formal contract with claim tables, hard stop rules, and batch worker constraints.

## Related Pages

- [[enforcement-and-process-rules]] — existing 13 rules
- [[pytorch-ratchet-build-plan]] — Phase 7 status
- [[migration-registry]] — family status (currently stale)
- [[session-handoff-2026-04-07]] — honest assessment of what's real vs theater
- [[tool-manifest-audit]] — tool-depth reporting gap
