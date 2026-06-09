---
title: Cross-Field Research Intersection Map
created: 2026-05-18
updated: 2026-05-18
type: concept
tags: [research, mmm, systems, formal-methods, topology, qit]
sources:
  - /tmp/opus_research_field_map_narrow_out.json
  - /tmp/wiki_source_corpus_mmm_inventory_20260518.json
  - queries/whole-wiki-mmm-source-research-campaign-2026-05-18.md
framing: current
---

# Cross-Field Research Intersection Map

## Purpose
This page maps external research fields into the wiki as support lanes for future enrichment and MMM/harness compression.

It is not a proof surface. It is a saliency and routing surface: it names fields, concepts, search terms, authors, intersection points, and no-overclaim fences so future agents can find aligned research without letting external vocabulary replace the system's own constraint-first spine.

## Controller boundary
The Opus worker produced the field map below from a bounded read-only prompt. Hermes/controller has not independently verified every paper/author claim here. Treat the map as a research queue and saliency guide, not as a completed bibliography.

# Field-Intersection Map — Wiki MMM Enrichment 2026-05-18

Worker receipt. Compact mapping from external fields to current wiki surfaces, with patch/create targets, search seeds, and overclaim fences. Research support, not repo evidence.

---

## 1. Viability theory
- **Aligned concepts:** [[basin-stability-and-viability-support]] (viability kernel, reachable set, safe trajectory, constraint-over-time); [[anti-teleology-future-option-selection]] (viable continuations).
- **Future intersection:** viability kernel as the formal proxy for "admissible continuations"; 1-Wasserstein viability could ground anti-teleology over distributions rather than points.
- **Pages to patch/create:** patch the two above; create `concepts/viability-kernel-as-future-option-formal-proxy.md`.
- **Search terms / authors:** viability kernel, reachable set, invariant set, set-valued analysis, capture basin, Wasserstein viability — Aubin, Saint-Pierre, Frankowska, Cardaliaguet, Quincampoix.
- **Fence:** a viability kernel computed under a reduced encoding is not the full system's viable set; "admissible continuation" in prose is not a computed kernel.

## 2. Dynamical systems / attractor basins
- **Aligned concepts:** [[systems-philosophy-attractor-basin-inversion]] (basin from repeated survival), [[basin-stability-and-viability-support]] (perturbation stability), [[perturbation-depth-basin-edge-table]].
- **Future intersection:** Menck-style basin-stability volume gives an operational replacement for prose "basin pull"; multi-node basin stability matches the row-level scout work; bifurcation as basin-edge generator.
- **Pages to patch/create:** patch the three above; create `concepts/basin-stability-volume-operational-witness.md`.
- **Search terms / authors:** basin stability, multi-node basin stability, fractal basin boundary, Milnor attractor, riddled basin, Hopf bifurcation — Menck, Kurths, Milnor, Strogatz, Ott, Feudel.
- **Fence:** an "attractor" named in prose remains a candidate until perturbation/return-rate evidence exists; salience of the word is not evidence of the structure.

## 3. Cybernetics
- **Aligned concepts:** [[systems-philosophy-attractor-basin-inversion]] (feedback, error correction, Ashby variety, regulator theorem); implicit in MMM tool-action grammar.
- **Future intersection:** Ashby's Law of Requisite Variety formally grounds "strong constraints require wide exploration"; Conant–Ashby good-regulator theorem links viability to a model carried inside the regulator.
- **Pages to patch/create:** create `concepts/requisite-variety-wide-exploration-support.md`, `concepts/good-regulator-theorem-support.md`; cross-link to [[llm-bias-inversion-rules]].
- **Search terms / authors:** requisite variety, good regulator theorem, viable system model, second-order cybernetics, autopoiesis — Ashby, Conant, Beer, von Foerster, Maturana, Varela, Pask.
- **Fence:** cybernetic vocabulary is a pressure lens, not authority; "purposive system" readings smuggle teleology back in unless future-option pressure is held distinct from goal-destiny.

