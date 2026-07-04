---
title: Wiki-Driven ArXiv Search Queue
created: 2026-04-10
updated: 2026-04-11
type: query
tags: [reference, research, query, ingest]
sources:
  - /Users/joshuaeisenhart/wiki/concepts/research-source-coverage-index.md
  - /Users/joshuaeisenhart/wiki/concepts/current-research-overlays.md
  - /Users/joshuaeisenhart/wiki/concepts/notebooklm-reference-pack-intake.md
  - /Users/joshuaeisenhart/wiki/concepts/research-support-bibliography.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Wiki-Driven ArXiv Search Queue

## Question
Which arXiv sources should be searched next, given the current wiki gaps, routing pages, and open questions?

## Scope
This is an ingest queue, not canon.
It takes the current wiki’s routing cues and turns them into focused arXiv search lanes.
Chinese-philosophy support is kept on the bibliography side unless a search is explicitly comparative or historical.

## What the wiki says is high-yield
Primary signals came from:
- [[research-source-coverage-index]]
- [[current-research-overlays]]
- [[notebooklm-reference-pack-intake]]
- [[research-support-bibliography]]

The strongest next lanes are the ones with either thin source coverage or explicit open questions.

## Search lanes

### 1) Distinguishability / quantum resource theory
Wiki signal:
- operational identity
- probe-relative equivalence
- admissibility under comparison
- trace-distance / resource-theory support

Suggested search phrase:
- `all:quantum+resource+theory+distinguishability`

Seed arXiv hits from the first pass:
- `1510.03695v2` — Relative submajorization and its use in quantum resource theories
- `1907.06306v2` — Resource theory of asymmetric distinguishability for quantum channels
- `1806.04937v3` — The first law of general quantum resource theories
- `2111.12646v4` — Stochastic approximate state conversion for entanglement and general quantum resource theories

Use when the question is: what survives under operational comparison, and what is only a change of description?

### 2) Process / relational / topos support
Wiki signal:
- [[process-philosophy-and-relational-physics]]
- [[topos-quantum-mechanics-reference]]
- relation-first support, not substance-first narration

Suggested search phrase:
- `all:topos+quantum+mechanics`

