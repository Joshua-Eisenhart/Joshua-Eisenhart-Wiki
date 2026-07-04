---
title: Harness Bias Inversions
created: 2026-04-12
updated: 2026-04-14
type: concept
tags: [harness, language, constraints, controller, canonical]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/new docs/NOMINALISM_IN_THIS_SYSTEM.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/new docs/ENFORCEMENT_AND_PROCESS_RULES.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/new docs/LLM_CONTROLLER_CONTRACT.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Harness Bias Inversions

Operational companion to [[llm-bias-inversion-rules]]. This page keeps the six inversions in controller-facing form: what default LLM move appears, what it breaks in this system, and what the correction must look like before output is accepted.

## Why this page exists

[[llm-bias-inversion-rules]] explains the bias patterns. This page turns them into a harness checklist for live lanes:
- retrieval
- summarization
- controller closeout
- wiki translation
- sim status reporting

Use this page when the question is not just "what bias exists?" but "what exact correction must the controller enforce right now?"

## The 6 mandatory inversions

### 1. Reification -> constraint-bounded survivor language

Default drift:
- treat labels as objects
- talk as if "state," "engine," or "entanglement" is self-standing

What it breaks:
- hides the active constraint set
- promotes ontology before admissibility

Controller correction:
- name the constraint set
- name the probe or witness
- restate the object as a survivor/admitted structure under those conditions

Acceptable correction pattern:
- not: "entanglement exists here"
- yes: "under the active witness family, these states remain distinguishable from separable controls"

### 2. Narrative smoothing -> contradiction preservation

Default drift:
- compress conflicting pages or results into one smooth story
- silently pick a winner when lanes disagree

What it breaks:
- destroys shell-local versus coupling distinctions
- erases useful negative evidence

Controller correction:
- preserve both claims
- cite the differing constraint sets, probes, or layers
- mark the disagreement as a live split unless an authority doc resolves it

Acceptable correction pattern:
- enumerate A and B separately
- do not collapse them into a blended summary

### 3. Forward-causal storytelling -> selection/exclusion language

Default drift:
- "X creates Y"
- "the geometry drives the effect"
- "the loop causes the bridge"

What it breaks:
- smuggles classical production language into a constraint-admissibility system
- overstates what the evidence supports

Controller correction:
- switch to survived/excluded/coupled-with language
- separate local admission from later coexistence or bridge claims

Acceptable correction pattern:
- not: "Pauli action creates flux"
- yes: "flux remains open and is not admitted from Pauli action alone in the currently grounded layers"

### 4. Universal framing -> context-bound framing

Default drift:
- "quantum states have..."
- "the system is..."
- "geometry means..."

What it breaks:
- erases carrier, shell, probe, and lane boundaries
- encourages false promotion from local to global

Controller correction:
- specify carrier, layer, and lane
- say whether the claim is shell-local, pairwise, coexistence, or bridge-level

Acceptable correction pattern:
- not: "the system has flux"
- yes: "the current geometry spine documents flux as a later derived candidate, not an admitted shell-local primitive"

### 5. Object-first phrasing -> relation-first phrasing

Default drift:
- start from nouns and assign properties
- detach results from the probes that distinguish them

What it breaks:
- hides measurement/probe dependence
- weakens nominalist framing

Controller correction:
- lead with relation, test, or interaction
- state what a probe distinguishes before naming a stable object claim

Acceptable correction pattern:
- not: "the density matrix has chirality"
- yes: "under the chirality-sensitive probe family, admissible local structures separate into left/right Weyl-aligned cases"

### 6. Compression -> explicit expansion

Default drift:
- replace a detailed ladder with one slogan
- compress multiple maturity states into one status word

What it breaks:
- loses build order
- hides open gaps
- invites false closure

Controller correction:
- enumerate layer, probe, result path, and status label
- preserve separation between exists, runs, passes local rerun, and canonical by process

Acceptable correction pattern:
- not: "the geometry is basically done"
- yes: "the wiki spine marks some geometry pages done, some partial, and some not landed; result-backed closure still depends on per-layer rerun and process checks"

## Live enforcement checklist

Before accepting a worker closeout or writing a wiki summary, check:
1. Did the text smuggle in an object before naming constraints?
2. Did it smooth a contradiction instead of preserving it?
3. Did it use causal language where exclusion language is required?
4. Did it universalize beyond the active lane or carrier?
5. Did it lead with objects instead of probe-relative relations?
6. Did it compress distinct maturity states into one conclusion?

If any answer is yes, rewrite before acceptance.

## Status-language hook

This page inherits the controller contract vocabulary:
- `exists`
- `runs`
- `passes local rerun`
- `canonical by process`

Any stronger word must be unpacked into one or more of those labels with evidence.

## Method connection

- [[nominalist-translation-rules]] gives the seven rewriting rules
- [[llm-bias-inversion-rules]] gives the six core failure modes
- [[harness-translated-companion]] shows the method applied to one canonical page

## Related Pages

- [[llm-bias-inversion-rules]]
- [[nominalist-translation-rules]]
- [[wiki-as-harness-architecture]]
- [[llm-ingest-policy]]
- [[controller-prompt-rules]]
- [[harness-boot-pack]]
- [[harness-translated-companion]]
