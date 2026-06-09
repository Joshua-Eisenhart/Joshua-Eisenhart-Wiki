---
title: LLM Ontology Smuggling Reference
created: 2026-04-09
updated: 2026-04-10
type: concept
tags: [reference, harness, language, formal, constraints]
sources:
  - Bender and Koller, Climbing Towards NLU: On Meaning, Form, and Understanding in the Age of Data (2020)
  - Shanahan, Talking About Large Language Models (2022)
  - Mitchell and Krakauer, The Debate Over Understanding in AI's Large Language Models (2023)
  - Milliere, Language Models as Models of Language (2023)
framing: current
---

# LLM Ontology Smuggling Reference

LLMs carry implicit ontological commitments from training data. When describing novel systems, they unconsciously inject these commitments — smuggling in assumptions the system does not make.

## The 7 Smuggling Patterns

### 1. Substance Smuggling

**What it is:** Assuming that the things being discussed are enduring substances with intrinsic properties.

**Example:** "A quantum state has definite values for all observables" — assumes substances with properties, which quantum mechanics denies.

**Why LLMs do it:** Training data overwhelmingly uses substance-grammar (SVO: subject-verb-object). "The electron has spin-up" is grammatically natural. "The measurement, when performed on the carrier, registers spin-up" is not.

**Counter:** Force process-grammar. Every sentence must name the operation/probe/measurement, not just the object.

### 2. Causal Smuggling

**What it is:** Assuming that events have causes in the efficient-cause sense (A pushes B to happen).

**Example:** "Decoherence causes quantum states to become classical" — assumes a causal mechanism driving the transition.

**Why LLMs do it:** Causal language is the default mode for explaining sequences. Training data rarely uses constraint-based or selection-based language.

**Counter:** Replace "causes" with "is excluded by" or "does not survive under." Constraint language, not causal language.

### 3. Universal Smuggling

**What it is:** Stating claims as universally true rather than context-bound.

**Example:** "Density matrices are positive semidefinite" — true, but only under the CPTP constraint. Under other constraints, different objects might appear.

**Why LLMs do it:** Universal statements are shorter, more confident-sounding, and more common in training data.

**Counter:** Always name the constraint set. "Under CPTP constraints, density matrices are positive semidefinite."

### 4. Teleological Smuggling

**What it is:** Assuming that processes have purposes or goals.

**Example:** "The constraint cascade aims to find irreducible families" — implies the cascade has a goal it works toward.

**Why LLMs do it:** Teleological language makes explanations feel satisfying. "X happens in order to achieve Y" is a natural narrative frame.

**Counter:** Describe the outcome without implying intention. "When all constraints are active, the surviving set has 28 members."

### 5. Essentialist Smuggling

**What it is:** Assuming that categories have essences — necessary and sufficient conditions that define them.

**Example:** "Entanglement is fundamentally about non-separability" — treats non-separability as the essence of entanglement rather than one test among many.

**Why LLMs do it:** Essentialist definitions are compact and feel authoritative. Training data is full of "X is essentially Y" constructions.

**Counter:** Describe operational tests, not essences. "States classified as entangled by PPT, concurrence, and negativity tests show the following behavior..."

### 6. Narrative Smuggling

**What it is:** Organizing information as a story with beginning, middle, and end rather than as a constraint structure.

**Example:** "First, the system starts in a pure state. Then, noise is applied. Finally, the system decoheres to a mixed state." — tells a story instead of describing constraint responses.

**Why LLMs do it:** Narrative is the dominant mode of training data. Stories are engaging and feel explanatory.

**Counter:** Describe constraint sets and surviving structures. "Under {preparation, noise, measurement} constraints, the admissible set is the set of mixed states reachable from pure states via CPTP maps."

### 7. Compression Smuggling

**What it is:** Summarizing details that are actually load-bearing.

**Example:** "The cascade reduces 53 legos to 28" — compresses 7 layers of constraint-specific killing into one sentence, losing all information about which constraints kill what.