Seed arXiv hits from the first pass:
- `1004.3561v1` — Topos Quantum Logic and Mixed States
- `0712.4003v1` — Topos theory and `neo-realist' quantum theory
- `quant-ph/9609002v2` — Relational Quantum Mechanics
- `2412.05997v3` — Doubly Quantum Mechanics

Use when the question is: which mathematical frame supports relational reading without collapsing into classical ontology?

### 3) Stochastic thermodynamics / open quantum systems
Wiki signal:
- [[stochastic-thermodynamics-reference]]
- open-system recovery behavior
- dynamical stability and recurrence

Suggested search phrase:
- `all:stochastic+thermodynamics+open+quantum+systems`

Seed arXiv hits from the first pass:
- `quant-ph/0410161v1` — Description of quantum dynamics of open systems based on collision-like models
- `2309.13408v2` — On the unraveling of open quantum dynamics
- `1210.5071v1` — Stochastic Thermodynamics, Reversible Dynamical Systems and Information Theory
- `1911.01730v3` — Thermodynamics of Quantum Causal Models: An Inclusive, Hamiltonian Approach
- `1810.05583v5` — Thermodynamic length in open quantum systems

Use when the question is: what are the minimal thermodynamic or dynamical structures that survive open-system coupling?

### 4) Quantum Shannon / compression / source coding
Wiki signal:
- [[quantum-shannon-theory-reference]]
- [[quantum-information-measures]]
- compression, low-rank structure, and source coding

Suggested search phrase:
- `all:quantum+source+coding+compression`

Seed arXiv hits from the first pass:
- `quant-ph/0209124v3` — Simple construction of quantum universal variable-length source coding
- `1511.06071v2` — Channel Simulation and Coded Source Compression
- `1308.4283v3` — Entanglement-assisted zero-error source-channel coding

Use when the question is: how do compression, coding, and operator truncation line up without forcing a single interpretation too early?

### 5) LLM failure modes / hallucination / faithfulness
Wiki signal:
- [[llm-bias-and-failure-modes-reference]]
- [[llm-ontology-smuggling-reference]]
- [[llm-bias-inversion-rules]]
- support for the wiki’s controller discipline

Suggested search phrase:
- `all:hallucination+large+language+model`

Seed arXiv hits from the first pass:
- `2409.11353v3` — THaMES: An End-to-End Tool for Hallucination Mitigation and Evaluation in Large Language Models
- `2503.21676v2` — How do language models learn facts? Dynamics, curricula and hallucinations
- `2506.22486v1` — Hallucination Detection with Small Language Models
- `2402.11651v2` — Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents
- `2604.08545v1` — Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

Use when the question is: what failure modes need to be controlled before the wiki treats LLM output as stable support?

### 6) Viability / attractor / recurrence
Wiki signal:
- [[viability-theory-reference]]
- [[attractor-basins-formal-reference]]
- [[distance-metrics-state-space]]

Suggested search phrase:
- `all:viability+kernel+attractor+basin`

Seed arXiv hits from the first pass:
- `2107.02684v2` — Collective management of environmental commons with multiple usages: a guaranteed viability approach
- `1907.08101v2` — What attracts to attractors?
- `1308.3819v5` — Fast Basins and Branched Fractal Manifolds of Attractors of Iterated Function Systems
- `2409.01079v1` — Attractor Basins in Concurrent Systems

Use when the question is: which notion is actually load-bearing for persistence under perturbation, viability or attraction?

### 7) Evolutionary / Darwinian / constructor support
Wiki signal:
- [[evolutionary-epistemology-reference]]
- [[evolutionary-models-qit-alignment]]
- [[current-research-overlays]]

Suggested search phrase:
- `all:replicator+dynamics+information+geometry OR all:constructor+theory+information`

Seed arXiv hits from the first bounded search:
- `0911.1383` — Information Geometry and Evolutionary Game Theory
- `1405.5563` — Constructor Theory of Information

Use when the question is: how the wiki's evolutionary lane links selection, admissibility, Fisher-Rao/Shahshahani geometry, and possible/impossible task language without flattening them into one story.

## Secondary lane: geometry / holonomy
Wiki signal:
- [[fiber-bundles-and-spin-geometry]]
- [[quantum-geometry-fubini-study]]
- [[quantum-fisher-information-geometry]]
- [[berry-phase-and-holonomy]]

Suggested search phrase:
- `all:fubini-study+berry+phase+holonomy`

This lane is useful when the search target is intrinsic geometry, transport, and memory under loops.
It is lower priority than the six lanes above because the wiki already has more direct geometry coverage than coverage in the support lanes.

## Ingest rule
For each lane:
1. search arXiv by the suggested phrase
2. read the abstract first
3. if it looks genuinely supporting, add it to the open-access intake or citation-only queue
4. route the paper to the owner page that actually needs it
5. keep support material separate from formal math pages

## Triage note
Not every first-pass hit should be downloaded.
Use the source-coverage pages to decide whether the item is:
- download-first
- citation-only for now
- background support only

## Immediate ingest shortlist
These are the first papers I would move into the reading/ingest lane because their abstracts match the current wiki gaps cleanly:
- `1907.06306v2` — Resource theory of asymmetric distinguishability for quantum channels
- `1510.03695v2` — Relative submajorization and its use in quantum resource theories
- `1004.3561v1` — Topos Quantum Logic and Mixed States
- `2409.11353v3` — THaMES: An End-to-End Tool for Hallucination Mitigation and Evaluation in Large Language Models
- `2503.21676v2` — How do language models learn facts? Dynamics, curricula and hallucinations
- `2402.11651v2` — Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents
- `2506.22486v1` — Hallucination Detection with Small Language Models
- `2412.05997v3` — Doubly Quantum Mechanics

## Priority download order
If I were choosing the next actual downloads, I would start here:
1. `1907.06306v2` — strongest fit for probe-relative distinguishability / resource theory.
2. `1510.03695v2` — adds the geometric/LP-duality side of resource comparison.
3. `1004.3561v1` — clean support for relational / topos framing.
4. `2409.11353v3` — good support for controller discipline around hallucination mitigation.
5. `2503.21676v2` — directly relevant to factual learning dynamics and hallucination emergence.

### Second-pass download order from the current wiki gaps
1. `1810.05583v5` — thermodynamic length / open quantum systems; strongest fit for stochastic thermodynamics + information geometry.
2. `2107.02684v2` — guaranteed viability framing; strongest fit for viability theory.
3. `1511.06071v2` — channel simulation and coded source compression; best fit for the quantum Shannon / compression lane.
4. `1308.4283v3` — entanglement-assisted zero-error source-channel coding; supports exact-coding boundaries.
5. `1907.08101v2` — what makes attractors robust; best for tightening attractor-vs-viability distinctions.

Why this order:
- the first two strengthen the math-first distinguishability lane
- the third strengthens the relation-first / process support lane
- the fourth and fifth strengthen the LLM failure-mode support lane
- the doubly quantum mechanics paper is interesting but less directly tied to the wiki’s current gaps than the three above
- the second-pass set fills the biggest remaining source gaps on stochastic thermodynamics, viability, quantum Shannon, and attractor theory

## Abstract-level readout
This is the next ingest pass: what each paper actually contributes once you read the abstract, in wiki terms.

### 1907.06306v2 — Resource theory of asymmetric distinguishability for quantum channels
- Gives a channel-level resource theory, not just a state-level one.
- Treats distinguishability as an operational resource under superchannels.
- Uses one-shot and asymptotic formulations, including distinguishability distillation and dilution.
- Best fit pages: [[distinguishability-formal-reference]], [[constraint-on-distinguishability]], [[resource-theories-quantum-reference]].

### 1510.03695v2 — Relative submajorization and its use in quantum resource theories
- Generalizes majorization to a relation that handles approximate resource conversion.
- Provides a geometric/LP-duality formulation through Lorenz curves.
- Useful where the wiki wants comparison, reversibility, and constraint geometry rather than simple equality.
- Best fit pages: [[distinguishability-formal-reference]], [[distance-metrics-state-space]], [[quantum-information-measures]].

### 1004.3561v1 — Topos Quantum Logic and Mixed States
- Supports a non-classical logical frame that is distributive, intuitionistic, and contextual.
- Emphasizes geometric underpinning without relying on linear structure as the starting point.
- Good support for relational framing without collapsing into substance-first language.
- Best fit pages: [[topos-quantum-mechanics-reference]], [[process-philosophy-and-relational-physics]], [[current-research-overlays]].

### 0712.4003v1 — Topos theory and `neo-realist' quantum theory
- Gives a shorter relational / topos introduction emphasizing logical aspects and context-relative truth.
- Best fit pages: [[topos-quantum-mechanics-reference]], [[process-philosophy-and-relational-physics]], [[current-research-overlays]].

