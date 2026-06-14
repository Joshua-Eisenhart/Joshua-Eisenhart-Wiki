# Wiki Ingest Queue and Priorities

Purpose: bounded ingest queue for what still needs to be processed into the wiki from live repo/current surfaces, result artifacts, tool-gap surfaces, and separate external sources.

Status: active current ingest-planning note.

Use this when:
- deciding the next bounded wiki ingest tranche
- choosing between repo-doc ingest, result-artifact ingest, tool-gap ingest, and external-source ingest
- preventing overnight/manual wiki work from drifting into salience-first blob building

Current truth:
- The wiki is structurally clean, but many live repo/current surfaces and result families still need deeper bounded routing or ingestion.
- The overnight run has mostly improved role clarity and front-door discipline so far; that reduces blob risk but does not by itself complete repo/result ingest.
- Ingest should stay bounded: one cluster, one packet family, or one external-source tranche at a time.
- The main ranking question is entropy/refinement level, not a hard canon/non-canon split: all of these surfaces reflect on the same idea-space, but some are better front doors and others are driftier support/reflection material.
- The project history matters for routing: many ideas first appeared as application/pattern recognitions and only later ratcheted back toward root constraints and a sim/proof system, so genealogy pages should preserve that path rather than rewriting everything as if it started fully root-first.
- External LEV runtime material is separate-but-connected: ingest it only as runtime/control-plane bridge language, not as a replacement for the constraint/geometry spine.

## Priority order
0. Current-route correction when front doors are wrong (example: current Wizard binding is v4.3; v4.3 is object-preservation / maintenance preflight, v4.2 remains runtime, and v4.1 is legacy/provenance only).
1. Repo-current doctrine/bridge docs that look highly connected but under-routed in the public wiki.
2. Result/sim artifact families that already exist on disk and need clean public landing/routing.
3. Tool-gap and capability-ledger surfaces that describe still-open capability holes.
4. External-source ingest such as `lev_mega_book_curated.pdf`, but only with explicit bridge fencing.

## Queue A — ingest first: repo-current doctrine / bridge docs

These look like the highest-value next public routing/deepening candidates from `system_v5/new docs/` and `system_v5/new docs/plans/`:

- `plans/geometry_stack_ratchet_doctrine.md`
  - why: likely a strong geometry-order/stack doctrine surface that should connect to current geometry/support pages
- `LLM_CONTROLLER_CONTRACT.md`
  - why: truth-label discipline and hard-stop language should stay tightly routed under the front door as the wiki deepens
- `ENFORCEMENT_AND_PROCESS_RULES.md`
  - why: build-order and process-standard framing belong close to the anti-drift controller contract and should remain visibly distinct from finished proof
- `ANOMALOUS_COMPUTER_SCIENCE_TRANSLATION.md`
  - why: looks like a direct bridge page between system-native framing and CS/runtime language
- `NOMINALIST_CS_AND_JP_SYSTEMS_TERMS.md`
  - why: likely strong bridge/crosswalk material for nominalist-CS / JP-facing vocabulary
- `OWNER_DOCTRINE_SELF_SIMILAR_FRAMEWORKS.md`
  - why: likely live owner-side doctrine support for existing framework/teleology/self-similar surfaces
- `LEGACY_CONTEXT_AND_GENEALOGY.md`
  - why: likely the cleanest repo-current source for preserving the system's older idea genealogy without flattening it into present authority
- `plans/TOOL_CAPABILITY_AND_INTEGRATION_LEDGER.md`
  - why: likely live capability-gap ledger that should tighten wiki tooling-status / tool-capability routing
- `TOOL_LEGO_INTEGRATION_MATRIX.md`
  - why: likely live matrix surface that may deserve a cleaner wiki router / support note
- `plans/sim_process_gap_log.md`
  - why: likely direct support for current process-gap and controller-maintenance pages
- `V5_CONTENT_GAP_ANALYSIS.md`
  - why: explicit gap surface; useful for planning what repo doctrine still lacks clean wiki landing
- `CLASSICAL_DOC_ILLUMINATION_INDEX.md`
  - why: likely useful as a bounded support router for classical doctrine mirrors

## Queue B — ingest soon: result / sim artifact families

These already exist on disk and likely need better public landing, packetization, or routing one family at a time:

