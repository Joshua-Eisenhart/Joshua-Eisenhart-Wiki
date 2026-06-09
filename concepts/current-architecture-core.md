---
title: Current Architecture Core
created: 2026-04-07
updated: 2026-04-13
type: summary
tags: [reference, research, system, architecture]
sources:
  - raw/articles/new-docs/SYSTEM_ARCHITECTURE_REFERENCE.md
framing: dated_architecture_snapshot
---

# Current Architecture Core

This is a dated architecture snapshot extracted from older doc mirrors. It is
useful for concepts and language, not current Codex Ratchet executable
authority. For live process/status authority, start with
[[projects/codex-ratchet/read-first]] and [[specs/codex-ratchet/README]].

## Overview
Extracted from v5 docs. Covers CS axiom translation, graph topology as first admissible geometry, Lev stack host architecture planes, runtime kernel objects, and sim admission contract.

For the live controller-facing rendering of those same ideas, read this together with [[codex-ratchet-cs-bounded-system-framing]], [[nominalist-cs-framing]], and [[controller-state-transition-model]]. Those pages translate the architecture core into current queue, truth-label, maintenance-surface, and bounded-transition language.

## CS Axiom Translation (EC-1 through EC-7)
The system's axioms translated to computer science terms:
- EC-1 Identity not primitive: Object is "same" only if witnessed by handles/receipts/invariant checks
- EC-2 Equality not primitive: Equivalence is contract-based (schema checks, type checks)
- EC-3 Identity requires boundary: Module exists only relative to scope, ownership, interface
- EC-4 Time/causality from ordered composition: Causal chain = event log, not story told afterward
- EC-5 Geometry/coordinates not primitive: Architecture views are derived projections over state
- EC-6 Closure never assumed: Two APIs compose only if explicit contract says so
- EC-7 Every claim needs finite witness: Every action needs evidence (receipt, log, diff, hash, test)

## 8 CS General Principles
Bounded execution (token budgets, iteration caps), append-only history, compensation not erasure (undo is new event), locality (sandboxing, namespace boundaries), contract-first execution (schemas, validation gates), fail-closed admission (unknown means deny), evidence-backed progress, projection not ontology (dashboards are materialized views).

## Graph Topology as First Admissible Geometry
Once identity, equality, geometry, causality are not primitive, what remains: finite tokens, finite relations, ordered composition, compatibility/incompatibility. The current architecture orders this graph-native layer before metric geometry: constraints -> finite relations -> G=(V,E) -> paths -> cycles -> higher topology. Hopf/Weyl/QIT geometry is treated here as a richer later route over the same candidate constraint-topological support, not proof that all routes collapse to one CS chain.

A later thread-level correction sharpens this further: support surfaces are primary, operators are later. The important question is what can run on a given support and what must be simulated rather than declared. See [[support-first-constraint-manifold-dependency-chain]].

## Host Architecture Planes (Lev Stack)
| Plane | Role |
|---|---|
| Topology | Allowable regions, graph connectivity, transitions, gates |
| Orchestration | Loop policies, traversal strategies, retry, phase advancement |
| Dispatch | Executing transforms, sims, reviewers, validators |
| Event Spine | Append-only: witness traces, evidence, step history |

## Runtime Kernel Objects
RuntimeState: region, phaseIndex, phasePeriod, loopScale, boundaries, invariants, dof, context. Probe: state-observation operator -> Observation. Transform: ordered state-evolution. Witness: evidence object with trace of StepEvents. StepEvent: single transition record.

## Sim Admission Contract
The old shorthand was: every sim declares class, tier, tools, inputs, outputs,
allowed claims, and blockers. Current sim-contract authority belongs to
[[specs/codex-ratchet/lego-sim-contract-current]] plus the live repo
`system_v5` docs and validators.

## Related pages
- [[codex-ratchet-cs-bounded-system-framing]]
- [[nominalist-cs-framing]]
- [[controller-state-transition-model]]
- [[lego-sim-contract]]
- [[lego-build-catalog]]
- [[actual-lego-registry]]
- [[system-context-handoff-current]]
- [[constraint-on-distinguishability-full-math]]
- [[current-pre-axis-sim-status-keep-open-diagnostic-broken]]
