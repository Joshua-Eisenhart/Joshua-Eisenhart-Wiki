---
title: Sim-runner Claude correction prompt
created: 2026-06-30
type: sendable-correction-prompt
status: current
claim_ceiling: Hermes checked current Lev source snippets/process state; this prompt corrects routing and seam framing, not admission.
---

# Sim-runner Claude correction prompt — 2026-06-30

Paste this to the sim-runner Claude thread.

```text
You are partly right but off in the important way.

Correct:
- Do not edit Codex's live `/Users/joshuaeisenhart/GitHub/lev` working tree while Codex owns it.
- `rerun_commands` `/etc/hosts` path ownership bug is real.
- Forbidden authority value normalization exists; the remaining bypass is key normalization / suspicious-key rejection.

Incorrect / misframed:
- Do not say Hermes claimed the ClaimGate host witness has no MAC. The current blocker is not the steering host witness MAC. The host witness MAC exists and blocks cross-process witness replay.
- The open A22c-family issue is host-trusted evidence/root authority: same-process issuer + caller-settable root / public issuer path, not raw no-MAC witness replay.
- Do not defer the verified-blocker wave until some unrelated corpus proposal wave finishes. If you cannot edit the live tree, you can still run the read-only verifier/spec wave now, or work in a separate worktree if explicitly authorized.

Your next useful job is a verified blocker/fix-spec wave, not another stall.

Run these as read-only lanes immediately, with receipts under:
`/tmp/claude-burn-2026-06-29/lev-sim-runner-spec/<lane-id>.md`

Lanes:
1. `a22c-host-trust-root-spec`
   - Separate three surfaces:
     a. ClaimGate steering host witness MAC: already present; do not relitigate.
     b. Host-trusted evidence refs in `handlers/claim-gate-loop.ts`: MAC entries exist, but root/issuer authority may remain forgeable through same-process issue + caller-settable root.
     c. Graph-event trust A23b: Codex reports closed; verify current code/tests, but do not treat it as the same as A22c.
   - Output exact current status and minimal fix spec.

2. `rerun-commands-path-spec`
   - Verify `hostCheckoutPathExists` and `/etc/hosts` behavior.
   - Specify minimal ownership/hash-binding fix and regression test.

3. `forbidden-key-normalization-spec`
   - Verify value normalization exists in `isTruthyAuthorityValue`.
   - Verify key matching remains exact `Set.has(key)`.
   - Specify key normalization or suspicious-key rejection tests for case/space/zero-width/homoglyph variants.

4. `evidence-manifest-host-context-spec`
   - Determine whether `sourceBoundEvidenceContext` is host-issued or producer-derived in the current Wizard path.
   - Specify host-attested context fix.

5. `seed-integrity-replay-spec`
   - Determine whether `nextRunSeed` and seed replay ledger are host-anchored or document/env-root anchored.
   - Specify HMAC/ledger-root fix.

6. `wizard-host-consumed-path-spec`
   - Verify whether custom `wizard_*` obligations have real host internal verifiers, or whether Wizard still cannot reach `host_consumed` through the real path.
   - Specify Option A/Option B implementation path.

Rules:
- Read-only in the live Lev tree unless owner explicitly authorizes a separate worktree.
- Do not ask whether to do the verifier wave; do it.
- Do not wait on unrelated corpus work.
- Each receipt must say: observed / inferred / open, file:line anchors, exact test to add, exact implementation file(s), and whether Codex should patch it in the live tree.

If you want to implement rather than just spec, ask for explicit authorization to create a separate worktree. Otherwise stay read-only and produce the full spec packet now.
```
