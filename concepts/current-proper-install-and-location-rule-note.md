---
title: Current Proper Install And Location Rule Note
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, system, tooling]
sources:
  - /Users/joshuaeisenhart/wiki/raw/articles/new-docs/archive_old/CURRENT_PROPER_INSTALL_AND_LOCATION_RULE_NOTE.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/Makefile
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/TOOLING_STATUS.md
  - raw/articles/new-docs/archive_old/CURRENT_PROPER_INSTALL_AND_LOCATION_RULE_NOTE.md
framing: legacy
priming: false
spec_mirrors:
  - specs/codex-ratchet/tool-function-receipt-status
  - specs/codex-ratchet/lego-sim-contract-current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Current Proper Install And Location Rule Note

## Overview
Historical working note on install conventions and file location rules for the system. Use the repo Makefile `PYTHON` value and the current specs mirrors for repo-facing work.

Current interpreter authority: `/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3`, from `/Users/joshuaeisenhart/Desktop/Codex Ratchet/Makefile`.

## Key Rules
- April-era sim results went to `system_v4/probes/a2_state/sim_results/`
- April-era sim code lived in `system_v4/probes/`
- Current repo-bound formal-scout work lives under `system_v5/ops/formal_scouts/` with current status in `system_v5/docs/FORMAL_SCOUT_READINESS_INDEX.md` and `system_v5/docs/SIM_ESTATE_INTEGRATION_INDEX.md`
- Export blocks follow the current repo contract and spec mirrors
- Tool installs must be in the venv, not system Python
- Each sim must produce a JSON artifact in the results directory

## Location Discipline
- April-era active sims: `system_v4/probes/`
- April-era sim results: `system_v4/probes/a2_state/sim_results/`
- Current formal scouts: `system_v5/ops/formal_scouts/`
- Current formal-scout results: `system_v5/ops/formal_scouts/results/`
- Current repo-facing status: `system_v5/docs/FORMAL_SCOUT_READINESS_INDEX.md` and `system_v5/docs/SIM_ESTATE_INTEGRATION_INDEX.md`
- Legacy handoffs/reviews: `.agent/handoffs/active/` and `.agent/reviews/active/`
- Boot prompts: defined in [[boot-prompt-templates]]

## Install Rule
Use the Makefile interpreter path when the repo has multiple Python environments. Never use archived Homebrew examples as current Codex Ratchet authority.

## Promotion Blockers
Missing artifact = promotion blocked. diagnostic_only results cannot support geometry claims. No sim may claim results above its declared resolution level.

## Related pages
- [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]]
- [[specs/codex-ratchet/tool-function-receipt-status|tool-function-receipt-status]]
- [[current-architecture-core]]
- [[agent-workflow-and-boot-architecture]]
