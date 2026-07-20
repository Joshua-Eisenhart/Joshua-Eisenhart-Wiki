---
title: QIT engines as a perception program
created: 2026-07-19
updated: 2026-07-19
type: concept
tags: [qit, engines, perception, quantum, world-engine]
sources:
  - system_v8/loop3_senses/LOOP3_FOUNDATION_CARD.md
  - system_v8/loop3_senses/visibility_sanity_gate.py
  - system_v8/engines_perception/engine_processor_v0.py
  - system_v8/engines_perception/processor_at_scale.py
  - system_v8/loop2_world/perception_intelligence_v0.py
  - system_v8/nested_manifold/stage64_constraint_tournament.py
  - owner-pack-RATCHET_189 (deliverable_189/01_MAIN_IDEAS.md)
  - owner-pack-RATCHET_188 (WHY_64_CANDIDATES_16_OPERATE_187.md)
framing: current
status: research-note
---

# QIT engines as a perception program

## The admission criterion: perception is not free

An engine's information processing counts as perception only if it clears a fail-closed gate, not by running or producing plausible-looking output. `LOOP3_FOUNDATION_CARD.md` states the binding correction directly: "FAIL-CLOSED VISIBILITY SANITY GATE before ANY carrier scaling" (`system_v8/loop3_senses/LOOP3_FOUNDATION_CARD.md:9`). The negative case that forced this rule is Pack 188: its recurrent body has "NO perception: rho_{t+1}=F(rho,d,G) has no object argument => chi(O:rho)=0 provably; its single attractor is an eraser" (same file, line 6). A density update with no object argument cannot carry object information by construction — the gate exists because that failure mode is real, not hypothetical.

## The visibility gate, G1–G5

`system_v8/loop3_senses/visibility_sanity_gate.py` implements five named checks (`checks["G1"]`…`checks["G5"]`, lines 979–1066):

- **G1** `raw_views_have_object_predictive_information` — held-out bitwise accuracy on raw partial views exceeds max(train-selected chance, shuffled-label p95) by more than 0.02.
- **G2** `observation_encoder_alters_density_conditionally` — the density update is physical CPTP, both outcome branches separate from the same parent at every stage position, at least 95% of different-view state pairs separate, and frozen/deterministic-replay controls behave.
- **G3** `holevo_object_information_above_shuffled_labels` — for every view k=0..5, categorical Holevo chi(full 8-bit object word O; rho_k) exceeds that k's shuffled-label p95 by more than 1e-6 bits.
- **G4** `simple_density_probe_beats_chance_under_full_visibility` — at every k, a 15-Pauli ridge probe beats train-selected chance.
- **G5** `carrier_comparison_eligibility_only` — true only if G1–G4 all pass; even then the correction "performs zero carrier comparisons" (script docstring, lines 6–7).

Fail-closed is implemented, not asserted: the output directory refuses reuse (`refuse_to_reuse`, line 122), any exception writes a receipt with every gate forced `False` (`fatal_receipt`, lines 700–744), and a `--fix-v1` rerun is refused unless the parent receipt is a retained failure whose diagnosed `fix_v1_mode` matches the requested fix (lines 1222–1236). The card's own summary of the rule: "Any gate red = stop, fix, rerun" (`LOOP3_FOUNDATION_CARD.md:14`).

### Executed receipts

The v3 original run failed closed: G1 pass (accuracy 0.85 vs chance 0.494, shuffled p95 0.550), G2 pass, **G3 fail** (per-k margins over shuffled p95 `[0.0397, 0.0088, 0.0023, 0.00004, -0.0044, -0.0034]`, negative at k=4,5), **G4 fail** (pooled accuracy 0.606 vs chance 0.494, but per-k margins go negative at k=2 and k=5), G5 correctly false (`system_v8/loop3_senses/results/visibility_sanity_gate_v3/receipt.json`, `checks`, `all_pass: false`, `accepted_status_label: "runs"`). Diagnosis routed to the `update` component with a proposed `update_residual` fix.

The `fix_v1` rerun (adding a 0.5 view-local residual to the persistent density after each view) passed all five gates: G3 margins `[0.0397, 0.0268, 0.0356, 0.0624, 0.0716, 0.0920]` (all positive), G4 per-k margins `[0.2375, 0.1188, 0.0875, 0.1688, 0.2625, 0.2000]` (all positive, pooled 0.769 vs chance 0.494), G5 `carrier_comparison_eligible: true`, `all_pass: true`, `accepted_status_label: "passes local rerun"` (`.../visibility_sanity_gate_v3/fix_v1/receipt.json`). Claim ceiling stays explicit throughout: `promotion_allowed: false`, `carrier_comparison_executed: false` — passing the gate makes carrier comparison *eligible*, it does not execute one.

