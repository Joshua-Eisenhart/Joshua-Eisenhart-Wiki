---
title: Packet 4 Constraint Boundary Receipt — Josh Roots / Leviathan / Codex Ratchet
created: 2026-06-18
updated: 2026-06-18
type: processing-receipt
status: candidate/controller-verification-required
claim_ceiling: receipt and verification ledger only; not full provenance adjudication, not runtime test proof, not maintainer acceptance
---

# Packet 4 Constraint Boundary Receipt — 2026-06-18

## Task

Write the wiki-only Josh/root-constraint boundary pages for Leviathan without collapsing Leviathan into Codex Ratchet.

Hard scope followed:

- Wrote only under `/Users/joshuaeisenhart/wiki/projects/leviathan-current`.
- Did not edit `/Users/joshuaeisenhart/GitHub/leviathan`.
- Did not edit Codex Ratchet.
- Treated repo sources as read-only evidence.

## Files written

1. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/josh-root-constraints-in-leviathan.md`
2. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/lev-five-constraints-vs-f01-n01.md`
3. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/codex-ratchet-vs-leviathan-boundary.md`
4. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/packet-4-constraint-boundary-receipt-2026-06-18.md` (this file)

No other files were intentionally created or modified.

## Required project files read

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/read-first.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/README.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/bounded-ingestion-plan.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/provenance-ledger-josh-jp-pass-1-2026-06-18.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/packet-4-provenance-receipt-2026-06-18.md`
- `/Users/joshuaeisenhart/wiki/wizard/harness-consolidated/14_leviathan_os_constraint_map.md`

## Additional wiki files read

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/josh-contribution-signal-radar.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/josh-contribution-signal-index-2026-06-17.md` — attempted, but direct read exceeded safety character limit; prior radar/ledger and source files carried the needed evidence.
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/contract-surface-map.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/flowmind-control-plane.md`

## Leviathan repo sources read read-only

Primary current docs/specs:

- `/Users/joshuaeisenhart/GitHub/leviathan/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-flowmind.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-kernel.md`

FlowMind and ratchet design/provenance docs:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/design-flowmind.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-system.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/design/proposal-flowmind-ratchet.md`

Current FlowMind/kernel config and code:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/constraint-manifold.flow.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/system/ratchet-admission.flow.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/constraint-manifold.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/schemas/system-flowmind.schema.yaml`

Rust kernel sources:

- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/manifold.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/bridge.rs`

Searches/read-only source discovery:

- Searched `/Users/joshuaeisenhart/GitHub/leviathan` for `*constraint*` paths.
- Searched current repo content for `F01_FINITUDE`, `N01_NONCOMMUTATION`, `Constraint Manifold`, `Ratchet Admission`, `C1_finitude`, `C2_non_commutation`.
- Searched `core/flowmind` for ABAC/C3-C5 references; no concrete `abac-policy-engine.ts` file was found in that bounded search, though `constraint-manifold.ts` references it in comments.

## What was found

### 1. Explicit Josh contribution signal exists in current docs

`/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md:190-200` explicitly attributes to Josh the identification of two orthogonal constraint systems — ontological constraints (`ratchet`, `finitude`, `non-commutation`) and operational constraints (`ABAC`, `leases`, `containment`) — unified in a single declarative substrate.

This supports a Josh/root-constraint contribution claim at the conceptual/provenance layer. It does not prove current-code authorship.

### 2. Current FlowMind constraint surfaces support C1/F01 and C2/N01 as roots

Observed support:

- `core/flowmind/system/constraint-manifold.flow.yaml:36-59` declares C1 as `F01_FINITUDE` and C2 as `N01_NONCOMMUTATION`, both `tier: root_axiom`, `configurable: false`, `derivation: null`.
- `core/flowmind/src/kernel/constraint-manifold.ts:1-19` states the TypeScript validator enforces C1/C2 as the two irreducible root axioms and exports only `F01_FINITUDE | N01_NONCOMMUTATION` as `ConstraintId`.
- `core/flowmind/schemas/system-flowmind.schema.yaml:276-312` defines root axioms as irreducible, not configurable, FATAL, and not derived.

### 3. C3/C4/C5 are present but must stay governance/derived-aligned here

Observed support:

- `core/flowmind/system/constraint-manifold.flow.yaml:61-109` marks C3-C5 as `governance_assumptions`, `tier: governance`, `status: assumed`, and `configurable: true`, with derivation paths.
- `core/flowmind/schemas/system-flowmind.schema.yaml:313-357` defines governance assumptions as enforced but not yet proven from C1+C2 unless promoted to `derived_canon`.
- `docs/design/proposal-flowmind-system.md:113-115` says Josh's Thread B bootpack starts with exactly two initial terms, `F01_FINITUDE` and `N01_NONCOMMUTATION`, and says C3-C5 are governance rules believed true but not yet proven from C1+C2.

