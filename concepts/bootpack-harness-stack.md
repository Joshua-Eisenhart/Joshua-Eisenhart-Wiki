---
title: Bootpack Harness Stack
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, research, system]
sources:
  - raw/articles/system-v5-reference-docs/Older Legacy/BOOTPACKS/BOOTPACK_THREAD_A_v2.60.md
  - raw/articles/system-v5-reference-docs/Older Legacy/BOOTPACKS/BOOTPACK_THREAD_B_v3.9.13.md
  - raw/articles/system-v5-reference-docs/Older Legacy/BOOTPACKS/BOOTPACK_THREAD_S_v1.64.md
  - raw/articles/system-v5-reference-docs/Older Legacy/BOOTPACKS/MEGABOOT_RATCHET_SUITE_v7.4.2-PROJECTS copy.md
  - raw/articles/system-v5-reference-docs/Older Legacy/BOOTPACKS/MEGABOOT_RATCHET_SUITE_v7.4.7-PROJECTS_PATCHED_CONSTRAINT_MANIFOLD copy.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Bootpack Harness Stack

## Overview
A family of noncanon boot and packaging documents that define how Thread A, Thread B, and Thread S are initialized, enforced, and compiled into larger ratchet suites.

## Main points
- Thread A is the teaching/orchestration layer.
- The legacy source described Thread B as a hardened enforcement kernel and sole source of truth; current Codex Ratchet authority does not inherit that claim.
- Thread S is the save/index/compiler layer.
- The megaboot suites bundle those threads into a larger project bootstrap process.
- The docs emphasize deterministic boot order, failure isolation, and replayable artifacts.

## Related pages
- [[graph-driven-intent-runtime]]
- [[source-notes]]
