---
title: Codex Ratchet CS Bounded System Framing
created: 2026-04-11
updated: 2026-05-21
type: concept
framing: conceptual_controller_model_snapshot
tags: [system, controller, queue, audit, constraints, maintenance]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/controller_maintenance_checklist.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/on-demand-telegram-runner.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/sim_backlog_matrix.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/sim_truth_audit.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/wiki_ingest_and_lego_maintenance.md
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/process-contract-mirror-index.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/llm-controller-contract-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/enforcement-process-rules-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/formal-scout-readiness-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
---

# Codex Ratchet CS Bounded System Framing

## Overview
Codex Ratchet can be read in computer-science terms as a bounded controller system for staged artifact construction. Hermes is the controller. Claude Code CLI or Codex CLI may be used as workers. The queue is explicit. State changes are admitted only through bounded verification. Evidence lives in files, result JSONs, ledgers, and wiki pages rather than in model memory.

This framing should stay constraint-first and nominalist. The system does not start from a claim of completed theory closure. It starts from declared objects, allowed transitions, and evidence-bearing maintenance surfaces.

Status boundary: this page is a conceptual controller framing, not a live queue, validator, or sim-status surface. For current repo process/status, start at [[specs/codex-ratchet/process-contract-mirror-index|process-contract-mirror-index]], [[specs/codex-ratchet/llm-controller-contract-current|llm-controller-contract-current]], [[specs/codex-ratchet/formal-scout-readiness-status|formal-scout-readiness-status]], and [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]].

## System model
In this controller-model snapshot, the system has five main parts:

1. controller
   - Hermes chooses the next bounded move from the live control surfaces.
   - Hermes owns truth labels, health reporting, progress reporting, and closeout.
   - Workers are subordinate execution surfaces, not truth authorities.

2. bounded objects
   - queue items: batches, lanes, packets, lego prerequisites, engine-readiness gates
   - evidence artifacts: scripts, result JSONs, audit tables, ledgers, wiki concept pages
   - status-bearing rows: truth-audit entries, backlog rows, lego-registry rows
   - maintenance surfaces: docs that track queue, truth, tool depth, and wiki sync

3. transition rules
   - every run must declare a bounded objective, expected outputs, and a verify step
   - stronger status cannot be inferred from weaker status
   - docs, ledgers, and wiki should be patched together when state materially changes
   - geometry-before-axis is a global ordering constraint on the queue

4. worker layer
   - workers can execute one bounded non-overlapping subtask
   - workers may produce files and candidate summaries
   - controller must audit worker output before promotion

5. closure surfaces
   - backlog queue
   - truth audit
   - controller checklist
   - Telegram runner / liveness protocol
   - tool-maintenance matrix
   - lego ledgers
   - touched wiki concept pages

## Controller as a state machine
A run is not modeled as open-ended autonomy. It is a bounded state machine with explicit control checks.

Minimal state sequence:
1. discover
   - read live control surfaces
   - identify primary lane and maintenance lane
2. bind
   - define bounded objective
   - name the exact prerequisite or gate being advanced
   - define expected outputs and verify step
3. launch
   - start a real worker or real foreground task
   - do not mark the run active until the actual worker/process is confirmed
4. execute
   - perform one primary lane plus one maintenance lane by default
   - keep file sets non-overlapping if parallel workers exist
5. heartbeat
   - report current lane, current task, last successful step, health, changed files, next bounded step
   - distinguish controller alive from worker alive from work completed
6. audit
   - run the bounded verification pass
   - classify outputs with explicit truth labels
7. close
   - record what prerequisite or gate actually moved
   - update touched maintenance surfaces or queue them explicitly
   - report blockers and next bounded move

Failure mode is fail-soft rather than silent disappearance: if one bounded step fails, the blocker should be recorded and the run should still move into diagnosis or closeout when safe.

## Bounded objects
The repo-current controller language already treats the important objects as bounded and typed.

### 1. Queue objects
The queue surface cited by this snapshot is `system_v5/docs/plans/plans/sim_backlog_matrix.md`.
Its objects are not generic tasks; they are lane-scoped construction packets with:
- priority
- objective
- current state
- next bounded move
- notes or preferred tool pressure

The queue is constrained by policy:
- build engines through controlled lego construction
- geometry-before-axis
- one primary lane plus one maintenance lane per batch
- pairwise/coexistence after local legos are real
- flux remains derived and gated behind lower work

So the queue is not a todo list. It is an ordered admission surface with dependency constraints.

### 2. Truth-bearing objects
The truth audit defines four public labels:
- `exists`
- `runs`
- `passes local rerun`
- `canonical by process`

These act like a bounded status lattice with monotone promotion rules. A stronger label requires new evidence; it is never inherited automatically.

This is one of the most important CS-native readings of the system: state labels are process claims about artifacts, not metaphysical claims about the world.

### 3. Evidence artifacts
Evidence is file-backed and typed. Typical artifact classes are:
- executable probe or engine scripts
- result JSON files
- audit tables in markdown
- backlog rows
- lego catalog and registry rows
- wiki concept pages summarizing current framing

The controller should prefer newer structured result files over stale prose when they disagree. That is a concrete source-precedence rule.

