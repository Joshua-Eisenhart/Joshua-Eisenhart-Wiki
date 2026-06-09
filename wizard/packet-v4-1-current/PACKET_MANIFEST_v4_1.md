---
title: Wizard v4.1 Packet Manifest
type: manifest
packet: v4.1
framing: standalone
---

# Packet Manifest v4.1

This folder is a standalone Wizard packet.

## Required Main Boot

FULL mode:

1. `mmm/main/full/md/MMM_MAIN_FULL_v4_1.md`
2. `WIZARD_FULL_v4_1.md`
3. `skills/SKILLS_MANIFEST_v4_1.md`
4. task/source material

COMPACT mode:

1. `mmm/main/compact/md/MMM_MAIN_COMPACT_v4_1.md`
2. `WIZARD_COMPACT_v4_1.md`
3. `skills/SKILLS_MANIFEST_v4_1.md`
4. task/source material

## Required Worker Boot

1. `mmm/mini/MINI_MMM_LOAD_CONTRACT_v4_1.md`
2. assigned full or compact member mini-MMM from `mmm/mini/full/...` or `mmm/mini/compact/...`
3. registry fallback: `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_1.md`
4. assigned task card
5. source slice or tool surface
6. `schemas/RECEIPT_SCHEMA_v4_1.md`

## Required Skill Bindings

- Substantive Codex-adapter Wizard runs load `skills/claude-bridge/SKILL.md` when Claude external-worker capacity is available.
- `failure.premortem_council` loads `skills/premortem/SKILL.md`.
- If that skill path is unavailable, the premortem route is blocked or explicitly degraded; it is not replaced by generic risk analysis.

## Optional Runtime Adapters

- `adapters/CODEX_ADAPTER.md`
- `adapters/CLAUDE_ADAPTER.md`
- `adapters/HERMES_ADAPTER.md`

Load only the adapters for the runtime actually being used.

## Schemas

- `schemas/RECEIPT_SCHEMA_v4_1.md`
- `schemas/COMPILE_GATE_SCHEMA_v4_1.md`

## Definitions And Runtime

- `WIZARD_FULL_v4_1.md`
- `WIZARD_COMPACT_v4_1.md`
- `definitions/MEMBER_DEFINITIONS_v4_1.md`
- `00_BOOT.md`
- `01_UNIVERSAL_THREE_COUNCIL_WIZARD.md`
- `02_MEMBER_REGISTRY_AND_MINI_MMMS.md`
- `03_RECEIPTS_AND_COMPILE_GATES.md`
- `04_FOLLOW_UP_COUNCIL.md`
- `05_RUN_PROTOCOL_AND_RETRY.md`
- `06_OUTPUT_FORMAT_AND_SCORING.md`
- `07_TASK_CARDS.md`
- `taskcards/CHILD_TASK_CARDS_v4_1.md`
- `08_EXAMPLE_OUTPUT.md`
- `09_CONFORMANCE_HARNESS.md`
- `conformance/validate_loop_contract_fixtures.py`
- `conformance/fixtures/loop_contract_fixtures_v4_1.json`
- `conformance/fixtures/sample_cross_loop_ledger_v4_1.json`
- `conformance/fixtures/stale_mirror/premortem/SKILL.md`
- `10_DELIBERATOR_CONTRACT.md`

The split docs are source docs for the compiled runnable FULL file, not deleted
or deprecated.

## Salience

- `mmm/FULL_MMM_v4_1.md`
- `mmm/COMPACT_MMM_v4_1.md`
- `mmm/main/full/`
- `mmm/main/compact/`
- `mmm/mini/full/`
- `mmm/mini/compact/`
- `mmm/mini/MINI_MMM_LOAD_CONTRACT_v4_1.md`
- `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_1.md`
- `taskcards/CHILD_TASK_CARDS_v4_1.md`
- `skills/SKILLS_MANIFEST_v4_1.md`
- `skills/claude-bridge/SKILL.md`
- `skills/premortem/SKILL.md`
- `skills/council-members/`

MMMs and mini-MMMs are salience surfaces. They are not deterministic rules.
