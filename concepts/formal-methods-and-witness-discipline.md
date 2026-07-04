---
title: Formal Methods and Witness Discipline
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, validation, system, architecture]
sources:
  - raw/articles/new-docs/references/FORMAL_METHODS_AND_WITNESS_DISCIPLINE_REFERENCE.md
  - raw/articles/new-docs/AGENT_WORKFLOW_AND_BOOT_ARCHITECTURE.md
  - raw/articles/new-docs/SYSTEM_ARCHITECTURE_REFERENCE.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Formal Methods and Witness Discipline

## Overview
This reference covers model checking, SAT/SMT, proof-carrying code, CEGAR, bisimulation, trace theory, refinement, invariants, and fail-closed design.

## Main points
- Verification is built around checkable witnesses and certificates.
- Bisimulation captures interaction-level indistinguishability.
- Refinement and invariants formalize safety-preserving narrowing.
- Fail-closed design matches the wiki’s evidence-first and deny-by-default discipline.

## Why it matters
This is the formal-methods companion to the system’s witness discipline and fail-closed architecture.

## Concurrency and Trace Theory
The formal-methods toolkit includes labeled transition systems (LTS), trace equivalence, bisimulation, and refinement — directly relevant to the system's N01 (noncommutation) constraint and the multi-shell coexistence program. Trace equivalence captures which operator orderings are physically indistinguishable; bisimulation captures branching structure. See [[concurrency-and-trace-theory-reference]] for the full treatment.

## Related pages
- [[system-architecture-reference]]
- [[stack-authority-and-capability-index]]
- [[constraint-on-distinguishability]]
- [[tier-status]]
- [[system-tools-and-plan]]
- [[axis-0-1-2-qit-packet]]
- [[concurrency-and-trace-theory-reference]]
- [[topos-quantum-mechanics-reference]]
