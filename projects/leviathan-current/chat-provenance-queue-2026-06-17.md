---
title: Leviathan Current Wiki Chat Provenance Queue
date: 2026-06-17
worker: chat-provenance-worker
inventory: /Users/joshuaeisenhart/wiki/projects/leviathan-current/source-inventory-2026-06-17.json
repo: /Users/joshuaeisenhart/GitHub/leviathan
head: a661ecbf410469becd7b89c3bfc5ee215721ae34
candidate_count: 250
owned_output: chat-provenance-queue-2026-06-17.md
status: wave-1-first-pass
---

# Leviathan Current Wiki — Chat / Transcript Provenance Queue

Wave 1 first pass over `chat_or_transcript_candidates` from the source inventory. This is a classification and processing queue only. It intentionally does **not** import raw chat/transcript content or promote chat-derived claims to current wiki truth.

## First-pass guardrails

- No chat-derived, transcript-derived, or handoff-derived claim becomes current truth without corroboration in current code, current docs, active decisions, or direct owner confirmation.
- Treat `.lev/pm/handoffs/*` as assistant-authored session continuity artifacts, not canonical product documentation.
- Treat `archive`, `scratch-202601`, and `sdk-first-superseded` paths as prior art only.
- Do not bulk-import raw transcript files, event logs, or index JSONL into the wiki. Capture metadata/provenance first.
- If secrets, tokens, credentials, private prompts, or sensitive local paths are encountered during later processing, redact secret values as `[REDACTED]` and record only that redaction occurred.

## Method

- Loaded the JSON inventory and inspected the 250-row `chat_or_transcript_candidates` queue.
- Classified primarily by relative path, filename, size, and inventory reason.
- Used only small previews for representative files where useful: one current handoff, one event-log sample, one design doc, one workshop transcript, and selected config/report/skill surfaces. No broad chat ingestion was performed.
- No raw Josh/JP chat export was identifiable from path/name in this candidate set. Several generated files contain JP-era local paths or agent task prompts; those are flagged as provenance/secret caution, not chat truth.

## Counts by primary class

| Class | Rows | Bytes | Notes |
|---|---:|---:|---|
| likely Josh/JP chat | 0 | 0 | No obvious raw human chat export by filename/path in this queue. |
| assistant/model transcript | 0 | 0 | No obvious verbatim model transcript; session handoffs are classified by topic as implementation conversations. |
| repo-generated report/log | 18 | 55174 | Reports, analysis stubs, command/rules/skill docs, index manifests. |
| product/design discussion | 6 | 149939 | Current design and decision documents surfaced by transcript/chat keywords. |
| implementation conversation | 126 | 1753786 | Active/current session handoffs and implementation continuity notes. |
| legacy/archive | 88 | 972670 | Archived, scratch, or superseded planning/session material. |
| needs secret/provenance caution | 4 | 1543658 | Runtime logs/index/config/hook paths; process metadata only first. |
| unknown | 8 | 1022826 | External research/video transcripts or unclear artifacts needing source identification. |

## First tranche queue — process these first

Purpose: establish a current-intent provenance spine without ingesting raw transcript/log content. For each row, extract only provenance metadata, source links, dates, and claims that can be checked against current repo/docs.

| # | Class | Size | Path | Handling note |
|---:|---|---:|---|---|
| 53 | product/design discussion | 42817 | `.lev/pm/designs/phase-3-jobtype-recognition-architecture.md` | design/decision planning surface; useful for intent, not current truth |
| 55 | product/design discussion | 35975 | `.lev/pm/designs/phase4-weight-system-architecture.md` | design/decision planning surface; useful for intent, not current truth |
| 54 | product/design discussion | 32926 | `.lev/pm/designs/phase-5-agentic-compiler-architecture.md` | design/decision planning surface; useful for intent, not current truth |
| 52 | product/design discussion | 29535 | `.lev/pm/designs/leviathan-meta-framework.md` | design/decision planning surface; useful for intent, not current truth |
| 51 | product/design discussion | 4535 | `.lev/pm/designs/agent-adapter-e2e-plan.md` | design/decision planning surface; useful for intent, not current truth |
| 50 | product/design discussion | 4151 | `.lev/pm/decisions/d16-dogfood-is-preset-plugin-first.md` | design/decision planning surface; useful for intent, not current truth |
| 144 | implementation conversation | 28274 | `.lev/pm/handoffs/20260310-sdlc-workgraph-deterministic-lifecycle-convergence-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 145 | implementation conversation | 2576 | `.lev/pm/handoffs/20260310-sdlc-workgraph-deterministic-lifecycle-convergence-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 163 | implementation conversation | 23839 | `.lev/pm/handoffs/20260314-architecture-decisions-session-9.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 169 | implementation conversation | 29807 | `.lev/pm/handoffs/20260314-poly-daemon-production-ready-session-15.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 177 | implementation conversation | 32273 | `.lev/pm/handoffs/20260314-s17-arscontexta-skill-graph-social-session-17.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 127 | implementation conversation | 17919 | `.lev/pm/handoffs/20260310-flowmind-graph-alignment-meta-interview-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 128 | implementation conversation | 20665 | `.lev/pm/handoffs/20260310-flowmind-harness-control-plane-boundary-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 142 | implementation conversation | 16225 | `.lev/pm/handoffs/20260310-sdlc-flowmind-deepen-validate-hygiene-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 159 | implementation conversation | 22218 | `.lev/pm/handoffs/20260312-sdlc-autodev-heartbeat-session-4.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 162 | implementation conversation | 29467 | `.lev/pm/handoffs/20260313-sdlc-autodev-heartbeat-session-6.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 150 | implementation conversation | 14966 | `.lev/pm/handoffs/20260311-graph-convergence-session-3.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 154 | implementation conversation | 14579 | `.lev/pm/handoffs/20260311-work-mvp-flowmind-replatform-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 119 | implementation conversation | 31682 | `.lev/pm/handoffs/20260310-agentping-browser-control-plane-sdk-session-stack-session-6.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 115 | implementation conversation | 29714 | `.lev/pm/handoffs/20260309-storage-cms-memory-graph-thread-repair-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |

## Next 40 high-value candidates

These are the next highest-value non-archive, non-caution candidates after the first tranche. Process in order, but collapse obvious session series into one provenance note when they are continuations of the same workstream.

