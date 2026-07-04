---
title: Tier Status (2026-04-05 Snapshot)
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, simulation, status]
sources:
  - raw/articles/new-docs/TIER_STATUS.md
framing: historical_preaxis_snapshot
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Tier Status (2026-04-05 Snapshot)

## Overview
Date: 2026-04-05. Historical pre-Axis snapshot. Vocabulary: survived/killed/open/not_yet_tested. NOT pass/fail -- this system falsifies what it can and reports what remains. "Tiers" are resolution levels for finite exploration of M(C), not floors in a building. Do not use this page as live repo status; use the current spec mirrors and repo receipts for current B2/B3/B5 truth.

## Resolution 0-2: Root Constraints and Charter (Analytical)
Resolution 0 (F01+N01): DOCTRINAL -- not mechanically executed. z3 predicates exist but never run. Resolution 1 (Admissibility Charter): DOCTRINAL -- charter written, no executable validator. Resolution 2 (M(C) Characterization): DOCTRINAL -- defined in prose, no computational characterization.

## Resolution 3+: Sims Begin

### Resolution 3: Geometry/Operator Basis
OPEN (Type1 survived, Type2 open). B3.1 basis remap: survived. B3.2 coord change: survived (SymPy proof). B3.3 noncomm ablation: survived (SymPy proof). B3.4 all 4 operators load-bearing: survived. Type1 crosscheck: survived. Type2: fully_matches=false -- OPEN.

### Resolution 4: Weyl Layer
OPEN (Type1 survived, Type2 open). Weyl geometry ladder audit: holonomy varies across torus, signatures separable. Type2 inversion still open.

### Resolution 5: Bridge Xi
OPEN. Xi bridge bakeoff: chiral least-arbitrary (composite 0.80, only family with I_c>0 everywhere). History-window leads pointwise by ~0.93 MI. No winner selected.

### Resolution 6: Cut A|B
PARTIAL. C2 (entropy structure): historical source label survived / keep open -- VN entropy is necessary. C1 (entanglement witness): PARTIAL -- MI-based negatives not killed (0/16), concurrence/negativity kill fake coupling (16/16), mispair 8/16 killed.

### Resolution 7: Kernel
INFORMATIVE but embargoed. K1_Ic (coherent information) wins 5/6 vs MI 4/6. Does NOT unlock Tier 7 until Tiers 3-6 close.

### Resolution 8: Edge Writeback
SURVIVED. Source snapshot claimed the JSON artifact existed; not confirmed in the 2026-05-21 checkout audit. P1-P5 all pass in the source snapshot. 7/7 dynamic slot columns with nonzero variance.

## Detailed Sim Results
Resolution 3: B3.1 basis remap survived, B3.2 coord change survived (SymPy proof), B3.3 noncomm ablation survived (SymPy proof), B3.4 all 4 operators load-bearing survived. Type1 crosscheck survived. Type2: fully_matches=false (OPEN). Resolution 4: Weyl-ambient rung has independent witness survived, holonomy varies across torus, witness_separable=true. Resolution 5: Chiral bridge composite 0.80, I_c>0 on all 6 configs. History-window leads pointwise by MI gap ~0.93. Resolution 6: C2 entropy structure SURVIVED (8/8 VN-positive stages, Shannon/purity shortcuts killed). C1 entanglement witness: MI-based fake_coupling_kill_count=0 (MI does NOT kill fake coupling). (from TIER_STATUS.md)

## Related pages
- [[current-preaxis-status-and-ordering-note]]
- [[current-pre-axis-sim-status-keep-open-diagnostic-broken]]
- [[ladders-fences-admission-reference]]
- [[constraint-on-distinguishability-full-math]]
