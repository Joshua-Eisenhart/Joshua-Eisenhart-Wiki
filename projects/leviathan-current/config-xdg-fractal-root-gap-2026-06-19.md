---
title: Leviathan Config XDG Fractal Root Gap
created: 2026-06-19
updated: 2026-06-19
type: architecture-gap
status: current-source-synthesis
claim_ceiling: config/XDG gap map only; not config proof or runtime certification
tags: [leviathan, config, xdg, local-first, runtime-paths, v4]
sources:
  - projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19.md
---

# Leviathan Config XDG Fractal Root Gap

Config and XDG paths are central but underdocumented in the wiki relative to their importance.

## Why this matters

Local-first and federate-ready claims depend on where configuration, runtime state, cache, plugins, FlowMind declarations, and project/module/env overlays live.

## Hidden skeleton

The V4 bundle flags these as important:

- XDG paths;
- config cascade;
- project/module/env layering;
- plugin config;
- FlowMind declarations;
- runtime paths;
- clean clone vs local-only assumptions.

## Safe verdict

Config is a structural dependency for runtime/product claims. It needs its own proof/readiness page before local-first or federated claims are treated as product-ready.

## Read next

- [[projects/leviathan-current/onboarding-dx-proof-ladder-v4-2026-06-19]]
- [[projects/leviathan-current/exec-poly-daemon-package-posture-v4-2026-06-19]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]
