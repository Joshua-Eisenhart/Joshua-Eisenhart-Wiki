last_updated: 2026-04-17T07:07:25Z

# Tier B spawn plan

Historical/non-executable spawn plan, superseded by current system_v5 gates.
Ignore armed/current/runner-live/green wording unless a fresh repo preflight and
current user request reauthorize this exact lane.

Historical status at time of writing: armed, waiting on Tier A gate green.
Source briefs: ops/HERMES_RULES.md, ops/SIM_RUNNER.md, ops/TIER_B.md, ops/AUDIT_TRAIL.md.

## Plan-era gate read
- Tier A evidence file: `~/wiki/projects/codex-ratchet/tier_a.md`
- Current state at plan write: `Status: blocked` (timestamp in file: `2026-04-17T06:49:54Z`)
- STATUS dashboard cross-check: `Tier A: blocker   Gate: red`
- Runner state at plan write: PID 34263 alive; log present; current probe idle
- Tier B launch condition: Tier A gate green in `tier_a.md` / dashboard, runner live, and preflight acceptable per `ops/HERMES_RULES.md`

## Historical launch batch on gate pass
Spawn one batch with 5 Haiku layer workers + 1 Haiku auditor.
All workers use isolated worktrees via `hermes -w` and disjoint file-prefix scopes.
No worker executes sims. Workers only write probes, commit per-probe, append basenames to `ops/queue_tier_b.txt`, and update the canonical wiki audit files.

## Shared worker read order
Every worker prompt must begin with this exact read order:
1. `~/wiki/wizard/harness-consolidated/00_READ_FIRST.md`
2. `~/wiki/wizard/harness-consolidated/06_coupling_program_order.md`
3. `~/wiki/wizard/harness-consolidated/07_z3_unsat_primacy.md`
4. `system_v4/probes/SIM_TEMPLATE.py`
5. Scan `~/wiki/concepts/` for layer-name matches
6. Read this file: `~/wiki/projects/codex-ratchet/tier_b_spawn_plan.md`

## Shared worker guardrails
- Scope is your prefix only.
- Shell-local only. No cross-layer coupling, coexistence, topology-variant, emergence, or bridge claims.
- If a candidate depends on another layer, record `requires coupling; deferred to Tier D` and stop that line of work.
- New probes must be `SIM_TEMPLATE` conformant.
- Each new probe must set `classification = "canonical"`.
- Each new probe must include at least one `load_bearing` tool from Tier A capability surfaces.
- Positive + negative + boundary sections are required.
- Language discipline from `wizard/harness-consolidated/03_language_discipline.md` applies; banned verbs stay banned.
- Commit format per probe: `tier-b/B<n>: <probe-name>`.
- After each committed probe: append basename to `ops/queue_tier_b.txt` and append a one-line entry to `~/wiki/projects/codex-ratchet/_steward_log.md` in the canonical format.
- Do not execute probes directly; runner owns execution.

## Shared worker success criteria
A layer worker is done only when all are true:
- inventory completed for its scope
- shell-local gaps named under harness step 1
- minimum count of new canonical probes written for that layer
- every new probe committed and enqueued to `ops/queue_tier_b.txt`
- per-layer report written to `~/wiki/projects/codex-ratchet/tier_b_<layer>.md`
- no cross-layer coupling drift in any new Tier B probe

## Worker B1 — geometry towers / stacks
Worker id: B1
Model tier: Haiku
Scope: `gtower_*`, `gstack_*`
Target minimum: 10 new canonical shell-local probes
Preferred subdomains to spread if sub-workers needed:
- exceptional / reduction / invariants (`gtower_*`)
- shell-local operator families and probes (`gtower_*`)
- `gstack_*` shell-local bundle / fibration / stack surfaces
Current visible inventory signals:
- many `gtower_*` files already exist, including shell-local, pairwise, triple, topology-variant, and emergence surfaces
- `gstack_*` shell-local files exist and can anchor gap-filling without cross-layer drift
B1 per-layer report path: `~/wiki/projects/codex-ratchet/tier_b_gtower_gstack.md`

B1 worker instruction block:
- Inventory existing `gtower_*` and `gstack_*` probes.
- Classify each relevant file as `canonical`, `classical_baseline`, or `broken`.
- Find shell-local gaps only: states, operators, probes, entropies well-defined in isolation.
- Prefer files under 500 lines where possible.
- Use disjoint filenames not already present.
- Write at least 10 new canonical shell-local probes.

## Worker B2 — Hopf
Worker id: B2
Model tier: Haiku
Scope: `hopf_*`
Target minimum: 6 new canonical shell-local probes
Current visible inventory signals:
- broad Hopf corpus exists, including many coupling and bridge files; avoid those lanes
- shell-local anchors exist around Hopf torus, connection, winding, holonomy, and fibration surfaces
B2 per-layer report path: `~/wiki/projects/codex-ratchet/tier_b_hopf.md`

B2 worker instruction block:
- Inventory `hopf_*` files and isolate shell-local-only surfaces.
- Ignore pairwise/triple/topology/emergence/bridge files except as anti-pattern boundaries.
- Fill shell-local gaps around fiber winding, holonomy, connection, torus geometry, operator families, and probe-local distinguishability.
- Write at least 6 new canonical shell-local probes.

## Worker B3 — Weyl
Worker id: B3
Model tier: Haiku
Scope: `weyl_*`
Target minimum: 6 new canonical shell-local probes
Current visible inventory signals:
- very large `weyl_*` corpus exists with many non-shell-local files; strong risk of coupling drift
- shell-local anchors appear around Weyl geometry, chirality, nested shell, root-system local structure, and rescaling shells
B3 per-layer report path: `~/wiki/projects/codex-ratchet/tier_b_weyl.md`

