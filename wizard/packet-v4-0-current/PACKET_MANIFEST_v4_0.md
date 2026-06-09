---
title: Wizard v4.0 Packet Manifest
type: manifest
packet: v4.0
framing: standalone
---

# Packet Manifest v4.0

This folder is a standalone Wizard packet.

## Required Main Boot

1. `mmm/FULL_MMM_v4_0.md`
2. `00_BOOT.md`
3. `01_UNIVERSAL_THREE_COUNCIL_WIZARD.md`
4. `03_RECEIPTS_AND_COMPILE_GATES.md`
5. `04_FOLLOW_UP_COUNCIL.md`
6. `05_RUN_PROTOCOL_AND_RETRY.md`
7. `06_OUTPUT_FORMAT_AND_SCORING.md`
8. `09_CONFORMANCE_HARNESS.md`

## Required Worker Boot

1. `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_0.md`
2. assigned member slice
3. assigned task card
4. source slice or tool surface
5. `schemas/RECEIPT_SCHEMA_v4_0.md`

## Optional Runtime Adapters

- `adapters/CODEX_ADAPTER.md`
- `adapters/CLAUDE_ADAPTER.md`
- `adapters/HERMES_ADAPTER.md`

Load only the adapters for the runtime actually being used.

## Schemas

- `schemas/RECEIPT_SCHEMA_v4_0.md`
- `schemas/COMPILE_GATE_SCHEMA_v4_0.md`

## Definitions And Runtime

- `definitions/MEMBER_DEFINITIONS_v4_0.md`
- `07_TASK_CARDS.md`
- `08_EXAMPLE_OUTPUT.md`
- `09_CONFORMANCE_HARNESS.md`

## Salience

- `mmm/FULL_MMM_v4_0.md`
- `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_0.md`

MMMs and mini-MMMs are salience surfaces. They are not deterministic rules.
