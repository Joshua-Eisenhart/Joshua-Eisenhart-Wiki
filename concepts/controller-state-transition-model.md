---
title: Controller State Transition Model
created: 2026-04-11
updated: 2026-05-21
type: concept
framing: conceptual_controller_model_snapshot
tags: [controller, workflow, planning, validation, maintenance]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/EXPLICIT_CONTROLLER_MODEL.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/sim_backlog_matrix.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/sim_truth_audit.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/tool_integration_maintenance_matrix.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/controller_maintenance_checklist.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/on-demand-telegram-runner.md
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/process-contract-mirror-index.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/llm-controller-contract-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/enforcement-process-rules-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/lego-sim-contract-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/formal-scout-readiness-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
---

# Controller State Transition Model

## Role in the live wiki cluster
- Strongest use: controller-facing bridge page for the repo's bounded object-transition model after the `hermes-current/` spine and the immediate controller contract surfaces have already been loaded.
- Weak use: first-stop front door for the whole wiki, or substitute for the repo's live truth/queue/tool/checklist surfaces themselves.
- Authority boundary: this page explains the controller/state-transition model and how the live repo surfaces divide labor; it does not outrank `hermes-current/` for entry behavior, and it does not replace fresh repo artifacts or `sim_truth_audit.md` when the question is the strongest safe current label.
- Current status boundary: use [[specs/codex-ratchet/process-contract-mirror-index|process-contract-mirror-index]], [[specs/codex-ratchet/llm-controller-contract-current|llm-controller-contract-current]], [[specs/codex-ratchet/formal-scout-readiness-status|formal-scout-readiness-status]], and [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]] for current wiki-side routing.

## Recommended reading order
1. `hermes-current/read-first.md` and the rest of the `hermes-current/` spine
2. `projects/codex-ratchet/read-first.md`
3. `system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md`
4. `system_v5/docs/LLM_CONTROLLER_CONTRACT.md`
5. this page when the task is specifically about controller object transitions, queue/truth/tool/closeout division of labor, or maintenance closure semantics
6. the live operational repo surfaces named below for the actual current queue/truth/tool/run state

## Purpose
This page is the bounded bridge between the repo's explicit controller framing and the live operational surfaces.

The key separation is:
- conceptual authority explains what the controller is and what kinds of state transitions are allowed
- live operational surfaces record what is currently queued, what is currently true, which tools are actually load-bearing, and what maintenance closure is still required
- the automated sim runner is only one runtime surface inside that controller stack, while the wiki-builder path is a separate maintenance/synchronization path over ledgers and `/Users/joshuaeisenhart/wiki`

Do not treat those as interchangeable.

## The core model in one sentence
The controller is a state-transition manager for bounded research objects, not a prose summarizer and not a generic sim runner.

Its job is to move one explicit object through the next honest transition, demand evidence for that move, then repair the queue/truth/tool/maintenance projections that depend on that evidence.

## What the controller is actually controlling
Per the explicit model, the controller is controlling state rather than documents. In practice that means five distinct surfaces:

1. queue state
- what bounded object is allowed to move next
- live surface: `system_v5/docs/plans/plans/sim_backlog_matrix.md`

2. evidence and truth-label state
- what was actually run, rerun, falsified, or still only exists on disk
- live surface: `system_v5/docs/plans/plans/sim_truth_audit.md`

3. tool-depth state
- which tools are merely installed or imported versus genuinely load-bearing in the current lane
- live surface: `system_v5/docs/plans/plans/tool_integration_maintenance_matrix.md`

4. run-operations state
- whether a bounded run was prepared, launched, monitored, audited, and closed correctly
- live surface: `system_v5/docs/plans/plans/controller_maintenance_checklist.md`

5. maintenance state
- which ledgers, registries, docs, and wiki pages became stale because evidence changed
- distributed across the four live surfaces above plus the lego catalog/registry and touched wiki pages

The explicit controller model is the authority on how to think about these surfaces. The live docs are the authority on current operational status inside each surface.

## Memory-facing clarification
The controller should also keep one storage split explicit:
- durable user/environment facts belong in Hermes memory
- session-specific work history belongs in session recall
- durable project structure belongs in the wiki
- exact truth claims belong in repo artifacts and live operational docs

See [[hermes-memory-and-wiki-roles]] for the compact storage rule. This matters because a controller that treats chat memory, wiki summaries, and result artifacts as interchangeable will drift even if its queue logic is otherwise correct.

## Public truth labels vs implementation detail
The public controller contract still uses only four safe status labels:
- `exists`
- `runs`
- `passes local rerun`
- `canonical by process`

Keep those four labels primary on controller-facing wiki pages.

Separate claim-state ladder:
- `proven` for narrower claims that have survived the right evidence gate
- `candidate` for live but still testable interpretations
- `open` for materially unsettled questions
- `snapshot-labeled` for dated audit/state statements that should not be silently refreshed into timeless truth

