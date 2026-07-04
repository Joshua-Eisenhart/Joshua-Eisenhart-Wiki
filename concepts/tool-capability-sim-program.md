---
title: Tool Capability Sim Program
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [concept, research, tooling, simulation, planning, validation]
sources:
  - raw/articles/new-docs/archive_old/NONCLASSICAL_SYSTEM_TOOL_PLAN.md
  - raw/articles/new-docs/TOOLING_STATUS.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Tool Capability Sim Program

## Overview
The stack should not only use tools opportunistically inside larger sims. It should also have bounded sims/probes designed to test the tools themselves so their real capability range is known before a load-bearing use.

## Why it matters here
A repeated project failure mode is:
- tool is installed or named
- tool appears in imports or plans
- but its actual capability envelope in this stack is still unknown

Tool capability sims fix that.

## What a tool capability sim should test
For a given tool:
- what job it is supposed to do here
- what minimal bounded task it can actually do
- what failure modes it has in this stack
- what counts as merely decorative versus load-bearing use
- how it compares against a simpler baseline or alternate tool

## Example targets
- Z3 impossibility micro-probes
- cvc5 cross-check / SyGuS micro-probes
- sympy derivation probes
- rustworkx DAG/routing probes
- XGI multi-way interaction probes
- TopoNetX cell-complex probes
- PyG tensor-on-graph probes
- GUDHI filtration/persistence probes
- geomstats geodesic/metric probes
- e3nn equivariance probes

## Two-track architecture
Tool capability sims should now be read through an explicit two-track boundary:
- classical baseline sims: numpy/classical substrate computes the object
- canonical sims: the nonclassical tool stack computes the object or the decisive structural claim

This means every major tool family can have:
1. a baseline/reference sim
2. a canonical/tool-native counterpart
3. a comparison surface explaining what the tool adds beyond the baseline

See [[classical-baseline-vs-canonical-tool-boundary]].

Important caution:
- these are comparison and refinement surfaces, not canon stamps
- a tool capability sim can show that a tool is useful or even load-bearing in one bounded lane without proving that the broader doctrine lane is closed

## Why this matches the lego program
These are tool-legos:
- bounded
- falsifiable
- reusable
- directly useful for later bigger sims

So tool capability sims are not side work. They are part of building a reliable foundation.

## How it connects
- [[tooling-status]]
- [[nonclassical-system-tool-plan]]
- [[tool-manifest-audit]]
- [[support-first-constraint-manifold-dependency-chain]]
- [[research-inventory-and-foundations]]