### quant-ph/9609002v2 — Relational Quantum Mechanics
- Replaces observer-independence with relation-relative state assignment.
- Best fit pages: [[process-philosophy-and-relational-physics]], [[nominalism-in-this-system]], [[current-research-overlays]].

### 1906.10184 — A Free Energy Principle for a Particular Physics
- Gives a Markov-blanket and NESS framing that links directly to active inference and self-organization.
- Best fit pages: [[fep-and-active-inference-reference]], [[autopoiesis-and-enactivism-reference]], [[current-research-overlays]].

### 2409.11353v3 — THaMES: An End-to-End Tool for Hallucination Mitigation and Evaluation in Large Language Models
- Gives a concrete pipeline for hallucination detection and mitigation.
- Useful as a controller-support reference for evaluation, not as a theory page.
- Strongly aligned with the wiki’s insistence on negative tests, mitigation, and explicit handling of failure modes.
- Best fit pages: [[llm-bias-and-failure-modes-reference]], [[llm-ontology-smuggling-reference]], [[llm-controller-contract]].

### 2503.21676v2 — How do language models learn facts? Dynamics, curricula and hallucinations
- Shows factual learning as a staged process with a plateau before precise recall.
- Ties hallucination emergence to knowledge acquisition and data distribution.
- Useful for understanding why bad scheduling can corrupt parametric memory.
- Best fit pages: [[llm-bias-and-failure-modes-reference]], [[current-research-overlays]], [[research-support-bibliography]].

