---
title: Hermes Context Stress Wiki Processing 2026-05-18
created: 2026-05-18
updated: 2026-05-18
type: query
tags: [hermes, mmm, context-window, wiki-processing, saliency]
sources:
  - /tmp/hermes_mmm_complete_read_manifest_20260518.json
  - /tmp/hermes_wiki_context_stress_scan_20260518.json
framing: current
---

# Hermes Context Stress Wiki Processing 2026-05-18

## Purpose
This page records the fast long-context stress tranche requested after the Hermes context/compression patch checks. It intentionally loads the active Hermes spine, reads the v4.2 MMM estate, and scans the wiki broadly so the live session exercises a large context window while also leaving a useful routing artifact.

## Checked / read surfaces
- `hermes-current/` spine: `read-first`, identity/preferences, active intentions, environment/rules, current-vs-legacy, skills/agent rules, active plans, ingest queue, and the May 18 wiki-work receipt.
- `wizard/packet-v4-2-current/mmm/`: 52 markdown files, 2,542,217 characters, 94,795 lines, manifest `/tmp/hermes_mmm_complete_read_manifest_20260518.json`.
- Broad wiki scan: published/current routing folders, excluding archives and `.obsidian`.

## MMM facts loaded
- `FULL_MMM_v4_2.md` is canonical runtime, 1,009,323 chars, 36,825 lines, sha256 `4098936c2ec2d3244bb421fb3733728d57c26a89aedf476ae0575716c19ef31f`.
- `COMPACT_MMM_v4_2.md` is canonical runtime, 126,550 chars, 4,698 lines, sha256 `ad6b3eaee5b90e3aab58e661c900b3a3b96e0d7bd27a3b414973496126bbac9b`.
- `mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md` is canonical runtime member registry, 31,511 chars, 692 lines, sha256 `af451de89f7d20499ffb8c610f02b8e7fbf4391002331a2249af21b23af4ae62`.
- `SALIENCY_TRANCHE_01_CANDIDATE.md` is packet-local but `reference-only`; it should be used as source-language overlay, not runtime promotion.

## Broad scan counts
- Markdown files scanned: 1441
- Pages with any MMM/source/result/tool/research signal: 1044
- `mmm_saliency` total hits: 4444
- `source_doc` total hits: 293
- `result_router` total hits: 1167
- `tool_proof` total hits: 1381
- `research_basin` total hits: 2059

