---
title: Distinguishability Formal Reference
created: 2026-04-07
updated: 2026-04-10
type: summary
tags: [reference, research, validation]
sources:
  - raw/articles/new-docs/references/DISTINGUISHABILITY_FORMAL_REFERENCE.md
  - /Users/joshuaeisenhart/wiki/raw/papers/open_access/meta/webui_deepresearch_candidate_sources_2026_04_10.json
  - https://arxiv.org/abs/1907.06306v2
  - https://arxiv.org/abs/1510.03695v2
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Distinguishability: Formal Reference

## Overview
The MOST SYSTEM-CRITICAL reference doc because "constraint on distinguishability" is the system's primitive substance. This is the actual mathematics across QIT, statistics, information geometry, resource theory, and philosophy — not the system's application of it.

## Trace Distance (Quantum Distinguishability Metric)

T(ρ, σ) = (1/2) ||ρ - σ||₁. Ranges from 0 (identical) to 1 (orthogonal). Operational meaning (Helstrom-Holevo theorem): given equal priors, maximum probability of correctly distinguishing ρ from σ in one shot = (1/2)(1 + T). Trace distance IS optimal discrimination advantage. Variational form: T(ρ,σ) = sup_{0 ≤ P ≤ I} Tr[P(ρ - σ)].

## Fidelity

F(ρ, σ) = (Tr[√(√ρ σ √ρ)])². For pure states: F = |⟨ψ|φ⟩|². High fidelity = hard to distinguish. Fuchs-van de Graaf inequalities: 1 - √F ≤ T ≤ √(1 - F).

## Holevo Bound

For ensemble {pᵢ, ρᵢ} encoding classical variable X: I_acc(X:Y) ≤ χ = S(Σᵢ pᵢρᵢ) - Σᵢ pᵢS(ρᵢ). χ = maximum classical information extractable per quantum system. HSW theorem: χ is the asymptotically achievable classical capacity.

## Operational Equivalence (Spekkens)

Two preparations P1, P2 are operationally equivalent if no experiment distinguishes them: p(k|P1,M) = p(k|P2,M) for all M and k. Spekkens (2005): operationally indistinguishable preparations can still require different underlying ontic assignments, so operational equivalence is not the same thing as ontological identity. Harrigan-Spekkens classification: ψ-ontic (quantum states distinguishable at ontic level) vs ψ-epistemic (quantum indistinguishability reflects genuine ontic overlap). PBR-style arguments only constrain ψ-epistemic overlap under additional assumptions such as independent state preparation; they should not be retold as unconditional ontology proofs.

## Indistinguishability Relations and Quotient Structures

S/~_M = effectively distinct states given measurement M. Examples: topology (homeomorphism under continuous probes), algebra (isomorphism under homomorphisms), quantum (density matrices = quotient under all POVM measurements), thermodynamics (macrostates = quotient under macroscopic observables). Refinement ordering: more probes (M1 ⊂ M2) → finer equivalence classes. The density matrix is best treated here as an operational state specification / quotient at the chosen probe resolution. Infinitely many pure-state decompositions can realize the same density matrix, and no POVM on the system alone separates those ensembles.

## Coarse-Graining and Information Loss

Coarse-graining = surjective map φ: X_fine → X_coarse. Under renormalization group flow: statistical manifold contracts in irrelevant directions, distances along relevant directions preserved exactly. Information-theoretic derivation of universality: coarse-graining kills fine-grained distinctions, leaving only universality classes. Entropy increase: S(φ(ρ)) ≥ S(ρ). Second law = coarse-graining statement — entropy increases because macroscopic observables cannot track microscopic distinctions.

## Data Processing Inequality (DPI)

Classical: I(X;Z) ≤ I(X;Y) for Markov chain. Quantum: D(N(ρ) || N(σ)) ≤ D(ρ || σ) for CPTP map. T(N(ρ), N(σ)) ≤ T(ρ, σ): physical evolution can only make states HARDER to distinguish, never easier. The DPI guarantees quotient structures under coarse-graining are STABLE — once distinctions are lost, they stay lost. This is the formal backbone.

## Blackwell Order

Experiment σ Blackwell-dominates σ' iff any of three equivalent conditions hold: utility dominance, garbling (σ' is a noisy version of σ), strategy inclusion. Blackwell's theorem (1951, 1953): these are equivalent. The Blackwell order is a PARTIAL order — two experiments can be incomparable. A more informative experiment better distinguishes between states of the world.

## Fisher Information and Cramér-Rao

I(θ) = E_θ[(∂/∂θ log p(X|θ))²]. Cramér-Rao: Var_θ(T) ≥ 1/I(θ). Fisher information defines Riemannian metric on statistical manifold: high Fisher info = nearby parameter values produce very DIFFERENT distributions. Čencov (1982): Fisher-Rao metric is (up to constant) the UNIQUE Riemannian metric invariant under sufficient statistics. The geometry of distinguishability is canonical. QFI = 4 × Bures metric.

## Resource Theory of Distinguishability