### B1. Cl(3) / Cl(6) result family
- `system_v4/probes/results/sim_cl3_basis.json`
- `system_v4/probes/results/sim_cl3_bivector_exp.json`
- `system_v4/probes/results/sim_cl3_rotor_product.json`
- `system_v4/probes/results/sim_cl3_composition.json`
- `system_v4/probes/results/sim_cl3_reflection.json`
- `system_v4/probes/results/sim_cl3_invariants.json`
- `system_v4/probes/results/sim_cl6_basis.json`
- `system_v4/probes/results/sim_cl6_rotor_product.json`
- `system_v4/probes/results/sim_cl6_spin_group_embedding.json`
- `system_v4/probes/results/sim_cl6_chirality.json`
- why: these are compact, already-artifacted, and fit bounded packet/public-router ingest well

### B2. Lego result families
- `system_v4/probes/sim_results/lego_*.json`
- strong examples:
  - `lego_info_geometry_results.json`
  - `lego_positive_maps_results.json`
  - `lego_quantum_capacities_results.json`
  - `lego_fiber_bundles_results.json`
  - `lego_flux_candidates_results.json`
- why: many likely exist only as artifacts or partial summaries; good tranche shape is one lego family at a time

### B3. Geometry / engine result families
- `system_v4/probes/sim_results/geom_*.json`
- `system_v4/probes/sim_results/engine_*_results.json`
- why: likely under-routed relative to the geometry/engine concept pages already in the wiki

### B4. Classical doctrine mirrors
- `system_v4/probes/classical_doctrine_mirrors/sim_results/*.json`
- why: these are especially good for bounded “classical baseline mirror” routing pages without widening into whole-program synthesis

## Queue C — ingest as explicit open gaps / maintenance surfaces

These look like live open gaps that should drive bounded wiki work:

- Treat this lane as dated capability/gap evidence at mixed refinement levels. Keep freshness dates visible, and do not let repo presence or tool usage alone count as `canonical by process`.

- `concepts/tooling-status.md`
  - still-open items named there:
    - TopoNetX barely used
    - XGI multi-way packet relations missing
    - cell-complex reasoning on shell families missing
    - promotion pressure remaining gap
- `concepts/research-source-coverage-index.md`
  - explicit rule: every owner page should eventually point either to a downloaded source packet or an explicit citation-only queue
- `concepts/arxiv-2603-21852-eml-operator.md`
  - explicit gap: atomized EML legos do not yet count as landed sim work in the wiki
- `concepts/pauli-on-weyl-loop-interaction.md`
  - explicit note that it is not yet a finished/closed doctrine page

## Queue D — separate-but-connected external ingest only as bridge

### D1. LEV runtime/control-plane book
- `/Users/joshuaeisenhart/Desktop/lev_mega_book_curated.pdf`
- safe landing type:
  - runtime/control-plane bridge source
  - crosswalk page
  - explicit same / analogous / different mapping
- do not use as:
  - theorem source
  - replacement vocabulary for root doctrine pages
- best first tranche:
  - raw provenance wrapper
  - extracted text artifact
  - title/introduction/table-of-contents mapping
  - one bounded LEV-term ↔ current-system crosswalk page

### D2. Codex Ratchet `READ ONLY Reference Docs`
- `/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/READ ONLY Reference Docs`
- status:
  - eventually needs processing and ingestion
  - higher-entropy and drift-prone reflection corpus on the same overall idea-space
  - not a front-door authority surface by default, but still useful as deeper support/genealogy/recovery material
  - for now, ingest should be done here in a bounded controller/manual lane, not by the overnight wiki run
- safe use:
  - support-layer enrichment
  - genealogy/context recovery
  - entropy-refinery input for Hermes/manual processing before promotion into cleaner wiki surfaces
  - bounded backfill for pages that already have stronger current authority surfaces
- unsafe use:
  - replacing current doctrine pages
  - outranking `system_v5/new docs` or the repo-current controller contract
  - treating higher-entropy reference prose as if it were already refined enough for `hermes-current/` or other front-door pages
  - letting the overnight wiki run wander into this high-drift corpus before a bounded manual ingest plan exists
- best first tranche:
  - build a filename/content inventory
  - group by cluster
  - identify which existing wiki pages need support-only backlinks or caveated source additions
  - only then process one bounded cluster at a time

