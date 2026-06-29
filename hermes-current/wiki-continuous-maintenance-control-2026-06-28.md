# Wiki Continuous Maintenance Control — 2026-06-28

Status: active control surface for ongoing bounded wiki maintenance.

## Purpose

Josh asked Hermes to keep the wiki up to date, preserve work that would otherwise be lost, keep running general wiki improvement, keep digesting research, track projects, and keep Hermes memory compact.

This note records the live automation and the rules that keep it useful rather than becoming a broad churn loop.

## Current automation

- Cron job: `wiki-general-bounded-deepening`
- Job ID: `a2e9088a081e`
- Schedule: every 12 hours
- Repeat: forever
- Delivery: local cron output only
- Workdir: `/Users/joshuaeisenhart/wiki`
- Skills loaded per tick: `overnight-wiki-deepening-runs`, `wiki-maintenance-and-harness`, `memory-offload-to-wiki-harness`, `capture`
- Toolsets: `file`, `terminal`, `web`, `search`

## Runtime status at setup

- Gateway: running under launchd after `hermes gateway start`
- Cron status: gateway running; cron jobs can fire automatically
- Structural wiki probe before this setup patch: clean
  - `page_count=460`
  - `index_header_count=460`
  - `indexed_link_count=579`
  - `missing_pages=0`
  - `orphans=0`
  - `broken_links=0`
  - `stubs=0`
  - `malformed_wikilinks=0`
  - `stale_namespace_wikilinks=0`

## Per-tick contract

Each autonomous tick must:

1. read the Hermes front door and routing surfaces first;
2. run `tools/wiki_probe.py` before edits;
3. pick exactly one bounded tranche;
4. prefer structure, routing, project trackers, existing-page deepening, source-backed research support, or memory-offload hygiene;
5. avoid broad rewrites and blob pages;
6. patch or create only what the tranche needs;
7. update `index.md`, nearby routers, and `log.md` when a public page is created;
8. run final `tools/wiki_probe.py` after the log edit;
9. report scope, files changed, verification, blockers, and next tranche.

## Route and cost guards

- No broad external model swarms.
- No mass OpenRouter calls.
- No `gpt-3.5-turbo` autonomous route.
- No recursive cron scheduling from inside a cron tick.
- No repo-backed claim promotion unless the tick freshly checks the repo evidence.
- Older facts must be labelled as prior-audit or snapshot-based.
- Secrets must be redacted as `[REDACTED]`.

## Current claim ceiling

This setup proves the control note was created, the cron job was scheduled, the gateway was started, and one manual tick completed with `last_status=ok`. It does not prove that every future tick will be useful; future ticks still need their own output receipts and final probe results.

## First tick receipt

Manual run: `cronjob run a2e9088a081e` at setup time.

Observed result:

- job executed successfully with `last_status=ok`
- scheduler stayed enabled with next run at `2026-06-28T14:56:41.453530-07:00`
- first tick performed a structural page-count repair and added a log entry
- final post-run probe returned:
  - `page_count=460`
  - `index_header_count=460`
  - `indexed_link_count=580`
  - `missing_pages=0`
  - `orphans=0`
  - `broken_links=0`
  - `stubs=0`
  - `malformed_wikilinks=0`
  - `stale_namespace_wikilinks=0`

## First scheduled tick review

Checked from the resumed Hermes thread after session `20260628_022538_84ac8a` broke:

- `cronjob list` showed `wiki-general-bounded-deepening` / `a2e9088a081e` still enabled and scheduled.
- Last scheduled run: `2026-06-28T15:01:15.160031-07:00`, status `ok`.
- Next scheduled run: `2026-06-29T03:01:15.160031-07:00`.
- The older `leviathan-current-wiki-bounded-deepening` job `33efc1f65a72` remains paused/disabled.
- Resume preflight probe returned `page_count=460`, `index_header_count=460`, `indexed_link_count=581`, and zero missing pages, orphans, broken links, stubs, malformed wikilinks, or stale namespace wikilinks.
- `git diff --check` passed.

Claim ceiling: this confirms the scheduler state and wiki structural health at resume time. It does not certify the semantic quality of future autonomous ticks; each tick still needs its own bounded receipt and final probe.

## Next review

Review job `a2e9088a081e` after the next scheduled tick. If it fails, edits too broadly, or promotes repo claims without fresh evidence, pause the job and tighten the prompt before resuming.
