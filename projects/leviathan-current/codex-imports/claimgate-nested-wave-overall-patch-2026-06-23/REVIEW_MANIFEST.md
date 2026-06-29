# Review Manifest

## Base

```text
base_commit: f9185635334f6e1232504306169a3af1da6eedd4
patch_sha256: 5527cbac266b31f34cb39033d7312b83dab7175ab7fda27c0b72a83e1b2a9d82
```

## Patch scale

```text
22 files changed
9019 insertions
63 deletions
```

See:

- `review-stat.txt`
- `name-status.txt`
- `numstat.txt`

## File groups

### ClaimGate steering and host-consumption boundary

- `core/orchestration/src/handlers/claimgate-steering.ts`
- `core/orchestration/src/handlers/claimgate-steering.test.ts`
- `core/orchestration/src/proof/claim-gate-steering-run.ts`
- `core/orchestration/src/proof/claim-gate-steering-run.test.ts`

Purpose: keep source projections from self-promoting, expose/verify host consumption, preserve authority boundary.

### ClaimGate council-wave loop

- `core/orchestration/src/proof/claim-gate-loop.ts`
- `core/orchestration/src/proof/claim-gate-loop.test.ts`
- `core/orchestration/src/handlers/claim-gate-loop.ts`
- `core/orchestration/src/handlers/claim-gate-loop.test.ts`

Purpose: formalize council-wave input, required gates, failure packets, requeue events, repair-wave planning, graph-patch proposal/admission/apply-plan receipt boundaries.

### Harness repair dispatch and CDO integration

- `core/harness/src/execution/claim-gate-repair-dispatch.ts`
- `core/harness/src/execution/claim-gate-repair-dispatch.test.ts`
- `core/harness/src/execution/cdo-triple50.ts`
- `core/harness/src/execution/cdo-triple50.test.ts`
- `core/harness/src/execution/index.ts`

Purpose: route ClaimGate failure packets into repair dispatch and bind council-wave surfaces into CDO/triple50 execution.

### Package/config/test visibility

- `core/orchestration/package.json`
- `core/orchestration/config.yaml`
- `core/orchestration/src/index.ts`
- `core/orchestration/src/proof/index.ts`
- `core/orchestration/vitest.config.ts`
- `core/harness/package.json`
- `core/harness/vitest.config.ts`

Purpose: expose the new surfaces and make targeted tests discoverable.

### Sparse outside-model flow

- `.lev/flows/cdo-openrouter-sparse.flow.yaml`
- `.lev/flows/cdo.openrouter.sparse.profile.yaml`

Purpose: bounded sparse external-model lane, not default bulk worker authority.

## Architecture note

The intended hierarchy is:

```text
Run / Wizard
  -> Waves
      -> Councils
          -> Subcouncils / Teams
              -> Agents
                  -> Skills + MMMs + Tools + Source Packs
```

The management plane is parallel:

```text
Operations Council: conductor, resource manager, laggard monitor
Context Council: skill/MMM/source/object loaders
Gate/Receipt Council: gate ops, receipt manager, evidence binder, claim ceiling watcher
Reroute Council: failure packet router, provider rerouter, repair dispatcher, human escalation router
```

## Claim ceiling

The patch is a candidate for review. It does not yet prove:

- all spawned agents load skills/MMMs at runtime;
- full nested wave/council execution is complete;
- production host admission;
- that every management-plane role is implemented;
- that the entire Lev repository is green.

It does preserve the upgrade direction and provides code/test surfaces to review.
