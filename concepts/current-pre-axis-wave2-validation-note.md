---
title: Current Pre-Axis Wave2 Validation Note
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, simulation, validation]
sources:
  - raw/articles/new-docs/archive_old/CURRENT_PRE_AXIS_WAVE2_VALIDATION_NOTE.md
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/formal-scout-readiness-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/lego-sim-contract-current.md
framing: historical_validation_snapshot
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Current Pre-Axis Wave-2 Validation Note

## Overview
Historical snapshot dated 2026-04-04. Status: do not treat as closure. Records specific wave-2 simulation results that were validated in that wave.

Status boundary: read "current" here as current to the 2026-04-04 wave, not current to the repo. The listed PASS items remain dated result claims unless refreshed through current repo receipts and validators.

Artifact availability note: the exact result JSON filenames cited below were not present in the current checkout during the 2026-05-21 wiki audit. The two pytest files exist under `system_v4/tests/`, not top-level `tests/`.

## Validated Results
- sim_a0_kernel_discriminator.py -> PASS. Winner: K1_Ic (coherent information), score 5/6. Results in a0_kernel_discriminator_results.json.
- sim_c1_mispair_probe.py -> PASS. Verdict: operator-driven mispair behavior. That artifact set supports an operator-structured mismatch diagnosis, but not the older `Fe/Fi universally entangling` summary. Results in `c1_mispair_probe_results.json`.
- sim_xi_bridge_bakeoff.py -> PASS. Least-arbitrary bridge family: chiral. Results in xi_bridge_bakeoff_results.json.
- sim_history_vs_pointwise_ax0.py -> PASS. Pointwise and history-window families remain distinct; no collapse claimed. Results in history_vs_pointwise_ax0_results.json.

## Additional Validation
The source note reported pytest tests passed: 16/16 on `test_pimono_fail_closed_edge_cases.py` and `test_pimono_runner_roundtrip_smoke.py`. In the current checkout these files are under `system_v4/tests/`.

## What This Note Does NOT Claim
- No Axis-entry closure
- No Tier 5 closure
- No C1 closure
- No Type2 Weyl inversion resolution
- No claim that pointwise and history-window families should be merged

## Related pages
- [[current-pre-axis-sim-status-keep-open-diagnostic-broken]]
- [[current-pre-axis-sim-status-wave1-refresh]]
- [[current-preaxis-status-and-ordering-note]]
