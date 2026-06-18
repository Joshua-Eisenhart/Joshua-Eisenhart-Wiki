---
title: Leviathan Current State and Roadmap
created: 2026-06-17
updated: 2026-06-17
type: status-wiki-page
status: packet-1 current-authority synthesis
claim_ceiling: roadmap/docs/code-scout synthesis; not build/test verification
sources:
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md
  - /Users/joshuaeisenhart/GitHub/leviathan/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/package.json
  - /Users/joshuaeisenhart/GitHub/leviathan/pnpm-workspace.yaml
---

# Current State and Roadmap

## Bottom line

The repo-current docs say Leviathan has a real foundation, but is not yet a finished universal agent runtime.

The strong part is the architecture: FlowMind, Graph, Event Bus, Exec/Poly/Daemon, AgentPing, specs, packages, CLI shape, event discipline, and constraint-manifold language are all visible. The weak part is product hardening: enterprise pillars, security, DX, MCP/A2A completeness, budget/resource enforcement, and some docs/code drift remain open.

## Current-state claims from `ROADMAP.md`

| Area | Roadmap claim | Status label |
|---|---|---|
| Framework decoupling | 70% framework-decoupled; 10 modules fully decoupled, 5 soft-coupled, 2 hard-coupled. | roadmap claim |
| Providers | 11 provider harnesses. | roadmap claim; count drift exists in docs |
| MCP | 5 MCP client adapters, 0 MCP servers implemented; 7 needed. | roadmap claim; code has a stub-like MCP surface |
| Enterprise | 0/9 pillars enterprise-ready; 2 partial, 5 minimal, 2 missing. | roadmap claim |
| Security | `process.env` passed wholesale to spawned agents. | roadmap risk |
| DX | 6.2/10; quick wins include links/install/examples/`lev init`. | roadmap risk |
| Release readiness | 837 files security-hardened; 118 dependency vulnerabilities remaining. | roadmap claim |
| Execution reality | 1.46:1 docs-to-code ratio; 1,031 test files; 60+ CLI commands; 4 CI workflows. | roadmap claim |

## Active workstreams named by roadmap

- Voice-first orchestration.
- `lev-forge` self-hosted CI/CD and VCS stacking.
- 5-tier memory.
- Framework intake.
- Architecture convergence / S10.
- OSS release.

## 2026 execution phases named by roadmap

1. **Foundation** — framework-agnostic core, enterprise POCs, agent identity.
2. **Protocol** — MCP-native everything.
3. **Enterprise pillars** — ABAC, audit trails, kill switches, cost tracking, resource governor, approvals, compliance.
4. **Open Source Launch** — OSS/enterprise split, examples, `lev init`, contributor guide, community launch.

## What is doing well

Observed from docs/package/code scout:

- The project has a coherent ownership map: modules have named package surfaces and specs.
- `core/poly/bin/lev` is the root CLI entry path in package metadata.
- The runtime has explicit separations: FlowMind does not dispatch workers; Orchestration does not mutate policy; Graph does not schedule; Event Bus carries lifecycle events.
- The repo has a serious spec corpus: `docs/specs/README.md` says 61 specs.
- The project is unusually explicit about its own gaps. That is a strength because it gives the wiki a real status map rather than only marketing language.

## Where it is failing or under-built

Observed from current docs and cheap checks:

- **Security**: roadmap explicitly flags wholesale `process.env` passing to spawned agents.
- **Enterprise**: roadmap says 0/9 pillars are enterprise-ready.
- **Protocol**: roadmap says 0 MCP servers implemented, even though code has a `core/poly/src/surfaces/mcp/index.ts` surface; this needs status clarification.
- **DX**: roadmap calls out broken links/install/examples and missing `lev init` as quick wins.
- **Architecture vs implementation**: root README says architecture is ahead of some implementation.
- **Status drift**: some spec statuses and paths conflict; see `contract-surface-map.md`.
- **Planning debt**: North Star names docs-to-code ratio and bus factor as high/critical risks.

## Where it is promising

- The constraint manifold is not just prose: it appears in FlowMind system declarations and kernel code surfaces.
- The package topology is broad enough to be a real runtime rather than a single wrapper library.
- The event bus / graph / orchestration / policy split gives the system a way to avoid one giant black-box agent loop.
- The OSS/enterprise split has a recognizable business structure: useful core runtime for free; governance and enterprise hardening for paid deployments.
- AgentPing and LevUI IR give the runtime a non-chat surface strategy.

## Tensions to preserve

Do not smooth these away:

1. **Vision vs current hardening** — the docs say “operating system for agent-human symbiosis,” but also say the universal graph and enterprise readiness are not complete.
2. **MCP-native positioning vs roadmap gap** — docs market MCP-native direction, but roadmap says 0 MCP servers.
3. **Provider count drift** — docs mention 10 and 11 provider harnesses in different places.
4. **AgentLease pillar vs implementation evidence** — AgentLease is central in vision, but identity/permissions/enterprise controls are not complete.
5. **Quick-start vs DX warnings** — README has a normal quick start; North Star/Roadmap say install/examples/DX need repair.
6. **Roadmap date drift** — roadmap frontmatter says 2026-02-20 while footer says 2026-03-14.

## Next verification packets

- Packet 2 should run module-by-module code/spec checks and, where safe, targeted tests.
- Packet 3 should separate AgentPing / AgentLease product surfaces from implementation status.
- Packet 4 should map Josh's contributions using exact repo, design, PM, and chat provenance.
