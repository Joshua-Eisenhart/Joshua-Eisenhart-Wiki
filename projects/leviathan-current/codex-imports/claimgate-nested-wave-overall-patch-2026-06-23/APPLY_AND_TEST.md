# Apply And Test Recipe

## Apply without pushing

From a clean Lev checkout:

```bash
git checkout -b review/claimgate-nested-wave-20260623
git apply --check claimgate-nested-wave-overall.patch
git apply claimgate-nested-wave-overall.patch
```

No push is required. If GitHub review is needed later, push the branch only after local review:

```bash
git push -u origin review/claimgate-nested-wave-20260623
```

## Targeted tests

Run the orchestration ClaimGate tests:

```bash
cd core/orchestration
pnpm exec vitest run \
  src/proof/claim-gate-loop.test.ts \
  src/handlers/claim-gate-loop.test.ts \
  src/proof/claim-gate-steering-run.test.ts \
  src/handlers/claimgate-steering.test.ts
```

Run the harness execution tests:

```bash
cd core/harness
pnpm exec vitest run --config vitest.config.ts \
  src/execution/claim-gate-repair-dispatch.test.ts \
  src/execution/cdo-triple50.test.ts
```

Run typechecks:

```bash
pnpm --filter @lev-os/orchestration typecheck
pnpm --filter @lev-os/harness-sdk typecheck
```

## Expected first-pass review result

The patch should apply cleanly to base commit:

```text
f9185635334f6e1232504306169a3af1da6eedd4
```

A clean apply-check was verified before this packet was created.

## If it is too large

Split in this order:

1. `core/orchestration/src/proof/claim-gate-loop.ts` and tests.
2. `core/orchestration/src/handlers/claim-gate-loop.ts` and handler tests.
3. `core/harness/src/execution/claim-gate-repair-dispatch.ts` and tests.
4. `core/harness/src/execution/cdo-triple50.ts` integration.
5. OpenRouter sparse flow/profile.
