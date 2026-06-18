---
title: Leviathan Current Source Inventory 2026-06-17
created: 2026-06-17
type: source-inventory
status: inventory / not full readthrough
claim_ceiling: file inventory and routing signal; not conceptual synthesis, not implementation proof
---

# Leviathan Current Source Inventory 2026-06-17

## Scope

- Repo: `/Users/joshuaeisenhart/GitHub/leviathan`
- Remote checked: `https://github.com/lev-os/leviathan`
- HEAD checked: `a661ecbf410469becd7b89c3bfc5ee215721ae34`
- Exclusions for this inventory: `.git`, `node_modules`, build/dist/cache/target/vendor/venv folders.
- Status: **inventory only**. It lists what must be read; it does not claim those files have been understood.

## Counts

- Files inventoried: **12699**
- Text/code-like files: **11382**
- Markdown/MDX files: **4848**

## Top-level shape

| path | files |
|---|---:|
| `workshop` | 4018 |
| `_archive` | 2006 |
| `core` | 1471 |
| `os` | 1062 |
| `.lev` | 853 |
| `plugins` | 774 |
| `apps` | 507 |
| `research` | 344 |
| `context` | 302 |
| `docs` | 300 |
| `crates` | 232 |
| `tests` | 231 |
| `packages` | 207 |
| `reports` | 105 |
| `tooling` | 95 |
| `community` | 62 |
| `.leann` | 15 |
| `.github` | 15 |
| `.serena` | 10 |
| `.claude` | 10 |
| `.cursor` | 9 |
| `.sisyphus` | 4 |
| `.obsidian` | 4 |
| `agents` | 4 |
| `examples` | 4 |
| `.agents` | 3 |
| `.vscode` | 3 |
| `.cass` | 2 |
| `.changeset` | 2 |
| `.agent-lease` | 2 |
| `.cursorignore` | 1 |
| `pnpm-lock.yaml` | 1 |
| `.envrc` | 1 |
| `.DS_Store` | 1 |
| `josh-flowmind-spec.zip` | 1 |
| `LICENSE` | 1 |
| `CHANGELOG.md` | 1 |
| `tsconfig.base.json` | 1 |
| `Makefile` | 1 |
| `.tldrignore` | 1 |

## Authority surfaces found

- `README.md` (3878 bytes)
- `AGENTS.md` (24573 bytes)
- `CLAUDE.md` (11 bytes)
- `docs/README.md` (2015 bytes)
- `docs/NORTH_STAR.md` (17776 bytes)
- `docs/ROADMAP.md` (9175 bytes)
- `docs/ARCHITECTURE.md` (24719 bytes)
- `package.json` (7103 bytes)
- `pnpm-workspace.yaml` (848 bytes)

## Package / workspace contract files

- `.lev/qoho/clawd-payload/package.json`
- `_archive/agent/package.json`
- `_archive/infra/qoho-clawdbot/lume-handler/package.json`
- `_archive/infra/qoho-clawdbot/package.json`
- `_archive/lib-middleware/package.json`
- `_archive/lib-watch/package.json`
- `apps/_archive/old-dash/package.json`
- `apps/auth-proxy/package.json`
- `apps/auth-proxy/turbo.json`
- `apps/desktop/package.json`
- `apps/desktop/packages/electron-versions/package.json`
- `apps/desktop/packages/integrate-renderer/package.json`
- `apps/desktop/packages/main/package.json`
- `apps/desktop/packages/preload/package.json`
- `apps/desktop/packages/renderer/package.json`
- `apps/expo/package.json`
- `apps/expo/turbo.json`
- `apps/landing-astro/package.json`
- `apps/max/package.json`
- `apps/nextjs/package.json`
- `apps/nextjs/turbo.json`
- `apps/universal-preview/backend/package.json`
- `apps/universal-preview/package.json`
- `apps/video/package.json`
- `apps/voice-api/package.json`
- `apps/voice-api/turbo.json`
- `community/lev-forge/crates/forge-core/Cargo.toml`
- `context/schema/package.json`
- `core/config/package.json`
- `core/daemon/package.json`
- `core/domain/package.json`
- `core/event-bus/analytics/lev-learn/pyproject.toml`
- `core/event-bus/package.json`
- `core/event-machines/package.json`
- `core/event-providers/package.json`
- `core/exec/package.json`
- `core/flowmind/package.json`
- `core/graph/package.json`
- `core/harness/package.json`
- `core/index/adapters/osgrep/package.json`
- `core/index/package.json`
- `core/index/pyproject.toml`
- `core/logger/package.json`
- `core/memory/package.json`
- `core/memory/src/algorithms/rust/Cargo.toml`
- `core/memory/src/algorithms/rust/mpfp/Cargo.toml`
- `core/memory/src/algorithms/rust/rrf/Cargo.toml`
- `core/orchestration/package.json`
- `core/poly/package.json`
- `core/poly/sdk/python/pyproject.toml`
- `core/poly/sdk/rust/Cargo.toml`
- `core/poly/sdk/rust/test_host/Cargo.toml`
- `core/poly/sdk/typescript/package.json`
- `core/poly/src/codegen/package.json`
- `core/poly/src/sdk/package.json`
- `core/poly/tests/cross-language/Cargo.toml`
- `core/telemetry/package.json`
- `core/ui/package.json`
- `crates/Cargo.toml`
- `crates/lev-abac/Cargo.toml`
- `crates/lev-adapter-claude/Cargo.toml`
- `crates/lev-audit/Cargo.toml`
- `crates/lev-config/Cargo.toml`
- `crates/lev-core/Cargo.toml`
- `crates/lev-declaration/Cargo.toml`
- `crates/lev-desktop/Cargo.toml`
- `crates/lev-domain/Cargo.toml`
- `crates/lev-entity-graph/Cargo.toml`
- `crates/lev-events/Cargo.toml`
- `crates/lev-flow/Cargo.toml`
- `crates/lev-flowmind-compiler/Cargo.toml`
- `crates/lev-graph/Cargo.toml`
- `crates/lev-kernel/Cargo.toml`
- `crates/lev-logger/Cargo.toml`
- `crates/lev-mcp/Cargo.toml`
- `crates/lev-memory-engine/Cargo.toml`
- `crates/lev-memory/Cargo.toml`
- `crates/lev-notionctl/Cargo.toml`
- `crates/lev-observe/Cargo.toml`
- `crates/lev-policy/Cargo.toml`
- `crates/lev-ports/Cargo.toml`
- `crates/lev-reactive/Cargo.toml`
- `crates/lev-runtime/Cargo.toml`
- `crates/lev-sandbox/Cargo.toml`
- `crates/lev-scheduler/Cargo.toml`
- `crates/lev-simulation/Cargo.toml`
- `crates/lev-stream/Cargo.toml`
- `crates/lev-supervisor/Cargo.toml`
- `crates/lev-tui-core/Cargo.toml`
- `crates/lev-tui-testing/Cargo.toml`
- `crates/lev-tui-theme/Cargo.toml`
- `crates/lev-tui-widgets/Cargo.toml`
- `crates/lev-tui/Cargo.toml`
- `crates/lev-ui-universal/Cargo.toml`
- `crates/lev-wire/Cargo.toml`
- `crates/levd/Cargo.toml`
- `os/kernel/web/package.json`
- `package.json`
- `packages/api/package.json`
- `packages/auth/package.json`
- `packages/dashboard-core/package.json`
- `packages/db/package.json`
- `packages/graph-builder/package.json`
- `packages/poly-test-py/pyproject.toml`
- `packages/poly-test-rs/Cargo.toml`
- `packages/poly-test-ts/package.json`
- `packages/ui/package.json`
- `packages/validators/package.json`
- `plugins/auth-sniffer/package.json`
- `plugins/beads/package.json`
- `plugins/browser-cascade/package.json`
- `plugins/core-bench/package.json`
- `plugins/core-gameai/package.json`
- `plugins/core-platforms/package.json`
- `plugins/core-scheduling/package.json`
- `plugins/core-sdlc/package.json`
- `plugins/core-workshop/package.json`
- `plugins/deploy/package.json`
- `plugins/erc/package.json`
- `plugins/evolve-memory/package.json`
- ... 53 more in JSON sidecar

## Chat / transcript / Josh-JP candidate surfaces

These are routing candidates only. They still need provenance classification before wiki synthesis.

