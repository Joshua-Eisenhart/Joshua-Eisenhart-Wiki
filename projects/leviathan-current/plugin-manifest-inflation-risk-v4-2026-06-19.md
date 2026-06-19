---
title: Leviathan Plugin Manifest Inflation Risk
created: 2026-06-19
updated: 2026-06-19
type: plugin-audit-map
status: current-source-synthesis
claim_ceiling: plugin posture map only; plugin counts do not prove working plugins
tags: [leviathan, plugins, manifests, overclaim-risk, v4]
sources:
  - projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19.md
  - projects/leviathan-current/plugin-ownership-map.md
---

# Leviathan Plugin Manifest Inflation Risk

Plugin manifest breadth is impressive but easy to overclaim. Do not summarize a manifest count as working plugins.

## Posture labels

| Label | Meaning |
|---|---|
| `ships-with + tests + src + command proof` | strongest plugin posture |
| `ships-with + source only` | source-backed, proof missing |
| `ships-with:false + mature source` | mature direction, not shipped |
| `ships-with:false + shell` | shell/proposal |
| `manifest-only / no src` | not a working plugin claim |
| `proposal / capability direction` | design/provenance only |
| `archive / provenance` | historical |
| `unknown until package-specific audit` | needs inspection |

## Examples to keep fenced

- `qit-engines`: source/provenance rich, `ships-with:false`, no src/tests in manifest posture.
- `vision`: provider selection/privacy/surface architecture, not shipping proof.
- `voice`: rich daemon/session/realtime config, `ships-with:false`.
- `browser`: command surfaces and FlowMind programs, but needs command/test proof.
- `sdlc`: ships with rich flow surface, but full live loop remains proof-gated.

## Read next

- [[projects/leviathan-current/plugin-ownership-map]]
- [[projects/leviathan-current/surface-family-matrix-v4-2026-06-19]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]
