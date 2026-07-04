---
title: Cvc5 SMT and SyGuS Reference
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [concept, research, formal, tooling, proof, constraints, mathematics]
sources:
  - raw/articles/new-docs/TOOLING_STATUS.md
  - raw/articles/new-docs/references/FORMAL_METHODS_AND_WITNESS_DISCIPLINE_REFERENCE.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# cvc5 SMT and SyGuS Reference

## Overview
cvc5 serves as the second proof/solver surface in the stack. Its role is not just redundancy with Z3: it also brings a stronger synthesis-facing flavor through SyGuS.

## Best-fit jobs in this stack
- cross-check Z3 proofs and exclusions
- syntax-guided synthesis (SyGuS)
- secondary proof pressure on seam/bridge claims
- guard against overfitting one solver's modeling quirks

## Why it matters here
The stack wants more than one proof surface when a claim is load-bearing. cvc5 provides:
- solver diversity
- synthesis capabilities
- additional pressure on exact bridge/cut conditions

## Limits
cvc5 is not automatically needed on every bounded packet. It becomes most useful when:
- a Z3 result is highly load-bearing
- synthesis of a boundary or candidate expression matters
- a second proof surface strengthens trust in a hard exclusion/result

## Current concrete tool-capability anchor
The current bounded anchor is `system_v4/probes/sim_cvc5_shells_crosscheck.py`, which now makes its own baseline-vs-canonical split explicit in the emitted result JSON.

Baseline/reference task:
- run the bounded shell-admissibility exclusions with Z3 alone and treat that as the single-solver proof reference

Canonical tool-native counterpart:
- rerun the same bounded claims through cvc5 as an independent solver
- require solver-agreement on the UNSAT/SAT verdicts
- attempt a real SyGuS boundary-synthesis task rather than leaving cvc5 as a declared import

Current load-bearing contract:
- **z3** is load-bearing only if it supplies the reference verdicts being cross-checked claim-by-claim
- **cvc5** is load-bearing only if it independently reproduces those bounded verdicts and executes the SyGuS step as a real synthesis action
- if cvc5 is merely imported, or if the SyGuS/cross-check work is skipped, the packet does not honestly count as canonical-by-process for cvc5 capability

This is a good model for future cvc5 work in the repo: keep the packet bounded, keep the reference-vs-canonical split explicit, and promote cvc5 by making it solve or synthesize something that matters to the claim rather than just agreeing in prose.

## How it connects
- [[smt-formal-falsifier-lane]]
- [[z3-smt-solver-reference]]
- [[formal-methods-and-witness-discipline]]
- [[tooling-status]]
- [[controller-prompt-rules]]
- [[llm-research-gap-matrix]]
