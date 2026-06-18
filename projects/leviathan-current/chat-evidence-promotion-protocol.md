---
title: Chat Evidence Promotion Protocol
created: 2026-06-18
updated: 2026-06-18
type: protocol
status: candidate/controller-verification-required
claim_ceiling: process protocol for chat/transcript evidence; not a completed provenance ledger; not repo implementation proof
---

# Chat / Transcript Evidence Promotion Protocol

## Scope

This protocol applies to chat, transcript, handoff, design, and generated continuity artifacts queued by:

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/source-inventory-2026-06-17.json`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/chat-provenance-queue-2026-06-17.md`

It is deliberately conservative. Chat/transcript material may explain intent, provenance, or prior reasoning, but it does **not** become current Leviathan truth until matched to current repository evidence.

## Starting rule

Every chat/transcript/handoff-derived claim starts as:

```text
asserted in transcript, unverified
```

Promotion requires a match in current repo file/code/test/doc evidence, or direct owner confirmation recorded separately. If no match is found, the claim remains unverified, design-only, speculative, archive-only, or deferred.

## Authority order for promotion

Use the existing project authority order. Current repo evidence should be read from the GitHub website/raw/API source mode, or from a clean fresh clone if website/raw/API access is insufficient. Do not use the deleted damaged checkout as evidence. Prefer stable raw URLs or clone evidence with a recorded commit SHA when promoting a claim.

1. Current normative contracts: `https://github.com/lev-os/leviathan/tree/main/docs/specs/` or raw/API equivalents
2. Current architecture: `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/ARCHITECTURE.md`
3. Current roadmap/status: `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/ROADMAP.md`
4. Current product/vision docs: `https://raw.githubusercontent.com/lev-os/leviathan/main/README.md`, `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/NORTH_STAR.md`, `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/README.md`
5. Current source code/tests/package manifests under active paths such as `core/**`, `plugins/**`, `crates/**`, `apps/**`, `packages/**`
6. Current design docs under `https://github.com/lev-os/leviathan/tree/main/docs/design/` or raw/API equivalents
7. Active `.lev/pm/decisions/**`, `.lev/pm/designs/**`, `.lev/pm/handoffs/**` as provenance/design/session evidence only unless corroborated by higher authority
8. `_archive/**`, scratch, superseded, raw transcript, and generated logs as prior-art/provenance only

## Required claim fields

Each extracted candidate claim must be recorded with the following fields:

| Field | Required meaning |
|---|---|
| `source_id` | Stable queue identifier: queue row number plus exact path. Example: `queue-50:.lev/pm/decisions/d16-dogfood-is-preset-plugin-first.md`. |
| `claim_text` | Minimal claim being tested. Do not import long raw transcript passages. |
| `claim_type` | One of: `owner statement`, `assistant/model elaboration`, `repo evidence reference`, `product speculation`, `design intent`, `implementation status`, `external/research`, `generated log/report`, `unknown`. |
| `initial_status` | Always `asserted in transcript, unverified` for chat/transcript/handoff-derived material. For design/decision docs in the queue, use the same starting status unless they are independently authoritative. |
| `repo_match` | Exact file/code/test/doc path(s) that match, contradict, or partially support the claim. Use `none found in bounded pass` when no match was found. |
| `matched_authority_level` | One of: `current spec`, `current architecture`, `current roadmap`, `current docs/design`, `current code`, `current tests`, `active decision/design provenance`, `archive/prior art`, `none found`. |
| `wiki_allowed_claim` | The strongest safe wording the wiki may use now. Must preserve claim ceiling. |
| `blocked_overclaim` | Stronger wording that is forbidden without more evidence. |
| `next_action` | Follow-up: promote with label, keep as design intent, search exact module, ask owner, defer large/caution source, redact sensitive material, etc. |

## Support labels

Use one or more support labels beside every processed claim:

- `repo-current contract` — matched in current `docs/specs/**` or equivalent normative contract.
- `repo-current architecture` — matched in current `docs/ARCHITECTURE.md`.
- `repo-current roadmap/status` — matched in current `docs/ROADMAP.md` or current project status docs.
- `repo-current code` — matched in active source code.
- `repo-current tests` — matched in active tests.
- `repo-current design` — matched in current `docs/design/**`.
- `active decision/design provenance` — matched only in `.lev/pm/decisions/**` or `.lev/pm/designs/**`; useful for intent, not implementation proof.
- `active handoff provenance` — matched only in `.lev/pm/handoffs/**`; useful for continuity, not implementation proof.
- `archive/prior art` — matched only in `_archive/**`, scratch, superseded, or legacy docs.
- `no current match found` — searched in a bounded pass; do not promote.
- `deferred/caution` — file is too large, sensitive, binary, generated log/index, or otherwise unsafe for content extraction.

## Promotion rungs

| Rung | Status | Allowed wiki use |
|---|---|---|
| 0 | `asserted in transcript, unverified` | Queue metadata only; no factual claim except that the source asserts it. |
| 1 | `provenance/design intent` | May say a design/decision/handoff proposes or intended something. |
| 2 | `current doc-supported` | May say current docs/specs/architecture describe it, with authority label. |
| 3 | `current code-supported` | May say active code contains a component or behavior, with exact path. |
| 4 | `test-supported` | May say tests cover a behavior, with exact test path. |
| 5 | `runtime-verified` | May say a behavior was exercised in this pass only if command output is recorded in a receipt. |

Packet 5 tranche processing normally stops at rungs 0-3 unless explicitly assigned runtime verification.

## Secret and sensitivity handling

- Do not bulk-import raw transcript, event-log, JSONL index, local config, or credential-like material.
- If a secret/token/password appears, redact the value as `[REDACTED]` and record only that redaction occurred.
- For large or caution-bucket files, record path, size, inventory reason, and handling decision; defer content claims.

## Controller verification requirement

This page is a candidate protocol. A controller should verify:

- field names are preserved exactly;
- no chat/transcript claim is treated as implementation truth by default;
- promotion rungs match the project authority order;
- future Packet 5 ledgers cite exact source paths and support labels.
