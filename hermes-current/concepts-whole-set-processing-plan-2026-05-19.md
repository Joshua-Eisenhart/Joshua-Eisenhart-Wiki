# Concepts Whole-Set Processing Plan — 2026-05-19

Purpose: stop concept-page sprawl/redundancy and process `/Users/joshuaeisenhart/wiki/concepts` as a whole set.

Status: active cleanup/control note.

## Correction being preserved

The concepts folder is becoming redundant. Adding one more routing page for every correction can make the wiki worse even when each page is locally useful.

The whole concept set must be processed as a corpus:

- identify overlapping pages
- assign page roles
- merge or archive duplicates
- keep educational pages readable
- keep repo/spec/result ledgers separate from learning pages
- preserve source provenance without multiplying tiny routers
- route first-40 math/geometry pages into existing pages where possible instead of creating unnecessary new stubs

## Observed snapshot, 2026-05-19

`/Users/joshuaeisenhart/wiki/concepts` active markdown files observed: 377.

High-overlap clusters found by filename scan:

- geometry: 19 pages
- source: 18 pages
- tool: 15 pages
- manifold: 11 pages
- research: 11 pages
- basin: 10 pages
- entropy: 5 pages
- terrain: 5 pages
- operator: 4 pages
- Weyl: 3 pages
- G-structure: 2 pages
- Hopf: 2 pages

This is only a filename-level scan. It is enough to prove redundancy risk, not enough to decide merges.

## 2026-05-19 first read-only audit artifact

Audit artifact: [[concepts-cluster-audit-2026-05-19]].

This is a filename/frontmatter/body-skim clustering pass over 377 active concept files. It found 344 cluster-hit rows across geometry/G-structure/manifold, basin/attractor, source/research, tools, and entropy/terrain/operator packets. It is not a merge decision. Use it to assign reading packets to workers.

## Required processing method

Do not keep adding pages as the default move.

For each cluster, workers should produce a cluster report:

1. all pages in cluster
2. page role for each page
3. overlap / duplicate content
4. which page should be the main educational page
5. which page should be a source/provenance page
6. which page should be a result/sim ledger
7. which page should be archived or merged
8. which page needs rewriting for readability
9. which links/routes must be repaired
10. whether any page should remain because it has a distinct role

## Page-role taxonomy

Use these roles before editing:

- educational concept page: teaches the idea
- source digest: summarizes source docs/screenshots/threads/books
- result/sim ledger: tracks receipts and claim ceilings
- project application page: explains repo use only
- comparison page: distinguishes nearby ideas
- router/index page: points to a cluster, should be few
- glossary/dictionary page: term definitions only
- archive candidate: duplicate/stale/outdated after merge

A cluster can have several pages, but not several pages doing the same role.

## Priority clusters

### 1. G-structure / manifold / geometry cluster

Reason: current correction revealed that G-structure pages and new ledgers can quickly multiply.

Candidate pages from filename scan include:

- `g-structure-tower.md`
- `g-structure-variant-sim-ledger.md`
- `g-tower-hopf-weyl-integration.md`
- `geometry-ingredient-map.md`
- `geometry-stack-ratchet-doctrine.md`
- `support-first-constraint-manifold-dependency-chain.md`
- `constraint-manifold-architecture.md`
- `current-geometry-spine-status.md`
- `differential-geometry-and-bundles-reference.md`
- `fiber-bundles-and-spin-geometry.md`
- `fiber-bundles-and-spin-geometry-reference.md`
- `hopf-fibration-mathematics.md`
- `hopf-foliation-structure.md`

Needed output:

- one main educational geometry/G-structure page or small set
- one variant sim ledger
- one source/provenance digest if needed
- one project application/status page if needed
- archive/merge recommendations for duplicates

### 2. Basin / attractor / viability cluster

Reason: F01+N01 basin pressure just created new pages, but the cluster already had many basin pages.

Candidate pages include:

- `f01-n01-root-constraint-basin-pressure.md`
- `basin-manifold-claim-contract.md`
- `attractor-basins-formal-reference.md`
- `basin-stability-and-viability-support.md`
- `systems-philosophy-attractor-basin-inversion.md`
- `attractor-basin-classifier-case-table.md`
- `attractor-basin-result-surface-ledger.md`
- `attractor-basin-row-level-evidence-ledger.md`
- `perturbation-depth-basin-edge-table.md`
- `qit-basin-engine-synthesis.md`

Needed output:

- educational basin primer
- root-pressure page
- claim contract
- result/evidence ledger(s)
- merge/archive list

### 3. Source / research cluster

Reason: source docs and research should become readable learning surfaces, not scattered source indexes.

Candidate pages include source-notes indexes, research inventories, research-support bibliography, cross-field research intersection map, source-language reservoir, and source digest pages.

Needed output:

- stable source processing spine
- research learning path
- archive/merge stale indexes where possible

### 4. Tools cluster

Reason: tool pages should teach tools and distinguish mention/import/install/callable/supportive/load-bearing/canonical-by-process.

Needed output:

- educational tool pages
- repo tool-use router
- result/receipt matrix
- archive/merge duplicative status pages

## Parallel worker plan

When Sonnet high / Claude Code is available, run this as a parallel cluster audit.

Parent lanes:

1. geometry/G-structure cluster auditor
2. basin/attractor cluster auditor
3. source/research cluster auditor
4. tools/tooling cluster auditor
5. entropy/terrain/operator cluster auditor
6. navigation/index integrity auditor

Each worker should be read-only first. No worker should archive or rewrite pages until the controller accepts the cluster map.

## Worker receipt format

- cluster name
- files read
- role assigned to each page
- overlap map
- recommended main page(s)
- recommended merge targets
- archive candidates
- pages that should stay separate
- link/routing repairs needed
- proposed new pages, if any, with justification
- risk of losing important source/provenance
- next safe edit tranche