Therefore the pages mark C3/C4/C5 as derived/aligned governance constraints unless future repo evidence promotes them.

### 4. Repo-current Leviathan is a runtime, not Codex Ratchet

Observed support:

- `README.md:17-28` frames Lev as an open runtime for agent-human systems.
- `ARCHITECTURE.md:21-27` defines Lev as compiling/validating declarations through FlowMind, executing through Orchestration, routing events through Event Bus, running bindings through Poly, and extending via plugins.
- `ROADMAP.md:14-31` preserves current hardening gaps and prevents overclaiming.

### 5. Ratchet implementation evidence is partial and must be caveated

Observed support:

- `core/flowmind/system/ratchet-admission.flow.yaml` declares a rich 5-gate / 7-stage admission contract.
- `crates/lev-kernel/src/ratchet.rs` implements simpler evidence-presence admission with forward-only admitted IDs and tests for evidence-required/admitted/re-evaluation behavior.

The pages preserve the contract-vs-implementation gap and do not import Codex Ratchet proof/sim claims as Lev implementation proof.

## Files and pages produced

### `josh-root-constraints-in-leviathan.md`

Purpose: maps Josh/root-constraint contribution into current Lev surfaces with three layers separated:

1. repo-current implementation/contracts;
2. JP/Lev-dev intent;
3. Josh/root-constraint contribution.

Includes exact source paths, support labels, and overclaim guards.

### `lev-five-constraints-vs-f01-n01.md`

Purpose: maps Lev's five constraints against F01/N01 and preserves source-supported tiering:

- C1/F01 = root;
- C2/N01 = root;
- C3/C4/C5 = governance / derived-aligned unless repo evidence promotes them.

Includes North Star tension, Rust kernel note, wiki doctrine bridge status, and do-not-overclaim language.

### `codex-ratchet-vs-leviathan-boundary.md`

Purpose: hard non-collapse boundary between Codex Ratchet and Leviathan.

Includes the required sentence:

```text
Leviathan contains many Josh ideas but is NOT Codex Ratchet.
```

Also includes bridge statements, do-not-import rule, and layered safe/unsafe claims.

## Unresolved provenance gaps

1. **Raw Josh source archive not inspected.** `josh-flowmind-spec.zip` / raw Josh ratchet source files were not opened in this packet.
2. **Chat provenance remains unpromoted.** Session handoffs/transcripts were not promoted to repo-current truth. The prior provenance ledger remains the controlling source for guarded chat/provenance claims.
3. **ABAC governance implementation path unresolved.** `constraint-manifold.ts` says C3-C5 governance assumptions live in `abac-policy-engine.ts`, but bounded search under `core/flowmind` did not find a matching file. The pages therefore rely on YAML/schema/design/Rust enum support, not a located ABAC implementation file.
4. **Full boot path not verified.** This packet did not run package tests, typechecks, boot smokes, or end-to-end FlowMind kernel initialization.
5. **Current-code authorship not adjudicated.** Explicit Josh contribution signal exists in docs; JP role is design/provenance-supported; most code files themselves do not carry human authorship attribution.
6. **North Star vs FlowMind tiering tension remains.** `NORTH_STAR.md` calls all five constraints non-negotiable kernel DNA, while current FlowMind tiering distinguishes C1/C2 roots from C3-C5 governance assumptions. Pages preserve the tension rather than erasing it.

## Controller verification needs

A controller/editor should verify:

1. Frontmatter on all four files includes `title`, `created`, `updated`, `type`, `status: candidate/controller-verification-required`, and `claim_ceiling`.
2. `codex-ratchet-vs-leviathan-boundary.md` contains the exact required sentence: `Leviathan contains many Josh ideas but is NOT Codex Ratchet.`
3. No files outside the four assigned wiki outputs were modified by this packet.
4. Source paths and line ranges are acceptable for the current wiki citation style.
5. Claims about C1/C2 roots and C3-C5 governance/derived status match the intended controller doctrine.
6. The pages do not import Codex Ratchet proof/sim/math results as Leviathan implementation evidence.
7. The pages do not overstate runtime verification; no tests were run in this wiki-only tranche.
8. The unresolved ABAC implementation path gap should be either accepted as open or assigned to a later source pass.

## Final guardrail

This packet's outputs are candidate wiki boundary pages. They are ready for controller verification, not canonical final doctrine.
