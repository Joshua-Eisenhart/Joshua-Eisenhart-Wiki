---
title: LLM Research Enforcement Validator
created: 2026-04-10
updated: 2026-04-15
type: concept
tags: [reference, audit, validation, system, tooling]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/skills/llm_research_enforcement_validator.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/LLM_RESEARCH_GAP_MATRIX.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# LLM Research Enforcement Validator

## Role in the live wiki cluster
- Strongest use: implementation-facing summary of what the repo validator script actually checks before a controller accepts a worker closeout.
- Weak use: public repo-status authority page or replacement for the controller contract.
- Authority boundary: this page mirrors one repo implementation surface and its closeout schema; broad public status language still comes from [[llm-controller-contract]] and [[enforcement-and-process-rules]].

## Overview
Controller-side validation surface for research-closeout packets. This mirrors the repo script `system_v4/skills/llm_research_enforcement_validator.py` so the wiki has a public explanation of what the validator is checking before a controller should accept a worker closeout.

## What it checks
- Required closeout fields exist.
- Status vocabulary is in the allowed validator set.
- Strong claims require non-empty load-bearing tools.
- `canonical by process` requires a fresh rerun flag.
- The gap matrix has the expected ladder cells and valid cell values.

## Status vocabulary note
The validator script and the gap-matrix JSON are not fully vocabulary-aligned with the public controller docs yet:
- repo public controller/docs spine: `exists`, `runs`, `passes local rerun`, `canonical by process`
- repo validator implementation: `exists`, `runs locally`, `passes local rerun`, `proof-backed`, `canonical by process`
- repo gap-matrix JSON: `exists`, `runs`, `passes local rerun`, `proof-backed`, `canonical by process`

That means this page should describe the validator as an implementation-facing closeout checker, not as the source of the public reporting vocabulary. For broad repo-state summaries in the wiki, keep the four-label controller contract primary and treat `proof-backed` plus the validator-only `runs locally` spelling as implementation-detail or closeout-schema language unless the public docs themselves change.

## Why it matters
This validator does not magically make enforcement automatic. It is a fail-closed controller tool that should run before accepting closeouts or gap-matrix promotions in the research-enforcement lane.

## Related pages
- [[llm-controller-contract]]
- [[llm-research-gap-matrix]]
- [[controller-prompt-rules]]
- [[enforcement-and-process-rules]]
