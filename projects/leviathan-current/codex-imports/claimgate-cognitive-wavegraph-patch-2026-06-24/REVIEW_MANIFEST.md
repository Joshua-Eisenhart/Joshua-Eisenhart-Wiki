# Review Manifest

## Claim Ceiling

`local_fixture_proof_slice_with_injected_provider_runner_factories_not_live_provider_auth_not_lev_canon`

## Included Surface

- ClaimGate deterministic loop contracts and receipts.
- ClaimGate steering host-consumption hardening.
- Cognitive wavegraph executable slice.
- Gate 0A model-lane formation and runtime outcome normalization.
- Injected provider runner seam plus named factories for Claude Bridge, OpenRouter
  Chinese-family lanes, xAI/Grok, Google Gemini TUI, Codex, and local providers.
- Handler and test wiring for orchestration proof surfaces.
- PM plan/report/handoff artifacts that explain the patch boundary.

## Model-Lane Requirement

A model-diversity claim is valid only when Gate 0A carries per-lane receipts for:

- at least three Claude Bridge lanes;
- OpenRouter Chinese-family lanes for DeepSeek, GLM, Kimi, MiniMax, and Qwen;
- xAI/Grok;
- Google Gemini TUI or unavailable receipt;
- Codex/local.

Model agreement remains advisory. Convergence is not proof.

## New Runner Contract

`runClaimGateModelLaneRuntimeRunners` accepts provider-keyed injected runners and
normalizes their output into `ClaimGateModelLaneRuntimeOutcome`. It records:

- success;
- timeout;
- schema-invalid output;
- provider error;
- blocked lane;
- unavailable lane.

The deterministic proof core does not perform live provider auth, network, or CLI work.
Live transport bindings are the next patch.

## Review Risks

- Patch is still fixture-level, not production runtime.
- Context loading is compiler-minted from fixture content, not installed skill
  resolution.
- Provider-runner factories are tested with injected process/HTTP dependencies, not live provider credentials or real CLI/API calls.
- The patch is large because it preserves PM docs and tests in the send packet.
- Older ClaimGate ZIPs and screenshots remain provenance only.