## Stop rule

Do not add more concept pages for this lane unless one of these is true:

- no existing page can carry the role
- the new page is a cluster-level control/ledger page needed before merging
- the user explicitly wants a new educational page
- a source/sim receipt needs a distinct result ledger

Otherwise, patch/merge existing pages.

## Immediate next tranche

Run a read-only whole-concepts cluster audit and produce a merge/role map before further concept-page expansion.

Related notes:

- [[math-geometry-learning-wiki-plan-2026-05-19]]
- [[source-corpus-deep-reading-parallel-plan-2026-05-19]]
- [[wiki-ingest-queue-and-priorities]]

Write mode: controller-maintained.


## 2026-05-19 geometry/G-structure/manifold cluster audit

Audit artifact: [[geometry-gstructure-manifold-cluster-readonly-audit-2026-05-19]].

This read-only pass inspected 15 high-priority geometry/G-structure/manifold pages and produced role guesses plus high-overlap pairs. It does not decide merges. Provisional structure: keep educational reference pages separate from system synthesis/application pages, keep `g-structure-variant-sim-ledger` as a result/variant ledger, and inspect overlap pairs before any archive/merge action.


## 2026-05-19 geometry consolidation decision packet

Decision packet: [[geometry-gstructure-manifold-consolidation-decision-packet-2026-05-19]].

This packet proposes roles and a first safe edit tranche for the geometry/G-structure/manifold cluster. It recommends keeping educational pages, G-structure variant ledgers, synthesis/application pages, and status routers separate; flags `constraint-manifold-architecture` as a placeholder repair/archive candidate; and flags `fiber-bundles-and-spin-geometry` vs `fiber-bundles-and-spin-geometry-reference` as the first likely merge/redirect pair.

## 2026-05-19 physics / ToE cluster audit

Audit artifact: [[physics-toe-cluster-readonly-audit-2026-05-19]].

This read-only pass answers the open "own physics model / ToE" question by mapping the existing cluster before further concept expansion. It found that the physics model is already present but split across candidate-thesis pages, legacy source digests, thin generated-source pages, math-carrier pages, research support pages, and result routers. First role clarification landed in [[owner-thesis-and-cosmology]], [[entropic-monism-origin-and-cosmology]], [[legacy-physics-cosmology]], and [[eisenhart-unified-physics-module]].

Next safe tranche: Packet B (`grok unified phuysics nov 29th.txt`) is now extracted at [[packet-b-grok-unified-physics-extraction-2026-05-19]] and summarized into [[eisenhart-unified-physics-module]]. Continue packet-by-packet: Holodeck source packet next for the broader all-model lane, or Packet C (`grok eisenhart model .txt`) if staying inside ToE/physics formula/claim extraction; then `gemini toe summary volume 1-23.pdf`, Dark Empress Part 3 / Chapters 9-13, and OCR for `grok rosetta stone.pdf`.

## 2026-05-19 Holodeck source packet extraction

Extraction artifact: [[holodeck-source-packet-extraction-2026-05-19]].

This packet confirms the concepts-folder consolidation rule: the Holodeck lane did not need a new concept page. The existing page roles are adequate; the missing piece was a source-level extraction ledger that separates the owner memory/world-model kernel from generated hardware/tooling/physics/Klein/consciousness elaboration. First safe follow-through is role/source-control patching on [[holodeck-docs]] and [[projective-holodeck-memory-model]], not concept sprawl.

## 2026-05-19 all-model family cluster audit

Audit artifact: [[model-family-reality-cluster-audit-2026-05-19]].

This read-only pass extends the ToE audit into the larger family the user named: reality/ToE, Holodeck, Leviathan v3.2, Dark Empress, Grandmaster, self-similar five-framework doctrine, personality/IGT mode grammar, and QIT/math carrier pages. It found that the wiki already contains the major families, but the learning path is still distributed and redundancy-prone.

Provisional structure: do not create one giant model page. Keep separate lanes for candidate reality/physics, Holodeck memory/world-model architecture, Leviathan runtime/governance provenance, legacy book-scale sources, IGT/personality grammar, and QIT/math carriers. Use crosswalks to show the shared F01+N01 / bounded-order generator without collapsing the families into a single object.

Next safe tranche: Packet B (`grok unified phuysics nov 29th.txt`) has now been extracted at [[packet-b-grok-unified-physics-extraction-2026-05-19]], and the Holodeck packet has now been extracted at [[holodeck-source-packet-extraction-2026-05-19]]. Continue packet-by-packet through Leviathan v3.2 for the broad all-model lane or Packet C (`grok eisenhart model .txt`) for the narrower ToE/physics formula lane; then proceed to Dark Empress, Grandmaster, personality/IGT, and QIT/math carriers.

## 2026-05-19 Leviathan v3.2 Governance & Community Ingestion

Extraction artifact: [[packet-k-leviathan-v3-2-governance-and-community-extraction-2026-05-19]].

This packet continues the concepts-folder consolidation rule. It processes the remainder of the Leviathan v3.2 book (Chapters 3, 4, 8, 12, 14, 15, 16, and 17) covering multi-layered delegated proxy voting with 60% base veto power, the Anti-Internet offline social layer, pre-established trolley car guidelines (prioritizing inaction and rule-followers), the cooperative community layer, and onboarding paths. It deepens [[leviathan-framework]] and [[leviathan-system]] rather than creating new concept-page sprawl.

Next safe source tranche: The preferred next broad all-model packet is Packet E (`gemini hexagram spinor arch.txt`) 12-bit stack architecture, followed by the Dark Empress book packet, Grandmaster book packet, personality/IGT packet, QIT/math-carrier packet, and then the external research bridge.

