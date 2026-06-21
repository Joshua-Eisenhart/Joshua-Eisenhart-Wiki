---
title: Attractor Basin Digger
created: 2026-06-21
updated: 2026-06-21
type: concept
status: current-research-overlay
claim_ceiling: concept/design term; classifier proposal only
tags: [attractor-basin-digger, research-ratchet, basin, project-harness, drift]
---

# Attractor Basin Digger

## Definition

**Attractor Basin Digger** is the Research Ratchet subsystem that decides whether a proposed next move preserves and deepens the active project basin.

It protects against the failure mode where the model remembers related facts but loses the object, frontier, claim ceiling, or live gates.

## Output classes

```text
basin_deepening
basin_leakage
basin_split
basin_kill
insufficient_evidence
```

## Inputs

- current object id;
- current frontier;
- claim ceiling;
- SpinorMemoryCell set;
- operator trace;
- receipt lineage;
- graveyard list;
- source refs;
- proposed GraphPatchProposal.

## Questions

```text
What object are we inside?
What invariant basis must be conserved?
Which moves are forbidden?
Which leakage paths are live?
Which branch splits are real?
Which dead branches are being repeated?
What next gate deepens the basin?
```

## Relationship to sims

Codex sims become basin probes when they test:

- escape/leakage edges;
- basin boundaries;
- order-sensitive constraint application;
- quotient erasures;
- killed simpler explanations;
- survivorship under ratcheted constraints.

See also:

- [[concepts/spinor-memory]]
- [[projects/research-ratchet/spinor-memory-and-attractor-basin-digger-2026-06-21]]
- [[projects/research-ratchet/codex-sim-basin-dynamics-plan-2026-06-21]]