## Queue E — IGT / I-Ching / Taijitu source doc family (HIGH PRIORITY symbolic/correlation lane)

Large body of source material in `system_v5/READ ONLY Reference Docs/` that is only partially ingested so far. These docs cover the IGT win/lose/WIN/LOSE pattern system, the I-Ching/hexagram correlation layer, and the yin-yang / taijitu symbolic layer. They are their own independent sim target — do NOT pre-map onto QIT engine doctrine.

**Fencing rule**: IGT/I-Ching/taijitu docs are correlation layers and symbolic witnesses. They are not primary math docs. Ingest them with explicit fencing: symbolic layer ≠ math anchor, and no convergence with QIT engines should be claimed until independently-run sims agree on invariants.

### E1. Primary source docs (read before any sim or wiki work on IGT)

| Doc | Lines | Content |
|---|---|---|
| `JUNGIAN_FUNCTIONS_AND_IGT_EXPLICIT_MATH_GEOMETRY_MAP copy.md` | 425 | Explicit three-layer map: carrier geometry / operator math / IGT stage grammar. Keeps layers separate. Most authoritative IGT source. |
| `TAIJITU_AXES_0_6_EXPLICIT_SYMBOLIC_LAYER copy.md` | 450 | Taijitu symbolic layer for all 7 axes. Explicit strong/weak alignments with current lower-stack atlas. |
| `TAIJITU_PROBE_RECONCILIATION_CARD copy.md` | 86 | **Already well-structured**: strong alignments, active mismatches, demoted hypotheses, live symbolic assignments, next sim discriminators, fences. |
| `iching axes rosetta.md` | 84 | Owner's working notes mapping I-Ching / yin-yang symbol onto axes 0-6. Raw/working, not doctrine. |
| `Rosetta Terrain Mapping.md` | 111 | Terrain names mapped onto symbolic layer. |
| `terrain rosetta strong math.md` | 187 | Terrain map with explicit math. |
| `terrains.md` | 174 | Terrain definitions. |
| `Ring Checkerboard Gradient .md` | 14 | Ring checkerboard = IGT carrier pattern. |
| `math free axes.md` | 88 | Axes described without math (symbolic). |
| `primitive axes with no math.md` | 109 | Earlier version of axis descriptions. |

### E2. Existing sim probes for IGT/I-Ching (already in repo)

- atom-chain family:
  - `sim_igt_atom_1_carrier.py`
  - `sim_igt_atom_2_structure.py`
  - `sim_igt_atom_3_reduction.py`
  - `sim_igt_atom_4_admissibility.py`
  - `sim_igt_atom_5_distinguishability.py`
  - `sim_igt_atom_6_chirality.py`
  - `sim_igt_atom_7_coupling.py`
- `sim_igt_nested_WIN_LOSE_attractor.py`, `sim_igt_win_lose_atomic.py`
- `sim_igt_deep_nested_win_lose_irreducibility.py`, `sim_igt_deep_ring_topology_chirality.py`
- `sim_igt_yin_yang_ansatz.py`, `sim_igt_nested_yin_yang_IGT_equivalence.py`
- `sim_yinyang_axis_mapping.py` — demoted as witness surface, not authority surface
- `64_HEXAGRAM_STATE_SPACE.md` in `system_v4/docs/` — fenced proposal-only scaffold (line meanings for Axis 3/4/5 stale)

### E3. What the TAIJITU_PROBE_RECONCILIATION_CARD says about what still needs sims

- `Axis 3`: needs one bounded discriminator — do 16 chart-locked macro-stage tokens cluster by inner/outer loop class better than older chirality language?
- `Axis 4`: keep symbolic CW/CCW fenced; runtime anchor is `UEUE` vs `EUEU`
- `Axis 5`: needs discriminator only if testing whether S-curve proposal tracks T vs F operator split
- 64-slot scaffold: needs fencing not rewrite — stale Axis 3/4/5 line meanings must not re-enter live stack

### E4. Recommended ingest approach (one tranche at a time)

2026-06-04 routing correction: PEPS3D references in older wiki/repo routing are stale; CTMRG/PEPS3D is retired as load-bearing per the 2026-06-03 session handoff. The current honest Codex Ratchet spine is the deflation map, and the verdict audit receipt provides fresh evidence for wiki routing. See [[deflation-map-2026-06-04]] and [[verdict_audit_receipt_2026-06-04|verdict audit receipt 2026-06-04]].

