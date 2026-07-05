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

## Queue A — repo-current doctrine / bridge docs status map

2026-07-03 path/status audit: the live Codex Ratchet repo stores these surfaces under `system_v5/docs/`, not the older `system_v5/new docs/` path. This table is a routing/project-tracker snapshot only: this tick checked file presence and wiki landing routes, and reread `AGENTS.md`, `LLM_CONTROLLER_CONTRACT.md`, `NOMINALIST_CS_AND_JP_SYSTEMS_TERMS.md`, and `OWNER_DOCTRINE_SELF_SIMILAR_FRAMEWORKS.md` for authority shape. It did not rerun repo tests, validators, or result artifacts.

| Repo-current source | Wiki landing / status | Next action |
|---|---|---|
| `system_v5/docs/plans/plans/geometry_stack_ratchet_doctrine.md` | [[geometry-stack-ratchet-doctrine]] exists | landed; keep as support/router, not proof |
| `system_v5/docs/LLM_CONTROLLER_CONTRACT.md` | [[llm-controller-contract]] exists | landed; keep status-label discipline close to front doors |
| `system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md` | [[enforcement-and-process-rules]] exists | landed; use for build-order/process guardrails |
| `system_v5/docs/ANOMALOUS_COMPUTER_SCIENCE_TRANSLATION.md` | [[anomalous-computer-science-translation]] exists | landed; keep as CS translation layer |
| `system_v5/docs/NOMINALIST_CS_AND_JP_SYSTEMS_TERMS.md` | [[nominalist-cs-jp-systems-bridge]] exists under the repo-declared mirror slug | landed as bridge/crosswalk; do not create duplicate slug |
| `system_v5/docs/OWNER_DOCTRINE_SELF_SIMILAR_FRAMEWORKS.md` | [[self-similar-frameworks-and-teleological-doctrine]] exists under the repo-declared mirror slug | landed as doctrine/support mirror; do not create duplicate slug |
| `system_v5/docs/LEGACY_CONTEXT_AND_GENEALOGY.md` | [[legacy-context-and-genealogy]] exists | landed; preserves genealogy without present-tense promotion |
| `system_v5/docs/plans/plans/TOOL_CAPABILITY_AND_INTEGRATION_LEDGER.md` | [[tool-capability-and-integration-ledger]] exists | landed; use for capability-gap/tool-routing questions |
| `system_v5/docs/TOOL_LEGO_INTEGRATION_MATRIX.md` | [[tool-lego-integration-matrix]] exists | landed; use as matrix/router support |
| `system_v5/docs/plans/plans/sim_process_gap_log.md` | [[sim-process-gap-log]] exists | landed 2026-07-05 as repo-current process-gap digest; prior-audit/source snapshot only, no rerun/promotion |
| `system_v5/docs/V5_CONTENT_GAP_ANALYSIS.md` | [[v5-content-gap-analysis]] exists | landed; use as gap-planning surface |
| `system_v5/docs/CLASSICAL_DOC_ILLUMINATION_INDEX.md` | no public wiki landing found in this tick | open Queue A gap; candidate support-router tranche after `sim_process_gap_log` |

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

2026-07-01 routing correction: PEPS3D references in older wiki/repo routing are stale, but do not say CTMRG is globally retired. The retired carrier is the single-fused PEPS3D contraction; CTMRG remains admissible inside nested 2D PEPSKit layers when a receipt carries contraction-error certificates. The current honest Codex Ratchet spine is the deflation map and nested PEPS2D/Hopfield-plus-certified-carrier routing, and the verdict audit receipt remains prior-audit evidence for wiki routing. See [[deflation-map-2026-06-04]] and [[verdict_audit_receipt_2026-06-04|verdict audit receipt 2026-06-04]].

1. Completed: `TAIJITU_PROBE_RECONCILIATION_CARD` → [[taijitu-probe-reconciliation-card]]. Keep it as a symbolic-reconciliation digest, not a front-door doctrine page.
2. Completed: `JUNGIAN_FUNCTIONS_AND_IGT_EXPLICIT_MATH_GEOMETRY_MAP` → [[jungian-functions-and-igt-explicit-math-geometry-map]]. Keep geometry, operator math, ordered tokens, and stage grammar explicitly separate.
3. Completed: artifact audit of the atom chain and nearest follow-ons → [[igt-atom-result-audit]]. Keep the audit honest: `exists` only unless rerun in-session.
4. Blocked: local rerun of the seven-atom chain with the repo interpreter. Do not treat this as the next active wiki spine until the blocker is cleared and rerun evidence exists.
5. Next: route Codex Ratchet pages through the deflation map and verdict audit evidence; patch stale carrier references by separating retired single-fused PEPS3D from still-valid per-2D-layer CTMRG, without promoting any carrier to formal admission.
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

