# Trust-spine red-team: 5 test specs (for Codex)

Perfect. Now let me create a concise summary as my final output:

```typescript
// SUMMARY OF 5 CONCRETE RED-TEAM TEST SPECS FOR LEV TRUST SPINE

// Spec 1: Forged Engine Digest Reaching Wizard Runner
// File: core/orchestration/src/handlers/lev-wizard-ratchet.test.ts
// Test name: 'rejects forged engine digest not host-built (A-prime regression)'
// Attack: External caller provides structurally valid LevEngineSubstrateDigest
//         that was NOT built by the real three-engine runner
// Expected: engineSubstrateValidation.ok = false
//           findings include "digest must be host-built by the Lev real-engine runner"
// Avoid: Do NOT mock isHostBuiltLevEngineSubstrateDigest() to return true


// Spec 2: Stale Engine Source Hash (Digest Built with Old Carrier Code)
// File: core/orchestration/src/handlers/lev-wizard-ratchet.test.ts
// Test name: 'rejects engine digest with stale source hashes'
// Attack: Digest legitimately host-built, but carrier scripts (Julia/JAX/PyTorch)
//         have been updated since; digest carries OLD hashes
// Expected: engineSubstrateValidation.ok = false
//           findings include hash mismatch between digest lanes and current carrier
// Avoid: Do NOT stub carrier code loader or use mocked readFileSync()


// Spec 3: External Digest Injection via Exported runLevWizardRatchetCouncil
// File: core/orchestration/src/handlers/lev-wizard-ratchet.test.ts
// Test name: 'rejects engine digest injected via runLevWizardRatchetCouncil input'
// Attack: External caller calls exported function directly with forged digest,
//         bypassing buildRealThreeEngineEnvelopeAndDigest() flow
// Expected: engineSubstrateValidation.ok = false (same as Spec 1)
// Avoid: Do NOT set engineSubstrateAuthority='test_fixture_only' or NODE_ENV='test'


// Spec 4: Serialized/Same-Process Digest Replay (No Nonce Detection)
// File: core/orchestration/src/handlers/lev-wizard-ratchet.test.ts
// Test name: 'replay of captured real digest in same process (no nonce detection)'
// Attack: Real digest captured from prior run, replayed in later run (same process).
//         Without nonce/run-id/timestamp, digests are indistinguishable.
// Expected CURRENT: engineSubstrateValidation.ok = true (VULNERABILITY CONFIRMED)
// Expected FIXED: ok = false with "run-id mismatch" finding (after nonce added)
// Implementation: Run wizard twice, capture digest from first, pass to second.
//                 Assert ok=true, document that future nonce will flip this to false.
//                 DO NOT implement the fix in this test.
// Avoid: Do NOT seed HOST_BUILT_ENGINE_SUBSTRATE_DIGEST_HASHES as empty


// Spec 5A: Test-Fixture Bypass Authority Confined to NODE_ENV=test
// File: core/orchestration/src/handlers/lev-wizard-ratchet.test.ts
// Test name: 'test_fixture_only authority confined to NODE_ENV=test (part A)'
// Attack: Setter can invoke runLevWizardRatchetCouncil with
//         engineSubstrateAuthority='test_fixture_only' AND NODE_ENV='test'
// Expected: engineSubstrateValidation.ok = true (bypass allows test fixtures)
// This test documents that the bypass EXISTS and works as designed for unit tests.


// Spec 5B: Authority Bypass Blocked When NODE_ENV !== 'test'
// File: core/orchestration/src/handlers/lev-wizard-ratchet.test.ts
// Test name: 'test_fixture_only authority blocked when NODE_ENV !== test (part B)'
// Attack: Same as 5A, but NODE_ENV is set to 'production' (or undefined)
// Expected: engineSubstrateValidation.ok = false (bypass is ignored)
//           findings include standard "caller-provided digest is projection-only"
// Assertion: engineSubstrateAuthority flag has no effect outside test environments


// Spec 5C: Authority Bypass Confined to Test Runtime Path Only
// File: core/orchestration/src/handlers/lev-wizard-ratchet.test.ts
// Test name: 'engineSubstrateAuthority parameter not exposed in production handler'
// Assertion: engineSubstrateAuthority is ONLY in the exported test function,
//            NOT in any production orchestration entry point.
//            Codebase search: grep for engineSubstrateAuthority in src/handlers/
//            should appear ONLY in handler test code, never in production CLI.


// KEY GATES BEING TESTED:
// 1. validateLevEngineSubstrateDigest() — contract shape validation
// 2. isHostBuiltLevEngineSubstrateDigest() — in-process Set<string> tracking
// 3. engineSubstrateAuthority flag + NODE_ENV guard
//
// KNOWN VULNERABILITIES THESE SPECS WILL CATCH:
// - Forged digests from untrusted sources
// - Stale/outdated engine code signatures
// - Digest replay within same process (no nonce)
// - Test-fixture escape hatch leaking to production
//
// CURRENT IMPLEMENTATION GAPS (from memory):
// - No nonce/run-id/timestamp in digest → replay vulnerability (Spec 4)
// - No process-spanning digest auth beyond Set (confirmed by host-trust-secret.ts notes)
// - test_fixture_only bypass guarded only by NODE_ENV check (Spec 5 validates boundary)
```

