---
type: query
created: 2026-05-18
updated: 2026-05-18
tags: [research, mmm, harness, tooling, audit, wizard]
sources:
  - /tmp/wiki_whole_scan_20260518.json
  - /tmp/wiki_external_grok_gemini_audit_20260518.json
---

# Whole-Wiki Research / MMM / Tool Gap Audit — 2026-05-18

## Purpose
This is the receiving queue for the user's request to work on the whole wiki, not just one front-door patch.

The wiki should compress into a harness and MMM estate. That means the next work is not only page cleanup. It must improve:

- research coverage for the kind of system being built;
- tool-use documentation for the repo's growing proof/sim/tool estate;
- MMM quality as a language-and-structure substrate;
- sentence-level and noun-level alignment, not just keyword frequency;
- Grok/Gemini/Claude/Codex pressure as external audit lanes, without letting provider agreement promote truth.

## Evidence used
- Local scan artifact: `/tmp/wiki_whole_scan_20260518.json`.
- External pressure artifact: `/tmp/wiki_external_grok_gemini_audit_20260518.json`.
- Key status: Grok/xAI and Gemini keys were loaded from `~/.zshrc` / Hermes env without printing secrets.
- Boundary: this page is an audit and queue. It does not claim the listed pages are already fixed.

## Top tranche queue

### 0. Systems philosophy / attractor-basin inversion
The wiki must preserve wide exploration under strong constraints so basins emerge rather than being named prematurely. See [[systems-philosophy-attractor-basin-inversion]] and the research queue [[systems-attractor-basin-research-queue-2026-05-18]].


### 1. Tool-use and formal-scout integration map
Build a public router that explains how the repo's tool surfaces should be used, one tool/function family at a time.

Targets:
- `system_v5/ops/formal_scouts/`
- `system_v5/ops/tooling/`
- `scripts/`
- `concepts/current-tool-status-installed-vs-missing-vs-not-wired.md`
- thin tool pages such as [[geomstats-manifold-geometry-reference]], [[clifford-geometric-algebra-reference]], [[e3nn-equivariant-geometry-reference]], [[xgi-hypergraph-reference]], and [[rustworkx-graph-algorithms-reference]]

Needed output:
- one tool-use router page;
- per-tool status: installed / callable / used in a probe / load-bearing / open gap;
- exact admissible use: z3/cvc5 for falsifiers, sympy for symbolic sanity, Clifford for rotor/spin algebra, geomstats for manifold ops, e3nn/PyG for equivariant/graph learning, rustworkx/XGI/TopoNetX/GUDHI for graph/hypergraph/topology carriers.

### 2. Research lanes for the actual system being built
Do not search one generic topic. Build lane-specific research queues.

Priority lanes:
- geometric deep learning and equivariant networks: e3nn, PyG, representation constraints;
- topological data analysis and carrier spaces: GUDHI, persistent homology, cell complexes, hypergraphs;
- formal verification and SMT: z3/cvc5 as admissibility/falsifier layers;
- Clifford/spin/fiber-bundle geometry: spinors, chirality, holonomy, special geometry;
- categorical / sheaf / topos / operadic support for relation-first and local-global reasoning;
- resource theories, distinguishability, information geometry, and noncommutation;
- LLM harness research: retrieval, evals, faithfulness, recursive self-improvement, KB compression, tool-use agents.

Needed output:
- update [[research-source-coverage-index]] and [[current-research-overlays]] with these lanes;
- create a query page for arXiv/source intake only after lane mapping is explicit;
- keep humanities/philosophy support lanes citation/bibliography-side unless they have a real arXiv/tool lane.

### 3. MMM quality upgrade: beyond word frequency
MMMs should not only store word distributions. They should carry high-salience language forms that pull future agents into the right basin.

MMM ingredients to add:
- great sentences: short, reusable, high-gradient sentences that encode constraints and prevent collapse;
- great thinkers: not as authority worship, but as resonance handles and counter-bias lenses;
- aligned formal nouns: holonomy, sheaf, fibration, spinor, chirality, obstruction, adjunction, functor, invariant, quotient, gauge, support, carrier, admissibility, distinguishability;
- anti-primitive guard phrases: no primitive identity, equality, time, causality, geometry, probability;
- negative evidence phrases: killed / open / survived / graveyard / falsifier / blocked;
- tool nouns tied to action: z3=falsify, GUDHI=topology witness, Clifford=spin/rotor check, XGI=multi-way relation carrier.

Needed output:
- one `MMM quality rubric` page;
- one `formal noun / great sentence reservoir` page;
- patch the strongest current MMM routers under `wizard/harness-consolidated/` and `wizard/packet-v4-2-current/mmm/` to point to those reservoirs.

### 4. Harness compression and version-sprawl repair
The wiki should compress into usable front doors, not drown agents in packet/version history.

Needed output:
- v4.2-current Wizard route remains dominant;
- v4.1 and earlier packets stay provenance;
- current Hermes spine points to active v4.2 and the MMM reservoirs;
- historical logs are not rewritten, but current front doors must not repeat superseded route claims.

### 5. Repo-added surface reconciliation
The user has added lots to the repo. The wiki needs a repeated reconciliation loop, not one static page.

