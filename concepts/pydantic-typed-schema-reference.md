---
title: Pydantic Typed Schema Reference
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [concept, research, tooling, formal, systems]
sources:
  - raw/articles/new-docs/SYSTEM_ARCHITECTURE_REFERENCE.md
  - raw/articles/new-docs/archive_old/NONCLASSICAL_SYSTEM_TOOL_PLAN.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Pydantic Typed Schema Reference

## Overview
Pydantic is the typed-schema layer in the architectural tool plan. It matters because the stack wants typed contracts for sims, witnesses, graph nodes, and artifact payloads.

## Best-fit jobs in this stack
- typed sim contracts
- typed witness payloads
- typed graph/runtime objects
- validation before writing artifacts

## Why it matters here
If the project is serious about bounded objects and fail-closed admission, typed schemas are part of the foundation rather than convenience glue.

## How it connects
- [[jsonschema-artifact-validation-reference]]
- [[system-architecture-reference]]
- [[nonclassical-system-tool-plan]]
- [[formal-methods-and-witness-discipline]]
