---
title: AgentPing Human-Loop Surfaces
created: 2026-06-18
updated: 2026-06-18
type: product-surface-map
status: candidate/controller-verification-required
claim_ceiling: current-source wiki map; not runtime health proof; not standalone AgentPing release assessment
---

# AgentPing Human-Loop Surfaces

## Bottom line

AgentPing is the named human-loop surface layer for Lev: it turns agent events into visible, auditable, resumable interactions for humans.

The checked sources support a strong architectural claim, but not a full runtime-health claim. Lev docs say AgentPing is the default interaction layer; specs define protocol and dashboard expectations; source paths for an adapter and E2E test exist. This page does not claim the AgentPing submodule currently builds or passes tests.

## What AgentPing is in current docs

| Claim | Support | Source |
|---|---|---|
| AgentPing is the default human-loop surface and interaction layer. | repo-doc claim | `/Users/joshuaeisenhart/GitHub/leviathan/docs/README.md` lines 39-47 |
| AgentPing is highlighted as an AI-native interaction protocol and human-loop surface system. | repo-doc claim | `/Users/joshuaeisenhart/GitHub/leviathan/README.md` lines 66-75 |
| The North Star treats AgentPing as the surface where humans interact with agents beyond chat. | repo-doc claim / product vision | `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md` lines 17-23 and 44-66 |
| AgentPing can be absent while Lev still functions as runtime/SDK/CLI infrastructure. | repo-doc claim | `/Users/joshuaeisenhart/GitHub/leviathan/docs/README.md` lines 41-47 |

Plain version:

```text
Lev can run as a runtime without AgentPing, but Lev as a full human-facing surface product expects an AgentPing-like host.
```

## Protocol shape

`docs/specs/spec-agentping.md` says AgentPing defines typed ping/pong interactions. It names pings such as notification, approval, selection, input, step approval, confirmation, progress, data request, escalation, and context update.

Support level: **repo spec / draft lifecycle**, not verified running service.

Key source:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-agentping.md` lines 31-38 describes the protocol, HTTP API, Web UI, WebSocket endpoint, SDK state, and current permissive validation limits.
- Lines 39-49 define target-state lifecycle requirements: registration, ping lifecycle, structured payloads, blocking approval workflows, health protocol, and timeout semantics.
- Lines 50-62 map ownership to `community/agentping/**`, adapters, API client, web UI, CLI, Slack/webhook adapters, and a Lev integration bridge.

## Surface unification target

`docs/specs/spec-agentping-surfaces.md` describes a target to merge separate canvas-like surfaces into one web UI with Studio as a mode, canvas components, and expand/contract UX.

Support level: **draft spec / target state**.

Important guard: the same file explicitly says the current state is three separate canvas-like surfaces and the target is a unified web UI. So the wiki should not describe the unified surface as already landed.

Source:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-agentping-surfaces.md` lines 32-35 and 38-52.

## Host relationship

The host relationship spec says AgentPing is a sister project, standalone in its own right, and the default dashboard host/UI kit for full Lev surface experiences.

Support level: **repo spec / architectural boundary**.

Source:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-agentping-host-relationship.md` lines 31-33: Lev is protocol authority; AgentPing is reference host implementation.
- Lines 39-68: AgentPing is a standalone host; Lev can function as SDK/CLI/runtime substrate without it, but needs a host project for full dashboard experience.
- Lines 78-90: current host-agent relationship is informal and target state is formal host registration, capability declaration, lifecycle, trust delegation, and standalone verification.

## Observed code/test surfaces

| Surface | Support | Notes |
|---|---|---|
| `plugins/core-platforms/src/adapters/agentping.ts` | observed file/path | Generates `agentping.yaml` and `.agentping/config.json` for dashboard-runner integration; writes Storybook/dev-server dashboard configs. |
| `tests/e2e/real/03-agentping-dashboard/agentping.test.ts` | observed test file/path | Test source starts AgentPing daemon from `community/agentping`, hits `/health`, and checks status `ok`; this page did not run it. |
| `community/agentping` | observed submodule/path signal | Current `git status --short` shows `m community/agentping`; dirty submodule state means runtime claims need fresh source-specific verification. |

## What is open

- This page did not run AgentPing daemon tests.
- This page did not verify the `community/agentping` submodule build or package state.
- The docs contain strong target-state language; controller should keep `draft`, `target`, and `observed file` separate.
- Runtime health remains **open** until the daemon, dashboard, adapter generation, and relevant E2E test are run in a clean bounded check.

## Overclaim guard

Safe wording:

```text
AgentPing is Lev's default human-loop surface layer and reference host direction. Specs and adapter/test files exist. Runtime health still needs a fresh build/test check.
```

Unsafe wording:

```text
AgentPing is fully landed, production-ready, or canonically healthy.
```
