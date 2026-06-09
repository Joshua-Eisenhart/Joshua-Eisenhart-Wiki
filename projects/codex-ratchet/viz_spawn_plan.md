# VIZ spawn plan

Archived worker prompt from 2026-04-17. Do not execute directly; commit and
spawn instructions below are historical examples only.

last_updated: 2026-04-17

Historical worker batch described at time of writing; do not spawn from this page:

1. VIZ-8
- Scope: `system_v4/visualization/viewers/scrubber_pyvista.py`, `system_v4/tests/test_viz_scrubber_load.py`
- Goal: slice 8 witness/exclusion timeline overlay in live scrubber
- Success: targeted scrubber tests pass, then full `system_v4/tests/test_viz_*.py -q` passes, commit `tier-viz/8: ...`

2. VIZ-9
- Scope: `system_v4/visualization/reporting.py`, `system_v4/visualization/inspection.py`, `system_v4/tests/test_viz_report.py`, related viz tests if needed
- Goal: slice 9 lane-admission gate visualization in reporting/inspection surfaces
- Success: targeted report/inspection tests pass, then full `system_v4/tests/test_viz_*.py -q` passes, commit `tier-viz/9: ...`

3. VIZ-MANIM
- Scope: `scripts/render_manim_*.py`, `system_v4/tests/test_viz_manim_*.py`, supporting scene-only files if needed
- Goal: render an actual Manim scene visualizing D1 UNSAT certificates from `boundary_g_to_hopf_admissibility_results.json`; show admitted E6 Hopf S^3, excluded S^7 on A1, excluded winding=0
- Success: scene file updated, actual render attempted in active runtime, targeted tests updated, commit `tier-viz/7b: ...` or blocker recorded if runtime gate remains

Shared constraints:
- Every worker reads `~/wiki/wizard/harness-consolidated/00_READ_FIRST.md` first.
- Respect `ops/HERMES_RULES.md`, `ops/OVERNIGHT.md`, `ops/TIER_VIZ.md`.
- No cross-tier edits.
- Commit each slice when finished.
- Report only completion or blocker.
