---
title: Leviathan Operating Contract vs Product Proof
created: 2026-06-19
updated: 2026-06-19
type: assessment
status: current-source-synthesis
claim_ceiling: source/wiki synthesis only; not fresh runtime proof, maintainer acceptance, product readiness, or release certification
tags: [leviathan, operating-contract, product-proof, claim-ladder, v4]
sources:
  - projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19.md
  - projects/leviathan-current/proof-backed-status-dashboard.md
  - specs/leviathan-current/README.md
---

# Leviathan Operating Contract vs Product Proof

Leviathan has a strong operating-contract culture. That is real value: docs, specs, AGENTS rules, FlowMind declarations, package boundaries, receipts, and proof language all push the repo toward evidence-aware work.

But an operating contract is not product proof.

## Claim ladder

| Rung | Meaning | Safe use |
|---|---|---|
| narrative | product or vision language | category/story only |
| contract | spec or architecture declares ownership or behavior | source-backed design intent |
| package surface | package exists with exports/scripts/deps | package-backed surface |
| source implementation | code implements a narrow behavior | implemented narrowly |
| test surface | tests or package test command exist | testable surface |
| proof receipt | command run recorded with exit/result | proof-backed at packet/SHA |
| product surface | user-facing app/API flow works | product-backed narrow flow |
| release-ready | install, docs, security, smoke, community gates green | not currently established |

Most overclaims collapse rungs. The wiki should force each major sentence to say which rung it is on.

## Safe verdict

Leviathan is serious as an agent-runtime architecture and operating-contract system. Its release/product proof remains mixed and must be checked by current command receipts.

## Blocked wording

- fully green
- product-ready
- enterprise-ready
- launch-ready
- all packages work
- all surfaces are implemented

## Read next

- [[projects/leviathan-current/docs-authority-vs-status-drift-v4-2026-06-19]]
- [[projects/leviathan-current/proof-backed-status-dashboard]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]