| # | Score | Class | Size | Path | Why / handling |
|---:|---:|---|---:|---|---|
| 84 | 79 | implementation conversation | 13084 | `.lev/pm/handoffs/20260307-daemon-runtime-warm-worker-pool-architecture-plan-session-1.md` | current handoff, architecture, daemon, runtime |
| 103 | 79 | implementation conversation | 21268 | `.lev/pm/handoffs/20260309-lev-newcomer-explainer-content-segments-session-1.md` | current handoff, newcomer, explainer, content |
| 109 | 79 | implementation conversation | 7089 | `.lev/pm/handoffs/20260309-paperclip-timetravel-architecture-company-project-model-session-5.md` | current handoff, architecture, timetravel, paperclip |
| 110 | 79 | implementation conversation | 9588 | `.lev/pm/handoffs/20260309-paperclip-timetravel-architecture-lev-agent-boost-session-6.md` | current handoff, architecture, timetravel, paperclip |
| 111 | 79 | implementation conversation | 17586 | `.lev/pm/handoffs/20260309-paperclip-timetravel-architecture-lev-agent-workflows-session-4.md` | current handoff, architecture, timetravel, paperclip |
| 129 | 79 | implementation conversation | 17950 | `.lev/pm/handoffs/20260310-lev-newcomer-explainer-content-segments-session-2.md` | current handoff, newcomer, explainer, content |
| 130 | 79 | implementation conversation | 6273 | `.lev/pm/handoffs/20260310-lev-newcomer-explainer-content-segments-session-3.md` | current handoff, newcomer, explainer, content |
| 136 | 79 | implementation conversation | 9939 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-2.md` | current handoff, sdlc, exec, convergence |
| 137 | 79 | implementation conversation | 13345 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-3.md` | current handoff, sdlc, exec, convergence |
| 138 | 79 | implementation conversation | 15914 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-4.md` | current handoff, sdlc, exec, convergence |
| 139 | 79 | implementation conversation | 19903 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-5.md` | current handoff, sdlc, exec, convergence |
| 140 | 79 | implementation conversation | 6164 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-6.md` | current handoff, sdlc, exec, convergence |
| 141 | 79 | implementation conversation | 5967 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-7.md` | current handoff, sdlc, exec, convergence |
| 143 | 79 | implementation conversation | 7857 | `.lev/pm/handoffs/20260310-sdlc-runtime-exec-handoff-hygiene-session-1.md` | current handoff, sdlc, exec, runtime |
| 1 | 71 | implementation conversation | 26609 | `.lev/pm/handoffs/20260309-droid-intake-transcript-visual-explainer-session-1.md` | current handoff, explainer, droid |
| 58 | 71 | implementation conversation | 28333 | `.lev/pm/handoffs/20260220-flowmind-ratchet-harness.md` | current handoff, flowmind, harness |
| 62 | 71 | implementation conversation | 10580 | `.lev/pm/handoffs/20260221-152500-graph-runtime-sprint.md` | current handoff, graph, runtime |
| 78 | 71 | implementation conversation | 13786 | `.lev/pm/handoffs/20260305-154705-auth-sniffer-skills-reconciliation.md` | current handoff, skill, auth |
| 79 | 71 | implementation conversation | 33146 | `.lev/pm/handoffs/20260306-171351-paperclip-timetravel-bridge.md` | current handoff, timetravel, paperclip |
| 83 | 71 | implementation conversation | 6435 | `.lev/pm/handoffs/20260307-browser-audit-auth-session-design.md` | current handoff, auth, browser |
| 102 | 71 | implementation conversation | 5363 | `.lev/pm/handoffs/20260309-lev-exec-sdk-first-until-fix-session-1.md` | current handoff, exec, sdk |
| 104 | 71 | implementation conversation | 13876 | `.lev/pm/handoffs/20260309-leviathan-graph-analysis-content-lev-homepage-session-4.md` | current handoff, graph, content |
| 105 | 71 | implementation conversation | 10527 | `.lev/pm/handoffs/20260309-mesh-marketplace-virtengine-interleave-session-1.md` | current handoff, marketplace, mesh |
| 106 | 71 | implementation conversation | 24800 | `.lev/pm/handoffs/20260309-mesh-marketplace-virtengine-jeff-ideation-session-1.md` | current handoff, marketplace, mesh |
| 113 | 71 | implementation conversation | 14560 | `.lev/pm/handoffs/20260309-prompt-stack-sdk-absorption-session-2.md` | current handoff, prompt-stack, sdk |
| 117 | 71 | implementation conversation | 9437 | `.lev/pm/handoffs/20260310-120000-harness-flowmind-next.md` | current handoff, flowmind, harness |
| 122 | 71 | implementation conversation | 25046 | `.lev/pm/handoffs/20260310-auth-sniffer-runtime-deep-fixes-session-1.md` | current handoff, auth, runtime |
| 126 | 71 | implementation conversation | 5966 | `.lev/pm/handoffs/20260310-exec-architecture-refactor-session-1.md` | current handoff, architecture, exec |
| 135 | 71 | implementation conversation | 12891 | `.lev/pm/handoffs/20260310-sdlc-convergence-chore-roadmap-session-1.md` | current handoff, sdlc, convergence |
| 151 | 71 | implementation conversation | 12860 | `.lev/pm/handoffs/20260311-sdlc-autodev-heartbeat-session-1.md` | current handoff, sdlc, autodev |
| 153 | 71 | implementation conversation | 2720 | `.lev/pm/handoffs/20260311-substrate-convergence-session-1.md` | current handoff, convergence, substrate |
| 155 | 71 | implementation conversation | 11120 | `.lev/pm/handoffs/20260312-autodev-loop-skill-redesign-session-1.md` | current handoff, autodev, skill |
| 158 | 71 | implementation conversation | 6030 | `.lev/pm/handoffs/20260312-sdlc-autodev-heartbeat-session-3.md` | current handoff, sdlc, autodev |
| 161 | 71 | implementation conversation | 8589 | `.lev/pm/handoffs/20260313-sdlc-autodev-heartbeat-session-5.md` | current handoff, sdlc, autodev |
| 97 | 68 | implementation conversation | 36880 | `.lev/pm/handoffs/20260309-agentping-web-ui-consolidation-session-3.md` | current handoff, agentping |
| 116 | 68 | implementation conversation | 42026 | `.lev/pm/handoffs/20260309-timetravel-bookmarks-smaug-intake-session-1.md` | current handoff, timetravel |
| 30 | 63 | implementation conversation | 3241 | `.lev/handoffs/exec-test-strategy.md` | current handoff, exec |
| 57 | 63 | implementation conversation | 10066 | `.lev/pm/handoffs/20260220-081342-cascading-context-artifact-lifecycle.md` | current handoff, context |
| 63 | 63 | implementation conversation | 14257 | `.lev/pm/handoffs/20260222-graph-infrastructure-session-7.md` | current handoff, graph |
| 64 | 63 | implementation conversation | 28719 | `.lev/pm/handoffs/20260222-work-flowmind-conversion-session-1.md` | current handoff, flowmind |

