---
title: Codex Red-Team Targets — Lev ClaimGate 3-Root Fix
created: 2026-06-28
updated: 2026-06-28
type: codex-build-packet
status: actionable-target-packet
claim_ceiling: Claude/Codex target handoff copied from volatile scratch plus Hermes file verification; not implementation proof; not regression rerun after fix
source_claude_memory: /Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/project_lev_spine_forgery_redteam_3roots.md
source_claude_memory_sha256: bf03be717fd16173126f45a20810b63164bbf0731b1f1db89763021a9a9f4af9
source_volatile_packet: /private/tmp/claude-501/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/623c64fd-11b7-4916-b915-b9f62696575b/scratchpad/codex_redteam_targets.md
source_volatile_packet_sha256: 5b631d51a7c033975b04772797c4da29132da240c4524909ec0fe6e17c8783c0
related:
  - projects/leviathan-current/lev-claimgate-digging-status-2026-06-28
  - projects/leviathan-current/lev-claimgate-ratchet-memory-harness-plan-2026-06-25
---

# Codex Red-Team Targets — Lev ClaimGate 3-Root Fix

## Purpose

Preserve the volatile Claude scratchpad target packet as a durable wiki handoff for Codex.

This is the build target list for turning the red-team swarm into regression tests and root fixes. It is not proof that the fixes landed.

## Source verification

Hermes read both source files from disk before copying this packet:

- Claude project memory note: `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/project_lev_spine_forgery_redteam_3roots.md`
  - lines: `27`
  - sha256: `bf03be717fd16173126f45a20810b63164bbf0731b1f1db89763021a9a9f4af9`
- Claude volatile scratch packet: `/private/tmp/claude-501/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/623c64fd-11b7-4916-b915-b9f62696575b/scratchpad/codex_redteam_targets.md`
  - lines: `44`
  - sha256: `5b631d51a7c033975b04772797c4da29132da240c4524909ec0fe6e17c8783c0`

Support level: file-read and checksum verified. The attack results remain reported by the red-team swarm unless independently rerun in the Lev tree.

## Codex red-team targets — 3-root fix + 16 regression tests

Source: red-team swarm `we1z95nfh`, 16/24 attacks broke through, all reported RUN + source-confirmed. Fix is 3 roots, not 16 patches. Each attack below becomes a regression test that must fail, meaning it must be rejected, after the root fix.

Priority order:

1. Root 1 — gates falsely pass.
2. Root 2 — route/carrier laundering.
3. Root 3 — replay/freshness.

## Root 1 — boundary gates trust caller-supplied tokens, ok-flags, or projections

Fix: at every boundary the host recomputes the verdict and issues the trust token plus execution witness. This must be non-bypassable. It must not be flag-gated like `consume --real-engines`. Producer-supplied tokens, flags, and projections are never authority.

| id | attack | cite | must fail after fix |
|---|---|---|---|
| A22 | producer-named `--host-trusted-evidence-ref` confers trust | `claim-gate-loop.ts:1542-1543` | ref with no host issuance → not trusted; gate rejects |
| A23 | forged applyPlan + caller trusted-ref → `graphMutationApplied:true` | `recordClaimGateGraphPatchExecution` | no real host apply → `graphMutationApplied` stays false |
| A2 | forged receipt passes when `allowEmbeddedNegativeControl:true` | `mechanical-probe-runner.ts:479-481` | canonical Julia lane must keep the execution defence on |
| A3 | forged digest in `boundary.json` → consume `host_consumed` | `claim-gate-steering-run.ts:619-620` | consume host-rebuilds/validates digest unconditionally |
| A12 | consume passes on hand-written `passed` statuses | same | host re-executes obligations, not re-folds |
| A14 | mutually agreeing forged eval-output + proof-spec | same | source provenance required, not just `projected == recomputed` |
| A15 | forged `falsifierStatus:closed` for an open claim | `lev-wizard-ratchet.ts:196-197` | falsifier from host engine, not hardcoded/producer field |
| A20 | forged `objectRef` passes `object_binding` | `claim-gate-loop` object binding | host-attestation anchor, not string equality |
| A24 | injected skill `ok` flag, never executed | `proof/lev-wizard-ratchet.ts:708` | re-invoke `validateFormalSkillSet` / `SourcePack` |
| A16 | forged `nextRunSeed` passes seed integrity | `createSeededLevWizardRatchetInput` | external/host anchor, not intra-doc cross-ref |

## Root 2 — carrier guard is path-string-only

Fix: hash the carrier scripts, realpath canonicalize, case-fold where needed, and check content provenance. Do not rely on path substring blocklists.

| id | attack | cite | must fail after fix |
|---|---|---|---|
| A8 | macOS case-fold `/codex-ratchet/` | `real-three-engine-envelope.ts:33-47` | canonicalized case → rejected |
| A9 | CR `carrierPath` via non-blocklisted `pathSource` | `projection-binding.ts:611-615` | content of `carrierPath` inspected → rejected |
| A10 | CR scripts copied to a clean temp path | substring blocklist | script content hash → rejected as non-Lev |
| A11 | `file:` ref into `~/Codex-Ratchet` in skill source pack | `validateSkillSourcePack` | sourceRoot origin restriction → rejected |
| A19 | neutral-path stale carrier, env `pathSource` | guard env precedence | content anchor → rejected |

## Root 3 — no anti-replay / freshness

Fix: session/nonce binding plus seen-digest store. Receipts must be bound to the session that requested them.

| id | attack | cite | must fail after fix |
|---|---|---|---|
| A6 | replay captured digest/witness pair | no freshness in `core/graph/src` | stale/seen digest → rejected |
| A18 | replay old `nextRunSeed` into a new session | seed path | session binding → rejected |

## Held guards — do not regress

These internal re-checks held during the red team. Keep them green while fixing the boundary layer.

- A4 tampered invariant → caught by literal re-check on re-parsed stdout.
- A5 negative-control no-diff → caught by recomputed `outputDiffersFromPrimary`, `mechanical-probe-runner.ts:487`.
- A7 carrier symlink → caught by `realpathSync`.

The bug is boundary anchoring, not internal recomputation.

## Claim ceiling

This page preserves an actionable target packet. It does not prove Codex has implemented the fixes. The real verification loop is to rerun the exact 24 attacks after Codex lands the three-root fix and confirm:

- all 16 broke-through attacks now fail closed;
- the 3 held guards still hold;
- setup errors are marked `could-not-run`, not counted as held.
