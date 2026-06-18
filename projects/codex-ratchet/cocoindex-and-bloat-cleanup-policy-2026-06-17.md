---
title: Codex Ratchet CocoIndex and Bloat Cleanup Policy
created: 2026-06-17
type: project-status
status: active cleanup policy
claim_ceiling: operational routing and cleanup policy only; not a scientific admission surface
---

# Codex Ratchet CocoIndex and Bloat Cleanup Policy — 2026-06-17

Purpose: keep `~/wiki` and `/Users/joshuaeisenhart/Codex-Ratchet` searchable for LLM agents without letting local indexes, generated JSON, legacy packets, or raw provenance swamp the retrieval layer.

## Current routing

CocoIndex is a semantic map, not authority.

- Wiki MCP server: `cocoindex_wiki`
- Wiki wrapper: `/Users/joshuaeisenhart/.local/bin/cocoindex-wiki-mcp`
- Repo MCP server: `cocoindex_codex_ratchet`
- Repo wrapper: `/Users/joshuaeisenhart/.local/bin/cocoindex-codex-ratchet-mcp`
- CocoIndex executable: `/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc`

Correct use:
1. Search CocoIndex for likely files/chunks.
2. Read exact files before making load-bearing claims.
3. Treat result JSON and audit verdict files by claim ceiling, not by retrieval rank.
4. Refresh indexes after routable wiki/repo docs change.

## Measured bloat state

Observed during the 2026-06-17 cleanup pass.

### Wiki

Before lean rebuild:
- `~/wiki/.cocoindex_code`: about `681M`
- total wiki: about `862M`
- JSON chunks were a major index component.

After lean rebuild:
- `~/wiki/.cocoindex_code`: `336M`
- total wiki: `517M`
- chunks: `53121`
- languages: markdown `44835`, text `7462`, python `778`, bash `36`, yaml `10`
- JSON is excluded from the wiki semantic index.

### Codex-Ratchet repo

Before lean rebuild:
- repo `.cocoindex_code`: about `1.4G`
- total repo: about `2.6G`
- large JSON generated results dominated semantic-index noise.

After initial lean rebuild:
- repo `.cocoindex_code`: `1.1G`
- total repo: `2.3G`
- chunks: `189047`
- languages: python `138086`, markdown `24561`, json `12938`, text `12102`, javascript `768`, yaml `214`, bash `145`, toml `119`, html `114`

That still missed the requested `400-700M` working-tree target. The corrected sequence is: shrink generated repo payload first, then rebuild CocoIndex over the smaller/current corpus.

After generated-result gzip + current-surface CocoIndex rebuild:
- total repo with CocoIndex kept: `623M`
- repo `.cocoindex_code`: `63M`
- chunks: `10069`
- files: `771`
- languages: markdown `9979`, toml `90`
- remaining uncompressed generated result JSON >= `1M`: `0`

The final repo index is current-surface/router oriented, not full code/evidence indexing. Exact source, legacy docs, JSON specs, and gzipped evidence remain available by file reads.

## Cleanup classes

| Class | Examples | Policy |
|---|---|---|
| Local cache | `.cocoindex_code/`, `.pytest_cache/`, `.DS_Store` | Ignore locally; safe to reset/rebuild/delete when no daemon is using it. |
| Generated evidence | `system_v6/sims/**/results/*.json`, envelope results/specs, trajectory artifacts | Do not delete casually. Prefer compress/archive with checksums and keep small verdict/router docs visible. |
| Authored source/control | `.py`, `.jl`, validators, specs, audit verdicts, README/router docs | Keep visible unless explicitly retired. Source is stronger than generated result bulk for LLM retrieval. |
| Legacy/provenance | Wizard old packet folders, raw PDFs, old system_v4/v5 docs, read-only legacy docs | Preserve provenance; move only under a named archive policy. Do not silently erase genealogy. |
| Archive candidate | old duplicate packet zips, superseded full MMM JSON copies, huge result JSON families after summary manifests exist | Candidate only after manifest, checksum, route update, and restore path exist. |

## Compression/archive rule for large sim results