## Risky, large, or provenance-sensitive files

Do **not** bulk read or import these. Capture file metadata, source URL if present in the first safe lines, and a handling decision. Treat event/index/config content as potentially containing copied prompts, local paths, or source text.

| # | Size | Path | Primary class | Handling |
|---:|---:|---|---|---|
| 27 | 1362074 | `.leann/indexes/lev-code/documents.leann.passages.jsonl` | needs secret/provenance caution | caution: inspect only targeted small slices; redact secrets/private values |
| 15 | 570988 | `workshop/poc/cdo/pocs/consciousness-integration/dmt/andrew_gallimore_dmt_brain_scans_transcript.txt` | unknown | large raw transcript: identify source and summarize provenance only |
| 16 | 190355 | `workshop/poc/cdo/pocs/consciousness-integration/dmt/dmt_clean_transcript.txt` | unknown | large raw transcript: identify source and summarize provenance only |
| 29 | 171520 | `.lev/events.jsonl` | needs secret/provenance caution | caution: inspect only targeted small slices; redact secrets/private values |
| 4 | 163123 | `workshop/analysis/factory-droid-leo-tchourakov/transcript.raw.txt` | unknown | large raw transcript: identify source and summarize provenance only |
| 28 | 9789 | `.lev/config.yaml` | needs secret/provenance caution | caution: inspect only targeted small slices; redact secrets/private values |
| 26 | 275 | `.github/hooks/dcg.json` | needs secret/provenance caution | caution: inspect only targeted small slices; redact secrets/private values |

## Processing protocol for future workers

1. **Metadata first:** record path, size, date encoded in filename, inventory reason, primary class, and whether the file is active/current/archive/caution.
2. **Source lookup before content:** use filename/frontmatter/source URL/references to identify whether the file is a human chat, model session summary, generated report, external video transcript, or repo log.
3. **No truth promotion:** any claim extracted from a handoff/transcript must be marked `claim_status: unverified` until matched to current repo code/docs/decisions.
4. **Small previews only:** for files over 100 KiB, JSONL logs, indexes, config, or raw transcripts, read at most the first safe slice needed for provenance. Do not quote long transcript passages into the wiki.
5. **Secret hygiene:** if a key/token/password/private prompt appears, replace the value with `[REDACTED]`; keep only the path and a minimal note that sensitive content exists.
6. **Archive discipline:** archive/superseded rows may explain history but cannot override active architecture or current source code.
7. **Cluster series:** repeated session-number handoffs (`sdlc-convergence-exec-glue-session-*`, `lev-newcomer-explainer-content-segments-*`, etc.) should be processed as clusters to avoid duplicate wiki claims.
8. **External transcripts:** identify source URL and topic; decide whether the transcript is third-party research evidence, not Leviathan project truth.

## Defer / special handling buckets

### Caution bucket
- `.github/hooks/dcg.json` (275 bytes): runtime/index/config/log; may include prompts, absolute paths, copied source text, or local hook paths.
- `.leann/indexes/lev-code/documents.leann.passages.jsonl` (1362074 bytes): runtime/index/config/log; may include prompts, absolute paths, copied source text, or local hook paths.
- `.lev/config.yaml` (9789 bytes): runtime/index/config/log; may include prompts, absolute paths, copied source text, or local hook paths.
- `.lev/events.jsonl` (171520 bytes): runtime/index/config/log; may include prompts, absolute paths, copied source text, or local hook paths.

### Unknown/external transcript bucket
- `workshop/analysis/factory-droid-leo-tchourakov/transcript.md` (54514 bytes): external transcript/research artifact; provenance/source must be identified before wiki use.
- `workshop/analysis/factory-droid-leo-tchourakov/transcript.raw.txt` (163123 bytes): external transcript/research artifact; provenance/source must be identified before wiki use.
- `workshop/poc/cdo/pocs/consciousness-integration/dmt/andrew_gallimore_dmt_brain_scans_transcript.txt` (570988 bytes): external transcript/research artifact; provenance/source must be identified before wiki use.
- `workshop/poc/cdo/pocs/consciousness-integration/dmt/dmt_clean_transcript.txt` (190355 bytes): external transcript/research artifact; provenance/source must be identified before wiki use.
- `workshop/transcripts/transcript-2LdG-kH4gOY.txt` (8719 bytes): external transcript/research artifact; provenance/source must be identified before wiki use.
- `workshop/transcripts/transcript-DDGcd1JoJV0.txt` (2732 bytes): external transcript/research artifact; provenance/source must be identified before wiki use.
- `workshop/transcripts/transcript-wA6I2vK1N2E.txt` (14383 bytes): external transcript/research artifact; provenance/source must be identified before wiki use.
- `.lev/pm/analysis/session-hooks-simulation-2026-01-25.md` (18012 bytes): no stronger provenance signal from filename/path/size in first pass.

### Legacy/archive bucket
88 rows are legacy/archive or superseded. Defer unless a current page needs historical context. See full classified queue below.

## Full classified queue

Compact first-pass classification for all 250 candidate rows.

### likely Josh/JP chat (0)

_No rows in this class._

### assistant/model transcript (0)

_No rows in this class._

### repo-generated report/log (18)

