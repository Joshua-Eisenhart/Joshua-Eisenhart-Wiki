# Tier A spawn plan

Historical 2026-04-17 Tier A spawn plan. Non-executable. Do not treat
active/canonical/rerun language here as current readiness or promotion; verify
live repo receipts and current user authorization first.

Status: historical active-at-write-time
Brief: ops/TIER_A.md
Date: 2026-04-17 UTC

Preflight
- git status cleaned by committing safe doc-metadata snapshot and the untracked ops briefs.
- Harness present at ~/wiki/wizard/harness-consolidated/00_READ_FIRST.md.
- Active scope recorded in /tmp/hermes_active_scopes.txt.

Worker lanes and scopes
1. T1 serializer/backfill
   - Scope: system_v4/probes/a2_state/_doc_illum_common.py
            system_v4/probes/a2_state/_couple_common.py
            system_v4/probes/a2_state/_triple_common.py
            system_v4/probes/a2_state/_quad_common.py
            plus re-run of the canonical result files missing tool_integration_depth.
   - Deliverables: helper patch, reruns, zero canonical results missing depth.

2. T2 axis0 rename pass
   - Scope: system_v4/probes/axis0_*.py
   - Deliverables: judging-function label strip/rename pass, grep zero hits.

3. T3 SIM_TEMPLATE conformance audit
   - Scope: audit artifact only at system_v4/probes/a2_state/sim_results/tier_a_t3_audit.json
   - Deliverables: per-probe classification a/b/c for canonical results missing depth.

4. T4-T9 tool-pair integration sims
   - Scope: one file each under system_v4/probes/tool_integration_<pair>.py and matching result JSON.
   - Pairs: z3_sympy, sympy_pyg, pyg_torch, clifford_weyl, toponetx_pyg, cvc5_sympy.
   - Deliverables: canonical sim, non-empty tool manifest reasons, tool_integration_depth with at least one load-bearing tool, positive/negative/boundary tests, local rerun result JSON.

5. Auditor
   - Scope: ~/wiki/projects/codex-ratchet/tier_a_audit_log.md and final verification pass.
   - Deliverables: commit/result cross-checks, no unresolved discrepancies at closeout.

Execution order
- Batch 1: audit current state, patch helpers, axis0 pass, classify missing-depth probes.
- Batch 2: rerun missing-depth probes and verify canonical result coverage.
- Batch 3: build six tool-pair integration sims in disjoint file scopes.
- Batch 4: closeout verification, write ~/wiki/projects/codex-ratchet/tier_a.md, one L3 report.

Stop conditions
- Missing single-probe rerun path in Makefile or helper scripts.
- Any axis0 label deletion that breaks a sim without a bounded fix.
- Any tool-pair sim blocked by missing dependency or absent template requirement.
- Any scope collision or git-integrity issue.