## 4. Topological data analysis (TDA)
- **Aligned concepts:** [[basin-stability-and-viability-support]] (persistent topology of dynamics, zigzag for Hopf); [[topology-carrier-tool-lane]]; GUDHI in [[repo-tool-use-router]].
- **Future intersection:** persistence diagrams as basin-edge witnesses; zigzag persistence detecting parameterized basin transitions; Mapper as state-space partition probe; persistent-homology fractal-dim estimate as basin-shape descriptor.
- **Pages to patch/create:** patch the three above; create `concepts/persistence-as-basin-edge-witness.md`.
- **Search terms / authors:** persistent homology, zigzag persistence, Mapper, persistence diagram, persistence landscape, stability theorem — Carlsson, Edelsbrunner, Ghrist, Cohen-Steiner, Chazal, Bubenik, Tralie.
- **Fence:** persistence is filtration-relative; calling structure "persistent" without naming the filtration and the stability witness is overclaim.

## 5. Graph / hypergraph / cell complexes
- **Aligned concepts:** [[basin-stability-and-viability-support]] (higher-order dynamics, multi-way constraints); [[repo-tool-use-router]] (XGI, TopoNetX, rustworkx, NetworkX); [[topology-carrier-tool-lane]].
- **Future intersection:** Kuramoto on cell complexes as multistability witness on higher-order carriers; differentiable cell-complex inference (DCM) for learning carrier topology; higher-order contagion as analogy fence (carrier, not metaphysics).
- **Pages to patch/create:** patch the three above; create `concepts/higher-order-carrier-support-map.md`.
- **Search terms / authors:** higher-order networks, simplicial Kuramoto, Hodge Laplacian, hypergraph contagion, cell-complex Langevin, topological signal processing — Battiston, Bianconi, Lambiotte, Bick, Schaub, Hajij, Bodnar.
- **Fence:** multi-way structure is load-bearing only when pairwise reduction provably loses dynamics; otherwise the higher-order carrier is decorative.

## 6. Formal methods / SMT
- **Aligned concepts:** [[repo-tool-use-router]] (z3/cvc5 as SMT falsifier, UNSAT/countermodel surface); [[smt-formal-falsifier-lane]]; tool-action grammar in MMM reservoir.
- **Future intersection:** UNSAT core as basin-boundary certificate; bounded model checking as perturbation-depth proxy; SMT countermodel as concrete kill-witness; CHC/Alloy for higher-level structural counterexamples; model counting for basin-volume bounds.
- **Pages to patch/create:** patch the two above; create `concepts/unsat-core-as-basin-boundary-witness.md`.
- **Search terms / authors:** SMT, UNSAT core, bounded model checking, CHC, TLA+ refinement, Alloy, abstract interpretation, model counting — de Moura, Bjørner, Kroening, Lamport, Jackson, Cousot.
- **Fence:** UNSAT in a reduced encoding is not whole-system proof; "killed by SMT" only kills the claim under the exact encoding submitted, not its prose paraphrase.

## 7. Quantum information theory (QIT)
- **Aligned concepts:** corpus family `entropy_qit` (216 files); [[qit-graph-geometry-promotion-router]] (referenced); MMM grammar around distinguishability, channel, density, entropy.
- **Future intersection:** relative entropy / quantum Fisher information as formal distinguishability metric for probe-relative identity; quantum channels / POVMs as a probe-model formalism; entanglement entropy as multi-way-carrier witness.
- **Pages to patch/create:** patch [[qit-graph-geometry-promotion-router]]; create `concepts/qit-distinguishability-probe-relative-support.md`.
- **Search terms / authors:** von Neumann entropy, relative entropy, quantum Fisher information, POVM, quantum channel, Stinespring dilation, data processing inequality — Nielsen, Chuang, Wilde, Hayden, Renner, Petz, Preskill.
- **Fence:** QIT transfers metrics, not metaphysics; "noncommutation" in classical-state grammar is an analogy until a quantum probe is encoded and measured; entropy bounds are not basin existence.