| # | Class | Size | Path | Handling note |
|---:|---|---:|---|---|
| 2 | repo-generated report/log | 2575 | `.lev/pm/reports/droid-transcript-visual-analysis-2026-03-09.md` | analysis/report generated from repo or source material |
| 5 | repo-generated report/log | 84 | `workshop/analysis/transcript-DDGcd1JoJV0/analysis.md` | analysis/report generated from repo or source material |
| 6 | repo-generated report/log | 5527 | `workshop/analysis/transcript-RDoTY4_xh0s/analysis.md` | analysis/report generated from repo or source material |
| 7 | repo-generated report/log | 4457 | `workshop/analysis/transcript-ePFAVGcPh7U/analysis.md` | analysis/report generated from repo or source material |
| 8 | repo-generated report/log | 84 | `workshop/analysis/transcript-f1-graphics/analysis.md` | analysis/report generated from repo or source material |
| 9 | repo-generated report/log | 90 | `workshop/analysis/transcript-fireship-remotion/analysis.md` | analysis/report generated from repo or source material |
| 10 | repo-generated report/log | 1997 | `workshop/analysis/transcript-obsidian-qmd-cluster/analysis.md` | analysis/report generated from repo or source material |
| 11 | repo-generated report/log | 4891 | `workshop/analysis/transcript-qiOu7Ptjxng/analysis.md` | analysis/report generated from repo or source material |
| 12 | repo-generated report/log | 2645 | `workshop/analysis/transcript-redis-context-engine/analysis.md` | analysis/report generated from repo or source material |
| 13 | repo-generated report/log | 93 | `workshop/analysis/transcript-spotify-wrapped-2025/analysis.md` | analysis/report generated from repo or source material |
| 14 | repo-generated report/log | 1442 | `workshop/analysis/transcript-triage.md` | analysis/report generated from repo or source material |
| 20 | repo-generated report/log | 4835 | `.agents/skills/workflow-api2cli-api2cdp-manual-lifecycle/SKILL.md` | agent/tool config, command shim, rules doc, or index manifest matched by keyword |
| 21 | repo-generated report/log | 2392 | `.agents/skills/workflow-dotfiles-sync/SKILL.md` | agent/tool config, command shim, rules doc, or index manifest matched by keyword |
| 22 | repo-generated report/log | 1803 | `.claude/commands/handoff-resume.md` | agent/tool config, command shim, rules doc, or index manifest matched by keyword |
| 23 | repo-generated report/log | 651 | `.claude/commands/handoff.md` | agent/tool config, command shim, rules doc, or index manifest matched by keyword |
| 24 | repo-generated report/log | 7988 | `.claude/commands/lev-dashboard.md` | agent/tool config, command shim, rules doc, or index manifest matched by keyword |
| 25 | repo-generated report/log | 4425 | `.cursor/rules/README.md` | agent/tool config, command shim, rules doc, or index manifest matched by keyword |
| 31 | repo-generated report/log | 9195 | `.lev/indexes/manifest.yaml` | agent/tool config, command shim, rules doc, or index manifest matched by keyword |

### product/design discussion (6)

| # | Class | Size | Path | Handling note |
|---:|---|---:|---|---|
| 50 | product/design discussion | 4151 | `.lev/pm/decisions/d16-dogfood-is-preset-plugin-first.md` | design/decision planning surface; useful for intent, not current truth |
| 51 | product/design discussion | 4535 | `.lev/pm/designs/agent-adapter-e2e-plan.md` | design/decision planning surface; useful for intent, not current truth |
| 52 | product/design discussion | 29535 | `.lev/pm/designs/leviathan-meta-framework.md` | design/decision planning surface; useful for intent, not current truth |
| 53 | product/design discussion | 42817 | `.lev/pm/designs/phase-3-jobtype-recognition-architecture.md` | design/decision planning surface; useful for intent, not current truth |
| 54 | product/design discussion | 32926 | `.lev/pm/designs/phase-5-agentic-compiler-architecture.md` | design/decision planning surface; useful for intent, not current truth |
| 55 | product/design discussion | 35975 | `.lev/pm/designs/phase4-weight-system-architecture.md` | design/decision planning surface; useful for intent, not current truth |

### implementation conversation (126)

