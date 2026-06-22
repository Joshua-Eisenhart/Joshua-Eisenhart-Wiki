---
title: "Independent Audit — ClaimGate Wave-Admission (v56 merged / v56 strict / v57)"
status: independent_audit_verified_local
date: 2026-06-22
auditor: claude (external pass, not the cut author)
scope: packages/claimgate-wave-runtime across the three uploaded cuts
relation: external counterpart to the in-package AUDIT_*.md self-audits (those are self-graded; this is not)
claim_ceiling: "local-rerun evidence on the uploaded zips only — not a production, host, eval, or canon claim"
---

# Independent Audit — ClaimGate Wave-Admission (v56 ×2, v57)

This is an **external** audit. Each uploaded cut ships its own `AUDIT_*.md`
(`AUDIT_V56_MERGED_WAVEGRAPH_ADMISSION.md`, `AUDIT_V56_STRICT_PROVENANCE_ADMISSION.md`,
`AUDIT_CODEX_V57_CLAUDE_DELTA_WAVE_ADMISSION.md`). Those are the authors grading their
own diffs. This document is the independent pass and is kept outside the package on purpose.

Status ladder used here: `exists < runs < passes local rerun < canonical by process`.
Nothing below is asserted above `passes local rerun`.

## Cuts audited

| Cut | Version | Entries (internal/actual) | doctor |
|---|---|---|---|
| v56 merged wavegraph | `1.50.0-v56-merged-wavegraph-admission` | 478 / 478 | ok |
| v56 strict provenance | `1.50.0-v56-strict-provenance-admission` | 480 / 480 | ok |
| v57 codex+claude delta | `1.51.0-codex-v57-claude-delta-wave-admission` | 482 / 482 | ok |

Entry counts are honest (internal == actual); no packaging lie of the v40 era. The entire
v56→v57 thread is concentrated in one package, `claimgate-wave-runtime`; the two v56 cuts and
v57 differ **only** in that package's `src/index.js` and its test file.

## Verdict

Mostly disciplined, genuinely-gated work. `promotion_allowed: false` is hardwired and holds; the
real deterministic ClaimGate-core gate is in the admission path and fails closed; the test suite
is fail-closed, not happy-path. **Two theater spots were found — one on each side — both honestly
disclaimed but dressed beyond what they prove.** Neither is a promotion bypass or fraud. One of the
two (the Codex side) is a real forgeability gap and has been closed with a verified patch (see below).

## What is real (not theater)

- **Wave admission delegates to the real gate and fails closed.** `requestWaveAdmission`
  (`src/index.js:947`) calls `core.runVerification(...)` — the same deterministic gate used
  elsewhere — and sets `wave_can_promote: false`, `promotion_authority: 'claimgate-core'`.
  Probes: unclean loop → `admitted=false, core_status=not_run, ["wave_loop_not_clean"]`;
  clean loop + empty evidence → the real gate runs and returns `rework_required` → `admitted=false`.
- **`promotion_allowed: false` is genuinely hardwired** on every wave object, with explicit
  `blocked_consumers: [canon_promotion, lev_host_admission_claim, production_connector_claim]`.
  The wave cannot self-promote.
- **Tests are fail-closed** (122 wave assertions; e.g. "requires_read waves must fail closed
  without bound reads", "claimed-read-without-file must be blocked", "hash-mismatched content
  must be blocked"). Read-gates, evidence binding, and the source-side signature forgery test
  (attacker-key manifest → blocked) are real.
- **Signed source manifests are cryptographically real** (ECDSA via `manifest-gate`); an
  `attacker-key`-signed source entry is correctly rejected (`tests/wave-runtime-tests.js:460`).

## Theater #1 — the "self-verifying loop" is a scripted fixture (Claude delta)

`docs/150_WAVE_RUNTIME_RECEIPT_BOUNDARY_LOOP.md` sells the loop as
*"pass 1 check 100, reject 12 → pass 2 reject 3 → pass 3 reject 0."* That convergence is
**hardcoded**. `makeRows` (`src/index.js:596`) contains `badPass1` (a fixed set of 12 item IDs),
`badPass2` (3 IDs), pass-3 empty — and fabricates each row's data (`value: 99`, empty `revenue`,
mismatched hash) so the checklist rejects exactly those predetermined items. The loop *structure*
is real (real `gateWaveRun` per wave, real `wizard.runVerificationChecklist`, real requeue
carry-forward via `currentItems`), but it replays a script on rigged data, and the test asserts
`rejected === 12`, locking the fixture in. It is labeled "fixture" in the doc's honest ceiling,
but presented as an emergent verification result.