### 4. Maintenance surfaces
Maintenance surfaces are first-class objects because they preserve system state across runs.
Important current surfaces include:
- `system_v5/docs/plans/plans/sim_backlog_matrix.md`
- `system_v5/docs/plans/plans/sim_truth_audit.md`
- `system_v5/docs/plans/plans/tool_integration_maintenance_matrix.md`
- `system_v5/docs/plans/plans/controller_maintenance_checklist.md`
- `system_v5/docs/plans/plans/on-demand-telegram-runner.md`
- `system_v5/docs/16_lego_build_catalog.md`
- `system_v5/docs/17_actual_lego_registry.md`
- current wiki concept pages

In CS terms, these are not comments on the system from the outside. They are part of the controller memory and audit boundary.

## State transitions
The cleanest current-docs reading is that Codex Ratchet allows only bounded state transitions on explicit objects.

Examples:
- queue row: `ready_now -> selected for batch -> audited this run -> next bounded move updated`
- result file: `exists -> runs -> passes local rerun -> canonical by process`
- lego row: `partial -> better specified -> rerun-backed -> ledger/wiki synchronized`
- run health: `healthy | blocked | degraded`
- maintenance closure: `touched -> updated` or `touched -> explicitly queued`

Transitions are guarded by evidence checks, not by narrative summaries. A worker saying something improved is not itself a valid transition.

## Queue semantics
The queue is live, but bounded.

Queue semantics from the source docs behind this snapshot:
- the backlog matrix is the primary live queue surface
- the process gap log is derived diagnostic state, not the primary queue
- the controller chooses the next bounded construction or validation step unless the user overrides
- queue progress means advancing lego completion, lego validation, assembly prerequisite clarity, or engine-readiness gating
- running more sims without moving one of those gates is not queue progress

That makes the queue closer to a dependency-governed work scheduler than to an exploration sandbox.

## Geometry-before-axis as a global ordering constraint
The CS framing should preserve the repo's build-order discipline.

Geometry-before-axis is not just a scientific preference. It functions as a global scheduler constraint:
- do not widen from geometry into axis work
- do not promote bridge or entropy-first claims early
- keep flux as a derived downstream family
- complete lower local geometry/chirality/operator packets before later bridge or axis layers

In program-analysis language, axis work is blocked on unsatisfied upstream dependencies. The controller should enforce that ordering rather than summarize around it.

## Truth labels as process-level types
The four truth labels are best understood as process-level types attached to artifacts.

- `exists`: storage claim only
- `runs`: execution claim
- `passes local rerun`: bounded validation claim
- `canonical by process`: strongest admission claim; requires process compliance, not just success output

This matters because the system explicitly rejects status collapse. The labels do not name subjective confidence. They name distinct verified transition classes.

## Evidence artifacts and provenance
Current docs emphasize that result JSONs, audit rows, and ledgers carry provenance that should survive across sessions.

Useful provenance rules already present in repo docs:
- cite exact files and result paths
- trust newer result artifacts over stale prose when they disagree
- classify wiki pages and docs as current / legacy / supporting / archive when needed
- keep local repo authority above external support surfaces

So the system is not memory-first. It is artifact-first with controller-managed provenance.

## Maintenance surfaces as persistent memory
A developer or LLM can treat the maintenance surfaces as the durable state interface of the controller.

They serve different roles:
- backlog matrix: queue and dependency ordering
- truth audit: public truth-status table
- tool matrix: declared versus load-bearing tool role
- controller checklist: run protocol
- Telegram runner: reporting and liveness protocol
- lego ledgers: grouped and exhaustive object inventories
- wiki pages: current-docs-aligned concept compression for later retrieval

The repo docs explicitly say that docs, ledgers, and wiki should be updated together when material state changes. That is a write-through maintenance rule across persistent state surfaces.

## Nominalist reading
This page should not reify the system into a single closed grand object.

The safer nominalist reading is:
- only bounded objects named in the live surfaces are admitted
- only declared transitions with evidence should be treated as real state change
- higher-level summaries must remain subordinate to file-backed artifacts
- broad bridge or closure claims stay blocked unless their prerequisite objects are already real by process

That keeps the CS framing faithful to the repo's current anti-overclaim discipline.

## Practical reading for developers and LLMs
If you are operating inside this system, the default behavior is:
1. read the live control surfaces first
2. choose one bounded primary lane plus one maintenance lane
3. identify the exact object or gate to move
4. produce file-backed evidence
5. assign only the truth label earned by that evidence
6. patch maintenance surfaces before calling the batch closed

That is the current repo-native notion of progress.

## Related pages
- [[llm-controller-contract]]
- [[specs/codex-ratchet/process-contract-mirror-index]]
- [[specs/codex-ratchet/llm-controller-contract-current]]
- [[controller-state-transition-model]]
- [[current-architecture-core]]
- [[nominalist-cs-framing]]
- [[concurrency-and-trace-theory-reference]]
- [[topos-quantum-mechanics-reference]]
- [[quantum-shannon-theory-reference]]
- [[aligned-sim-backlog-and-build-order]]
- [[sim-build-spine-and-wiki-maintenance]]
- [[constraint-geometry-axis0-separation]]
- [[wiki-as-harness-architecture]]
- [[llm-constraint-harness-wiki]]
