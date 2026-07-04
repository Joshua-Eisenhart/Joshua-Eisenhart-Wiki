---
title: Leviathan to QIT Engine Glossary
created: 2026-04-11
updated: 2026-04-14
type: concept
framing: current
tags: [glossary, leviathan, qit, engines, constraints, translation]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/EXPLICIT_CONTROLLER_MODEL.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/ANOMALOUS_COMPUTER_SCIENCE_TRANSLATION.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/CONSTRAINT_ON_DISTINGUISHABILITY_FULL_MATH.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/LADDERS_FENCES_ADMISSION_REFERENCE.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/sim_backlog_matrix.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/controller_maintenance_checklist.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Leviathan to QIT Engine Glossary

## Overview
This page is the side-by-side term map for readers who already understand Leviathan-style constraint engineering but do not yet understand the QIT engine program.

Use it when the reader does not need the full explanation first and instead needs direct vocabulary conversion.

The goal is not to claim the two systems are identical.
The goal is to make the structural correspondences explicit enough that a systems/dev reader can follow what the QIT engine stack is trying to build.

## Quick orientation
Short bridge:
- Leviathan is constraint engineering for agent behavior and runtime governance.
- The QIT engine program is constraint engineering for information-state transformation and engine-cycle admissibility.

In both cases, the constraint regime comes first and downstream code or runtime behavior is treated as a projection of that regime.

## Side-by-side glossary

| Leviathan term | QIT engine term | What it means in this bridge |
|---|---|---|
| DNA contract | root constraints + admissibility rules | The declaration of what the system is allowed to count as a real object or lawful move before downstream implementation details matter. |
| gate / eval | probe / falsifier / boundary test | The mechanism that decides whether a candidate object, transform, or cycle is admitted, excluded, or still open. |
| harness | simulation + audit regime | The bounded execution and verification environment used to test whether candidate structures are actually lawful. |
| runtime graph | state/operator/topology structure | The active relational structure in which transforms, couplings, and cycle behavior are expressed. |
| workstream | bounded lego / packet / lane | A narrow constructive unit of work such as a local state family, geometry packet, operator family, or engine-readiness gate. |
| compile declaration into runtime | compile candidate into sim/result artifact | Turn a conceptual candidate into a bounded executable test plus a result artifact with explicit status. |
| artifact | result JSON / proof witness / audit row | The file-backed evidence surface that records what was actually observed in a bounded run. |
| ratchet | monotone promotion discipline | Stronger claims require stronger evidence; process labels should not be promoted from weaker labels automatically. |
| immutable receipt | result artifact + explicit truth label | The durable record of what was run, what passed, and what remains open. |
| loss function | admissibility / exclusion surface | The constraint surface that determines what the system learns to preserve and what it rejects. |
| adversarial hardening | stronger negatives and fence tests | Every exploit, proxy failure, or overclaim should produce a stronger falsifier or sharper exclusion test. |
| non-commutation | operator order / transform order | The sequence of transforms is load-bearing; A then B is not equivalent to B then A. |
| finitude | bounded state families / bounded probe sets / bounded cycles | All constructive work must respect finite carriers, finite probes, finite compute, and bounded claims. |
| session memory | maintenance surfaces and ledgers | Durable state is preserved in explicit queue, truth-audit, registry, and wiki surfaces rather than in informal narrative memory. |
| intent | engine-readiness target / bounded build move | The declared next constructive objective that the controller is trying to advance. |
| control plane | Hermes/controller lane | The layer that chooses the next bounded move, manages workers, verifies outputs, and updates continuity surfaces. |
| worker | bounded sim/probe execution surface | A subordinate execution path that can produce candidate artifacts but does not own truth labels. |
| lease / trust model | promotion gate / admissibility gate | Stronger capability or stronger claims must be earned through demonstrated bounded compliance, not assumed by default. |

## Translation notes
### 1. DNA is not code, and admissibility is not code
The strongest shared idea is that the source of truth is upstream of implementation.

In Leviathan language:
- the DNA is the authoritative contract

In QIT-engine language:
- admissibility rules are the authoritative contract for state objects, transforms, and cycles

The code is downstream in both cases.

### 2. Gates and probes play the same structural role
Leviathan uses gates to decide what is accepted.
The QIT engine stack uses probes, falsifiers, and boundary tests to decide what structures are actually lawful.

That does not make them numerically identical, but it makes them functionally comparable.

### 3. Ratchet and promotion discipline are directly comparable
Leviathan’s ratchet language maps well onto the QIT engine stack’s insistence that stronger labels require stronger evidence.

In the QIT stack, a file should not become stronger just because:
- it exists
- it runs
- it produced one interesting output

Promotion has to be earned through bounded reruns, tool-honest evidence, and explicit process compliance.

### 4. Finitude and non-commutation are not just philosophy here
They map directly into the engine program:
- finitude -> bounded state spaces, bounded probe sets, bounded packets, bounded claims
- non-commutation -> operator order matters, cycle order matters, composition order matters

These are not decorative metaphors. They are part of the execution semantics.

### 5. Why entropy is not the same as a score
A dev reader may be tempted to treat entropy as the equivalent of one scalar eval metric.
That is too weak.

In this system:
- entropy is a readout
- distinguishability and admissibility are deeper than the readout

A cycle is not valid just because some aggregate quantity looks good.
The structure has to remain lawful under probes, transforms, and composition.

## Minimal sendable bridge
If you need one compact sentence:

What Leviathan does for agent behavior with DNA, gates, and ratchets, the QIT engine program does for information-state transformation with admissibility rules, probes, and cycle-level constraints.

## Related pages
- [[qit-engine-dev-technical-brief]]
- [[qit-engine-constraint-engineering-bridge]]
- [[codex-ratchet-cs-bounded-system-framing]]
- [[qit-basin-engine-synthesis]]
- [[qit-engine-geometry-entropy-bridge]]
- [[constraint-on-distinguishability]]
- [[formal-constraints-and-geometry]]
- [[nominalist-cs-framing]]
