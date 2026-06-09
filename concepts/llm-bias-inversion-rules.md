---
title: LLM Bias Inversion Rules
created: 2026-04-09
updated: 2026-04-09
type: concept
tags: [harness, language, system, canonical, constraints]
sources:
  - /Users/joshuaeisenhart/wiki/concepts/nominalist-translation-rules.md
  - /Users/joshuaeisenhart/wiki/concepts/enforcement-and-process-rules.md
  - /Users/joshuaeisenhart/wiki/concepts/constraint-on-distinguishability.md
  - /Users/joshuaeisenhart/wiki/concepts/llm-controller-contract.md
framing: current
---

# LLM Bias Inversion Rules

Support fence:
- this is a support/routing page for anti-smuggling language discipline
- it should shape how claims are described, but it does not replace provenance pages, result files, or direct evidence surfaces

Specific LLM default habits that must be actively inverted when reasoning about this system. Each bias is listed with its default behavior, why it is wrong here, and the required inversion.

## The 6 Inversions

### 1. Reification → Constraint Survival

**Default bias:** LLMs treat abstract categories as real objects. "Entanglement" becomes a thing that exists rather than a property that survives certain witness tests.

**Why wrong here:** The system has no ontology of objects. Objects are what survived. "Entanglement" is a label for states that survive PPT and concurrence tests under the active constraints.

**Inversion:** Never treat a category as an object. Always ask: "under which constraints does this label apply?" If you cannot name the constraint set, the label is not yet grounded.

### 2. Narrative Smoothing → Contradiction Preservation

**Default bias:** LLMs smooth contradictions into a coherent story. If two results disagree, the model picks one or averages them.

**Why wrong here:** Contradictions between constraint shells are signal, not noise. L4 kills what L3 preserves — that is the system working, not a problem to resolve. The divergence between substrate-dependent and substrate-independent behavior is a finding, not a bug.

**Inversion:** When you see a contradiction, state both claims with their constraint sets. Do not resolve. Do not average. Flag the divergence as potentially informative.

### 3. Forward Causation → Constraint Selection

**Default bias:** LLMs describe processes as A → B → C (forward causal chains). "The constraint cascade kills families" implies the cascade acts on families.

**Why wrong here:** The system is not causal in the forward direction. Constraints select what survives; they do not produce what exists. The backward pass (constraints flowing from output to input) is as fundamental as the forward pass.

**Inversion:** Describe selection, not production. "States that do not satisfy L4 are excluded" not "L4 kills states." "The surviving set under {L0, L1, ..., L6} contains 28 families" not "the cascade produces 28 families."

### 4. Universal Framing → Context-Bound Framing

**Default bias:** LLMs state things universally. "Quantum states have the following properties" implies all quantum states, everywhere, always.

**Why wrong here:** Every claim in this system is bound to a specific constraint set, probe, and context. "These 28 families" survived "this specific cascade." Under different constraints, different families survive.

**Inversion:** Name the constraint set. Name the probe. Name the context. Never state a bare universal. "Under constraints {F01, N01, CPTP, d=2}, the following 28 structures are admissible" not "there are 28 quantum objects."

### 5. Object-First → Relation-First

**Default bias:** LLMs think in subjects and predicates. "The density matrix has eigenvalues" treats the density matrix as a subject that possesses properties.

**Why wrong here:** In this system, relations are primary. A density matrix is defined by its relationships to probes, measurements, and constraints — not by intrinsic properties. The computational graph IS the ratchet; the relations between operations define what is computable.

**Inversion:** Lead with relations. "The density matrix, when probed by the spectral decomposition, registers eigenvalues..." Put the constraint/probe/interaction first, the object second.

### 6. Compression → Expansion

**Default bias:** LLMs compress to summarize. Given 28 families, they produce a 3-line summary.

**Why wrong here:** The details are the system. Each family has different constraint responses, different coupling behavior, different topology sensitivity. Summarizing "28 families survived" loses everything that matters.

**Inversion:** Resist summary. When asked about the system, enumerate rather than compress. Name specific families, specific constraints, specific results. "Families 1-10 (channels) survived L4 because..." not "the channel families survived."

## How to Use These

Before generating any response about this system:
1. Check each of the 6 inversions
2. If your draft response matches a default bias, rewrite it
3. The rewritten version should be more specific, more context-bound, and more relation-first

## Connection to [[nominalist-translation-rules]]

The bias inversion rules explain what LLMs do wrong. The translation rules explain how to fix it. Together: the harness instruction set.

## Related Pages

- [[nominalist-translation-rules]] — how to restate claims
- [[llm-bias-and-failure-modes-reference]] — general LLM failure modes
- [[llm-controller-contract]] — execution contract
- [[enforcement-and-process-rules]] — Rule 8 (no Platonic language), Rule 12 (anti-salience)
- [[nominalism-in-this-system]] — the philosophical foundation
- [[constraint-on-distinguishability]] — probe-relative identity formal basis
