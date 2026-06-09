---
title: Skills Plan Keep Build Patch Retire
created: 2026-04-07
updated: 2026-04-24
type: summary
tags: [reference, research, system, planning]
sources:
  - raw/articles/new-docs/archive_old/SKILLS_PLAN__KEEP_BUILD_PATCH_RETIRE.md
framing: legacy
priming: false
---

# Skills Plan -- Keep / Build / Patch / Retire

## Overview
Defines how skills should be handled across the system so they become an operational layer instead of a pile of partially-related procedures. Covers: Hermes use, bounded ingestion, QIT/sim workflow, proof/graph/tooling workflow, cleanup/inventory workflow.

## Governing Rule
A skill should exist only if it has a recurring operational job. Do not keep or build skills that are: decorative, stale, narrative-only, one-off and trivial, disconnected from real workflow.

## Skill Status Classes
- keep: useful now, aligned with real workflow, worth maintaining
- build: needed but not yet properly formalized as a skill
- patch: already useful but incomplete, stale, or not aligned with current reality
- retire: no longer justified, stale, superseded, or misleading enough to remove
- reference_only: useful pattern source, not yet worth turning into a live skill

## What Skills Are For
Skills should serve recurring operational patterns: bounded [[bounded-hermes-ingestion-protocol|Hermes ingestion]], repo/tooling audits, QIT engine planning, pre-Axis sim classification, proof/graph tool wiring, cleanup planning, environment verification, artifact verification.

## Skills Curation Process
1. Inventory all existing skill-like procedures
2. Classify each as keep/build/patch/retire/reference_only
3. For keep/build: formalize with explicit inputs, outputs, and success criteria
4. For patch: identify the specific gap and fix it
5. For retire: remove from active use, archive if historically useful

## Key Skill Categories
- Ingestion: bounded pack preparation, frame selection, output formatting
- Audit: doc overlap detection, Platonic residue cleaning, vocabulary compliance
- Simulation: lego sim construction, result classification, negative control design
- Tool: environment verification, tool wiring, artifact validation
- Planning: batch task decomposition, dependency ordering, promotion gating

## Related pages
- [[hermes-stack-and-addons-plan]]
- [[agent-workflow-and-boot-architecture]]
- [[bounded-hermes-ingestion-protocol]]
- [[full-machine-python-repo-skills-inventory]]
