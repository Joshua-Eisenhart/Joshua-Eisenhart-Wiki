# CocoIndex Wiki MCP Memory Layer

Purpose: document the working CocoIndex-backed semantic retrieval layer for `~/wiki` and how Hermes, Claude Code, Codex, and other MCP-capable agents should use it.

Status: active operational routing note; retrieval layer, not authority by itself.

Use this when:
- an agent needs broad semantic search over `~/wiki`
- a future session asks how Hermes/Claude/Codex should access the wiki index
- a wiki answer should be grounded by finding the right files before reading exact text
- the CocoIndex daemon, MCP wrapper, or index freshness needs verification

## Current setup

Target corpus:
- `/Users/joshuaeisenhart/wiki`

CocoIndex Code executable:
- `/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc`

MCP wrapper:
- `/Users/joshuaeisenhart/.local/bin/cocoindex-wiki-mcp`

Wrapper behavior:
- changes directory to `/Users/joshuaeisenhart/wiki`
- runs `ccc mcp` from the Homebrew-Python-backed venv

Hermes MCP server name:
- `cocoindex_wiki`

Codex-Ratchet repo MCP server name:
- `cocoindex_codex_ratchet`

Codex-Ratchet repo MCP wrapper:
- `/Users/joshuaeisenhart/.local/bin/cocoindex-codex-ratchet-mcp`

Observed Hermes tool shape:
- `mcp_cocoindex_wiki_search`

Claude Code / Codex expected MCP server name:
- `cocoindex_wiki`

## What CocoIndex is for

CocoIndex is the semantic map over the wiki. It helps an agent find likely relevant files and chunks before spending context on exact reads.

Correct use:
1. Search CocoIndex with the broad semantic question.
2. Treat returned snippets as leads, not authority.
3. Read the actual wiki files and lines with file tools before making load-bearing claims.
4. Classify each source by current/legacy/raw/project role using [[current-vs-legacy]].
5. Answer or patch from checked file contents, not from retrieval snippets alone.

Useful filters:
- `languages: ["markdown"]` for wiki-note work
- `paths: ["hermes-current/*"]` for Hermes spine work
- `paths: ["projects/codex-ratchet/*"]` for Codex Ratchet front-door/project routing
- `refresh_index: true` when wiki files just changed and the search must see the new text

## What CocoIndex is not

CocoIndex is not:
- injected memory
- canonical truth
- a proof or admission surface
- a substitute for reading `hermes-current/read-first.md`
- a substitute for project front doors or exact result files
- automatically visible to raw chat models without MCP/tool access

Retrieval strength is not authority strength. A high-scoring chunk can still be legacy, raw intake, stale, or a candidate page with a strict claim ceiling.

## Cross-agent access

Hermes:
- configured with MCP server `cocoindex_wiki`
- uses the wrapper at `/Users/joshuaeisenhart/.local/bin/cocoindex-wiki-mcp`
- new/restarted Hermes sessions should discover the search tool automatically

Claude Code:
- add with:
  - `claude mcp add -s user cocoindex_wiki -- /Users/joshuaeisenhart/.local/bin/cocoindex-wiki-mcp`
- then restart/start a fresh Claude Code session and verify with `claude mcp list` or `claude mcp get cocoindex_wiki`

Codex:
- configured globally with MCP server `cocoindex_wiki` via:
  - `codex mcp add cocoindex_wiki -- /Users/joshuaeisenhart/.local/bin/cocoindex-wiki-mcp`
- observed 2026-06-17 with:
  - `codex mcp get cocoindex_wiki`
  - `codex mcp list`
- new Codex app/CLI sessions should discover the server automatically; an already-running Codex thread may need a fresh session before the MCP tool appears in its tool list

Boundary:
- Claude-owned wiki surfaces under `claude-memory/` remain Claude-owned. Hermes may read them but should not edit them.
- Hermes-owned surfaces under `hermes-current/` remain Hermes/controller-maintained. Claude may read them but should not edit them unless explicitly authorized.

## Verification commands

From the wiki root:

```bash
/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc status
```

Refresh the index after wiki edits:

```bash
/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc index
```

Search from the command line:

```bash
/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv-homebrew/bin/ccc search --lang markdown --limit 5 "Hermes memory offload read first"
```

Hermes MCP check:

```bash
hermes mcp test cocoindex_wiki
```

Codex MCP checks:

```bash
codex mcp get cocoindex_wiki
codex mcp list
```

## Known pitfalls

- The broken default Python venv at `/Users/joshuaeisenhart/.local/share/hermes-tools/cocoindex-code/venv` was not deleted during setup. It was created from a Python whose `sqlite3.Connection` lacks `enable_load_extension`; keep using `venv-homebrew` unless the old venv is intentionally cleaned up.
- A stale `ccc run-daemon` can keep running from the wrong venv. Check process paths if indexing/search reports the old SQLite extension error.
- Large wiki indexes can take longer than ordinary foreground timeouts. Treat timeout as open until `ccc status` and process checks prove failure or completion.
- Default CocoIndex Code settings index markdown plus JSON/text/code. Use markdown filters when evaluating note quality separately from receipt/manifest JSON.
- 2026-06-17 cleanup policy: the wiki index excludes JSON/JSONL from the semantic map; the Codex-Ratchet repo index excludes bulky generated result/evidence JSON patterns where possible. Exact files remain on disk and should be read directly when load-bearing. See [[projects/codex-ratchet/cocoindex-and-bloat-cleanup-policy-2026-06-17]].

## Update rule

After any wiki maintenance tranche that changes routable pages, refresh CocoIndex and run at least one semantic search for the new/changed phrase. The wiki probe checks structural integrity; CocoIndex search checks retrievability.

Related notes:
- [[read-first]]
- [[environment-and-rules]]
- [[skills-and-agent-rules]]
- [[current-vs-legacy]]
- [[hermes-memory-offload]]

Write mode: controller-maintained.
