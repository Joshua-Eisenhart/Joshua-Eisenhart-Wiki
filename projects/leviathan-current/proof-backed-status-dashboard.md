---
title: Leviathan Proof-Backed Status Dashboard
created: 2026-06-19
updated: 2026-06-19
type: status-dashboard
status: current-source-split
source_repo: lev-os/leviathan
source_snapshot: 5dd98ac4ce7afeb9e4351787179c60208de6d23f
claim_ceiling: proof routing and split-verdict dashboard; not a fresh proof rerun; not release readiness certification
sources:
  - https://raw.githubusercontent.com/lev-os/leviathan/5dd98ac4ce7afeb9e4351787179c60208de6d23f/docs/ROADMAP.md
  - https://raw.githubusercontent.com/lev-os/leviathan/5dd98ac4ce7afeb9e4351787179c60208de6d23f/mvp.md
  - https://raw.githubusercontent.com/lev-os/leviathan/5dd98ac4ce7afeb9e4351787179c60208de6d23f/core/eval/src/constraint-manifold.ts
  - https://raw.githubusercontent.com/lev-os/leviathan/5dd98ac4ce7afeb9e4351787179c60208de6d23f/core/flowmind/src/kernel/system-flowmind-loader.ts
  - /Users/joshuaeisenhart/wiki/projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18.md
  - /Users/joshuaeisenhart/wiki/projects/leviathan-current/packet-8-wizard-mass-swarm-receipt-2026-06-18.md
---

# Proof-Backed Status Dashboard

## Current Verdict

The current source docs disagree. This page does not resolve the disagreement by prose.

Latest source read: `5dd98ac4ce7afeb9e4351787179c60208de6d23f`.

| Area | Latest source-doc state | Last wiki proof state | Safe wiki label |
|---|---|---|---|
| Manual event projection | `ROADMAP.md` and `mvp.md` both describe manual projection/dispatch as working. | Packet 7/8 focused on adjacent proof surfaces, not a full current-SHA rerun. | source-aligned, needs current proof packet for fresh green |
| S4 real `lev exec` | Both docs cite `rcpt-8a4f95daa123b2a2` as certifying bounded real exec. | Not rerun in this intake. | source-aligned by named receipt |
| Pentagon / Run Fabric | `ROADMAP.md` says red/regressed; `mvp.md` says named and default gates green. | Packet 7/8 on older clean clone found named SDK/Poly green, default daemon gate red/blocked. | split verdict, rerun required |
| `@lev-os/testing` | `ROADMAP.md` says fails; `mvp.md` says passes. | Packet 7/8 found blocked before assertions. | split verdict, rerun required |
| Security P0 | `ROADMAP.md` says open; `mvp.md` says scoped gate green. | Not rerun in this intake. | split verdict, rerun required |
| F01/N01 root validator | Current code defines `F01_FINITUDE` / `N01_NONCOMMUTATION` in `@lev-os/eval` and FlowMind loader binds `constraint-manifold` to that native implementation. | Source-read only in this pass; not a package test rerun. | implemented-narrowly, needs test rerun for fresh green |
| System FlowMind YAML rules | Current executor says YAML pipeline stages pass at boot in MVP because they are declarations; runtime rule interpretation is Phase 2+. | Source-read only. | design-backed / not runtime-enforced broadly |
| Launch readiness | Both docs still block full launch readiness. | Wiki agrees. | not launch-ready |

## Required Next Proof Packet

Use a disposable clean clone at the current SHA, then record:

```bash
git rev-parse HEAD
git status --short
pnpm install
pnpm --filter @lev-os/testing test
lev pentagon run --project . --json
lev pentagon gate --project . --json
lev pentagon run --suite pentagon-sdk-poly-binding --json
pnpm audit --audit-level high
```

If install or command prerequisites fail, the proof packet should say blocked and preserve the source-doc split.

## Do Not Say

- "fully green"
- "enterprise-ready"
- "launch-ready"
- "default daemon proof is settled"
- "`@lev-os/testing` is green"

until a current proof packet earns those exact claims.