| # | Class | Size | Path | Handling note |
|---:|---|---:|---|---|
| 1 | implementation conversation | 26609 | `.lev/pm/handoffs/20260309-droid-intake-transcript-visual-explainer-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 30 | implementation conversation | 3241 | `.lev/handoffs/exec-test-strategy.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 56 | implementation conversation | 2511 | `.lev/pm/handoffs/20260216-hard-cut-supersession-index.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 57 | implementation conversation | 10066 | `.lev/pm/handoffs/20260220-081342-cascading-context-artifact-lifecycle.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 58 | implementation conversation | 28333 | `.lev/pm/handoffs/20260220-flowmind-ratchet-harness.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 59 | implementation conversation | 15673 | `.lev/pm/handoffs/20260220-lev-forge-cdo-handoff.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 60 | implementation conversation | 10715 | `.lev/pm/handoffs/20260220-repo-restructure-public-lev.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 61 | implementation conversation | 37020 | `.lev/pm/handoffs/20260220-sprint-planning-workflow-codification.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 62 | implementation conversation | 10580 | `.lev/pm/handoffs/20260221-152500-graph-runtime-sprint.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 63 | implementation conversation | 14257 | `.lev/pm/handoffs/20260222-graph-infrastructure-session-7.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 64 | implementation conversation | 28719 | `.lev/pm/handoffs/20260222-work-flowmind-conversion-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 65 | implementation conversation | 13571 | `.lev/pm/handoffs/20260223-sdlc-tooling-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 66 | implementation conversation | 7543 | `.lev/pm/handoffs/20260224-064844-platform-binding-event-provider-alignment-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 67 | implementation conversation | 1634 | `.lev/pm/handoffs/20260224-pi-agentping-integration-handoff.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 68 | implementation conversation | 4635 | `.lev/pm/handoffs/20260224-runtime-mvp-critical-plan-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 69 | implementation conversation | 32088 | `.lev/pm/handoffs/20260224-work-flowmind-protocol-integration-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 70 | implementation conversation | 6844 | `.lev/pm/handoffs/20260227-kingly-platform-strategy-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 71 | implementation conversation | 20678 | `.lev/pm/handoffs/20260303-ecosystem-intake-framework-audit-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 72 | implementation conversation | 11815 | `.lev/pm/handoffs/20260303-lev-agentic-dx-audit-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 73 | implementation conversation | 5935 | `.lev/pm/handoffs/20260303-offgrid-session-3.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 74 | implementation conversation | 14743 | `.lev/pm/handoffs/20260303-sdk-first-cross-lang-compliance.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 75 | implementation conversation | 19110 | `.lev/pm/handoffs/20260303-voice-dashboard-10-step-plan.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 76 | implementation conversation | 24807 | `.lev/pm/handoffs/20260303-voice-dashboard-plugin-native.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 77 | implementation conversation | 7694 | `.lev/pm/handoffs/20260303-voice-dashboard-session-handoff.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 78 | implementation conversation | 13786 | `.lev/pm/handoffs/20260305-154705-auth-sniffer-skills-reconciliation.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 79 | implementation conversation | 33146 | `.lev/pm/handoffs/20260306-171351-paperclip-timetravel-bridge.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 80 | implementation conversation | 21751 | `.lev/pm/handoffs/20260306-190740-notion-plugin-cli-and-surface.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 81 | implementation conversation | 25630 | `.lev/pm/handoffs/20260306-agents-work-reconcile-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 82 | implementation conversation | 16029 | `.lev/pm/handoffs/20260307-agentping-web-ui-consolidation-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 83 | implementation conversation | 6435 | `.lev/pm/handoffs/20260307-browser-audit-auth-session-design.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 84 | implementation conversation | 13084 | `.lev/pm/handoffs/20260307-daemon-runtime-warm-worker-pool-architecture-plan-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 85 | implementation conversation | 13635 | `.lev/pm/handoffs/20260307-ecosystem-intake-mastra-engram-runtime-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 86 | implementation conversation | 2805 | `.lev/pm/handoffs/20260307-hybrid-type-contracts-session.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 87 | implementation conversation | 14488 | `.lev/pm/handoffs/20260307-levui-ir-genui-vision-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 88 | implementation conversation | 5936 | `.lev/pm/handoffs/20260307-marketplace-gtm-bundle-sprint.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 89 | implementation conversation | 3011 | `.lev/pm/handoffs/20260307-phase1-implementation-pr61.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 90 | implementation conversation | 8688 | `.lev/pm/handoffs/20260307-pi-host-adapter-refactor.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 91 | implementation conversation | 16464 | `.lev/pm/handoffs/20260307-pr-merge-train-github-review-fix-merge-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 92 | implementation conversation | 2819 | `.lev/pm/handoffs/20260307-rust-knowledge-pipeline-handoff.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 93 | implementation conversation | 2179 | `.lev/pm/handoffs/20260307-warm-worker-pool-gate-validation.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 94 | implementation conversation | 18283 | `.lev/pm/handoffs/20260307-work-skill-contract-pass1-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 95 | implementation conversation | 2122 | `.lev/pm/handoffs/20260308-bookmark-ingest-agent-session33-handoff.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 96 | implementation conversation | 6231 | `.lev/pm/handoffs/20260308-doc-lifecycle-cleanup-agent-handoff.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 97 | implementation conversation | 36880 | `.lev/pm/handoffs/20260309-agentping-web-ui-consolidation-session-3.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 98 | implementation conversation | 17033 | `.lev/pm/handoffs/20260309-agentping-web-ui-consolidation-session-4.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 99 | implementation conversation | 15216 | `.lev/pm/handoffs/20260309-claude-codex-base-harness-contract-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 100 | implementation conversation | 6829 | `.lev/pm/handoffs/20260309-e2e-test-suite-repair.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 101 | implementation conversation | 22472 | `.lev/pm/handoffs/20260309-ext-deps-onboarding-smaug-futureproof-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 102 | implementation conversation | 5363 | `.lev/pm/handoffs/20260309-lev-exec-sdk-first-until-fix-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 103 | implementation conversation | 21268 | `.lev/pm/handoffs/20260309-lev-newcomer-explainer-content-segments-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 104 | implementation conversation | 13876 | `.lev/pm/handoffs/20260309-leviathan-graph-analysis-content-lev-homepage-session-4.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 105 | implementation conversation | 10527 | `.lev/pm/handoffs/20260309-mesh-marketplace-virtengine-interleave-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 106 | implementation conversation | 24800 | `.lev/pm/handoffs/20260309-mesh-marketplace-virtengine-jeff-ideation-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 107 | implementation conversation | 9757 | `.lev/pm/handoffs/20260309-notionctl-plugin-core-execution-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 108 | implementation conversation | 10845 | `.lev/pm/handoffs/20260309-ops-sync-dashboard-chezmoi-agents-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 109 | implementation conversation | 7089 | `.lev/pm/handoffs/20260309-paperclip-timetravel-architecture-company-project-model-session-5.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 110 | implementation conversation | 9588 | `.lev/pm/handoffs/20260309-paperclip-timetravel-architecture-lev-agent-boost-session-6.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 111 | implementation conversation | 17586 | `.lev/pm/handoffs/20260309-paperclip-timetravel-architecture-lev-agent-workflows-session-4.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 112 | implementation conversation | 12778 | `.lev/pm/handoffs/20260309-prompt-stack-plugin-bidirectional-stopgap-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 113 | implementation conversation | 14560 | `.lev/pm/handoffs/20260309-prompt-stack-sdk-absorption-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 114 | implementation conversation | 9307 | `.lev/pm/handoffs/20260309-sdlc-hygiene-handoff-lifecycle-encoding-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 115 | implementation conversation | 29714 | `.lev/pm/handoffs/20260309-storage-cms-memory-graph-thread-repair-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 116 | implementation conversation | 42026 | `.lev/pm/handoffs/20260309-timetravel-bookmarks-smaug-intake-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 117 | implementation conversation | 9437 | `.lev/pm/handoffs/20260310-120000-harness-flowmind-next.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 118 | implementation conversation | 2856 | `.lev/pm/handoffs/20260310-120000-pr87-branch-alignment.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 119 | implementation conversation | 31682 | `.lev/pm/handoffs/20260310-agentping-browser-control-plane-sdk-session-stack-session-6.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 120 | implementation conversation | 29687 | `.lev/pm/handoffs/20260310-agentping-core-thread-centric-conversion-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 121 | implementation conversation | 11738 | `.lev/pm/handoffs/20260310-agentping-standalone-host-and-surface-proof-session-5.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 122 | implementation conversation | 25046 | `.lev/pm/handoffs/20260310-auth-sniffer-runtime-deep-fixes-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 123 | implementation conversation | 13460 | `.lev/pm/handoffs/20260310-autodev-loop-operationalization-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 124 | implementation conversation | 18050 | `.lev/pm/handoffs/20260310-chore-loop-session.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 125 | implementation conversation | 2740 | `.lev/pm/handoffs/20260310-core-alignment-chore-loop-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 126 | implementation conversation | 5966 | `.lev/pm/handoffs/20260310-exec-architecture-refactor-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 127 | implementation conversation | 17919 | `.lev/pm/handoffs/20260310-flowmind-graph-alignment-meta-interview-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 128 | implementation conversation | 20665 | `.lev/pm/handoffs/20260310-flowmind-harness-control-plane-boundary-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 129 | implementation conversation | 17950 | `.lev/pm/handoffs/20260310-lev-newcomer-explainer-content-segments-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 130 | implementation conversation | 6273 | `.lev/pm/handoffs/20260310-lev-newcomer-explainer-content-segments-session-3.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 131 | implementation conversation | 7056 | `.lev/pm/handoffs/20260310-pr100-evolve-memory-review-fixes-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 132 | implementation conversation | 2193 | `.lev/pm/handoffs/20260310-remaining-chores-handoff.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 133 | implementation conversation | 2249 | `.lev/pm/handoffs/20260310-sdk-cutover-complete-session-final.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 134 | implementation conversation | 3348 | `.lev/pm/handoffs/20260310-sdk-cutover-sentinel-alignment-session-3.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 135 | implementation conversation | 12891 | `.lev/pm/handoffs/20260310-sdlc-convergence-chore-roadmap-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 136 | implementation conversation | 9939 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 137 | implementation conversation | 13345 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-3.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 138 | implementation conversation | 15914 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-4.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 139 | implementation conversation | 19903 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-5.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 140 | implementation conversation | 6164 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-6.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 141 | implementation conversation | 5967 | `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-7.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 142 | implementation conversation | 16225 | `.lev/pm/handoffs/20260310-sdlc-flowmind-deepen-validate-hygiene-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 143 | implementation conversation | 7857 | `.lev/pm/handoffs/20260310-sdlc-runtime-exec-handoff-hygiene-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 144 | implementation conversation | 28274 | `.lev/pm/handoffs/20260310-sdlc-workgraph-deterministic-lifecycle-convergence-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 145 | implementation conversation | 2576 | `.lev/pm/handoffs/20260310-sdlc-workgraph-deterministic-lifecycle-convergence-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 146 | implementation conversation | 16156 | `.lev/pm/handoffs/20260311-execution-dag-exec-stress-import-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 147 | implementation conversation | 26531 | `.lev/pm/handoffs/20260311-flowmind-masfactory-parity-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 148 | implementation conversation | 17455 | `.lev/pm/handoffs/20260311-flowmind-masfactory-parity-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 149 | implementation conversation | 5272 | `.lev/pm/handoffs/20260311-gen-ui-session-shell-poc-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 150 | implementation conversation | 14966 | `.lev/pm/handoffs/20260311-graph-convergence-session-3.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 151 | implementation conversation | 12860 | `.lev/pm/handoffs/20260311-sdlc-autodev-heartbeat-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 152 | implementation conversation | 5629 | `.lev/pm/handoffs/20260311-sdlc-control-plane-pilot-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 153 | implementation conversation | 2720 | `.lev/pm/handoffs/20260311-substrate-convergence-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 154 | implementation conversation | 14579 | `.lev/pm/handoffs/20260311-work-mvp-flowmind-replatform-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 155 | implementation conversation | 11120 | `.lev/pm/handoffs/20260312-autodev-loop-skill-redesign-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 156 | implementation conversation | 6348 | `.lev/pm/handoffs/20260312-graph-deep-research.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 157 | implementation conversation | 11245 | `.lev/pm/handoffs/20260312-orchestration-entity-placement-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 158 | implementation conversation | 6030 | `.lev/pm/handoffs/20260312-sdlc-autodev-heartbeat-session-3.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 159 | implementation conversation | 22218 | `.lev/pm/handoffs/20260312-sdlc-autodev-heartbeat-session-4.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 160 | implementation conversation | 17978 | `.lev/pm/handoffs/20260313-cdo-architecture-deliberation-session-8.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 161 | implementation conversation | 8589 | `.lev/pm/handoffs/20260313-sdlc-autodev-heartbeat-session-5.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 162 | implementation conversation | 29467 | `.lev/pm/handoffs/20260313-sdlc-autodev-heartbeat-session-6.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 163 | implementation conversation | 23839 | `.lev/pm/handoffs/20260314-architecture-decisions-session-9.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 164 | implementation conversation | 3836 | `.lev/pm/handoffs/20260314-autodev-loop-drift-scan-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 165 | implementation conversation | 8689 | `.lev/pm/handoffs/20260314-bench-core-bench-plugin-promotion-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 166 | implementation conversation | 19691 | `.lev/pm/handoffs/20260314-branch-consolidation-catalogue.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 167 | implementation conversation | 11549 | `.lev/pm/handoffs/20260314-consolidation-bugfix-experimentation-session-2.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 168 | implementation conversation | 13683 | `.lev/pm/handoffs/20260314-infra-index-beads-cleanup-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 169 | implementation conversation | 29807 | `.lev/pm/handoffs/20260314-poly-daemon-production-ready-session-15.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 170 | implementation conversation | 9925 | `.lev/pm/handoffs/20260314-s10-execution-session-10.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 171 | implementation conversation | 5999 | `.lev/pm/handoffs/20260314-s11-cdo-decisions-reconciliation-session-11.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 172 | implementation conversation | 9191 | `.lev/pm/handoffs/20260314-s12-reconciliation-rollup-session-12.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 173 | implementation conversation | 15726 | `.lev/pm/handoffs/20260314-s13-architecture-plane-separation-session-13.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 174 | implementation conversation | 16334 | `.lev/pm/handoffs/20260314-s14-architecture-plane-separation-session-14.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 175 | implementation conversation | 5618 | `.lev/pm/handoffs/20260314-s14-retro-poly-drift-remediation-session-14.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 176 | implementation conversation | 14200 | `.lev/pm/handoffs/20260314-s16-skill-infrastructure-session-16.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 177 | implementation conversation | 32273 | `.lev/pm/handoffs/20260314-s17-arscontexta-skill-graph-social-session-17.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 178 | implementation conversation | 11839 | `.lev/pm/handoffs/20260315-poly-remediation-bdd-coverage-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |
| 179 | implementation conversation | 2197 | `.lev/pm/handoffs/20260315-wave1-5-parallel-implementation-session-1.md` | session handoff / implementation continuity artifact; likely assistant-authored summary |

