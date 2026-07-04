---
title: Graph-Driven Intent Runtime
created: 2026-04-07
updated: 2026-04-13
type: concept
tags: [graph, runtime, leviathan, developer, computer-science, translation]
sources:
  - raw/articles/system-v5-reference-docs/Older Legacy/jp graph prompt!!.txt
  - raw/articles/legacy-books/leviathan-v3-2-word.txt
  - /Users/joshuaeisenhart/GitHub/leviathan/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md
framing: current
framing_note: Current dev-facing bridge page. Restates the legacy graph/intent lane in cleaner runtime terms for JP/CS handoff without promoting the legacy prompt itself to repo contract status.
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Graph-Driven Intent Runtime

## Overview
This page is the main JP/CS-facing bridge for the graph/proposal-first lane.

Its core claim is simple: the system should not treat chat as truth. It should treat chat as an action surface that produces observations, proposals, and bounded state transitions against an explicit graph.

That makes this page a current translation surface, not a raw-source digest and not a live repo contract page.

## Role in the live wiki cluster
- **Strongest use:** main dev-facing explanation of the proposal-first graph/runtime lane for JP or other CS readers.
- **Weak use:** not a substitute for live repo contracts and not the right page for deep legacy provenance or worldview placement.
- **Authority boundary:** current translation surface. It restates the legacy graph/intent lane in runtime language, but it does not define the repo's normative interfaces by itself.

Its role is distinct from nearby pages:
- [[leviathan-framework]] = legacy social-OS and semantic-computing genealogy
- [[model-context-overlay]] = legacy interpretive overlay and worldview-placement surface
- [[recursive-science-methodology-reference]] = recursive correction/accounting method
- [[holodeck-qit-fep-leviathan-integration]] = world-model, memory, and simulation-side integration

## Recommended reading order
If the immediate question is runtime/dev handoff, do **not** start in [[leviathan-framework]] or [[model-context-overlay]] unless provenance is the actual question. Start with the repo authority ladder and this page, then backtrack to genealogy only when needed.

For JP-facing handoff, the clean route is:
1. live Lev repo docs (`README.md` -> `docs/README.md` -> `docs/ARCHITECTURE.md` -> `docs/ROADMAP.md`)
2. this page for the graph/proposal-first runtime rendering
3. [[recursive-science-methodology-reference]] for the update/accounting discipline behind the runtime loop
4. [[holodeck-qit-fep-leviathan-integration]] for the internal world-model and memory layer
5. [[leviathan-framework]] and [[model-context-overlay]] only when genealogy/provenance or historical framing becomes necessary

## Repo authority ladder for JP handoff
When this page is used in a developer handoff, the live repo docs should be loaded in this order:
- `README.md` = what Lev is and the quick three-plane orientation
- `docs/README.md` = which doc surfaces outrank which others (`docs/specs/` > `docs/ARCHITECTURE.md` > `docs/ROADMAP.md` > `docs/design/` > `docs/_inbox/`)
- `docs/ARCHITECTURE.md` = hard runtime boundaries and ownership labels
- `docs/ROADMAP.md` = honest current-state surface
- `docs/specs/` = normative contracts when a concrete interface matters

## Core operating model
The durable kernel from the legacy prompt is:
- the graph is the truth-bearing state surface
- messages are observations, not final facts
- every response is a proposal against graph state
- nothing is final until it passes an explicit acceptance/gating step
- views are projections of graph state, not substitutes for it

This is the important CS/dev move: runtime state should not be hidden inside prose continuation.

## The primitive set worth preserving
The raw source names a useful runtime vocabulary:
- message = raw observation arriving through an action surface
- intent = directional pressure, not yet a goal theorem
- entity / relation = explicit graph objects
- proposal = suggested change to graph state
- patch = concrete mutation candidate
- view = projection for docs, UI, explanation, or task surfaces
- tick = one bounded state-advance cycle

These primitives are valuable because they keep reasoning, proposal, mutation, and acceptance from collapsing together.

## Separation discipline
The strongest operational rule in the source is a separation rule:
- reasoning is not the same as proposal
- proposal is not the same as patch
- patch is not the same as acceptance

