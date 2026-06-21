---
title: ClaimGate authority state machine for Research Ratchet
created: 2026-06-21
updated: 2026-06-21
type: state-machine
status: current-research-overlay
claim_ceiling: authority-chain mapping; no production host/KMS/HSM claim
tags: [claimgate, authority, trust-root, state-machine, research-ratchet, spinor-memory]
---

# ClaimGate authority state machine for Research Ratchet

## Purpose

ClaimGate is the authority transition spine for Research Ratchet. Spinor Memory should mirror ClaimGate lifecycle state; it must not replace it.

## State chain

The authority chain is:

```text
proposal
  -> owner approval
  -> host consumption request
  -> host receipt
  -> admission result
  -> enforcement state
```

The v39 line tightened the chain by unifying admission logic, adding expiry/replay/request binding, and preserving proposal-only discipline. The v40 line wired trust-root verification through consume when configured. The v41 line makes enforcing scope require trust-root verified owner and host authority and adds non-authoritative spinor memory.

## State labels for Spinor Memory

A `SpinorMemoryCell` should use explicit authority state:

```text
draft
proposal_only
owner_approved
host_requested
host_receipted
admitted_probe
admitted_enforcing_verified
blocked
graveyarded
```

Do not collapse these states.

## Required transitions

```text
draft -> proposal_only
proposal_only -> owner_approved
owner_approved -> host_requested
host_requested -> host_receipted
host_receipted -> admitted_probe
host_receipted -> admitted_enforcing_verified
any -> blocked
any -> graveyarded
```

## Enforcing transition rule

For enforcing scope, `admitted_enforcing_verified` requires:

- owner trust root configured;
- owner approval signature verifies against trusted owner key;
- host trust root configured;
- host receipt signature verifies against trusted host key;
- request hash binding present;
- expiry valid;
- approval not replayed;
- receipt and proposal hashes match;
- approval decision is the expected approval decision.

Without those, the memory cell may record proposal/probe/advisory state, but not enforcing authority.

## Replay rule

An enforcement-grade owner approval should be single-use unless explicitly designed otherwise. Persistent spent-approval ledger entries should block second consumption.

## What Spinor Memory may do

Spinor Memory may show that a claim is pre- or post-gate, preserve left/right authority orientation, warn that a requested operator is illegal, mark graveyard collisions, rerank retrieved notes by authority state, and support ColdStartPacket reconstruction.

Spinor Memory may not sign, verify signatures, decide admission, promote canon, convert probe approval into enforcement, or replace Eval/Effect/ClaimGate receipts.

## State-machine test matrix

| Test | Expected |
| --- | --- |
| host consume before owner approval | blocked |
| expired approval | blocked |
| replayed approval | blocked |
| host receipt missing request hash | blocked |
| fixture/no trust root with enforcing scope | blocked |
| trusted owner + trusted host + correct request/receipt | enforcing admitted |
| LLM prose says pass | no authority change |
| dashboard green | no authority change |
