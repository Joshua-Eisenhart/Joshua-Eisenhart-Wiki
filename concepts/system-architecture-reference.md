---
title: System Architecture Reference
created: 2026-04-07
updated: 2026-04-10
type: summary
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/SYSTEM_ARCHITECTUREREFERENCE.md
framing: mixed
---

# System Architecture Reference

## Overview
Support/reference extraction of CS axioms, host planes, runtime kernel objects, and enforcement principles from the v5 reference docs. Use it as a historical/current-docs-aligned reference surface, not as the sole live rulebook.

## CS Axiom Translation (EC-1 through EC-7)

| ID | Statement | CS meaning | Forbids |
|---|---|---|---|
| EC-1 | Identity not primitive | Object is "same" only if witnessed by handles/receipts/invariant checks | Assuming sameness after mutation without proof |
| EC-2 | Equality not primitive | Equivalence is contract-based: schema checks, type checks, compatibility checks | Free substitution, semantic smuggling |
| EC-3 | Identity requires boundary | Service/agent/module exists only relative to scope, ownership, interface boundary | Ambient authority, global omniscience |
| EC-4 | Time/causality derived from ordered composition | Causal chain = event log and receipt chain, not a story told afterward | Causal handwaving, time as ordering oracle |
| EC-5 | Geometry/coordinates not primitive | Architecture views are derived projections over state | Global coordinate thinking |
| EC-6 | Closure never assumed | Two APIs compose only if explicit contract says they do | Implicit interoperability, magic composition |
| EC-7 | Every claim needs finite witness | Every action needs evidence: receipt, log, diff, hash, test, measurement | "Trust me," unverifiable state |

## 8 CS General Principles

| Principle | CS form |
|---|---|
| Bounded execution | Token budgets, iteration caps, timeouts, memory limits |
| Append-only history | Event logs, immutable receipts, write-ahead records |
| Compensation not erasure | Undo is a new event. Compensating transactions, tombstones |
| Locality | Sandboxing, capability grants, namespace boundaries |
| Contract-first execution | Schemas, typed interfaces, validation gates |
| Fail-closed admission | Unknown means deny. Schema-required execution |
| Evidence-backed progress | Receipts, test results, metrics, state hashes |
| Projection not ontology | Dashboards, summaries, caches are materialized views only |

## Graph Topology as First Admissible Geometry

Once identity, equality, geometry, causality are not primitive, what remains: finite tokens, finite relations, ordered composition, compatibility/incompatibility. That is graph-native. The chain is constraints to finite relations to G=(V,E) to paths to cycles to higher topology. Graph structure comes earlier than metric geometry. Hopf/Weyl/QIT geometry is a later richer realization of the same constraint-topological structure.

## Host Architecture Planes (Lev Stack)

| Plane | Role |
|---|---|
| Topology | Allowable regions, graph connectivity, transitions, gates, terminals |
| Orchestration | Loop policies, traversal strategies, retry, phase advancement |
| Dispatch | Executing transforms, sims, reviewers, validators |
| Event Spine | Append-only: witness traces, evidence, step history |

## Runtime Kernel Objects

| Object | Definition |
|---|---|
| RuntimeState | region, phaseIndex, phasePeriod, loopScale, boundaries, invariants, dof, context |
| Probe | State-observation operator to Observation (probeId + features) |
| Transform | Ordered state-evolution: apply(state, input) to next_state |
| Witness | Evidence object (positive/negative/counterexample) + trace of StepEvents |
| StepEvent | Single transition record: at, op, beforeHash, afterHash |

## Sim Admission Contract

Every sim must declare: sim_class, tier, required_tools, required_inputs, required_outputs, allowed_claims, promotion_blockers. Missing anything fails closed.

## 6 Enforcement Principles

1. **Claim Gate**: no prose upgrades results. Only artifact class can.
2. **No Smoothing Rule**: branch conflicts stored as separate branches.
3. **Boot Gate**: boots read only decision log, sim registry, artifact registry, tranche ledger.
4. **Doc Freeze Rule**: docs are reference only. Runtime truth must be machine-readable artifacts.
5. **Concrete Principle**: do not trust LLM to follow process. Make process executable. Make violations mechanically visible.
6. **Minimal v5 Law**: required step must have artifact. Required tool must have output present. Incomplete outputs not promoted. Open branch cannot narratively close.

## Minimum Clean Stack
Target tools: networkx (graph structure), pydantic (typed schemas), jsonschema (artifact validation), z3 (proof/admissibility gates), pytest (tiered sim contracts), hypothesis (property-based pressure). Note: z3 installed but not directly imported at module level — pySMT is the abstraction layer. This describes target stack, not current live state. Current live repo already carries a broader optional sim stack as well, including torch, sympy, cvc5, geomstats, rustworkx, xgi, TopoNetX, GUDHI, and torch-geometric. For future basin-engine work, likely next-tier additions are optional tools such as QuTiP, CVXPY, and JAX-family solvers, not replacements for the pure lego base. (from SYSTEM_ARCHITECTURE_REFERENCE.md)

## Layer 0/1/2 Control Governance

**Layer 0 (invariants):** Constraint-driven ratchet engine, not a proof system. Like evolution — branches, dead branches. What survives is bounded admissible process under constraint; [[attractor-basins-formal-reference|attractor basins]] are one possible regime, not the generic identity of survival. Two root constraints: FINITUDE + NONCOMMUTATION. The machine is the product. Implicit is the enemy. A2 is the user.

**Layer 1 (architecture):** Thread roles: A2 (mining/governance), A1 (strategy/sim generation), A0 (deterministic compiler), B (canon enforcement), SIM (terminal execution). Entropy tiers E0-E3: E3 (high: holodeck, Grok/Gemini), E2 (medium: physics fuel), E1 (low: constraint ladder specs), E0 (very low: bootpacks, strongest low-entropy anchors). Graveyard-first is the historical framing: everything starts DEAD, the graveyard is the workspace, and survivors earned their way out.

**Layer 2 (direction):** Exploratory, not locked. Build order proposals, current priorities. Axes math without axis labels: topology and math can be ratcheted without Jung/IGT/MBTI/I-Ching terms in Thread B. Labels are [[rosetta-terrain-mapping|Rosetta overlay]] only.

## How it connects
This doc is the operational backbone for [[constraint-surface-and-process]] and [[stack-authority-and-capability-index]]. The enforcement principles are what make [[formal-methods-and-witness-discipline]] mechanically real rather than aspirational.

## Open questions
- Minimum Clean Stack (networkx, pydantic, jsonschema, z3, pytest, hypothesis) describes the target, not current live state. z3 is installed but not directly imported at module level.
