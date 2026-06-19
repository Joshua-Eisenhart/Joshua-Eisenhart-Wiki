---
title: Repo Indexing and Bloat Policy Mirror
created: 2026-06-19
type: policy-mirror
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, cocoindex, bloat]
sources:
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/cocoindex-and-bloat-cleanup-policy-2026-06-17.md
---


# Repo Indexing and Bloat Policy Mirror — 2026-06-19

## Correct search/use sequence

1. Search CocoIndex for likely files/chunks.
2. Exact-read files before load-bearing claims.
3. Treat result JSON and audit verdicts by claim ceiling, not retrieval rank.
4. Refresh indexes after routable docs change.

## Generated-result policy

Keep small README/audit/spec/router files visible. Compress or archive huge generated JSON only after:

- exact original path recorded;
- SHA-256 checksum recorded;
- stable archive destination named;
- restore path exists;
- validators/audit paths updated or marked restore-required;
- CocoIndex refreshed.

## Wiki-page implication

Do not copy raw JSON to wiki prose. Create a small router/manifest page with exact paths, checksums, and claim ceilings.
