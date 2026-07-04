# Wiki vault — agent rules

This vault is the owner's second brain (Obsidian, git-versioned). Codex maintenance runs and any other agents working here follow these rules.

## Structure

- `index.md` — front door, keep under 120 lines. Full listing lives in `index-full.md`.
- `raw/` — untouched source material. Never edit; only link from it.
- `entities/` — one page per concrete recurring thing (people, repos, tools, systems).
- `concepts/` — one page per idea, pattern, or doctrine.
- `projects/` — project state and routers.
- `ops/` — maintenance logs (`maintenance-log.md`, `contradictions.md`, `orphans.md`, `stale-status.md`).
- `_archive/` — do not modify.

## Writing rules

1. New page → link it from at least one hub (index, a project read-first, or an entity page). No orphans.
2. One subject per page. If a page covers two subjects, split it.
3. Never delete content; archive or redirect-stub instead.
4. Contradictions are listed in `ops/contradictions.md`, never silently resolved. Divergent readings stay divergent until the owner decides.
5. Status labels carry dates. Do not upgrade a status label without evidence.
6. Commit locally after each maintenance pass. Never push.

## Research intake (from Hermes skills)

- Keep `raw/papers` as source intake and processed wiki pages under `concepts/`, `queries/`, project pages, indexes, and logs.
- Split arXiv lanes from non-arXiv foundation or bibliography lanes; do not force books, reports, products, or historical foundations into arXiv/raw-paper intake.
- Query pages are queues, not canon. Mark unresolved candidates clearly and do not cite or promote them until exact sources are resolved and read.
- Avoid thin reference pages: new or promoted reference pages need at least 40 nonblank body lines, plus concrete relevance and related links.
- Fix orphans before closing: add index/hub links and at least two meaningful backlinks when creating a new queue or reference page.

## Recall layer

Semantic recall over this vault uses codebase-memory-mcp. After any pass that adds or edits pages, refresh the index:

```
~/.local/bin/codebase-memory-mcp cli index_repository '{"repo_path":"/Users/joshuaeisenhart/wiki"}'
```

To search the vault structurally before grepping:

```
~/.local/bin/codebase-memory-mcp cli search_code '{"repo_path":"/Users/joshuaeisenhart/wiki","pattern":"<query>"}'
```

## Scheduled maintenance

- Nightly: `~/.local/bin/wiki-nightly-compile` — link new pages into hubs, update index, commit, re-index recall.
- Weekly: `~/.local/bin/wiki-weekly-lint` — merge clear duplicates (max 10), list contradictions/orphans/stale statuses, commit.