That separation is what keeps the system from turning into a persuasive chatbot that silently edits truth.

## Tick-cycle crosswalk to the live Lev runtime
The legacy prompt says every turn simulates a tick. The current Lev repo gives that intuition a cleaner runtime rendering.

The useful crosswalk is:
- **INGEST / OBSERVE** -> action surfaces receive input as events or observations, not as already-trusted truth
- **PROPOSE** -> the system forms candidate graph deltas, task deltas, or state interpretations
- **GATE** -> policy and ownership checks decide what may advance
- **APPLY / UPDATE** -> accepted deltas become explicit state transitions
- **EMIT** -> the system records the transition on the event spine for replay, audit, or downstream surfaces

This is why the graph-driven page matters for JP handoff: it is a conceptual runtime rendering that aligns with the repo's explicit state/policy/event boundaries.

## Four-plane crosswalk to Lev repo docs
The live Lev docs separate policy, state, execution, and causality instead of flattening them.

A useful translation is:
- **FlowMind / control-policy plane** -> where constraints, gates, and allowed moves are declared
- **Graph / state-knowledge plane** -> where entities, relations, proposals, and accepted state live
- **Orchestration / execution plane** -> where bounded work is scheduled and run
- **Event Bus / causality plane** -> where transitions are emitted, replayed, and audited

This page mainly explains the Graph-facing side of that architecture, but it only makes full sense when paired with the other three planes.

## Repo role labels the wiki should not erase
The live repo keeps several engineering roles explicit that this translation page should preserve:
- `README.md` gives a fast three-plane view: FlowMind, Graph, Event Bus.
- `docs/ARCHITECTURE.md` hardens that into four planes by separating **Orchestration** as its own execution plane.
- `core/poly` owns binding/routing and generated control surfaces; `core/exec` owns execution-engine behavior.
- AgentPing is the default human-loop host/surface system, not the runtime core itself.

So this page should not silently collapse Graph, FlowMind, Orchestration, Poly, Exec, and AgentPing into one generalized "graph runtime" label. Its job is narrower: render the proposal-first graph intuition in terms that line up cleanly with those explicit repo owners.

## What this page is not
This page should not be flattened into any of the following:
- a generic "everything is a graph" slogan
- ordinary chat memory with prettier labels
- document-first truth where markdown pages silently outrank runtime state
- a claim that the current Lev repo already implements the full legacy prompt literally

The repo docs are still the authority for actual runtime ownership and contracts.

## Why this matters for JP/CS readers
JP is already building a runtime where policy, graph state, and event flow are explicit. This page helps explain why the older Leviathan lane converges naturally toward that architecture:
- intent should be interpreted, not merely string-matched
- state should be explicit and reviewable
- transitions should be proposal/gate/apply rather than narrative drift
- surfaces should project state rather than replace it

That is the part worth handing off, not the exact legacy prompt footer format.

## Safe claim boundary
What is safe to say:
- the legacy prompt clearly preserves a proposal-first, graph-first runtime intuition
- that intuition aligns well with the live Lev architecture's explicit state/policy/event split
- this page is a useful dev-facing translation surface for JP handoff

What is not safe to say:
- that the legacy prompt itself is the runtime contract
- that every part of the current Lev repo was derived from this source
- that graph state alone captures the full Leviathan / holodeck / QIT architecture without the world-model and method layers
- that this page by itself captures the full Poly / Exec / AgentPing ownership split or the repo's 3-plane versus 4-plane authority surfaces

## One-sentence summary
The graph-driven intent runtime is the JP-facing translation of a proposal-first idea: messages are observations, graph state is explicit truth-bearing state, and every meaningful change should move through a bounded propose -> gate -> apply -> emit cycle rather than disappearing into chat prose.

## Related pages
- [[leviathan-framework]]
- [[model-context-overlay]]
- [[recursive-science-methodology-reference]]
- [[holodeck-qit-fep-leviathan-integration]]
- [[a2-intent-summary]]
- [[leviathan-world-engine-memo]]
- [[source-notes]]
