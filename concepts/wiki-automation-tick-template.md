---
title: Wiki Automation Tick Template
created: 2026-04-13
updated: 2026-04-13
type: concept
framing: current
tags: [harness, wiki, automation, process, controller, template]
sources:
  - concepts/wiki-automation-contract.md
  - concepts/controller-prompt-rules.md
  - concepts/docs-framing-map.md
  - concepts/tool-capability-sim-program.md
framing_note: Concrete template for repeated Hermes wiki automation ticks. Use this to build cron prompts or manual bounded automation runs.
---

# Wiki Automation Tick Template

## Purpose
This page turns the wiki automation contract into a concrete tick template.

Use it when building:
- cron prompts
- repeated controller runs
- bounded autonomous wiki-maintenance passes

Live execution companions:
- `/Users/joshuaeisenhart/wiki/tools/wiki_probe.py`
- `/Users/joshuaeisenhart/wiki/config/wiki_automation_surface_map.json`
- `system_v5/docs/plans/wiki-automation-run-contract.md`
- `system_v5/docs/plans/wiki-automation-claude-terminal-orchestration.md`
- `system_v5/docs/plans/local-launch-checklist-wiki-automation.md`

## Core model
One tick = one bounded tranche.

A good tick does not try to improve the whole wiki.
It reads live authority surfaces, picks one tranche in order, uses Hermes's built-in tools, verifies, logs, and stops.

## Default read order
Every tick should begin by reading:
1. `/Users/joshuaeisenhart/wiki/index.md`
2. `/Users/joshuaeisenhart/wiki/concepts/topic-map.md`
3. `/Users/joshuaeisenhart/wiki/concepts/current-research-overlays.md`
4. `/Users/joshuaeisenhart/wiki/log.md`
5. `system_v5/docs/plans/wiki_ingest_and_lego_maintenance.md`
6. `system_v5/docs/plans/sim_backlog_matrix.md`
7. `system_v5/docs/plans/sim_truth_audit.md`
8. `/Users/joshuaeisenhart/wiki/config/wiki_automation_surface_map.json`
9. any tranche-specific authority pages

Then, if the tranche is cluster-specific, read the nearest routing/synthesis page for that cluster before editing.

## Default verification order
Before choosing the tranche, recompute:
1. actual public page count
2. missing-from-index pages
3. broken links
4. orphan pages
5. malformed wiki-link artifacts

Only after that choose the tranche.

## Ordered tranche menu
Pick the first unfinished/highest-priority tranche from this ordered menu:

### Tranche 1 — structural integrity
Targets:
- index count
- missing-from-index pages
- broken links
- orphans
- malformed matrix/wiki links

### Tranche 2 — routing coherence
Targets:
- `index.md`
- `topic-map.md`
- `current-research-overlays.md`
- `docs-framing-map.md`
- `docs-alignment-catalog.md`
- legacy routing pages

### Tranche 3 — role clarification
Targets:
- synthesis vs dev-facing vs support vs provenance vs comparison pages
- recommended reading order notes
- role labels inside overlapping clusters

### Tranche 4 — bounded content deepening
Targets:
- one cluster only
- no cross-cluster widening unless required for backlinks or role repair

### Tranche 5 — support-layer enrichment
Targets:
- bibliography/support pages
- support references
- repo-context links relevant to JP/dev handoff

### Tranche 6 — handoff polish
Targets:
- JP/dev reading path
- CS/runtime translation
- concise role separation for handoff pages

## Hermes-first tool rule
Default tools for a tick:
- read/search/patch/write
- execute_code or terminal for audits and reductions
- session search if prior session context matters

Use external/helper systems only if the tranche explicitly needs them.
Do not hand the tick over to an outside automation layer by default.

## Tick declaration template
Each run should explicitly declare:

- tranche:
- why this tranche is next:
- target pages:
- read order:
- allowed edits:
- forbidden widening:
- verification steps:
- stop rule:

## Example tick declaration
- tranche: routing coherence
- why this tranche is next: structural integrity is already clean, but the live cluster still has routing drift
- target pages: `topic-map.md`, `current-research-overlays.md`, `docs-framing-map.md`
- read order: `index.md` -> `topic-map.md` -> `current-research-overlays.md` -> `docs-framing-map.md` -> target cluster pages
- allowed edits: routing lines, updated dates, role labels, one bounded log entry
- forbidden widening: no new theory pages, no broad cluster prose expansion
- verification steps: recompute page count, check missing-from-index, confirm route visibility for target pages
- stop rule: stop after routing repair and verification only

## Cron prompt skeleton
Use this exact pattern as the backbone of a cron prompt:

1. Work in `~/wiki` and treat the live filesystem as authority.
2. Read `index.md`, `topic-map.md`, `current-research-overlays.md`, and `log.md` first.
3. Recompute actual public page count, missing-from-index pages, broken links, orphans, and malformed wiki-link artifacts.
4. Choose exactly one tranche from the ordered tranche menu.
5. Use Hermes built-in tools first.
6. Patch only the target pages for that tranche.
7. Update touched pages' `updated` dates.
8. Append one bounded log entry naming changed files and verification result.
9. Rerun verification.
10. Report:
   - tranche run
   - pages changed
   - verification result
   - next tranche suggestion
11. Stop.

## Output template
Every tick report should return:
- Tranche
- Why chosen
- Pages changed
- Verification
- Remaining issues
- Next bounded tranche

## Anti-drift rules
- do not choose by salience
- do not widen to a neighboring cluster because it seems relevant
- do not create new public pages unless the tranche explicitly justifies one
- do not skip routing/log verification after content edits
- do not promote legacy synthesis into live proof claims

## JP/dev-facing rule
If the tick is handoff-oriented:
- read the nearest Lev runtime/architecture docs if needed
- translate into CS/runtime/process language
- preserve nuance from the source layer
- keep provenance, support, synthesis, and dev pages distinct

## One-sentence summary
A wiki automation tick should read, audit, choose one tranche, patch only that tranche with Hermes-first tools, verify, log, report, and stop.

## Related pages
- [[wiki-automation-contract]]
- [[controller-prompt-rules]]
- [[wiki-as-harness-architecture]]
- [[tooling-status]]
- [[tool-capability-sim-program]]
- [[docs-framing-map]]
