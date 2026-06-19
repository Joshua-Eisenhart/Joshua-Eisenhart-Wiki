---
title: Leviathan Security Gate Stack
created: 2026-06-19
updated: 2026-06-19
type: security-map
status: current-source-synthesis
claim_ceiling: security gate map only; not a security signoff or vulnerability clearance
tags: [leviathan, security, audit, gate-stack, v4]
sources:
  - projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19.md
  - projects/leviathan-current/proof-backed-status-dashboard.md
---

# Leviathan Security Gate Stack

Security is a stack of gates, not one audit command.

## Gate ladder

1. no known secret leaks in docs/wiki;
2. no obvious unsafe dynamic execution in critical paths;
3. child-process environment is explicitly whitelisted;
4. `pnpm audit --audit-level high` passes;
5. low/moderate risk reviewed;
6. auth/token/cache surfaces reviewed;
7. agent execution sandbox/bounds tested;
8. daemon/service exposure reviewed;
9. AgentGuard/leases/ABAC enforcement proven on real flows;
10. release-candidate security signoff.

## Current caution

The roadmap names blockers such as `new Function`, legacy shell execution, ambient `process.env` leakage, and audit vulnerabilities. Do not summarize security as green from one command.

## Read next

- [[projects/leviathan-current/enterprise-readiness-gap-v4-2026-06-19]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]
- [[projects/leviathan-current/proof-backed-status-dashboard]]
