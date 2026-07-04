---
title: Wizard Agent Adapters
created: 2026-04-28
updated: 2026-04-30
type: concept
tags: [wizard, adapter, multi-agent, controller, bridge, provenance]
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Wizard Agent Adapters

The wiki is the universal source. Claude, Codex, Hermes, and later systems should derive runtime adapters from it instead of copying one another's files.

## Derivation Layers

- L0 universal source: [[wizard/README]], [[wizard/01-wizard-general]], [[wizard/02-mmm-reference]], [[wizard/03-followups-and-compositions]], and [[wizard/05-validation-gates]].
- L1 neutral adapter contract: the fields a runtime must map, such as route category, receipt shape, boot order, and MMM loading.
- L2 runtime adapter: the actual local file or prompt surface used by Claude, Codex, Hermes, or another agent.

Runtime adapters may inject spawn syntax, model routing, memory paths, verbosity rules, and UI conventions. Those injections must be extension points, not edits to the universal source.

## Shared Invariants

- Single source: wiki universal pages define the contract.
- Single-writer namespaces: agents do not write each other's memory folders.
- Receipt truth: every visible route is `spawned`, `blocked`, `deferred`, or `simulated`.
- Boot order: positive harness and MMM context arrives before task work.
- Status honesty: derived adapters are labeled derived, not canonical.

## Claude

Claude adapters can use prose-heavy surfaces, external Opus calls, and session receipts. Opus is advisory in this Codex workflow: it can suggest and audit, but Codex accepts, rejects, or edits before durable wiki writes.

## Codex

Codex adapters should prefer explicit receipt artifacts, local validation, and final synthesis that distinguishes external oracle suggestions from Codex-accepted changes. Codex can use native subagents and Claude Bridge together, but it should not count a controller-local Opus synthesis as worker plurality.

## Hermes

Hermes adapters should preserve wiki-style spine prose, wikilinks, and evidence-status hedges. Hermes may tune the voice, but it should not mutate the universal Wizard reference to match Hermes surface style.

## Bridge Rule

External model bridges are system routes. They return receipts. They do not become native subagents, and they do not get write authority over the wiki unless the controlling agent applies and verifies the change.

## Adapter Rule

Adapters are derived, not authoritative. If Claude, Codex, Hermes, or another runtime needs a shorter surface, it can compile one from the wiki. That compiled surface must name what it omitted and where the full reference lives.

## Adapter Responsibilities

Every adapter should define which wiki pages it reads, which MMM or mini-MMM files it loads, how it records route receipts, how it distinguishes spawned/blocked/deferred/simulated work, how external model advice is marked advisory, how follow-up options are rendered, where proof/graph/sim receipts are stored, and what counts as live behavior proof.

## Codex Adapter Shape

Codex should treat local scripts and native subagents differently. A local script can validate structure, copy files, package zips, and run proof gates. Native subagents can explore or implement bounded slices. Neither one automatically proves that a future Claude or Hermes boot will behave the same way.

Codex may use Opus through the Claude bridge as an external advisory route. That route is useful only when the receipt is archived and Codex makes an explicit accept/reject decision.

## Adapter Failure Modes

Adapters fail when they shorten the full bank into tiny labels, hide route categories, call controller-local headings a multi-agent wave, load raw negative examples into positive boot, treat external advice as accepted text, or write runtime-specific paths into the universal wiki.

Adapter success means the runtime can produce the full Wizard shape when asked and a shorter honest shape when the task is small.