## E1/E2 and the L/R (and Type-1/Type-2) namings — three sources, not collapsed

`LOOP3_FOUNDATION_CARD.md` names the asymmetry abstractly: "Two engines: E1 candidate-first confirmation (predict->probe->correct); E2 measurement-first reconstruction (measure->reconstruct->counterprobe). Both contain deduction+induction; asymmetry = which loop conditions which" (line 27). No executed sim in the read set runs an E1/E2-labeled pair by that name.

What is executed is a different-but-related asymmetry: `engine_processor_v0.py` runs a LEFT engine (plain stage64 L-side generators) against a RIGHT engine (complex-conjugated generators, reversed schedule order) — see the "L/R asymmetry vector" (lines 527–539). Measured results: `admaccL=0.5625`/`admaccR=0.5000`, `bitaccL=0.7812`/`bitaccR=0.8438`, `chiL=0.2892`/`chiR=0.2528`, profile L2 distance 0.2872, admissibility-error Hamming 2, bit-error Hamming 12 (`system_v8/engines_perception/results/processor_v0/receipt.json`, findings). A third naming appears in `WHY_64_CANDIDATES_16_OPERATE_187.md`: "Type-1" and "Type-2" engines, distinguished by which of 8 stages is outer/inner-loop and by deduction/induction cycle direction (stage table, lines 28–45), with the note that "Their conceptual coupling is through the joint state and whole manifold, not an accidental serial causal arrow" (line 49). E1/E2, L/R, and Type-1/Type-2 are held here as three distinct namings pending an explicit reconciliation receipt — the source files do not state they are the same object.

## Objects as action-conditioned predictive quotients

The card states the operational definition directly: "Objects = action-conditioned predictive quotients: h ~ h' iff sup_{pi,T} D(P(T|h,pi),P(T|h',pi)) <= eps. Simulator IDs are scaffolding; merge/split/refine/Purgatory per probes. LLM may narrate but cannot write an object without a perception receipt" (`LOOP3_FOUNDATION_CARD.md:24-26`). `01_MAIN_IDEAS.md` gives the same shape for the Holodeck program: "an object is an equivalence class that stays sufficient across a declared family of action-conditioned future tests," `x~_O x' iff` the admitted action-conditioned future probes cannot distinguish them at the required scale (section 9). The contrast with objects-as-primitives is explicit in both sources: identity is never `A=A`, it is a probe-relative equivalence class that a later intervention can split (section 1 of `01_MAIN_IDEAS.md`), and in `visibility_sanity_gate.py` the object variable is deliberately the categorical full 8-bit word, not a simulator ID (`object_variable_definition` field, receipt).

## Stage-per-qubit and "engines = compression"

Not in the primary read set but owner-attributed and dated the same day: an owner statement (2026-07-19, during the spinor-JEPA tournament v0) reaffirms a 3-qubit minimum from independent loop-2 evidence ("2-qubit register capacity-limited (occluded acc 0.54 vs twin 0.60, Bayes 0.88; belief Holevo at null; no gain from full visibility)"), proposes the stage-per-qubit hypothesis — "each engine stage of an engine may need its own qubit — 8 stages -> up to 8-qubit engine register, stage k reading/writing qubit k with cross-qubit coupling" — and states "ENGINES = COMPRESSION: the engines are the way all this complexity gets compressed — the stage-structured register manages 2^n complexity through n stage-typed operations" (owner memory note, `feedback_loop_foundations_stage_qubit_compression.md`). This is stated as an untested hypothesis with a named test design (register scaling ladder 2->3->4->8 qubits, structured-vs-unstructured register at matched dimension), not an executed result in the files read for this note.

## The state tuple Z = (rho_fast, m_slow, W, G, H)