Implementation or closeout tooling may still expose extra internal vocabulary such as `proof-backed` or older `runs locally` wording in specific repo scripts, checklists, or machine-readable gap/validator surfaces. Treat those as implementation-detail or local closeout schema, not as replacements for the public four-label reporting spine unless the repo's public controller contract itself changes.

Practical reading rule:
- when this page summarizes controller state, report the public four-label contract first
- if an implementation surface uses extra terms, name them explicitly as tool/detail vocabulary rather than silently blending them into the main controller status ladder
- if a repo artifact and a summary disagree, the fresher artifact wins, but the summary should still translate back into the public four-label contract where possible

## Conceptual authority vs live operational authority

### Conceptual authority
`system_v5/docs/EXPLICIT_CONTROLLER_MODEL.md` defines:
- the unit of work: one bounded candidate or lego transition
- core objects: lego, candidate, probe/sim, result artifact, evidence record, queue item, registry row, maintenance surface
- allowed transitions
- prohibited shortcuts
- the evidence hierarchy

This is the stable framing doc. It says what kinds of moves are legitimate.

### Live operational authority
The `system_v5/docs/plans/plans/` surfaces answer different questions:

- `sim_backlog_matrix.md`: what should move next
- `sim_truth_audit.md`: what can be claimed honestly right now
- `tool_integration_maintenance_matrix.md`: which tools are truly carrying weight in the current build
- `controller_maintenance_checklist.md`: what the controller must do before, during, and after a run so the run counts as real progress

These docs should be read as materialized views over current repo state, not as abstract philosophy.

## The runtime object model
The controller model becomes concrete when the main objects are kept separate:

- lego: the default local construction unit
- candidate: a proposed object/relation not yet earned as process-canonical
- probe or sim: one bounded execution against one object or narrow relation
- result artifact: the machine-readable output from that bounded execution
- evidence record: the cited path-level support for a claim
- queue item: the next allowed bounded move
- registry/ledger row: a persistent summary projection, never the primary evidence itself
- maintenance surface: any document or machine ledger that must be updated when evidence changes

This matters because many repo errors come from collapsing these layers, for example:
- treating a registry row as evidence
- treating result-file existence as rerun success
- treating tool installation as tool-depth proof
- treating a completed run as closed before maintenance surfaces are repaired

## Allowed state-transition chain
The explicit controller model gives the current bounded transition vocabulary. In developer terms, the normal flow is:

This can be read as a typed transition system rather than workflow prose. Each node is a bounded object-state, each edge is guarded by a specific evidence condition, and illegal edge-skips are exactly the failure mode the repo keeps calling out when docs get ahead of reruns.

1. source material -> normalized object
- extract one concrete lego/candidate from mixed prose or bundled rows

2. normalized object -> queued build target
- name the exact bounded probe, dependency, expected artifact, and verify step

3. queued build target -> fresh evidence
- run the bounded probe and produce a path-citable artifact

4. fresh evidence -> truth label
- classify only as strongly as the evidence warrants

5. truth label -> registry/ledger/queue maintenance
- patch backlog, truth audit, registry rows, tool-depth notes, and stale prose as needed

6. local lego -> bounded successor
- only after the lower object is real enough, promote to pairwise/coexistence or another higher bounded move

The important discipline is that every arrow has its own admission gate. No transition should be skipped just because the narrative feels plausible.

## Relation to concurrency and contextual semantics

This page sits naturally beside two other CS-native references:
- [[concurrency-and-trace-theory-reference]] explains why order-sensitive transitions should not be quotiented away when they are load-bearing
- [[topos-quantum-mechanics-reference]] gives a context-sensitive truth analogy for why stronger claims cannot be flattened across incomparable evaluation contexts

Those references do not replace the controller model, but they sharpen it. The controller is effectively maintaining a guarded transition system over typed artifacts, with context-sensitive promotion rules and explicit forbidden shortcuts.

## How the live surfaces map onto the transition chain

### 1. Queue surface: `sim_backlog_matrix.md`
This is the live answer to: what bounded move is currently worth doing?

Current structure:
- Lane A: classical engine baseline work
- Lane B: geometry-manifold spine
- Lane C: maintenance/control surfaces

This page is not truth authority by itself. It is queue authority. It should only contain tasks that can plausibly produce an artifact or clear a real blocker.

Practical reading rule:
- use it to choose the next move
- do not use it to infer that the move has already run or passed

### 2. Truth surface: `sim_truth_audit.md`
This is the live answer to: what status label is currently justified for key files?

The current four public labels remain:
- `exists`
- `runs`
- `passes local rerun`
- `canonical by process`

This page is where status collapse is prevented. It explicitly separates file presence, execution success, rerun-backed passing status, and process-canonical promotion.

Practical reading rule:
- if a result file exists but has not been freshly rerun, the truth surface may still keep rerun status as unknown
- if prose and the truth audit disagree, the fresher evidence-backed truth surface wins

