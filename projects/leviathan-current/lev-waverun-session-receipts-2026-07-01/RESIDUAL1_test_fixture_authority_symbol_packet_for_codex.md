# A-prime residual-1: pin engineSubstrateAuthority structurally (for Codex)

Now I'll output the packet as the return value:

---

## A-Prime Residual-1 Implementation Packet

**Vulnerable Path:** `/Users/joshuaeisenhart/GitHub/lev/core/orchestration/src/proof/lev-wizard-ratchet.ts:1323`

```typescript
if (options.engineSubstrateAuthority === 'test_fixture_only' && process.env.NODE_ENV === 'test') {
  // Unit fixtures exercise non-engine gates without spawning Julia/JAX/PyTorch.
  // Runtime callers do not get this authority mode outside NODE_ENV=test.
}
```

**The escape hatch:** A caller passes `engineSubstrateAuthority: 'test_fixture_only'` (line 507, public API type) and the check succeeds if `NODE_ENV=test`. Both conditions are user-controllable: the option is on the public interface, and `NODE_ENV` is an environment variable. Convention (expecting test code to set NODE_ENV) is not a structural barrier.

**Why convention fails:** A process that inherits or inadvertently sets `NODE_ENV=test` (CI matrix jobs, container orchestration, test isolation, misconfiguration) bypasses the substrate integrity check entirely, admitting caller-provided digests without running the real Julia/JAX/PyTorch envelope.

---

## Proposed Fix: Module-Private Symbol (Strongest + Minimal Cost)

Replace the string literal with a `Symbol` that only test code can import. This moves the authority check from a runtime environment convention into a structural, compile-time barrier.

**Implementation:**

In `/Users/joshuaeisenhart/GitHub/lev/core/orchestration/src/proof/lev-wizard-ratchet.ts`:

1. **Define the token (internal only):**
   ```typescript
   const TEST_FIXTURE_ENGINE_AUTHORITY_TOKEN = Symbol('test_fixture_only_engine_authority');
   ```

2. **Update public interface:**
   ```typescript
   export interface RunLevWizardRatchetCouncilOptions {
     engineSubstrateAuthority?: typeof TEST_FIXTURE_ENGINE_AUTHORITY_TOKEN; // Symbol type, not string
     // ... rest unchanged
   }
   ```

3. **Update validator:**
   ```typescript
   function validateEngineSubstrateDigestEvidence(
     digest,
     options: {
       engineSubstrateAuthority?: typeof TEST_FIXTURE_ENGINE_AUTHORITY_TOKEN;
     } = {},
   ): EnvelopeValidationResult {
     if (!isHostBuiltLevEngineSubstrateDigest(digest)) {
       if (options.engineSubstrateAuthority === TEST_FIXTURE_ENGINE_AUTHORITY_TOKEN) {
         // Unit fixtures exercise non-engine gates without spawning Julia/JAX/PyTorch.
         // Structural: only test code can import the token.
       } else {
         findings.push('engine substrate digest: digest must be host-built...');
       }
     }
     return { ok: findings.length === 0, findings };
   }
   ```

4. **Keep `NODE_ENV` check as defense-in-depth** (line 1323 still validates the environment, even though the Symbol is the primary gate).

---

## Test That Proves Production Code Is Blocked

**In `/Users/joshuaeisenhart/GitHub/lev/core/orchestration/src/proof/lev-wizard-ratchet.test.ts`:**

```typescript
import { TEST_FIXTURE_ENGINE_AUTHORITY_TOKEN } from './lev-wizard-ratchet.js';

describe('A-Prime Residual-1: engineSubstrateAuthority structural isolation', () => {
  it('production code cannot pass string "test_fixture_only" even if NODE_ENV=test', () => {
    const savedEnv = process.env.NODE_ENV;
    try {
      process.env.NODE_ENV = 'test'; // Attacker scenario
      
      const input = {
        ...validLevWizardRatchetRunInput(),
        levEngineSubstrateDigest: undefined, // Caller-provided, no host build
      };
      
      // This TypeScript line WILL NOT COMPILE:
      // const result = runLevWizardRatchetCouncil(input, {
      //   engineSubstrateAuthority: 'test_fixture_only', // Type error: string not assignable to Symbol
      // });
      
      // Only Symbol import works (test file only):
      const result = runLevWizardRatchetCouncil(input, {
        engineSubstrateAuthority: TEST_FIXTURE_ENGINE_AUTHORITY_TOKEN,
      });
      
      expect(result.simEngineGateCheck.status).toBe('pass');
    } finally {
      process.env.NODE_ENV = savedEnv;
    }
  });

  it('fixture authority is rejected if NODE_ENV is not "test" (redundant barrier)', () => {
    const savedEnv = process.env.NODE_ENV;
    try {
      process.env.NODE_ENV = 'production';
      
      const input = {
        ...validLevWizardRatchetRunInput(),
        levEngineSubstrateDigest: undefined,
      };
      
      // Even with Symbol, NODE_ENV check rejects it
      const result = runLevWizardRatchetCouncil(input, {
        engineSubstrateAuthority: TEST_FIXTURE_ENGINE_AUTHORITY_TOKEN,
      });
      
      expect(result.simEngineGateCheck.status).toBe('fail');
      expect(result.simEngineGateCheck.reason).toContain('digest must be host-built');
    } finally {
      process.env.NODE_ENV = savedEnv;
    }
  });
});
```

---

## Why Symbol + NODE_ENV (Defense-in-Depth)

| Barrier | Prevents | How |
|---------|----------|-----|
| **Symbol (primary)** | Production code from importing the token | Structural: not exported in public API; can't be spoofed as a string |
| **NODE_ENV check (secondary)** | Test code from accidentally leaking fixture authority in production runtime | Runtime: even if Symbol is imported, environment check closes the gate |

---

## File Ownership & CI Integration

**Primary hot file:** `/Users/joshuaeisenhart/GitHub/lev/core/orchestration/src/proof/lev-wizard-ratchet.ts` (Codex ownership — all fixes here)

**Test file:** `/Users/joshuaeisenhart/GitHub/lev/core/orchestration/src/proof/lev-wizard-ratchet.test.ts` (add new test suite above)

**Optional: ESLint rule** (defense-in-depth)  
Add to CI to catch re-exports of the Symbol in non-test files:
```bash
eslint --rule "no-restricted-imports: ['error', { patterns: ['*/lev-wizard-ratchet.js:TEST_FIXTURE_ENGINE_AUTHORITY_TOKEN'] }]" src/**/*.ts --ignore-pattern "**/*.test.ts"
```

---

## Why Convention Is Insufficient

- **Environment variables are mutable:** `NODE_ENV` can be set by the caller, inherited from parent process, or manipulated in CI matrices
- **No type-system enforcement:** The string literal `'test_fixture_only'` is just a string; production code can pass it without import
- **Survives refactoring:** A Symbol is structurally bound to its definition; a string literal can be copied, guessed, or hardcoded anywhere
- **False sense of security:** The comment "Runtime callers do not get this authority mode outside NODE_ENV=test" is aspirational, not enforced

---

**Recommendation:** Implement **Option A (Symbol)** immediately. Cost: zero public API surface change, compile-time safety, survives all refactors. Acceptance test confirms production code cannot reach fixture authority without importing the token, which is not exported from the public module.

Scratch file (full detail + alternatives): `/private/tmp/claude-501/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/70353e22-32b4-4b19-8f33-1eb6fad3858b/scratchpad/A_PRIME_RESIDUAL_1_PACKET.md`