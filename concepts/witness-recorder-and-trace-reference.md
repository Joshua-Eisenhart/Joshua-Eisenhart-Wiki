---
title: Witness Recorder and Trace Reference
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [concept, research, tooling, formal, systems, validation]
sources:
  - raw/articles/new-docs/SYSTEM_ARCHITECTURE_REFERENCE.md
  - raw/articles/new-docs/archive_old/NONCLASSICAL_SYSTEM_TOOL_PLAN.md
framing: current
---

# Witness Recorder and Trace Reference

## Overview
The witness recorder is the append-only witness-trace layer named in the tool plan and architecture surfaces. It is important because the stack wants explicit evidence traces, not just final summaries.

## Best-fit jobs in this stack
- append-only witness traces
- provenance for claim/counterexample paths
- step history for bounded runs
- persistent evidence objects for later audit

## Why it matters here
The project’s evidence model is not only “did it run?” but “what explicit trace or witness object supports the claim?” This page names that tooling role directly.

## How it connects
- [[current-formal-methods-core]]
- [[system-architecture-reference]]
- [[nonclassical-system-tool-plan]]
- [[probe-doc-result-map]]