### 1006.1420 — Landauer’s principle in the quantum domain
- Corrects strong-coupling bookkeeping around heat, work, and entropy.
- Best fit pages: [[stochastic-thermodynamics-reference]], [[quantum-information-measures]], [[qit-vocabulary-discipline-reference]].

### quant-ph/0406166v3 — Contextuality for preparations, transformations and unsharp measurements
- Gives operational contextuality over preparations, transformations, and measurements.
- Best fit pages: [[distinguishability-formal-reference]], [[constraint-on-distinguishability-formal-reference]], [[qit-vocabulary-discipline-reference]].

### 1201.6554v2 — Distinct Quantum States Can Be Compatible with a Single State of Reality
- Supports the guardrail that overlap in quantum state descriptions does not itself prove ontology.
- Best fit pages: [[distinguishability-formal-reference]], [[nominalism-in-this-system]], [[current-research-overlays]].

### 2207.05221v4 — Language Models (Mostly) Know What They Know
- Gives a self-evaluation / calibration lane via P(True) and P(IK).
- Best fit pages: [[llm-bias-and-failure-modes-reference]], [[llm-constraint-harness-wiki]], [[current-research-overlays]].

### 2212.09251v1 — Discovering Language Model Behaviors with Model-Written Evaluations
- Uses LM-written evaluations to discover behaviors like sycophancy and inverse scaling.
- Best fit pages: [[llm-bias-and-failure-modes-reference]], [[llm-constraint-harness-wiki]], [[research-support-bibliography]].

### 2212.03551v5 — Talking About Large Language Models
- Warns against anthropomorphizing LLMs and importing human mental-state words too casually.
- Best fit pages: [[llm-ontology-smuggling-reference]], [[llm-bias-and-failure-modes-reference]], [[research-support-bibliography]].

### 2020.acl-main.463 — Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data
- Guards against conflating form-only training with meaning or understanding.
- Best fit pages: [[llm-ontology-smuggling-reference]], [[research-support-bibliography]], [[current-research-overlays]].

### 1810.05583v5 — Thermodynamic length in open quantum systems
- Gives a metric view of open-system dissipation and optimal protocols.
- Best fit pages: [[stochastic-thermodynamics-reference]], [[information-geometry-reference]], [[distance-metrics-state-space]].

### 2107.02684v2 — Collective management of environmental commons with multiple usages: a guaranteed viability approach
- Gives a guaranteed-viability treatment of shared resources and survival under constraints.
- Best fit pages: [[viability-theory-reference]], [[attractor-basins-formal-reference]], [[qit-basin-engine-synthesis]].

### 1511.06071v2 — Channel Simulation and Coded Source Compression
- Connects coded source compression with quantum channel simulation.
- Best fit pages: [[quantum-shannon-theory-reference]], [[compression-to-density-matrix-map]], [[cptp-maps-and-channels]].

### 1308.4283v3 — Entanglement-assisted zero-error source-channel coding
- Useful for exact coding and entanglement-assisted boundaries.
- Best fit pages: [[quantum-shannon-theory-reference]], [[entanglement-theory]], [[quantum-information-measures]].

