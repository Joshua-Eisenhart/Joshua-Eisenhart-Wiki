---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [testing, fuzzing, metamorphic, property-based, simulation, falsifier]
sources: []
---

# Property, Fuzz, and Metamorphic Testing Support

## Purpose
This page supports the negative-sim and mass-sim-generator lanes with testing methods that generate many bounded cases without turning volume into proof.

The core role:

Property-based, fuzz, and metamorphic tests are wide-exploration tools. They are valuable because they throw many perturbations at invariants and KILL conditions, then preserve failures as boundary evidence.

## Method roles

### Property-based testing
Use for:
- generating many inputs under a stated domain;
- checking invariants across cases;
- shrinking failures to minimal counterexamples;
- finding edge cases the author did not hand-write.

Good fit here:
- tensor shape invariants;
- density-matrix validity;
- trace/PSD/Hermitian constraints;
- noncommutation swap guards;
- conservation or monotonicity expectations;
- graph/topology carrier constraints.

### Fuzzing
Use for:
- stressing parsers, schemas, runners, and artifact contracts;
- adversarial input generation;
- robustness checks around result JSONs and tool manifests.

Good fit here:
- result schema validation;
- claim table parsing;
- LLM-extracted record safety;
- generated sim templates;
- external source sanitization before Grok/Gemini/Sonnet/Opus review.

### Metamorphic testing
Use when exact expected outputs are hard, but transformations should preserve or predictably change properties.

Good fit here:
- equivalent gauge/coordinate transformations;
- scaling/renormalization checks;
- perturbation monotonicity;
- graph relabeling invariance;
- density-matrix basis changes;
- topology signatures under allowed transformations.

## Why this matters for anti-teleology
These methods let the system explore many possible futures without privileging one future story.

They produce:
- survived cases;
- killed cases;
- shrunk counterexamples;
- open boundaries;
- invariant-preserving transformations;
- invariant-breaking transformations.

That is exactly the basin-emergence pattern.

## Relation to current pages
- [[negative-sims-and-kill-tests-support]]: property/fuzz/metamorphic tests are concrete ways to create KILL boundaries.
- [[mass-sim-generator-wide-exploration-support]]: these methods discipline generated sim packets.
- [[attractor-basin-classifier-case-table]]: row labels can be treated as outputs of a classifier that should be stress-tested.
- [[perturbation-depth-basin-edge-table]]: perturbation rows are a natural metamorphic/parametric test surface.
- [[smt-formal-falsifier-lane]]: SMT complements property testing by proving or killing finite encodings.

## Good test contracts
A generated property/fuzz/metamorphic test should name:
- input domain;
- invariant or metamorphic relation;
- expected witness or KILL condition;
- tool/function used;
- result schema;
- shrink or minimization behavior if applicable;
- claim ceiling.

## MMM sentences
- A counterexample is a compressed boundary.
- Shrinking a failure is finding the smallest edge of the basin.
- Metamorphic tests ask which transformations preserve the claim.
- Fuzzing turns surprise into an audit surface.
- Many generated cases are useful only when the invariant is explicit.


## 2026-05-18 live repo mapping
Live repo scan artifact:
- `/tmp/repo_property_fuzz_metamorphic_scan_20260518.json`

High-signal current surfaces:

`grok_sim` rows in this list are sidequest/proposal or failure-mining surfaces. They require formal-scout translation before they count as repo evidence or canon.

- `system_v5/ops/formal_scouts/results/attractor_basin_success_criteria_receipt_classifier_probe_results.json` — scan score 156
- `system_v4/probes/sim_heat_work_measure_feedback_cycle_invariant_correlation.py` — scan score 91
- `system_v5/ops/formal_scouts/sim_attractor_basin_success_criteria_receipt_classifier_probe.py` — scan score 80
- `system_v4/probes/sim_capability_hypothesis_isolated.py` — scan score 79
- `system_v4/probes/sim_q2_clifford_structure.py` — scan score 70
- `system_v4/probes/sim_integration_hypothesis_z3_property_guard.py` — scan score 59
- `system_v5/grok_sim/loop_runner/proposed_formal_sims/manifold_legos_nonclassical/spatial_temporal_possibility_doc_grounded_rotation_survivor_probe.py` — scan score 58
- `system_v4/a2_state/skill_understanding_index_v1.json` — scan score 57
- `system_v5/grok_sim/loop_runner/proposed_formal_sims/manifold_legos_nonclassical/spatial_temporal_six_dim_rotation_class_survivor_probe.py` — scan score 55
- `system_v5/grok_sim/loop_runner/proposed_formal_sims/manifold_legos_nonclassical/dark_energy_dark_matter_shell_direction_observability_ladder_probe.py` — scan score 54
- `system_v4/a1_state/rosetta_v2.json` — scan score 54
- `system_v4/probes/sim_e3nn_ic_invariance.py` — scan score 52
- `system_v4/probes/a2_state/sim_results/heat_work_measure_feedback_cycle_invariant_correlation_results.json` — scan score 52
- `system_v5/READ ONLY Reference Docs/Older Legacy/Leviathan v3.2 word.txt` — scan score 48
- `system_v4/probes/sim_gopakumar_vafa_invariants_canonical.py` — scan score 46
- `system_v4/visualization/validator.py` — scan score 44
- `system_v4/probes/test_graph_invariants_deep.py` — scan score 44
- `system_v4/visualization/inspection.py` — scan score 43
- `system_v5/READ ONLY Reference Docs/Older Legacy/lev_nonclassical_runtime_design_audited.md` — scan score 40
- `scripts/system_surface_audit.py` — scan score 39


Interpretation:
- Hypothesis is already present as a tool-capability and integration surface, not just a future idea.
- `sim_capability_hypothesis_isolated.py` is especially important because it tests whether Hypothesis can find a counterexample when an invariant is intentionally broken.
- `sim_integration_hypothesis_z3_property_guard.py` is the key coupling surface: property-based generation plus z3 constraint-admissibility.
- Several invariant sims show the broader pattern, but invariant language alone does not equal property-based testing.

Next wiki work:
- create a focused Hypothesis + z3 property-guard router;
- distinguish property-based tests, invariant checks, and fuzz-like generated cases;
- map which surfaces are capability probes vs load-bearing integration.

## Stop conditions
Do not claim:
- many tests prove the theory;
- fuzzing replaces formal proof;
- property-based testing replaces full tensor/correlation/chirality structure;
- metamorphic invariance under one transformation proves all transformations.

## Related pages
- [[hypothesis-z3-property-guard-router]]
- [[negative-sims-and-kill-tests-support]]
- [[mass-sim-generator-wide-exploration-support]]
- [[anti-teleology-future-option-selection]]
- [[systems-philosophy-attractor-basin-inversion]]
- [[smt-formal-falsifier-lane]]
- [[repo-tool-use-router]]
- [[generated-source-safety-for-external-model-review]]
