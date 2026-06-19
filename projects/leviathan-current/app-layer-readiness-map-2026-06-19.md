---
title: Leviathan App Layer Readiness Map
created: 2026-06-19
updated: 2026-06-19
type: product-map
status: current-source-synthesis
claim_ceiling: app-layer posture map only; no app is release-certified by this page
tags: [leviathan, apps, product-surface, readiness, v4]
sources:
  - projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19.md
---

# Leviathan App Layer Readiness Map

The app layer is real but uneven. Leviathan is not one UI and not one app maturity level.

## Observed app families

The root package includes app workspaces such as desktop, expo, landing, lev-now, nextjs, shift-app, video, and voice-api.

Examples from the V4 bundle:

- `apps/desktop` is an Electron desktop service manager with packaging/publish scripts and Electron Forge dependencies.
- `apps/lev-now` has dev/build/start/renderer scripts, but deploy is not configured.

## App posture categories

Use these labels before claiming readiness:

- demo;
- dashboard;
- desktop shell;
- service manager;
- production candidate;
- archive;
- unknown until source/test audit.

## Safe verdict

App surfaces are real enough to audit as product layer. They are not uniformly product-ready.

## Read next

- [[projects/leviathan-current/surface-family-matrix-v4-2026-06-19]]
- [[projects/leviathan-current/onboarding-dx-proof-ladder-v4-2026-06-19]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]