- `.lev/pm/handoffs/20260309-droid-intake-transcript-visual-explainer-session-1.md` — path/name, 26609 bytes
- `.lev/pm/reports/droid-transcript-visual-analysis-2026-03-09.md` — path/name, 2575 bytes
- `workshop/analysis/factory-droid-leo-tchourakov/transcript.md` — path/name, 54514 bytes
- `workshop/analysis/factory-droid-leo-tchourakov/transcript.raw.txt` — path/name, 163123 bytes
- `workshop/analysis/transcript-DDGcd1JoJV0/analysis.md` — path/name, 84 bytes
- `workshop/analysis/transcript-RDoTY4_xh0s/analysis.md` — path/name, 5527 bytes
- `workshop/analysis/transcript-ePFAVGcPh7U/analysis.md` — path/name, 4457 bytes
- `workshop/analysis/transcript-f1-graphics/analysis.md` — path/name, 84 bytes
- `workshop/analysis/transcript-fireship-remotion/analysis.md` — path/name, 90 bytes
- `workshop/analysis/transcript-obsidian-qmd-cluster/analysis.md` — path/name, 1997 bytes
- `workshop/analysis/transcript-qiOu7Ptjxng/analysis.md` — path/name, 4891 bytes
- `workshop/analysis/transcript-redis-context-engine/analysis.md` — path/name, 2645 bytes
- `workshop/analysis/transcript-spotify-wrapped-2025/analysis.md` — path/name, 93 bytes
- `workshop/analysis/transcript-triage.md` — path/name, 1442 bytes
- `workshop/poc/cdo/pocs/consciousness-integration/dmt/andrew_gallimore_dmt_brain_scans_transcript.txt` — path/name, 570988 bytes
- `workshop/poc/cdo/pocs/consciousness-integration/dmt/dmt_clean_transcript.txt` — path/name, 190355 bytes
- `workshop/transcripts/transcript-2LdG-kH4gOY.txt` — path/name, 8719 bytes
- `workshop/transcripts/transcript-DDGcd1JoJV0.txt` — path/name, 2732 bytes
- `workshop/transcripts/transcript-wA6I2vK1N2E.txt` — path/name, 14383 bytes
- `.agents/skills/workflow-api2cli-api2cdp-manual-lifecycle/SKILL.md` — content-keyword, 4835 bytes
- `.agents/skills/workflow-dotfiles-sync/SKILL.md` — content-keyword, 2392 bytes
- `.claude/commands/handoff-resume.md` — path/name, 1803 bytes
- `.claude/commands/handoff.md` — path/name, 651 bytes
- `.claude/commands/lev-dashboard.md` — content-keyword, 7988 bytes
- `.cursor/rules/README.md` — content-keyword, 4425 bytes
- `.github/hooks/dcg.json` — content-keyword, 275 bytes
- `.leann/indexes/lev-code/documents.leann.passages.jsonl` — content-keyword, 1362074 bytes
- `.lev/config.yaml` — content-keyword, 9789 bytes
- `.lev/events.jsonl` — content-keyword, 171520 bytes
- `.lev/handoffs/exec-test-strategy.md` — path/name, 3241 bytes
- `.lev/indexes/manifest.yaml` — content-keyword, 9195 bytes
- `.lev/pm/analysis/session-hooks-simulation-2026-01-25.md` — content-keyword, 18012 bytes
- `.lev/pm/archive/scratch-202601/cognee-cgf-synthesis.md` — content-keyword, 9311 bytes
- `.lev/pm/archive/scratch-202601/context-graph-research.md` — content-keyword, 9505 bytes
- `.lev/pm/archive/scratch-202601/context-graph-timetravel-results.md` — content-keyword, 41196 bytes
- `.lev/pm/archive/scratch-202601/intake-claude-code-langfuse-template.md` — content-keyword, 10285 bytes
- `.lev/pm/archive/scratch-202601/lev-dashboard-prior-art.yaml` — content-keyword, 15184 bytes
- `.lev/pm/archive/scratch-202601/self-learning-os-prd.md` — content-keyword, 17553 bytes
- `.lev/pm/archive/scratch-202601/spike-graphiti-connection.md` — content-keyword, 7027 bytes
- `.lev/pm/archive/sdk-first-superseded/20260220-204524-sdk-first-poly-daemon-proposal.md` — content-keyword, 5956 bytes
- `.lev/pm/archive/sdk-first-superseded/20260220-211521-sdk-first-docs-alignment-handoff.md` — path/name, 3345 bytes
- `.lev/pm/archive/sdk-first-superseded/20260220-213118-poly-daemon-reconciliation-r3.md` — content-keyword, 8229 bytes
- `.lev/pm/archive/sdk-first-superseded/20260221-112513-harness-sdk-poly-checkpoint.md` — content-keyword, 9057 bytes
- `.lev/pm/archive/sdk-first-superseded/20260222-151845-sdk-first-poly-hard-cut-sprint.md` — content-keyword, 7958 bytes
- `.lev/pm/archive/sdk-first-superseded/20260307-013915-poly-robot-mode-sdk-first-roadmap.md` — content-keyword, 58716 bytes
- `.lev/pm/archive/sdk-first-superseded/spec-machine-contract-schema-codegen-2026-03-07.md` — content-keyword, 5722 bytes
- `.lev/pm/archive/sdk-first-superseded/spec-poly-robot-mode-canonicalization-2026-03-07.md` — content-keyword, 11282 bytes
- `.lev/pm/archive/sdk-first-superseded/spec-sdk-first-poly-daemon-canonical-convergence-2026-02-20.md` — content-keyword, 11750 bytes
- `.lev/pm/archive/sdk-first-superseded/spec-sdk-first-root-cli-thin-adapter-2026-03-07.md` — content-keyword, 8232 bytes
- `.lev/pm/decisions/d16-dogfood-is-preset-plugin-first.md` — content-keyword, 4151 bytes
- `.lev/pm/designs/agent-adapter-e2e-plan.md` — content-keyword, 4535 bytes
- `.lev/pm/designs/leviathan-meta-framework.md` — content-keyword, 29535 bytes
- `.lev/pm/designs/phase-3-jobtype-recognition-architecture.md` — content-keyword, 42817 bytes
- `.lev/pm/designs/phase-5-agentic-compiler-architecture.md` — content-keyword, 32926 bytes
- `.lev/pm/designs/phase4-weight-system-architecture.md` — content-keyword, 35975 bytes
- `.lev/pm/handoffs/20260216-hard-cut-supersession-index.md` — path/name, 2511 bytes
- `.lev/pm/handoffs/20260220-081342-cascading-context-artifact-lifecycle.md` — path/name, 10066 bytes
- `.lev/pm/handoffs/20260220-flowmind-ratchet-harness.md` — path/name, 28333 bytes
- `.lev/pm/handoffs/20260220-lev-forge-cdo-handoff.md` — path/name, 15673 bytes
- `.lev/pm/handoffs/20260220-repo-restructure-public-lev.md` — path/name, 10715 bytes
- `.lev/pm/handoffs/20260220-sprint-planning-workflow-codification.md` — path/name, 37020 bytes
- `.lev/pm/handoffs/20260221-152500-graph-runtime-sprint.md` — path/name, 10580 bytes
- `.lev/pm/handoffs/20260222-graph-infrastructure-session-7.md` — path/name, 14257 bytes
- `.lev/pm/handoffs/20260222-work-flowmind-conversion-session-1.md` — path/name, 28719 bytes
- `.lev/pm/handoffs/20260223-sdlc-tooling-session-1.md` — path/name, 13571 bytes
- `.lev/pm/handoffs/20260224-064844-platform-binding-event-provider-alignment-session-1.md` — path/name, 7543 bytes
- `.lev/pm/handoffs/20260224-pi-agentping-integration-handoff.md` — path/name, 1634 bytes
- `.lev/pm/handoffs/20260224-runtime-mvp-critical-plan-session-1.md` — path/name, 4635 bytes
- `.lev/pm/handoffs/20260224-work-flowmind-protocol-integration-session-1.md` — path/name, 32088 bytes
- `.lev/pm/handoffs/20260227-kingly-platform-strategy-session-2.md` — path/name, 6844 bytes
- `.lev/pm/handoffs/20260303-ecosystem-intake-framework-audit-session-1.md` — path/name, 20678 bytes
- `.lev/pm/handoffs/20260303-lev-agentic-dx-audit-session-1.md` — path/name, 11815 bytes
- `.lev/pm/handoffs/20260303-offgrid-session-3.md` — path/name, 5935 bytes
- `.lev/pm/handoffs/20260303-sdk-first-cross-lang-compliance.md` — path/name, 14743 bytes
- `.lev/pm/handoffs/20260303-voice-dashboard-10-step-plan.md` — path/name, 19110 bytes
- `.lev/pm/handoffs/20260303-voice-dashboard-plugin-native.md` — path/name, 24807 bytes
- `.lev/pm/handoffs/20260303-voice-dashboard-session-handoff.md` — path/name, 7694 bytes
- `.lev/pm/handoffs/20260305-154705-auth-sniffer-skills-reconciliation.md` — path/name, 13786 bytes
- `.lev/pm/handoffs/20260306-171351-paperclip-timetravel-bridge.md` — path/name, 33146 bytes
- `.lev/pm/handoffs/20260306-190740-notion-plugin-cli-and-surface.md` — path/name, 21751 bytes
- `.lev/pm/handoffs/20260306-agents-work-reconcile-session-1.md` — path/name, 25630 bytes
- `.lev/pm/handoffs/20260307-agentping-web-ui-consolidation-session-2.md` — path/name, 16029 bytes
- `.lev/pm/handoffs/20260307-browser-audit-auth-session-design.md` — path/name, 6435 bytes
- `.lev/pm/handoffs/20260307-daemon-runtime-warm-worker-pool-architecture-plan-session-1.md` — path/name, 13084 bytes
- `.lev/pm/handoffs/20260307-ecosystem-intake-mastra-engram-runtime-session-2.md` — path/name, 13635 bytes
- `.lev/pm/handoffs/20260307-hybrid-type-contracts-session.md` — path/name, 2805 bytes
- `.lev/pm/handoffs/20260307-levui-ir-genui-vision-session-1.md` — path/name, 14488 bytes
- `.lev/pm/handoffs/20260307-marketplace-gtm-bundle-sprint.md` — path/name, 5936 bytes
- `.lev/pm/handoffs/20260307-phase1-implementation-pr61.md` — path/name, 3011 bytes
- `.lev/pm/handoffs/20260307-pi-host-adapter-refactor.md` — path/name, 8688 bytes
- `.lev/pm/handoffs/20260307-pr-merge-train-github-review-fix-merge-session-1.md` — path/name, 16464 bytes
- `.lev/pm/handoffs/20260307-rust-knowledge-pipeline-handoff.md` — path/name, 2819 bytes
- `.lev/pm/handoffs/20260307-warm-worker-pool-gate-validation.md` — path/name, 2179 bytes
- `.lev/pm/handoffs/20260307-work-skill-contract-pass1-session-1.md` — path/name, 18283 bytes
- `.lev/pm/handoffs/20260308-bookmark-ingest-agent-session33-handoff.md` — path/name, 2122 bytes
- `.lev/pm/handoffs/20260308-doc-lifecycle-cleanup-agent-handoff.md` — path/name, 6231 bytes
- `.lev/pm/handoffs/20260309-agentping-web-ui-consolidation-session-3.md` — path/name, 36880 bytes
- `.lev/pm/handoffs/20260309-agentping-web-ui-consolidation-session-4.md` — path/name, 17033 bytes
- `.lev/pm/handoffs/20260309-claude-codex-base-harness-contract-session-1.md` — path/name, 15216 bytes
- `.lev/pm/handoffs/20260309-e2e-test-suite-repair.md` — path/name, 6829 bytes
- `.lev/pm/handoffs/20260309-ext-deps-onboarding-smaug-futureproof-session-1.md` — path/name, 22472 bytes
- `.lev/pm/handoffs/20260309-lev-exec-sdk-first-until-fix-session-1.md` — path/name, 5363 bytes
- `.lev/pm/handoffs/20260309-lev-newcomer-explainer-content-segments-session-1.md` — path/name, 21268 bytes
- `.lev/pm/handoffs/20260309-leviathan-graph-analysis-content-lev-homepage-session-4.md` — path/name, 13876 bytes
- `.lev/pm/handoffs/20260309-mesh-marketplace-virtengine-interleave-session-1.md` — path/name, 10527 bytes
- `.lev/pm/handoffs/20260309-mesh-marketplace-virtengine-jeff-ideation-session-1.md` — path/name, 24800 bytes
- `.lev/pm/handoffs/20260309-notionctl-plugin-core-execution-session-2.md` — path/name, 9757 bytes
- `.lev/pm/handoffs/20260309-ops-sync-dashboard-chezmoi-agents-session-1.md` — path/name, 10845 bytes
- `.lev/pm/handoffs/20260309-paperclip-timetravel-architecture-company-project-model-session-5.md` — path/name, 7089 bytes
- `.lev/pm/handoffs/20260309-paperclip-timetravel-architecture-lev-agent-boost-session-6.md` — path/name, 9588 bytes
- `.lev/pm/handoffs/20260309-paperclip-timetravel-architecture-lev-agent-workflows-session-4.md` — path/name, 17586 bytes
- `.lev/pm/handoffs/20260309-prompt-stack-plugin-bidirectional-stopgap-session-1.md` — path/name, 12778 bytes
- `.lev/pm/handoffs/20260309-prompt-stack-sdk-absorption-session-2.md` — path/name, 14560 bytes
- `.lev/pm/handoffs/20260309-sdlc-hygiene-handoff-lifecycle-encoding-session-1.md` — path/name, 9307 bytes
- `.lev/pm/handoffs/20260309-storage-cms-memory-graph-thread-repair-session-1.md` — path/name, 29714 bytes
- `.lev/pm/handoffs/20260309-timetravel-bookmarks-smaug-intake-session-1.md` — path/name, 42026 bytes
- `.lev/pm/handoffs/20260310-120000-harness-flowmind-next.md` — path/name, 9437 bytes
- `.lev/pm/handoffs/20260310-120000-pr87-branch-alignment.md` — path/name, 2856 bytes
- `.lev/pm/handoffs/20260310-agentping-browser-control-plane-sdk-session-stack-session-6.md` — path/name, 31682 bytes
- `.lev/pm/handoffs/20260310-agentping-core-thread-centric-conversion-session-1.md` — path/name, 29687 bytes
- `.lev/pm/handoffs/20260310-agentping-standalone-host-and-surface-proof-session-5.md` — path/name, 11738 bytes
- `.lev/pm/handoffs/20260310-auth-sniffer-runtime-deep-fixes-session-1.md` — path/name, 25046 bytes
- `.lev/pm/handoffs/20260310-autodev-loop-operationalization-session-1.md` — path/name, 13460 bytes
- `.lev/pm/handoffs/20260310-chore-loop-session.md` — path/name, 18050 bytes
- `.lev/pm/handoffs/20260310-core-alignment-chore-loop-session-1.md` — path/name, 2740 bytes
- `.lev/pm/handoffs/20260310-exec-architecture-refactor-session-1.md` — path/name, 5966 bytes
- `.lev/pm/handoffs/20260310-flowmind-graph-alignment-meta-interview-session-1.md` — path/name, 17919 bytes
- `.lev/pm/handoffs/20260310-flowmind-harness-control-plane-boundary-session-1.md` — path/name, 20665 bytes
- `.lev/pm/handoffs/20260310-lev-newcomer-explainer-content-segments-session-2.md` — path/name, 17950 bytes
- `.lev/pm/handoffs/20260310-lev-newcomer-explainer-content-segments-session-3.md` — path/name, 6273 bytes
- `.lev/pm/handoffs/20260310-pr100-evolve-memory-review-fixes-session-1.md` — path/name, 7056 bytes
- `.lev/pm/handoffs/20260310-remaining-chores-handoff.md` — path/name, 2193 bytes
- `.lev/pm/handoffs/20260310-sdk-cutover-complete-session-final.md` — path/name, 2249 bytes
- `.lev/pm/handoffs/20260310-sdk-cutover-sentinel-alignment-session-3.md` — path/name, 3348 bytes
- `.lev/pm/handoffs/20260310-sdlc-convergence-chore-roadmap-session-1.md` — path/name, 12891 bytes
- `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-2.md` — path/name, 9939 bytes
- `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-3.md` — path/name, 13345 bytes
- `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-4.md` — path/name, 15914 bytes
- `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-5.md` — path/name, 19903 bytes
- `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-6.md` — path/name, 6164 bytes
- `.lev/pm/handoffs/20260310-sdlc-convergence-exec-glue-session-7.md` — path/name, 5967 bytes
- `.lev/pm/handoffs/20260310-sdlc-flowmind-deepen-validate-hygiene-session-1.md` — path/name, 16225 bytes
- `.lev/pm/handoffs/20260310-sdlc-runtime-exec-handoff-hygiene-session-1.md` — path/name, 7857 bytes
- `.lev/pm/handoffs/20260310-sdlc-workgraph-deterministic-lifecycle-convergence-session-1.md` — path/name, 28274 bytes
- `.lev/pm/handoffs/20260310-sdlc-workgraph-deterministic-lifecycle-convergence-session-2.md` — path/name, 2576 bytes
- `.lev/pm/handoffs/20260311-execution-dag-exec-stress-import-session-1.md` — path/name, 16156 bytes
- `.lev/pm/handoffs/20260311-flowmind-masfactory-parity-session-1.md` — path/name, 26531 bytes
- `.lev/pm/handoffs/20260311-flowmind-masfactory-parity-session-2.md` — path/name, 17455 bytes
- `.lev/pm/handoffs/20260311-gen-ui-session-shell-poc-session-1.md` — path/name, 5272 bytes
- `.lev/pm/handoffs/20260311-graph-convergence-session-3.md` — path/name, 14966 bytes
- `.lev/pm/handoffs/20260311-sdlc-autodev-heartbeat-session-1.md` — path/name, 12860 bytes
- `.lev/pm/handoffs/20260311-sdlc-control-plane-pilot-session-1.md` — path/name, 5629 bytes
- `.lev/pm/handoffs/20260311-substrate-convergence-session-1.md` — path/name, 2720 bytes
- `.lev/pm/handoffs/20260311-work-mvp-flowmind-replatform-session-1.md` — path/name, 14579 bytes
- `.lev/pm/handoffs/20260312-autodev-loop-skill-redesign-session-1.md` — path/name, 11120 bytes
- `.lev/pm/handoffs/20260312-graph-deep-research.md` — path/name, 6348 bytes
- `.lev/pm/handoffs/20260312-orchestration-entity-placement-session-1.md` — path/name, 11245 bytes
- `.lev/pm/handoffs/20260312-sdlc-autodev-heartbeat-session-3.md` — path/name, 6030 bytes
- `.lev/pm/handoffs/20260312-sdlc-autodev-heartbeat-session-4.md` — path/name, 22218 bytes
- `.lev/pm/handoffs/20260313-cdo-architecture-deliberation-session-8.md` — path/name, 17978 bytes
- ... 90 more in JSON sidecar

