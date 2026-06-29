---
title: Lev Nested Wave Council Management Plane Patch Bundle
created: 2026-06-23
type: codex-memory-context-packet
status: patch_preserved_not_applied
source_repo: /Users/joshuaeisenhart/GitHub/lev
claim_ceiling: selected patch bundle only; not Lev canon, not merged, not fully revalidated in this preservation step
patch_file: lev-nested-wave-council-management-selected.patch
patch_sha256: 5527cbac266b31f34cb39033d7312b83dab7175ab7fda27c0b72a83e1b2a9d82
---

# Lev Nested Wave Council Management Plane Patch Bundle

## Why this exists

This preserves the current ClaimGate / nested-council / management-plane upgrade as a bounded patch bundle instead of spreading it into Lev canon during a dirty worktree session.

The user correction that controls this bundle:

```text
Waves are nested sets of councils. Many so-called waves are actually councils.
Lev also needs a parallel management plane: management agents, rerouting agents,
resource managers, context loaders, laggard monitors, gate operators, and receipt managers.
```

## Architecture captured

```text
WizardRun
  Work Plane
    sequenced Waves
      nested Councils
        subcouncils / teams
          agents
            skills + MMMs + tools + source packs

  Management Plane
    Run Conductor
    Resource Manager
    Context Loader
    Laggard Monitor
    Reroute Manager
    Failure Packet Router
    GateOps Manager
    Receipt Manager
    Blackboard / State Manager
    Claim Ceiling Manager
    Human Escalation Manager

  Gate Plane
    Lev root gates
    ClaimGate promotion gates
    host eval / receipt / admission
```

## Included patch surfaces

Tracked diffs included:

- `core/orchestration/src/handlers/claimgate-steering.ts`
- `core/orchestration/src/proof/claim-gate-steering-run.ts`
- `core/orchestration/src/proof/claim-gate-steering-run.test.ts`
- `core/orchestration/src/proof/index.ts`
- `core/orchestration/src/index.ts`
- `core/orchestration/package.json`
- `core/orchestration/vitest.config.ts`
- `core/orchestration/config.yaml`
- `core/harness/src/execution/cdo-triple50.ts`
- `core/harness/src/execution/cdo-triple50.test.ts`
- `core/harness/src/execution/index.ts`
- `core/harness/package.json`
- `core/harness/vitest.config.ts`

Untracked new-file diffs included when present:

- `core/orchestration/src/proof/claim-gate-loop.ts`
- `core/orchestration/src/proof/claim-gate-loop.test.ts`
- `core/orchestration/src/handlers/claim-gate-loop.ts`
- `core/orchestration/src/handlers/claim-gate-loop.test.ts`
- `core/orchestration/src/handlers/claimgate-steering.test.ts`
- `core/harness/src/execution/claim-gate-repair-dispatch.ts`
- `core/harness/src/execution/claim-gate-repair-dispatch.test.ts`
- `.lev/flows/cdo-openrouter-sparse.flow.yaml`
- `.lev/flows/cdo.openrouter.sparse.profile.yaml`

## Explicitly excluded from this patch

The Lev working tree currently contains many unrelated dirty paths, including app UI, graph, flowmind, poly, sdlc, event logs, and generated reports. Those are not included here. This bundle is intentionally narrow: ClaimGate steering, council-wave loop surfaces, cdo-triple50 execution binding, and repair dispatch.

## Claim ceiling

This is a saved patch candidate and context packet. It is not:

- an applied Lev architecture decision;
- a committed implementation;
- proof that the runtime loads every skill/MMM before spawn;
- proof that nested waves/councils are fully managed at runtime;
- proof that all dirty repo changes are coherent.

Before promotion, re-apply in a clean branch/worktree and run targeted tests.

## Promotion path

1. Review the patch against current `dna/graph.yaml` and `.lev/validation-gates.yaml`.
2. Split into smaller patches if needed:
   - ClaimGate loop/contracts;
   - cognitive member manifest gate;
   - management-plane contracts;
   - repair dispatch and laggard/reroute semantics;
   - CDO/triple50 integration.
3. Add formal schemas:
   - `WaveRecipe`;
   - `CouncilRecipe`;
   - `ManagementAgentRecipe`;
   - `GateContract`;
   - `GateToWaveRoute`;
   - `FailurePacket`.
4. Require loader receipts before claiming `MMM-backed` or `skill-backed` execution.
5. Consume through host Lev gates before any graph mutation claim.

## Patch integrity

```text
sha256  5527cbac266b31f34cb39033d7312b83dab7175ab7fda27c0b72a83e1b2a9d82  lev-nested-wave-council-management-selected.patch
```
