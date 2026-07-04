---
title: System Tools and Plan
created: 2026-04-07
updated: 2026-04-08
type: concept
tags: [system, planning, validation, architecture]
sources:
  - raw/articles/system-v5-reference-docs/System tools and plan.md
  - raw/articles/new-docs/TOOLING_STATUS.md
  - raw/articles/new-docs/TODO.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# System Tools and Plan

## Overview
This page keeps the tooling and process plan separate from the math docs.

## The v5 failure mode
The real failure mode is not intelligence but missing enforcement. Without hard gates, the model will skip prerequisites, use whatever tool is easiest, produce summaries instead of substrates, mix diagnostic probes with real evidence, collapse open branches into one story, and mutate docs instead of building runtime truth. v4 demonstrated this: old-doc overload, graph overload, reduced probes treated too strongly, validator-green drift without substrate compliance.

## Sim Admission Contract and Process Contract
Every sim must declare: sim_class, tier, required_tools, required_inputs, required_outputs, allowed_claims, promotion_blockers. If anything is missing, it fails closed. Every tranche has required order, allowed tools, required outputs, forbidden shortcuts, and a stop rule. The build order is: carrier -> geometry -> Weyl/chirality -> transport -> negatives -> placement/embargo -> bridge/cut -> entropy -> higher consumers.

## Mandatory tools by tier
Required now: networkx (core graph structure), pydantic (typed schemas), jsonschema (artifact validation), z3 (constraint/admissibility checks), pytest (executable gates), hypothesis (property-based pressure). Required for full-geometry sims: TopoNetX (higher-order topology), witness trace recorder, constraint report generator, graph artifact emitter. Minimum clean stack: networkx + z3 + pydantic/jsonschema + pytest/hypothesis.

## Enforcement rules
No prose can upgrade a result — only artifact class can. Branch conflicts must be stored as separate branches; open candidates stay open; dead branches get marked dead, not blended into survivors. Docs are reference only by default; runtime truth must be emitted as machine-readable artifacts. Boot reads decision log, sim registry, artifact registry, and tranche ledger — nothing else is boot-authoritative.

## Concrete principle
Do not trust the LLM to follow process. Make the process executable. Make violations mechanically visible. Make unauthorized success impossible. If a step is required, it must have an artifact. If a tool is required, its output must be present. If outputs are incomplete, the run is not promoted. If branch status is open, the system may not narratively close it.

## Source
Extracted from `raw/articles/system-v5-reference-docs/System tools and plan.md`. See [[formal-methods-and-witness-discipline]] for the formal methods layer, [[tooling-status]] for current tool installation status, and [[enforcement-and-process-rules]] for the process enforcement rules.
