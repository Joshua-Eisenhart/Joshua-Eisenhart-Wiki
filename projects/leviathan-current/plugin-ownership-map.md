---
title: Plugin Ownership Map
created: 2026-06-17
updated: 2026-06-19
type: runtime-plugin-map
status: current-source-reader
source_repo: lev-os/leviathan
source_snapshot: b7bca2cdbed5862743395f7c0330e7d640132764
claim_ceiling: source/package inventory and ownership map; not plugin runtime proof; not full plugin audit
sources:
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ARCHITECTURE.md
  - https://github.com/lev-os/leviathan/tree/b7bca2cdbed5862743395f7c0330e7d640132764/plugins
---

# Plugin Ownership Map

## Current Correction

The older Packet 2 plugin map was written against a damaged local checkout and an older plugin inventory. A fresh 2026-06-19 clone at `b7bca2cdbed5862743395f7c0330e7d640132764` found flat current plugin paths such as `plugins/platforms/**`, `plugins/sdlc/**`, `plugins/bench/**`, and `plugins/gameai/**`.

Do not use old `plugins/core-platforms/**` or `plugins/core-sdlc/**` wording on current pages except as historical alias context.

## Boundary Summary

Plugins are runtime/domain extensions. They can contribute FlowMind programs, Poly surfaces, daemon processes, adapters, commands, templates, and domain-specific behavior. They do not take over the core ownership of FlowMind, Orchestration, Graph, Event Bus, Exec, Poly, or Daemon.

## Current Plugin Package Inventory

Fresh package-path scan found these plugin packages:

```text
plugins/apptestr
plugins/auth-sniffer
plugins/autoresearch
plugins/beads
plugins/bench
plugins/browser
plugins/cdo
plugins/claw-router
plugins/code-graph
plugins/context
plugins/context-compress
plugins/dashboard
plugins/defendr
plugins/deploy
plugins/discourse-graph
plugins/dna
plugins/erc
plugins/evolve-memory
plugins/gameai
plugins/genui-exec-daemon
plugins/graph-adapters
plugins/graph-trustgraph
plugins/guardrails
plugins/harness-patterns
plugins/mastra
plugins/notion
plugins/now
plugins/obsidian-surface
plugins/osint
plugins/platforms
plugins/prompt-stack
plugins/publisher
plugins/pulumi
plugins/reactive
plugins/reasoning-enhance
plugins/samurai
plugins/scheduling
plugins/sdlc
plugins/sentinel
plugins/sim-eval
plugins/slate
plugins/timetravel
plugins/token-compress
plugins/vault
plugins/vision
plugins/voice
plugins/watchdog
plugins/wiggum-marketer
plugins/workflow-orchestrator
plugins/workshop
plugins/writer
```

This is package existence, not proof each plugin builds or works.

## Architecture-Owned Plugin Categories

`docs/ARCHITECTURE.md` names these high-level plugin ownership categories:

| Category | Current path |
|---|---|
| Platform integrations | `plugins/platforms/**` |
| SDLC integration surfaces | `plugins/sdlc/**` |
| Deployment adapters | `plugins/deploy/**` |
| Beads artifact tracking | `plugins/beads/**` |
| Graph adapter extensions | `plugins/graph-adapters/**` |
| Mastra workflow integration | `plugins/mastra/**` |
| Notion direct API integration | `plugins/notion/**` |
| Voice-first interaction surface | `plugins/voice/**` |
| Multi-modal capture and perception | `plugins/vision/**` |
| Auth pattern detection | `plugins/auth-sniffer/**` |
| Browser automation cascade | `plugins/browser/**` |
| Biomimetic memory / skill evolution | `plugins/evolve-memory/**` |

## Not Checked Here

No plugin builds, tests, config validators, daemon launches, Poly registry builds, or MCP/CLI smokes were run for this page.
