---
title: Source Provenance Appendix - ClaimGate Nested Wave Patch
created: 2026-06-23
status: reference_provenance_for_review
claim_ceiling: source/provenance appendix only; not Lev canon, not applied patch content
---

# Source Provenance Appendix

This appendix records the previous ClaimGate zips, patch deltas, and JP comments
that shaped the current `claimgate-nested-wave-overall.patch` send packet.

The current send packet remains the narrow review artifact:

```text
claimgate-nested-wave-overall.patch
```

The sources below are provenance and design pressure. They are not automatically
imported into Lev, not host-admitted, and not a substitute for Lev's gates.

## Current Send-Packet Boundary

The send packet intentionally preserves the ClaimGate / nested-wave / management
plane upgrade as a reviewable patch candidate against Lev:

```text
WizardRun
  Work Plane:
    sequenced waves -> nested councils -> agents -> skills/MMMs/tools/source packs
  Management Plane:
    conductor/resource/context/laggard/reroute/gate/receipt/failure routing
  Gate Plane:
    Lev gates + ClaimGate gates + host eval/receipt/admission
```

It does not claim that the full nested council runtime, full skill/MMM loading,
or production host admission is complete.

## Artifact Inventory

### Zips

| Artifact | Observed package version | Entries | Size | SHA256 | Intake status |
|---|---:|---:|---:|---|---|
| `/Users/joshuaeisenhart/Downloads/ClaimGate_CoreLevOS_COMPLETE_SINGLE_ZIP_codex_v57_claude_delta_wave_admission.zip` | `1.51.0-codex-v57-claude-delta-wave-admission` | 482 | 747148 | `8b175f8358f23692275c25b0f0fdd3f105dfb6d9c00ae55c3813bbe02ffb4b76` | Source/reference |
| `/Users/joshuaeisenhart/Downloads/ClaimGate_CoreLevOS_COMPLETE_SINGLE_ZIP_codex_v58_live_swarm_reroute_gate.zip` | `1.52.0-codex-v58-live-swarm-reroute-gate` | 487 | 754965 | `6dc9be8208787c5fdf009494731898c1fcec12142296c8207172cf1877067053` | Source/reference |
| `/Users/joshuaeisenhart/Downloads/ClaimGate_CoreLevOS_COMPLETE_SINGLE_ZIP_v58_wavegraph_source_read_loop.zip` | `1.52.0-v58-wavegraph-source-read-loop` | 491 | 760704 | `b87b5724e5e79bacf962cfb9d938180fc4a2605b555f31608c07d736310230dc` | Source/reference |
| `/Users/joshuaeisenhart/Downloads/ClaimGate_CoreLevOS_COMPLETE_SINGLE_ZIP_codex_v58_live_swarm_honesty_delta.zip` | `1.52.0-codex-v58-live-swarm-reroute-gate` | 496 | 769565 | `3843085b81fc92820e29e689c77ab8a0b78df05adfb2596c27e956eaff19c0e3` | Source/reference; filename is newer than package version |
| `/Users/joshuaeisenhart/Desktop/claimgate archive/claimgate_v57_claude_delta_wave_admission.zip` | `1.52.0-codex-v58-live-swarm-reroute-gate` | 16138 | 12296039 | `65385dc18397996c638bf6cfdf331567406ae38a685f2f3cacbdf446d40a3d18` | Archive/Finder variant; not canonical v57 |

Observed warning: the `final_verification/VERIFIED_CURRENT_CUT.txt` files inside
these v57/v58 packages still report the older v45 package identity. Treat those
verification files as stale unless separately re-run. The package metadata,
audit docs, zip counts, and current local apply/test checks outrank the stale
verification prose.

### Patch Deltas

| Patch | Size | SHA256 | Core content | Intake status |
|---|---:|---|---|---|
| `/Users/joshuaeisenhart/Downloads/claimgate_v58_live_swarm_honesty_delta.patch` | 31689 | `6f2aa49ea23d2195572b870311fd9ff11c88deb2665c2f47c8949f1af9c77177` | `tools/live-swarm-run.js`, `tests/live-swarm-tests.js`, packaging, compact `.cdo` dogfood receipts | Candidate hardening input |
| `/Users/joshuaeisenhart/Downloads/claimgate_v58_host_signature_repair.patch` | 17403 | `4ed058d5716959676226618c3cf87367522eb2789e8a4c0f6113bc269f3d4234` | `claimgate-wave-runtime` host-admission signature checks, tests, verification note rewrite | Candidate hardening input |

The current JP send packet does not automatically include either delta. They are
kept here so a reviewer can see which hardening paths exist without widening the
main patch review.

## Useful Mechanics Preserved From Earlier Cuts

### v57 Claude-Delta Wave Admission

Useful pattern:

- Read-required waves fail closed by default.
- Demo wave loops bind read evidence.
- Noncommutative wave ordering preserves different outcomes instead of pretending
  `construction -> verification` equals `verification -> construction`.
- Unknown start waves block.
- Clean wave loops can ask ClaimGate core for admission while keeping
  `promotion_allowed:false` at the wave runtime layer.

Boundary:

- The Claude branch is source material, not authority.
- Local tests/product verification are the authority.
- No production Lev host/eval admission is claimed by the package.

### v58 WaveGraph Source-Read Loop

Useful pattern:

```text
SourcePackReadLedger
  -> SourcePackConsumptionGate
  -> WaveGraphGate
  -> WaveRun/WaveGate
  -> AttractorBasinBindingGate
```