### legacy/archive (88)

| # | Class | Size | Path | Handling note |
|---:|---|---:|---|---|
| 33 | legacy/archive | 9311 | `.lev/pm/archive/scratch-202601/cognee-cgf-synthesis.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 34 | legacy/archive | 9505 | `.lev/pm/archive/scratch-202601/context-graph-research.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 35 | legacy/archive | 41196 | `.lev/pm/archive/scratch-202601/context-graph-timetravel-results.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 36 | legacy/archive | 10285 | `.lev/pm/archive/scratch-202601/intake-claude-code-langfuse-template.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 37 | legacy/archive | 15184 | `.lev/pm/archive/scratch-202601/lev-dashboard-prior-art.yaml` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 38 | legacy/archive | 17553 | `.lev/pm/archive/scratch-202601/self-learning-os-prd.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 39 | legacy/archive | 7027 | `.lev/pm/archive/scratch-202601/spike-graphiti-connection.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 40 | legacy/archive | 5956 | `.lev/pm/archive/sdk-first-superseded/20260220-204524-sdk-first-poly-daemon-proposal.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 41 | legacy/archive | 3345 | `.lev/pm/archive/sdk-first-superseded/20260220-211521-sdk-first-docs-alignment-handoff.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 42 | legacy/archive | 8229 | `.lev/pm/archive/sdk-first-superseded/20260220-213118-poly-daemon-reconciliation-r3.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 43 | legacy/archive | 9057 | `.lev/pm/archive/sdk-first-superseded/20260221-112513-harness-sdk-poly-checkpoint.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 44 | legacy/archive | 7958 | `.lev/pm/archive/sdk-first-superseded/20260222-151845-sdk-first-poly-hard-cut-sprint.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 45 | legacy/archive | 58716 | `.lev/pm/archive/sdk-first-superseded/20260307-013915-poly-robot-mode-sdk-first-roadmap.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 46 | legacy/archive | 5722 | `.lev/pm/archive/sdk-first-superseded/spec-machine-contract-schema-codegen-2026-03-07.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 47 | legacy/archive | 11282 | `.lev/pm/archive/sdk-first-superseded/spec-poly-robot-mode-canonicalization-2026-03-07.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 48 | legacy/archive | 11750 | `.lev/pm/archive/sdk-first-superseded/spec-sdk-first-poly-daemon-canonical-convergence-2026-02-20.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 49 | legacy/archive | 8232 | `.lev/pm/archive/sdk-first-superseded/spec-sdk-first-root-cli-thin-adapter-2026-03-07.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 180 | legacy/archive | 11329 | `.lev/pm/handoffs/archive/20260104-022433-protocol-semantics-openskills.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 181 | legacy/archive | 10294 | `.lev/pm/handoffs/archive/20260104-032609-lev-2mzu-agent-src-migration.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 182 | legacy/archive | 16670 | `.lev/pm/handoffs/archive/20260104-033500-agency-gastown-context-protocol.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 183 | legacy/archive | 9749 | `.lev/pm/handoffs/archive/20260105-124500-lev-find-deps-xdg.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 184 | legacy/archive | 7496 | `.lev/pm/handoffs/archive/20260105-124500-poly-status-recon.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 185 | legacy/archive | 9573 | `.lev/pm/handoffs/archive/20260105-174500-prose-flowmind-evaluation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 186 | legacy/archive | 7168 | `.lev/pm/handoffs/archive/20260106-120500-flowmind-v2-meta-prompt-templates.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 187 | legacy/archive | 11562 | `.lev/pm/handoffs/archive/20260106-145500-vectorindex-benchmarks-four-issue-research.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 188 | legacy/archive | 13993 | `.lev/pm/handoffs/archive/20260106-171308-parallel-swarm-config-debt.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 189 | legacy/archive | 13496 | `.lev/pm/handoffs/archive/20260106-171929-poly-xdg-deps-boot-architecture.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 190 | legacy/archive | 10742 | `.lev/pm/handoffs/archive/20260106-200138-lev-surface-area-protocol-handlers.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 191 | legacy/archive | 20780 | `.lev/pm/handoffs/archive/20260107-002319-skill-discovery-metadata-index.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 192 | legacy/archive | 10290 | `.lev/pm/handoffs/archive/20260107-002351-parallel-swarm-ontology-dashboard.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 193 | legacy/archive | 6998 | `.lev/pm/handoffs/archive/20260107-003337-next-steps-metadata-index.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 194 | legacy/archive | 10551 | `.lev/pm/handoffs/archive/20260107-203500-lev-dashboard-shell-planning.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 195 | legacy/archive | 9356 | `.lev/pm/handoffs/archive/20260111-043058-lev-align-north-star-alignment.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 196 | legacy/archive | 10556 | `.lev/pm/handoffs/archive/20260111-043058-lev-align-north-star.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 197 | legacy/archive | 8398 | `.lev/pm/handoffs/archive/20260111-050104-lev-align-north-star.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 198 | legacy/archive | 9129 | `.lev/pm/handoffs/archive/20260111-050319-alignment-audit-north-star.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 199 | legacy/archive | 10397 | `.lev/pm/handoffs/archive/20260111-051450-lev-align-alignment-audit.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 200 | legacy/archive | 9645 | `.lev/pm/handoffs/archive/20260113-204500-dashboard-gap-consolidation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 201 | legacy/archive | 11277 | `.lev/pm/handoffs/archive/20260114-223900-lev-tooling-integration-scout.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 202 | legacy/archive | 5494 | `.lev/pm/handoffs/archive/20260114-233318-alignment-north-star-and-lev-align.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 203 | legacy/archive | 4171 | `.lev/pm/handoffs/archive/20260115-061800-lev-lifecycle-restructure.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 204 | legacy/archive | 11153 | `.lev/pm/handoffs/archive/20260115-071500-openprose-claude-prose-architecture.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 205 | legacy/archive | 10256 | `.lev/pm/handoffs/archive/20260115-235849-command-skill-reorg-sdk-design.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 206 | legacy/archive | 11782 | `.lev/pm/handoffs/archive/20260116-002500-ralph-decoupling-sdk-consolidation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 207 | legacy/archive | 11257 | `.lev/pm/handoffs/archive/20260116-013909-lev-exec-consolidation-plan.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 208 | legacy/archive | 12026 | `.lev/pm/handoffs/archive/20260116-024500-flowmind-graph-unification-planning.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 209 | legacy/archive | 12070 | `.lev/pm/handoffs/archive/20260117-000536-lev-context-yaml-architecture.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 210 | legacy/archive | 10214 | `.lev/pm/handoffs/archive/20260117-003500-lev-extensibility-framework-complete.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 211 | legacy/archive | 8530 | `.lev/pm/handoffs/archive/20260117-004646-cdo-runner-and-lcars-foundation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 212 | legacy/archive | 15117 | `.lev/pm/handoffs/archive/20260117-013138-skill-consolidation-core-reorg.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 213 | legacy/archive | 5600 | `.lev/pm/handoffs/archive/20260117-033453-agent-first-handler-types.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 214 | legacy/archive | 10738 | `.lev/pm/handoffs/archive/20260117-043301-graph-builder-e2e-repair.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 215 | legacy/archive | 13241 | `.lev/pm/handoffs/archive/20260117-052959-fractal-polymorph-architecture.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 216 | legacy/archive | 13346 | `.lev/pm/handoffs/archive/20260117-064500-rfc-convo-scanner-lifecycle.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 217 | legacy/archive | 13093 | `.lev/pm/handoffs/archive/20260117-070000-sources-yaml-implementation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 218 | legacy/archive | 9310 | `.lev/pm/handoffs/archive/20260117-072350-lev-exec-model-routing-fix.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 219 | legacy/archive | 4998 | `.lev/pm/handoffs/archive/20260117-073947-polyglot-graph-phase123-complete.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 220 | legacy/archive | 9743 | `.lev/pm/handoffs/archive/20260117-075830-hexagonal-index-overhaul-complete.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 221 | legacy/archive | 4606 | `.lev/pm/handoffs/archive/20260117-081617-lev-666h-graph-migration.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 222 | legacy/archive | 16981 | `.lev/pm/handoffs/archive/20260117-092252-10x-production-refactor-iterate-improve.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 223 | legacy/archive | 14634 | `.lev/pm/handoffs/archive/20260117-092501-dashboard-0.1.0-complete.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 224 | legacy/archive | 9832 | `.lev/pm/handoffs/archive/20260117-103000-core-build-platform-adapters.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 225 | legacy/archive | 4043 | `.lev/pm/handoffs/archive/20260117-143500-dag-algorithm-fix-discovery.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 226 | legacy/archive | 10772 | `.lev/pm/handoffs/archive/20260117-145714-ci-debug-gh-cli-remaining.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 227 | legacy/archive | 13124 | `.lev/pm/handoffs/archive/20260117-145800-lev-meta-mode-ralph-dag.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 228 | legacy/archive | 10835 | `.lev/pm/handoffs/archive/20260117-185100-ralph-mcp-codifier-remaining.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 229 | legacy/archive | 10634 | `.lev/pm/handoffs/archive/20260119-122312-core-reorg-lifecycle-rename.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 230 | legacy/archive | 6942 | `.lev/pm/handoffs/archive/20260119-124500-lifecycle-observe-rename-complete.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 231 | legacy/archive | 8128 | `.lev/pm/handoffs/archive/20260120-185724-skills-ecosystem-discovery.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 232 | legacy/archive | 5928 | `.lev/pm/handoffs/archive/20260120-190500-cli-architecture-consolidation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 233 | legacy/archive | 5145 | `.lev/pm/handoffs/archive/20260120-191949-xdg-migration-scheduler.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 234 | legacy/archive | 3687 | `.lev/pm/handoffs/archive/20260120-235449-dependabot-vuln-remediation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 235 | legacy/archive | 12399 | `.lev/pm/handoffs/archive/20260121-010822-cli-router-registry-first.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 236 | legacy/archive | 12847 | `.lev/pm/handoffs/archive/20260121-013500-harness-architecture-ralph-loop-primitives.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 237 | legacy/archive | 11308 | `.lev/pm/handoffs/archive/20260121-094324-harness-interface-consolidation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 238 | legacy/archive | 20754 | `.lev/pm/handoffs/archive/20260121-094500-lev-skills-audit-consolidation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 239 | legacy/archive | 5567 | `.lev/pm/handoffs/archive/20260121-095627-ci-cd-dependabot-remediation.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 240 | legacy/archive | 5147 | `.lev/pm/handoffs/archive/20260121-101500-schema-migration-cdo-gap.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 241 | legacy/archive | 22757 | `.lev/pm/handoffs/archive/20260121-120500-cognee-poly-integration-spike.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 242 | legacy/archive | 10865 | `.lev/pm/handoffs/archive/20260121-155935-lev-exec-tmux-escape-spike.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 243 | legacy/archive | 18314 | `.lev/pm/handoffs/archive/20260121-162253-lev-claude-adapter-epic.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 244 | legacy/archive | 7455 | `.lev/pm/handoffs/archive/20260121-183301-agent-adapter-scanner-architecture.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 245 | legacy/archive | 8380 | `.lev/pm/handoffs/archive/20260121-183947-cdo-debug-lev-graph-decision-intake.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 246 | legacy/archive | 8442 | `.lev/pm/handoffs/archive/20260121-185500-cdo-lev-graph-proper-run.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 247 | legacy/archive | 8883 | `.lev/pm/handoffs/archive/20260121-202500-cognee-poly-graph-synthesis.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 248 | legacy/archive | 7729 | `.lev/pm/handoffs/archive/20260121-212815-context-consolidation-harness-architecture.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 249 | legacy/archive | 11029 | `.lev/pm/handoffs/archive/20260121-cdo-lev-graph-final.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |
| 250 | legacy/archive | 3607 | `.lev/pm/handoffs/archive/20260121-cdo-lev-graph-poc.md` | archive/superseded path; prior-art only unless corroborated by current code/docs |