**Why LLMs do it:** Compression is rewarded in training (concise answers score higher). But the details ARE the system.

**Counter:** When asked about the system, enumerate rather than summarize. Name specific constraints, specific families, specific results.

## How Smuggling Corrupts Research

### Corrupts Sim Interpretation

When an LLM describes sim results, it smuggles in:
- Causal framing ("the constraint killed this family")
- Essentialist framing ("this family is essentially a channel")
- Narrative framing ("first L3 enriches, then L4 selects")

The correct framing:
- Constraint framing ("this family does not survive when L4 is active")
- Operational framing ("this family passes PPT under L3 but not under L3+L4")
- Structural framing ("the admissible set under L3 contains N_f families; under L3+L4, it contains N_f - k")

### Corrupts Status Reporting

When an LLM reports status, it smuggles in:
- Universal claims ("all 28 families pass")
- Teleological framing ("the system is converging on the right answer")
- Compression ("everything works")

The correct framing:
- Context-bound claims ("28 families pass C1/C3/C4 under the Phase 7 test suite")
- Structural framing ("the surviving set under current constraints has 28 members")
- Enumerated ("family 1 passes, family 2 passes, ...")

### Corrupts Theory Construction

When an LLM proposes new theory, it smuggles in:
- Substance ontology (proposing new objects)
- Causal mechanisms (proposing how things "work")
- Essentialist definitions (proposing what things "really are")

The correct approach:
- Constraint ontology (proposing new constraints to test)
- Selection descriptions (proposing what would survive/exclude)
- Operational definitions (proposing new probes/tests)

## Connection to This System

### The System Is Explicitly Anti-Smuggling

- [[nominalist-translation-rules]] — operationalizes anti-smuggling as translation rules
- [[llm-bias-inversion-rules]] — specific inversions of each smuggling pattern
- [[enforcement-and-process-rules]] — Rule 8 (no Platonic language), Rule 12 (anti-salience)
- [[llm-controller-contract]] — status label constraints prevent compression smuggling

### Detection Method

Before accepting any LLM output about this system, check:
1. Does it name the constraint set? (catches universal smuggling)
2. Does it name the probe? (catches essentialist smuggling)
3. Does it use selection language? (catches causal smuggling)
4. Does it enumerate rather than summarize? (catches compression smuggling)
5. Does it describe processes, not substances? (catches substance smuggling)

## 2026-04-10 arXiv source addition

### 2212.03551v5 — Talking About Large Language Models
- Warns against anthropomorphizing LLMs and against casually importing human notions like "knows", "believes", and "thinks".
- Useful as a language-discipline support for avoiding ontology smuggling in AI descriptions.
- Best fit pages: [[llm-ontology-smuggling-reference]], [[llm-bias-and-failure-modes-reference]], [[research-support-bibliography]].

### 2020.acl-main.463 — Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data
- Argues that form-only training cannot by itself deliver meaning or human-analogous understanding.
- Useful as a guardrail against overreading language-model competence and conflating string prediction with meaning.
- Best fit pages: [[llm-ontology-smuggling-reference]], [[research-support-bibliography]], [[current-research-overlays]].

## Related Pages

- [[llm-bias-inversion-rules]] — the 6 mandatory inversions
- [[nominalist-translation-rules]] — the 7 translation rules
- [[llm-bias-and-failure-modes-reference]] — general LLM failure modes
- [[anti-reification-and-nominalism-reference]] — anti-reification philosophy
- [[process-and-systems-thinking-reference]] — process-over-object thinking
- [[operationalism-and-measurement-reference]] — probe-relative meaning
- [[research-support-bibliography]] — external support cluster

## Sources

- Bender, Koller. "Climbing Towards NLU: On Meaning, Form, and Understanding in the Age of Data." ACL 2020.
- Shanahan. "Talking About Large Language Models." arXiv:2212.03551, 2022.
- Mitchell, Krakauer. "The Debate Over Understanding in AI's Large Language Models." PNAS 120, e2215907120 (2023).
- Millière. "Language Models as Models of Language." (2023).
