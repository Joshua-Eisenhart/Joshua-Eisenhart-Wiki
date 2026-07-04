---
title: Current Tool Status Operational Classification
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, system, tooling]
sources:
  - /Users/joshuaeisenhart/wiki/raw/articles/new-docs/archive_old/CURRENT_TOOL_STATUS__OPERATIONAL_CLASSIFICATION.md
  - raw/articles/new-docs/archive_old/CURRENT_TOOL_STATUS__OPERATIONAL_CLASSIFICATION.md
framing: legacy
priming: false
spec_mirrors:
  - specs/codex-ratchet/tool-function-receipt-status
  - specs/codex-ratchet/lego-sim-contract-current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Current Tool Status: Operational Classification

## Overview
Classifies tools by their historical operational role in the system. Superseded by [[tooling-status]] as a dated snapshot and by [[specs/codex-ratchet/tool-function-receipt-status|Tool Function Receipt Status]] plus [[specs/codex-ratchet/lego-sim-contract-current|Lego Sim Contract Current Mirror]] for current repo-facing status.

## Tool Roles

### Sim Runners
Execute simulation code and produce result artifacts. Example: `system_v4.runners.run_real_ratchet`. Must produce JSON artifacts in sim_results/. Must declare: role, tier/resolution, tools, artifacts, negatives, promotion status.

### Validators
Check result artifacts against contract requirements. Part of [[current-architecture-core|SIM boot]] audit. Verify: verdict field present, negative controls included, promotion status declared, correct vocabulary.

### Provers
Run formal proof tools (SymPy, z3) to verify mathematical claims. Results become witnesses in the system's evidence structure.

### Geometry Tools
Compute geometric quantities: trace distance, Bures distance, fidelity, Berry phase, quantum Fisher information. Feed into the [[constraint-on-distinguishability-full-math|constraint surface]] evaluation.

### Data Tools
Handle JSON artifacts, graph structures, and result serialization. Include networkx, TopoNetX, and custom graph tools.

## Operational Status Classification
- Tier 1 (core, always needed): sympy, numpy, json, pathlib
- Tier 2 (simulation, frequently needed): qutip, scipy, networkx
- Tier 3 (geometry, specialized): TopoNetX, PyG, custom bridges
- Tier 4 (proof, emerging): z3, formal verification tools

## Related pages
- [[tooling-status]]
- [[current-tool-status-installed-vs-missing-vs-not-wired]]
- [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]]
- [[current-architecture-core]]
