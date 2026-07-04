---
title: Agent Workflow And Boot Architecture
created: 2026-04-07
updated: 2026-04-08
type: summary
framing: legacy_workflow_reference
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/AGENT_WORKFLOW_AND_BOOT_ARCHITECTURE.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Agent Workflow And Boot Architecture

Legacy prompt/workflow artifact. Do not execute or treat as current agent
routing unless the current user request explicitly reauthorizes this exact lane;
current Codex Ratchet authority is repo `AGENTS.md` plus live `system_v5`
process docs.

## Overview
Defines the Hermes-to-Claude terminal workflow, boot types, contamination rules, and harness construction plan. Supersedes previous workflow docs as of 2026-04-05.

## Architecture
Hermes (A2) launches [[claude-code]] terminals with boot prompts. Each terminal runs its boot, produces repo artifacts, and Hermes audits results. As of 2026-04-05, Hermes launches Claude Code terminals natively (NousResearch/hermes-agent#5155). Pi-Mono is retired as the primary launcher.

## Boot Types

### A2 / Mining (Hermes)
Role: Owner's voice, high-entropy ingestion, external fuel, associative thinking, planning and audit. Bounded intake only -- never give unbounded packs. Cannot write canon.

### A1 / Recon (Claude Code)
Role: Understand and advocate for the owner's candidate geometry. Sim it richly. Preserve nuance. Build the phenotype description. This IS [[constraint-surface-and-process|harness construction]]. Must test weirdest, most falsifiable predictions first. Uses survived/killed/open vocabulary.

### A0 / Compiler (Claude Code)
Role: Structural audit and record. Campaign tape. Graveyard views. Extractive only -- never invents. Deterministic ordering. Source pointers on everything.

### B / Ratchet (Claude Code)
Role: Blind constraint enforcement. Accept or reject candidates against M(C). Does not know which candidate the owner favors. Constraint definitions do not reference any specific candidate. NO_INFERENCE, NO_REPAIR, NO_SMOOTHING. Currently not fully operational because the agent harness is still being constructed via A1 recon.

### SIM / Discipline Enforcer (Claude Code)
Role: Enforce rules about what sims must declare and produce. Not a sim runner -- a sim auditor. Execution lives in the runner layer (e.g. `system_v4.runners.run_real_ratchet`); SIM only audits artifacts.

## Contamination Rule
A1 output (recon) does NOT become B evidence (canon) without the proper pipeline: A1 produces recon artifacts, A0 or A1 translates into B-admissible format, A0 lints for structural compliance, B accepts or rejects blind to A1 provenance. If A1 output is directly cited as B evidence, that is contamination.

## Terminal Lifecycle
Terminals can be short-lived (one task), long-running (extended session), or recycled (reopen with same/different boot). Each launch specifies boot type, rules, allowed outputs, contamination avoidance, and downward-blind scope.

## Harness Construction (Meta-Goal)
The current meta-goal is building the agent harness that constrains how agents think. Order: A1 recon first, build harness from understanding, harness constrains agents to think non-Cartesian, then run formal ratchet (B boot) inside the harness.

## Dangerous Mode Policy
Dangerous mode allowed when: handoff is bounded and explicit, task is conservative and auditable, boot type is declared, terminal will be audited. Not a blank check.

## SIM Discipline Rules
Every sim must declare: role, tier/resolution, tools, artifacts, negatives, promotion status. diagnostic_only results cannot support geometry claims. Missing artifact = promotion blocked. Sims built from small composable pieces (lego sims). Each sim tests ONE thing. No sim may claim results above declared resolution level. (from AGENT_WORKFLOW_AND_BOOT_ARCHITECTURE.md)

## Handoff Files
Handoff files in .agent/handoffs/active/ queue bounded tasks. Each specifies: which boot, resolution level, available artifacts from lower resolutions, what terminal must NOT see (downward-blind enforcement). Terminal at resolution N sees 0..N-1, NOT N+1+. (from AGENT_WORKFLOW_AND_BOOT_ARCHITECTURE.md)

## Related pages
- [[boot-prompt-templates]]
- [[stack-authority-and-capability-index]]
- [[ladders-fences-admission-reference]]
- [[system-context-handoff-current]]
