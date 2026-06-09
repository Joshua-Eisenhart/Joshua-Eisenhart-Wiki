---
title: Codex Ratchet Concepts Migration Index
created: 2026-05-21
updated: 2026-05-21
type: migration-index
framing: current
tags: [specs, codex-ratchet, migration, wiki-hygiene]
sources:
  - /Users/joshuaeisenhart/wiki/concepts
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/FORMAL_SCOUT_READINESS_INDEX.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/SIM_ESTATE_INTEGRATION_INDEX.md
---

# Codex Ratchet Concepts Migration Index

This is a control map, not a move log. No page is moved merely because it appears here.

The purpose is to stop mixing concept-wiki work with repo/spec mirror work. `/concepts` should remain a source and salience reservoir. Repo status, contract mirrors, and validator snapshots should consolidate under `/specs/codex-ratchet/` or be clearly labeled as historical.

## Move Or Mirror To Specs First

These pages carry repo status, live counts, validator truth, tool-role eligibility, or contract mirrors. They should be mirrored or moved under `/specs/codex-ratchet/` before being treated as current status surfaces.

| page | reason | first repair |
|---|---|---|
| [[formal-scout-readiness-index-router]] | live formal-scout counts and provider/readiness status | mirrored to [[specs/codex-ratchet/formal-scout-readiness-status|formal-scout-readiness-status]]; concept page marked historical snapshot |
| [[sim-estate-integration-index-router]] | live sim estate, Grok/formal split, tool-role gate | mirrored to [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]]; concept page marked historical snapshot |
| [[repo-tool-use-router]] | tool-use counts plus `/tmp` scan provenance | routed to [[specs/codex-ratchet/tool-function-receipt-status|tool-function-receipt-status]] and sim-estate status; `/tmp` scan marked ephemeral |
| [[sim-run-catalogue-and-result-family-router]] | result-estate counts and family routing | marked historical catalogue snapshot; live counts routed to formal-scout, sim-estate, and tool-function spec mirrors |
| [[tool-function-receipt-matrix-router]] | dated `2026-05-17` function/API receipt matrix snapshot | mirror exists at [[specs/codex-ratchet/tool-function-receipt-status|tool-function-receipt-status]]; remaining page can become pointer/historical router |
| [[tool-capability-and-integration-ledger]] | tool coupling eligibility language | marked derived historical ledger; routed to tool-function and sim-estate specs |
| [[tool-lego-integration-matrix]] | derived matrix that can read as admission | marked derived historical matrix; routed to tool-function, sim-estate, and lego-contract specs |
| [[tooling-status]] | installed/missing tool status | marked historical tooling snapshot; routed to current specs |
| [[current-tool-status-installed-vs-missing-vs-not-wired]] | old tool-status note with current title | marked legacy; routed to current specs |
| [[current-tool-status-operational-classification]] | old tool-status note with current title | marked legacy; routed to current specs |
| [[current-proper-install-and-location-rule-note]] | legacy interpreter/location advice | marked legacy; current interpreter set to repo Makefile `PYTHON` and routed to current specs |

## Process Contract Mirrors

These pages should become spec mirrors, not concept doctrine.

| page | reason | first repair |
|---|---|---|
| [[enforcement-and-process-rules]] | repo process contract mirror | mirrored to [[specs/codex-ratchet/enforcement-process-rules-current|enforcement-process-rules-current]]; concept page marked historical |
| [[llm-controller-contract]] | repo controller contract mirror | mirrored to [[specs/codex-ratchet/llm-controller-contract-current|llm-controller-contract-current]]; concept page marked historical |
| [[lego-sim-contract]] | repo lego/sim contract mirror | mirrored to [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]] with `sim_execution_kind`, `tool_lego_fit_probe`, and `divergence_log` rules |
| [[classical-baseline-vs-canonical-tool-boundary]] | important policy page with dated examples | marked concept policy snapshot; April examples labeled dated; current contracts/status mirrors linked |
| [[manifold-wizard-operation-router]] | Wizard/process routing | marked process router snapshot; sim/proof/tool-stage work routed to the sim full-wizard runbook and current process mirrors |
| [[codex-ratchet-cs-bounded-system-framing]] | useful CS translation, but source paths moved | marked conceptual controller model snapshot; moved plan paths repaired to `system_v5/docs/plans/plans/...`; current specs linked |
| [[controller-state-transition-model]] | useful model, stale source paths | marked conceptual controller model snapshot; moved plan paths repaired to `system_v5/docs/plans/plans/...`; current specs linked |

## Historical Snapshots To Downrank

These may remain useful, but should not read as live current status.

| page family | reason | first repair |
|---|---|---|
| [[battery-index]] | April index with authoritative language | marked historical battery snapshot; routed current status to contract/status mirrors |
| [[migration-registry]] | old migration registry | marked historical migration snapshot; added not-live-result-count boundary |
| [[v5-content-gap-analysis]] | dated 2026-04-05 integration guide | marked historical gap snapshot; routed current status to specs |
| [[todo]] | stale worklist | archive or rewrite from current blockers |
| [[todo-additional-reference-docs]] and [[todo-philosophical-harness-docs]] | legacy queues | mark historical and link remaining gaps |
| `current-pre-axis*` pages | April snapshots with current titles | marked historical pre-Axis snapshots; routed current status to v5 spec mirrors |
| [[session-handoff-2026-04-07]] | session artifact with invalidation risks | marked session-artifact snapshot; counts/successes require current receipts before reuse |
| [[session-handoff-2026-04-13-automated-run-and-tool-sims]] | mixed external/session report | marked session-artifact snapshot; moved plan paths repaired; current claims require repo receipts |
| [[system-context-handoff-current]] | title says current, framing says legacy | marked legacy handoff snapshot with title caveat |
| `venv-*` pages | cleanup state is stale | marked cleanup snapshots; deletion/readiness claims require fresh local reverify |
| [[sim-corrections-and-classifications]] and [[sim-session-index]] | old result/status snapshots | marked historical correction/session catalogue snapshots |

