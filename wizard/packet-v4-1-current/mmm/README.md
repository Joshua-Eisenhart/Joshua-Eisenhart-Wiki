---
title: Wizard v4.1 MMM Directory
type: mmm_index
packet: v4.1
framing: standalone
---

# Wizard v4.1 MMM Directory

This directory is required. Wizard v4.1 is not a no-MMM system.

## Required Load Surfaces

- `FULL_MMM_v4_1.md`: full main-thread salience loaded before boot/core/runtime docs.
- `COMPACT_MMM_v4_1.md`: compact main-thread salience for constrained runtimes.
- `main/full/md/MMM_MAIN_FULL_v4_1.md`: versioned full main MMM source.
- `main/compact/md/MMM_MAIN_COMPACT_v4_1.md`: versioned compact main MMM source.
- `mini/full/...`: full route/member mini-MMM files.
- `mini/compact/...`: compact route/member mini-MMM files.
- `mini/MEMBER_MINI_MMM_REGISTRY_v4_1.md`: route/member mini-MMM registry for exact slice lookup.
- `mini/MINI_MMM_LOAD_CONTRACT_v4_1.md`: worker load order and fallback rules.

## Boot Rule

Main thread load order starts here:

1. Load `mmm/main/full/md/MMM_MAIN_FULL_v4_1.md` for FULL mode, or `mmm/main/compact/md/MMM_MAIN_COMPACT_v4_1.md` for COMPACT mode.
2. Load `00_BOOT.md`.
3. Load `01_UNIVERSAL_THREE_COUNCIL_WIZARD.md`.
4. Load the task and source material.
5. Load only the adapter docs required by the active runtime.

Worker load order starts from `mini/MINI_MMM_LOAD_CONTRACT_v4_1.md`, then loads the exact full or compact member mini-MMM for the assigned route.

## Completeness Note

The current v4.1 MMM surface is restored from the v3.4 full/compact MMM tree. It intentionally does not import the full v2.8 expanded estate.
