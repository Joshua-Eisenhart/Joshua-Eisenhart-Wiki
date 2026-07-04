---
title: Research Source Coverage Index
created: 2026-04-10
updated: 2026-04-12
type: summary
tags: [reference, research, intake, coverage]
sources:
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/notebooklm_reference_pack_status.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/first_batch_manifest.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/second_batch_manifest.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/third_batch_manifest.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/fourth_batch_manifest.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/fifth_batch_manifest.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/sixth_batch_manifest.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/seventh_batch_manifest.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/eighth_batch_manifest.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/citation_stub_queue.json
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/webui_deepresearch_candidate_sources_2026_04_10.json
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Research Source Coverage Index

## Overview
This page shows which research domains have real downloaded source packets under `raw/papers`, which are still citation-only, and which owner pages they should feed. It is a coverage and routing surface, not a theory page.

## Current totals
- Downloaded and text-extracted source packets in `raw/papers/open_access`: 26 unique PDF/text pairs
- Downloaded ledger/domain rows in `notebooklm_reference_pack_status.json`: 29, including 3 cross-domain duplicate assignments
- Citation-only / unsourced references still waiting on sourcing: 125
- Materialized priority citation stub queue entries: 6
- Candidate citation additions from audited WebUI returns: 16
- Raw PDF folder: `/Users/joshuaeisenhart/wiki/raw/papers/open_access/pdfs`
- Raw text folder: `/Users/joshuaeisenhart/wiki/raw/papers/open_access/text`
- Raw manifest folder: `/Users/joshuaeisenhart/wiki/raw/papers/open_access/meta`

## Domain coverage
Downloaded counts in the domain table are ledger/domain-routing rows, not unique files on disk.
| Domain | Downloaded | Citation-only | Primary owner pages |
|---|---:|---:|---|
| attractors_viability | 3 | 12 | [[attractor-basins-formal-reference]], [[viability-theory-reference]] |
| autopoiesis_fep | 1 | 13 | [[autopoiesis-and-enactivism-reference]], [[fep-and-active-inference-reference]] |
| chinese_philosophy | 0 | 10 | [[chinese-philosophy-reference]], [[nominalism-philosophical-foundation]], [[qit-vocabulary-discipline-reference]] |
| concurrency_trace_formal_methods | 1 | 3 | [[concurrency-and-trace-theory-reference]], [[formal-methods-and-witness-discipline-reference]] |
| distinguishability_resource_theory | 4 | 12 | [[distinguishability-formal-reference]], [[constraint-on-distinguishability-formal-reference]], [[resource-theories-quantum-reference]] |
| evolutionary_darwinism | 2 | 18 | [[evolutionary-epistemology-reference]], [[current-research-overlays]] |
| fiber_topology_spin_geometry | 2 | 13 | [[fiber-bundles-and-spin-geometry-reference]], [[formal-constraints-and-geometry]] |
| information_geometry | 2 | 5 | [[information-geometry-reference]], [[distance-metrics-state-space]] |
| llm_failure_modes | 5 | 3 | [[llm-bias-and-failure-modes-reference]], [[llm-ontology-smuggling-reference]], [[llm-bias-inversion-rules]] |
| process_relational_topos | 4 | 9 | [[process-philosophy-and-relational-physics]], [[topos-quantum-mechanics-reference]], [[current-research-overlays]] |
| quantum_shannon_compression | 2 | 19 | [[quantum-shannon-theory-reference]], [[quantum-information-measures]] |
| stochastic_thermodynamics | 3 | 8 | [[stochastic-thermodynamics-reference]], [[qit-engine-proto-ratchet-and-sim-plan]] |

## Audited WebUI return queue
- Three GitHub WebUI return branches were audited as `pass with cautions`: useful for source-finding and wording fences, but not canon.
- Their candidate additions are queued in `raw/papers/open_access/meta/webui_deepresearch_candidate_sources_2026_04_10.json`.
- The strongest queued upgrades hit distinguishability, stochastic thermodynamics, viability / attractor language, LLM failure modes, and Chinese-philosophy support.

## Highest-yield next sourcing lanes
- LLM failure modes: already partially populated; good candidate for direct owner-page expansion next.
- Chinese philosophy: currently citation-only; this lane needs a source packet or carefully bounded citation use.
- Evolutionary / Darwinian support: now seeded, but still broad enough that a second bounded pass could tighten the constructor/replicator split.
- Concurrency / trace formal methods: now seeded with one bridge paper but still thin if the controller/tooling lane needs tighter formal-methods support.
- Stochastic thermodynamics: now less thin than before, but still benefits from broader fluctuation/unraveling coverage beyond the currently downloaded bridge papers.
- Attractors / viability: no longer zero-download, but still worth extending if the basin/viability split needs more than the current three papers.

## Admission rules
- Downloaded does not mean earned lower-loop truth.
- Citation-only entries are routing markers, not processed evidence.
- Every owner page should eventually point either to a downloaded source packet or to an explicit citation-only queue.
- Use [[notebooklm-reference-pack-intake]] for the broad bibliography view and this page for coverage / gaps.

## Related pages
- [[notebooklm-reference-pack-intake]]
- [[current-research-overlays]]
- [[qit-vocabulary-discipline-reference]]
- [[wiki-driven-arxiv-search-queue]]
