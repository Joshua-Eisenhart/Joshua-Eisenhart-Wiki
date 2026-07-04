---
title: Wizard Read First
created: 2026-04-28
updated: 2026-06-13
packet: v4.3
type: concept
tags: [wizard, boot-law, harness]
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Wizard Read First

Current Wizard is **v4.3** and lives in this folder.

## Current boot order

1. Read `README.md`.
2. Read `packet-v4-3-current/README.md`.
3. Read `packet-v4-3-current/00_READ_FIRST.md`.
4. Load the v4.3 MMM: `packet-v4-3-current/mmm/FULL_MMM_v4_3.md`, or `packet-v4-3-current/mmm/COMPACT_MMM_v4_3.md` plus `packet-v4-3-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md` when context is tight.
5. Read `packet-v4-3-current/WIZARD_v4_3.md`.
6. Load the native adaptation for the active LLM/system:
   - Hermes: `hermes-version-current/`
   - Claude Code: `claude-version-current/`
   - Codex: `codex-version-current/` when present
7. Load the user task.
8. Use legacy packets only if the current v4.3 core or active adapter explicitly needs provenance/source material.

## Folder model

All Wizard versions and all LLM-specific adaptations may live under `~/wiki/wizard/`.

The shared packet is portable. The per-LLM folders are native. Do not collapse those two roles.

## Route truth

No receipt means not run. Synthesis is not execution. Started workers are not completed workers. Parent-reported children are not raw child proof unless raw nested artifacts are visible.

## Output truth

Wizard output is headered and non-log-shaped. Use compact human synthesis first, then receipts/proof strip. Raw logs are diagnostics only.

## Status labels

`exists < runs < passes local rerun < canonical by process`. Reading a file proves only `exists`.

## Legacy packets

`packet-v4-2-current/` and earlier are legacy/provenance. They may contain useful MMM reservoirs, examples, topology language, and migration source material, but they are not the current runtime target.
