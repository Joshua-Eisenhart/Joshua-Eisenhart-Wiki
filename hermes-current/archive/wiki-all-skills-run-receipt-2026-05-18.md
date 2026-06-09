# Wiki All-Skills Run Receipt — 2026-05-18

Purpose: compact receipt for the Hermes request to run the wiki skills against the wiki.

Status: current bounded run receipt; not a claim that the whole wiki is finished.

## Request
User asked: "run all the hermes wiki skills on the wiki".

## Skills covered
- `harness-bootstrap`: loaded the Hermes current spine before acting.
- `wiki-harness-build-session`: ran the whole-wiki structural audit path and chose bounded tranches instead of one unbounded rewrite.
- `wiki-maintenance-and-harness`: checked live structural health, queue surfaces, source/result/MMM/tool routers, and claim fences.
- `wiki-ingest-and-lego-maintenance`: checked ingest queue, result catalogue, tool router, and sim/result distinction.
- `wiki-upgrade-audit`: checked Hermes front door, current-vs-legacy, active plans, and wrote this durable receipt.
- `wiki-research-gap-fill`: checked existing research/MMM/tool gap surfaces and preserved the next research lane shape instead of duplicating pages.
- `memory-offload-to-wiki-harness`: confirmed `hermes-current/` remains the main frame-loader and `hermes-memory-offload` stays a migration ledger, not the main authority.
- `close`: this receipt plus the final probe line are the bounded close surface.

## Runtime truth
- Hermes spine read: `read-first`, `about-me-and-how-to-work-with-me`, `active-intentions`, `environment-and-rules`, `current-vs-legacy`, `skills-and-agent-rules`, and `active-plans`.
- Attempted external subagent fanout failed before execution because the configured subagent provider returned an invalid xAI API-key error. No subagent findings were used as evidence.
- Controller fallback used local file/Python probes only.

## Verification
Initial live probe:
- command: `python3 tools/wiki_probe.py --wiki-root /Users/joshuaeisenhart/wiki --output /tmp/hermes_wiki_probe_allskills.json`
- result observed: `page_count=393`, `index_header_count=393`, `indexed_link_count=422`, `missing_pages=[]`, `orphans=[]`, `broken_links=[]`, `stubs=[]`, `malformed_wikilinks=[]`, `stale_namespace_wikilinks=[]`.

Supplemental custom scan:
- published files: `393`
- unique published stems: `393`
- frontmatter issues in published pages: `0`
- note: the naive custom wikilink scan reported namespaced/path links and non-published root/wizard links as apparent extras/broken links. The repository-local `wiki_probe.py` is the binding structural check for this vault shape.

## Findings
- The wiki is structurally clean under the live probe.
- The broad queue already exists and is the right controller surface: `hermes-current/wiki-ingest-queue-and-priorities.md`.
- Whole-wiki campaign surfaces already exist, including `queries/whole-wiki-research-mmm-tool-gap-audit-2026-05-18.md`, `concepts/repo-tool-use-router.md`, `concepts/sim-run-catalogue-and-result-family-router.md`, and MMM reservoir pages.
- The next honest work is not creating another broad queue. It is selecting the next bounded tranche from the existing queue.

## Next bounded tranche recommendation
Run Queue E local rerun only if Codex Ratchet status is now green. If not green, do one wiki-only tranche from the existing campaign:
1. Deepen one thin tool reference page from `repo-tool-use-router`, preferably `geomstats-manifold-geometry-reference` or `clifford-geometric-algebra-reference`.
2. Or deepen one research lane from `whole-wiki-research-mmm-tool-gap-audit-2026-05-18`, preferably SMT/formal falsifier or topology carrier tools.
3. Or process one already-run result family from `sim-run-catalogue-and-result-family-router` at catalogue/router status only.

## Do not
- Do not claim this run completed the whole wiki.
- Do not promote provider/subagent agreement to evidence; the subagent attempt failed.
- Do not rerun Codex Ratchet sims unless the current repo status gate is green.
- Do not create duplicate queue pages while the existing queue and campaign pages are working.

Related notes:
- [[wiki-ingest-queue-and-priorities]]
- [[whole-wiki-research-mmm-tool-gap-audit-2026-05-18]]
- [[repo-tool-use-router]]
- [[sim-run-catalogue-and-result-family-router]]
- [[active-plans]]

Write mode: controller-maintained receipt.
