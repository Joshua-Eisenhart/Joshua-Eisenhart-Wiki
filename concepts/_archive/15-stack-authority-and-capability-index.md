---
title: Stack Authority And Capability Index
created: 2026-04-07
updated: 2026-04-08
type: summary
framing: archived_source_bundle_snapshot
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/15_stack_authority_and_capability_index.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Stack Authority and Capability Index

## Overview
Archived source-bundle governance snapshot for the new-docs stack. `canonical` below is a bundle-internal reference label, not current repo status, readiness, or promotion authority. Not a math doc — a governance doc.

## Canonical Stack Index

| Doc | Class | Status | Role |
|---|---|---|---|
| 00_manifest | index | canonical | folder index |
| CONSTRAINT_SURFACE_AND_PROCESS | process | canonical | process rules, constraint surface, boots |
| TOOLING_STATUS | status | canonical | current tooling state |
| TIER_STATUS | status | canonical | tier/resolution status |
| BOOT_PROMPT_TEMPLATES | prompt | canonical | launchable boot prompts |
| AGENT_WORKFLOW_AND_BOOT_ARCHITECTURE | architecture | canonical | boot/agent architecture |
| 06_entropy_sweep_protocol | protocol | canonical | entropy sweep rules |
| 07_model_math_geometry_sim_plan | plan | canonical | model-to-sim stack |
| 13_mimetic_meme_manifold_source_map | source-note | canonical | source-backed corpus |
| 14_mimetic_meme_manifold_canonical_synthesis | synthesis | canonical | merged synthesis |
| 15_stack_authority_and_capability_index | governance | canonical | this doc |

## Boot Capability Matrix

| Boot | Can run sims | Can audit | Can write canon | Artifact class |
|---|---|---|---|---|
| A1 / Recon | drives runner | no | no | recon artifacts |
| A0 / Compiler | no | yes | no | campaign tape |
| B / Ratchet | no | yes | yes | canon / ratchet decisions |
| SIM / Discipline Enforcer | no | yes | no | sim audits |
| Hermes / A2 | no | yes | no | plans / audits / routing |
| RUNNER | yes | no | no | sim result artifacts (.json) |

## Authority Rules

- canonical = current best internal reference for that layer
- source-note = may inform synthesis but does not override canonical governance
- archive_old = historical unless explicitly promoted
- If a boot can audit but not run sims, the docs must say so explicitly
- If a sim claim is live, the file must state the artifact and execution path

## Governance Gaps

- Some historical docs still mention archived execution paths
- Some active docs need provenance-based file names
- Some status claims need alignment to canonical tooling and tier docs

## How it connects
This governance doc references [[constraint-surface-and-process]] and [[system-architecture-reference]]. See [[00-manifest]] for the folder index and [[boot-prompt-templates]] for the actual boot prompts.

## Open questions
- Whether the governance gaps should be tracked as a TODO or as a living audit.
