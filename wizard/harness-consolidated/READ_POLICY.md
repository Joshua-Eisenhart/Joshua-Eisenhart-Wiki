last_updated: 2026-04-17

# Read Policy — Tiered Priming by Context Budget

When an agent cannot read all 20 harness files, it should still be primed. Pick the tier that fits the context budget; never skip priming because context is tight.

## Tier 1 — Injection only (tightest, no reads)

Use when: token budget does not allow even one file read (e.g. inline tool call, sub-subagent, slash command template).

Action: prepend **Block A** (60 words) from `SALIENCE_PREAMBLE.md` to the system prompt. No file reads required.

Covers: root axiom, primitive relation, banned / preferred verbs, status ladder, pushback.

Known gaps: no claim pattern, no grammar, no phrasebook, no anti-patterns. Output under this tier is admissible for short replies but NOT for substantive claims or sim reports.

## Tier 2 — Standard (loader + verbs + grammar)

Use when: budget allows ~300 lines of reading before task work.

Action:
1. Prepend **Block B** (140 words) from `SALIENCE_PREAMBLE.md` to the system prompt
2. Read `SALIENCE_LOADER.md`
3. Read `03_language_discipline.md` (verbs)
4. Read `16_dictionary.md` (nouns)
5. Read `19_grammar.md` (sentence patterns)

Covers: injection priming + read-time discipline + claim-level grammar.

Known gaps: no coupling program order, no status-label specifics, no sim-kind discipline, no UNSAT primacy, no anti-patterns, no pushback doctrine. Use for short analysis tasks and drafting — NOT for canonical sim work or for multi-step coordination.

## Tier 3 — Deep (full boot)

Use when: agent will do canonical sim work, multi-step coordination, doctrine edits, or any substantive artifact production.

Action: follow `00_READ_FIRST.md` in full. All 20 files including anti-patterns, status ladder, z3 UNSAT primacy, coupling program order, pushback, owner doctrine index, PyTorch ratchet, f01/n01 axioms, Leviathan constraint map, pre-emit audit, red-team probes.

Covers: full harness.

## Selection rule

- canonical sim / owner doctrine work → Tier 3 (required)
- drafting, analysis, code review → Tier 2 (default)
- inline tool calls, short slash commands, sub-subagents spawned by another subagent → Tier 1
- if an agent reports task completion under Tier 1 or Tier 2 that required Tier 3, the parent must rerun under Tier 3 before accepting the result

## Anti-patterns

- skipping priming entirely because "context is tight" — use Tier 1 at minimum
- claiming Tier 3 was applied when only Tier 1 was injected
- upgrading claims earned under Tier 2 into canonical status labels without a Tier 3 pass

## See also

- `SALIENCE_LOADER.md`
- `SALIENCE_PREAMBLE.md`
- `00_READ_FIRST.md`
- `04_status_label_hierarchy.md`