**Current Queue E status: IGT source extraction is already public-routed and source-hash checked (verified 2026-06-30)**
- Gate status: `UNBLOCKED` snapshot (2026-06-04). The 9 pending codex2 verdicts were independently audited and rerun at that time — see [[deflation-map-2026-06-04]] and `wizard/hermes-version-current/verdict_audit_receipt_2026-06-04.md`. 8/9 were audit-confirmed and 1 was fabricated. Do not treat this line as a fresh rerun unless a later tick reruns it.
- The seven-atom local rerun is no longer the named gating item in this queue. The already-landed extraction page is [[igt-axes-terrain-source-extraction-2026-06-04]], which processes the 10 listed source docs into structured axis→math mappings, engine patterns, testable predictions, and open discriminators.
- 2026-06-29 cron guard: `/tmp/igt_source_extraction.md` was absent when checked, so the earlier `Active: codex2 ... is extracting` line is now stale prior-plan language, not a live worker fact. The 10 listed source docs were present on disk, but no extraction artifact was promoted from `/tmp` in that tick.
- 2026-06-29 routing repair: this cron tick directly read [[igt-axes-terrain-source-extraction-2026-06-04]], confirmed it is already indexed, added frontmatter/role fences, and routed it through [[current-research-overlays]] and [[topic-map]]. Claim ceiling: dated source-processing page plus routing coherence only; no fresh extraction rerun, no source-hash recomputation, no sim rerun, and no QIT/Axis/trigram promotion.
- 2026-06-30 source-freshness recheck: the ten listed docs were present at both the off-vault READ ONLY source root and the wiki-local raw mirror; all SHA256 values matched the existing [[igt-axes-terrain-source-extraction-2026-06-04]] source table, and desktop/wiki raw copies matched byte-for-byte. This was freshness/routing evidence only, not a new extraction or sim rerun.
- 2026-06-30 Axis3 discriminator-design tranche: the bounded Axis3 inner/outer-vs-chirality/type test design was added to [[igt-axes-terrain-source-extraction-2026-06-04]]. Claim ceiling: proposal/test design only; no sim was run, and Axis3 remains strongest-as-inner/outer but still open against live chirality/type/flux alternatives until a finite observable test excludes them.
- 2026-07-01 Axis5 discriminator-design tranche: the bounded Axis5 symbolic-overlay test design was added to [[igt-axes-terrain-source-extraction-2026-06-04]]. Claim ceiling: proposal/test design only; no sim was run, and Axis5 remains strong as an operator/generator-family split while S-curve, lobe-weighting, `FeFi`/`TiTe`/`TeTi`, and unequal-win/loss language remain live overlays until finite observables exclude or admit them.
- 2026-07-02 64-slot scaffold-fencing tranche: the stale Ax3/Ax4/Ax5 line meanings from `64_HEXAGRAM_STATE_SPACE.md` were routed into [[igt-axes-terrain-source-extraction-2026-06-04]] as a fence, not a duplicate concept page. Claim ceiling: source/routing guard only; no sim was rerun, and the prior `eng_64_hexagram_julia_results.json` remains snapshot evidence (`tool_lego_fit_probe`, `promotion_allowed=false`, `n_distinct=16`).
- 2026-07-02 Axis4 discriminator-design tranche: the bounded Axis4 symbol-direction test design was added to [[igt-axes-terrain-source-extraction-2026-06-04]]. Claim ceiling: proposal/test design only; no sim was run, and Axis4 remains strong as a noncommuting order split while clockwise/counterclockwise and older `TiFe`/`FeTi` visual-direction language stay live overlays until finite observables exclude or admit them.
- Next safe wiki move: step back to the broader project tracker/repo-current queue before adding more IGT prose, unless a future owner/controller request explicitly asks for another IGT symbolic-overlay tranche.

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
