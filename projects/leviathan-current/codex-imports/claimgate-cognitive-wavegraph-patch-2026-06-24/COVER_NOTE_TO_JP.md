# Cover Note To JP

This is a review packet for the ClaimGate cognitive wavegraph patch candidate.

The patch is intentionally framed as a Lev-native proposal path, not a second
proof system. It adds a fixture-level executable slice for nested waves,
councils, skill/MMM/source-loaded members, management sidecars, deterministic
ClaimGate loops, model-lane formation, runtime outcome normalization, and host
ClaimGate steering projection.

The newest delta is the Gate 0A provider-runner factory layer:

- model lane manifests require Claude Bridge, OpenRouter Chinese-family checks,
  xAI/Grok, Google Gemini TUI, and Codex/local lanes;
- injected provider runner factories cover Claude Bridge, OpenRouter Chinese-family, xAI/Grok, Google Gemini TUI, and Codex/local routes;
- runner outputs normalize success, timeout, schema-invalid,
  provider-error, blocked, and unavailable outcomes into runtime receipts;
- every lane remains advisory-only and every failed lane becomes a typed
  FailurePacket rather than disappearing into aggregate model prose.

Claim ceiling: local fixture/proof slice with injected runner factories. This does
not prove live provider auth/tool/network success, full skill/MMM/source loading, full wave
scheduler integration, or production host admission.

Suggested review order:

1. `core/orchestration/src/proof/claim-gate-wavegraph-slice.ts`
2. `core/orchestration/src/proof/claim-gate-model-lane-runners.ts`
3. `core/orchestration/src/proof/claim-gate-model-lane-runners.test.ts`
4. `core/orchestration/src/proof/claim-gate-wavegraph-slice.test.ts`
5. `core/orchestration/src/proof/claim-gate-loop.ts`
6. `core/orchestration/src/proof/claim-gate-steering-run.ts`
7. `.lev/pm/plans/plan-claimgate-gate-ratchet-wavegraph.md`
