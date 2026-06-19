---
title: Leviathan Current State And Roadmap
created: 2026-06-17
updated: 2026-06-19
type: status-wiki-page
status: current-source-split
source_repo: lev-os/leviathan
source_snapshot: b7bca2cdbed5862743395f7c0330e7d640132764
claim_ceiling: source-doc status reconciliation; not fresh command proof; not release readiness certification
sources:
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ROADMAP.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/mvp.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/README.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ARCHITECTURE.md
---

# Current State And Roadmap

## Bottom Line

Current source at `b7bca2cdbed5862743395f7c0330e7d640132764` contains a real status split:

- `docs/ROADMAP.md` says Pentagon/Run Fabric provider proof is red, `@lev-os/testing` fails, daemon state is unknown, and security P0 remains open.
- `mvp.md` says named and default Pentagon proof, `@lev-os/testing`, and scoped security P0 are green, while launch readiness remains blocked by always-on daemon/event automation and downstream MVP surfaces.

This page did not rerun those commands. Treat the disagreement as a source-doc contradiction until a fresh proof packet on the current SHA settles it.

## Safe Current Verdict

Lev is a pre-release runtime with serious architecture, real package surfaces, and some proof-bearing paths. It is not safe to call it fully launch-ready, enterprise-ready, or fully green from docs alone.

## Source Split Dashboard

| Area | `docs/ROADMAP.md` at `b7bca2cd` | `mvp.md` at `b7bca2cd` | Wiki status |
|---|---|---|---|
| Manual events / trigger projection | Says manual events mode works against proof-spine fixture with no daemon side effects. | Says manual dispatch/projection is working. | Source-aligned as working at source-doc level. |
| S4 real `lev exec` | Says S4 real exec is certified by `rcpt-8a4f95daa123b2a2`. | Says S4 is certified / not full MVP. | Source-aligned as certified by named receipt, but not rerun here. |
| Pentagon / Run Fabric | Says provider proof regression is red and S5/Pentagon must be repaired. | Says named SDK/Poly provider proof and default daemon gate are green. | Split verdict; needs fresh rerun. |
| `@lev-os/testing` | Says package fails. | Says package passes. | Split verdict; needs fresh rerun. |
| Security P0 | Says `new Function`, legacy `execSync(command)`, ambient env leakage, and high audit vulns remain open. | Says scoped gate green, high audit exits 0, and unsafe env spreads are removed. | Split verdict; needs fresh security rerun. |
| Launch readiness | Blocks OSS until security, install/doctor, proof-spine, and real user quickstart are green. | Says MVP is still not launch-ready due to always-on daemon/event automation and downstream surfaces. | Source-aligned: not launch-ready. |

## Next Useful Proof Work

The next high-value packet is a clean-clone proof rerun on `b7bca2cdbed5862743395f7c0330e7d640132764`:

1. Install dependencies.
2. Rerun named and default Pentagon gates.
3. Rerun `@lev-os/testing`.
4. Rerun event-dispatch proof path.
5. Rerun scoped security grep/audit gates.
6. Write a dated proof packet that reconciles or preserves the `ROADMAP.md` / `mvp.md` split.

Until then, say "source-doc split" rather than "green" or "red" for the disputed areas.