Now I'll output the final answer:

---

# Five Concrete Red-Team Test Specifications for Lev Trust Spine

I've drafted five precise red-team test specs for the engine digest validation backbone. Each spec defines the attack vector, exact forged input shape, expected validation fields, and pass-by-construction risks to avoid.

## Test Specification Summary

**Spec 1: Forged Engine Digest Reaching Wizard Runner** ✓
- **File:** `core/orchestration/src/handlers/lev-wizard-ratchet.test.ts`
- **Test name:** `'rejects forged engine digest not host-built (A-prime regression)'`
- **Attack:** External caller provides structurally valid `LevEngineSubstrateDigest` that is NOT in `HOST_BUILT_ENGINE_SUBSTRATE_DIGEST_HASHES`
- **Expected result:** `engineSubstrateValidation.ok === false`, findings include "digest must be host-built by the Lev real-engine runner; caller-provided digest is projection-only"
- **Gate being tested:** `isHostBuiltLevEngineSubstrateDigest()` at line 1322
- **Pass-by-construction risk:** Do NOT mock `isHostBuiltLevEngineSubstrateDigest()` to return true; verify the function returns false for non-built digests

**Spec 2: Stale Engine Source Hash (Old Carrier Code)** ✓
- **File:** `core/orchestration/src/handlers/lev-wizard-ratchet.test.ts`
- **Test name:** `'rejects engine digest with stale source hashes'`
- **Attack:** Digest legitimately host-built earlier, but Julia/JAX/PyTorch carrier code has since been updated; digest carries OLD hashes in its lane records
- **Expected result:** `engineSubstrateValidation.ok === false`, findings include hash mismatch (e.g., "julia lane input hash mismatch: expected sha256:new-..., got sha256:old-...")
- **Gate being tested:** Source hash validation in `validateLevEngineSubstrateDigest()` lanes comparison
- **Pass-by-construction risk:** Do NOT bypass source-hash comparison by stubbing the carrier loader; the test must compute fresh carrier hashes and compare against the digest's recorded lanes

**Spec 3: External Digest Injection via Exported runLevWizardRatchetCouncil** ✓
- **File:** `core/orchestration/src/handlers/lev-wizard-ratchet.test.ts`
- **Test name:** `'rejects engine digest injected via runLevWizardRatchetCouncil input parameter'`
- **Attack:** External caller calls the exported `runLevWizardRatchetCouncil()` function directly (line 2381) with a forged digest, bypassing the normal `buildRealThreeEngineEnvelopeAndDigest()` flow
- **Expected result:** `engineSubstrateValidation.ok === false` (same rejection as Spec 1, since the digest is not in the host-built set)
- **Gate being tested:** `isHostBuiltLevEngineSubstrateDigest()` at line 1322
- **Pass-by-construction risk:** Do NOT set `engineSubstrateAuthority: 'test_fixture_only'` or `NODE_ENV='test'`; verify the rejection happens even when the digest passes schema validation

