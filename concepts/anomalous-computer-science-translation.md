---
title: Anomalous Computer Science Translation
created: 2026-04-11
updated: 2026-05-19
type: concept
tags: [translation, computer-science, state-machine, compiler, harness, validation]
sources:
  - system_v5/docs/ANOMALOUS_COMPUTER_SCIENCE_TRANSLATION.md
---

# Anomalous Computer Science Translation

## Overview
This translation layer restates the project's internal terminology in explicit computer-science terms. It ensures that both the wiki, human developers, and LLM worker agents can reason about the system's operational graph without flattening it into vague, high-entropy philosophical or theoretical prose.

## Role in the Live Wiki Cluster
*   **Strongest Use:** Bridge document that maps project-local domain language (such as *lego*, *probe*, *sim*, *harness*, *maintenance surface*) directly to industry-standard software engineering and compiler-design concepts.
*   **Weak Use:** Theoretical physics proof or mathematical carrier derivation.
*   **Authority Boundary:** Repo-facing translation layer. It does not replace the native repository ontology, but serves as a machine-readable explanation of how the system operates as a constrained execution environment.

---

## One-Sentence Translation
> **Codex Ratchet is an LLM-guided research compiler and verification harness that turns high-entropy source material into explicit testable objects, runs bounded local executables against them, records evidence, and updates persistent state only when the evidence changes what is honestly claimable.**

---

## System Translation Table

| Repo Term | Computer-Science Translation | Practical Meaning |
| :--- | :--- | :--- |
| **lego** | Primitive typed unit | Smallest local object worth building or testing (such as a single-function probe). |
| **candidate** | Provisional object | Proposed unit or claim not yet promoted by execution evidence. |
| **probe / sim** | Executable verification function | Bounded run (Python/z3/CVC5) that tests one specific object or relation. |
| **result artifact** | Machine output record | JSON/log/audit emitted by execution (e.g. `results/*.json`). |
| **registry / ledger row** | Materialized state view | Persistent, structured projection of current object status. |
| **queue item** | Scheduled transition request | Next allowed move with explicit prerequisites, inputs, and outputs. |
| **truth label** | Verification state | Explicit claim level (e.g., `exists` < `runs` < `passes local rerun` < `canonical by process`). |
| **maintenance surface** | Derived cache / projection | Documents or indexes that must stay synchronized after evidence changes. |
| **shell-local** | Single-node / single-module scope | Object tested in isolation (pre-lego or pre-coupling). |
| **pairwise / coexistence** | Interaction-level test | Compatibility or coupling between already-realized local objects. |
| **bridge claim** | High-order integration claim | Cross-object or cross-layer assertion that must be deferred until late in the build order. |

---

## The System as a Compiler Pipeline

In computer-science terms, the repository functions less like a passive text notebook and more like a seven-stage compiler and verification pipeline:

1.  **Source Ingestion:** Parsing high-entropy, raw text or PDFs into discrete segments.
2.  **Object Normalization:** Translating raw assertions into structured, typed candidate files.
3.  **Dependency Resolution:** Analyzing prerequisite topological and promotion orders (the build order).
4.  **Bounded Execution:** Running automated scripts (e.g., Python simulations, SMT solvers) in isolated environments.
5.  **Evidence Capture:** Generating JSON metadata and log outputs detailing the execution path.
6.  **State Classification:** Verifying results against the strict truth-label hierarchy.
7.  **Projection & Maintenance Update:** Rebuilding downstream indexes, routers, and map pages to synchronize the derived state.

---

## The System as a State Machine

The core object lifecycle is strictly governed by state transitions:

```text
  [Source Fragment] ──► [Normalized Object] ──► [Queued Target] ──► [Executed Probe]
                                                                          │
  [Successor State] ◄── [Registry Update]  ◄── [Evidence Status] ◄────────┘
```

### Prohibited Transitions
To prevent systemic drift and overclaiming, the scheduler/controller must automatically reject invalid transitions, including:
*   **Prose claim without execution evidence:** Promoting a theory page without citing an active on-disk result JSON.
*   **Bridge promotion before local-object validation:** Asserting high-level integration before the primitive legos have achieved `passes local rerun` status.
*   **Status inflation:** Upgrading an object from `exists` to `passes local rerun` without executing an in-session verification run.
*   **Queue motion without an artifact path:** Advancing a queue transition without recording the exact file path of the generated evidence.

---

## The System as an LLM Harness

To operate reliably, LLM agents (such as Codex, Claude Code, or subagents spawned via `delegate_task`) must be treated as execution components inside a highly constrained harness:

*   **Inputs:** Raw source documents, legacy notes, registries, and existing result JSONs.
*   **Controller:** The orchestrator that schedules and executes a single, bounded object transition.
*   **Workers:** LLM instances assigned to perform narrow, sandboxed tasks with concrete exit criteria.
*   **Validators:** Automated testing scripts, local reruns, and schema audits.
*   **Artifacts:** Generated result files, updated registers, and patched code blocks.
*   **Closeout:** Final status-label classification paired with immediate maintenance updates.

The LLM is highly effective when constrained to orchestrate within this execution loop; it fails when allowed to behave as a free-form, unverified summarizer.

---

## Translation Rules for Wiki Authors

When drafting or editing wiki documentation, authors must actively translate project-local jargon into industry-standard CS terminology:

*   *"lego"* ──► primitive object, bounded unit, local executable target.
*   *"build order"* ──► dependency order, topological order, promotion order.
*   *"truth audit"* ──► consistency check between claims and on-disk execution artifacts.
*   *"maintenance surface"* ──► derived state view that must stay synchronized.
*   *"controller"* ──► scheduler and state-transition manager.
*   *"bridge"* ──► higher-order integration layer.

Pairing project-native terms with their computer-science equivalents ensures both human readers and autonomous models interpret the requirements with absolute clarity.

---

## Related Pages
*   [[nominalist-cs-framing]] ── the core nominalist computational discipline.
*   [[nominalist-cs-jp-systems-bridge]] ── translation of Jordan Peterson's archetypal vocabulary.
*   [[llm-controller-contract]] ── the status-label and verification protocol.
*   [[enforcement-and-process-rules]] ── compiler build-order constraints.
*   [[anti-reification-and-nominalism-reference]] ── classical nominalist roots.
