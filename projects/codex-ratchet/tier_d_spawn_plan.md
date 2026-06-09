# Tier D spawn plan

Historical 2026-04-17 launch plan only. Launch gates, runner-live checks,
canonical labels, and UNSAT targets below are plan-era requirements, not current
Tier D proof or authorization.

Status: waiting on Tier B gate.
Date: 2026-04-17 00:00 PDT
Source brief: ops/TIER_D.md

## Plan-Era Blocker Snapshot
1. `~/wiki/projects/codex-ratchet/tier_b.md` is not green.
   - Current contents show `Status: blocker` and `Tier B not launched`.
2. Tier D precondition `all 5 ~/wiki/projects/codex-ratchet/tier_b_<layer>.md exist` is not satisfied.
   - Current matches: only `tier_b_spawn_plan.md` exists.
3. Repo preflight is not clean right now.
   - `git status --short` shows modified queue/results files.
4. Runner log path exists.
   - `overnight_logs/sim_runner_current.log`: exists.

## Archived Plan Body - Do Not Execute

The archived plan would have launched Tier D when all of the following were true:
- `~/wiki/projects/codex-ratchet/tier_b.md` shows `Gate: green`.
- All 5 layer reports exist at `~/wiki/projects/codex-ratchet/tier_b_<layer>.md`.
- Runner is live per ops/SIM_RUNNER.md.
- Preflight is clean after auto-handling only the safe buckets from ops/HERMES_RULES.md.
- No sibling scope collision is present in `/tmp/hermes_active_scopes.txt`.

## Boundary packet layout
The archived plan would have spawned exactly 4 Sonnet workers in isolated worktrees, one boundary each, disjoint probe scopes only.

### D1 — G -> Hopf
- Scope: `boundary_g_to_hopf_*`
- Output probe: `system_v4/probes/boundary_g_to_hopf_admissibility.py`
- Question: which Hopf classes are UNSAT on non-E-class root systems?
- Required result keys:
  - `boundary: "g_to_hopf"`
  - `positive_admissible`
  - `negative_unsat`
  - `boundary_edge`
  - `anti_tautology_check`

### D2 — Hopf -> Weyl
- Scope: `boundary_hopf_to_weyl_*`
- Output probe: `system_v4/probes/boundary_hopf_to_weyl_admissibility.py`
- Question: which chirality choices are UNSAT on given fibration winding?
- Required result keys:
  - `boundary: "hopf_to_weyl"`
  - `positive_admissible`
  - `negative_unsat`
  - `boundary_edge`
  - `anti_tautology_check`

### D3 — Weyl -> Flux
- Scope: `boundary_weyl_to_flux_*`
- Output probe: `system_v4/probes/boundary_weyl_to_flux_admissibility.py`
- Question: which flux orientations are UNSAT without spinor carrier?
- Required result keys:
  - `boundary: "weyl_to_flux"`
  - `positive_admissible`
  - `negative_unsat`
  - `boundary_edge`
  - `anti_tautology_check`

### D4 — Flux -> Pauli
- Scope: `boundary_flux_to_pauli_*`
- Output probe: `system_v4/probes/boundary_flux_to_pauli_admissibility.py`
- Question: which Pauli axes are UNSAT without flux orientation?
- Required result keys:
  - `boundary: "flux_to_pauli"`
  - `positive_admissible`
  - `negative_unsat`
  - `boundary_edge`
  - `anti_tautology_check`

## Worker read order
Every boundary worker reads, in this order:
1. `~/wiki/wizard/harness-consolidated/00_READ_FIRST.md`
2. `~/wiki/wizard/harness-consolidated/02_constraint_admissibility_primer.md`
3. `~/wiki/wizard/harness-consolidated/06_coupling_program_order.md`
4. `~/wiki/wizard/harness-consolidated/07_z3_unsat_primacy.md`
5. `system_v4/probes/SIM_TEMPLATE.py`
6. lower boundary report `~/wiki/projects/codex-ratchet/tier_b_<lower>.md`
7. upper boundary report `~/wiki/projects/codex-ratchet/tier_b_<upper>.md`
8. Named Tier D probe references if they exist; otherwise stop and report the missing reference rather than inventing substitute authority.

## Non-negotiable worker requirements
- `classification = "canonical"`
- SMT tool contract: `z3` or `cvc5` must be `load_bearing`
- `sympy` must be `load_bearing` or `supportive`
- Positive section: at least 1 admissible SAT witness
- Negative section: at least 2 UNSAT certificates on forbidden compositions
- Boundary section: edge cases only
- Anti-tautology self-check must pass before commit
- Workers write probes and enqueue basenames to `ops/queue_tier_d.txt`; workers never run sims
- Commit format: `tier-d/D<n>: <boundary> admissibility UNSAT certificates`

## Archived launch sequence when gate turns green
1. Read ops/HERMES_RULES.md, ops/SIM_RUNNER.md, ops/TIER_D.md, ops/AUDIT_TRAIL.md.
2. Run preflight:
   - `git status --short`
   - auto-handle only safe buckets A-E from ops/HERMES_RULES.md
   - block on any remaining non-empty status or unsafe bucket
   - check `/tmp/hermes_active_scopes.txt` for scope collision
3. Verify runner is live, not just log-path-present.
4. Append terminal start line to `~/wiki/projects/codex-ratchet/_steward_log.md`.
5. Rewrite `~/wiki/projects/codex-ratchet/tier_d.md` with `last_updated:` header and `Status: in_progress`.
6. Plan-era step: spawn D1-D4 in one batch with disjoint scopes.
7. After each worker commit, append basename to `ops/queue_tier_d.txt` and append steward log line.
8. Do not execute probes directly; runner owns execution.
9. After runner marks all 4 `DONE`, run auditor pass and write:
   - `~/wiki/projects/codex-ratchet/tier_d_audit.md`
   - `~/wiki/projects/codex-ratchet/tier_d_certificates.md`
   - refreshed `~/wiki/projects/codex-ratchet/tier_d.md`

## Auditor packet
Use a Sonnet judgment pass after runner completion.
Checks:
- canonical classification present
- SMT tool is load-bearing
- at least 2 UNSAT certificates per boundary
- fresh independent re-verification of each stored UNSAT encoding
- each UNSAT references lower-layer structure
- positive + negative + boundary sections present
- no banned verbs in probe or result JSON
- no cross-layer scope creep

## Gate evidence required for Tier D green
- 4 boundary probes committed
- runner marks all 4 as DONE
- at least 8 UNSAT certificates total
- all UNSAT independently re-verified
- anti-tautology check passed for each boundary
- no banned verbs in any probe or result

## Blocker discipline
If launch is blocked after Tier B turns green, write the blocker to `~/wiki/projects/codex-ratchet/tier_d.md` and `_steward_questions.md` with exact missing prerequisite. Do not invent a weaker gate.
