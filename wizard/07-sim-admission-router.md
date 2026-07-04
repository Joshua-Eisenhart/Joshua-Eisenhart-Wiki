---
title: Wizard Sim Admission Router
created: 2026-04-28
updated: 2026-04-28
type: concept
tags: [wizard, simulation, validation, qit, queue, receipt, status]
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Wizard Sim Admission Router

The Wizard helps build sims by routing proposals into admission decisions. It should not simply describe why a sim failed. It should decide the next bounded move: rerun, repair, downgrade, promote, archive, or turn into a proof/graph check.

## Status Ladder

Use the wiki ladder:

`exists < runs < passes local rerun < canonical by process`

Never skip a rung. A sim that exists but has no current receipt is not a result. A sim that runs once but lacks a negative battery is not canonical. A sim with a graph proof can earn a local witness without proving the full engine.

## Admission Decisions

- `rerun`: the artifact is plausible, but the receipt is stale, missing, or too narrow.
- `repair`: the sim has a local bug, missing dependency, bad fixture, or unclear acceptance check.
- `downgrade`: the artifact overclaims; keep it as toy, Tier D, or hypothesis support.
- `promote`: local rerun and gate evidence support the next status rung.
- `archive`: the sim is superseded, duplicate, or irreparable without new theory.
- `translate`: the idea belongs in a proof, graph, or smaller harness test before simulation.

## Required Receipt Fields

Every sim admission receipt should name:

- source file or page
- current status
- command or harness that ran
- pass/fail result
- claim ceiling
- missing negative battery
- next artifact
- owner-visible follow-up route

## Skip-Ahead Guard

Block promotion when:

- a sim result is only copied from old logs
- a proof tool is mentioned but not run
- graph evidence is structural only but the claim says engine-level alignment
- a large QIT claim relies on a toy or proxy probe
- the Wizard uses voice agreement instead of executable evidence

## Build Preference

Prefer the smallest witness that can survive rerun. For QIT engines, the useful next move is often a narrow proof/graph/sim receipt, not a larger prose synthesis.

## Routing Examples

If a sim exists but has no current receipt, route to `rerun`.

If a sim produces a result but the acceptance check is unclear, route to `repair`.

If a sim is toy-scale but described with engine-scale language, route to `downgrade`.

If a proof gate can check the core claim more cleanly than a large sim, route to `translate`.

If a graph check supports ordering but not full engine behavior, route to `promote` only at the graph-structure claim ceiling.

If a result depends on a missing tool integration, route to `repair` or `blocked`, not `promote`.

## Wizard Output For Sim Admission

A sim admission answer should contain current file or page, current status label, admission decision, exact command or gate, claim ceiling, falsifier, next artifact, and follow-up composition.

This keeps the Wizard from turning sim work into commentary.