Needed output:
- scan `system_v5/docs`, `system_v5/new docs`, `system_v5/ops`, and `scripts` for new/high-signal surfaces;
- classify each as: current authority, tool-use doc, result evidence, candidate scout, legacy/provenance, or ignore;
- patch the wiki queue and routing pages in small batches.

## Thin high-value pages found by local scan
These pages are plausible next deepening targets because they are short but central to tools, research, or harness routing:
- `concepts/system-tools-and-plan.md` — 23 lines, 3 links
- `concepts/geomstats-manifold-geometry-reference.md` — 20 lines, 4 links
- `concepts/research-index.md` — 29 lines, 10 links
- `concepts/clifford-geometric-algebra-reference.md` — 20 lines, 5 links
- `concepts/todo-philosophical-harness-docs.md` — 30 lines, 2 links
- `concepts/e3nn-equivariant-geometry-reference.md` — 22 lines, 4 links
- `concepts/constraint-geometry-axis0-separation.md` — 39 lines, 8 links
- `concepts/retooled-external-methods-runtime-design.md` — 17 lines, 4 links
- `concepts/xgi-hypergraph-reference.md` — 20 lines, 4 links
- `concepts/apple-axes-terrain-operator-math.md` — 25 lines, 3 links
- `concepts/fiber-bundles-and-spin-geometry.md` — 42 lines, 16 links
- `concepts/research-index-compression-terms.md` — 37 lines, 7 links
- `concepts/model-math-geometry-sim-plan.md` — 32 lines, 6 links
- `concepts/pre-axies-math-and-geometry-work-out.md` — 19 lines, 3 links
- `concepts/why-qit-engines-need-exotic-geometry.md` — 18 lines, 5 links
- `concepts/rustworkx-graph-algorithms-reference.md` — 26 lines, 4 links
- `concepts/operator-algebras-and-representation.md` — 38 lines, 7 links
- `concepts/research-inventory-and-foundational-findings.md` — 26 lines, 5 links
- `concepts/bootpack-harness-stack.md` — 16 lines, 2 links
- `concepts/constraint-on-admissibility-entropy-tables-entropic-monism.md` — 38 lines, 4 links
- `concepts/llm-research-enforcement-validator.md` — 34 lines, 6 links
- `concepts/current-tool-status-installed-vs-missing-vs-not-wired.md` — 28 lines, 6 links
- `concepts/llm-bias-and-multi-thread-harness-reference.md` — 37 lines, 5 links
- `concepts/toponetx-topological-complex-reference.md` — 20 lines, 4 links
- `concepts/model-math-geometry-source-digest.md` — 31 lines, 7 links
- `concepts/sympy-symbolic-math-reference.md` — 27 lines, 4 links
- `concepts/gudhi-persistent-topology-reference.md` — 19 lines, 3 links
- `concepts/current-tool-status-operational-classification.md` — 34 lines, 7 links
- `concepts/nominalist-framing.md` — 28 lines, 14 links
- `concepts/constraint-manifold-architecture.md` — 4 lines, 2 links

## External pressure summary

### Grok/xAI pressure
Grok emphasized:
- formal_scout/provider-receipt surfaces as live pressure lanes;
- tool integration across Clifford/e3nn/GUDHI/XGI/TopoNetX/rustworkx/PyG/z3/sympy;
- MMM carrier spaces that include geometry/topology/formal nouns, not only words;
- great-thinker and great-sentence reservoirs as anti-frequency MMM support.

### Gemini pressure
Gemini emphasized:
- a unified/current Wizard/API schema to reduce version sprawl;
- sim-estate integration as the bridge from concept pages to Python execution;
- provider audit receipts as machine-readable health evidence;
- missing quick-start/how-to surfaces for formal scouts and new probes;
- a formal noun dictionary and rationale index for why each tool belongs.

## Immediate next three tranches
1. Tool-use router: created [[repo-tool-use-router]] to map current repo tool surfaces to wiki tool reference pages and stage-gated uses; next step is per-tool deepening.
2. MMM reservoir: created [[mmm-formal-noun-and-great-sentence-reservoir]] as the first formal-noun / great-sentence / thinker-resonance reservoir; next patch current MMM surfaces to consume it.
3. Research lane queue: update research overlays and source coverage with the lane-specific research agenda above. Topology carrier tranche created at [[topology-carrier-tool-lane]].

## Stop conditions
- Do not promote provider suggestions to sim evidence.
- Do not update Codex Ratchet runner/sim status unless a fresh project status and repo checks support it.
- Do not widen one tranche into a whole-wiki rewrite.
- Do not let MMM quality collapse to style imitation or word-frequency-only tuning.

## Related pages
- [[math-geometry-anti-teleology-source-alignment-audit-2026-05-18]]
- [[wiki-ingest-queue-and-priorities]]
- [[research-source-coverage-index]]
- [[current-research-overlays]]
- [[research-support-bibliography]]
- [[current-tool-status-installed-vs-missing-vs-not-wired]]
- [[wiki-as-harness-architecture]]
- [[harness-boot-pack]]
- [[nominalist-translation-rules]]
- [[llm-bias-inversion-rules]]
