---
title: Nominalist CS Framing
created: 2026-04-11
updated: 2026-04-14
type: concept
tags: [concept, system, architecture, implementation, constraints, harness, language]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/NOMINALISM_IN_THIS_SYSTEM.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/ANOMALOUS_COMPUTER_SCIENCE_TRANSLATION.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/EXPLICIT_CONTROLLER_MODEL.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md
framing: current
---

# Nominalist CS Framing

## Purpose
This page gives the implementation-native rendering of the system for LLMs and developers. It is the compact correction for the default misread: the project is not mainly a theory ontology, worldview essay, or geometry-first metaphysics. It is a bounded constraint-and-probe system that only earns identities, statuses, and higher-level objects through admissible operations.

## Role in the live wiki cluster
- Strongest use: shortest current page for translating repo-native language into controller/state-machine language without losing the nominalist discipline.
- Weak use: full runtime architecture, queue authority, or doctrine genealogy.
- Authority boundary: this page is a translation layer. Operational truth still comes from `system_v5/docs/EXPLICIT_CONTROLLER_MODEL.md`, `system_v5/docs/LLM_CONTROLLER_CONTRACT.md`, and the live `system_v5/docs/plans/` surfaces.

## Why default LLM/software priors misread the project
Default model and software habits import the wrong primitives:

- identity-first: assumes stable objects exist before probes
- summary-first: treats compression as understanding
- construction-first: proposes entities before naming exclusion rules
- geometry-import: treats manifolds, shells, and carriers as primitive givens rather than admissible later renderings
- entropy-primacy: treats entropy/information as the base substance instead of downstream bookkeeping
- bridge inflation: jumps from local object talk to global doctrine claims

In repo terms, those habits collapse `candidate`, `lego`, `probe`, `artifact`, `registry row`, and `canonical` into one vague thing. [[llm-ontology-smuggling-reference]] and [[llm-controller-contract]] already document the resulting overclaim pattern.

## The nominalist implementation rule
Render the system in this order:

1. active constraints
2. admissible probes
3. exclusion conditions
4. surviving local objects
5. evidence artifacts
6. status labels
7. only then higher-order summaries or bridge language

That order matches the repo's controller discipline better than any philosophy-first summary. The system should be read as a state-transition harness over bounded candidates, not as a library of pre-existing essences.

## Compact CS translation table

| Repo-native term | Nominalist-CS rendering | Why it matters |
|---|---|---|
| lego | primitive typed unit under a bounded probe target | keeps work local instead of theory-inflated |
| candidate | provisional object | prevents premature identity claims |
| probe / sim | executable verification function | ties claims to runs rather than summaries |
| result artifact | machine output record | keeps evidence path-specific |
| truth label | verification state | separates `exists`, `runs`, `passes local rerun`, and `canonical by process` |
| maintenance surface | derived state view | forces ledgers/wiki/docs to follow evidence changes |

## Core replacements
### 1. No primitive identity
A "thing" in this system is not primitive. Identity is probe-relative distinguishability under a finite admissible family. In implementation terms: an object is whatever remains stably nameable after a bounded probe suite fails to split it further.

Bad render: "the shell/object/family is X"
Good render: "under probe family M and current constraints, this candidate is treated as one object for the next transition"

### 2. Constraints before summaries
The first useful question is not "what is it?" but "what constraints and probes are in force?" The repo's controller contract, lego contract, and explicit controller model are all constraint-first admission systems.

Implementation translation:
- constraints define allowed transitions
- probes define observable distinctions
- summaries are derived views over prior evidence

### 3. Exclusion before construction
The graveyard is not secondary. Kills, blockers, negatives, and non-admitted states carry more implementation information than survivor prose. A valid page or controller action should name what would exclude the claim, not only what the claim says.

Implementation translation:
- negative suites are part of object definition
- promotion is earned by surviving named kill conditions
- registries project exclusion history, not just survivor labels

