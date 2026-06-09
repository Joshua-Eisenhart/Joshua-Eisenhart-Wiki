---
title: Wizard Local Runner V2 7
created: 2026-04-28
updated: 2026-04-28
type: concept
tags: [wizard, mmm, packet, receipt]
framing: current
source_path: current/WIZARD_LOCAL_RUNNER_v2_7.md
---

# Wizard Local Runner v2.7

Status: local receipt runner. Not live wiring.

Run from an extracted packet root:

```bash
python3 tools/run_wizard_system.py \
  --general-size standard \
  --feedback "tiny feedback implemented" \
  --task "Improve and locally run the repaired MMM Wizard packet."
```

Run from the Codex Ratchet repo:

```bash
python3 scripts/run_wizard_system.py \
  --candidate-root work/mmm_wizard_repair/mmm_wizard_complete_system_packet_v2_7_candidate \
  --out-dir work/mmm_wizard_repair/runs/wizard_local_run_latest \
  --general-size standard \
  --feedback "tiny feedback implemented" \
  --task "Improve and locally run the repaired MMM Wizard packet."
```

Run the Wizard General bakeoff from the Codex Ratchet repo:

```bash
python3 scripts/run_wizard_general_bakeoff.py \
  --feedback "tiny feedback implemented" \
  --task "Compare Wizard General sizes and choose the best runtime surface."
```

The runner loads repaired MMM language bodies, writes lane receipts, writes a
final answer, and validates that every visible Wizard lane in that answer has a
receipt row.

`standard` is the default runtime size. `compact` is a cheat sheet, `ultra` is
emergency shorthand, and `full` is reference/debugging material.

Local runner rows use `local_receipt`, not `spawned`, because this runner does
not create live subagents. Receipt validation for these rows must be run with
local-receipt allowance; live acceptance still needs fresh-agent logs.

Scope boundary:
- This proves local packet receipt truth.
- This does not prove live model behavior.
- Live wiring still requires fresh-agent boot logs, unlisted-material block
  receipt, rollback or hold log, and no-MMM versus main-MMM versus mini-MMM
  comparison.
