---
title: Hermes Repos And Ecosystem Classification
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/archive_old/HERMES_REPOS_AND_ECOSYSTEM_CLASSIFICATION.md
framing: legacy
priming: false
---

# Hermes Repos and Ecosystem Classification

## Overview
Classifies Hermes-related repos and ecosystem surfaces so they can be planned, installed, referenced, or ignored explicitly. Part of the Hermes stack planning layer.

## Classification Labels
- core: first-class part of the Hermes stack
- active_dependency: needed directly for current active Hermes setup
- inspect_now: should be read/reviewed now, not necessarily installed immediately
- reference_only: useful to consult, not part of live stack
- method_mine: useful as source of patterns or techniques
- later_integration_candidate: worth considering once current stack is stable
- not_justified_yet: interesting but not currently justified

## Core Hermes Surfaces

### Hermes Agent (~/GitHub/hermes-agent)
Classification: core, active_dependency. This is Hermes itself. Currently treated as the A2 high-entropy ingestion plane per [[agent-workflow-and-boot-architecture]]. Primary operational agent surface. Immediate action: stabilize, understand, classify add-ons.

## Hermes Improvement Repos

### Hermes Agent Self-Evolution (~/GitHub/hermes-agent-self-evolution)
Classification: inspect_now, method_mine, later_integration_candidate. Directly aimed at improving Hermes Agent. Useful for evolving skills, tool descriptions, prompts, and later code. Belongs to second-order optimization phase, not immediate foundation. Higher priority: Hermes core + tool stack + bounded ingestion + QIT proto work.

## Ecosystem Curation Surfaces
Hermes ecosystem repos should be classified using the same labels. Each surface needs explicit classification rather than remaining a vague cluster.

## Related pages
- [[hermes-stack-and-addons-plan]]
- [[agent-workflow-and-boot-architecture]]
- [[system-meta-plan-repos-python-skills-hermes]]
- [[full-machine-python-repo-skills-inventory]]