### 4. Anti-geometry-import
Geometry is not the primitive source code of the system. Geometry is one admissible rendering that becomes available after the root constraint layer and local object layer are fixed. Importing geometry too early smuggles ontology and makes the system look like a manifold-discovery project instead of a probe-disciplined build process.

Implementation translation:
- carrier/geometry layers are fields on a sim contract, not self-justifying foundations
- topology or shell language must stay subordinate to probe/evidence status
- geometry claims without local executable support remain candidate language

### 5. Anti-entropy-primacy
Entropy is not the base object. It is a later metric, bookkeeping surface, or derived discriminator over already-admitted structures. Treating entropy as primitive causes the system to be misread as an optimization or thermodynamic monism engine.

Implementation translation:
- entropy labels should come after object admission
- information measures describe states of a run, not the source of object identity
- the controller should never use entropy rhetoric to skip evidence gates

## Implementation-native rendering
For developer use, the safest compact rendering is:

Codex Ratchet is a bounded research-object compiler and verification harness whose basic unit is a candidate under constraints, not an entity with primitive identity.

Its operational lifecycle is:

`source fragment -> normalized candidate -> bounded probe -> exclusion/survival artifact -> status label -> registry projection -> possible successor`

The important nominalist point is where identity enters: not at source ingestion, but only after the probe/exclusion stage gives a stable enough quotient for current work.

## What pages and agents should say instead
Prefer these implementation-native forms:

- not "X exists"
  but "path P exists" or "candidate X has status `exists`"
- not "this proves X"
  but "probe Y emitted artifact Z and did not exclude claim C under named criteria"
- not "the system is a geometry"
  but "the system currently renders one receipt-scoped candidate/survivor slice in geometry terms"
- not "entropy drives the process"
  but "entropy is one measurement family over the named receipt-scoped slice"
- not "this object is canonical"
  but "this candidate reached `canonical by process` under the controller contract"

## Repo-current anchors
This framing is now explicit across the repo-current docs:

- `system_v5/docs/ANOMALOUS_COMPUTER_SCIENCE_TRANSLATION.md` treats the system as compiler + harness + registry updater
- `system_v5/docs/EXPLICIT_CONTROLLER_MODEL.md` defines progress as bounded object transitions, not theory understanding
- `system_v5/docs/LLM_CONTROLLER_CONTRACT.md` separates status labels and blocks summary inflation
- `system_v5/docs/LEGO_SIM_CONTRACT.md` requires explicit negatives, artifacts, and promotion blockers
- `system_v5/docs/NOMINALISM_IN_THIS_SYSTEM.md` carries the deeper derivation from `a=a iff a~b`

This page's contribution is to unify those operational rules with the nominalist claim: no primitive identity, no ontology smuggling, probe-relative identity, exclusion-first construction.

## Practical writing rule for the wiki
When a page is about live system behavior, prefer this sentence order:

1. name the constraint set
2. name the probe or execution surface
3. name the exclusion or failure conditions
4. name the current surviving object/status
5. only then give a summary sentence

If a summary cannot be expanded back into those four items, it is probably smuggling ontology or compressing away load-bearing structure.

## Recommended reading order
- [[nominalism-in-this-system]] — deeper derivation and anti-reification basis
- [[nominalist-cs-framing]] — this page, for the shortest implementation-native rendering
- [[codex-ratchet-cs-bounded-system-framing]] — live controller/queue/memory-surface translation
- [[controller-state-transition-model]] — exact runtime object-transition model
- [[qit-engine-dev-framing]] — compact downstream dev-facing handoff for the QIT engine lane

## Related pages
- [[nominalism-in-this-system]]
- [[nominalist-framing]]
- [[nominalist-cs-cluster]]
- [[codex-ratchet-cs-bounded-system-framing]]
- [[controller-state-transition-model]]
- [[llm-ontology-smuggling-reference]]
- [[translation-methodology-reference]]
- [[llm-controller-contract]]
- [[lego-sim-contract]]
- [[current-architecture-core]]
- [[nominalist-cs-jp-systems-bridge]]
