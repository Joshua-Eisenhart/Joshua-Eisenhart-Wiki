---
title: Cross-Model Readout Matrix v0->v1 (Stage 4) — built + fresh-audited
created: 2026-06-08
updated: 2026-06-08
type: session-receipt
tags: [codex-ratchet, stage-4, cross-model-readout, three-engine, scratch-diagnostic]
status: receipt
claim_ceiling: scratch_diagnostic; promotion_allowed=false; formal_admission_allowed=false; identity_assertion=false. No canon, no formal admission, no bridge/physics/IGT/Holodeck truth or identity claim, no Axis0.
---

# cross_model_readout_matrix v0 -> v1

First NEW Stage-4 packet of the 2026-06-08 session (not a rebuild of the six verified scratch envelopes). Reads ONE already-verified finite carrier through multiple model lenses without smuggling canon — the program's compression claim, in bounded form.

## What it is
Shared support = the Clifford-spinor density carrier S, read through 4 lenses (readout maps A_i over the SAME S):
- QIT (von Neumann / subsystem entropy, coherence, purity)
- IGT (win-lose payoff-asymmetry |z_i - z_j|, read ONLY as a lens — no identity claim)
- Holodeck/runtime (deterministic runtime/reachability signature)
- physics/math (Clifford grade content / Pauli-basis invariant)

Three-engine, mode=all_three_full_sims: Julia AUTHORITATIVE (QuantumOptics entropy + CliffordAlgebras grade, load-bearing), JAX (jnp readouts + z3+cvc5 derive-in-solver flip), PyTorch REQUIRED (torch.func.jacrev). Each leg computes locally (reads_peer_result=false); envelope aggregates after. Validates `scripts/validate_three_engine_sim_result.py --require-pytorch` -> ok:true.

## The claim + the v0->v1 harden
LOAD-BEARING CLAIM: the 4 lenses are genuinely DISTINCT readouts of the same carrier, NOT relabelings (escapes the KILLED IGT<->QIT "Rosetta" circular-labeling failure).
- v0 (4-state support): fresh-audited GENUINE-bounded-readout-matrix, but ONE named gap — QIT/IGT/holodeck shared one ordering (only physics reordered), so non-relabeling rested on functional form, not ordering, for 3 of 4 lenses.
- v1 (6-state support, added uniform_mixed + even_parity_mixed): added a DERIVED pairwise inversion-count (co-monotonicity) matrix. Result rows: `[0,4,1,9]`, `[4,0,3,2]`, `[1,3,0,8]`, `[9,2,8,0]`; off-diagonal min = 1 => NO two lenses co-monotone. Identical across all 3 engines. Weakest pair (qit<->holodeck, count 1) has a real witnessed inversion: ghz_phase vs even_parity_mixed (qit 2.6931>1.6363, holodeck 2.5203<2.5275). Non-relabeling now holds by ORDERING for all 4 lenses, not just physics. Gap closed.

## Controls (all value-coupled, flip)
label-shuffle l1=32.76; carrier-erasure collapse 6->1 classes + structure 2.894->0.0; map-erasure(igt) 0.731->0.0; order-reversal 0.742; z3+cvc5 derive-in-solver unsat->sat (both solvers); torch.func.jacrev same-axis 0.0 / cross-axis 0.366.

## Audit
Both v0 and v1 fresh-audited by a fresh-context auditor that RE-RAN all three legs and RE-COMPUTED the inversion matrix from raw values (builder's verdict not trusted). v1 verdict: **gap-closed-genuine** (passes-local-rerun). One robustness nit (SMT biased_probs hand-transcribed literal, verified == carrier diagonal; could be pulled programmatically in a future pass — not a correctness failure).

## GAINED / NOT_GAINED
GAINED: the same finite carrier admits 4 genuinely-distinct model readouts; distinctness proven by (a) carrier-erasure collapse and (b) pairwise ordering inversions for every lens-pair. NOT_GAINED: no identity between lenses, no canon, no formal admission, no bridge/physics/IGT/Holodeck truth claim, no Axis0.

## Files
- system_v5/ops/formal_scouts/foundation_cross_model_readout_matrix_v1_{envelope,jax,pytorch}.py
- system_v5/julia_carrier/foundation_cross_model_readout_matrix_v1_julia.jl
- results/foundation_cross_model_readout_matrix_v1_{envelope,jax,pytorch}_results.json + julia_carrier/results/..._julia_results.json
- v0 siblings under the same names with _v0_.

cf [[projects/codex-ratchet/manifold-layers-and-sim-queue-capture-2026-06-08]] (Stage 4 + cross-model readout = the next frontier) [[projects/codex-ratchet/read-first]].
