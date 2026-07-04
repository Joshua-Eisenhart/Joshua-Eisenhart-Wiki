---
title: Nonclassical System Tool Plan
created: 2026-04-07
updated: 2026-04-13
type: summary
tags: [reference, research, system, tooling, planning]
sources:
  - raw/articles/new-docs/archive_old/NONCLASSICAL_SYSTEM_TOOL_PLAN.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Nonclassical System Tool Plan

## Overview
Formal working plan for tools to install and use for the nonclassical pre-Axis simulation system. Defines the actual tool stack with named jobs.

## Governing Rule
Only add or keep a tool if it has a named job in the pre-Axis sim pipeline. Not allowed to drift into: toy sims, narrative proofs, scalar-only reductions, classical smoothing, using easiest tool instead of what the tier requires.

## Core Architectural Split

### Owner Stack (auditable core)
- pydantic: typed schemas for sim contracts, graph nodes, witness payloads
- jsonschema: artifact validation and anti-drift enforcement
- networkx: canonical in-memory graph structure
- GraphML: stable graph interchange format
- witness recorder: append-only witness traces with provenance
- pytest: executable gates per tier
- hypothesis: property-based pressure on invariants
- z3: hard admissibility, impossibility, embargo checks

### Augmentation Stack (richness/sidecar)
- torch: tensor substrate
- PyTorch Geometric (PyG): tensorized heterograph projections
- TopoNetX: higher-order topology, cells, boundaries
- clifford: noncommutative / graded / orientation-aware algebra
- pyquaternion: spinor/quaternion transformations (S3/Hopf/Weyl)
- hypernetx/xgi: higher-arity relational structure

### Fresh Proof/Geometry Additions
- cvc5: second solver, SyGuS synthesis
- sympy: exact symbolic pressure on lower-tier identities
- gudhi: topology-pressure on geometry ratchet
- ripser.py: persistence diagrams

## Tool Justification Categories
A tool is justified if it supports: admissibility checking, candidate-law synthesis/refinement, exact symbolic pressure, topology-pressure, rich tensor/chirality/entanglement simulation, graph-native state/writeback, negative-suite generation, witness/provenance discipline, promotion/embargo enforcement.

## Related pages
- [[tooling-status]]
- [[tool-capability-sim-program]]
- [[networkx-graph-structure-reference]]
- [[pydantic-typed-schema-reference]]
- [[jsonschema-artifact-validation-reference]]
- [[pytest-tiered-gate-reference]]
- [[hypothesis-property-based-testing-reference]]
- [[witness-recorder-and-trace-reference]]
- [[e3nn-equivariant-geometry-reference]]
- [[lean4-proof-assistant-reference]]
- [[tlaps-temporal-proof-reference]]
- [[z3-smt-solver-reference]]
- [[cvc5-smt-and-sygus-reference]]
- [[sympy-symbolic-math-reference]]
- [[rustworkx-graph-algorithms-reference]]
- [[xgi-hypergraph-reference]]
- [[toponetx-topological-complex-reference]]
- [[pytorch-geometric-reference]]
- [[gudhi-persistent-topology-reference]]
- [[geomstats-manifold-geometry-reference]]
- [[clifford-geometric-algebra-reference]]
- [[current-architecture-core]]
- [[nonclassical-topological-runtime-design]]
- [[current-tool-status-operational-classification]]
