---
title: Wiki Automation Contract
created: 2026-04-13
updated: 2026-04-13
type: concept
framing: current
tags: [harness, wiki, automation, process, tooling, controller]
sources:
  - concepts/controller-prompt-rules.md
  - concepts/tooling-status.md
  - concepts/tool-capability-sim-program.md
  - concepts/system-tools-and-plan.md
  - concepts/session-handoff-2026-04-13-automated-run-and-tool-sims.md
framing_note: Current controller contract for bounded wiki automation. Encodes ordered execution, full-tool usage discipline, and anti-salience drift for autonomous wiki work.
---

# Wiki Automation Contract

## Overview
This page defines how autonomous wiki work should run.

The point is not to let an LLM roam around the wiki doing the most salient thing first.
The point is to make wiki automation bounded, ordered, tool-rich, and controller-disciplined.

This contract is for the wiki-builder path, not for the automated sim runner.
- the sim runner builds or reruns probes, batches, and controller audits
- the wiki-builder path ingests repo/doc/result changes into ledgers, routing pages, and `/Users/joshuaeisenhart/wiki`
- runner hardening like queue orchestration, lockfiles, heartbeats, or closeout contracts belongs to the sim-runner surfaces, not to this wiki-automation contract

## Core rule
Wiki automation should be controller-led and tranche-based.

That means each automation tick must:
1. read authority surfaces first
2. choose one bounded tranche
3. use the full relevant toolset for that tranche
4. verify before promotion
5. log exactly what changed
6. stop

No free wandering.
No salience-first cluster jumping.
No broad synthesis before authority/routing/verification steps are complete.

## Why this is needed
The repeated failure mode is:
- the model notices the most vivid or philosophically rich page
- expands that first
- ignores process order
- fails to update neighboring routing surfaces
- leaves logs, index, and support layers unsynchronized
- creates overlap drift when another lane touches the same cluster

So the automation process must optimize for:
- order
- boundedness
- verification
- synchronization
- explicit role separation

not just local page quality.

## Hermes-first full-tool principle for wiki automation
Hermes already has built-in wiki-capable tools, so those should be the default controller surface for wiki automation.

That means the baseline tool surface is already inside Hermes:
- file read/search/patch/write
- terminal / execute_code for audits and reduction scripts
- session recall
- cron for repeated bounded ticks
- bounded delegation when explicitly useful

Wiki automation should therefore not be designed as if it first needs an outside automation layer.
It should be designed as a better process over Hermes's built-in capabilities, with external repos or helper systems used only when a tranche genuinely needs them.

### Hermes built-in tools (default)
Use these first:
- read/search/patch/write for page work
- terminal or execute_code for filesystem audits, counts, consistency checks, and reduction scripts
- session search when prior work from earlier sessions matters
- cron only for repeated bounded ticks with explicit stop rules
- delegate/subagent tools only for bounded gap-finding or parallel audit slices, never as the authority source

### External/helper tools (subordinate)
Only use when the tranche clearly needs them:
- external repos such as `codex-autoresearch`
- Claude Code or other worker CLIs
- repo-local helper scripts outside the normal Hermes tool surface

These are subordinate supports, not the default controller for wiki work.

### Research/context tools
Use when needed:
- repo inspection against related codebases (for example Leviathan OS) when the handoff audience or runtime framing depends on it
- local source corpus and raw-source reading before synthesis
- bibliography/support pages when a nuanced claim needs support-layer routing rather than just more prose

### What this means in practice
A good automation pass might use:
- Hermes file tools to patch pages
- Hermes execute_code to recompute page/index counts and missing coverage
- Hermes search tools to find routing gaps across the whole wiki
- Hermes terminal or repo inspection to match JP/Lev-OS framing
- Hermes log/index/topic-map/current-research updates in the same tranche

Current live execution primitives for this lane are now explicit:
- `/Users/joshuaeisenhart/wiki/tools/wiki_probe.py`
- `/Users/joshuaeisenhart/wiki/config/wiki_automation_surface_map.json`
- `system_v5/docs/plans/wiki-automation-run-contract.md`
- `system_v5/docs/plans/wiki-automation-claude-terminal-orchestration.md`
- `system_v5/docs/plans/local-launch-checklist-wiki-automation.md`

