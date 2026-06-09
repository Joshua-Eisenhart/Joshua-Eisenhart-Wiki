---
type: query
created: 2026-05-18
updated: 2026-05-18
tags: [source-processing, legacy, reference-docs, ingest, audit]
sources:
  - /tmp/wiki_legacy_reference_mathgeom_inventory_20260518.json
---

# READ ONLY Source-Doc Processing Ledger — 2026-05-18

## Purpose
This ledger tracks whether the READ ONLY legacy/reference source docs have been processed into the wiki.

It is intentionally conservative:
- “coverage hit” is a routing clue, not proof of processing;
- “low coverage” means no obvious wiki hit under the rough scan, not definitely unprocessed;
- high-entropy generated docs require owner-kernel vs generated-elaboration separation before promotion.

## Inventory basis
Source inventory artifact:
- `/tmp/wiki_legacy_reference_mathgeom_inventory_20260518.json`

Observed source files: 361

Rough low-coverage files: 130

## Cluster ledger

| Cluster | Source count | Rough low-coverage count | Current wiki status | Next action |
|---|---:|---:|---|---|
| `deep_research_results` | 15 | 13 | partly processed for attractor/Holodeck: [[attractor-holodeck-future-option-source-router]] | verify by file cluster; create router before per-file pages |
| `legacy_core_root` | 230 | 74 | mixed or unknown | verify by file cluster; create router before per-file pages |
| `qit_graph_rosetta_cluster` | 8 | 6 | partly processed: [[qit-graph-geometry-promotion-router]], [[empirical-math-rosetta]] | verify by file cluster; create router before per-file pages |
| `system_v5_reference_docs` | 76 | 20 | mixed; likely many current/reference docs still need role classification | verify by file cluster; create router before per-file pages |
| `ultra_high_entropy_docs` | 29 | 16 | mostly unprocessed / high-risk; needs sanitized owner-kernel extraction | verify by file cluster; create router before per-file pages |
| `v4_upgrades` | 3 | 1 | mixed or unknown | verify by file cluster; create router before per-file pages |

## High-priority unprocessed or weakly processed files
These are not all “missing.” They are the first candidates for bounded verification.

