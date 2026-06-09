---
title: Wizard v4.1 Packet
type: packet_readme
packet: v4.1
framing: standalone
---

# Wizard v4.1 Packet

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

1. Load the main MMM for the chosen mode:
   - FULL: `mmm/main/full/md/MMM_MAIN_FULL_v4_1.md`
   - COMPACT: `mmm/main/compact/md/MMM_MAIN_COMPACT_v4_1.md`
2. Load the matching runnable Wizard document:
   - FULL: `WIZARD_FULL_v4_1.md`
   - COMPACT: `WIZARD_COMPACT_v4_1.md`
3. Load `skills/SKILLS_MANIFEST_v4_1.md`.
4. Load the task and source material.
5. Load adapter docs only when the active runtime needs them.
6. For substantive Codex-adapter Wizard work, load `skills/claude-bridge/SKILL.md` and `skills/premortem/SKILL.md`.

For subagents and subsubagents:

1. Load the assigned full or compact mini-MMM slice from `mmm/mini/full/...` or `mmm/mini/compact/...`, using `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_1.md` as the registry fallback.
2. Load the assigned route/member task card.
3. Load the source slice or tool surface.
4. Load the receipt format from `schemas/RECEIPT_SCHEMA_v4_1.md`.

For `failure.premortem_council` in Codex runtimes:

1. Load `skills/premortem/SKILL.md`.
2. Run the Premortem skill workflow inside the Failure Council route.
3. Record skill load status and premortem evidence in the receipt.
4. Do not create reports, transcripts, HTML, or open a browser.

For Claude external-worker routes in Codex runtimes:

1. Load `skills/claude-bridge/SKILL.md`.
2. Use packet-local wrappers under `skills/claude-bridge/scripts/`.
3. Count only completed receipt-backed Claude outputs.

## File Map

- `WIZARD_FULL_v4_1.md`: primary full runnable Wizard document with embedded definitions.
- `WIZARD_COMPACT_v4_1.md`: primary compact runnable Wizard document with embedded definitions.
- `skills/SKILLS_MANIFEST_v4_1.md`: local skill index and load rules.
- `skills/claude-bridge/SKILL.md`: local Claude external-worker bridge.
- `skills/premortem/SKILL.md`: local Premortem skill used by `failure.premortem_council`.
- `skills/council-members/`: portable wiki-hosted council-member skills for runtime mirrors.
- `mmm/README.md`: required MMM directory index and boot reminder.
- `mmm/FULL_MMM_v4_1.md`: full main-thread salience pack.
- `mmm/COMPACT_MMM_v4_1.md`: compact main-thread salience pack.
- `mmm/main/full/`: versioned full main MMM source files.
- `mmm/main/compact/`: versioned compact main MMM source files.
- `mmm/mini/full/`: full route/member mini-MMM files.
- `mmm/mini/compact/`: compact route/member mini-MMM files.
- `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_1.md`: route/member mini-MMM slices.
- `mmm/mini/MINI_MMM_LOAD_CONTRACT_v4_1.md`: worker mini-MMM load order and fallback rules.
- `definitions/MEMBER_DEFINITIONS_v4_1.md`: definitions for every member.
- `schemas/RECEIPT_SCHEMA_v4_1.md`: portable receipt schema.
- `schemas/COMPILE_GATE_SCHEMA_v4_1.md`: universal and adapter compile gates.
- `taskcards/CHILD_TASK_CARDS_v4_1.md`: formal child task-card defaults for parent-launched children.
- `adapters/CODEX_ADAPTER.md`: Codex runtime binding.
- `adapters/CLAUDE_ADAPTER.md`: Claude runtime binding.
- `adapters/HERMES_ADAPTER.md`: Hermes memory/process binding.
- `00_BOOT.md` through `10_DELIBERATOR_CONTRACT.md`: source split docs used to compile the full runnable file.

## Portability Rule

This packet should not require outside packet files. Adapters may point to local runtime tools or memory systems, but those are runtime bindings, not universal requirements.

## Acceptance Rule

Do not treat the packet as runnable just because the docs are present. A runtime should have a conformance harness or equivalent checks for boot order, receipt truth, compile gate separation, and answer-first output.