That is the right meaning of "full tool set" here:
Hermes-first, multi-tool, tranche-bounded work.
Not salience wandering.
Not file-only patching.
Not handing the whole wiki over to an external automation layer by default.

## Ordered tranche model
Automation should pick exactly one tranche per tick.

Recommended tranche order:
1. structural integrity
   - page count
   - index coverage
   - broken links
   - orphan pages
   - malformed wikilinks / fake matrix links
2. routing coherence
   - index
   - topic-map
   - current-research-overlays
   - docs-framing / alignment / legacy routing surfaces
3. role clarification
   - synthesis vs dev-facing vs support vs provenance vs comparison pages
4. content deepening
   - one bounded cluster only
5. support-layer enrichment
   - bibliography / support references / repo-context links
6. handoff polish
   - JP/dev-facing reading path and translation clarity

Do not skip upward in that order just because a later tranche is more intellectually salient.

## Parallel independent-concept rule
When multiple wiki concepts are genuinely independent, they should be worked in parallel by separate Claude Code terminals rather than collapsed into one smoothing pass.

Use this pattern when:
- the concepts do not share the same target files
- the concepts can each be verified against separate authority clusters
- the main risk is conceptual collapse from one agent over-synthesizing them into a single blended story

Required discipline:
- one Claude Code terminal per independent concept cluster
- non-overlapping file sets per terminal
- Hermes remains the controller and final reconciler
- each terminal must stay inside its own authority/read-order bundle
- only after the parallel passes finish should Hermes reconcile index/log/routing surfaces

Why:
- this preserves concept independence
- it prevents the model from smoothing distinct concepts into one unified but inaccurate narrative
- it keeps provenance and framing differences visible instead of letting them collapse together

## Bounded tranche template
Each automation tick should declare:
- tranche name
- exact target pages
- read order
- allowed edits
- forbidden widening
- verification steps
- stop rule

Example:
- tranche: holodeck provenance cleanup
- targets: `holodeck-docs`, `projective-holodeck-memory-model`, `holodeck-as-recall-space`
- forbidden widening: no new theory pages, no personality edits, no Leviathan routing edits unless directly required for backlinks
- verification: page exists, backlinks intact, no broken links introduced, log entry appended
- stop rule: stop after these pages and routing/log repair only

## Anti-salience rule
The controller must not pick work by vividness or novelty alone.

Bad pattern:
- new metaphysical insight appears
- agent expands a glamorous page first
- support/routing/state surfaces drift

Good pattern:
- read live authority surfaces
- identify the next tranche in order
- complete the whole tranche
- stop

## Relation to tool-capability sims
The same logic applies to wiki automation itself.
Wiki automation should eventually have capability-tested patterns for:
- count/index reconciliation
- routing-gap detection
- cluster-role clarification
- source-provenance separation
- JP/dev handoff translation

That is, wiki automation should itself become a bounded, tool-capable lane rather than a vague assistant habit.

## Recommended autonomous tick contract
For repeated automation:
1. read `index.md`, `topic-map.md`, `current-research-overlays.md`, `log.md`
2. recompute actual public page count
3. detect missing-from-index, broken links, orphans, malformed wiki links
4. choose exactly one bounded tranche from the ordered model
5. patch only that tranche
6. append one bounded log entry
7. rerun verification
8. report what changed and what tranche should be next

## JP/CS handoff rule
When the tranche concerns pages likely to be handed to JP or another dev:
- inspect the relevant Lev repo docs if needed
- translate into runtime/architecture/process language
- keep the philosophy/physics source nuance, but do not leave the result in source-native-only language
- do not pretend a legacy source already defines the runtime contract

## One-sentence summary
Good wiki automation is not "have the LLM improve the wiki"; it is an ordered, controller-led, Hermes-first, full-tool, bounded tranche process that uses verification and routing repair to prevent salience-first drift.

## Related pages
- [[controller-prompt-rules]]
- [[wiki-automation-tick-template]]
- [[llm-controller-contract]]
- [[wiki-as-harness-architecture]]
- [[tool-capability-sim-program]]
- [[tooling-status]]
- [[system-tools-and-plan]]
- [[docs-framing-map]]
- [[current-research-overlays]]
