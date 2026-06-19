---
title: Repo to Wiki Ingestion Protocol
created: 2026-06-19
type: protocol
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, ingestion, wiki-process]
sources:
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/repo-current-surface-ingest-2026-06-17.md
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/cocoindex-and-bloat-cleanup-policy-2026-06-17.md
  - Joshua-Eisenhart-Wiki/specs/codex-ratchet/README.md
---


# Repo to Wiki Ingestion Protocol — 2026-06-19

## Goal

Move repo ideas into wiki memory without copying raw evidence bulk, flattening status labels, or promoting scratch work.

## Ingestion sequence

1. Name the source tranche.
2. Classify source family:
   - authority/process;
   - executable source;
   - result/validator receipt;
   - scratch diagnostic;
   - source-processing/provenance;
   - generated/cached bulk.
3. Exact-read the source file.
4. Extract only the receiver lesson.
5. Assign claim ceiling.
6. Choose destination:
   - `specs/codex-ratchet/` for repo-facing mirrors/status snapshots;
   - `projects/codex-ratchet/` for current project routers/intake;
   - `concepts/` for owner/source/genealogy/divergence;
   - `templates/` for reusable forms.
7. Add demotion/stop rule.
8. Add index card only if it improves findability.
9. Refresh CocoIndex.

## Receiver lesson format

```yaml
source_path:
source_class:
source_timestamp:
receiver_page:
wiki_role:
safe_claim:
unsafe_inference:
claim_ceiling:
promotion_allowed: false
formal_admission_allowed: false
exact_read_required_before_reuse: true
```

## Do not ingest

- Large raw JSON into prose pages.
- Old logs as current truth.
- Assistant memory as owner doctrine.
- Result pass summaries without the result path.
- Snapshot counts without generated timestamp.
