---
title: Leviathan Provenance Status Guardrails
created: 2026-06-19
updated: 2026-06-19
type: provenance-guardrail
status: current-source-synthesis
claim_ceiling: provenance labeling policy only; not authorship proof
tags: [leviathan, provenance, josh, jp-smith, codex-ratchet, claim-ceiling]
sources:
  - /Users/joshuaeisenhart/.codex/attachments/9d7bccf2-41e3-4c04-9659-2e2acb2d01da/pasted-text.txt
  - projects/leviathan-current/josh-jp-attribution-boundary-v2-2026-06-19.md
  - projects/leviathan-current/no-ratchet-from-leviathan-policy.md
  - projects/leviathan-current/wizard-origin-provenance-note-2026-06-19.md
---

# Leviathan Provenance Status Guardrails

When provenance is unclear, say "unspecified." Do not launder a likely story into authorship fact.

## Status Labels

| Label | Meaning |
|---|---|
| verified | commit history, source file, maintainer statement, or owner-confirmed artifact supports it |
| user-provided | Josh stated it, but independent source proof is not attached here |
| source-signal | keyword, file, package, or doc suggests a connection |
| unspecified | not enough evidence to assign author/origin |
| disputed | sources or owner notes conflict |
| rejected | current boundary pages explicitly block it |

## Current Guardrails

- Codex Ratchet does not come from Leviathan.
- Convergent Ratchet-side material should be treated as Joshua-origin unless direct contrary evidence exists.
- JP Smith is credited with the original Wizard idea per Josh; this is `user-provided` unless a separate source artifact is attached.
- Current Wizard packet lineage is separate from the original idea provenance.
- Leviathan can host Joshua constraint/QIT material without becoming Codex Ratchet.
- Josh-associated artifacts inside Leviathan are not proof of total architecture authorship.

## Required Fields For Future Provenance Pages

```yaml
claim:
claimant:
status: verified | user-provided | source-signal | unspecified | disputed | rejected
evidence:
verification_target:
unsafe_promotions:
```

## Blocked Claims

- Josh authored all Leviathan implementation.
- JP originated Codex Ratchet root constraints.
- Codex Ratchet is a Leviathan subsystem.
- Wizard is purely JP's or purely Josh's without lineage split.

## Read Next

- [[projects/leviathan-current/josh-jp-attribution-boundary-v2-2026-06-19]]
- [[projects/leviathan-current/no-ratchet-from-leviathan-policy]]
- [[projects/leviathan-current/wizard-origin-provenance-note-2026-06-19]]
- [[projects/leviathan-current/leviathan-claim-ceilings-2026-06-19]]
- [[projects/leviathan-current/packet-14-pasted-fep-atlas-and-leviathan-boundary-intake-2026-06-19]]
