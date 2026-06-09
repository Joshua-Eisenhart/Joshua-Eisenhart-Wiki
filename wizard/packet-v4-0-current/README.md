---
title: Wizard v4.0 Packet
type: packet_readme
packet: v4.0
framing: standalone
---

# Wizard v4.0 Packet

This is a standalone Wizard packet.

It is meant to be portable: copy this folder to another model, runtime, team, or knowledge base and use it without any outside packet dependency.

## What This System Does

The Wizard is a bounded-work compiler.

It uses three sequential councils:

1. Decision Council: choose the smallest useful bounded move.
2. Failure Council: stress, falsify, harden, split, block, or kill that move.
3. Follow-Up Council: create executable next prompts and options.

The system uses MMMs and mini-MMMs as salience: they make the right language, distinctions, and reasoning moves more available. They are not deterministic rules.

## Boot Order

For a new main thread:

1. Load `mmm/FULL_MMM_v4_0.md`.
2. Load `00_BOOT.md`.
3. Load `01_UNIVERSAL_THREE_COUNCIL_WIZARD.md`.
4. Load the task and source material.
5. Load adapter docs only for the runtime actually being used.

For subagents and subsubagents:

1. Load the assigned mini-MMM slice from `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_0.md`.
2. Load the assigned route/member task card.
3. Load the source slice or tool surface.
4. Load the receipt format from `schemas/RECEIPT_SCHEMA_v4_0.md`.

## File Map

- `00_BOOT.md`: load order, runtime boundaries, route truth.
- `01_UNIVERSAL_THREE_COUNCIL_WIZARD.md`: portable universal model.
- `02_MEMBER_REGISTRY_AND_MINI_MMMS.md`: member families and route-local salience.
- `03_RECEIPTS_AND_COMPILE_GATES.md`: receipt truth, bounded-work gate, sim/profile gates.
- `04_FOLLOW_UP_COUNCIL.md`: follow-up generation and composition options.
- `05_RUN_PROTOCOL_AND_RETRY.md`: full/partial run minimums, retries, liveness.
- `06_OUTPUT_FORMAT_AND_SCORING.md`: readable output shape, council notation, score.
- `07_TASK_CARDS.md`: bounded parent, child, compile-gate, and reroute cards.
- `08_EXAMPLE_OUTPUT.md`: example of properly formatted output.
- `09_CONFORMANCE_HARNESS.md`: fixture-backed acceptance checks.
- `mmm/FULL_MMM_v4_0.md`: full main-thread salience pack.
- `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_0.md`: route/member mini-MMM slices.
- `definitions/MEMBER_DEFINITIONS_v4_0.md`: definitions for every member.
- `schemas/RECEIPT_SCHEMA_v4_0.md`: portable receipt schema.
- `schemas/COMPILE_GATE_SCHEMA_v4_0.md`: universal and adapter compile gates.
- `adapters/CODEX_ADAPTER.md`: Codex runtime binding.
- `adapters/CLAUDE_ADAPTER.md`: Claude runtime binding.
- `adapters/HERMES_ADAPTER.md`: Hermes memory/process binding.

## Portability Rule

This packet should not require outside packet files. Adapters may point to local runtime tools or memory systems, but those are runtime bindings, not universal requirements.

## Acceptance Rule

Do not treat the packet as runnable just because the docs are present. A runtime should have a conformance harness or equivalent checks for boot order, receipt truth, compile gate separation, and answer-first output.
