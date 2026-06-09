---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [attractors, basins, results, evidence, formal-scouts, routing]
sources:
  - /tmp/attractor_basin_result_surface_ledger_inspect_20260518.json
---

# Attractor-Basin Result-Surface Ledger

## Purpose
This page is the first ledger for attractor/basin result surfaces.

It exists to prevent a common overclaim:

A result file mentioning attractor, basin, perturbation, Hopf, FEP, or topology does not by itself prove basin teleology or Holodeck engine truth.

Each surface needs a status, evidence role, claim ceiling, and next verification path.

## Evidence boundary
Inspection artifact:
- `/tmp/attractor_basin_result_surface_ledger_inspect_20260518.json`

This pass inspected JSON structure and key fields. It did not rerun sims and did not upgrade statuses.

## Ledger

| Surface | Current class | Evidence role | Claim ceiling | Next verification |
|---|---|---|---|---|
| `system_v5/ops/formal_scouts/results/attractor_basin_success_criteria_receipt_classifier_probe_results.json` | formal_scout | classifier / success-criteria receipt for basin candidate claims | formal scout only; no Axis0/FEP/Holodeck physics promotion | read claim_ceiling/blockers; map criteria to anti-teleology page; rerun only under repo status gate |
| `system_v5/ops/formal_scouts/results/stage_record_true_perturbation_depth_probe_results.json` | formal_scout | perturbation-depth receipt for local stage-record repair depth | formal scout only; not global manifold or deep-basin proof | map perturbation rows to basin-edge concepts; check next_work blockers |
| `system_v5/ops/formal_scouts/results/axis0_plural_candidate_multicarrier_drive_controls_probe_results.json` | formal_scout | plural candidate / multicarrier drive-control scout | candidate pressure; not Axis0 promotion | preserve plural candidates; avoid single-winner collapse |
| `system_v5/ops/formal_scouts/results/source_native_hopf_fep_igt_chirality_prediction_probe_results.json` | formal_scout | Hopf/FEP/IGT/chirality prediction scout | finite source-native predictor; not canon or final FEP | separate Grok reference hypothesis from formal translation and stage rows |
| `system_v5/evidence/qit_engine_evidence_index.json` | index | evidence index / blocked candidate tracker | index status only; blocked rows remain blocked | use as router into specific result paths; do not promote index presence |
| `system_v5/evidence/formal_scout_readiness_index.json` | index | readiness index for formal scout estate | readiness health only; not individual result proof | fix readiness defects before broad scout promotion |
| `system_v5/evidence/tool_function_receipt_matrix.json` | index | tool/function receipt matrix | matrix summary only; row-level receipt decides | extract row-level carrier/tool function targets |


## Cross-surface reading

### What looks strong
- Several surfaces explicitly carry `claim_ceiling`, `classification`, `promotion_allowed`, `TOOL_MANIFEST`, and `TOOL_INTEGRATION_DEPTH` fields.
- That is good: the result estate is already trying to prevent overpromotion.
- Formal-scout classification is visible in the fields rather than hidden in prose.

### What remains risky
- The terms “attractor”, “basin”, “Hopf”, “FEP”, “engine”, and “chirality” are high-salience and easy for LLMs to overread.
- The presence of `all_pass` or positive rows can still coexist with a narrow `claim_ceiling`.
- Index files are especially dangerous: they point to result surfaces but are not themselves proof of those surfaces.

## Router rules
1. Read `claim_ceiling` before reading `positive` or `all_pass`.
2. Read `promotion_allowed` before writing any promoted status language.
3. Keep `formal_scout` separate from canonical sim/result status.
4. Treat Grok/Gemini/Claude provider text as reference/pressure only unless the repo result says otherwise.
5. Preserve plural candidate rows as plural; do not compress into one attractor story.
6. Map KILL/blocker/graveyard companions into the basin boundary.

## How this supports anti-teleology
These result surfaces help anti-teleology only when they preserve the field of possible continuations:

- blockers show future paths that are not yet admissible;
- perturbation rows show basin-edge sensitivity;
- plural candidates show non-privileged futures;
- formal scouts provide pressure without final authority;
- tool matrices show which functions can witness which carrier features.

## Next work
1. Extract row-level details from `attractor_basin_success_criteria_receipt_classifier_probe_results.json` — first row-level ledger created at [[attractor-basin-row-level-evidence-ledger]].
2. Extract perturbation rows from `stage_record_true_perturbation_depth_probe_results.json`.
3. Create a small concept page for `claim ceiling` if no current page already carries the idea cleanly.
4. Patch the anti-teleology page with one example from these ledgers after row-level extraction.

## Related pages
- [[sim-math-geometry-result-surface-router]]
- [[anti-teleology-future-option-selection]]
- [[systems-philosophy-attractor-basin-inversion]]
- [[attractor-holodeck-future-option-source-router]]
- [[repo-tool-use-router]]
- [[smt-formal-falsifier-lane]]
- [[topology-carrier-tool-lane]]