Large generated JSON files may be compressed or moved only when all of these are true:

1. A small human/LLM-readable summary remains in place or is linked from the sim folder.
2. The exact original path is recorded.
3. A SHA-256 checksum is recorded before the move/compression.
4. The archive destination is named and stable.
5. Any validator or audit path that expects the original file is either updated or explicitly marked as requiring restore.
6. CocoIndex is refreshed after the router/summary files change.

Preferred shape:

- keep `audit_verdict.md`, `README.md`, `spec.json`, small manifests, and source files visible;
- compress huge `results/*.json` files only after a restore command and checksum manifest exist;
- do not index huge result JSON semantically by default; read them exactly only when needed.

## Wizard/wiki legacy packet rule

`wizard/packet-v4-3-current/` is current. Earlier Wizard packet folders are legacy/provenance unless a task explicitly asks for genealogy or migration comparison.

Policy:
- keep current v4.3 surfaces routable;
- do not boot from v4.2 or older as current runtime law;
- legacy packet zips and old full MMM JSON copies are archive candidates, not immediate deletion targets;
- if moved later, preserve one clear provenance pointer and update `wizard/AGENTS.md`, `wizard/README.md`, and this wiki index.

## Verification commands

Wiki:

```bash
cd /Users/joshuaeisenhart/wiki
/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc status
/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc search --lang markdown --limit 5 "CocoIndex wiki MCP memory layer semantic retrieval"
```

Repo:

```bash
cd /Users/joshuaeisenhart/Codex-Ratchet
/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc status
/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc search --lang markdown --limit 5 "geometric constraint manifold M(C) root constraints finitude noncommutation"
/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc search --lang markdown --limit 5 "promotion_allowed formal_admission_allowed classification scratch diagnostic sim result contract"
```

## Current status

- Memory pointer fixed: long-form details belong in wiki/router docs, not injected Hermes memory.
- Wiki lean index verified: JSON removed from wiki semantic index; markdown/text remain searchable.
- Repo lean index verified: root-constraint and admission-contract searches return strong current repo hits.
- No authored repo/wiki content was deleted in this pass.
- Only local noise was removed: `.DS_Store` files and CR `.pytest_cache`.

## Next admissible cleanup

Do not mass-delete. The next real cleanup should be a manifest-backed archive/compression tranche for the largest `system_v6/sims/**/results/*.json` families, starting with one sim folder, with checksum + restore instructions before any move.

First dry-run manifest exists in the repo:

- `system_v6/receipts/gcm_constraint_carve_6q_v0_archive_dry_run_manifest_20260617.json`

It records the largest `gcm_constraint_carve_6q_v0` result family without moving or compressing anything: `18` target-folder files, `6` hashed candidates, largest result `303318038` bytes, `7` filename reference hits, and `79` sim-id reference hits.

Follow-up executed in repo receipt `system_v6/receipts/generated_result_json_gzip_manifest_20260617.json`:

- generated result JSON compressed in place as `.json.gz`: `58` files
- decompressed gzip SHA-256 restore check: passed for all `58`
- original generated JSON total: `667.3M`
- compressed total: `14.0M`
- saved: `653.4M`
- final repo size with CocoIndex kept: `623M`

## Wiki JSON cleanup execution

The wiki does not need content JSON/JSONL as authored knowledge surfaces. A follow-up pass removed wiki content JSON after hashing, while preserving hidden Obsidian app config JSON.

Manifest/receipt:

- `projects/codex-ratchet/wiki-json-cleanup-manifest-2026-06-17.md`

Verified state:

- removed wiki content JSON/JSONL files: `889`
- removed wiki content JSON/JSONL bytes: `40.1M`
- remaining JSON/JSONL outside `.obsidian/`, `.git/`, and `.cocoindex_code/`: `0`
- wiki total with CocoIndex kept after reset/rebuild: `475M`
- wiki CocoIndex after reset/rebuild: `336M`
- preserved hidden app config: `.obsidian/*.json`

Restore path for tracked content JSON, if needed:

```bash
git checkout -- <path>
```