### needs secret/provenance caution (4)

| # | Class | Size | Path | Handling note |
|---:|---|---:|---|---|
| 26 | needs secret/provenance caution | 275 | `.github/hooks/dcg.json` | runtime/index/config/log; may include prompts, absolute paths, copied source text, or local hook paths |
| 27 | needs secret/provenance caution | 1362074 | `.leann/indexes/lev-code/documents.leann.passages.jsonl` | runtime/index/config/log; may include prompts, absolute paths, copied source text, or local hook paths |
| 28 | needs secret/provenance caution | 9789 | `.lev/config.yaml` | runtime/index/config/log; may include prompts, absolute paths, copied source text, or local hook paths |
| 29 | needs secret/provenance caution | 171520 | `.lev/events.jsonl` | runtime/index/config/log; may include prompts, absolute paths, copied source text, or local hook paths |

### unknown (8)

| # | Class | Size | Path | Handling note |
|---:|---|---:|---|---|
| 3 | unknown | 54514 | `workshop/analysis/factory-droid-leo-tchourakov/transcript.md` | external transcript/research artifact; provenance/source must be identified before wiki use |
| 4 | unknown | 163123 | `workshop/analysis/factory-droid-leo-tchourakov/transcript.raw.txt` | external transcript/research artifact; provenance/source must be identified before wiki use |
| 15 | unknown | 570988 | `workshop/poc/cdo/pocs/consciousness-integration/dmt/andrew_gallimore_dmt_brain_scans_transcript.txt` | external transcript/research artifact; provenance/source must be identified before wiki use |
| 16 | unknown | 190355 | `workshop/poc/cdo/pocs/consciousness-integration/dmt/dmt_clean_transcript.txt` | external transcript/research artifact; provenance/source must be identified before wiki use |
| 17 | unknown | 8719 | `workshop/transcripts/transcript-2LdG-kH4gOY.txt` | external transcript/research artifact; provenance/source must be identified before wiki use |
| 18 | unknown | 2732 | `workshop/transcripts/transcript-DDGcd1JoJV0.txt` | external transcript/research artifact; provenance/source must be identified before wiki use |
| 19 | unknown | 14383 | `workshop/transcripts/transcript-wA6I2vK1N2E.txt` | external transcript/research artifact; provenance/source must be identified before wiki use |
| 32 | unknown | 18012 | `.lev/pm/analysis/session-hooks-simulation-2026-01-25.md` | no stronger provenance signal from filename/path/size in first pass |
