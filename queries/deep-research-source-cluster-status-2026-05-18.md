---
type: query
created: 2026-05-18
updated: 2026-05-18
tags: [source-processing, deep-research, legacy, routing, audit]
sources:
  - /tmp/deep_research_source_cluster_status_20260518.json
  - /tmp/wiki_legacy_reference_mathgeom_inventory_20260518.json
---

# Deep Research Source Cluster Status — 2026-05-18

## Purpose
This page is the first cluster-level status table for `READ ONLY Legacy core_docs/deep_research_results/`.

It prevents two bad outcomes:
- treating all DR files as already processed because some cluster pages now exist;
- creating one public stub per file without first deciding each file's role.

## Boundary
This is a routing/status table, not source ingestion. Each file still needs bounded reading before any strong claim is extracted.

## Status table

| Source file | Keywords | Current route | Target / next wiki surface | Coverage signal |
|---|---|---|---|---|
| `READ ONLY Legacy core_docs/deep_research_results/DR_p_vs_np_qit.md` | attractor, basin, qit, operator, constraint, entropy, topology, sim | needs bounded review | (tbd) | wizard/packet-v4-2-current/mmm/mini/full/voices/md/MMM_VOICE_ZHUANGZI_FULL_v4_1.md; wizard/packet-v4-2-current/mmm/mini/full/voices/md/MMM_VOICE_SYSTEMS_FULL_v4_1.md; wizard/packet-v4-2-current/mmm/mini/full/voices/md/MMM_VOICE_STRATEGY_FULL_v4_1.md |
| `READ ONLY Legacy core_docs/deep_research_results/DR_leviathan_holodeck_bridge_v2.md` | attractor, basin, hopf, qit, operator, constraint, entropy, topology | attractor/Holodeck routed or adjacent | [[attractor-holodeck-future-option-source-router]] | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_parallel_sim_evaluations.md` | future, weyl, spinor, qit, operator, constraint, topology, sim | wide-exploration/sim process support | [[systems-philosophy-attractor-basin-inversion]] | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_mass_sim_generator.md` | future, constraint, entropy, sim, proof | wide-exploration/sim process support | [[systems-philosophy-attractor-basin-inversion]] | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_attractor_basin_dashboard.md` | future, attractor, basin, geometry, hopf, qit, operator, constraint | attractor/Holodeck routed or adjacent | [[attractor-holodeck-future-option-source-router]] | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_dark_sector_entropic.md` | qit, operator, constraint, entropy, sim | needs bounded review | (tbd) | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_riemann_hypothesis_gue.md` | operator, constraint, sim | needs bounded review | (tbd) | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_pytest_qit_invariants.md` | future, qit, operator, entropy, sim | needs bounded review | (tbd) | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_entropic_monism_hopf.md` | attractor, basin, geometry, hopf, spinor, clifford, chirality, operator | attractor/Holodeck routed or adjacent | [[attractor-holodeck-future-option-source-router]] | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_dark_matter_energy_qit.md` | qit, operator, constraint, distinguishability, entropy, sim | needs bounded review | (tbd) | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_problem_spec_design.md` | operator, constraint, sim | needs bounded review | (tbd) | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_security_audit.md` | future, attractor, basin, weyl, spinor, qit, operator, entropy | needs bounded review | (tbd) | wizard/packet-v4-2-current/mmm/mini/full/compositions/md/MMM_COMPOSITION_ALL_C_FULL_v4_1.md; wizard/packet-v4-2-current/mmm/FULL_MMM_v4_2.md; wizard/packet-v4-1-current/mmm/mini/full/compositions/md/MMM_COMPOSITION_ALL_C_FULL_v4_1.md |
| `READ ONLY Legacy core_docs/deep_research_results/DR_leviathan_holodeck_bridge_v1.md` | geometry, qit, operator, constraint, entropy, manifold, sim | attractor/Holodeck routed or adjacent | [[attractor-holodeck-future-option-source-router]] | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_negative_sims_kill_tests.md` | geometry, operator, constraint, entropy, sim | negative-sim/falsifier support | [[smt-formal-falsifier-lane]] / [[attractor-basin-row-level-evidence-ledger]] | none |
| `READ ONLY Legacy core_docs/deep_research_results/DR_godel_turing_self_reference.md` | operator, constraint, entropy, sim, proof | needs bounded review | (tbd) | none |


## Immediate processing order
1. Negative sims / kill tests: strongest process support; clean support page created at [[negative-sims-and-kill-tests-support]].
2. Parallel/mass sim generator: supports wide exploration under strong constraints; support page created at [[mass-sim-generator-wide-exploration-support]].
3. Remaining attractor/Holodeck adjacent docs: process only where they add owner-kernel material not already in [[attractor-holodeck-future-option-source-router]].
4. Other DR files: classify as support/proposal/reference/defer before public page creation.

## Stop conditions
- Do not treat generated DR reports as owner doctrine.
- Do not promote source-document proposals into current repo truth.
- Do not create many shallow public pages; prefer cluster routers and support pages.
- Preserve generated vs owner-kernel distinction.

## Related pages
- [[read-only-source-doc-processing-ledger-2026-05-18]]
- [[math-geometry-anti-teleology-source-alignment-audit-2026-05-18]]
- [[attractor-holodeck-future-option-source-router]]
- [[generated-source-safety-for-external-model-review]]
- [[systems-philosophy-attractor-basin-inversion]]