1. Completed: `TAIJITU_PROBE_RECONCILIATION_CARD` → [[taijitu-probe-reconciliation-card]]. Keep it as a symbolic-reconciliation digest, not a front-door doctrine page.
2. Completed: `JUNGIAN_FUNCTIONS_AND_IGT_EXPLICIT_MATH_GEOMETRY_MAP` → [[jungian-functions-and-igt-explicit-math-geometry-map]]. Keep geometry, operator math, ordered tokens, and stage grammar explicitly separate.
3. Completed: artifact audit of the atom chain and nearest follow-ons → [[igt-atom-result-audit]]. Keep the audit honest: `exists` only unless rerun in-session.
4. Blocked: local rerun of the seven-atom chain with the repo interpreter. Do not treat this as the next active wiki spine until the blocker is cleared and rerun evidence exists.
5. Next: route Codex Ratchet pages through the deflation map and verdict audit evidence; patch stale carrier references without promoting PEPS3D/CTMRG.
6. Then: I-Ching hexagram structure sim (`sim_iching_trigram_adjacency`, `sim_iching_hexagram_structure`) — pure combinatorial, no QIT framing.
7. Do NOT ingest as: convergence claims, doctrine updates, or QIT engine evidence.


## Queue G — math / geometry / anti-teleology source alignment
- source-doc processing ledger: [[read-only-source-doc-processing-ledger-2026-05-18]]

- `queries/math-geometry-anti-teleology-source-alignment-audit-2026-05-18.md`
- priority: high
- why: reconciles READ ONLY legacy/reference source docs with sim math/geometry surfaces and the anti-teleology / future-option selection frame.

## Queue F — whole-wiki research / MMM / tool-use gap audit
- `queries/whole-wiki-research-mmm-tool-gap-audit-2026-05-18.md`
- priority: high
- why: this captures the broad user request to improve the wiki as a harness/MMM estate, not just patch one route.
- first three tranches: tool-use router, MMM reservoir, research lane queue.


## 2026-05-19 source-corpus deep reading correction

Planning/control note: [[source-corpus-deep-reading-parallel-plan-2026-05-19]].

Correction: the READ ONLY source corpora and book/thread-scale works must not be reduced to tiny repo-spec summaries. The next large campaign should use Sonnet-high/Claude Code parallel workers when available to actually read source packets, produce layered executive summaries, extract themes/concepts/research/tool connections, and only then synthesize educational wiki pages. Repo application remains downstream and fenced, not the whole meaning of the source.

Near-term launch prep: build a manifest with file sizes, rough token estimates, packet boundaries, worker receipt templates, and parent/child lane assignments for:
- `system_v5/READ ONLY Reference Docs`
- `READ ONLY Legacy core_docs`
- Dark Empress / other book-scale sources
- old thread dumps and generated/high-entropy mixed sources


## 2026-05-19 math / geometry learning-wiki correction

Planning/control note: [[math-geometry-learning-wiki-plan-2026-05-19]].

Correction: the screenshot folder and screenshot-derived math are source material for an educational math/geometry curriculum, not just attachments or repo-spec evidence. The wiki needs pages that teach the system's math: G-structures, manifold layers, Hopf/fiber/bundle geometry, operators, Lindblad/Hamiltonian dynamics, entropy/information, topology, terrain grammar, and symbolic/correlation layers.

Near-term launch prep: build a screenshot manifest and run vision/OCR workers over the 26 screenshot files in `raw/articles/system-v5-reference-docs/Screenshots`, then synthesize concept pages and a reader-facing learning path.

