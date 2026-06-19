---
title: Wizard Universal Harness
created: 2026-04-28
updated: 2026-06-19
packet: v4.3
type: concept
framing: current
---

# Wizard Universal Harness

Current Wizard is **v4.3**.

The proper shared v4.3 packet lives here:

- `packet-v4-3-current/`

All LLM-specific Wizard versions can also live in this folder as sibling adaptations:

- `hermes-version-current/` — Hermes-native Wizard v4.3.
- `claude-version-current/` — Claude Code-native Wizard v4.3.
- `codex-version-current/` — reserved for a Codex-native Wizard v4.3 when built.

Older packets are legacy/provenance:

- `packet-v4-2-current/`
- `packet-v4-1-current/`
- earlier packet folders

## Core rule

A general Wizard packet cannot run a system by itself. Each LLM/system must make a native version that binds the shared Wizard mechanisms to its own tools, memory, skills, context window, output surface, and failure modes.

Hermes is one adaptation. Claude is one adaptation. Codex can have its own adaptation. No system's adapter is automatically authority for another system.

Copying files is allowed. Adoption requires retuning.

## Reading order

1. `00-read-first.md`
2. `packet-v4-3-current/README.md`
3. `packet-v4-3-current/00_READ_FIRST.md`
4. load `packet-v4-3-current/mmm/FULL_MMM_v4_3.md`, or `packet-v4-3-current/mmm/COMPACT_MMM_v4_3.md` plus `packet-v4-3-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md` when context is tight
5. `packet-v4-3-current/WIZARD_v4_3.md`
6. the active LLM's native adaptation folder
7. older packets only when needed as source/provenance

## Provenance Notes

- [[wizard/wizard-origin-and-jp-smith-provenance]] — owner-confirmed starter note crediting JP Smith with the original Wizard idea. It is not a full lineage ledger for v4.1/v4.2/v4.3, MMM, taskcards, conformance files, or LLM adapters.

## Runtime-native adaptations

- `hermes-version-current/` — adopted/always-on in Hermes through profile `HERMES.md` and the `hermes-wizard` skill.
- `claude-version-current/` — Claude Code adaptation surface; currently built but still needs full skill adoption and retuning of copied Hermes-named schemas/conformance files.

## Status

This folder is the shared Wizard home. `packet-v4-3-current/` is the current shared core. Per-LLM folders are custom adapters. v4.2 and earlier remain source material, not current runtime law.