- `READ ONLY Legacy core_docs/QIT_GRAPH_SCHEMA.md` — keywords: hopf, weyl, spinor, clifford, chirality, qit, operator, sim, proof
- `READ ONLY Legacy core_docs/00_MANIFEST__CORE_DOCS_ORDER_v1.md` — keywords: attractor, basin, constraint, entropy, sim
- `READ ONLY Legacy core_docs/QIT_COMPRESSION_FUTURE_REFERENCES.md` — keywords: future, hopf, weyl, spinor, clifford, chirality, qit, topology
- `READ ONLY Legacy core_docs/QIT_GRAPH_LAYER_MAPPING.md` — keywords: future, hopf, weyl, clifford, chirality, qit, operator, entropy, manifold, topology
- `READ ONLY Legacy core_docs/QIT_GRAPH_PROMOTION_GATES.md` — keywords: clifford, chirality, qit, operator, entropy, topology, sim, proof
- `READ ONLY Legacy core_docs/HOLODECK_SCIENCE_SYSTEM_v1.md` — keywords: attractor, hopf, qit, entropy, sim
- `READ ONLY Legacy core_docs/QIT_GRAPH_SYNC_README.md` — keywords: future, hopf, weyl, spinor, clifford, chirality, qit, operator, sim, proof
- `READ ONLY Legacy core_docs/EMPIRICAL_MATH_ROSETTA.md` — keywords: geometry, operator, constraint, distinguishability, entropy, flux, topology, sim
- `READ ONLY Legacy core_docs/ultra high entropy docs/STRICT_MINING_BATCH01_600.docx` — keywords: 
- `READ ONLY Legacy core_docs/ultra high entropy docs/gemini leviathan convo.pdf` — keywords: 
- `READ ONLY Legacy core_docs/ultra high entropy docs/STRICT_MINING_COMPILED_10BATCHES_6000_v1.docx` — keywords: 
- `READ ONLY Legacy core_docs/ultra high entropy docs/gemini toe summary volume 1-23.pdf` — keywords: 
- `READ ONLY Legacy core_docs/ultra high entropy docs/grok rosetta stone.pdf` — keywords: 
- `READ ONLY Legacy core_docs/ultra high entropy docs/STRICT_MINING_LEDGER_INDEX_v1.md` — keywords: qit, manifold
- `READ ONLY Legacy core_docs/ultra high entropy docs/grok gemini save. .pages` — keywords: 
- `READ ONLY Legacy core_docs/ultra high entropy docs/eisenhart_rosetta_master_doc_vNext.md` — keywords: geometry, hopf, weyl, spinor, chirality, operator, constraint, distinguishability, entropy, flux
- `READ ONLY Legacy core_docs/ultra high entropy docs/GPT 12_29 pro plan vs browser crashes.md` — keywords: qit, operator, constraint, distinguishability, entropy, sim
- `READ ONLY Legacy core_docs/v4 upgrades/jp lev web outputs.txt` — keywords: geometry, hopf, constraint, distinguishability, topology, sim
- `READ ONLY Legacy core_docs/deep_research_results/DR_leviathan_holodeck_bridge_v2.md` — keywords: attractor, basin, hopf, qit, operator, constraint, entropy, topology, sim
- `READ ONLY Legacy core_docs/deep_research_results/DR_parallel_sim_evaluations.md` — keywords: future, weyl, spinor, qit, operator, constraint, topology, sim, proof
- `READ ONLY Legacy core_docs/deep_research_results/DR_mass_sim_generator.md` — keywords: future, constraint, entropy, sim, proof
- `READ ONLY Legacy core_docs/deep_research_results/DR_attractor_basin_dashboard.md` — keywords: future, attractor, basin, geometry, hopf, qit, operator, constraint, entropy, flux
- `READ ONLY Legacy core_docs/deep_research_results/DR_dark_sector_entropic.md` — keywords: qit, operator, constraint, entropy, sim
- `READ ONLY Legacy core_docs/deep_research_results/DR_riemann_hypothesis_gue.md` — keywords: operator, constraint, sim
- `READ ONLY Legacy core_docs/deep_research_results/DR_pytest_qit_invariants.md` — keywords: future, qit, operator, entropy, sim
- `READ ONLY Legacy core_docs/deep_research_results/DR_entropic_monism_hopf.md` — keywords: attractor, basin, geometry, hopf, spinor, clifford, chirality, operator, constraint, entropy
- `READ ONLY Legacy core_docs/deep_research_results/DR_dark_matter_energy_qit.md` — keywords: qit, operator, constraint, distinguishability, entropy, sim
- `READ ONLY Legacy core_docs/deep_research_results/DR_problem_spec_design.md` — keywords: operator, constraint, sim
- `READ ONLY Legacy core_docs/deep_research_results/DR_leviathan_holodeck_bridge_v1.md` — keywords: geometry, qit, operator, constraint, entropy, manifold, sim
- `READ ONLY Legacy core_docs/deep_research_results/DR_negative_sims_kill_tests.md` — keywords: geometry, operator, constraint, entropy, sim
- `READ ONLY Legacy core_docs/deep_research_results/DR_godel_turing_self_reference.md` — keywords: operator, constraint, entropy, sim, proof
- `READ ONLY Legacy core_docs/upgrade docs/SYSTEM_UPGRADE_PLAN_EXTRACT_PASS8.md` — keywords: constraint
- `READ ONLY Legacy core_docs/upgrade docs/SYSTEM_UPGRADE_PLAN_EXTRACT_PASS7.md` — keywords: constraint, sim
- `READ ONLY Legacy core_docs/upgrade docs/DIRECTED_EXTRACTION_ANSWERS.md` — keywords: constraint, sim
- `READ ONLY Legacy core_docs/upgrade docs/DIRECTED_EXTRACTION_ANSWERS_v2.md` — keywords: attractor, basin, constraint, sim
- `READ ONLY Legacy core_docs/upgrade docs/DIRECTED_EXTRACTION_AUDIT_AND_QUESTIONS.md` — keywords: constraint, sim
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/NLM_PROMPT_BATCH_1.md` — keywords: hopf, chirality, qit, operator, entropy, manifold, topology, sim, proof
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/AXIS3_HYPOTHESES.md` — keywords: geometry, hopf, weyl, spinor, chirality, constraint, flux, manifold, sim
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/DEEP_RESEARCH_PROMPT_BANK.md` — keywords: future, attractor, basin, geometry, hopf, clifford, qit, operator, entropy, sim
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/NLM_AXIS_0_AND_4_PREP.md` — keywords: chirality, qit, constraint, entropy, sim
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/SIM_CATALOG_AXIS_DISCOVERY.md` — keywords: geometry, hopf, qit, operator, constraint, manifold, sim
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/TERRAIN_MATH_LEDGER_v1.md` — keywords: geometry, hopf, weyl, chirality, qit, operator, constraint, distinguishability, manifold, topology
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/MATH_NOMINALISM_SYNTHESIS.md` — keywords: geometry, qit, operator, constraint, entropy, manifold, sim
- `READ ONLY Legacy core_docs/a2_runtime_state archived old state/A2_LOW_ENTROPY_LIBRARY_v4.md` — keywords: future, operator, constraint, distinguishability, entropy, topology
- `READ ONLY Legacy core_docs/a2_runtime_state archived old state/README_A2_EXPORT_PACK_SMALL.md` — keywords: 
- `READ ONLY Legacy core_docs/a2_runtime_state archived old state/A2_SYSTEM_SPEC_v1.md` — keywords: constraint
- `READ ONLY Legacy core_docs/a2_runtime_state archived old state/A2_EPISODE_01_WORKING_LOG.md` — keywords: future, geometry, constraint, distinguishability, entropy, manifold, topology, sim
- `READ ONLY Legacy core_docs/a2_runtime_state archived old state/A2_WORKING_UPGRADE_CONTEXT_v1.md` — keywords: future, geometry, qit, operator, constraint, distinguishability, entropy, manifold, topology, sim
- `READ ONLY Legacy core_docs/a2_runtime_state archived old state/A2_JP_BEHAVIORAL_BOOT.md` — keywords: sim
- `READ ONLY Legacy core_docs/a2_runtime_state archived old state/FULL_READ_LOG_PASS_4.md` — keywords: geometry, hopf, qit, constraint, entropy, manifold, topology, z3
- `READ ONLY Legacy core_docs/a2_runtime_state archived old state/A2_INTENT_MANIFEST_v1.md` — keywords: constraint, sim, proof
- `READ ONLY Legacy core_docs/a2_runtime_state archived old state/STRUCTURAL_MEMORY_MAP_v2.md` — keywords: operator, constraint, entropy, topology, sim
- `READ ONLY Legacy core_docs/a2_feed_high entropy doc/grok eisenhart model .txt` — keywords: future, attractor, geometry, hopf, spinor, chirality, operator, entropy, manifold, topology
- `READ ONLY Legacy core_docs/a2_feed_high entropy doc/grok toe redo save.txt` — keywords: future, attractor, geometry, entropy, sim
- `READ ONLY Legacy core_docs/a2_feed_high entropy doc/gpt thread a1 trigram work out .txt` — keywords: 
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/THREAD_S_FULL_SAVE/THREAD_S_SAVE_SNAPSHOT_v2.txt` — keywords: 
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/THREAD_S_FULL_SAVE/SHA256SUMS.txt` — keywords: 
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/GEOMETRY_ADMISSIBILITY_v1.md` — keywords: geometry
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Engine contract v1.md` — keywords: 
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/RELATIONAL_TRANSPORT_ADMISSIBILITY_v1.md` — keywords: distinguishability
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/METRIC_ADMISSIBILITY_v1.md` — keywords: geometry, distinguishability
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/DUALITY_CLASS_ADMISSIBILITY_v1.md` — keywords: distinguishability
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/CANDIDATE_PROPOSAL_v1.md` — keywords: future, constraint
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Path contract v1.md` — keywords: geometry, topology
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/REFINEMENT_CONTRACT_v1.1.md` — keywords: operator
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Cognition rosetta v1.md` — keywords: z3
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/AXIS_FUNCTION_ADMISSIBILITY_v1.md` — keywords: distinguishability
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/archive_manifest_v_1.md` — keywords: geometry, hopf, qit, constraint, entropy, manifold, topology, sim
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Entropy contract v1.md` — keywords: geometry, constraint, entropy, topology
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/COORDINATE_ADMISSIBILITY_v1.md` — keywords: geometry, constraint, distinguishability
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Physics Rosetta v1.md` — keywords: operator, entropy, manifold, topology, sim
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Topology contract v1.md` — keywords: geometry, operator, topology
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/CONSTRAINT_MANIFOLD_DERIVATION_v1.md` — keywords: geometry, constraint, manifold
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Curvature contract v1.md` — keywords: geometry
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/DYNAMICAL_ADMISSIBILITY_BOUNDARY_v1.md` — keywords: future
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Constraints. Entropy.md` — keywords: teleology, future, geometry, operator, constraint, distinguishability, entropy, category, topology, sim
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/STATE_ABSTRACTION_ADMISSIBILITY_v1.md` — keywords: teleology, future, geometry, constraint, distinguishability, manifold
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/DIMENSIONALITY_ADMISSIBILITY_v1.md` — keywords: geometry
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Transport contract v1.md` — keywords: operator, entropy
- `READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/AXIS_SET_ADMISSIBILITY_v1.md` — keywords: 

## Already routed during this campaign
- QIT graph / promotion gates → [[qit-graph-geometry-promotion-router]]
- Empirical math Rosetta → [[empirical-math-rosetta]]
- Attractor / Holodeck / future-option cluster → [[attractor-holodeck-future-option-source-router]]
- Systems / anti-teleology research queues → [[systems-attractor-basin-research-queue-2026-05-18]], [[math-geometry-anti-teleology-source-alignment-audit-2026-05-18]]

## Next processing order
1. Deep research result cluster: verify which `DR_*` docs remain unprocessed and create cluster routers, not one-off stubs.
2. Ultra high entropy docs: sanitize first; extract owner kernels only.
3. system_v5 READ ONLY Reference Docs: compare to current system_v5 docs and concepts; route as reference/provenance/support, not current authority by default.
4. v4 upgrade docs: process only if they still carry unique kernels not already in current pages.

## Safety rules
- Do not rewrite READ ONLY source files.
- Do not send unsanitized generated docs to external model lanes.
- Do not treat generated elaboration as owner doctrine.
- Do not promote legacy/reference content above repo-current status surfaces.
- Prefer cluster routers before creating many public pages.

## Related pages
- [[deep-research-source-cluster-status-2026-05-18]]
- [[math-geometry-anti-teleology-source-alignment-audit-2026-05-18]]
- [[qit-graph-geometry-promotion-router]]
- [[attractor-holodeck-future-option-source-router]]
- [[generated-source-safety-for-external-model-review]]
- [[wiki-ingest-queue-and-priorities]]
