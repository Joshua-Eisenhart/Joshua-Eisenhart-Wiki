---
title: Codex Ratchet Slim Front Door Load Order
created: 2026-06-19
type: project-front-door
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, read-first, load-order]
sources:
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/read-first.md
  - Codex-Ratchet/README.md
  - Codex-Ratchet/system_v5/docs/CURRENT_DOCS_MAP.md
---


# Codex Ratchet Slim Front Door Load Order — 2026-06-19

## Use this first

This page is the compact load-order card. The dense project front door remains the main router.

## Minimum load

1. `projects/codex-ratchet/read-first`
2. `specs/codex-ratchet/README`
3. `specs/codex-ratchet/process-contract-refresh-mirror-2026-06-19`
4. `specs/codex-ratchet/status-labels-crosswalk-2026-06-19`
5. Task-specific router below.

## Task router

| Task type | Load next |
|---|---|
| Sim/proof/tool-stage work | `specs/codex-ratchet/sim-full-wizard-parallel-runbook-mirror-2026-06-19`, `specs/codex-ratchet/sim-template-result-schema-mirror-2026-06-19` |
| Repo layout or docs navigation | `specs/codex-ratchet/repo-layout-current-mirror-2026-06-19`, `specs/codex-ratchet/current-docs-map-mirror-2026-06-19` |
| Result/status summary | `specs/codex-ratchet/formal-scout-and-sim-estate-snapshot-readme-2026-06-19`, exact repo result path |
| Source-processing route | `projects/codex-ratchet/repo-to-wiki-ingestion-protocol-2026-06-19`, `templates/codex-ratchet/repo-to-wiki-tranche-template` |
| Carrier / `M(C)` / QIT / Axis0 / bridge claim | `projects/codex-ratchet/m-c-and-carrier-claim-ceiling-router-2026-06-19` |
| Wiki cleanup / indexing | `projects/codex-ratchet/cocoindex-friendly-page-shape-2026-06-19`, active CocoIndex policy |

## Stop rule

If a page would need a current repo count, a result verdict, or a promotion label, stop and exact-read the live repo artifact first.

## Safe wording

Use:

```text
source-processing only
router only
scratch diagnostic
dated snapshot
not admitted
not promoted
needs exact repo receipt
```

Avoid:

```text
proved
verified
settled
canonical
complete
admitted
full QIT engine
Axis0 solved
physics claim
```

unless the exact source/result gate is cited.