## Highest-signal pages
- `queries/math-geometry-anti-teleology-source-alignment-audit-2026-05-18.md` — chars 27447; scores {'mmm_saliency': 3, 'source_doc': 45, 'result_router': 15, 'tool_proof': 64, 'research_basin': 68}; headings: Math / Geometry / Anti-Teleology Source Alignment Audit — 2026-05-18; Purpose; Source coverage audit
- `wizard/packet-v4-1-current/WIZARD_FULL_v4_1.md` — chars 231688; scores {'mmm_saliency': 68, 'source_doc': 3, 'result_router': 87, 'tool_proof': 0, 'research_basin': 0}; headings: Wizard Full v4.1; Boot Shortcut; Compiled Source
- `concepts/cross-field-research-intersection-map.md` — chars 16545; scores {'mmm_saliency': 21, 'source_doc': 0, 'result_router': 12, 'tool_proof': 17, 'research_basin': 101}; headings: Cross-Field Research Intersection Map; Purpose; Controller boundary
- `queries/read-only-source-doc-processing-ledger-2026-05-18.md` — chars 14779; scores {'mmm_saliency': 0, 'source_doc': 89, 'result_router': 19, 'tool_proof': 9, 'research_basin': 31}; headings: READ ONLY Source-Doc Processing Ledger — 2026-05-18; Purpose; Inventory basis
- `concepts/sim-math-geometry-result-surface-router.md` — chars 11750; scores {'mmm_saliency': 3, 'source_doc': 1, 'result_router': 24, 'tool_proof': 71, 'research_basin': 33}; headings: Sim Math / Geometry Result-Surface Router; Purpose; Evidence boundary
- `concepts/qit-basin-engine-synthesis.md` — chars 13804; scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 1, 'tool_proof': 0, 'research_basin': 112}; headings: QIT Basin Engine Synthesis; 1. Current Truth; 2. Basin Math
- `hermes-current/wiki-work-receipt-2026-05-18.md` — chars 7036; scores {'mmm_saliency': 19, 'source_doc': 6, 'result_router': 41, 'tool_proof': 5, 'research_basin': 38}; headings: Wiki Work Receipt — 2026-05-18; Correction; Prior Hermes terminals recovered
- `projects/codex-ratchet/_steward_questions.md` — chars 530603; scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 93, 'tool_proof': 0, 'research_basin': 6}; headings: Codex-Ratchet Steward Questions; Q1 — qutip + cirq capability FAILs (resolved); Q2 — orphan canonical results downgrade (resolved in part)
- `queries/systems-attractor-basin-research-queue-2026-05-18.md` — chars 28126; scores {'mmm_saliency': 8, 'source_doc': 0, 'result_router': 1, 'tool_proof': 3, 'research_basin': 81}; headings: Systems / Attractor-Basin Research Queue — 2026-05-18; Purpose; Core research claim to support
- `concepts/attractor-basins-formal-reference.md` — chars 8548; scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 0, 'tool_proof': 0, 'research_basin': 91}; headings: Attractor Basins Formal Reference; Overview; Formal Definitions
- `wizard/packet-v4-2-current/WIZARD_v4_2.md` — chars 29680; scores {'mmm_saliency': 76, 'source_doc': 3, 'result_router': 1, 'tool_proof': 0, 'research_basin': 0}; headings: Wizard v4.2 Operational Runtime; Purpose; Authority
- `queries/whole-wiki-mmm-source-research-campaign-2026-05-18.md` — chars 6241; scores {'mmm_saliency': 20, 'source_doc': 10, 'result_router': 20, 'tool_proof': 2, 'research_basin': 27}; headings: Whole-Wiki MMM Source Research Campaign 2026-05-18; Purpose; Source corpora in scope
- `concepts/anti-teleology-future-option-selection.md` — chars 6066; scores {'mmm_saliency': 4, 'source_doc': 0, 'result_router': 8, 'tool_proof': 7, 'research_basin': 58}; headings: Anti-Teleology and Future-Option Selection; Purpose; Plain statement
- `queries/deep-research-source-cluster-status-2026-05-18.md` — chars 5602; scores {'mmm_saliency': 6, 'source_doc': 21, 'result_router': 9, 'tool_proof': 2, 'research_basin': 38}; headings: Deep Research Source Cluster Status — 2026-05-18; Purpose; Boundary
- `concepts/basin-stability-and-viability-support.md` — chars 15230; scores {'mmm_saliency': 6, 'source_doc': 0, 'result_router': 1, 'tool_proof': 3, 'research_basin': 64}; headings: Basin Stability and Viability Support; Purpose; Basin stability
- `wizard/packet-v4-2-current/mmm/FULL_MMM_v4_2.md` — chars 1009323; scores {'mmm_saliency': 24, 'source_doc': 0, 'result_router': 5, 'tool_proof': 17, 'research_basin': 25}; headings: Wizard Full MMM v4.2; v4.2 saliency patch: output-language self-saliency; words
- `concepts/sim-run-catalogue-and-result-family-router.md` — chars 12870; scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 47, 'tool_proof': 6, 'research_basin': 18}; headings: Sim Run Catalogue and Result Family Router; Purpose; Evidence boundary
- `concepts/tooling-status.md` — chars 12620; scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 3, 'tool_proof': 67, 'research_basin': 0}; headings: Tooling Status; Current Truth; GREEN — Installed, imported, verified
- `concepts/mmm-language-sea-quotes-couplings-triples.md` — chars 22437; scores {'mmm_saliency': 27, 'source_doc': 4, 'result_router': 3, 'tool_proof': 7, 'research_basin': 26}; headings: MMM Language Sea, Quotes, Couplings, and Triples; Purpose; Quality target
- `concepts/repo-tool-use-router.md` — chars 8956; scores {'mmm_saliency': 5, 'source_doc': 0, 'result_router': 26, 'tool_proof': 36, 'research_basin': 0}; headings: Repo Tool-Use Router; Purpose; Evidence boundary
- `concepts/systems-philosophy-attractor-basin-inversion.md` — chars 6205; scores {'mmm_saliency': 9, 'source_doc': 0, 'result_router': 5, 'tool_proof': 7, 'research_basin': 46}; headings: Systems Philosophy and Attractor-Basin Inversion; Purpose; The inversion
- `wizard/packet-v4-1-current/mmm/FULL_MMM_v4_1.md` — chars 1008022; scores {'mmm_saliency': 19, 'source_doc': 0, 'result_router': 5, 'tool_proof': 17, 'research_basin': 25}; headings: Wizard Full MMM v4.1; words; couplings
- `wizard/packet-v4-1-current/mmm/main/full/md/MMM_MAIN_FULL_v4_1.md` — chars 1008020; scores {'mmm_saliency': 18, 'source_doc': 0, 'result_router': 5, 'tool_proof': 17, 'research_basin': 25}; headings: MMM_MAIN_FULL_v4_1; words; couplings
- `wizard/packet-v3-4-current/mmm/main/full/md/MMM_MAIN_FULL_v3_4.md` — chars 1008020; scores {'mmm_saliency': 18, 'source_doc': 0, 'result_router': 5, 'tool_proof': 17, 'research_basin': 25}; headings: MMM_MAIN_FULL_v3_4; words; couplings
- `concepts/attractor-basin-classifier-case-table.md` — chars 10207; scores {'mmm_saliency': 1, 'source_doc': 0, 'result_router': 7, 'tool_proof': 1, 'research_basin': 55}; headings: Attractor-Basin Classifier Case Table; Purpose; Evidence boundary
- `queries/whole-wiki-research-mmm-tool-gap-audit-2026-05-18.md` — chars 10043; scores {'mmm_saliency': 20, 'source_doc': 0, 'result_router': 5, 'tool_proof': 29, 'research_basin': 9}; headings: Whole-Wiki Research / MMM / Tool Gap Audit — 2026-05-18; Purpose; Evidence used
- `concepts/attractor-basin-row-level-evidence-ledger.md` — chars 4653; scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 10, 'tool_proof': 1, 'research_basin': 51}; headings: Attractor-Basin Row-Level Evidence Ledger; Purpose; Extracted receipts
- `wizard/packet-v3-3-current/mmm/main/full/md/MMM_MAIN_FULL_v3_3.md` — chars 1044076; scores {'mmm_saliency': 18, 'source_doc': 0, 'result_router': 5, 'tool_proof': 13, 'research_basin': 25}; headings: MMM_MAIN_FULL_v3_3; MMM_MAIN_FULL_v3_3; words
- `concepts/attractor-basin-result-surface-ledger.md` — chars 5265; scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 20, 'tool_proof': 1, 'research_basin': 37}; headings: Attractor-Basin Result-Surface Ledger; Purpose; Evidence boundary
- `wizard/packet-v2-8-expanded-current/main_mmm/full/md/MMM_MAIN_FULL_v2_8.md` — chars 1041322; scores {'mmm_saliency': 12, 'source_doc': 0, 'result_router': 5, 'tool_proof': 11, 'research_basin': 25}; headings: MMM_MAIN_FULL_v2_8; words; couplings