**Spec 4: Serialized/Same-Process Digest Replay (No Nonce Protection)** ✓
- **File:** `core/orchestration/src/handlers/lev-wizard-ratchet.test.ts`
- **Test name:** `'replay of captured real digest in same process (no nonce detection)'`
- **Attack:** A real digest is captured from a successful wizard run, then replayed in a LATER run (same process, same user). Without a nonce/run-id/timestamp, the captured digest is indistinguishable from a fresh build.
- **Expected result — CURRENT (vulnerable):** `engineSubstrateValidation.ok === true` (digest still passes because its hash is in `HOST_BUILT_ENGINE_SUBSTRATE_DIGEST_HASHES`)
- **Expected result — IF FIXED (with nonce):** `ok === false`, findings include "run-id mismatch: expected run-id from context, got stale run-id from digest"
- **Implementation guidance:** Run wizard twice in same test; capture digest from first run; pass to second run. Assert `ok === true`. DOCUMENT that adding a nonce/run-id would flip this to false. DO NOT implement the fix in the test.
- **Pass-by-construction risk:** Do NOT clear `HOST_BUILT_ENGINE_SUBSTRATE_DIGEST_HASHES` between runs (that would hide the replay); the test must demonstrate the SAME digest hash passing the guard twice

**Spec 5: Test-Fixture Bypass Authority (NODE_ENV=test Leak)** ✓ [Three sub-tests]

**5A: Bypass works as designed for unit fixtures**
- **File:** `core/orchestration/src/handlers/lev-wizard-ratchet.test.ts`
- **Test name:** `'test_fixture_only authority allows forged digests in NODE_ENV=test'`
- **Setup:** Set `NODE_ENV='test'`, call `runLevWizardRatchetCouncil()` with `engineSubstrateAuthority: 'test_fixture_only'` and a forged digest
- **Expected result:** `engineSubstrateValidation.ok === true` (bypass applies)
- **Purpose:** Document that the bypass exists and works as designed for legitimate unit fixtures (line 1323)

**5B: Bypass blocked when NODE_ENV !== 'test'**
- **File:** `core/orchestration/src/handlers/lev-wizard-ratchet.test.ts`
- **Test name:** `'test_fixture_only authority is ignored when NODE_ENV !== test'`
- **Setup:** Set `NODE_ENV='production'` (or undefined), call with `engineSubstrateAuthority: 'test_fixture_only'` and forged digest
- **Expected result:** `engineSubstrateValidation.ok === false`, findings include standard "caller-provided digest is projection-only" message
- **Assertion:** The flag has no effect outside test environments; non-test runtimes cannot use the bypass

**5C: Authority parameter confined to test code only (codebase assertion)**
- **File:** `core/orchestration/src/handlers/lev-wizard-ratchet.test.ts`
- **Test name:** `'engineSubstrateAuthority parameter not exposed in production handler entry point'`
- **Assertion:** The `engineSubstrateAuthority` parameter appears ONLY in test code (`lev-wizard-ratchet.test.ts` and the exported `runLevWizardRatchetCouncil()` function), never in the production handler (`handler.ts` CLI entry point or any public orchestration API)
- **Verification:** `grep engineSubstrateAuthority src/handlers/` should show ONLY test-scoped usage

---

## Implementation Notes

- **All tests go in:** `core/orchestration/src/handlers/lev-wizard-ratchet.test.ts` (existing test file for the handler)
- **Code under test:**
  - Function `validateEngineSubstrateDigestEvidence()` (line 1302–1334)
  - Set tracking `HOST_BUILT_ENGINE_SUBSTRATE_DIGEST_HASHES` (line 133–142 in `real-three-engine-envelope.ts`)
  - Schema validation `validateLevEngineSubstrateDigest()` (line 814–877 in `projection-binding.ts`)
- **Test fixtures already available:** `createDefaultLevWizardRatchetInput()`, `sha256Json()`, `sha256Text()`, `withIsolatedLevRuntime()`
- **CI/CD:** These tests should be added to the lev repo's GitHub Actions (or equivalent). Current memory notes indicate no `.github/workflows/*.yml` runs the orchestration proof/handler suite — adding these would close that gap.

The full specifications document (with complete TypeScript examples, all edge cases, and detailed pass-by-construction risk breakdowns) has been written to `/private/tmp/claude-501/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/70353e22-32b4-4b19-8f33-1eb6fad3858b/scratchpad/trust_spine_redteam_test_specs.md`.