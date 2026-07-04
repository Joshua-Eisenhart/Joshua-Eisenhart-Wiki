---
title: Executable Root-Axiom Micro-Sims
created: 2026-04-14
updated: 2026-05-21
type: concept
framing: source_present_result_partial_snapshot
tags: [formal-methods, constraints, distinguishability, simulation, axioms]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_f01_finite_state_set.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_f01_finite_measurement_set.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_f01_finite_hilbert_dim.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_f01_quotient_well_defined.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_n01_noncommutation_generic.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_n01_composition_order_distinguishes.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_n01_composition_order_distinguishes_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_n01_identity_via_indistinguishability.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_n01_indiscernibility_implies_identity.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_n01_pauli_algebra_closure.py
missing_result_receipts:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_f01_finite_state_set_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_f01_finite_measurement_set_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_f01_finite_hilbert_dim_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_f01_quotient_well_defined_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_n01_noncommutation_generic_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_n01_identity_via_indistinguishability_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_n01_indiscernibility_implies_identity_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_n01_pauli_algebra_closure_results.json
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Executable Root-Axiom Micro-Sims

## Purpose
This page turns the root axioms into a public executable cluster instead of leaving them only as doctrine sentences or scattered probe files.

## Role in the live wiki cluster
- Strongest use: route readers from the root-constraint doctrine into the new bounded probes that directly test F01 and N01.
- Weak use: declaring the whole root-axiom lane complete.
- Authority boundary: in this maintenance pass the artifacts below are summarized at `exists` unless a fresh rerun is cited.

## Packet snapshot
An explicit micro-sim packet for the two root constraints was recorded for this maintenance pass, but the exact current artifact links in this page need refreshing before it is read as a live artifact-layer census.

Source/result status in this 2026-05-21 source-path pass:
- the listed probe scripts are present
- only the composition-order result link was found at the old exact path
- the other old result receipt paths are listed in frontmatter as `missing_result_receipts`

Safe public label in this maintenance pass:
- source-present / result-link-partial, not rerun-backed and not a live artifact census

## F01 packet
F01 is represented here by direct bounded probes for:
- finite state set
- finite measurement set
- finite Hilbert dimension
- quotient well-definedness

Representative artifact behavior:
- `sim_axiom_f01_finite_measurement_set.py` uses z3 load-bearing to force distinct measurement indices in a finite set and return UNSAT for the pigeonhole violation case
- the same file uses SymPy supportively to exhibit the canonical finite Pauli measurement triad

## N01 packet
N01 is represented here by direct bounded probes for:
- generic noncommutation
- composition-order distinction
- identity via indistinguishability
- indiscernibility implies identity
- Pauli algebra closure as a joint F01+N01 carrier instance

Representative artifact behavior:
- `sim_axiom_n01_pauli_algebra_closure.py` uses SymPy load-bearing for symbolic Pauli closure on `C^2`
- torch is used supportively there as a numeric witness layer
- the negative tests explicitly reject a fake commutative-Pauli hypothesis

## Why this matters
This packet changes the public shape of the formal-methods lane in one important way:
- the root constraints are no longer only described as background principles
- they appear here as bounded executable objects with positive, negative, and boundary sections

That makes the lower-most admissibility layer more legible for later ledger normalization.

## What is already present
| Packet | Evidence path | Artifact-side internal field seen in this pass | Safe public label |
|---|---|---|---|
| F01 finite-state/measurement/Hilbert/quotient packet | source scripts are present; old result links are currently missing | dated tranche/source-present claim; not a live result-artifact census | source-present / result-link-missing |
| N01 noncommutation/order/identity/Pauli-closure packet | source scripts are present; only the composition-order result link was found at the old exact path | dated tranche/source-present claim; not a live result-artifact census | source-present / result-link-partial |

## What is still open
1. No fresh rerun was performed in this maintenance pass, so the packet stays below `runs` or `passes local rerun`.
2. Most old result receipt filenames cited by this page are missing in the current checkout and must be restored, relinked to exact current receipts, or rerun under the repo interpreter.
3. The grouped and exhaustive lego ledgers still describe these root constraints mostly as registry pressure rather than as a normalized explicit family.
4. The next useful normalization step is to connect these probes more directly to the root/admission rows in the public registry language.

## Related pages
- [[constraint-on-distinguishability]]
- [[constraint-on-distinguishability-full-math]]
- [[current-formal-methods-core]]
- [[sim-tranche-2026-04-14-axioms-tools-gerbes-motives]]
- [[llm-controller-contract]]
- [[nominalist-translation-rules]]
- [[actual-lego-registry]]
- [[lego-build-catalog]]