- **Status:** honest-but-staged. The structure passes local rerun; the convergence narrative is
  not emergent.
- **Recommendation:** rename/reframe the demo as a scripted fixture, or drive it from injected
  data so the reject counts are genuinely a function of input rather than baked into `makeRows`.

## Theater #2 — "strict provenance admission" accepted a forged, unsigned host receipt (Codex)

`gateStrictProvenanceAdmission` + `validateHostAdmissionReceipt` (Codex's v56-strict functions)
reuse v41's **real ECDSA signing for the source manifest** — but the `HostAdmissionReceipt` (the
object representing "the host admitted this") was a **plain unsigned object**. Verified forge,
on the unpatched v57:

```
{kind:'HostAdmissionReceipt', status:'admitted', host_id:'TOTALLY-FAKE-HOST',
 strict_provenance_gate_hash:<publicly computable sha256 of public wave fields>,
 effect_receipt_ref:'forged', eval_receipt_ref:'forged',
 connector_custody:{protection_level:'production'}}
   → validateHostAdmissionReceipt → status: PASSED, warnings: [], reasons: []
```

No key, no signature, fake host. Labeling `protection_level: 'production'` even suppressed the
`fixture_host_admission_not_production` warning (it fired only on `/^fixture/`). The gate hash is
`sha256` over public wave fields, so anyone can compute it. So after the v39→v41 arc made authority
cryptographically real, "strict provenance admission" introduced a **new unsigned, forgeable
host-authority surface** — strict on the source, theatrical on the host.

**Mitigation that limited the blast radius:** `promotion_allowed: false` is hardwired everywhere,
so a forged receipt could not actually *promote* — it only yielded a clean `passed` /
`host_admission_recorded` verdict a downstream consumer could misread as host admission.

### Fix (verified, shipped as a patch for the next cut)

The host receipt is brought to **parity with signed sources**:

- `validateHostAdmissionReceipt(receipt, expectedGateHash, trustRoot)` now requires a real
  signature (`receipt.signature.signature_b64`, rejected if missing or `fixture:`-prefixed),
  looks the `key_id` up in the trust root, and verifies an ECDSA signature over the receipt's
  authority fields **bound to the exact local gate hash**. New reason codes:
  `host_admission_signature_not_real`, `host_admission_untrusted_key`,
  `host_admission_signature_invalid`.
- The fixture/production distinction is now driven by the **verified signing key's**
  `protection_level` (unforgeable), not a self-declared receipt string.
- `manifest-gate` exports its existing `signString` / `verifySignature` primitives (reused, no new
  crypto). A `signHostAdmissionReceipt(...)` helper mints valid receipts.
- Two regression tests added: the exact unsigned forge → `host_admission_signature_not_real`
  (blocked); an attacker-key-signed receipt → `host_admission_untrusted_key` (blocked).

Verification (local rerun on the patched v57):

```
forged unsigned production receipt -> status: blocked | reasons: ["host_admission_signature_not_real"]
real signed fixture receipt        -> status: passed  | warnings: ["fixture_host_admission_not_production"]
npm test exit=0 (full suite green, incl. the 2 new regression tests) | doctor ok:true
```

Patch: `claude-delta-v58-host-admission-signature.patch` (3 files, +134/-25, applies clean to v57).

## Lesser findings

- **Self-grading "audits."** The in-package `AUDIT_*.md` files are authored by the cut authors.
  The v57 audit's framing ("Claude version numbers are not Codex version numbers… local tests are
  the authority") is a credit/authority framing, not a technical finding. Recommend not shipping
  self-authored `AUDIT_*.md` as if independent — this external doc is the counterpart.
- **Stale version label.** `docs/150_...` is titled "v51 Wave Runtime" but ships in the v56/v57
  package.
- **Noncommutativity / basin classifier** are real but hand-built precedence models (gate-before-
  source blocks by construction), not discovered properties. Fine as models; the framing implies
  more.

## Audit ceiling

Evidence here is `passes local rerun` on the three uploaded zips only. It is not a claim that
production Leviathan host/eval admitted any artifact, that real connector custody is active, or
that any wave can promote to canon. The fix raises the host-admission floor to signed-source
parity; it does not make the fixture host receipt a production admission.
