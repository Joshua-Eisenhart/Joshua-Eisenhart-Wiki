---
title: Codex Ratchet Status Labels Crosswalk
created: 2026-06-19
type: crosswalk
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, status-labels, claim-ceiling]
sources:
  - Codex-Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md
  - Codex-Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md
  - Codex-Ratchet/CLAUDE.md
---


# Codex Ratchet Status Labels Crosswalk — 2026-06-19

## Public repo truth labels

| Label | Meaning |
|---|---|
| `exists` | file/result is present |
| `runs` | executes with exit code 0 |
| `passes local rerun` | fresh local run confirms expected criteria |
| `canonical by process` | passes local rerun plus SIM_TEMPLATE/tool/classification/depth requirements |

## Internal sim role labels

| Label | Meaning |
|---|---|
| `admitted` | local sim-role admission under its stated claim ceiling |
| `keep_but_open` | useful but still open |
| `audit_further` | needs audit |
| `diagnostic_only` | not promotable |
| `broken` | fails or invalid |

## Source-processing/wiki labels

| Label | Meaning |
|---|---|
| `router` | points to sources; not evidence |
| `source-processing` | preserves source/provenance; not admission |
| `scratch_diagnostic` | useful pressure/control; no promotion |
| `dated_snapshot` | generated at a time; rerun before live claim |
| `promotion_allowed=false` | cannot be cited upward |
| `formal_admission_allowed=false` | no formal admission from this page/result |

## Crosswalk rule

Never map these upward automatically. A scratch diagnostic can be useful and still only have a public status of `exists` or `runs`. A local result can be `admitted` internally and still not be `canonical by process`.

## Ban list

Do not use without exact evidence path:

```text
verified
proven
settled
complete
canonical
admitted
all pass
```