## Ingested notes now created
These candidate papers now have source-backed or support-note pages in the wiki:
- [[resource-theories-quantum-reference]] — 1907.06306v2, 1510.03695v2, 1806.04937v3, 2111.12646v4
- [[distinguishability-formal-reference]] — 1907.06306v2 and 1510.03695v2
- [[topos-quantum-mechanics-reference]] — 1004.3561v1
- [[llm-bias-and-failure-modes-reference]] — 2409.11353v3, 2503.21676v2, 2402.11651v2, 2506.22486v1
- [[doubly-quantum-mechanics]] — 2412.05997v3
- [[quantum-shannon-theory-reference]] — quant-ph/0209124v3, 1511.06071v2, 1308.4283v3
- [[stochastic-thermodynamics-reference]] — 1810.05583v5, 1210.5071v1, 2309.13408v2
- [[viability-theory-reference]] — 2107.02684v2
- [[attractor-basins-formal-reference]] — 1907.08101v2, 2409.01079v1
- [[process-philosophy-and-relational-physics]] — quant-ph/9609002v2, 0712.4003v1
- [[fep-and-active-inference-reference]] — 1906.10184
- [[llm-constraint-harness-wiki]] — 2604.08545v1, 2207.05221v4, 2212.09251v1
- [[llm-ontology-smuggling-reference]] — 2212.03551v5
- [[stochastic-thermodynamics-reference]] — 1006.1420
- [[distinguishability-formal-reference]] — quant-ph/0406166v3, 1201.6554v2
- [[llm-ontology-smuggling-reference]] — 2020.acl-main.463
- [[llm-bias-and-failure-modes-reference]] — 2305.04388v2

## 2026-04-11 second-pass reprioritization from then-current gaps
This block is query-history. It predates the later geometry/Shannon downloads reflected in [[research-source-coverage-index]]; do not use it as the current coverage ledger. The sharpest remaining gaps were then:
1. `fiber_topology_spin_geometry` — then 0 downloaded; current coverage index shows 2 downloaded ledger/domain rows.
2. `quantum_shannon_compression` — then 0 downloaded; current coverage index shows 2 downloaded ledger/domain rows.
3. `stochastic_thermodynamics` — partially seeded, but still thin for open-system geometry and trajectory-level support.
4. `process_relational_topos` — seeded, but still light enough that one more clean owner-page paper helps.

## Revised priority download order
1. `quant-ph/0310053v1` — Two and Three Qubits Geometry and Hopf Fibrations
2. `hep-th/0404165v5` — Spin Hall effect and Berry phase of spinning particles
3. `quant-ph/0209124v3` — Simple construction of quantum universal variable-length source coding
4. `1511.06071v2` — Channel Simulation and Coded Source Compression
5. `1810.05583v5` — Thermodynamic length in open quantum systems

Why this order now:
- the first two directly patch the thinnest geometry / holonomy lane and route into pages that still lack arXiv-backed additions;
- the third and fourth patch the still-empty quantum-Shannon source lane with clean owner-page fits;
- the fifth remains a high-fit open-systems geometry paper for a lane that is seeded but still thin.

## 2026-04-11 abstract-level readout for the new top lane

### quant-ph/0310053v1 — Two and Three Qubits Geometry and Hopf Fibrations
- Uses Hopf fibrations to describe two- and three-qubit Hilbert-space geometry rather than treating the fibration as a one-qubit curiosity only.
- Makes entanglement content part of the geometric readout, which is a good fit for the wiki's insistence that correlation structure and carrier geometry stay coupled.
- Best fit pages: [[hopf-fibration-mathematics]], [[fiber-bundles-and-spin-geometry-reference]], [[entanglement-theory]].
- Triage: direct support for an owner page, download-first.

