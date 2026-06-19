---
title: Leviathan Exec Poly Daemon Package Posture
created: 2026-06-19
updated: 2026-06-19
type: package-map
status: current-source-synthesis
claim_ceiling: package posture and boundary map only; default daemon proof and product runtime remain separate gates
tags: [leviathan, exec, poly, daemon, packages, v4]
sources:
  - projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19.md
  - projects/leviathan-current/exec-poly-daemon-boundary.md
---

# Leviathan Exec Poly Daemon Package Posture

Exec, Poly, and Daemon are distinct and should stay distinct in the wiki.

## Package split

| Package | Role | Safe claim |
|---|---|---|
| `@lev-os/exec` | SDK-first execution contract for CLI/MCP/poly surfaces | execution contract package and central SDK surface |
| `@lev-os/poly` | Poly Registry System and `lev` binary/surface projection layer | registry/binder/surface projection layer |
| `@lev-os/daemon` | lifecycle, supervision, health monitoring, task execution | runtime process/lifecycle surface, proof-gated |

## Boundary

Exec is not the daemon. Poly is not the execution semantics. Daemon lifecycle health is not settled by package presence.

## Proof gate

Default daemon proof remains separate from named SDK/Poly proof. Cite current proof receipts before using "green" or "works."

## Read next

- [[projects/leviathan-current/proof-backed-status-dashboard]]
- [[projects/leviathan-current/runtime-module-map-full-2026-06-18]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]
