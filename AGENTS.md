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