## Candidate next routing pages missing explicit MMM hook
- `queries/read-only-source-doc-processing-ledger-2026-05-18.md` — scores {'mmm_saliency': 0, 'source_doc': 89, 'result_router': 19, 'tool_proof': 9, 'research_basin': 31}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/qit-basin-engine-synthesis.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 1, 'tool_proof': 0, 'research_basin': 112}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `projects/codex-ratchet/_steward_questions.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 93, 'tool_proof': 0, 'research_basin': 6}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/attractor-basins-formal-reference.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 0, 'tool_proof': 0, 'research_basin': 91}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/sim-run-catalogue-and-result-family-router.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 47, 'tool_proof': 6, 'research_basin': 18}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/tooling-status.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 3, 'tool_proof': 67, 'research_basin': 0}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/attractor-basin-row-level-evidence-ledger.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 10, 'tool_proof': 1, 'research_basin': 51}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/attractor-basin-result-surface-ledger.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 20, 'tool_proof': 1, 'research_basin': 37}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/viability-theory-reference.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 0, 'tool_proof': 0, 'research_basin': 42}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `queries/wiki-driven-arxiv-search-queue.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 3, 'tool_proof': 1, 'research_basin': 35}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/qit-geometry-thermodynamics-harness-synthesis.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 3, 'tool_proof': 0, 'research_basin': 34}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/probe-doc-result-map.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 2, 'tool_proof': 8, 'research_basin': 26}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/enforcement-and-process-rules.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 5, 'tool_proof': 30, 'research_basin': 0}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/perturbation-depth-basin-edge-table.md` — scores {'mmm_saliency': 0, 'source_doc': 1, 'result_router': 7, 'tool_proof': 0, 'research_basin': 25}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/shell-local-to-coupled-program.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 1, 'tool_proof': 29, 'research_basin': 0}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/qit-vocabulary-discipline-reference.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 0, 'tool_proof': 0, 'research_basin': 24}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/qit-engine-proto-ratchet-and-sim-plan.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 1, 'tool_proof': 0, 'research_basin': 22}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/universal-q-product-form.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 0, 'tool_proof': 22, 'research_basin': 0}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/cvc5-smt-and-sygus-reference.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 0, 'tool_proof': 22, 'research_basin': 0}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/lego-build-catalog.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 11, 'tool_proof': 10, 'research_basin': 0}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/max-stack-probe-variants-status-router.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 10, 'tool_proof': 11, 'research_basin': 0}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/current-formal-methods-core.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 3, 'tool_proof': 17, 'research_basin': 0}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/sim-estate-integration-index-router.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 11, 'tool_proof': 6, 'research_basin': 3}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/tradition-system-mapping-detailed.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 0, 'tool_proof': 0, 'research_basin': 20}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.
- `concepts/tool-function-receipt-matrix-router.md` — scores {'mmm_saliency': 0, 'source_doc': 0, 'result_router': 3, 'tool_proof': 16, 'research_basin': 0}; add either `MMM routing`, `source-language overlay`, or `claim-tier fence` if this page is meant to feed future packet salience.

## Claim boundary
- This is a routing/stress tranche, not proof that every page was semantically audited line-by-line.
- The MMM estate was fully read from disk into the manifest; large generated word/coupling/triplet reservoirs were not manually reprinted in this page.
- Packet mutation is not automatic: candidate salience remains reference-only until conformance/admission promotes it.

## Next bounded tranche
Promote one reviewed slice from `SALIENCY_TRANCHE_01_CANDIDATE.md` into either a compact injection surface or a redesigned functional mini-MMM slice, then run the A/B/C/D saliency behavior test again.
