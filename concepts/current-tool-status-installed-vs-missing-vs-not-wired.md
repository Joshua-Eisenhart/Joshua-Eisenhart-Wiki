---
title: Current Tool Status Installed Vs Missing Vs Not Wired
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, system, tooling]
sources:
  - /Users/joshuaeisenhart/wiki/raw/articles/new-docs/archive_old/CURRENT_TOOL_STATUS__INSTALLED_VS_MISSING_VS_NOT_WIRED.md
  - raw/articles/new-docs/archive_old/CURRENT_TOOL_STATUS__INSTALLED_VS_MISSING_VS_NOT_WIRED.md
framing: legacy
priming: false
spec_mirrors:
  - specs/codex-ratchet/tool-function-receipt-status
  - specs/codex-ratchet/sim-estate-integration-status
---

# Current Tool Status: Installed vs Missing vs Not Wired

## Overview
Current tool-use routing and admissible proof roles now live in [[specs/codex-ratchet/tool-function-receipt-status|Tool Function Receipt Status]] and [[specs/codex-ratchet/sim-estate-integration-status|Sim Estate Integration Status]]. Concept-level role language is routed by [[repo-tool-use-router]].

Classifies tools by their historical operational status: installed and working, installed but not wired into the pipeline, or missing entirely. Superseded by [[tooling-status]] as a dated snapshot and by the specs mirrors for current repo-facing status.

## Classification Framework

### Installed and Working
Tools that are installed in the venv, importable, and wired into the simulation pipeline. These can be run directly via the runner layer.

### Installed but Not Wired
Tools that are installed in the venv and importable, but not yet connected to the sim pipeline or handoff system. May require additional integration work (e.g., output format conversion, result artifact wiring).

### Missing
Tools that are not installed or not importable. Need pip install or system-level setup before they can be used.

## Key Distinction
A tool being installed does not mean it is operational. The wiring between tool output and sim results / JSON artifacts is a separate step. Many tools fall in the "installed but not wired" category.

## Installation Rule
Use the project venv, not system Python. Use exact interpreter path in all handoffs. See [[claude-code-dangerous-mode-policy]] for dangerous mode enforcement of this rule.

## Related pages
- [[tooling-status]]
- [[current-tool-status-operational-classification]]
- [[current-architecture-core]]
- [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]]
