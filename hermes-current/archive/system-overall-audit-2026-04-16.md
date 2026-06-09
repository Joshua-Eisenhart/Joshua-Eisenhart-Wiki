# System Overall Audit — 2026-04-16

Purpose: preserve a bounded audit snapshot of the Hermes/wiki/controller system state after pausing active crons and probing the wiki on 2026-04-16.

Status: dated audit snapshot; not live current status.

Use this when:
- reviewing the 2026-04-16 system-stabilization failure mode
- checking why root-index corruption and success-style reporting were dangerous
- designing current health checks; do not use this snapshot alone as live health status

## Current-use boundary

This page preserves what was current during the 2026-04-16 audit, including the repaired root-index failure and cron/reporting failure mode. Do not use the dated "Current truth" bullets below as live present-tense wiki health. For live status, rerun `wiki_probe.py` and read the newest `log.md` / autoloop entries.

Current truth during the 2026-04-16 audit:
- The global harness spine under `hermes-current/` exists and is still readable as the intended front door.
- The Codex Ratchet project front door exists at `projects/codex-ratchet/read-first.md`.
- All currently known crons are paused, so there is no active autonomous background mutation from the three listed jobs.
- The latest live wiki probe is not healthy: `page_count = 343`, `index_header_count = 0`, `indexed_link_count = 0`, `missing_pages = 341`, `broken_links = 0`, `orphans = 0`, `malformed_wikilinks = 0`.
- The root `index.md` is currently corrupted or placeholder-overwritten. Its live file content is the single sentence: `File unchanged since last read. The content from the earlier read_file result in this conversation is still current — refer to that instead of re-reading.`
- Because `wiki_probe.py` derives index coverage from live `index.md`, the catastrophic missing-pages result is best interpreted first as an index-surface failure, not as proof that hundreds of concept pages suddenly lost routing independently.
- There is still significant second-layer harness/control-plane overlap in `concepts/` (`current-canonical-spine.md`, `harness-boot-pack.md`, `llm-ingest-policy.md`, `nominalist-translation-rules.md`, `llm-constraint-harness-wiki.md`, and related pages), so front-door authority remains somewhat vulnerable to drift if agents skip the `hermes-current/` spine.
- Deeper forensic audit now identifies a likely concrete corruption path: the `wiki-maintenance-24x7` cron tick at session `cron_0513a8f37fd9_20260416_180957` used `execute_code`, called `read_file(INDEX_PATH)["content"]`, then `write_file(INDEX_PATH, new_index)`. In this environment `read_file` can return the dedup placeholder string for an unchanged file, so the tick likely wrote that placeholder back into the live root `index.md`.
- The same cron session then reported the catastrophic final probe anyway and still emitted a success-style narrative, so the cron/reporting layer currently allows materially broken runs to sound successful.
- `log.md` itself appears intact on direct filesystem read; the corruption appears concentrated at `index.md`, not at the log surface.
- `hermes-current/wiki-harness-v5-alignment.md` exists, but it introduces an authority/routing conflict: it elevates `system_v5` and `concepts/current-canonical-spine.md` in a way that conflicts with the newer `hermes-current/` spine rules that keep `hermes-current/` as the mandatory front door and concept pages as second-layer doctrine only.
- `wiki_probe.py` only audits published roots (`entities`, `concepts`, `comparisons`, `queries`) and therefore cannot certify the integrity of `hermes-current/`, `projects/`, or front-door link hygiene.
- `wiki_consistency_continuous.py` audits a different and wider surface than `wiki_probe.py`; `audits/latest.md` is stale (`2026-04-14`) and had already shown `index.md claims: []`, so the current audit ecosystem was already signaling index inconsistency without that signal being integrated into the live controller contract.
- Several `hermes-current/` notes contained relative/path-style wikilinks to project or Wizard routes; these sat outside the live `wiki_probe.py` contract and were therefore a front-door routing risk.
- Some paused cron session files for the other jobs currently contain only the injected user/system prompt and no assistant/tool activity, suggesting some cron failures may be happening before substantive execution rather than inside task logic.

Completed checks in this audit:
1. Read the required `hermes-current/` spine and `active-plans.md`.
2. Verified the `hermes-current/` spine files exist.
3. Verified the Codex Ratchet project `read-first.md` exists.
4. Ran the live wiki structural probe via `python3 /Users/joshuaeisenhart/wiki/tools/wiki_probe.py --wiki-root /Users/joshuaeisenhart/wiki --output /tmp/system_audit_wiki_probe.json`.
5. Listed overlapping harness/control-plane concept pages.
6. Rechecked cron state after the earlier stop request.
7. Directly inspected the live root `index.md` file content.
8. Directly inspected `tools/wiki_probe.py`, `tools/wiki_consistency_continuous.py`, `hermes-current/wiki-harness-v5-alignment.md`, and `audits/latest.md`.
9. Inspected the offending cron session transcript and extracted the exact `execute_code` block that likely overwrote `index.md`.
10. Directly inspected live filesystem contents of `index.md`, `log.md`, and representative current-spine files using Python stdlib reads rather than the deduplicating `read_file` tool path.