B3 worker instruction block:
- Inventory `weyl_*` files and classify shell-local versus non-shell-local before any writing.
- Keep work on chirality, local root-system structure, carrier-local geometry, isolated operator/probe families, and shell-local rescaling surfaces only.
- If a file idea touches Hopf, Clifford, Pauli, Dirac, contact, gerbe, or MERA composition, defer it to Tier D or later lanes.
- Write at least 6 new canonical shell-local probes.

## Worker B4 — Flux / U(1)
Worker id: B4
Model tier: Haiku
Scope: `flux_*`, `u1_*`
Target minimum: 6 new canonical shell-local probes
Existing shell-local anchors already visible:
- `system_v4/probes/sim_flux_stokes_cell_shell_canonical.py`
- `system_v4/probes/sim_u1_orientation_holonomy_shell_canonical.py`
- `system_v4/probes/sim_u1_wilson_loop_distinguishability_shell_canonical.py`
- `system_v4/probes/sim_u1_gauge_admissibility_constraint_shell_canonical.py`
- `system_v4/probes/sim_u1_structure_matrix_shell_canonical.py`
- `system_v4/probes/sim_u1_carrier_phase_shell_canonical.py`
B4 per-layer report path: `~/wiki/projects/codex-ratchet/tier_b_flux_u1.md`

B4 worker instruction block:
- Treat this as a new category lane with standard QED-style U(1) gauge formulation only.
- Keep work shell-local only; probe coupling to Pauli carriers may be named as a shell-local admissibility surface but never run as actual coupling.
- Fill gaps around gauge phase, holonomy, Wilson loops, local flux orientation, local admissibility constraints, and shell-local probe distinguishability.
- Write at least 6 new canonical shell-local probes beyond the already-visible anchors.

## Worker B5 — Clifford / Pauli
Worker id: B5
Model tier: Haiku
Scope: `clifford_*`, `pauli_*`
Target minimum: 4 new canonical shell-local probes
Current visible inventory signals:
- `clifford_*` corpus is large and includes many non-shell-local files; keep tight shell-local discipline
- `pauli_*` corpus is smaller and has room for isolated generator, algebra, and probe-local shell work
B5 per-layer report path: `~/wiki/projects/codex-ratchet/tier_b_clifford_pauli.md`

B5 worker instruction block:
- Inventory `clifford_*` and `pauli_*` files, then narrow to isolated algebra / generator / rotor / basis / probe-local surfaces only.
- No Weyl/Hopf coupling, no bridge claims, no cross-layer stack files.
- Prefer exact isolated algebra questions: admissible generator families, shell-local operator closure, rotor-local distinguishability, isolated probe response.
- Write at least 4 new canonical shell-local probes.

## Auditor — Tier B runner/result audit
Worker id: B-audit
Model tier: Haiku
Scope: `~/wiki/projects/codex-ratchet/tier_b*.md`, `ops/queue_tier_b.txt`, `overnight_logs/sim_runner_current.log`, claimed Tier B probe files/result JSONs
Output path: `~/wiki/projects/codex-ratchet/tier_b.md`

Auditor instruction block:
- Do not start until layer workers report probe-writing complete.
- Tail `overnight_logs/sim_runner_current.log` until all claimed Tier B probes show DONE or FAIL.
- For each claimed probe verify:
  - file exists
  - `SIM_TEMPLATE` conformance
  - runner reports DONE, not FAIL
  - result JSON has `classification = "canonical"`
  - at least one `load_bearing` tool present
  - positive + negative + boundary sections present
  - no cross-layer coupling in the probe body or result narrative
- Summarize per-layer counts and any failures.
- Rewrite `~/wiki/projects/codex-ratchet/tier_b.md` with gate evidence and blocker list if any remain.
- Telegram L3 once on gate pass or blocker only.

## Historical pre-launch controller checklist

Do not spawn workers from this page. The checklist below is preserved only as
the plan-era controller procedure.

1. Re-read `~/wiki/projects/codex-ratchet/tier_a.md` and `~/wiki/projects/codex-ratchet/STATUS.md`.
2. Require explicit green gate signal for Tier A.
3. Check runner live: `ps aux | grep '[s]im_runner.sh'` and tail runner log.
4. Run `git status --short`.
5. Check `/tmp/hermes_active_scopes.txt` for Tier B scope collisions.
6. Append Tier B controller startup line to `~/wiki/projects/codex-ratchet/_steward_log.md`.
7. Plan-era spawn step: B1–B5 in one batch if scope remains disjoint.
8. Spawn auditor only after writing/enqueue phase completes.

## Controller stop rules
- If Tier A is not green: do nothing except keep the watch armed.
- If runner is down at launch time: report blocker, do not spawn Tier B writers.
- If `git status --short` shows non-empty unsafe drift at launch time: report blocker, do not spawn.
- If a sibling Hermes terminal already owns Tier B scopes: pause and report blocker.
- If any worker drifts into coupling or bridge lanes: stop that worker and respawn with tighter scope.

## Expected artifacts after successful Tier B run
- `~/wiki/projects/codex-ratchet/tier_b.md`
- `~/wiki/projects/codex-ratchet/tier_b_gtower_gstack.md`
- `~/wiki/projects/codex-ratchet/tier_b_hopf.md`
- `~/wiki/projects/codex-ratchet/tier_b_weyl.md`
- `~/wiki/projects/codex-ratchet/tier_b_flux_u1.md`
- `~/wiki/projects/codex-ratchet/tier_b_clifford_pauli.md`
- queue additions in `ops/queue_tier_b.txt`
- append-only events in `~/wiki/projects/codex-ratchet/_steward_log.md`

## Current watch state
Historical watch state at the time of writing: this plan was ready for immediate worker launch once Tier A gate showed green. It is not an executable current instruction.