## 8. Tensor networks
- **Aligned concepts:** MMM tool-action nouns (tensor contraction); [[repo-tool-use-router]] (e3nn / PyG / torch / autograd) as adjacent compute surfaces.
- **Future intersection:** MPS/PEPS/MERA as carrier-compression ansätze for basin/manifold representation; tensor-train as a candidate for high-dimensional viability-kernel storage; ZX-calculus as a graphical-rewrite layer for noncommutation grammar.
- **Pages to patch/create:** create `concepts/tensor-network-carrier-compression-support.md`; cross-link to [[repo-tool-use-router]] and [[qit-graph-geometry-promotion-router]].
- **Search terms / authors:** MPS, PEPS, MERA, tensor train, tensor network contraction, ZX-calculus, bond dimension — Vidal, Verstraete, Cirac, Orús, Schollwöck, Coecke, Stoudenmire.
- **Fence:** a tensor-network ansatz that fits a basin shape is a representation hypothesis, not evidence the system is generated by that ansatz; bond dimension is a compression knob, not an ontological commitment.

## 9. Active inference / Free Energy Principle
- **Aligned concepts:** [[anti-teleology-future-option-selection]] (active inference as support analogy only, fenced); [[basin-stability-and-viability-support]] (policy-selection cluster); the existing FEP-as-not-root-ontology fence is already on the page.
- **Future intersection:** expected free energy as formal proxy for "future-option pressure" — many futures weighted, none privileged; k-means policy embedding as concrete pruning method; ontology fence must stay louder than the analogy.
- **Pages to patch/create:** patch [[anti-teleology-future-option-selection]] (reinforce fence, add bounded EFE-as-proxy paragraph); create `concepts/active-inference-future-option-support-fenced.md`.
- **Search terms / authors:** active inference, expected free energy, free energy principle, sophisticated inference, policy selection, hierarchical generative models — Friston, Parr, Da Costa, Sajid, Tschantz, Millidge, Buckley.
- **Fence:** FEP/active inference is a pressure lens, not root ontology; one expected future must not become privileged essence; EFE math is not proof the system runs on FEP.

## 10. Quality diversity / evolutionary search
- **Aligned concepts:** [[systems-philosophy-attractor-basin-inversion]] (novelty search, MAP-Elites, exploration/exploitation); [[anti-teleology-future-option-selection]] (quality-diversity lane); [[mass-sim-generator-wide-exploration-support]] (referenced).
- **Future intersection:** MAP-Elites archive as concrete instantiation of "wide exploration is required under strong constraints"; novelty search as evidence that goal-directedness is not necessary for finding basins; QD archive as basin-witness ledger; illumination as anti-collapse mechanism.
- **Pages to patch/create:** patch the three above; create `concepts/quality-diversity-as-wide-exploration-support.md`.
- **Search terms / authors:** MAP-Elites, novelty search, quality diversity, illumination algorithm, behavior characterization, CMA-ME — Mouret, Lehman, Stanley, Cully, Pugh, Clune, Fontaine.
- **Fence:** a QD archive shows that diverse niches were reachable under the chosen behavior characterization; it does not prove those niches are causally generative of the basin.

## 11. Operationalism · Nominalism · Process philosophy (three distinct lenses, held apart)
- **Aligned concepts:** corpus family `nominalism_identity` (143 files); [[mmm-formal-noun-and-great-sentence-reservoir]] (probe-relative identity, distinguishability, indistinguishable under); anti-reification grammar across the wiki.
- **Future intersection:**
  - *Operationalism* — bridge from prose claim to admissibility check ("which operation would witness this?").
  - *Nominalism* — keeps "name ≠ object"; supports probe-relative identity and resists reification of attractors.
  - *Process philosophy* — supports directedness without final-cause privilege; partner-language for anti-teleology, distinct from active-inference's information-theoretic frame.
