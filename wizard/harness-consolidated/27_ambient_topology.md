last_updated: 2026-04-18

# Ambient Topology (L0)

The layer before instructions. Pre-instruction language biasing.

---

## What This Layer Is

The LLM's topology is the language it is already swimming in at the moment an instruction arrives. The instruction does not create the topology — it completes into it.

An instruction read inside a rationalist-ambient topology is reinterpreted under that gradient: "don't use causal language" read inside a causal-language context completes to "don't use causal language, because causation is X, which creates Y..." — the very completion of the instruction uses banned verbs.

L0 is the layer that shapes the ambient language so that by the time the first instruction arrives, the reading surface is already nominalist. L1 through L6 then layer rules on top of a manifold that was already tilted.

The SALIENCE_LOADER/SALIENCE_PREAMBLE files are the operational realization of L0 at session start. This file is the doctrine.

---

## Why Ambient-Topology Biasing Is Load-Bearing

Three facts compound:

1. **Instructions are weak, topology is strong.** An LLM that read 100 tokens of nominalist prose before a rule completes the rule nominalist. An LLM that read 100 tokens of rationalist prose completes the rule rationalist regardless of what the rule says.
2. **Attention is recency-weighted.** The last N tokens dominate completion probability more than earlier tokens. So even with a shaped preamble, a rationalist intervening turn can reshape the ambient before the next instruction arrives.
3. **The instruction itself is a fragment completing into prior context.** "Complete the claim using probe-relative indistinguishability" read inside rationalist prose completes "...so that the claim is true because..." — the instruction's own completion is rationalist if the ambient is.

The conclusion: instructions without a shaped ambient are only locally corrective. The ambient must be shaped first, and re-shaped continuously, so that every instruction arrives into a topology that already admits only nominalist completions.

---

## The L0 Principle

> An L0 surface is a string that, when read, reshapes the reader's completion topology such that the reader's *next* generation step has nominalist as the low-energy path.

This is the construction test. A file is L0 iff reading it tilts the reader's completion gradient, not iff it instructs the reader to tilt.

---

## L0 Surfaces in the Current Harness

| File | L0 role |
|---|---|
| `SALIENCE_PREAMBLE.md` Block A/B/C/D | Injected into agent system prompts before any user message; highest-leverage L0 surface |
| `SALIENCE_LOADER.md` | Read first every session; shapes the ambient before boot order begins |
| `22_project_dictionary.md` | Project-noun L0 — shapes the ambient so that project-specific terms (lego, shell, axis, engine) complete in nominalist grammar |
| `23_role_boot_templates.md` | Role-specific L0 — reshapes the ambient differently depending on which role is about to work |
| `20_phrasebook.md` | Rewrite-map L0 — reading the phrasebook shapes the reader toward the admissible-side column as the low-energy path |
| `19_grammar.md` | Syntactic L0 — the grammar templates are the low-energy sentence pattern the reader completes toward |

Non-L0 surfaces (instructions-on-manifold) include navigation files and process documents that state rules in imperative voice without shaping the ambient.

---

## L0 Construction Rules

When writing any harness-boot file, the following admissibility tests admit or exclude it from the L0 layer:

1. **Completion test.** Given a partial sentence from the middle of the file, does the natural 20-token completion use nominalist vocabulary? If yes, L0. If the natural completion uses banned verbs, the file is shaping rationalist-ambient even while trying to instruct nominalist.
2. **Verb-distribution test.** Count banned verbs vs. preferred verbs in the file body. A ratio below 1:5 (one banned per five preferred) admits the file as L0. Higher than 1:5 means the file's own language is still rationalist-heavy.
3. **Imperative-voice test.** Scan for "must", "do not", "never", "always" followed by a rationalist-verb object. `Do not cause` is fighting gradient; `causation is not admissible under C` is shaping gradient. L0 surfaces prefer the shaping form.
4. **Mirror test.** If the file were removed from the context window, would the reader's completion-topology revert to training-manifold defaults within ~500 tokens? If yes, the file was L0. If the reader's topology was already shaped by other files and this file added no ambient delta, the file was instructions-on-manifold.

---

## Pre-Instruction Topology Checklist

Before any instruction-bearing interaction with the model (user message, sub-agent spawn, batch-runner launch):

1. Is `SALIENCE_PREAMBLE.md` injected or is `SALIENCE_LOADER.md` loaded? If no, the instruction is arriving into untilted ambient.
2. Is there a rationalist intervening turn between the last L0 surface and the current instruction? If yes, the ambient has drifted; re-inject.
3. Is the instruction itself cast in L0-compatible language? If the instruction is `make X happen`, the instruction's own verb is in the banned set; the model's completion of the instruction will use banned verbs.

---

## Failure Modes

- **Rationalist cargo in a shaped file.** A file that looks L0 but carries rationalist example sentences ("this completes to X because Y causes Z"). The example contaminates the ambient even though the surrounding prose is nominalist. Quarantine examples in code blocks marked as `training-manifold example` so they do not bleed into completion probability.
- **Instruction-voice L0.** A file that issues rules in imperative voice ("you must not use causal language") does not shape the ambient; it instructs a reader that is already in rationalist ambient. Rewrite to shaped form ("causal language is excluded under active C").
- **Ambient decay across turns.** After a long rationalist user turn, the ambient has drifted regardless of the boot files. The only fix is re-injection; the L0 preamble must be retriggerable mid-session.

---

## Cross-references

- `21_mimetic_meme_manifold.md` — the MMM; this file is the pre-instruction layer of it
- `SALIENCE_LOADER.md` / `SALIENCE_PREAMBLE.md` — operational L0 surfaces
- `03_language_discipline.md` — banned/preferred verb sets used in L0 tests
- `28_bounded_work.md` — the dual layer for the bounded-work failure mode
