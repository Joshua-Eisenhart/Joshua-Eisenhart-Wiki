---
title: Readme First V2 7
created: 2026-04-28
updated: 2026-04-28
type: concept
tags: [wizard, mmm, packet, receipt]
framing: current
source_path: README_FIRST_v2_7.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# README First v2.7

Status: repaired validated candidate; not wired into any runtime.

Validation receipts now live inside this packet:
- Full local Wizard run: `runs/wizard_local_run_latest/`
- Size bakeoff: `runs/wizard_general_bakeoff_latest/` (`standard` won for runtime use; `full` remains reference/debugging size)
- Proof/graph manifest: `runs/wizard_proof_manifest_latest/proof_validation.json`
- Full-format repair run: `runs/wizard_full_format_repair_latest/` (non-collapsed output with V1-V9/L10-L14/G15-G18/C19-C22)
- External Opus advisory run: `runs/opus_20_wave_advisory_20260428/` (20 Task calls completed; advisory-only, Codex decided writes)

Current taxonomy counts:
- compact_checks_guards_json: 3
- compact_compositions_json: 4
- compact_controller_acts_json: 1
- compact_lanes_json: 5
- compact_system_routes_json: 2
- compact_voices_json: 9
- full_checks_guards_json: 3
- full_compositions_json: 4
- full_controller_acts_json: 1
- full_lanes_json: 5
- full_system_routes_json: 2
- full_voices_json: 9
- standard_checks_guards_json: 3
- standard_compositions_json: 4
- standard_controller_acts_json: 1
- standard_lanes_json: 5
- standard_system_routes_json: 2
- standard_voices_json: 9
- ultra_checks_guards_json: 3
- ultra_compositions_json: 4
- ultra_controller_acts_json: 1
- ultra_lanes_json: 5
- ultra_system_routes_json: 2
- ultra_voices_json: 9

Load only current positive boot paths, the assigned language body, and task-provided files. Only current candidate material is bundled.

Local tools:
- `tools/run_wizard_system.py` writes route receipts, final answer, and validation reports.
- `tools/run_wizard_general_bakeoff.py` compares ultra/compact/standard/full Wizard General sizes.
- `tools/run_wizard_proof_manifest.py` runs wiki formal harness, Wizard receipt tests, and a Weyl graph proof check.
- `tools/refine_wizard_mmm_language.py` rebuilds the MMM JSON/Markdown language bodies without boot-visible metadata noise.
- `tools/package_wizard_candidate.py` writes a deterministic zip plus checksum receipt.

Build-mode additions:
- `current/WIZARD_QIT_BUILD_MODE_v2_7.md` points Wizard runs at the wiki QIT read pack, sim admission router, and proof/graph gates.
- The wiki is the universal source; Claude, Codex, Hermes, and other runtimes derive adapters from it rather than mutating this packet directly.
