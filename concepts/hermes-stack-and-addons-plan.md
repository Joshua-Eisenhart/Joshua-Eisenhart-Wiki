---
title: Hermes Stack And Addons Plan
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, system, planning]
sources:
  - raw/articles/new-docs/archive_old/HERMES_STACK_AND_ADDONS_PLAN.md
framing: legacy
priming: false
---

# Hermes Stack and Add-ons Plan

## Overview
Defines Hermes itself, Hermes-related repos, add-ons, skills, and improvement surfaces as a first-class stack. Specifically about Hermes -- not the whole machine.

## Core Role of Hermes
Hermes is not just a convenience agent. In this system: A2 high-entropy ingestion plane, bounded planning/audit surface, architecture support layer, system that can later help ratchet the broader stack. Treated as part of architecture, install/use plan, skills plan, and cleanup plan.

## Governing Rules for Hermes Use
1. Do not ask Hermes to understand the whole system at once
2. Feed Hermes bounded packs slowly (see [[bounded-hermes-ingestion-protocol]])
3. Every ingestion pass should have: scope, role, task, required output
4. Hermes should not be rewarded for smoothing ambiguity
5. Hermes should not be asked for narrative closure where proof/graph/sim pressure is required
6. Hermes should support QIT engine work, not replace it with prose
7. Stack planning should happen before mass installs or mass cleanup

## What Counts as Hermes Extensions
Hermes itself, related repos, things built to make Hermes better, self-improvement surfaces, skills, operational patterns, bounded ingestion/audit workflows. Does NOT mean random plugins.

## Stack Categories
1. Hermes core: main operational agent surface
2. Hermes improvement repos: self-evolution, skills development
3. Hermes ecosystem/reference repos: external references, patterns
4. Hermes skills: specific capabilities
5. Hermes bounded-ingestion procedures: see [[bounded-hermes-ingestion-protocol]]
6. Hermes verification and safety procedures
7. Hermes future self-improvement layer

## Hermes Core Requirements
"Solid" means: correct tool access, clear install/use path, bounded context discipline, stable skill loading behavior, no broad-prompt "digest everything" workflow, good support for formal docs and audits.

## Related pages
- [[hermes-repos-and-ecosystem-classification]]
- [[agent-workflow-and-boot-architecture]]
- [[bounded-hermes-ingestion-protocol]]
- [[skills-plan-keep-build-patch-retire]]
