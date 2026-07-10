# Wizard Model-Lane Runtime Audit - 2026-07-09

## Verdict

Lev can now call real NVIDIA, xAI, Gemini, and Claude Bridge model lanes and
retain receipt-bound output text. That runtime is useful only when the prompt
is bound to evidence and completeness is mechanically gated.

The first broad live run exposed a real failure mode: the default prompt was a
redacted fixture. GLM, MiniMax, Grok, and Gemini invented internal probe state,
latency, or Spinor drift they had not observed. Qwen refused the fiction. Those
responses are provider-runtime receipts, not useful system audits.

The runtime was then hardened to:

- allowlist exact lane IDs without deleting the full provider roster;
- hash the effective prompt rather than retain a static placeholder hash;
- preserve provider-reported model identity, output, elapsed time, receipt
  reference, and reported cost when a provider supplies cost;
- load an evidence packet from a named file;
- require five declared sections plus `END_OF_AUDIT` before success;
- fail closed on timeout, model mismatch, missing final content, truncation,
  schema failure, budget overrun, or provider error.

## Final Evidence-Bound Grok Run

The final bounded lane used only `xai-outside-critique`.

- Requested model: `grok-4.5`.
- Provider-reported model: `grok-4.5`.
- Effective prompt SHA-256:
  `8515547b0e4f3c2b84d0a10b1f58827e72ebb62590459477bf7c2d81266481b8`.
- Evidence packet SHA-256:
  `057438dacc5145368afcda78dffc7391308c5ce58fd4c9e61990445f193472ae`.
- Output SHA-256:
  `fe1d0737795ec5d8394065ed9c55334a31e553561a7d7e3fa7e2cf4c21bcc269`.
- Elapsed time: `36,096 ms`.
- Required sections: all present.
- End marker: present.
- Graph mutation: false.
- Result artifact SHA-256:
  `054d013a492144c9c0de478c87982ffe691d87369a3e767ef84717ab6ef9dac4`.

Durable result:
`/Users/joshuaeisenhart/GitHub/lev/.lev/pm/audits/model-lanes/lev-wizard-ratchet-dual-ratchet-grok45-v6-20260709.json`.

The advisory conclusion agrees with the local Ratchet gate: Type 1 is stable
under the declared finite sweep; Type 2 is underdetermined; four phases are
implemented and load-bearing but not forced; J3(O) exact parity does not supply
entropy/DPI; Axis0, entropy-gradient, perception, and object claims remain
blocked.

## Other Provider Lanes

The evidence-bound multi-provider run preserved rather than hid failures:

- NVIDIA GLM reported `z-ai/glm-5.2` and produced a grounded but truncated
  answer in one run, then timed out at 120 seconds in the larger run.
- NVIDIA Qwen reported `qwen/qwen3.5-122b-a10b`; the larger run returned no
  final answer body and failed schema.
- NVIDIA MiniMax succeeded on the short fixture but timed out on the evidence
  packet.
- Gemini reported `gemini-3.1-pro-preview` but truncated after the first
  section and failed schema.
- Kimi's NVIDIA endpoint returned HTTP 404 in the broad run and was not aliased
  to another model.
- Hermes MoA remains unavailable because the configured reference provider
  returned 401; no Codex-local substitution is allowed.

NVIDIA/xAI/Gemini responses did not report dollar cost, so their declared lane
budgets are not dollar-enforced by these receipts. The runtime records cost as
unknown rather than zero evidence.

## Fable High

A separate Claude Bridge advisory audit is durable in the Ratchet packet:

- actual model: `claude-fable-5`;
- effort: High;
- duration: `122.85 s`;
- reported cost: `$2.479553`;
- output SHA-256:
  `6b72895ad179bd53942d2a0b0c9a3d36492ea03f59a110cd8beb3f1495426ef9`;
- receipt SHA-256:
  `bea335d348319cbf32a9a03a3f463635c3d12001c5ace64850125ac6e59640cd`.

Fable independently rejected UP-130, retained the bounded Type-1 result, and
kept Type 2 underdetermined. It remains advisory, not proof.

## Lev Runtime Ceiling

The model calls are real. The overall Lev Wizard result remains blocked and
keeps `fixture_or_dry_run_until_live_model_and_engine_receipts` because:

- the native three-engine carrier is still the finite R0 probe quotient, not
  the source-faithful QIT 64-stage engine;
- ClaimGate steering recomputes failure and withholds the Spinor cell;
- model outputs are advisory and cannot mutate graph state;
- a model agreement is not a scientific gate.

`lev timetravel` is also currently registered but broken in this checkout: its
wrapper imports a missing `plugins/core-timetravel` implementation. External
research therefore used primary sources directly and records that executor
defect rather than claiming Lev research ran.

## Routes

- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
- [[projects/codex-ratchet/repository-research-and-tool-validation-2026-07-09]]
- [[projects/leviathan-current/qit-evidence-boundary-refresh-2026-07-09]]