- **Pages to patch/create:** create three separate pages — `concepts/operationalism-probe-relative-witness-support.md`, `concepts/nominalism-anti-reification-support.md`, `concepts/process-philosophy-anti-teleology-philosophical-support.md`; patch [[mmm-formal-noun-and-great-sentence-reservoir]].
- **Search terms / authors:** operationalism (Bridgman); nominalism, indistinguishability, ontological commitment (Quine, Goodman, Hartry Field); process philosophy, occasion of experience, prehension (Whitehead, Stengers, Rescher); relational physics (Rovelli) as bridge.
- **Fence:** philosophical pressure lenses are not authority replacements; quoting Whitehead, Quine, or Bridgman does not license a basin claim without an operational witness — and these three lenses must not be flattened into one "anti-realist" lane.

---

## Cross-field intersections worth a single page
- **Viability × TDA × Higher-order:** persistent features of viable sets on cell-complex carriers — `concepts/persistent-viability-on-higher-order-carriers.md`.
- **SMT × Viability:** UNSAT cores as boundary certificates of viability kernels — folds into `concepts/unsat-core-as-basin-boundary-witness.md`.
- **QIT × Operationalism:** distinguishability under probe as the empirical content of probe-relative identity — covered in lane 7 page.
- **Active inference × Quality diversity:** wide policy populations vs. EFE-pruned policies as two anti-teleology mechanisms held distinct, not merged.

## Global no-overclaim fences (apply to every entry)
- Research support is not repo evidence.
- Source resonance is not equivalence.
- A geometry/topology/QIT/FEP word is a routing hint until support is checked.
- A research lane that converges with the wiki's prose is pressure, not proof.
- Philosophical lenses are pressure lenses; they do not replace operational witness.

---

## Worker return

1. **Checked:** the five concept/query pages and the corpus inventory JSON named in the task card. No other files read. No edits.
2. **Concluded:** 11 fields mapped with aligned wiki concepts, future intersections, patch/create targets, search seeds, and per-field fences; cross-field bridges identified; global fences restated in the wiki's existing grammar.
3. **Remains open:**
   - Whether referenced pages (e.g. [[qit-graph-geometry-promotion-router]], [[mass-sim-generator-wide-exploration-support]], [[mmm-formal-noun-and-great-sentence-reservoir]], [[topology-carrier-tool-lane]], [[smt-formal-falsifier-lane]]) actually exist with the surfaces assumed here was not verified — controller should confirm before patching.
   - Tensor-networks lane has the thinnest current wiki anchor; it is more "future intersection" than "present alignment" and should not be promoted past that.
   - Process-philosophy lane needs author/source vetting before becoming a page; Whitehead/Stengers risk attracting the very teleology the wiki is trying to fence out.
4. **Surviving challenge to the framing:** the user list groups *operationalism / nominalism / process philosophy* as one bucket. Collapsing them is anti-collapse failure — operationalism is a witness-method, nominalism is an identity-grammar, process philosophy is a directedness-grammar. They were held distinct here; controller should keep them as three pages, not one. Likewise, active inference and quality diversity both support anti-teleology by different mechanisms and should not be merged into a single "future-option" lane.

## Controller next tranche
Create or patch one lane at a time. The strongest immediate candidates are:

1. `attractor-basin-research-support-map` — joins viability, basin stability, TDA, cybernetics, and quality diversity while preserving anti-teleology.
2. `mmm-source-language-reservoir` — extracts source-corpus language into compact MMM preinjection material.
3. `viability-kernel-as-future-option-formal-proxy` — makes future-option pressure operational without final-cause drift.
4. `unsat-core-as-basin-boundary-witness` — links z3/cvc5 proof tools to basin-boundary falsifier language.

## Related pages
- [[whole-wiki-mmm-source-research-campaign-2026-05-18]]
- [[basin-stability-and-viability-support]]
- [[systems-philosophy-attractor-basin-inversion]]
- [[anti-teleology-future-option-selection]]
- [[repo-tool-use-router]]
- [[topology-carrier-tool-lane]]
- [[smt-formal-falsifier-lane]]
- [[qit-graph-geometry-promotion-router]]
- [[mmm-formal-noun-and-great-sentence-reservoir]]