### hep-th/0404165v5 — Spin Hall effect and Berry phase of spinning particles
- Treats Berry curvature as load-bearing for spin transport and shows the associated position-space noncommutativity explicitly.
- Good support where the wiki wants Berry phase, holonomy, and spin transport to stay geometric rather than merely metaphorical.
- Best fit pages: [[berry-phase-and-holonomy]], [[fiber-bundles-and-spin-geometry-reference]], [[clifford-algebra-qit]].
- Triage: direct support for geometry/holonomy owner pages, download-first.

### quant-ph/0209124v3 — Simple construction of quantum universal variable-length source coding
- Gives a concrete variable-length source-coding construction with controlled overflow/error behavior.
- Strong fit for the wiki's compression lane because it supports bounded coding and source-rate language without interpretive stretch.
- Best fit pages: [[quantum-shannon-theory-reference]], [[compression-to-density-matrix-map]], [[quantum-information-measures]].
- Triage: direct owner-page support, download-first.

### 1511.06071v2 — Channel Simulation and Coded Source Compression
- Bridges source compression and channel simulation, which is the cleanest current bridge between the wiki's compression pages and channel-language pages.
- Best fit pages: [[quantum-shannon-theory-reference]], [[cptp-maps-and-channels]], [[compression-to-density-matrix-map]].
- Triage: direct owner-page support, download-first.

### 1810.05583v5 — Thermodynamic length in open quantum systems
- Adds a metric/geodesic treatment of minimally dissipative open-system protocols.
- Best fit pages: [[stochastic-thermodynamics-reference]], [[information-geometry-reference]], [[distance-metrics-state-space]].
- Triage: direct owner-page support, download-first.

## Cumulative ingested/support notes now created after the 2026-04-11 second pass
These candidate papers now have source-backed or support-note pages in the wiki:
- [[resource-theories-quantum-reference]] — 1907.06306v2, 1510.03695v2, 1806.04937v3, 2111.12646v4
- [[distinguishability-formal-reference]] — 1907.06306v2 and 1510.03695v2
- [[topos-quantum-mechanics-reference]] — 1004.3561v1
- [[llm-bias-and-failure-modes-reference]] — 2409.11353v3, 2503.21676v2, 2402.11651v2, 2506.22486v1
- [[doubly-quantum-mechanics]] — 2412.05997v3
- [[quantum-shannon-theory-reference]] — quant-ph/0209124v3, 1511.06071v2, 1308.4283v3
- [[stochastic-thermodynamics-reference]] — 1810.05583v5, 1210.5071v1, 2309.13408v2
- [[viability-theory-reference]] — 2107.02684v2
- [[attractor-basins-formal-reference]] — 1907.08101v2, 2409.01079v1
- [[process-philosophy-and-relational-physics]] — quant-ph/9609002v2, 0712.4003v1
- [[fep-and-active-inference-reference]] — 1906.10184
- [[llm-constraint-harness-wiki]] — 2604.08545v1, 2207.05221v4, 2212.09251v1
- [[llm-ontology-smuggling-reference]] — 2212.03551v5
- [[stochastic-thermodynamics-reference]] — 1006.1420
- [[distinguishability-formal-reference]] — quant-ph/0406166v3, 1201.6554v2
- [[llm-ontology-smuggling-reference]] — 2020.acl-main.463
- [[llm-bias-and-failure-modes-reference]] — 2305.04388v2
- [[fiber-bundles-and-spin-geometry-reference]] — quant-ph/0310053v1, hep-th/0404165v5
- [[berry-phase-and-holonomy]] — hep-th/0404165v5
- [[hopf-fibration-mathematics]] — quant-ph/0310053v1
- [[evolutionary-models-qit-alignment]] — 0911.1383
- [[evolutionary-epistemology-reference]] — 1405.5563
- [[concurrency-and-trace-theory-reference]] — 2409.01079v1

## Related pages
- [[research-source-coverage-index]]
- [[current-research-overlays]]
- [[notebooklm-reference-pack-intake]]
- [[research-support-bibliography]]
- [[current-canonical-spine]]