This is directly aligned with the Lev graph-patch framing: source reads become
load-bearing graph edges, later-wave starts must prove or backfill source
binding, and raw worker expansion without verification is treated as basin
leakage.

Boundary:

- Fixture-backed.
- Stronger than v57 because source-to-wave binding is load-bearing in tests.
- Still not production connector provenance or production Lev admission.

### v58 Live Swarm Reroute Gate

Useful pattern:

- Live swarm member failures become structured signals.
- Malformed/missing JSON and high failed-member ratios block instead of
  silently passing.
- Failed seats can reroute to a different provider.
- Receipts track provider attempts and reroute counts.
- Transparent advisory reviewer prompts replace cover-story framing.

Boundary:

- Live model/council output still cannot promote.
- Deterministic gates remain the promotion boundary.
- Local product proof, not production Leviathan host admission.

### v58 Live Swarm Honesty Delta

Useful pattern:

- Adds `live_swarm.too_much_signal_collapse`.
- Repeated identical `failure_signal` collapse is blocked.
- Packaging ships deeper receipt directories when present, not only summaries.
- Tiny two-seat Claude Bridge dogfood shows Sonnet/Opus JSON member observations
  can be parsed into receipts.

Boundary:

- Does not prove real API-backed multi-provider dogfood.
- Does not prove provider diversity for the tiny dogfood run because both models
  came through `anthropic-claude-bridge`.
- Does not repair the older scripted `100 -> 12 -> 3 -> 0` fixture loop.

### Host Signature Repair Patch

Useful pattern:

- Strict base64 decoding.
- DER ECDSA signature must consume the whole buffer.
- Host admission receipt signature payload excludes signature fields before
  verification.
- Trusted host keys must resolve from the host trust root.
- Production-key checks distinguish fixture/dev trust from production admission.

Boundary:

- Candidate hardening input only.
- Must be reconciled with Lev's current `claimgate-steering` consumer and
  receipt policy before being merged.

## JP Comments Distilled As Design Pressure

These comments are source commentary from JP, not binding Lev authority.

Accepted design pressure:

- Lev is literally a project harness eval suite.
- Look at `core/eval` plans.
- Search and compare `.lev` fractal island project conventions.
- Patches are welcome, but Lev is not complete.
- Use Lev OS underneath; do not re-implement proof concepts as a parallel stack.
- Semantic control means ontologies and scoring are fed into validator nodes on
  the graph; Lev exec dispatches and controls CLI agents; validators submit
  structured eval; deterministic gates outside agent control determine pass/fail.
- Proposals can update ontology, docs, code, or other graph material, but they
  must be part of the graph patch.
- Accepted canon/code goes into the world model and the graph projects out from
  that.
- The useful chain is roughly:

```text
world engine -> wiki/MMM/Lev flows/code -> graph
```

- The engine is a plugin/world-engine pattern, not only git mechanics.
- A gate digger is needed: use LLMs to generate gates for something else, but do
  not allow the LLM output itself to promote.
- Agent work can be judged by a second evaluator/validator; that evaluator can
  score structured variables, but the deterministic gate controls promotion.
- Parallel exploration at gates matters. Failures are valuable signal. Different
  branches/loops should approach the gate from different lines of attack.
- SDLC/ClaimGate/marketing/creative operations are a plausible first
  manifestation domain because they produce concrete tasks, evidence, metrics,
  and daily operational pressure.

Implication for the current patch:

The correct shape is not "another standalone ClaimGate proof stack." The correct
shape is a Lev-compatible patch that preserves:

```text
proposal -> gate -> repair/reroute loop -> evidence -> host receipt
```

while letting nested waves/councils/agents/skills/MMMs remain proposal and
execution surfaces, not authority surfaces.

## Relationship To Current Patch Packet

The current patch packet is intentionally narrower than the full v57/v58 archive
lineage. It should be reviewed as:

- Lev-side ClaimGate steering/loop/replay/admission surfaces.
- Repair dispatch and CDO/OpenRouter sparse advisory lanes.
- A candidate bridge from gates to repair loops.
- A preservation of nested wave/council/management-plane architecture.

It should not be reviewed as:

- a claim that all v57/v58 ClaimGate package code has been imported;
- a claim that JP has approved the patch;
- a claim that the screenshots are requirements;
- a claim that the stale package verification docs prove current v57/v58 state;
- a claim that live swarm or Claude Bridge output can promote anything.

## Next Review Routes

If this packet gets another pass before sending, the highest-leverage follow-up
routes are:

1. Compare the current patch's `claim-gate-loop` and repair dispatch with the
   v58 `WaveGraph Source-Read Loop`.
2. Decide whether `GateToWaveRoute` should be a first-class Lev contract.
3. Add explicit skill/MMM loading contracts for agents so nested councils do not
   degrade into ad hoc generic swarms.
4. Treat management agents as sidecars: conductor, resource manager, context
   loader, laggard monitor, reroute manager, gate ops, receipt manager,
   blackboard/state manager, claim ceiling manager, and human escalation.
5. Reconcile host signature repair with Lev's current steering consumer before
   importing any production-key semantics.

## Appendix Claim Ceiling

This appendix is a bounded provenance record. It preserves useful mechanics and
source pressure. It does not change Lev, does not alter the patch, does not
promote ClaimGate output, and does not turn screenshots or archived zips into
authority.
