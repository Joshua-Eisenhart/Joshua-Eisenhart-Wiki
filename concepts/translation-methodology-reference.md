---
title: Translation Methodology Reference
created: 2026-04-09
updated: 2026-04-10
type: concept
tags: [reference, harness, language, formal, constraints]
sources:
  - Quine, Word and Object (1960)
  - Davidson, Inquiries into Truth and Interpretation (1984)
  - Goodman, Ways of Worldmaking (1978)
  - Putnam, The Many Faces of Realism (1987)
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Translation Methodology Reference

How to restate the same claim across multiple framings. Not paraphrase — structured translation that preserves the constraint content while changing the ontological commitment.

## The 4 Framings

### 1. Ordinary Language

Default framing. Uses standard grammar, substance-verb-object construction, common vocabulary.

**Use when:** communicating with humans who do not share the system's framing.
**Risk:** carries all 7 smuggling patterns from [[llm-ontology-smuggling-reference]].

### 2. Nominalist Framing

Anti-reification. Replaces objects with survivors, essences with probe-relatives, causation with constraint coupling.

**Use when:** the claim needs to be checked against the system's ontology.
**Rules:** [[nominalist-translation-rules]] (7 mandatory rules).

### 3. Systems/Process Framing

Relational-first. Replaces components with interactions, states with frozen processes, properties with patterns across measurements.

**Use when:** the claim involves coupling, emergence, or multi-shell structure.
**Rules:** [[process-and-systems-thinking-reference]] (process-first, interaction-first, state-as-frozen-process).

### 4. Executable/Probe Framing

Operational. Replaces every concept with its probe file, result JSON, and test condition.

**Use when:** the claim needs to be tied to actual evidence.
**Rules:** name the probe, the result file, and the test that would falsify the claim.

## Translation Procedure

Given a claim in any framing:

### Step 1: Extract the Constraint Content

What constraint set, probe, and context does the claim depend on?

**Example:** "Entanglement is a resource for quantum computation."
- Constraint content: states that survive LOCC-separability tests can be used in certain computational protocols.

### Step 2: Restate in Each Framing

**Ordinary:** "Entanglement helps quantum computers do things classical computers can't."
**Nominalist:** "States that do not survive the separability test under LOCC are admitted as input to protocols that classical states cannot execute."
**Systems:** "The interaction between non-separable states and quantum gates produces computational patterns that the separable-state interaction does not."
**Executable:** "Running sim_concurrence_measure.py on state ρ gives C > 0. Running sim_vqe_ratchet.py with ρ as input produces results that sim_vqe_ratchet.py with separable input does not."

### Step 3: Check for Consistency

The 4 framings must be compatible. If they disagree, the claim is underspecified.

**Red flag:** If the ordinary-language version sounds confident but the executable version is vague, the claim is not grounded.

### Step 4: Flag Residue

Some content may not translate cleanly across all 4 framings. That residue is either:
- Load-bearing (the claim depends on a specific framing's commitments) → mark it
- Smuggling (the claim depends on an assumption that doesn't survive translation) → reject it

## The Inversion Test

Take any claim and invert it. If the inversion is equally plausible, the original claim carried unexamined assumptions.

**Claim:** "The constraint cascade reduces the number of families."
**Inversion:** "The constraint cascade reveals that fewer families were ever present than appeared to be."

Both are valid descriptions. The difference: "reduces" implies the families existed before and were destroyed. "Reveals" implies they were never really separate. The system's framing is closer to "reveals" (selection, not destruction).

## Connection to This System

### The Wiki IS the Translation Layer

[[wiki-as-harness-architecture]] Layer 3 is the translation stack. This page describes how that layer works.

The wiki stores claims in all 4 framings simultaneously:
- The concept pages (ordinary + nominalist)
- The translation rules (how to convert)
- The probe bridge (executable grounding)
- The gap audit (where translations break down)

### Translation Prevents Drift

When an LLM starts in ordinary language and drifts toward smuggling, the translation rules provide the correction path:
1. Take the smuggled claim
2. Translate to nominalist → strips reification
3. Translate to systems → strips substance ontology
4. Translate to executable → strips vagueness
5. If the claim survives all 4 translations, it is grounded

## Key Results

1. **Quine's indeterminacy of translation:** there is no unique "correct" translation between languages. Applied: multiple framings of the same claim are legitimate as long as they are constraint-compatible.
2. **Davidson's principle of charity:** interpret speakers as mostly rational and mostly right. Applied: when translating LLM output, assume the model is trying to say something true — the smuggling is in the framing, not the intent.
3. **Operational equivalence:** two concepts are operationally equivalent iff they produce the same predictions under all tests. Applied: two framings are equivalent iff they generate the same probe results.

## Related Pages

- [[nominalist-translation-rules]] — Rule 1-7 for nominalist restatement
- [[llm-bias-inversion-rules]] — inversion rules for each bias
- [[llm-ontology-smuggling-reference]] — the 7 smuggling patterns
- [[wiki-as-harness-architecture]] — how the wiki drives saliency
- [[operationalism-and-measurement-reference]] — probe-relative grounding
- [[process-and-systems-thinking-reference]] — systems framing
- [[research-support-bibliography]] — external support cluster
- [[anti-reification-and-nominalism-reference]] — nominalist philosophy

## Sources

- Quine. "Word and Object." MIT Press, 1960.
- Davidson. "Inquiries into Truth and Interpretation." Oxford University Press, 1984.
- Goodman. "Ways of Worldmaking." Hackett, 1978.
- Putnam. "The Many Faces of Realism." Open Court, 1987.