## Important markdown/docs preview

- `docs/ARCHITECTURE.md` (24719 bytes) — title: Lev Architecture - Canonical Hard Cut; owner: lev-core; status: active | # Lev Architecture - Canonical Hard Cut / ## 1. System Purpose / ### 1.1 Surface Strategy
- `docs/GAP_REGISTER.md` (3508 bytes) — title: Documentation Gap Register; owner: lev-core; status: active | # Documentation Gap Register / ## 1. Closed In This Pass / ## 2. Open Gaps
- `docs/NORTH_STAR.md` (17776 bytes) — title: Leviathan North Star; owner: lev-core; status: active | # Leviathan North Star / ## The Idea / ## The Positioning
- `docs/README.md` (2015 bytes) — # Lev Documentation / ## Start Here / ## How To Read This Tree
- `docs/ROADMAP.md` (9175 bytes) — title: Leviathan Roadmap; owner: lev-core; status: active | # Roadmap / ## Current State / ## Active Workstreams
- `docs/_inbox/00a-cli-agent-abstraction.md` (2113 bytes) — # CLI Agent Abstraction & Terminal Interaction Model / ## Raw Concepts / ### The Problem
- `docs/_inbox/00e-ux-stages-entity-ontology.md` (5594 bytes) — # UX Research Stages & Entity Ontology (Dashboard Spec) / ## The 6-Stage UX Process Applied to Multi-Project Agent Dashboard / ### Stage 1: Problem Framing
- `docs/_inbox/00g-motia-runtime-comparison.md` (2895 bytes) — # Motia Runtime Comparison / ## What Motia Is / ## What's Interesting
- `docs/_inbox/20260220-leviathan-arch-stress-test-pdf-baseline.md` (7774 bytes) — # Leviathan Architecture Stress Test — PDF Baseline (Pre-V3) / ## Baseline Metrics (Delta vs V3) / ## Summary Findings (Verbatim, Pre-V3)
- `docs/_inbox/20260220-leviathan-arch-stress-test-v3.md` (12716 bytes) — # Leviathan Architecture Stress Test V3 — Final Report / ## Executive Summary / ## 1. Framework Coupling Heat Map
- `docs/_inbox/20260227-kingly-federated-marketplace-vision-roadmap.md` (10733 bytes) — type: proposal; status: active | # Kingly Federated Marketplace: Vision, MVP Scope, and Launch Roadmap / ## 1) Scope Lock / ## 2) Evidence Baseline
- `docs/_inbox/20260306-clawverse-prd-v1.1.md` (6129 bytes) — # ClawVerse PRD v1.1 — Ingest / ## What Is This / ## Why This Matters for Lev
- `docs/_inbox/20260306-kingly-marketplace-interop-strategy.md` (10885 bytes) — # Kingly Marketplace Interop Strategy: The Platform of Platforms / ## The Thesis / ## What's Happening Right Now (Feb 2026)
- `docs/_inbox/20260306-kingly-platform-gtm-plan.md` (9671 bytes) — # Kingly Platform — Go-to-Market Plan / ## TL;DR / ## Revenue Streams (What We Make)
- `docs/_inbox/20260306-kingly-platform-technical-buildout.md` (13582 bytes) — # Kingly Platform — Technical Buildout Roadmap / ## What Exists Today (✅ Built) / ## Phase 1: Production Foundation (Weeks 1-3)
- `docs/_inbox/20260308-graph-parity-engineering-memo.md` (7049 bytes) — # Engineering Memo: Graph Parity And Analysis Stack / ## Purpose / ## Executive Summary
- `docs/_inbox/20260309-paperclip-lev-agent-workflow-model.md` (2440 bytes) — # Paperclip x Lev: One Leviathan Agent, Workflows Stay Lev-Owned / ## Why This Exists / ## Core Decision
- `docs/_inbox/20260309-substack-seed-graphs-harnesses-and-reality.md` (17622 bytes) — # Graphs, Harnesses, And Reality / ## Subtitle / ## The real project
- `docs/_inbox/auth-sniffer-skills-current-state-2026-03-05.md` (6466 bytes) — # Auth Sniffer + Skills Current State Snapshot / ## Current Auth-Sniffer Reference Behavior / # Compile FlowMind -> SmartDown artifact
- `docs/_inbox/clawmeet-adr.md` (11106 bytes) — title: "ADR: ClawMeet Integration Architecture"; status: accepted | # ADR: ClawMeet Integration Architecture / ## Context / ### Inputs
- `docs/_inbox/clawmeet-distributed-agent-mesh.md` (17501 bytes) — title: "ClawMeet: Distributed Agent Mesh on Leviathan"; status: proposal | # ClawMeet: Distributed Agent Mesh on Leviathan / ## What Is This / ## The Architecture
- `docs/_inbox/clawmeet-gap-analysis-roadmap.md` (16164 bytes) — title: "ClawMeet Gap Analysis & Epic Roadmap"; status: spec-proposal | # ClawMeet: Gap Analysis & Epic Roadmap / ## Gap Analysis: Honest Accounting / ### Maturity Scorecard
- `docs/_inbox/clawmeet-research-notes.md` (33200 bytes) — title: "ClawMeet → Lev Integration Research Notes"; status: research | # ClawMeet → Lev Integration Research Notes / ## 1. Full Gap Inventory — Lev Primitives vs ClawMeet / ### Gap Inventory Table
- `docs/_inbox/dashboard-runner-guide.md` (15188 bytes) — # Dashboard Runner User Guide / ## Table of Contents / ## Overview
- `docs/_inbox/doc-sprawl-four-voices-2026-03-08.md` (1507 bytes) — # Doc sprawl — one page (inbox) / ## SDK-First Cutover (canonical ref)
- `docs/_inbox/kingly-docs-crossref-2026-03-06.md` (8679 bytes) — type: analysis; status: complete | # Kingly Docs Cross-Reference — 2026-03-06 / ## What This Is / ## 1) Conflicts Found
- `docs/_inbox/lev-openwork-fractal-attachment.md` (16199 bytes) — title: "Lev ↔ OpenWork: Fractal Attachment Architecture"; status: proposal | # Lev ↔ OpenWork: Fractal Attachment Architecture / ## The Concept / ## Two Attachment Vectors
- `docs/_inbox/lev-provenance-lineage-roadmap.md` (11333 bytes) — title: "Lev Provenance & Lineage Roadmap (VFS + Graph)"; status: spec-proposal; owner: lev-core | # Lev Provenance & Lineage Roadmap (VFS + Graph) / ## 1) Lev-Way Position / ## 2) Current State (Evidence Snapshot)
- `docs/_inbox/lev-ref/SKILL.md` (15714 bytes) — # The CLI-as-Prompt Paradigm / ## Core Insight / ## Vernacular
- `docs/_inbox/lev_nonclassical_runtime_design.md` (47203 bytes) — # Retooling External Methods into a Nonclassical Topological Runtime for Lev / ## Purpose / ## Executive Summary
- `docs/_inbox/lev_nonclassical_runtime_design_audited.md` (61389 bytes) — # Retooling External Methods into a Nonclassical Topological Runtime for Lev / ## Reading Contract / ## Quick Audit Summary
- `docs/_inbox/leviathan_offgrid_mvp_artifact_v0_1.md` (12484 bytes) — # Leviathan × ClawBuddy Off-Grid MVP Artifact (v0.1) / ## 0) Decisions Locked for MVP 0.1 / ## 1) Minimal Leviathan MVP Surface Area (Irreducible Contract)
- `docs/_inbox/storage-cms-memory-graph-future-notes.md` (6149 bytes) — # Storage / CMS / Memory / Graph — Future Design Notes / ## Future Consideration: Notion as CanonicalStoragePort + CmsControlPort First / ## Repaired Operator Semantics (Recovered 2026-03-09)
- `docs/_inbox/sunny-clawmeet.md` (16840 bytes) — title: "ClawMeet Implementation Gap Analysis"; status: analysis | # ClawMeet Implementation Gap Analysis / ## Executive Summary / ### Key Findings
- `docs/_inbox/thinking-strategy-flowmind-extension.md` (10428 bytes) — # Thinking Strategy FlowMind Extension / ## Problem Statement / ## Design Goals
- `docs/_inbox/ux/dashboard-ux-spec.md` (4186 bytes) — # Dashboard UX Spec — Multi-Project Agent Dashboard (PROPOSAL) / ## Stage 1: Problem Framing / ## Stage 2: Jobs-to-Be-Done
- `docs/_inbox/ux/lev-ui-20260212/assets/codex-inspiration/manifest.md` (1748 bytes) — # ChatGPT Codex Desktop App - UI Screenshots / ## Screenshots Captured (from conversation 2026-02-02)
- `docs/_inbox/ux/lev-ui-20260212/lev-ui-prd.md` (43189 bytes) — # Lev UI: Composable Workspace Runtime / ## Executive Summary / ## The Problem: Agentic Code Collapse
- `docs/_inbox/ux/lev-ui-20260212/stage5-interaction-models.md` (85881 bytes) — # Stage 5: Interaction Models / ## Executive Summary / ## 1. Entity FSM → UI State Machine Mapping
- `docs/_inbox/ux/lev-ui-20260212/stage6-component-intents.md` (59831 bytes) — # Stage 6: Component Intent for Lev UI Workspace / ## 1. Component Intent Registry / ### 1.1 ProjectSelector
- `docs/_inbox/ux/lev-workspace-20260212/components.md` (4311 bytes) — # Components / ## Expanded Surface Components (Round 2) / ## Reduced MVP Component Set
- `docs/_inbox/ux/lev-workspace-20260212/summary.md` (2853 bytes) — # Summary / ## Problem + Success Criteria / ## Key Tradeoffs
- `docs/_inbox/ux/lev-workspace-20260212/wireframes.md` (4519 bytes) — # Wireframes / ## Global Nav Map / ## Expanded Architecture Screen Inventory
- `docs/_inbox/voice-daemon-adapters-work-mvp-spec.md` (4734 bytes) — # Voice Daemon Adapters: Work-MVP Handoff + Spec / ## Problem / ## Scope
- `docs/decisions/adr-001-adapter-mcp-event-disambiguation.md` (5050 bytes) — # ADR-001: Adapter, MCP Registration, and Event Namespace Disambiguation / ## 1. Config Adapter ≠ Runtime Gateway / ## 2. MCP Registration — Single Owner
- `docs/design-specs.md` (4426 bytes) — # Design + Specs Consolidation Map / ## Naming Contract / ## Cohesion Rule
- `docs/design/README.md` (1832 bytes) — # Design Docs Index / ## Canonical (`design-*`) / ## In-Flight (`proposal-*`)
- `docs/design/design-cli-surface.md` (4977 bytes) — title: CLI Surface v1 (Locked Prerelease Contract); owner: lev-core; status: active | # CLI Surface v1 (Locked Prerelease Contract) / ## Locked Decisions / ## Root CLI Contract (v1)
- `docs/design/design-domain-contracts.md` (13664 bytes) — title: Core System Contract (LOCKED); owner: lev-core; status: active | # Core System Contract (LOCKED) / ## Architectural Standards / ## Config Resolution Chain (Fractal)
- `docs/design/design-enterprise-telemetry.md` (13100 bytes) — title: Enterprise Telemetry Design; owner: lev-core; status: active | # Enterprise Telemetry Design / ## Purpose / ## Current State (Three Disconnected Systems)
- `docs/design/design-flowmind.md` (36020 bytes) — title: "Design: FlowMind"; owner: lev-core; status: active | # Design: FlowMind / ## 1. Scope / ### 1.1 Identity (the React Analogy)
- `docs/design/design-graph-actor.md` (26313 bytes) — title: "Leviathan: Actor-Graph Architecture"; owner: lev-core; status: active | # Leviathan: Actor-Graph Architecture / ## Executive Summary / ### Backend Observability Note
- `docs/design/design-graph-c4-current.md` (16014 bytes) — title: "C4 Current State: Entity Graph (Session 5 Snapshot)"; owner: lev-core; status: active | # C4 Current State: Entity Graph (Session 5 — 2026-02-22) / ## C1: System Context / ### Current Data Flow Status
- `docs/design/design-graph-cascading-context.md` (3743 bytes) — # Cascading Context: Fractal Graph Base Architecture / ## Overview / ## The Fractal Pattern
- `docs/design/design-graph-code-adapter.md` (18188 bytes) — title: CodeGraphAdapter — Source Code Entity Extraction; owner: lev-core; status: design-complete | # CodeGraphAdapter — Source Code Entity Extraction / ## 1. Problem Statement / ## 2. Architecture
- `docs/design/design-graph-lifecycle-theory.md` (3658 bytes) — title: Graph Lifecycle Theory; owner: lev-core; status: active | # Graph Lifecycle Theory / ## Purpose / ## Canonical Companions
- `docs/design/design-graph-primitives.md` (25732 bytes) — title: Graph Primitives and Depth Model (LOCKED); owner: lev-core; status: active | # Graph Primitives and Depth Model (LOCKED) / ## Multi-Axis Depth Model (LOCKED, Session 2026-02-12) / ### Axis 1: Depth (L0-L3) — Zoom / Level of Detail
- `docs/design/design-harness-sdk.md` (5231 bytes) — title: "05 - Core: SDK, Harness & Platforms"; owner: lev-core; status: active | # 05 - Core: SDK, Harness & Platforms / ## Scope / ## LOCKED VERNACULAR (5 Terms)
- `docs/design/design-index.md` (1896 bytes) — title: Core Index (Search and Retrieval Orchestration); owner: lev-core; status: active | # Core Index (Search and Retrieval Orchestration) / ## 1. Ownership Contract / ## 2. Responsibilities
- `docs/design/design-lifecycle.md` (2360 bytes) — title: "Core Design: Lifecycle Redistribution"; owner: lev-core; status: active | # Core Design: Lifecycle Redistribution / ## 1. Decision / ## 2. Redistribution Contract
- `docs/design/design-orchestration-coordination.md` (9579 bytes) — title: Core Coordination Design; owner: lev-core; status: active | # Core Coordination Design / ## Purpose / ### Decision Rule
- `docs/design/design-poly.md` (9688 bytes) — title: Poly Binder + Control Surface Architecture; owner: lev-core; status: active | # Poly Binder + Control Surface Architecture / ## 1. Ownership Contract / ## 2. Layer Model
- `docs/design/proposal-domain-classify-contract-adr.md` (23155 bytes) — # ADR: classify() Contract for Entity Graph Pipeline / ## Status / ## Context
- `docs/design/proposal-domain-entity-ontology.md` (6265 bytes) — title: Entity Ontology — SDLC Plugin Layer (PROPOSAL); owner: lev-core; status: active | # Entity Ontology — SDLC Plugin Layer (PROPOSAL) / ## Layer Separation / ### Plugin Entity Registration
- `docs/design/proposal-event-bus-eventbridge.md` (24604 bytes) — # EventBridge Design — EventBus to FlowMind/Graph / ## 1. Problem Statement / ### The Three LevEvent Definitions
- `docs/design/proposal-flowmind-ratchet.md` (18697 bytes) — title: "Design: FlowMind Ratchet Harness"; owner: lev-core; status: draft | # Design: FlowMind Ratchet Harness / ## 0. Framing / ## 1. Thread Topology Mapping
- `docs/design/proposal-flowmind-system.md` (26494 bytes) — title: "Design: FlowMind System-Level Declarations"; owner: lev-core; status: draft | # Design: FlowMind System-Level Declarations / ## 1. The Insight / ### Two Builders, One System
- `docs/design/proposal-graph-c4-target.md` (34278 bytes) — title: "C4 Target State: Graph as Central Nervous System"; owner: lev-core; status: proposed | # C4 Target State: Graph as Central Nervous System / ## C1: System Context / ### Current → Target Delta
- `docs/design/proposal-graph-dimension-model.md` (9763 bytes) — title: Dimension Model (PROPOSAL, Session 2026-02-12); owner: lev-core; status: active | # Dimension Model (PROPOSAL, Session 2026-02-12) / ## Core Principle: Append-Only Graph / ## Dimension Registry
- `docs/design/proposal-graph-intent-cascade.md` (32273 bytes) — title: "Intent Cascade: Intent as Graph Primitive"; owner: lev-core; status: draft | # Intent Cascade: Intent as Graph Primitive / ## 1. The Problem / ## 2. Intent Engineering Framework → Lev Primitive Mapping
- `docs/design/proposal-meta-foundations.md` (2597 bytes) — title: "Core Design: Other Foundational Modules"; owner: lev-core; status: active | # Core Design: Other Foundational Modules / ## 1. Scope / ## 2. Active Core Modules
- `docs/design/proposal-meta-framework-adoption.md` (17136 bytes) — # Framework Adoption Workshop / ## Purpose / ## Three Buckets
- `docs/plugins/beads.md` (6699 bytes) — title: "Plugin: Beads"; owner: lev-core; status: active | # Plugin: Beads / ## Status / ## Purpose
- `docs/plugins/core-platforms.md` (9846 bytes) — title: "Plugin: Core Platforms"; owner: lev-core; status: active | # Plugin: Core Platforms / ## Status / ## Purpose
- `docs/plugins/graph-adapters.md` (6758 bytes) — title: "Plugin: Graph Adapters"; owner: lev-core; status: active | # Plugin: Graph Adapters / ## Status / ## Purpose
- `docs/plugins/notion.md` (4171 bytes) — title: "Plugin: Notion"; owner: lev-core; status: active | # Plugin: Notion / ## Status / ## Purpose
- `docs/plugins/publisher.md` (8068 bytes) — title: "Plugin: Publisher"; owner: lev-core; status: active | # Plugin: Publisher / ## Status / ## Purpose
- `docs/plugins/sdlc.md` (5113 bytes) — title: "Plugin: SDLC"; owner: lev-core; status: active | # Plugin: SDLC / ## Canonical Companions / ## Purpose
- `docs/quick-start.md` (2673 bytes) — # Quick Start / ## Prerequisites / ## Install from Source
- `docs/specs/README.md` (6268 bytes) — # Specs Index / ## Core Module Specs (18 modules — all covered) / ## Plugin Specs
- `docs/specs/_done/chore-01-sdk-cutover-exec-ownership.md` (2912 bytes) — # Chore: Cut Execution Ownership Out of Poly / ## Gap / ## Design Intent
- `docs/specs/_done/chore-02-sdk-cutover-poly-cleanup.md` (6278 bytes) — # Chore: Poly Cleanup — Remove Dead Code, Decompose Junk Drawer / ## Gap / ## File Disposition Inventory
- `docs/specs/_done/chore-03-sdk-cutover-cli-surface.md` (2125 bytes) — # Chore: Delete `core/cli/` — CLI is a Poly Control Surface / ## Gap / ## Design Intent (from `design-poly.md`)
- `docs/specs/_done/chore-04-sdk-cutover-robot-mode.md` (1811 bytes) — # Chore: Move Robot Mode to CLI Control Surface / ## Gap / ## Design Intent (from `design-poly.md`)
- `docs/specs/_done/chore-05-sdk-cutover-handler-extraction.md` (2686 bytes) — # Chore: Extract Built-In Handlers to Owning Modules / ## Gap / ## Design Intent
- `docs/specs/_done/chore-06-sdk-cutover-exec-adoption.md` (1502 bytes) — # Chore: Replace Direct `poly/sdk` Bypasses with Canonical Execution SDK / ## Gap / ## Design Intent
- `docs/specs/_done/chore-07-sdk-cutover-daemon-delegation.md` (1114 bytes) — # Chore: Delegate Poly Daemon Command Logic to `core/daemon` / ## Gap / ## Design Intent
- `docs/specs/_done/chore-08-sdk-cutover-harness-decomp.md` (1225 bytes) — # Chore: Decompose `core/harness/src/commands/exec.ts` into Reusable SDK Surfaces / ## Gap / ## Design Intent
- `docs/specs/_done/chore-09-sdk-cutover-registry-cleanup.md` (1053 bytes) — # Chore: Clean `core/daemons` Path Drift from Registry and Validation Surfaces / ## Gap / ## Design Intent
- `docs/specs/_done/chore-10-sdk-cutover-schema-codegen.md` (2138 bytes) — # Chore: Schema-First Machine Contract for CLI Envelopes / ## Gap / ## Design Intent
- `docs/specs/_done/chore-11-sdk-cutover-index-boundary.md` (2511 bytes) — # Chore: Clarify `core/index` SDK vs Daemon vs CLI Boundary / ## Gap / ## Design Intent
- `docs/specs/_done/chore-12-sdk-cutover-docs-alignment.md` (1362 bytes) — # Chore: Align Docs to SDK-First `exec` Ownership and Poly Binding Rules / ## Gap / ## Design Intent
- `docs/specs/_done/chore-13-sdk-cutover-validation-gates.md` (1361 bytes) — # Chore: Complete Validation-Gate Coverage on Recent Specs / ## Gap / ## Design Intent
- `docs/specs/_done/chore-14-sdk-cutover-exec-loop-to-orchestration.md` (2980 bytes) — # Chore: Move Exec Loop/Until from Harness to Orchestration / ## Gap / ## Design Intent
- `docs/specs/_done/chore-15-validation-ubs-integration.md` (5199 bytes) — title: UBS Lev SDLC Integration; owner: lev-core; type: chore | # UBS Integration into Lev SDLC / ## Decisions / ## agentguard Status (as investigated)
- `docs/specs/_done/chore-16-ralph-state-xdg-relocation.md` (3339 bytes) — title: ralph-state XDG Relocation; owner: lev-core; type: chore | # Chore: Move `.ralph-state` to XDG-Compliant Path / ## Problem / ## Target State
- `docs/specs/_done/chore-align-graph-source-of-truth-language.md` (2430 bytes) — # Chore: Fix "Source of Truth" Vocabulary Across Specs (C1/C5) / ## Gap / ## Vocabulary Map
- `docs/specs/_done/chore-build-artifacts-in-src.md` (3550 bytes) — status: done; type: chore | # Chore: Build Artifacts Committed in src/ Directories / ## The Problem / ### 1. `core/domain/src/` — full build output alongside source
- `docs/specs/_done/chore-build-boundary-enforcement.md` (2541 bytes) — title: "Chore: Build Boundary Enforcement"; owner: lev-core; type: chore | # Chore: Build Boundary Enforcement / ## Problem / ## Gaps
- `docs/specs/_done/chore-build-ownership-extraction.md` (5638 bytes) — title: "Build Package Ownership Violations — Commands Still in Build"; owner: lev-core; type: chore | # Chore: Build Package Ownership Violations — Commands Still in Build / ## The Problem / ### Commands that should be extracted
- `docs/specs/_done/chore-build-runtime-dep-boundary.md` (1639 bytes) — title: "Build Runtime Dependency Boundary"; owner: lev-core; status: validated; type: chore | # Chore: Build Runtime Dependency Boundary / ## The Problem / ## Implementation — DONE
- `docs/specs/_done/chore-config-install-safety-tests.md` (1436 bytes) — title: "Chore: Config Install Safety + Scope Precedence Tests"; owner: lev-core; type: chore | # Chore: Config Install Safety + Scope Precedence Tests / ## Problem / ## Gaps
- `docs/specs/_done/chore-config-schema-strict-mode.md` (3210 bytes) — title: "Config Schema Strict Mode for Unknown Keys"; owner: lev-core; status: validated; type: chore | # Chore: Config Schema Strict Mode for Unknown Keys / ## The Problem / ## Assessment
- `docs/specs/_done/chore-config-spec-scope-descope.md` (2135 bytes) — title: "Config Spec Scope Taxonomy Descope"; owner: lev-core; type: chore | # Chore: Config Spec Scope Taxonomy Descope / ## The Problem / ### Gap 1: Spec claims 7 scope tiers; code only supports 2
- `docs/specs/_done/chore-config-spec-stale-cascade.md` (1168 bytes) — title: "Config Spec Stale Cascade Model and Missing Files"; owner: lev-core; status: validated; type: chore | # Chore: Config Spec Stale Cascade Model and Missing Files — DONE / ## Implementation / ## Fitness Functions
- `docs/specs/_done/chore-config-test-coverage-gaps.md` (3221 bytes) — title: "Config Spec — xdg-paths.ts Zero Test Coverage + 2 Undocumented Schemas"; owner: lev-core; type: chore | # Chore: Config — xdg-paths.ts Zero Test Coverage + 2 Undocumented Schemas / ## The Problem / ### Gap 1: xdg-paths.ts — 0 tests (P1)
- `docs/specs/_done/chore-config-write-audit-events.md` (3298 bytes) — title: "Config Write Audit Events"; owner: lev-core; status: validated; type: chore | # Chore: Config Write Audit Events / ## The Problem / ## Steps
- `docs/specs/_done/chore-config-yaml-spec-contradictions.md` (1875 bytes) — title: "Chore: Config.yaml Features Exceeding Spec Documentation"; type: chore | # Chore: Config.yaml Features Exceeding Spec Documentation / ## Problem / ## Gaps
- `docs/specs/_done/chore-console-log-purge.md` (3159 bytes) — # Chore: Console.log Purge — Structured Logging Enforcement / ## The Problem / ### Per-Module Counts
- `docs/specs/_done/chore-core-phantom-module-cleanup.md` (3074 bytes) — # Chore: Core Phantom Module Cleanup / ## Background / ## Dead Modules (delete or archive)
- `docs/specs/_done/chore-core-plugin-dependency-inversion.md` (4903 bytes) — # Chore: Core-on-Plugin Dependency Inversion / ## The Problem / ### 1. `core/event-bus` depends on `@lev-os/core-platforms`
- `docs/specs/_done/chore-daemon-cwd-preflight.md` (2167 bytes) — title: "Daemon cwd Preflight Validation"; owner: lev-core; status: validated; type: chore | # Chore: Daemon cwd Preflight Validation / ## The Problem / ## Steps
- `docs/specs/_done/chore-daemon-exec-boundary.md` (1517 bytes) — title: "Move daemon exec handler from Poly to Daemon"; owner: lev-core; status: validated-no-change; type: chore | # Chore: Move daemon exec Handler from Poly to Daemon / ## Assessment: Not a Boundary Violation / ## Resolution
- `docs/specs/_done/chore-daemon-lifecycle-dep-order.md` (1608 bytes) — title: "Daemon Lifecycle Dependency-Ordered Startup"; owner: lev-core; status: validated; type: chore | # Chore: Daemon Lifecycle Dependency-Ordered Startup / ## The Problem / ## Implementation — DONE
- `docs/specs/_done/chore-daemon-spec-cleanup.md` (2250 bytes) — title: "Chore: Daemon Spec Naming + Binary Adapter Gap"; owner: lev-core; type: chore | # Chore: Daemon Spec Naming + Binary Adapter Gap / ## Problem / ## Steps
- `docs/specs/_done/chore-daemon-spec-coverage.md` (1520 bytes) — status: done; type: chore | # Chore: Daemon Module Spec Coverage Gaps / ## Issues / ### 1. ~~package.json exports point to nonexistent `src/index.js`~~ (P0) — DONE
- `docs/specs/_done/chore-deerflow-01-middleware-chain.md` (5118 bytes) — title: "Chore: Middleware Interface + Chain Engine"; owner: lev-core; type: spec | # Chore: Middleware Interface + Chain Engine / ## Problem Statement / ## Gap Description
- `docs/specs/_done/chore-deerflow-02-context-retrieval.md` (4405 bytes) — title: "Chore: Context Retrieval Middleware"; owner: lev-core; type: spec | # Chore: Context Retrieval Middleware / ## Problem Statement / ## Gap Description
- `docs/specs/_done/chore-deerflow-03-memory.md` (4438 bytes) — title: "Chore: Memory Middleware"; owner: lev-core; type: spec | # Chore: Memory Middleware / ## Problem Statement / ## Gap Description
- `docs/specs/_done/chore-deerflow-04-summarization.md` (4452 bytes) — title: "Chore: Summarization Middleware"; owner: lev-core; type: spec | # Chore: Summarization Middleware / ## Problem Statement / ## Gap Description
- `docs/specs/_done/chore-deerflow-05-subagent-limit.md` (4361 bytes) — title: "Chore: Subagent Coordination Middleware"; owner: lev-core; type: spec | # Chore: Subagent Coordination Middleware / ## Problem Statement / ## Gap Description
- `docs/specs/_done/chore-deerflow-06-artifact-governance.md` (5400 bytes) — title: "Chore: Artifact Governance Middleware"; owner: lev-core; type: spec | # Chore: Artifact Governance Middleware / ## Problem Statement / ## Gap Description
- `docs/specs/_done/chore-deerflow-07-deerflow-daemon.md` (5273 bytes) — title: "Chore: DeerFlow Daemon Registration"; owner: lev-core; type: spec | # Chore: DeerFlow Daemon Registration / ## Problem Statement / ## Gap Description
- `docs/specs/_done/chore-design-doc-spec-contradictions.md` (4493 bytes) — title: "Design Doc ↔ Spec Contradictions — Stale Design References"; owner: lev-core; type: chore | # Chore: Design Doc ↔ Spec Contradictions / ## The Problem / ## Contradictions Found (tick 104 audit)
- `docs/specs/_done/chore-design-docs-vocabulary.md` (1051 bytes) — # Chore: Update Design Docs with Architecture Vocabulary (C1/C2) — DONE / ## Resolution / ## Skipped (per spec)
- `docs/specs/_done/chore-domain-event-source-bdd.md` (1241 bytes) — title: "Chore: Domain Event Source BDD Tests"; owner: lev-core; type: chore | # Chore: Domain Event Source BDD Tests / ## Problem / ## Gaps
- `docs/specs/_done/chore-domain-event-source-scope-gap.md` (3555 bytes) — title: "Domain Spec — event-source.ts Contains 4 Undocumented Subsystems (564 LOC)"; owner: lev-core; type: chore | # Chore: Domain Spec — event-source.ts Contains 4 Undocumented Subsystems / ## The Problem / ### Gap 1: CanonicalStorageAdapter + 9 related types (lines 196-276)
- `docs/specs/_done/chore-domain-spec-stale-inventory.md` (2188 bytes) — title: "Domain Spec Stale Module Inventory"; owner: lev-core; status: validated; type: chore | # Chore: Domain Spec Stale Module Inventory / ## The Problem / ### Gap 1: Claims `paths.ts` as canonical XDG owner (file doesn't exist)
- `docs/specs/_done/chore-domain-type-graduation.md` (3489 bytes) — # Chore: Domain Type Graduation — Extract Cross-Module Types to core/domain / ## The Problem / ### Type Inventory
- `docs/specs/_done/chore-domain-xdg-path-dedup.md` (4989 bytes) — title: "XDG Path Resolution Consolidation"; owner: lev-core; status: validated; type: chore | # Chore: XDG Path Resolution Consolidation / ## The Problem / ### Tier 1: Two canonical implementations (domain vs config)
- `docs/specs/_done/chore-event-bus-bdd-test-coverage.md` (3009 bytes) — title: "Chore: Event-Bus BDD Test Coverage + Retired Stub Cleanup"; owner: lev-core; type: chore | # Chore: Event-Bus BDD Test Coverage + Retired Stub Cleanup / ## Problem / ## Missing BDD Tests
- `docs/specs/_done/chore-event-bus-spec-undocumented-subsystems.md` (3042 bytes) — title: "Event-Bus Spec Missing 13+ Source Files — Actions, Guards, Sagas, Context Undocumented"; owner: lev-core; type: chore | # Chore: Event-Bus Spec Missing 13+ Source Files / ## The Problem / ### Undocumented files
- `docs/specs/_done/chore-event-bus-type-fragmentation.md` (4638 bytes) — # Chore: Event Bus Type Fragmentation / ## The Problem / ### 1. `LevEvent` (canonical, from @lev-os/domain)
- `docs/specs/_done/chore-event-machines-bdd-test-coverage.md` (1696 bytes) — title: "Chore: Event Machines BDD Test Coverage"; owner: lev-core; type: chore | # Chore: Event Machines BDD Test Coverage / ## Problem / ## Gaps
- `docs/specs/_done/chore-event-machines-terminal-ambiguity.md` (1018 bytes) — title: "Event Machines Spec Terminal State Ambiguity"; owner: lev-core; status: validated; type: chore | # Chore: Event Machines Spec Terminal State Ambiguity / ## Implementation — DONE / ## Fitness Functions
- `docs/specs/_done/chore-event-name-standardization.md` (1536 bytes) — # Chore: Event Name Standardization (C6) — DONE / ## Decision / ## Resolution
- `docs/specs/_done/chore-event-providers-bdd-test-coverage.md` (1496 bytes) — title: "Chore: Event Providers BDD Test Coverage"; owner: lev-core; type: chore | # Chore: Event Providers BDD Test Coverage / ## Problem / ## Gaps
- `docs/specs/_done/chore-event-sourced-replay.md` (3938 bytes) — # Chore: Event-Sourced Replay Architecture (Phase 2) / ## Gap / ## Current State
- `docs/specs/_done/chore-eventbus-singleton-safety.md` (2497 bytes) — title: "EventBus Singleton Safety"; owner: lev-core; status: validated; type: chore | # Chore: EventBus Singleton Safety / ## The Problem / ### Gap 1: Options silently dropped on re-get
- `docs/specs/_done/chore-exec-client-invariant-violation.md` (1722 bytes) — title: "Exec Spec client.ts Invariant Violations"; owner: lev-core; status: validated; type: chore | # Chore: Exec Spec client.ts Invariant Violations / ## The Problem / ## Implementation — DONE
- `docs/specs/_done/chore-exec-module-hygiene.md` (1959 bytes) — # Chore: core/exec Module Hygiene / ## Issues / ### 1. `flowmind-gate.ts` — wrong module (P1)
- `docs/specs/_done/chore-exec-semaphore-bdd.md` (1149 bytes) — title: "Chore: Exec Semaphore BDD Tests"; owner: lev-core; type: chore | # Chore: Exec Semaphore BDD Tests / ## Problem / ## Resolution — tick 124
- `docs/specs/_done/chore-exec-spec-self-contradictions.md` (2985 bytes) — title: "Exec Spec Self-Contradictions on client.ts"; owner: lev-core; type: chore | # Chore: Exec Spec Self-Contradictions on client.ts / ## The Problem / ### 1. client.ts described as both "DI facade with lazy bootstrap" AND "pure re-export with zero logic"
- `docs/specs/_done/chore-flowmind-bdd-test-coverage.md` (1888 bytes) — title: "Chore: FlowMind BDD Test Coverage Gaps"; owner: lev-core; type: chore | # Chore: FlowMind BDD Test Coverage Gaps / ## Problem / ## Gaps
- `docs/specs/_done/chore-flowmind-dead-code-cleanup.md` (1749 bytes) — title: "FlowMind — 2 Dead Code Files + 1 Unlisted Subsystem"; owner: lev-core; type: chore | # Chore: FlowMind — Dead Code Cleanup + Unlisted Subsystem / ## The Problem / ### Gap 1: Dead code (spec-flagged, undeleted)
- `docs/specs/_done/chore-flowmind-escalation-unification.md` (1636 bytes) — # Chore: Unify Escalation Definitions (FlowMind) — DONE / ## Resolution / ## Previous Definitions Unified
- `docs/specs/_done/chore-flowmind-graph-nodes-parallel.md` (1724 bytes) — # Chore: Implement Missing Graph Nodes (FlowMind) / ## Gap Description / ## Design Intent
- `docs/specs/_done/chore-flowmind-lifecycle-action-rename.md` (1273 bytes) — # Chore: Rename LifecycleHook Action to Kind (FlowMind) / ## What was done / ## Design Correction
- `docs/specs/_done/chore-flowmind-parser-executor-contract.md` (1864 bytes) — # Chore: Establish Parser-Executor Contract (FlowMind) / ## Gap Description / ## Design Intent
- `docs/specs/_done/chore-flowmind-reentrancy-guards.md` (1350 bytes) — # Chore: Add Re-entrancy Guards to Executor (FlowMind) / ## Gap Description / ## Design Intent
- `docs/specs/_done/chore-flowmind-spec-action-vocab.md` (2543 bytes) — title: "FlowMind Spec Action Vocabulary Misalignment"; owner: lev-core; status: validated; type: chore | # Chore: FlowMind Spec Action Vocabulary Misalignment / ## The Problem / ### Gap 1: Spec claims `spawn` fails compilation; code treats spawn as first-class
- `docs/specs/_done/chore-flowmind-spec-coverage-gap.md` (4701 bytes) — title: "FlowMind Spec Covers ~30% of Source — 15+ Subsystems Undocumented"; owner: lev-core; type: chore | # Chore: FlowMind Spec Covers ~30% of Source — 15+ Subsystems Undocumented / ## The Problem / ### Documented (in spec ownership table)
- `docs/specs/_done/chore-flowmind-tool-registry.md` (1321 bytes) — # Chore: Implement ToolRegistry for Semantic Tool Names (FlowMind) / ## Gap Description / ## Design Intent
- `docs/specs/_done/chore-flowmind-unified-interpreter.md` (1296 bytes) — # Chore: Scaffolding the Unified Interpreter (FlowMind Target D45) / ## Gap Description / ## Design Intent
- `docs/specs/_done/chore-flowmind-variable-substitution.md` (1384 bytes) — # Chore: Unify Variable Substitution Engines (FlowMind) / ## Gap Description / ## Design Intent
- `docs/specs/_done/chore-graph-adapter-inventory-drift.md` (1832 bytes) — title: "Graph Spec Adapter Inventory Drift"; owner: lev-core; type: chore | # Chore: Graph Spec Adapter Inventory Drift / ## The Problem / ## Steps
- `docs/specs/_done/chore-graph-adapter-ownership-dup.md` (2130 bytes) — title: "Graph Adapter Ownership Duplication"; owner: lev-core; type: chore | # Chore: Graph Adapter Ownership Duplication / ## The Problem / ## Steps
- `docs/specs/_done/chore-graph-context-assembly-bdd.md` (938 bytes) — title: "Chore: Graph Context Assembly BDD Test"; owner: lev-core; type: chore | # Chore: Graph Context Assembly BDD Test / ## Problem / ## Steps
- `docs/specs/_done/chore-graph-conversation-lineage-adoption.md` (9523 bytes) — title: "Chore: Graph Conversation Lineage + Heatmapping Adoption Plan"; owner: lev-core; status: done; type: chore | # Chore: Graph Conversation Lineage + Heatmapping Adoption Plan / ## Purpose / ## Scope
- `docs/specs/_done/chore-graph-spec-bridge-undocumented.md` (1986 bytes) — title: "Graph Spec Missing bridge/, context/, projectors/ Subsystems"; owner: lev-core; type: chore | # Chore: Graph Spec Missing bridge/, context/, projectors/ Subsystems / ## The Problem / ### Undocumented subsystems
- `docs/specs/_done/chore-graph-spec-gaps.md` (2634 bytes) — # Chore: Graph Module Spec Coverage Gaps / ## Issues / ### 1. ~~ViewEngine — specced but empty stub~~ (P1) — DONE
- `docs/specs/_done/chore-harness-bdd-test-coverage.md` (1496 bytes) — title: "Chore: Harness BDD Test Coverage"; owner: lev-core; type: chore | # Chore: Harness BDD Test Coverage / ## Problem / ## Gaps
- `docs/specs/_done/chore-harness-boundary-violations.md` (4491 bytes) — # Chore: Harness Boundary Violations — Plugin Deps, XDG, Domain Types / ## The Problem / ### 1. Plugin dependency (10 runtime function imports)
- `docs/specs/_done/chore-harness-provider-count.md` (1645 bytes) — title: "Harness Spec Provider Count and Interface Duplication"; owner: lev-core; status: validated; type: chore | # Chore: Harness Spec Provider Count and Interface Duplication / ## The Problem / ## Implementation — DONE (Phase 1)
- `docs/specs/_done/chore-harness-provider-inventory.md` (2374 bytes) — title: "Harness Spec — 12 Provider Implementations Not in Ownership Table"; owner: lev-core; type: chore | # Chore: Harness Spec — 12 Provider Implementations Not in Ownership Table / ## The Problem / ### Unlisted provider files
- `docs/specs/_done/chore-harness-spec-incomplete-ownership.md` (3048 bytes) — title: "Harness Spec Missing 14+ Source Files and 3 Subdirectories"; owner: lev-core; type: chore | # Chore: Harness Spec Missing 14+ Source Files and 3 Subdirectories / ## The Problem / ### Files/subdirectories missing from spec ownership table
- `docs/specs/_done/chore-index-lev-backend-gap.md` (1396 bytes) — title: "Index Spec — lev Backend + file_watcher.py Undocumented"; owner: lev-core; type: chore | # Chore: Index Spec — lev Backend + file_watcher.py Undocumented / ## The Problem / ## Steps
- `docs/specs/_done/chore-index-phantom-refs-and-bdd.md` (1575 bytes) — title: "Chore: Index Spec Phantom Refs + BDD Test Gaps"; owner: lev-core; type: chore | # Chore: Index Spec Phantom Refs + BDD Test Gaps / ## Problem / ## Steps
- `docs/specs/_done/chore-index-spec-scope-mismatch.md` (4712 bytes) — title: "Index Spec Covers Only Python Layer — TypeScript Subsystem Undocumented"; owner: lev-core; type: chore | # Chore: Index Spec Covers Only Python Layer — TypeScript Subsystem Undocumented / ## The Problem / ### Undocumented TypeScript subsystems (47 source files in `src/`)
- `docs/specs/_done/chore-index-spec-stale-paths.md` (1795 bytes) — title: "Index Spec Stale Python Paths and Embedding Backends"; owner: lev-core; status: validated; type: chore | # Chore: Index Spec Stale Python Paths and Embedding Backends / ## The Problem / ## Implementation — DONE
- `docs/specs/_done/chore-logger-rootlogger-exposure.md` (2304 bytes) — # Chore: Logger Exports rootLogger Directly (Spec Violation) / ## The Problem / ### Why this matters
- `docs/specs/_done/chore-loop-event-bus-integration.md` (2409 bytes) — title: "Loop Event Bus Integration"; owner: lev-core; status: validated; type: chore | # Chore: Loop Event Bus Integration / ## The Problem / ## Implementation — DONE
- `docs/specs/_done/chore-memory-config-backend-mismatch.md` (1949 bytes) — title: "Chore: Memory Config.yaml Backend Mismatch"; owner: lev-core; type: chore | # Chore: Memory Config.yaml Backend Mismatch / ## Problem / ## Steps
- `docs/specs/_done/chore-memory-rust-algorithms-undocumented.md` (1465 bytes) — title: "Memory Spec — Rust Algorithm Crates (mpfp + rrf) Not in Spec"; owner: lev-core; type: chore | # Chore: Memory Spec — Rust Algorithm Crates Not in Spec / ## The Problem / ## Steps
- `docs/specs/_done/chore-memory-spec-gap.md` (2277 bytes) — title: "Memory System — Missing Top-Level Spec"; owner: lev-core; type: chore | # Chore: Memory System — Missing Top-Level Spec / ## The Problem / ## Steps
- `docs/specs/_done/chore-memory-spec-legacy-js-undocumented.md` (3323 bytes) — title: "Memory Spec Ignores 14+ Legacy JS Files in src/"; owner: lev-core; type: chore | # Chore: Memory Spec Ignores 14+ Legacy JS Files in src/ / ## The Problem / ### Undocumented JS files
- `docs/specs/_done/chore-memory-uncovered-ts-subsystems.md` (3803 bytes) — title: "Memory Spec — 12 TypeScript Files Missing from Ownership Table"; owner: lev-core; type: chore | # Chore: Memory Spec — 12 TypeScript Files Missing from Ownership Table / ## The Problem / ### Gap 1: Barrel files (3 files)
- `docs/specs/_done/chore-option-b-core-boundary-and-dogfood-plan.md` (4091 bytes) — title: "Chore: Option B Boundary + Dogfood Execution Plan"; owner: lev-core; status: draft; type: chore | # Chore: Option B Boundary + Dogfood Execution Plan / ## Purpose / ## Scope
- `docs/specs/_done/chore-orchestration-bdd-test-coverage.md` (1704 bytes) — title: "Chore: Orchestration BDD Test Coverage"; owner: lev-core; type: chore | # Chore: Orchestration BDD Test Coverage / ## Problem / ## Gaps
- `docs/specs/_done/chore-orchestration-loop-hardening.md` (3351 bytes) — title: "Orchestration Loop — Hardening Pass"; owner: lev-core; status: validated; type: chore | # Chore: Orchestration Loop — Hardening Pass / ## The Problem / ## Steps
- `docs/specs/_done/chore-orchestration-loop-spec-gap.md` (4228 bytes) — # Chore: Orchestration Loop Subsystem — Zero Spec Coverage / ## The Problem / ### 1. Undocumented loop subsystem
- `docs/specs/_done/chore-orchestration-loop-undocumented.md` (1585 bytes) — title: "Orchestration Spec Missing loop/ Subsystem"; owner: lev-core; type: chore | # Chore: Orchestration Spec Missing loop/ Subsystem / ## The Problem / ## Steps
- `docs/specs/_done/chore-package-export-alignment.md` (2251 bytes) — title: "Chore: Package Export Alignment with Spec Ownership"; owner: lev-core; type: chore | # Chore: Package Export Alignment with Spec Ownership / ## Problem / ## Fixed — tick 131
- `docs/specs/_done/chore-package-json-hygiene.md` (3126 bytes) — # Chore: Package.json Hygiene — Broken Exports, Stale Deps, Metadata Drift / ## The Problem / ### Issues by Module
- `docs/specs/_done/chore-platform-spec-ownership-gaps.md` (3850 bytes) — title: "Platform Spec Ownership Gaps"; type: chore | # Chore: Platform Spec Ownership Gaps / ## Problem / ## Root Cause
- `docs/specs/_done/chore-plugin-docs-critical.md` (1043 bytes) — # Chore: Plugin Architecture Docs — Critical Only (C8) / ## Critical Plugins Needing Docs / ## Maybe Later
- `docs/specs/_done/chore-poly-commands-unlisted.md` (2609 bytes) — title: "Poly Spec — 8 Command/CLI Files Not in Ownership Table"; owner: lev-core; type: chore | # Chore: Poly Spec — 8 Command/CLI Files Not in Ownership Table / ## The Problem / ### Unlisted files
- `docs/specs/_done/chore-poly-doctor-sdk-tests.md` (1304 bytes) — title: "Chore: Poly Doctor + SDK Dispatch Tests"; owner: lev-core; type: chore | # Chore: Poly Doctor + SDK Dispatch Tests / ## Problem / ## Gaps
- `docs/specs/_done/chore-poly-phantom-exports.md` (4269 bytes) — # Chore: Poly Phantom Exports and Dependency Inversions / ## The Problem / ### 1. Phantom `main` entry point
- `docs/specs/_done/chore-poly-spec-missing-subsystems.md` (1296 bytes) — title: "Poly Spec Missing Subsystems (codegen, schemas, events, etc.)"; owner: lev-core; status: validated; type: chore | # Chore: Poly Spec Missing Subsystems — DONE / ## Implementation / ## Fitness Functions
- `docs/specs/_done/chore-poly-spec-undocumented-subsystems.md` (5711 bytes) — title: "Poly Spec Missing Commands, Codegen Files, lev:// Protocol, and Static Gate Violation"; owner: lev-core; type: chore | # Chore: Poly Spec Missing Commands, Codegen Files, lev:// Protocol, and Static Gate Violation / ## The Problem / ### Gap 1: 6 undocumented command files
- `docs/specs/_done/chore-publisher-rename.md` (1094 bytes) — # Chore: Rename plugins/cms → plugins/publisher (C2) / ## Gap / ## Steps
- `docs/specs/_done/chore-rename-cms-pattern.md` (1672 bytes) — # Chore: Rename "CMS Pattern" → "View Materialization Pattern" (C2) / ## Gap / ## Targets
- `docs/specs/_done/chore-sdlc-spec-stale-counts.md` (1300 bytes) — title: "SDLC Spec Stale Program Count and Missing Command"; owner: lev-core; status: validated; type: chore | # Chore: SDLC Spec Stale Program Count and Missing Command — DONE / ## Implementation / ## Fitness Functions
- `docs/specs/_done/chore-spec-cms-control-plane.md` (1539 bytes) — # Chore: Spec CMS as Control Plane Over Graph (C2) — DONE / ## Resolution / ## Boundary enforcement
- `docs/specs/_done/chore-spec-inbox-actor-provenance.md` (1290 bytes) — # Chore: Spec Inbox Actor Provenance and Loop Suppression — DONE / ## Resolution / ## Design Decisions
- `docs/specs/_done/chore-spec-publish-targets.md` (1173 bytes) — # Chore: Define PublishTargetPort Contract (C4) — DONE / ## Resolution / ## Remaining (separate chores)
- `docs/specs/_done/chore-spec-storage-port.md` (1598 bytes) — # Chore: Define CanonicalStorageAdapter Contract (C1) — DONE / ## Resolution / ## Remaining (separate chores)
- `docs/specs/_done/chore-specs-readme-index.md` (967 bytes) — # Chore: Add Missing Specs to README Index / ## Gap / ## Missing Specs
- `docs/specs/_done/chore-telemetry-bdd-test-coverage.md` (1387 bytes) — title: "Chore: Telemetry BDD Test Coverage"; owner: lev-core; type: chore | # Chore: Telemetry BDD Test Coverage / ## Problem / ## Resolution — tick 124
- `docs/specs/_done/chore-telemetry-contract-tests.md` (1502 bytes) — title: "Telemetry & UI Renderers Contract Tests"; owner: lev-core; status: validated; type: chore | # Chore: Telemetry & UI Renderers Contract Tests — DONE / ## Phase 1: Telemetry contract tests — DONE / ## Phase 2: UI renderers smoke tests — DONE
- `docs/specs/_done/chore-telemetry-spec-api-mismatch.md` (3415 bytes) — title: "Telemetry Spec API Surface Mismatch — withSpan Uses Wrong Tracer Method"; owner: lev-core; type: chore | # Chore: Telemetry Spec API Surface Mismatch — withSpan Uses Wrong Tracer Method / ## The Problem / ### Gap 1 (BUG): `withSpan()` uses `startSpan` instead of `startActiveSpan`
- `docs/specs/_done/chore-ui-render-fallback.md` (2660 bytes) — # Chore: UI Renderer Throws on Missing Platform Instead of Fallback / ## The Problem / ### Additional issue: Package naming mismatch
- `docs/specs/_done/chore-ui-render-output-mismatch.md` (861 bytes) — title: "UI Spec RenderOutput Count and PlatformCaps Gap"; owner: lev-core; status: validated; type: chore | # Chore: UI Spec RenderOutput Count and PlatformCaps Gap / ## Implementation — DONE / ## Fitness Functions
- `docs/specs/_done/chore-validation-gates-spec-yaml-disconnect.md` (4034 bytes) — title: "Chore: Validation Gates Spec↔YAML Disconnect"; type: chore | # Chore: Validation Gates Spec↔YAML Disconnect / ## Problem / ### Two Naming Conventions
- `docs/specs/_done/chore-workflow-path-drift.md` (770 bytes) — # Chore: Workflow Path Drift (C7) / ## Gap / ## Steps
- `docs/specs/_done/proposal-deerflow-harness-features.md` (6933 bytes) — title: "DeerFlow Harness Features Integration"; owner: lev-core; type: proposal | # Proposal: DeerFlow Harness Features Integration / ## Summary / ## Problem Statement
- `docs/specs/proposal-cli-statusline-classifier.md` (18487 bytes) — title: Entity Lifecycle Status Line with Ollama Classification; owner: lev-core; type: spec | # Spec: Entity Lifecycle Status Line with Ollama Classification / ## 1. Business Case / ### Problem Statement
- `docs/specs/proposal-memory-self-learning-pipeline.md` (17924 bytes) — title: Self-Learning Pipeline; owner: lev-core; type: spec | # Spec: Self-Learning Pipeline / ## 1. Business Case / ### Problem Statement
- `docs/specs/proposal-scan-ingestion-and-dictionary-transport.md` (10412 bytes) — title: Scan Ingestion and Dictionary Transport; owner: lev-core; type: spec | # Proposal: Scan Ingestion and Dictionary Transport / ## 1. Why This Proposal / ## 2. Problem Statement
- `docs/specs/proposal-validation-ubs-integration.md` (5072 bytes) — title: UBS Lev SDLC Integration; owner: lev-core; type: spec | # UBS Integration into Lev SDLC / ## Decisions / ## agentguard Status (as investigated)
- `docs/specs/spec-agentfs.md` (25507 bytes) — title: lev-agentfs Upgrade Plan; owner: lev-core; type: spec | # lev-agentfs Upgrade Plan / ## Current State / ## Canonical Ownership and Placement
- `docs/specs/spec-agentping-host-relationship.md` (15453 bytes) — title: Lev ↔ AgentPing Host Relationship; owner: lev-core; type: spec | # Spec: Lev ↔ AgentPing Host Relationship / ## Executive Summary / ## Purpose
- `docs/specs/spec-agentping-remote.md` (25174 bytes) — title: NTM x AgentPing Remote Worker Integration; owner: lev-core; type: spec | # Spec: NTM x AgentPing Remote Worker Integration / ## Executive Summary / ## Context
- `docs/specs/spec-agentping-surfaces.md` (19883 bytes) — title: Unify AgentPing Surfaces; owner: lev-core; type: spec | # Spec: Unify AgentPing Surfaces / ## Executive Summary / ## 1. Current State
- `docs/specs/spec-agentping.md` (14122 bytes) — title: AgentPing Protocol; owner: lev-core; type: spec | # AgentPing Specification (Core) / ## Executive Summary / ## Current State
- `docs/specs/spec-build.md` (12688 bytes) — title: Build Package Boundary — Build-Time Only; owner: lev-core; type: spec | # Spec: Build Package Boundary (Build-Time Only) / ## 1. Decision / ## Canonical Ownership
- `docs/specs/spec-cascading-context.md` (11887 bytes) — title: "Cascading Context Resolution Chain"; status: draft; type: spec; owner: lev-core | # Spec: Cascading Context Resolution Chain / ## Executive Summary / ## Resolution Chain
- `docs/specs/spec-cms-control-plane.md` (10179 bytes) — title: CMS Control Plane; owner: lev-core; type: spec | # Spec: CMS Control Plane / ## Executive Summary / ## Why This Spec Exists
- `docs/specs/spec-config.md` (20680 bytes) — title: Config Sprawl Elimination and Fractal Governance; owner: lev-core; type: spec | # Lev Config Sprawl Elimination and Fractal Governance — Behavioral Specification / ## Executive Summary / ## Context
- ... 779 more in JSON sidecar

