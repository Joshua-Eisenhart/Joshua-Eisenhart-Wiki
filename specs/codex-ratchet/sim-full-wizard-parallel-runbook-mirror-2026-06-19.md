---
title: Sim Full Wizard Parallel Runbook Mirror
created: 2026-06-19
type: spec-mirror
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, sim, wizard, parallel]
sources:
  - Codex-Ratchet/system_v5/ops/SIM_FULL_WIZARD_PARALLEL_RUNBOOK.md
  - Codex-Ratchet/AGENTS.md
---


# Sim Full Wizard Parallel Runbook Mirror — 2026-06-19

## Core rule

Every sim/proof/tool-stage turn uses Full Wizard as a max-useful parallel process across independent tool/function surfaces. The conservative boundary is admission/promotion, not candidate generation.

## Default topology

```text
wave 1: preflight + tool/function registry scouts
wave 2: packet authors/auditors + child fanout
wave 3: council/checks + follow-up make/scout/audit
wave 4: controller synthesis + runner handoff
```

## Parallel-safe work

- tool/function surface scouting;
- micro packet proposals;
- proof fixture selection;
- tool-lego fit candidate audits;
- result-schema audits;
- follow-up Make/Scout/Audit;
- read-only source/result checks.

## Serial work

- shared queue mutation where no atomic claim exists;
- result JSON classification;
- ledger updates;
- status-label changes;
- Git staging/commit/push;
- same-file edits.

## Default tool-stage fanout bank

```text
z3
cvc5
sympy
clifford
geomstats
e3nn
rustworkx
XGI
TopoNetX
GUDHI
PyG
PyTorch/autograd
```

Each row becomes:

```text
tool -> exact function/API surface -> tiny claim -> minimal fixture or useful lego target
```

## Acceptance distinctions

A sim-mode closeout must preserve:

- authored packet vs runner-executed result;
- queued row vs DONE row;
- result JSON vs ledger loopback;
- tool-function micro receipt vs tool-lego fit;
- tool-lego fit vs lego promotion;
- tool-tool coupling vs parallel imports.

## Claim ceiling

This mirror cannot certify that a Full Wizard run occurred. It only describes the expected shape.
