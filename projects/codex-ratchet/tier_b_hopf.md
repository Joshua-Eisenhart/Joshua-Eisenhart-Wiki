last_updated: 2026-04-17T08:49:02Z

# Tier B Hopf

Historical Tier B Hopf worker report. Written/enqueued/canonical wording
records April source/workflow state only; no sims were executed in this pass,
and current status requires live repo receipts.

Historical source-write status: written
Worker: B2
Scope: `hopf_*`
Lane discipline: shell-local only; pairwise / triple / topology-variant / emergence / bridge files excluded from new work.

## Inventory summary

Tracked Hopf-primary inventory before new B2 probes:
- shell-local total: 16
  - canonical: 10
  - classical_baseline: 4
  - broken / non-conformant helper surfaces: 2
- non-shell-local total: 40
  - canonical: 3
  - classical_baseline: 37
  - broken: 0

### Existing shell-local canonical
- `sim_hopf_connection_curvature_operators.py`
- `sim_hopf_deep_berry_phase_admissibility.py`
- `sim_hopf_deep_fiber_winding_number_bound.py`
- `sim_hopf_deep_s3_to_s2_partial_trace_consistency.py`
- `sim_hopf_deep_u1_holonomy_equivariance.py`
- `sim_hopf_fiber_equivalence.py`
- `sim_hopf_fibration_constraint_canonical.py`
- `sim_hopf_foliation_structure.py`
- `sim_hopf_symplectic_contact_torch_canonical.py`
- `sim_hopf_torch_foundation.py`

### Existing shell-local classical_baseline
- `classical_baseline_hopf_fibration.py`
- `sim_hopf_fibration_embedding_classical.py`
- `sim_hopf_pointwise_pullback.py`
- `sim_hopf_torus_lego.py`

### Existing shell-local broken / non-conformant
- `hopf_manifold.py` — utility/helper surface, not a SIM_TEMPLATE probe
- `hopf_torus_meta_sim.py` — legacy meta-sim, not shell-local Tier B process-conformant

### Non-shell-local boundary surfaces (inventory only; not modified)
Count only: 40 files.
These are mostly `pairwise_coupling`, `triple_coexistence`, `topology_variants`, `emergence_quantities`, and `bridge_claims` packets, plus multi-shell coupling chains. They were treated as anti-pattern boundaries for this Tier B pass and not used as targets.

## Shell-local gaps identified

From the existing shell-local inventory plus Hopf concept matches in `~/wiki/concepts/`, the open shell-local gaps were:
- local north/south section overlap transition law as its own bounded packet
- explicit horizontal-projector / vertical-removal constraint as its own packet
- explicit horizontal-lift 2π sign-flip / 4π closure packet
- explicit torus rank stratification packet: interior rank-2 torus vs boundary circle collapse
- explicit base-image + fiber-phase reconstruction packet
- explicit vertical-vs-horizontal response split at the Hopf map level
- explicit local connection gauge-transition packet separated from broader connection/curvature coverage

These stay inside harness step 1: shell-local objects and probes well-defined in isolation. Anything requiring another layer was deferred implicitly by not building it here.

## Historical B2 Source-Label Probe Writes

No sims were executed in this pass. `canonical` below is the dated source/queue
label, not current `canonical by process`.

1. `sim_hopf_section_overlap_transition.py`
   - chart-overlap law for north/south local sections
   - load-bearing tools: `sympy`, `pytorch`, `z3`
   - commit: `12530b119`

2. `sim_hopf_horizontal_projector_constraint.py`
   - principal connection projector, vertical removal, horizontal idempotence
   - load-bearing tools: `sympy`, `pytorch`, `z3`
   - commit: `5dce7584b`

3. `sim_hopf_horizontal_lift_closure.py`
   - horizontal equator lift: sign flip after `2π`, closure after `4π`
   - load-bearing tools: `sympy`, `pytorch`
   - supportive: `z3`
   - commit: `dc42b20e8`

4. `sim_hopf_torus_rank_stratification.py`
   - nested-torus interior rank vs boundary degeneration
   - load-bearing tools: `sympy`, `pytorch`, `z3`
   - commit: `65424096b`

5. `sim_hopf_base_section_phase_recovery.py`
   - reconstruction from base image plus one fiber phase
   - load-bearing tools: `sympy`, `pytorch`
   - supportive: `z3`
   - commit: `5fee5cb78`

6. `sim_hopf_vertical_horizontal_response.py`
   - zero vertical Hopf-image response vs nonzero horizontal response
   - load-bearing tools: `sympy`, `pytorch`
   - supportive: `z3`
   - commit: `f012af014`

7. `sim_hopf_connection_gauge_transition.py`
   - local north/south connection-form gauge transition on the overlap
   - load-bearing tools: `sympy`, `pytorch`
   - supportive: `z3`
   - commit: `b7d4f9ece`

## Queue append state

Appended to `ops/queue_tier_b.txt`:
- `sim_hopf_section_overlap_transition`
- `sim_hopf_horizontal_projector_constraint`
- `sim_hopf_horizontal_lift_closure`
- `sim_hopf_torus_rank_stratification`
- `sim_hopf_base_section_phase_recovery`
- `sim_hopf_vertical_horizontal_response`
- `sim_hopf_connection_gauge_transition`

## Steward log state

Canonical one-line steward entries were appended for each committed probe in `~/wiki/projects/codex-ratchet/_steward_log.md`.

## Stop state

No sims were executed.
No coupling / bridge / emergence work was added.
Work stopped after writing, per-probe committing, enqueueing, steward-log append, and layer-report rewrite.
