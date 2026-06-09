---
title: Hypothesis Property Based Testing Reference
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [concept, research, tooling, formal, validation]
sources:
  - raw/articles/new-docs/SYSTEM_ARCHITECTURE_REFERENCE.md
  - raw/articles/new-docs/archive_old/NONCLASSICAL_SYSTEM_TOOL_PLAN.md
framing: current
---

# Hypothesis Property-Based Testing Reference

## Overview
Hypothesis is the property-based pressure tool in the architectural plan. It matters when example-based tests are too weak and the project needs invariant pressure across many generated cases.

## Best-fit jobs in this stack
- invariant pressure on sims
- adversarial/generated test cases for bounded contracts
- wider negative/control coverage than hand-picked examples alone

## Why it matters here
The project repeatedly emphasizes negative sims, alternatives, and broader option pressure. Hypothesis is a natural test-layer tool for that style.

## How it connects
- [[pytest-tiered-gate-reference]]
- [[system-architecture-reference]]
- [[nonclassical-system-tool-plan]]
- [[formal-methods-and-witness-discipline]]
