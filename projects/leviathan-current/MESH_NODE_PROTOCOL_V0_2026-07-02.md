---
title: Mesh Node Protocol v0
created: 2026-07-02
updated: 2026-07-03
type: protocol-contract
status: current two-node practice formalized
claim_ceiling: contract record for the already-running Josh/JP two-node seam; not a generalized mesh launch, not a node #3 certification, and not canonical CR result promotion
tags: [lev, codex-ratchet, mesh, protocol, admissibility, evidence]
sources:
  - projects/leviathan-current/LEV_CR_INTEGRATION_STATE_2026-07-02.md
  - projects/leviathan-current/GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md
---

# Mesh Node Protocol v0 - 2026-07-02

This protocol formalizes the practice already running between Josh's Codex Ratchet node and JP's Lev node. It is not aspirational mesh language. It records the current two-node contract: sovereign machines exchange content-addressed artifacts, each receiving node verifies through its own gates, and every claim crossing the seam carries provenance plus executable falsifiers.

## Status ladder

Protocol claims use the same receipt-bound ladder as the integration state:

```text
exists < runs < passes fresh local rerun < mutation-proven load-bearing < admitted by declared gate < landed upstream < canonical by process
```

This page is `current two-node practice formalized`. It does not claim node #3 readiness, autonomous federation, or release-grade mesh operation.

## Related

- [Lev / CR Integration State](./LEV_CR_INTEGRATION_STATE_2026-07-02.md)
- [Gate Doctrine: Admissibility, Not Quality](./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md)
- [Relevant Docs Index](./RELEVANT_DOCS_INDEX_2026-07-02.md)
- [Codex Ratchet vs Leviathan Boundary](./codex-ratchet-vs-leviathan-boundary.md)
- [Leviathan Claim Ceilings](./leviathan-claim-ceilings-2026-06-19.md)

## Related Docs - 2026-07-03

Wiki:

- [[projects/leviathan-current/source/README]] and `projects/leviathan-current/source/leviathan-v3.2.txt` - archived v3.2 normative source copy and lineage-gap note.
- [[concepts/emotional-evolution-personality-system]] - commune/personality model adjacent to selective exposure, mirrors, service, and peer witness.
- [[wizard/harness-consolidated/19_grammar]] and [[wizard/harness-consolidated/20_phrasebook]] - current MMM/harness grammar and phrasebook.
- [[_archive/harness_2026-04-17_steward_trim/19_grammar]] and [[_archive/harness_2026-04-17_steward_trim/20_phrasebook]] - archived grammar/phrasebook lineage from the sweep.

Lev repo refs:

- `docs/_inbox/clawmeet-distributed-agent-mesh.md`
- `docs/specs/spec-poly.md`
- `docs/specs/spec-poly-ws-streaming.md`
- `docs/specs/spec-poly-*`
- `docs/specs/spec-semantic-control.md`
- `docs/design/design-semantic-control.md`

## Substrate: poly

This protocol formalizes and extends Lev `core/poly`; it does not parallel-invent a second mesh protocol. JP's grounding is explicit: "poly protocol is what i called it, didnt realize it was a mesh protocol at the time." Mesh Node Protocol v0 is therefore the receipt-bound articulation of the same substrate under the Josh/JP seam: `core/poly` supplies the proto-mesh protocol surface, and this page names the current obligations, claim ceilings, and cross-node evidence rules that grow out of it.

## Definitions

| Term | Contract meaning |
|---|---|
| NODE | A sovereign machine running `lev`, deterministic gates, an evidence estate, and a human owner. |
| EXCHANGE | Content-addressed artifacts only: git patch series with verbatim authorship, witness evidence JSONs with `sha256`/FNV addresses, receipts, and returned findings. |
| EVIDENCE ESTATE | The local inventory of source, artifacts, receipts, schemas, adapters, tests, gates, and graph rows a node can verify directly. |
| PEER WITNESS | The other node's gates and receipts. Peer witness is not a leader, authority transfer, or self-grading shortcut. |
| CORRECTION | A returned patch, receipt, or finding that changes the sender's candidate, schema, adapter, or claim language. |

## Obligations

Receiving nodes MUST verify through their own gates before integration.

Minimum receiving-node obligations:

