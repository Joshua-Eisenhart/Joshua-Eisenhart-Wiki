---
title: Leviathan Release Readiness Ladder
created: 2026-06-19
updated: 2026-06-19
type: readiness-ladder
status: current-source-synthesis
claim_ceiling: release-readiness ladder only; not a release certification
tags: [leviathan, release-readiness, proof, launch, v4]
sources:
  - projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19.md
  - projects/leviathan-current/proof-backed-status-dashboard.md
---

# Leviathan Release Readiness Ladder

Release readiness should be stated as a ladder, not a vibe.

## Ladder

| Rung | Required evidence |
|---|---|
| source-aligned | current docs/code say the surface exists |
| package-backed | package scripts/exports/deps support the claim |
| builds | clean clone build succeeds |
| narrow tests pass | named package or suite passes |
| default path passes | default user/operator command passes |
| security reviewed | security gate stack has current receipts |
| docs onboard | fresh reader can follow docs without local assumptions |
| product smoke passes | user-facing flow works end to end |
| release candidate | install/docs/security/smoke/community gates green |

## Current verdict

Leviathan has real source, package, and proof-backed slices. Full launch/release readiness is not established by the V4 bundle.

## Claim lint

Use "proof-backed at packet/SHA", "split-verdict", "design-backed", "package-backed", or "needs current proof packet" instead of broad "green" unless the exact gate is current.

## Read next

- [[projects/leviathan-current/proof-backed-status-dashboard]]
- [[projects/leviathan-current/docs-authority-vs-status-drift-v4-2026-06-19]]
- [[projects/leviathan-current/security-gate-stack-v4-2026-06-19]]