### 3. Tool-depth surface: `tool_integration_maintenance_matrix.md`
This is the live answer to: which tools are actually carrying load in the present build and where are the shallow spots?

It prevents another common collapse:
- imported tool != used tool
- used tool != load-bearing tool
- one strong tool anchor != lane completion

Practical reading rule:
- use it when deciding whether a claim type has the right proof/geometry/graph/topology pressure
- update it when a tool becomes newly load-bearing or regresses to decorative use

### 4. Run-operations surface: `controller_maintenance_checklist.md`
This is the live answer to: did the controller run the batch correctly as an operational process?

It governs:
- pre-run scoping
- launch discipline
- heartbeat and health checks
- post-run audit and closeout
- maintenance closure obligations

Practical reading rule:
- a run is not complete just because the worker stopped
- completion requires verification, truth labeling, and either maintenance updates or an explicit queued follow-up

## Real progress under this model
A run counts as real progress only if at least one bounded state actually changed. In current repo terms, that usually means one of the following happened:

This is why the controller should be read as an artifact-state machine rather than as a chat agent with a memory. Progress is not more narration. Progress is a legal state transition with surviving evidence and repaired downstream projections.

- a vague bundled object became an explicit row with a named probe target
- a queued item gained a real execution path
- a bounded rerun changed the safe truth label
- a tool moved from shallow/decorative to load-bearing in a relevant lane
- a stale backlog/truth/tool/registry/wiki surface was corrected to match fresh evidence
- a local lego became strong enough to feed one bounded successor

What does not count by itself:
- broad reading
- controller narration
- wiki growth without queue or truth consequences
- more sims run without a named object transition

## Queue semantics and noncommuting work

Not every next action commutes with every other. The repo's geometry-before-axis rule, shell-local-before-coexistence rule, and truth-before-doc-promotion rule together induce a partial order on legal work. In CS terms:
- some tasks are independent and can be parallelized safely
- some tasks are dependent and must remain ordered
- some transitions are blocked until a predecessor produces an artifact with the required label

That is why this page pairs well with [[concurrency-and-trace-theory-reference]]. A queue is not just a list; it is an admissible execution order over typed objects.

## The main anti-collapses this page is meant to preserve

1. concept vs operation
- explicit controller model explains the system
- live docs report current queue/truth/tool/run state

2. evidence vs projection
- result artifacts and reruns are primary evidence
- ledgers, matrices, and concept pages are projections of that evidence

3. queue vs truth
- being next in the queue does not imply the item is true or complete

4. tool presence vs tool depth
- installed/imported/mentioned does not equal load-bearing

5. execution vs closure
- a run that produced files but did not update or queue maintenance closure is operationally incomplete

## Developer reading order
When touching controller-facing work, use this order:

1. `system_v5/docs/EXPLICIT_CONTROLLER_MODEL.md`
- understand the allowed unit of work and transition discipline

2. `system_v5/docs/plans/plans/sim_backlog_matrix.md`
- identify the active bounded move

3. `system_v5/docs/plans/plans/sim_truth_audit.md`
- check the strongest safe current claim for the target object/result

4. `system_v5/docs/plans/plans/tool_integration_maintenance_matrix.md`
- confirm the tool-depth expectations for the claim type and lane

5. `system_v5/docs/plans/plans/controller_maintenance_checklist.md`
- execute the run and closeout without leaving maintenance drift behind

## Bottom line
The repo now has a cleaner split between controller ontology and controller operations.

- `EXPLICIT_CONTROLLER_MODEL.md` is the conceptual authority for the controller/state-transition model
- `sim_backlog_matrix.md` is the live queue surface
- `sim_truth_audit.md` is the live truth-status surface
- `tool_integration_maintenance_matrix.md` is the live tool-depth surface
- `controller_maintenance_checklist.md` is the live run-operations surface
- `on-demand-telegram-runner.md` is the live liveness/reporting surface for launch, heartbeat, and closeout behavior

The controller succeeds when it moves one bounded object through the next honest state transition and then keeps every affected operational surface aligned with that new evidence.

## Related pages
- [[llm-controller-contract]]
- [[specs/codex-ratchet/process-contract-mirror-index]]
- [[specs/codex-ratchet/llm-controller-contract-current]]
- [[specs/codex-ratchet/lego-sim-contract-current]]
- [[codex-ratchet-cs-bounded-system-framing]]
- [[nominalist-cs-framing]]
- [[concurrency-and-trace-theory-reference]]
- [[topos-quantum-mechanics-reference]]
- [[quantum-shannon-theory-reference]]
- [[aligned-sim-backlog-and-build-order]]
- [[sim-build-spine-and-wiki-maintenance]]
- [[tool-manifest-audit]]
- [[tooling-status]]
- [[agent-workflow-and-boot-architecture]]
- [[repo-mediated-multi-agent-workflow]]