- run `git am --check` or an equivalent dry-run before applying a patch series;
- preserve verbatim authorship for imported patch series unless the receiving owner explicitly rewrites and records that rewrite;
- run the node's declared tests, typechecks, adapters, and gate batteries before claiming integration;
- fail closed when evidence is sparse, self-graded, missing provenance, stale against source, or missing executable falsifiers;
- bind verification claims to exact commits, patch ids, addresses, command receipts, and schema versions;
- return findings to the sender as messages, patches, or receipts instead of silently promoting local interpretation.

The adapter rule is load-bearing: sparse evidence and self-graded evidence are not lower-quality passes. They are inadmissible until rerun or reshaped.

## AA-loop mapping

Owner Leviathan v3.2 framing maps onto the two-node seam as follows:

| AA-loop term | Mesh node mapping |
|---|---|
| inventory | evidence estate: local source, receipts, schemas, gates, adapters, and graph rows |
| exposure | sharing receipts and content-addressed artifacts across the seam |
| peer witness | the other node's gates, never a leader or global authority |
| correction | returned patch, failed receipt, hostile review finding, or schema repair |
| service | building adapters, witness packs, and receipt paths for each other |

The loop is bilateral. Josh/CR can send evidence and patches to JP/Lev; JP/Lev can send fixes, schemas, and findings back to Josh/CR. Neither side gets to promote a claim merely because the other side said it passed.

## Proof-graph rule

Claims never cross the seam without provenance and executable falsifiers.

For a claim-bearing artifact to cross:

- source provenance must be resolvable by commit, content hash, schema id, or receipt address;
- the claim must declare its earned status rung;
- `negative_tests` or an equivalent executable falsifier must be present for gate-relevant claims;
- the receiving adapter must be able to reject malformed, sparse, stale, or verdict-shaped provider evidence;
- graph/world-model residency, when used, must preserve labels and evidence references rather than flattening them into a broad "green" status.

Safe claim: "candidate evidence survived declared gates at commit/address X."

Unsafe claim: "the result is canonical" unless the owning process has separately promoted it to that rung.

## Protocol in action so far

| Event | Receipt-bounded status |
|---|---|
| Three-patch series landed verbatim | Patch-series exchange is working; authorship-preserving import has occurred. |
| Adapter caught idealized fixtures | Receiving-node gates rejected sender-side fixture assumptions; this is a successful fail-closed correction. |
| Rounding hole found by hostile review | Review exposed a tolerance/rounded-value hole; upstream fix compares unrounded values before tolerance. |
| Julia-leg fix converged independently on both nodes | Basin event: independent builders arrived at behaviorally equivalent repair pressure. |
| `cr_constraint_battery` superseded ours | Better provenance won; JP's upstream battery displaced the local candidate rather than preserving sender ownership. |

These events support a `current two-node practice formalized` status. They do not prove generalized mesh readiness.

## Current contract surface

| Surface | Current contract | Claim ceiling |
|---|---|---|
| Patch series | Sender exports ordered patches; receiver dry-runs, reads, applies, and tests locally. | `landed upstream` only when exact receiving commit is named. |
| Witness evidence JSON | Sender provides schema-shaped, content-addressed evidence. | `admitted by declared gate` only after receiver adapter and tests pass. |
| Receipts | Commands, results, graph rows, and addresses are exchanged as evidence, not authority. | Receipt proves what it records, no broader result promotion. |
| Returned findings | Receiver sends failures and corrections back across the seam. | Findings are correction inputs until applied and verified by sender. |

## Growth path, fenced for later

```text
FENCED / NOT CURRENT CLAIMS

node #3+ by induction:
  A third sovereign node may join only after the two-node obligations are boring,
  repeatable, and scripted enough that a new node can verify without social trust.

avatar membrane:
  Owner/avatar boundary work is future membrane design, not part of v0 exchange.
  JP adopts the avatar-membrane/selective-exposure concept as the intended
  direction for owner/avatar boundary work; existing low-level plumbing gives
  the seam something concrete to iterate on before any v0 exchange claim is
  expanded.

SBC / CRC / ECC accounting dimensions:
  Structural bookkeeping, cyclic redundancy, and error-correcting accounting lanes
  remain design candidates. They are stage-gated behind two-node hardening.
```

## Claim ceiling

This protocol may be cited as the current Josh/JP two-node contract and as evidence that the seam is already operating under content-addressed exchange plus receiving-node verification. It may not be cited as a mesh launch, leader election protocol, generalized federation proof, or admission of any CR result beyond the exact commits, patches, addresses, and receipts that passed declared gates.
