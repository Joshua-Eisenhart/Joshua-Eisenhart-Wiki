---
title: Sim Evidence and Status Label Discipline
created: 2026-06-19
type: status-router
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, sim, status-labels]
sources:
  - Codex-Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md
  - Codex-Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md
  - Codex-Ratchet/system_v4/probes/SIM_TEMPLATE.py
---


# Sim Evidence and Status Label Discipline — 2026-06-19

## The public status ladder

Use only:

```text
exists < runs < passes local rerun < canonical by process
```

No wiki page should compress this ladder into `verified`.

## Internal sim promotion states are different

Internal sim states such as `admitted`, `keep_but_open`, `audit_further`, `diagnostic_only`, and `broken` are not public repo truth labels. They can describe local sim role, not current repo-state proof.

## Evidence table

Before writing any broad status summary, fill:

| Claim | Source file | Result path | Criteria checked | Status label | Claim ceiling |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## No upward inference

A row that `runs` is not `passes local rerun`.

A scratch diagnostic with all-pass behavior is not canonical by process.

A `canonical` classification in a result still has its own claim ceiling and does not by itself admit bridge, axis, engine, QIT, physics, or final `M(C)` claims.

## Required demotion sentence

When a page imports a result family:

```text
Demote this claim if the exact result path, criteria checked, classification, tool manifest, tool integration depth, and ledger loopback cannot be exact-read.
```
