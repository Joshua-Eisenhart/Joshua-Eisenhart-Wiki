---
title: Tool Manifest Audit
created: 2026-04-08
updated: 2026-04-10
type: concept
tags: [audit, system, simulation, validation, planning]
sources:
  - raw/articles/new-docs/TOOL_MANIFEST_AUDIT.md
framing: historical_v4_manifest_audit
spec_mirrors:
  - specs/codex-ratchet/formal-scout-readiness-status
  - specs/codex-ratchet/sim-estate-integration-status
  - specs/codex-ratchet/tool-function-receipt-status
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Tool Manifest Audit

Audit of tool usage across `system_v4/probes/`. Audited against filesystem 2026-04-10.

Status boundary: this page is a dated `system_v4` manifest audit. It should not be used for current `system_v5` formal-scout/readiness/tool-role counts. For live repo status, use [[specs/codex-ratchet/formal-scout-readiness-status]], [[specs/codex-ratchet/sim-estate-integration-status]], and [[specs/codex-ratchet/tool-function-receipt-status]].

## Current Inventory (audited 2026-04-10)

- **sim_*.py files**: 613
- **engine_*.py files**: 13
- **Result JSONs**: 800 (in a2_state/sim_results/)

## Template Compliance (800 result JSONs, audited 2026-04-10)

| Field | Count | % |
|-------|-------|---|
| classification field | 365 | 45.6% |
| tool_manifest present | 358 | 44.8% |
| tool_manifest with non-empty reason | 357 | 44.6% |
| tool_integration_depth | 328 | 41.0% |
| ALL THREE fields | 328 | 41.0% |
| any tool used=True | 237 | 29.6% |
| any tool load_bearing | 221 | 27.6% |
| **Legacy (no classification)** | **435** | **54.4%** |

Significant improvement from earlier audits (previously 0.7% tool_manifest, 3.6% classification). Still 54.4% legacy results predate the template.

**Stale claim**: older summaries reported 764 result JSONs. Actual filesystem audit on 2026-04-10 finds 800 result JSONs. Update any downstream counts that cite the older total.

## Tool Stack Status (v4-only, 2026-04-10)

Strong adoption: z3 (29 sims), clifford (23), toponetx (17), sympy (16).
Minimal: PyG (8), torch (11), gudhi (3).
Zero real usage: cvc5, geomstats, e3nn, rustworkx, xgi.

## Critical Gaps

1. **54.4% legacy results** — no classification/tool_manifest/tool_integration_depth
2. **5 tools have zero real sim usage**: cvc5, geomstats, e3nn, rustworkx, xgi
3. **27.6% of results** have any tool marked load_bearing — still below the Rule 2 requirement that every canonical sim must have at least one nontrivial load-bearing tool

## Related Pages

- [[tooling-status]] — dated/broader routed tool usage status
- [[enforcement-and-process-rules]] — Rule 2 (try all tools, make one load-bearing)
- [[current-tool-status-installed-vs-missing-vs-not-wired]] — install status
- [[current-tool-status-operational-classification]] — operational classification
- [[pytorch-ratchet-build-plan]] — tool integration requirements
- [[migration-registry]] — per-family migration state

## 2026-05-17 system_v5 scope addendum

A later repo surface, [[tool-function-receipt-matrix-router]], routes `system_v5/docs/TOOL_FUNCTION_RECEIPT_MATRIX.md`: 108 exact tool/function receipt rows, 108 passing rows, 0 missing receipts, and 0 unresolved receipt contract shapes.

This is a different scope from the 2026-04-10 `system_v4/probes` manifest audit above. Do not overwrite the earlier v4 percentages with the v5 matrix. Treat both surfaces as `exists` anchors unless a fresh rerun in the current pass earns a stronger label.