First approved math/geometry curriculum batch: 40 pages, recorded in [[math-geometry-learning-wiki-plan-2026-05-19#First 40 math/geometry learning pages]]. Process in sub-batches of 5-8 pages; do not create 40 thin stubs.

Root-constraint retune: current formal sims now test whether `F01_FINITUDE` + `N01_NONCOMMUTATION` force or fail to force the layered finite noncommutative geometry / central attractor-basin surface. Math/geometry wiki pages must make this explicit: no basin/manifold/layer/gauge/engine claim advances without both roots tested and independently ablated. See [[math-geometry-learning-wiki-plan-2026-05-19#2026-05-19 root-constraint attractor-basin correction]].

First concept-page candidates from sampled screenshots:
- density operators and Bloch vectors
- Pauli Hamiltonians and ladder operators
- Lindblad operators and dissipators
- projectors/dephasing/filters
- topology/terrain chart grammar
- Hamiltonian sign flip and Type 1/Type 2 terrain candidates
- G-structures and manifold-layer reductions


## 2026-05-19 concepts whole-set processing correction

Planning/control note: [[concepts-whole-set-processing-plan-2026-05-19]].

Correction: `/Users/joshuaeisenhart/wiki/concepts` is becoming redundant. The next safe wiki move is not more page creation by default; it is a read-only whole-concepts cluster audit, role assignment, merge/archive plan, and then bounded consolidation tranches.

Observed snapshot: 377 active concept markdown files. High-overlap filename clusters include geometry (19), source (18), tool (15), manifold (11), research (11), basin (10), entropy (5), terrain (5), operator (4), Weyl (3), G-structure (2), and Hopf (2). Filename scan proves redundancy risk but does not decide merges.

Rule: before more concept-page expansion, assign page roles: educational concept, source digest, result/sim ledger, project application, comparison, router/index, glossary, or archive candidate.

## 2026-05-19 physics / ToE cluster route

Audit artifact: [[physics-toe-cluster-readonly-audit-2026-05-19]].

The open ToE / physics-model question now has a read-only role/source map. The current path is not to create a new giant ToE page yet. Use existing pages in this order: [[owner-thesis-and-cosmology]] as broad candidate-thesis router, [[entropic-monism-origin-and-cosmology]] as the educational physics-model entrypoint, [[legacy-physics-cosmology]] as the source-genealogy router, [[my-inputs-on-retrocausality]] as owner-kernel source language, then math-carrier pages and result routers.

Next safe tranche: continue source-packet extraction. `x grok chat TOE.txt` is already fully read and its owner-kernel extraction has been added to [[eisenhart-unified-physics-module]]. Continue with the high-entropy generated summaries and PDFs with owner-kernel vs generated-elaboration separation.

## 2026-05-19 all-model family route

Audit artifact: [[model-family-reality-cluster-audit-2026-05-19]].

User correction: the wiki should dig deeper into the whole model family, not only the ToE/physics lane. Include Holodeck, Leviathan v3.2, Dark Empress, Grandmaster, personality/IGT mode grammar, QIT/math carriers, READ ONLY source docs, and related research.

Route decision: do not make one giant all-model synthesis page. Keep family lanes separate and use the audit as the control map. The shared self-similar generator can be taught through crosswalks, but Holodeck, QIT, science method, IGT/personality, Leviathan, and physics/cosmology must remain distinct roles.

Completed 2026-05-19: Packet B extraction for `grok unified phuysics nov 29th.txt` now lives at [[packet-b-grok-unified-physics-extraction-2026-05-19]] and has been summarized into [[eisenhart-unified-physics-module]]. It is contradiction-bearing source material, not physics proof.

Completed 2026-05-19: Holodeck source packet extraction now lives at [[holodeck-source-packet-extraction-2026-05-19]]. It preserves the owner kernel from `holodeck-docs-md.txt` lines 34-48 and fences generated hardware/tooling/physics/Klein/consciousness elaboration. It deepens existing Holodeck lane pages instead of creating another public concept page.

Completed 2026-05-19: Packet C extraction for `grok eisenhart model .txt` now lives at [[packet-c-grok-eisenhart-model-extraction-2026-05-19]] and has been summarized into [[eisenhart-unified-physics-module]].

Completed 2026-05-19: Packet D extraction for `gemini toe summary volume 1-23.pdf` now lives at [[packet-d-gemini-toe-summary-extraction-2026-05-19]] and has been summarized into [[eisenhart-unified-physics-module]].

Next safe source tranche: proceed in packet order without widening into a giant synthesis. Preferred next broad all-model packet is Leviathan v3.2; if the controller wants to stay inside the ToE/physics lane one more step, Packet E is the `gemini hexagram spinor arch.txt` 12-bit stack architecture, followed by the Dark Empress book packet, Grandmaster book packet, personality/IGT packet, QIT/math-carrier packet, then external research bridge packet.

## Recommended first bounded tranche

**Already completed (2026-04-15):**
- `plans/G_TOWER_HOPF_WEYL_INTEGRATION_SPEC.md` → [[g-tower-hopf-weyl-integration]] ✅
- Cl(3)/Cl(6) result family → [[cl3-cl6-result-family]] ✅

**Already completed in Queue E:**
- `TAIJITU_PROBE_RECONCILIATION_CARD copy.md` → [[taijitu-probe-reconciliation-card]] ✅
- `JUNGIAN_FUNCTIONS_AND_IGT_EXPLICIT_MATH_GEOMETRY_MAP copy.md` → [[jungian-functions-and-igt-explicit-math-geometry-map]] ✅
- artifact audit of the atom chain and nearest follow-ons → [[igt-atom-result-audit]] ✅

**Completed: Queue A doctrine/genealogy refresh**
- `geometry_stack_ratchet_doctrine.md` → [[geometry-stack-ratchet-doctrine]] ✅
- `LEGACY_CONTEXT_AND_GENEALOGY.md` → [[legacy-context-and-genealogy]] ✅
- basis: log entries from 2026-04-16 and 2026-04-17 plus live page/index presence checked 2026-04-24

**Current correction tranche completed 2026-05-18: Wizard v4.2 baseline repair; amended 2026-06-13 for v4.3**
- repaired root Wizard front doors, `wizard/AGENTS.md`, root `index.md`, the Hermes Wizard skill, and progress/audit routing so v4.2 is current runtime and v4.1 is legacy/provenance.
- 2026-06-13 amendment: front doors now name the current binding as **v4.3**: v4.3 object-preservation / maintenance preflight where scoped, legacy v4.2 provenance thereafter.
- this does not complete the wiki; it only fixes the immediate front-door routing error.

**Next tranche: Queue E local rerun — blocked/deferred by Codex Ratchet status snapshot**
- Gate status: `UNBLOCKED` (2026-06-04). The 9 pending codex2 verdicts have been independently audited and rerun — see [[deflation-map-2026-06-04]] and `wizard/hermes-version-current/verdict_audit_receipt_2026-06-04.md`. 8/9 audit-confirmed, 1 fabricated.
- The seven-atom local rerun is no longer the gating item. The gate is now the IGT source extraction: processing the 10 source docs in `system_v5/READ ONLY Reference Docs/` into structured axis→math mappings, engine patterns, and testable predictions.
- Active: codex2 (GPT-5.5 xhigh) is extracting from all 10 IGT/axes/terrain source docs (~3,400 lines) into `/tmp/igt_source_extraction.md`. When it lands, the next wiki move is creating pages that carry the actual patterns in testable form.

Best external tranche, but later:
- LEV book title/introduction/TOC ingest as a fenced bridge-only lane

Do not:
- turn this queue into a giant omnibus backlog with no ordering
- ingest external bridge material into root doctrine pages
- promote artifact existence into stronger truth labels without repo-backed verification
- widen a single ingest tick into a whole cluster rewrite unless routing repair in the same cluster is strictly required

Related notes:
- [[active-plans]]
- [[wiki-harness-progress-and-audit]]
- [[projects/codex-ratchet/read-first]]
- [[hermes-memory-offload]]

Write mode: controller-maintained.
## 2026-05-18 whole-wiki MMM/source/research campaign

Current broad campaign page: [[whole-wiki-mmm-source-research-campaign-2026-05-18]].

Use it when the goal is overall wiki processing rather than one current sim. It covers READ ONLY source corpora, already-run sim catalogues, aligned research support, attractor-basin thinking, tool/research intersections, and MMM/saliency compression surfaces.

Next bounded tranche should usually be one of: MMM source-language reservoir, attractor/basin research support map, cross-field research intersection map, or a source-cluster ledger.

## 2026-05-18 all-Hermes-wiki-skills run

Receipt: [[wiki-all-skills-run-receipt-2026-05-18]].

Result: the live structural probe stayed clean, and the existing queue/campaign/router pages are still the correct control surfaces. The run did not create a duplicate omnibus queue. It narrowed the next safe work to one bounded tranche from the already-routed set.

Next admissible wiki-only tranche if Codex Ratchet status is not green: deepen one thin tool/reference page from [[repo-tool-use-router]], deepen one research lane from [[whole-wiki-research-mmm-tool-gap-audit-2026-05-18]], or process one already-run result family from [[sim-run-catalogue-and-result-family-router]] at catalogue/router status only.