Given verbatim in the card: "State: Z_t = (rho_fast, m_slow, W_jepa, G_nesting, H_history) — slow memory must survive the fast density's reconvergence (Pack-188 attractor lesson)" (`LOOP3_FOUNDATION_CARD.md:15-16`). Components as named: `rho_fast` is the fast-updating density state (the per-stage register in the executed sims); `m_slow` is slow memory that must persist across the fast state's reconvergence; `W_jepa` is a JEPA-style predictive weight/latent component; `G_nesting` is nesting/geometry structure; `H_history` is retained history. No file in the read set instantiates this five-part tuple as a running data structure — `perception_intelligence_v0.py` and `engine_processor_v0.py` carry `rho` (register density) and an across-word/across-view accumulator, but do not name or implement `m_slow`, `W_jepa`, `G_nesting`, or `H_history` as separate typed fields. The tuple is card-level design, status `exists` (stated in the card) not `runs`.

## The 16-of-64 constraint law

`WHY_64_CANDIDATES_16_OPERATE_187.md` states the count: "16 placements × 4 candidate operators = 64 addresses," "16 active + 48 rejected with witnesses = 64," with a 16-row stage table (Type-1/Type-2 × outer/inner × deduction/induction × 4 terrains) and the claim "Julia, JAX, and PyTorch independently reproduce the same addresses and density readouts. Worst disagreement across three drive values is 6.217248937900877×10⁻¹⁵" (lines 1–51). This cross-engine agreement number is reported in that document; no matching receipt JSON for it was read here, so it is reported as document-stated, not independently reverified from a receipt path in this note.

The executed implementation of the same 16-of-64 shape is `system_v8/nested_manifold/stage64_constraint_tournament.py`, run against a distinct constraint battery: K1 (commutator-norm kill of basis-aligned pairs), K2 (frame-sign selection, relational/argmax), K3 (chirality/flux-sign consistency). Its receipt (`system_v8/nested_manifold/results/stage64/receipt.json`) shows `all_pass: true` with all eleven checks true, including `K1_exactly_2_killed_every_stage`, `K2_frame_sign_load_bearing_flip_changes_operator`, `K3_admitted_flux_matches_sheet_every_stage`, `T_exactly_1_operating_per_stage_16_total`, `D_walls_enumerated_48`. The claim ceiling on that receipt is explicit: "executed finite instance of the 16x4 mutual-constraint tournament; no uniqueness/optimality claim; frame sign declared, not derived" and `promotion_allowed: false`. This K1/K2/K3 tournament and the Type-1/Type-2 deduction/induction stage table in `WHY_64_CANDIDATES...md` describe the same 16-of-64 count but are not shown in the read files to be the identical construction — held here as a second surviving account of "16 of 64," not merged with the first.

## The engines actually process, with honest negatives kept

`engine_processor_v0.py` and its scale-up `processor_at_scale.py` are the executed perception-lane sims feeding this program. Findings kept as honest negatives rather than smoothed: admissibility transfer to held-out packets is "data-limited, not engine-limited" — a full-monomial ridge upper bound on any word-wise readout reaches only 0.5000, and only a held-out-peeking oracle threshold reaches 0.6875 against a 0.6250 majority baseline (`processor_v0/receipt.json` findings). At scale, `pysindy` found no sparse per-stage information-gain law beyond cumulative-series autocorrelation (increment-scrambled control fits as well as real trajectories) — reported as an explicit honest negative in `processor_at_scale.py` (lines 439–450). `perception_intelligence_v0.py` reports the classical ID3 automaton twin matching or beating the QIT engine under occlusion on the loop-2 world task (findings block, "HONEST NEGATIVE KEPT").

## Open / unresolved

- E1/E2 (card), L/R (engine_processor_v0), and Type-1/Type-2 (WHY_64_CANDIDATES) are three distinct namings for engine asymmetry across three sources; no read file states they are the same object, and no reconciliation receipt exists.
- The Z = (rho_fast, m_slow, W_jepa, G_nesting, H_history) tuple is card-stated design, not an implemented data structure in any read sim.
- Stage-per-qubit and "engines = compression" are an owner hypothesis with a named test design, not an executed result.
- The stage64 K1/K2/K3 tournament receipt and the WHY_64_CANDIDATES deduction/induction stage table both claim a 16-of-64 structure; whether they are the same construction is unverified from the files read here.
- The cross-engine (Julia/JAX/PyTorch) agreement figure (6.2×10⁻¹⁵) is document-stated in `WHY_64_CANDIDATES_16_OPERATE_187.md`; no corresponding receipt JSON was located to reverify it independently.
- `visibility_sanity_gate_v3` passes at status `passes local rerun` only for correction 1 of the LOOP3 card; corrections 2 onward (E1/E2 win table, objects-as-quotients merge/split machinery, carrier tournament) are explicitly blocked consumers per that receipt's `blocked_consumers` field, not yet attempted.