## Source Path Repair Buckets

These are not conceptual failures. They are mostly path-migration and exact-result-file drift.

| bucket | affected examples | repair |
|---|---|---|
| one-level `system_v5` plans directory moved under the double-`plans` directory | [[aligned-sim-backlog-and-build-order]], [[controller-state-transition-model]], [[current-geometry-spine-status]], [[geometry-ingredient-map]], [[leviathan-world-engine-memo]] | handled for listed pages: moved paths repaired and concept pages downranked/routed to spec mirrors |
| old `system_v4/probes/a2_state/sim_results` exact JSON filenames missing | [[executable-root-axiom-micro-sims]], [[sim-tranche-2026-04-14-axioms-tools-gerbes-motives]], [[igt-atom-result-audit]], [[gerbe-g-tower-and-motives-packets]] | handled as source-present/result-missing or result-partial snapshots; next repair is exact receipt recovery, relink, or bounded rerun |
| raw reference docs moved/renamed | [[bootpack-thread-a-v2-60]], [[axis-0-spec-options]], [[legacy-physics-cosmology]], [[evolutionary-epistemology-reference]] | handled for listed pages: repointed to existing raw/legacy docs and added source/genealogy fences |
| `/tmp` scan artifacts | [[repo-tool-use-router]], [[sim-math-geometry-result-surface-router]], [[mmm-source-language-reservoir]], [[mmm-saliency-test-harness]], [[qit-graph-geometry-promotion-router]] | handled for listed pages: `/tmp` artifacts marked ephemeral; durable authority routed to READ ONLY corpora, repo receipts, or spec mirrors |

## Keep In Concepts

These are concept/source/salience pages. Repair wording if needed, but do not turn them into repo spec mirrors.

| page family | keep reason | repair style |
|---|---|---|
| [[owner-thesis-and-cosmology]], [[my-inputs-on-retrocausality]], [[entropic-monism-origin-and-cosmology]] | owner/source doctrine and TOE reservoir | preserve source voice; label candidate/proof boundary |
| [[legacy-physics-cosmology]], [[grandmaster-of-the-universe]], [[the-dark-empress]], [[legacy-source-history]] | legacy genealogy | fix source paths; do not promote |
| [[holodeck-docs]], [[projective-holodeck-memory-model]], [[holodeck-as-recall-space]], [[holodeck-doctrine]] | Holodeck concept/source model | keep source/generated split; soften implementation/proof wording |
| [[leviathan-framework]], [[leviathan-science-method-qit-engine-crosswalk]], [[leviathan-world-engine-memo]] | source/cross-domain synthesis | fix paths; keep live Lev repo authority separate |
| [[emotional-evolution-personality-system]], [[legacy-psychology-personality]] | personality source/genealogy | keep as candidate engine grammar, not typology canon |
| [[mmm-source-language-reservoir]], [[mmm-language-sea-quotes-couplings-triples]], [[wizard-v4-2-mini-mmm-redesign-spec]] | MMM salience reservoir | durable receipts before doctrine use |
| [[nominalist-translation-rules]], [[note-what-nominalist-reframing-actually-requires]], [[anti-reification-and-nominalism-reference]] | language discipline | avoid mechanical nominalist phrasing; preserve scoped survived/killed/open |

2026-05-21 keep-in-concepts pass:
- handled the owner/cosmology, Holodeck/Leviathan, personality/MMM, and nominalist-language concept slice;
- kept the pages in `/concepts` as source/salience/genealogy surfaces rather than converting them into repo spec mirrors;
- repaired the stale Dark Empress PDF source path, moved `/tmp` MMM worker artifacts out of durable `sources`, and fixed query/entity namespace wikilinks;
- added candidate/source/proof fences around owner physics identities, Holodeck implementation language, Leviathan crosswalk language, personality/governance mappings, MMM prompt-use claims, and anti-reification examples;
- validation after the pass: wiki probe clean, 90 audited frontmatter source refs present, 0 `/tmp` entries in audited `sources`.

## Reference Math Pages

Reference math can stay in `/concepts`, but should not smuggle repo admission.

First repair candidates:

- [[clifford-algebra-qit]]
- [[clifford-chirality-admissible-generators]]
- [[information-geometry-reference]]
- [[quantum-information-measures]]
- [[resource-theories-quantum-reference]]
- [[quantum-shannon-theory-reference]]
- [[tensor-network-axis0]]
- [[gerbe-g-tower-and-motives-packets]]
- [[g-tower-hopf-weyl-integration]]

Repair rule: split standard math facts, source analogy, and repo-earned artifact claims.

2026-05-21 reference-math pass:
- handled first candidate slice across Clifford, information geometry, quantum-information/resource/Shannon, tensor-network Axis 0, G-tower/Hopf/Weyl, and gerbe/G-tower/motives pages;
- repaired moved/missing source paths where found;
- downranked `current` pages to reference/candidate/snapshot framings where they carried repo-admission or pass language;
- split standard theorem wording from legacy/source analogy and repo-earned receipt claims;
- copied the source-present/result-unverified pattern from the source-path repair bucket onto tensor/G-tower pages with stale pass/canonical rows.

## Move Discipline

Before moving a page:

1. add or verify a replacement target under `/specs/codex-ratchet/`;
2. leave an Obsidian-compatible redirect or short stub if links are likely to exist;
3. do not move source/genealogy/salience pages merely because they are imperfect;
4. update only exact links touched by the move;
5. keep repo counts generated from repo evidence, not hand-maintained prose.
