---
title: Source and Lift Boundary
type: boundary
runtime: hermes
created: 2026-05-04
updated: 2026-05-04
---

# Source and Lift Boundary

This file prevents the main failure mode: copying the general Wizard or Codex style and mistaking that copy for a Hermes-native runtime.

## Definitions

- `source`: a file, tool output, memory entry, session summary, receipt, or worker result read in the current run.
- `lift`: the design move extracted from a source for Hermes use.
- `execution`: a current tool/worker/process action that actually ran.
- `proof`: a receipt plus controller reread that supports a scoped claim.

## Rules

1. A source can inspire a Hermes mechanism.
2. A source does not prove the mechanism runs in Hermes.
3. A lift must name what changed when adapted to Hermes.
4. A copied packet path is not a Hermes-native route.
5. Style transfer is not runtime integration.
6. Memory/session recall can locate prior decisions, not prove current execution.
7. A worker summary can suggest a change; controller verification decides adoption.

## Required source-and-lift fields

For each imported mechanism:

- source file/path
- source role
- source mechanism
- Hermes lift
- what Hermes changes
- what remains unproved
- adoption status: proposed / drafted / proved / adopted / rejected

## Label-strip test

Remove labels like Wizard, Council, Hume, Codex, Max Assembly, lane, voice, and MMM.

If the remaining behavior no longer has:

- a bounded target;
- a current evidence path;
- a success check;
- a stop condition;
- and a next move;

then it was decorative lift, not a real Hermes mechanism.

## Copy rejection test

Reject an import when it depends on:

- Codex native `spawn_agent` proof;
- Codex Ratchet sim stage gates for ordinary Hermes work;
- a fixed external model family quorum;
- v4.1 header/scoring ceremony as the visible surface;
- universal packet paths as Hermes authority;
- high-fanout stress capacity as default behavior.
