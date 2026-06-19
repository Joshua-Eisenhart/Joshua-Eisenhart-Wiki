---
title: Current v7 and v5 Reconciliation Router
created: 2026-06-19
type: router
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, v7, v5, reconciliation]
sources:
  - Codex-Ratchet/README.md
  - Codex-Ratchet/REPO_LAYOUT.md
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/read-first.md
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/repo-current-surface-ingest-2026-06-17.md
---


# Current v7 and v5 Reconciliation Router — 2026-06-19

## Problem

The wiki front door carries recent v7/v6 campaign language, while the repo root surfaces still route operators through `system_v5/docs`, `system_v4/probes`, and `scripts/`. This is not automatically a contradiction. It is a routing problem.

## Resolver

```text
repo process authority = current repo instructions + AGENTS.md + v5 process docs + current runbooks
repo active execution/result paths = exact local paths in current checkout
campaign/scratch/source tranche = v6/v7 pages, receipts, verdicts, and build reports
wiki surface = router, intake, source-processing, claim-ceiling preservation
promotion/status = only exact result/validator/controller gates
```

## When to use v7 pages

Use v7/v6 campaign pages for:

- current scratch diagnostics;
- base-floor/carrier tests;
- contextuality/router insights;
- campaign restart context;
- source-processing and model-route recovery.

Do not use them to override repo authority or status labels.

## When to use v5/v4 pages

Use v5/v4 surfaces for:

- process contracts;
- tool role/fanout discipline;
- sim template requirements;
- status-label discipline;
- current repo docs and layout routing;
- canonical result locations unless the live repo says otherwise.

## Page repair rule

If an old page makes v7 scratch claims look like v5 process admission, split it into:

1. source-processing / scratch-router section;
2. exact repo result path section;
3. claim ceiling section;
4. downstream task list.
