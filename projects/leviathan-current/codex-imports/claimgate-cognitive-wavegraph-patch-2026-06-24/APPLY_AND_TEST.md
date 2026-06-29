# Apply And Test

Base commit:

```text
f9185635334f6e1232504306169a3af1da6eedd4
```

Apply check:

```bash
git apply --check claimgate-cognitive-wavegraph.patch
```

Apply:

```bash
git apply claimgate-cognitive-wavegraph.patch
```

Focused validation used in the live dependency-bearing checkout:

```bash
cd core/orchestration
pnpm exec vitest run \
  src/proof/claim-gate-model-lane-runners.test.ts \
  src/proof/claim-gate-loop.test.ts \
  src/proof/claim-gate-steering-run.test.ts \
  src/proof/claim-gate-wavegraph-slice.test.ts \
  src/handlers/claim-gate-loop.test.ts \
  src/handlers/claimgate-steering.test.ts
pnpm exec tsc --noEmit
```

Additional hygiene used:

```bash
git diff --check -- \
  core/orchestration/package.json \
  core/orchestration/src/proof/claim-gate-model-lane-runners.ts \
  core/orchestration/src/proof/claim-gate-model-lane-runners.test.ts \
  core/orchestration/src/proof/claim-gate-wavegraph-slice.ts \
  core/orchestration/src/proof/claim-gate-wavegraph-slice.test.ts \
  core/orchestration/src/proof/index.ts \
  core/orchestration/src/index.ts
rg -n "export \\*" core/orchestration/src/index.ts core/orchestration/src/proof/index.ts
```

Expected result from focused validation:

```text
6 test files passed
97 tests passed
typecheck passed
```

Known unrelated warning: duplicate `test:pentagon` and `test:pentagon:gate`
script keys in the root `package.json`.
