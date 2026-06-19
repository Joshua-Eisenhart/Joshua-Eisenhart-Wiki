---
title: Ratchet Assessment Receipt
created: 2026-06-18
updated: 2026-06-19
type: receipt
status: historical-wiki-only-assessment
claim_ceiling: model-pressure and process receipt; not accepted Leviathan implementation work; not runtime proof
---

# Ratchet assessment receipt — 2026-06-18

## Status

Observed: this page is now a **wiki-only assessment receipt**, not a record of accepted Leviathan repo implementation work.

Scope correction: Josh clarified that this Hermes lane is for building the LevOS/Leviathan wiki, not for changing the Leviathan repo. Any local ratchet code edits made during the detour were reverted from the repo working tree.

## What the detour still usefully showed

Three OpenRouter model lanes were run as pressure readers:

- `openrouter/fusion`
- `z-ai/glm-5.2`
- `anthropic/claude-opus-4.8`

All three independently flagged the same repo/wiki understanding gap: the current ratchet story must not be explained as fully implemented just because the architecture and FlowMind contract name it.

## What was wrong in the wiki process

### 1. The wiki got ahead of runtime proof

Observed: earlier wiki pages could make the ratchet sound more landed than the code justified.

Correction: wiki pages should separate:

- **contract / intended ratchet** — what `core/flowmind/system/ratchet-admission.flow.yaml` says;
- **Rust/kernel implementation** — what `crates/lev-kernel/src/ratchet.rs` actually does;
- **TypeScript / FlowMind surfaces** — how policy/runtime docs refer to admission;
- **open gap** — what is still aspirational or unwired.

### 2. We under-used model diversity early

Observed: the first wiki wave used Hermes/subagent work and did not use enough independent model pressure for high-entropy concept extraction.

Correction: future Leviathan wiki packets should use OpenRouter Fusion and GLM 5.2 as preferred heavy pressure/synthesis lanes where available, with provider output treated as advisory until the controller verifies source paths and writes grounded markdown.

### 3. The repo build surface must be described honestly

Observed: running Cargo from repo root failed because the Rust workspace root is `crates/`. Running from `crates/` required a restored `crates/lev-agentfs` submodule worktree.

Wiki consequence: build/test notes should name exact roots and blockers instead of saying generic “tests pass/fail.”

## Repo mutation status

Observed after scope correction: the local changes in these files were reverted:

- `/Users/joshuaeisenhart/GitHub/leviathan/crates/Cargo.lock`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/bridge.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/lib.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/manifold.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs`

This page should not be cited as a repo patch receipt. It is a wiki/process correction receipt.

## Wiki guidance for future ratchet pages

Use this claim ceiling:

```text
The ratchet is a central intended admission discipline in Leviathan. The contract language is richer than the currently verified implementation surface. Explain both without collapsing contract intent into runtime proof.
```

Next useful wiki work:

- write a contract-vs-implementation ratchet page;
- map exact ratchet-related source files;
- keep Josh/root-constraint provenance separate from JP/Lev implementation ownership;
- keep model pressure receipts as advisory, never as repo truth.
