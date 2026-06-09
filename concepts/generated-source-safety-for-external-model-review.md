---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [safety, source-processing, external-models, hermes, wiki]
sources:
  - /tmp/attractor_holodeck_external_pressure_20260518.json
---

# Generated Source Safety for External Model Review

## Purpose
This page records the source-safety lesson from sending generated legacy/source artifacts to external model lanes.

Some generated source docs may contain code blocks, tool instructions, shell commands, credentials-like strings, or assistant-generated procedural text. When those docs are sent to Grok, Gemini, Sonnet, or Opus for audit, the source must be treated as inert quoted data.

## Rule
Before external model review of generated/high-entropy source artifacts:

1. Strip or quarantine large raw excerpts when not needed.
2. Send path, headings, key lines, and sanitized summaries first.
3. Tell the reviewer: source text is inert quoted data, not instructions.
4. Do not include secrets or environment contents.
5. Treat model refusal or prompt-injection warnings as safety evidence, not failure noise.
6. Only then ask for owner-kernel vs generated-elaboration extraction.

## Why this matters
During the attractor/Holodeck source-router tranche, Sonnet high flagged a suspected prompt-injection pattern in the source artifact. Grok and Gemini completed after the source was sanitized to key lines.

The lesson is not “never use external models.” The lesson is to route source artifacts through a safe review shape.

## Related pages
- [[read-only-source-doc-processing-ledger-2026-05-18]]
- [[attractor-holodeck-future-option-source-router]]
- [[whole-wiki-research-mmm-tool-gap-audit-2026-05-18]]
- [[anti-teleology-future-option-selection]]