Asymmetric (Wang & Wilde, 2019): objects are pairs (ρ, σ), free operations = quantum channels applied identically to both, asymptotic conversion rate = ratio of relative entropies. Symmetric (Salzmann et al., 2021): classical-quantum sources, conversion rate = ratio of quantum Chernoff divergences. Takagi & Regula (2019): for ANY resource theory, discrimination advantages form a complete family of monotones. State ρ convertible to σ by free operations iff ρ outperforms σ in every discrimination task.

## Identity from Distinguishability (Leibniz PII)

∀x,y: (∀P: P(x) ↔ P(y)) → x = y. Quantum challenge: electrons in singlet share all intrinsic properties. Weak discernibility (Saunders): fermions satisfy irreflexive relation "has opposite spin to" without distinct monadic properties. Formal takeaway: identity is not primitive — it is derived from distinguishability. What counts as "same" depends on probe resolution. The density matrix quotient IS this: states identified when no POVM separates them. DPI guarantees stability: if indistinguishable now, no processing will separate them. Identity is relational, resolution-dependent, probe-relative.

## 2026-04-10 intake upgrades (audited WebUI return)
These additions are queued as candidate citations and wording fences, not as downloaded theorem surfaces.

- Best next citation adds for this lane: Hughston-Jozsa-Wootters on ensemble non-uniqueness, Fuchs-van de Graaf on fidelity / trace-distance bounds, Abramsky-Brandenburger on contextuality as a global-section obstruction, Heunen-Landsman-Spitters on topos-style context dependence, and Torgersen / Audenaert for experiment comparison and quantum Chernoff discrimination.
- Strong wording fence from the audited return: `S/~_M` is the operational state space at probe resolution `M`; any ontological reading requires extra assumptions beyond operational equivalence.
- Keep the bridge split explicit: contextuality and topos/context language are support for context-indexed valuation and incompatibility, not automatic proof of a relation-first ontology.

## 2026-04-10 arXiv source additions

### 1907.06306v2 — Resource theory of asymmetric distinguishability for quantum channels
- Pushes distinguishability from states to channels.
- Makes the channel box the object of comparison.
- Gives operational meaning to asymmetry, distillation, and dilution in channel conversion.
- Best use here: a direct support paper for the resource-theory side of distinguishability.

### 1510.03695v2 — Relative submajorization and its use in quantum resource theories
- Gives a convertibility relation that is finer than plain majorization.
- Links resource comparison to Lorenz curves and linear-programming duality.
- Useful for approximate conversion and reversibility bounds.
- Best use here: a direct support paper for geometric comparison and operational convertibility.

### quant-ph/0406166v3 — Contextuality for preparations, transformations and unsharp measurements
- Generalizes contextuality to operational equivalence classes across preparations, measurements, and transformations.
- Useful for keeping probe-relative identity distinct from ontological identity and for the context-dependence of allowed comparisons.
- Best fit pages: [[distinguishability-formal-reference]], [[constraint-on-distinguishability-formal-reference]], [[qit-vocabulary-discipline-reference]].

### 1201.6554v2 — Distinct Quantum States Can Be Compatible with a Single State of Reality
- Shows that multiple quantum states can overlap on a single underlying state unless extra assumptions are added.
- Useful as a guardrail against turning operational equivalence into an automatic ontology claim.
- Best fit pages: [[distinguishability-formal-reference]], [[nominalism-in-this-system]], [[current-research-overlays]].

### Fit to the wiki
- These papers strengthen the claim that distinguishability is an operational ordering, not just a similarity metric.
- They support [[resource-theories-quantum-reference]] and [[constraint-on-distinguishability-full-math]].
- They do not collapse probe-relative identity into a single scalar metric; they add operational structure around it.

## Cross-Cutting Spine

Trace distance/Fidelity -> Operational equivalence -> Quotient structures -> Coarse-graining -> DPI -> Blackwell order -> Neyman-Pearson -> Fisher information -> Resource theory -> Leibniz PII. The DPI is the linchpin.

## Fit for this wiki
Best fit:
- the system's "a=a iff a~b" style probe-relative identity claims
- admissibility fences that depend on what survives the allowed probe family
- comparing candidate carriers by how much they can still distinguish after processing

Mismatch:
- the page is not a proof of the system's ontology
- distinguishability does not automatically settle geometry, algebra, or dynamics
- identity here is relational and resolution-dependent, not a blanket metaphysical identity claim

## How it connects
This is the formal backbone behind [[nominalism-in-this-system]] (a=a iff a~b) and [[constraint-on-distinguishability]]. See [[information-geometry-reference]] for the geometric version and [[quantum-fisher-information-geometry]] for the quantum Fisher info.
It is now also cross-supported by the 2026-04-10 arXiv additions on asymmetric distinguishability and relative submajorization.

## Open questions
- Whether quantum metric non-uniqueness (Petz: infinitely many monotone metrics) matters for the system's specific geometry.
- Which probe families should be treated as canonical witnesses versus merely supportive measurements.
