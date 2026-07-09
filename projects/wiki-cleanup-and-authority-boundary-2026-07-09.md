# Wiki Cleanup And Authority Boundary - 2026-07-09

## Decision

The wiki is a research and documentation surface. It is not a Python, Julia,
JSON, patch, archive, or runtime checkout.

Current authority boundaries:

- Codex-Ratchet source, sims, manifests, and results:
  `/Users/joshuaeisenhart/Codex-Ratchet`.
- Leviathan runtime and agent execution:
  `/Users/joshuaeisenhart/lev-main` and the newer comparison checkout under
  `/Users/joshuaeisenhart/GitHub/lev`.
- Wiki research and project state: Markdown pages under
  `/Users/joshuaeisenhart/wiki`.
- Raw source intake: preserved under `raw/`; PDFs may remain there. Raw source
  files are not rewritten into executable wiki infrastructure.

## Cleanup

The wiki previously tracked 495 files that were not Markdown or PDF: Python and
Julia sims, JSON result files, patches, screenshots, archives, logs, shell
launchers, and runtime support files. Those files have been removed from the
wiki current tree. Their prior versions remain recoverable from Git history;
the live executable copies belong in Codex-Ratchet or Leviathan.

Obsidian configuration remains because it is application configuration, not
research content. Raw source material remains under the raw intake boundary.

Generated run reports and Python cache files are not retained in the wiki.

## Sync Direction

The wiki is not a source-to-repo sync origin. New Leviathan versions are pulled
from their remotes into a separate local checkout, audited, and then used for
execution. Codex-Ratchet results are written to the Codex-Ratchet repo. The wiki
receives a Markdown research synthesis and links to receipts after the source
run is complete.

## Required Working Shape

```text
new Lev remote version
  -> local Lev checkout
  -> Lev executor runs bounded Codex sim
  -> Codex-Ratchet retains source/result receipt
  -> wiki receives Markdown research note and claim ceiling
```

No wiki page may claim a runtime result merely because a transcript or external
bundle says it ran. The source command, checkout, result path, and claim ceiling
must be named in the Markdown page.

## Retrieval Indexes

Maintain and consult the two retrieval/index layers across these four surfaces:

1. `/Users/joshuaeisenhart/wiki`
2. `/Users/joshuaeisenhart/Codex-Ratchet`
3. `/Users/joshuaeisenhart/lev-main` or the current clean Lev checkout
4. `/Users/joshuaeisenhart/Desktop/Codex Ratchet`

Indexes are for discovery on every substantive prompt. Exact reads, source
hashes, validators, and receipts decide the claim. A stale or failed index must
be reported and refreshed before relying on it.
