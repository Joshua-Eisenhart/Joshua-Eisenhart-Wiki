---
title: Sim Corrections And Classifications
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, simulation, corrections]
sources:
  - raw/articles/new-docs/SIM_CORRECTIONS_AND_CLASSIFICATIONS.md
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/formal-scout-readiness-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/lego-sim-contract-current.md
framing: historical_correction_ledger
---

# Sim Corrections and Classifications

## Overview
Date: 2026-04-05. Source: Hermes audit + Opus verification. Records corrections applied to earlier sim reports and classifies all sims by evidence quality.

Status boundary: this is an April correction/classification snapshot. It can explain why older reports changed, but it is not current validator or promotion authority. Current status lives in [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]], [[specs/codex-ratchet/formal-scout-readiness-status|formal-scout-readiness-status]], and the current repo receipts.

## Corrections Applied

### 1. Torus entropy peak location
Earlier: peak at eta=0.687. Correction: Clifford. Verification: at 10 cycles eta=0.76, at 200 cycles eta=0.76. NEAR Clifford (0.79) but not exactly. 50-cycle run showed anomalous peak at outer edge. Status: Clifford is the long-run attractor for entropy peak, but convergence is not monotonic. Peak region: eta~0.76-0.79.

### 2. Swapped inductive/deductive order
Earlier: C=0.040 (10 cycles). Correction: C=0.013 at 20 cycles. Not zero but severely degraded (0.16x baseline). Label earlier as "10-cycle transient."

### 3. Gudhi persistent homology
Betti_1 = 0 for long trajectories. Type 2 has one finite-persistence H1 interval but no true persistent loop. Do not describe trajectories as closed loops.

## Sim Classification

### April Source Highest-Evidence Bucket
April source-reported bucket: F01+N01 checks reported, commutative kills C. layer1: 15/15 fences, all violations kill. layer2: C^2, S^3, Hopf reported. layer3: fiber stationary, base traversing. layer4: L/R anti-aligned. layer5: 4 topologies forced by su(2). negative_sim_battery: 12 ablations, 6 killed, 4 severely hit. gauge_group: su(2)xu(1)=electroweak. engine_earned_entanglement: T1 accumulates, T2 dissipates. per_stage: Fi=only builder. ratchet_irreversibility: never returns to initial. Current verification/promotion requires repo receipts.

### Good Evidence (verified but not yet layered)
Bridge family comparisons, entropy sweep results, loop order tests.

### Diagnostic Only
Tool integration sims, snapshot checks, single-state probes.

## Related pages
- [[sim-session-index]]
- [[current-preaxis-status-and-ordering-note]]
- [[current-pre-axis-sim-status-keep-open-diagnostic-broken]]
- [[lego-sim-contract]]
- [[specs/codex-ratchet/lego-sim-contract-current]]
