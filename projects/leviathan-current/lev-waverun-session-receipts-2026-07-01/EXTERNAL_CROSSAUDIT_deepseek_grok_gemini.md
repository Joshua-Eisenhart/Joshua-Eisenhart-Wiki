# External cross-audit (deepseek/grok/gemini) — nonce is top risk

All three models responded successfully.

## External cross-audit results

**DeepSeek (OpenRouter, deepseek/deepseek-chat-v3):** Single biggest risk is the `test_fixture_only` escape hatch — convention-gating via `NODE_ENV=test` is fragile against misconfiguration or human error. Opt-in preflight CI is insufficient alone (opt-in risks neglect; stubs may keep dominating in practice). Wants mandatory CI on critical paths, removal or hardening of the fixture escape hatch, and a nonce on digests.

**Grok (xAI, grok-4.3):** Single biggest risk is the no-nonce same-process replay — it makes the in-process `Set` check "trivially satisfiable" without any real engine ever running. Opt-in preflight CI is explicitly "No — not enough": coverage stays voluntary and build-time-only; post-merge or supply-chain changes can reintroduce stubs. Wants mandatory signed attestation or a nonce/timestamp embedded in every digest.

**Gemini (2.5-flash):** Single biggest omission is the missing nonce, calling the in-process `Set` "a potentially reusable bypass for malicious actors co-located in the process." Explicitly answers "No, opt-in preflight-gated CI is not sufficient" — it doesn't touch the replay gap or the `NODE_ENV=test` escape hatch. Wants nonce-based digests per operation plus hardened test-environment overrides.

**Verdict split:** 2 of 3 (Grok, Gemini) name the missing nonce as the single most important gap; DeepSeek names the `test_fixture_only` hatch as most important but flags the nonce too. All three converge: opt-in preflight CI alone is not sufficient — unanimous "no."

## Synthesis — what the externals add beyond internal framing

1. **"Opt-in" itself is the second-order risk, not just the digest gap.** All three treat opt-in as a compliance/coverage problem, not just a technical one — voluntary CI participation degrades over time (neglect, supply-chain drift, stubs re-dominating) independent of whatever the CI job checks once it runs. The internal framing treats opt-in CI as *the fix*; the externals treat it as *itself under-specified* and wanting a mandatory-path complement.

2. **Attestation/signing as a stronger alternative than a nonce alone.** Grok specifically proposes "mandatory signed attestation" as an option alongside (not just) a nonce — pointing at cryptographic binding of the digest to the actual engine invocation, not just replay-prevention. That is a materially stronger mechanism than nonce-only and wasn't in the internal framing as stated.

3. **Unanimous rejection of "sufficient."** None of the three hedge — all three give a direct "no" to whether opt-in preflight-gated CI is an adequate authenticity backstop on its own, which is a firmer verdict than the internal framing (which posed it as an open question) had settled on.