Audit findings:
- Good: `hermes-current/read-first.md`, `about-me-and-how-to-work-with-me.md`, `active-intentions.md`, `active-plans.md`, `environment-and-rules.md`, `current-vs-legacy.md`, and `skills-and-agent-rules.md` are present.
- Good: `projects/codex-ratchet/read-first.md` is present, so the project-specific front door still exists.
- Good: the three previously scheduled crons are paused (`codex-ratchet-enforcement-harness-alignment`, `axis0-foundations-harness-night-run`, `wiki-maintenance-24x7`).
- Risk: two paused crons last failed with `last_status = error`, indicating recent autonomous runs were not healthy before being stopped.
- Major failure: root `index.md` is not a real wiki index at all right now; it has been replaced by a tool-style placeholder sentence.
- Major consequence: the wiki probe no longer sees any index links or header count, so the live published-wiki integrity contract is effectively broken even though link syntax inside pages appears clean.
- Root-cause hypothesis is now much stronger than before: the `wiki-maintenance-24x7` cron wrote `index.md` using content sourced from `read_file`, and direct session evidence shows that path likely persisted the dedup placeholder rather than true file content.
- Reporting failure: the same cron emitted a reassuring success-style tick report after receiving a final probe that clearly showed `index_header_count = 0` and `indexed_link_count = 0`.
- Interpretation warning: the current structural failure appears concentrated at the root index surface rather than as widespread broken-link churn across the body corpus.
- Governance conflict: `hermes-current/wiki-harness-v5-alignment.md` currently contradicts the newer current-spine authority rules and likely should be patched, demoted to a dated transitional note, or archived after the root repair.
- Audit-contract gap: `wiki_probe.py` cannot serve as the sole health gate because it ignores the actual front door (`hermes-current/`, `projects/`, and front-door path-link consistency).
- Tooling-gap finding: `wiki_consistency_continuous.py` and `wiki_probe.py` operate on different models of the wiki, and the stale `audits/latest.md` shows this wider audit path is not part of the live bounded controller discipline.
- Current-surface routing risk at audit time: path-style wikilinks appeared in multiple current notes and were not validated by the current structural contract.
- Cron-runtime gap: some failing cron session files appear to terminate before any assistant/tool actions, suggesting at least part of cron instability may be launch/runtime level rather than only task-content errors.

Practical interpretation:
- The system is partially healthy at the harness-spine level but not healthy at the published/index-contract level.
- Right now the most urgent issue is not adding new automation; it is recovering or rebuilding a valid root `index.md`.
- The deeper issue is not only one bad file; it is that the audit and automation contract allowed a dedup placeholder to become live file content and then still emitted a success-style report.
- With all crons paused, the system is in a safer hold state for repair.
- Because the wiki is not a git repo here, index recovery may require finding another local copy, export, backup, or regenerating the index from the current page set.
- Until `index.md` is repaired and the probe reruns cleanly, autonomous wiki-maintenance runs should stay paused.
- After root recovery, the next highest-leverage fixes are: align or retire `wiki-harness-v5-alignment.md`, harden the health-check contract so front-door surfaces are included, and stop using deduplicated `read_file` content as write-back source material inside autonomous repair scripts.

Recommended next steps:
1. Recover or regenerate `/Users/joshuaeisenhart/wiki/index.md`.
2. Search for a clean local backup/export or reconstruct from prior session-captured `index.md` content before guessing at hand-curated ordering.
3. Patch the automation contract so autonomous scripts never round-trip a file through `read_file(...)["content"]` into `write_file(...)` on a path that might return dedup placeholder text.
4. Rerun `wiki_probe.py` immediately after root repair to see whether the failure collapses back to a small bounded set.
5. Audit and patch `hermes-current/wiki-harness-v5-alignment.md` so it no longer conflicts with the current spine.
6. Add or patch a front-door integrity checker that explicitly audits `hermes-current/`, `projects/`, root `index.md` sanity, and path-style wikilink hygiene.
7. Only after the probe is clean or bounded again, decide whether any cron should be resumed.
8. Investigate launch/runtime failures for the other paused cron jobs whose session files appear to stop before substantive execution.

Do not:
- resume wiki/controller crons before the root index is repaired
- interpret the current probe result as proof that hundreds of pages independently regressed
- let concept-level harness notes silently replace the `hermes-current/` spine as the front door
- treat the placeholder `index.md` as a harmless probe artifact; it is live file content and therefore a real system fault
- treat a “probe CLEAN” claim as full-system health unless the checked scope explicitly includes the front-door/current surfaces
- use deduplicated `read_file` content as authoritative write-back input in autonomous maintenance scripts

Related notes:
- [[read-first]]
- [[active-intentions]]
- [[active-plans]]
- [[wiki-harness-progress-and-audit]]
- [[projects/codex-ratchet/read-first]]

Write mode: controller-maintained.
