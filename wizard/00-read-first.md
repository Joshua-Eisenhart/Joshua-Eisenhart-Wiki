---
title: Wizard Read First
created: 2026-04-28
updated: 2026-05-17
packet: v4.2
type: concept
tags: [wizard, boot-law, harness]
framing: current
---

# Wizard Read First

The active Wizard surface is the standalone v4.2 packet:

- `packet-v4-2-current/README.md`
- `packet-v4-2-current/WIZARD_v4_2.md`
- `packet-v4-2-current/mmm/FULL_MMM_v4_2.md`
- `packet-v4-2-current/skills/SKILLS_MANIFEST_v4_2.md`
- `packet-v4-2-current/mmm/` route-local mini-MMMs as needed

Use `packet-v4-2-current/README.md` for current Wizard work and follow that packet's runtime boot order. v4.1 is legacy/provenance unless explicitly requested.

## Boot order

1. Read `README.md`.
2. Read `packet-v4-2-current/README.md`.
3. Read `packet-v4-2-current/WIZARD_v4_2.md`.
4. Load `packet-v4-2-current/mmm/FULL_MMM_v4_2.md`.
5. Read `packet-v4-2-current/skills/SKILLS_MANIFEST_v4_2.md`.
6. Read the universal core and the adapter needed for the active runtime.
7. Load the user task.

If the user task explicitly asks for legacy v4.1 comparison/provenance, replace steps 2-6 with the boot order in `packet-v4-1-current/README.md`.

The v4.2 packet carries its own MMMs, mini-MMMs, route truth, councils, receipts, compile gates, follow-up contract, and adapters.

## Header / route truth

Use v4.2 packet header/routing rules when running current Wizard work. For Hermes-native runs, use the Hermes-owned result surface and compact proof strip from `hermes-version-current/` and the `hermes-wizard` skill.

No receipt means not run. Synthesis is not execution. Started workers are not completed workers. Parent-reported children are not raw child proof unless raw nested artifacts are visible.

## Status labels

`exists < runs < passes local rerun < canonical by process`. Reading a file proves only `exists`.

## Predecessors

`packet-v4-2-current/` is current Wizard. `packet-v4-1-current/`, `packet-v4-0-current/`, `packet-v3-5-current/`, `packet-v3-4-current/`, and earlier are reference/provenance. Mine them only when the task calls for genealogy or comparison. Do not load them as current runtime law.