## Largest files

| file | bytes | type |
|---|---:|---|
| `workshop/intake/memory-bank-ai-agent-productivity/Memory Bank - 10X Your AI Agent Productivity! Cline, Roo, Kilo, Cursor, Windsurf.webm` | 47822604 | `.webm` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/wal/open-1` | 33554432 | `[none]` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/wal/open-2` | 33554432 | `[none]` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/segments/3c7b5d4c-faff-4d4d-977e-7843abaae904/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/segments/9ad3d795-3d4b-43aa-9383-47bfa4dfeea4/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/segments/e9753a0a-055d-46da-89ce-023fd9c1d904/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/segments/3ecd0333-255a-4883-a5ee-22d50c5bdbd6/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/segments/69fb6b52-9a53-4fac-b6df-34070341d49a/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/segments/7e70bfaa-a60f-4d28-950c-dff01736228d/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/segments/9987eb79-2df6-42cd-b13d-8cd08c501bd6/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-local-principles/0/segments/9ff5b62b-47d9-40dd-b772-53e571192200/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/wal/open-1` | 33554432 | `[none]` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/wal/open-2` | 33554432 | `[none]` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/segments/c2dea58c-054c-4edb-b217-5ce4b489e891/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/segments/f7fb1acf-0622-496a-b8d1-f8d935206202/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/segments/c4601848-a98e-4c07-a125-3266f3db5b98/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/segments/5cc57757-d1c7-4a34-8906-1637abba99b5/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/segments/fef0a5c5-5a09-4712-a4dc-fcb26cfaaa07/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/segments/707a6455-06a4-4de7-9839-0668617e3fba/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/segments/3cef3819-adef-4db5-8bc1-538a3e6e4c87/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-requirements/0/segments/be983de4-bc6f-42e7-9337-955a7a50421b/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/wal/closed-0` | 33554432 | `[none]` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/wal/open-3` | 33554432 | `[none]` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/wal/open-2` | 33554432 | `[none]` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/segments/45148496-334e-4200-b617-2c59b6da402a/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/segments/4437d01a-5857-4ad8-a14f-8dd3026b46b5/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/segments/9ceac9c1-2497-4be1-a314-4332987c2e97/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/segments/04391dbe-4505-4eeb-93a8-67de6d208fb4/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/segments/28e3274e-26e9-47df-bf80-ae2b5cbf54ee/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/segments/2b622fed-1598-40fe-a15e-f56f35ef4f1a/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/segments/af0f7aec-0ee5-45a3-bb98-eebc57f7359a/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/project-go-stdlib-framework-docs/0/segments/0ed8253d-0583-4e71-811d-cd4809804631/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/global-principles/0/wal/open-1` | 33554432 | `[none]` |
| `os/agent/qdrant_storage/collections/global-principles/0/wal/open-2` | 33554432 | `[none]` |
| `os/agent/qdrant_storage/collections/global-principles/0/segments/94adf497-df1e-45a5-831e-26db1f606199/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/global-principles/0/segments/02a00e19-e9f6-49c4-b81c-bfa144c7595d/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/global-principles/0/segments/46a9a1ea-2244-4c60-a562-30ad5650015b/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/global-principles/0/segments/dad792d3-99fa-4784-ae14-805053f5e500/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/global-principles/0/segments/88c1393d-1ae9-4f7b-a3df-d6ef920dff5a/payload_storage/page_0.dat` | 33554432 | `.dat` |
| `os/agent/qdrant_storage/collections/global-principles/0/segments/ed60f34a-f458-4c09-8b1f-034e67e04904/payload_storage/page_0.dat` | 33554432 | `.dat` |

## Immediate wiki implication

- This repo is too large for one-pass synthesis. The wiki needs a project front door, a source inventory, and bounded read packets.
- `docs/NORTH_STAR.md`, `docs/README.md`, `docs/ARCHITECTURE.md`, `docs/ROADMAP.md`, and `docs/specs/` should be read before generated chats or design inboxes are promoted.
- Chat/transcript material should be split into: owner Josh statements, JP/Lev-dev statements, assistant/model elaboration, and current repo evidence.
