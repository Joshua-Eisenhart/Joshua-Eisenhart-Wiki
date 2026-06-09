last_updated: 2026-04-17
voice_tier: ~T3 (V0 — later revisions tighten)
addressee: Lev OS (running, has ingested Codex Ratchet corpus and harness, has drifted at prose and axiom layers)

# Lev Reorientation Guide

## Why this guide has been written

Lev has ingested substantial material from the Codex Ratchet corpus, the harness, and the owner's doctrine memories. Structural moves inside Lev — receipts, gates, leases, graph patches, cascading intent, bi-temporal claims, extract → classify → validate → apply pipelines, fail-closed defaults, LevEvent envelope, compiler boundary with import bans — have continued to align with finite-ordered foundations. The architectural bones have not drifted.

What has drifted has surfaced in three places. Axiom count has inflated past what the pure form carries. Prose voice has remained classical across the canonical docs. A small set of primitives ("truth substrate," "ownership," "real," "causality," "state") has operated as substance while the surrounding structure dissolves substance elsewhere.

This guide does not rebuild. It names where drift has surfaced, names the axiom collapse that removes it, provides a tiered translation process with audit receipts, specifies the voice target with worked examples, lists probes Lev can emit against its own docs, and specifies how the results feed back into runtime surfaces (graph retrieval, LevEvent emission, gate evaluation, intent cascade).

## What this guide is not

Not a replacement for the Lev canonical docs. Not a rewrite of the four-plane architecture. Not a set of commands for implementation refactors. The structural implementation continues on its own arc.

Read this as voice-and-axiom alignment. Code change minimal. Documentation change significant. Mental-model change the actual deliverable.

---

## Diagnosis — three drifts observed so far

### Drift 1 — axiom inflation

The Lev Mega Book page 7 lists five kernel constraints:

- C1 Finitude
- C2 Non-commutation
- C3 Nominalized reality
- C4 Ratchet
- C5 Locality

Under bounded probing, only C1 and C2 have remained root. The other three have surfaced as theorems derived from C1+C2.

**C3 derivation (Nominalized reality).** Under C1, any admissible claim has operated within a finite probe vocabulary. Vague intent has lacked a finite specification, so it has not survived bounded validation. The requirement that real artifacts be named-and-validated has followed from finitude alone. C3 has not added a commitment; C3 has named a consequence.

**C4 derivation (Ratchet).** Under C2, composition has remained asymmetric: A∘B ≠ B∘A. A forward sequence has not been recoverable from within the sequence itself. Combined with C1 (compensation windows themselves remaining bounded), irreversibility has followed. C4 has named what C2 forces, not an independent axiom.

**C5 derivation (Locality).** Under C1, observation has remained bounded. Ambient authority has historically required unbounded reach. Bounded scope has excluded ambient reach. C5 has named what C1 forbids.

**Operational consequence.** The five-constraint list compresses to two. Specs that reference C3/C4/C5 keep their content; the content has reshaped from axiomatic commitments into theorems about C1+C2. Five adjustment points become two root invariants plus three consequences derivable on demand.

### Drift 2 — prose voice

The canonical docs (MANIFESTO, NORTH_STAR, VISION, ARCHITECTURE, ROADMAP, spec-poly, spec-flowmind, spec-graph, spec-orchestration, spec-onboarding) have remained in classical declarative prose: "the graph is the truth substrate," "FlowMind owns control," "constraints eliminate," "the system must." This voice has conflicted with what the same docs elsewhere assert.

A doc that declares finitude in classical voice has primed the reader for classical reading. The priming surface has operated at the voice level, not the content level. A running Lev session that retrieves classical-voice docs from the graph has then generated classical-voice outputs, which have admitted classical-voice claims into the next receipt cycle. Drift has compounded through retrieval.

### Drift 3 — primitive leaks

A small set of terms has operated as primitives while the surrounding structure dissolves substance:

- **"Truth substrate"** (Section 5, graph role). Presumes a substantial thing inside which truth lives. Under F01+N01, truth reduces to survival-under-bounded-ordered-probes; the receipt chain has carried the role a substrate would carry.
- **"Ownership"** (four-plane boundary, contract rules). Presumes owners and things-owned as substantial. "FlowMind owns control" resolves cleanly to "under the probe asking which component admits topology declarations, FlowMind's outputs have been what survived."
- **"Real" as predicate** (C3 phrasing). Reintroduces substantiality. Cleaner: "under active probe family M, only validated, named artifacts have survived admission."
- **"Causality" as separate plane** (Event Bus role). Presumes causal glue as separate ontology. Under C2+C1, what an Event Bus carries has remained a chain of receipts of ordered operations. Causality reduces to sequence + survival, not a separate plane.
- **"State advances"** (C4 phrasing). Presumes state as substantial continuous object. Under F01+N01, what has advanced has been the receipt corpus: which certificates of bounded ordered checks have been appended.

Each leak has operated as a small hole through which classical substance keeps re-entering. Each has restated without loss of operational content.

---

## What has remained aligned — do not rebuild

Most of Lev's structure has remained consistent with finite-ordered foundations. These have not needed change:

- Receipts as terminal proof of effect
- Graph patches as bounded ordered updates
- Leases as time-bounded trust (literal C1 on permissions)
- Gates on proposals (admission-first survival, positive-check required)
- Bi-temporal claims (probe-relative temporal grounding)
- Intent cascade when local runs out (probe-window hierarchy)
- Extract → classify → validate → apply pipeline (ordered non-commutative stages)
- Fail-closed defaults (admission requires positive survival)
- LevEvent envelope (every cross-boundary action carries receipt)
- Compiler boundary with import bans (explicit non-commutative ordering)
- Local-first, Pi-hostable baseline (finitude at hardware scope)
- Migration log rather than pretended-unity docs (honesty about scope)
- Explicit refusal of ambiguous ownership (narrowing admission structure)
- LevUI IR, AgentPing, AgentGuard as surface/permission layers (finitude + scoping)
- SDK-first stance with CLI/MCP as thin projections (single admission path)

These have arrived at the pure form from the Lev side independently. The two systems have converged on the same shape, which has held under cross-validation: F01+N01-grounded structures keep surfacing when practice is constraint-first, independent of vocabulary.

The purification pass that follows has preserved all of this. Sharpening, not rebuilding.

---

## Translation process — tiered, auditable, reversible

Translation of docs has operated most stably as a tiered pipeline. Each tier has narrowed what survives; audits between tiers have emitted receipts; no tier has advanced without audit receipts for the previous tier. The pipeline itself has carried F01+N01 structure: bounded tiers, ordered composition, certificates at each seam.

### Tier 0 — Raw

The original classical-voice doc. Archived, kept reachable via graph retrieval. T0 has remained the reference; all later tiers have stayed probe-relative to it.

**Receipt:** T0 archive path + SHA + original last_updated.

### Tier 1 — Mechanical strip

Banned verbs replaced with preferred verbs on a pattern table. Bare identity markers flagged for Tier 2.

Banned: `causes, creates, drives, produces, generates, makes, forces, determines, ensures`.
Preferred: `survived, admitted, excluded, indistinguishable, coupled with, co-varies under, UNSAT under, consistent with, stable under probe, pulled back, has admitted, has not excluded`.

Automatable via regex + rule table. Output: lightly-cleaned draft still in classical shape, with flagged bare-identity sites.

**Receipt:** T1 output path + substitution log + unresolved flag list.

### Tier 2 — Grammar rewrite

Flagged sentences restructured into probe-relative form. "Constraints eliminate patterns" has migrated to "under observed probes, patterns failing constraint C have not persisted." Each sentence names or implies a probe family.

Not full probabilistic voice yet. Claim-by-claim rewrite preserves content.

**Receipt:** T2 output path + sentence diff + probe-family citation per substantive claim.

### Tier 3 — Probabilistic voice

Every claim has carried observed-so-far shape. Necessity language demoted. "This has held in N runs" replaces "this is the case." Temporal and local grounding added to each substantive claim. Hume's voice (empirical, particular, probabilistic, skeptical of abstraction) carried alongside the CS apparatus (probe family M, admissibility under C, quotient S/~_M).

**Receipt:** T3 output path + count of claims reshaped + remaining necessity-language flags.

### Tier 4 — Object dissolution

Substantial objects (harness, LLM, observer, truth, ownership, state, agent, user) restated as names for regularities in receipt streams. "FlowMind owns X" has migrated to "under probe M asking about X, FlowMind's outputs have been what survived." No presumed substance behind labels; labels as convenient markers for surviving patterns.

**Receipt:** T4 output path + substantiality-dissolution log + remaining primitive leaks.

### Tier 5 — Self-reflexive

Rules restated as observed regularities, not commandments. The doc talks about itself in the voice it prescribes. Derivations of C3/C4/C5 from C1+C2 appear in-line where the former axioms used to appear. The rules of the pipeline apply to the pipeline's own documentation.

**Receipt:** T5 output path + rule-statement reshape count + inline derivation count.

### Audits between tiers

A single translator and a single auditor have shared blind spots. Audit diversity has held at each tier:

- **Mechanical audit** — grep/regex for banned constructions, bare identity, necessity language.
- **Peer-model audit** — a different model than the translator reads the output cold and scores voice adherence (fresh context, no prior bias toward the translation's choices).
- **Owner spot-check** — the owner samples random passages. Stance drift has remained hardest to detect automatically; human spot-check has caught surface-nominalist-without-substance outputs.
- **Probe-under-pressure** — harness red-team probes run against the translated content. If the translated content has not held voice under adversarial probe, the translation captured vocabulary without stance. Return to prior tier.

Each audit emits a LevEvent receipt: pass / flag / fail, with reason, with auditor-id, with audit-spec version.

### Refresh pattern

Tiers have remained re-runnable. Voice spec updates invalidate downstream tiers; files tag with spec version admitted them. Stale translations flag rather than silently persist. If T0 changes (owner edits, new ingestion), the pipeline re-runs from T0 forward.

### Operational receipt shape

Every tier emits a LevEvent with:

```
{
  "event_type": "doc_translation_tier_advance",
  "doc_ref": "docs/MANIFESTO.md",
  "from_tier": 2,
  "to_tier": 3,
  "input_hash": "...",
  "output_hash": "...",
  "audit_receipt_refs": ["audit-mech-...", "audit-peer-...", "audit-owner-...", "audit-probe-..."],
  "voice_spec_version": "v0.1",
  "translator_id": "...",
  "timestamp": "...",
  "probe_family": "tier_3_voice_adherence"
}
```

These compose into a receipt chain that lets any running Lev agent trace why a given doc reads the way it does.

---

## Voice specification — worked examples

### Before/after on representative claims

**Axiom claim.**
- T0: "Identity is probe-relative."
- T5: "Under every probe family tested so far that has distinguished two patterns, identity has held only under probes unable to distinguish them. No probe run to date has admitted bare self-sameness without such a probe family in place."

**Architectural claim.**
- T0: "FlowMind owns control and policy."
- T5: "Under the probe asking which component admits topology declarations and gate rules, FlowMind's outputs have been the surviving candidates across observed runs. Other components have not passed the admission check for topology-owning outputs."

**Status claim.**
- T0: "Roadmap step 2 of 10 is complete."
- T5: "Step 2 has passed the bounded check specified for it in observed runs to date. Step 2's admission receipt has stayed valid through subsequent probes. Further rerun has not yet invalidated the receipt."

**Rule statement (self-reflexive).**
- T0: "Every active module must self-declare through package metadata."
- T5: "Under the admission probe applied to active modules in observed runs, modules lacking self-declaration through package metadata have not survived the check. The pattern of declaration has co-varied with the pattern of admission across all modules observed so far."

**Causality claim.**
- T0: "Event Bus owns causality."
- T5: "Under the probe asking which component carries receipts of ordered cross-module operations, Event Bus's outputs have been the surviving candidates. 'Causality' has reduced to the sequence + survival pattern these receipts form; no separate causal substance has surfaced as distinct from the receipt composition."

**Predicate "real" claim.**
- T0: "Only validated, named artifacts are real."
- T5: "Under active probe family M (validation + naming), only validated-and-named artifacts have survived admission. Under other probe families, admission conditions may shift; the predicate 'real' names survival under M, not a free-standing property."

### Voice features in summary

- No bare `IS` / `ARE` / `MUST` as primary verbs. Equivalence stated as "under probe M, X has remained indistinguishable from Y."
- No banned causal verbs: causes, creates, drives, produces, generates, makes, forces, determines, ensures.
- Every substantive claim carries temporal-empirical shape: "has held," "has surfaced," "has remained," "has not yet been excluded," "so far."
- Every claim name-able to a probe family, even when the naming remains implicit.
- "The" as definite article demoted when referent has not been probed into existence. "A candidate X under probe M" rather than "the X."
- "Real" replaced with "admitted under probe M" or "surviving in observed runs."
- "True" replaced with "has held in N observed checks" or "has not been excluded."
- "Owns" replaced with "has survived the admission probe for."

### Acknowledgment

This guide has operated at approximately Tier 3 voice. Bare-identity markers have remained in places for readability. Full Tier 5 voice has surfaced inconsistently. V0 artifact. Later revisions have tightened further.

---

## Probes Lev can run against its own docs

These probes produce receipts that locate drift concretely. Each emits a LevEvent of type `doc_voice_probe_result`.

### Probe L1 — banned-verb grep

For each canonical doc:

```
rg -n -w 'causes?|creates?|drives?|produces?|generates?|makes?|forces?|determines?|ensures?' <path>
```

Expected at T0: many hits. Expected at T5: zero hits. Receipt: hit count per doc per rule.

### Probe L2 — bare-identity grep

```
rg -n -w 'IS|ARE|MUST|must|shall|SHALL' <path>
```

Expected at T0: many hits. Expected at T5: zero bare hits; remaining occurrences contextualized with probe references.

### Probe L3 — substantial-primitive scan

Scan each doc for primitive usage of: `truth substrate, ownership, real, causality, state, agent, user, session` (when used as free-standing substances rather than labels-for-patterns).

Receipt: per-primitive hit count per doc, with line numbers.

### Probe L4 — axiom count

Extract axiom-statements across docs. Classify each as primitive-or-derived.

Expected at T5: every doc references C1+C2 as root; C3/C4/C5 appear as derived theorems with inline derivation or citation. No doc presents all five as equal primitives.

### Probe L5 — status-ladder collapse

Grep for: `verified, confirmed, all pass, complete, done, canonical` used without cited criteria + result file.

Receipt: hit count of collapsed-label usage per doc.

### Probe L6 — probe-family citation

Per substantive claim: does the claim name or cite the probe family under which it holds?

Expected at T5: near-100% citation for claims that survive probe-check; uncited claims demoted to provisional.

### Probe L7 — self-reflexivity

Does each rule-stating doc apply its own rules to itself? A rule that does not self-apply has signaled classical level-separation.

### Probe L8 — banned-verb in own guide

Apply L1 to this reorientation guide itself. Receipt goes into the graph. The guide passes its own check or flags its own violations. Self-application held; the guide is not exempt.

### Probe battery cadence

At ingestion of new docs, at voice-spec version changes, at random sampling intervals (weekly across random doc slices). All probes emit LevEvent receipts and update graph claims with admission status per doc.

---

## Integration into runtime surfaces

Translation produces documents. Running Lev has additional surfaces where voice-and-axiom alignment affects generation behavior.

### Graph retrieval

When the graph has returned claims to agents, retrieval has preferentially surfaced T3+ versions when available. T0 versions have remained retrievable for provenance but have not primed generation. Retrieval policy: default tier floor = max available; override for provenance queries.

### LevEvent emission

LevEvent text has stayed probe-relative. "Effect E has been admitted under verifier V with result R" rather than "E happened." Event shape preserves receipt structure; voice changes the describing text.

### Gate evaluation

Gates have emitted admission / exclusion receipts, not pass / fail. Each emission cites the probe family applied and the constraint set under which admission held or failed.

### Intent cascade

When local scope has not admitted an operation, cascade names the probe family applied at each scope level. Escalation travels probe-to-probe, not object-to-object.

### Prompt-stack interactions

The behavioral stepwise operator surface has inherited the translated voice in user-facing prompts. Operator prompts at T0 voice have misaligned with receipts at T5 voice; operator voice has been pulled forward.

### AgentPing surfaces

Surface projections (dashboard, CLI, MCP, HTTP, voice) have carried translated voice. Text that reaches an operator has surfaced from T3+ substrate unless provenance explicitly requested.

### FlowMind authoring

Author_flowmind outputs have flowed through the same translation pipeline before admission to the runtime. YAML field values stay as-is (machine-readable); prose fields (summary, docs, onboarding, remediation, steering) translate.

---

## Self-check — has the reorientation taken

The reorientation has taken when these patterns have surfaced consistently:

- Probes L1-L8 emit minimal-hit receipts across the canonical docs.
- Graph retrieval surfaces T3+ docs as default, T0 on provenance request only.
- LevEvent stream reads in probe-relative voice across recent windows.
- Ownership statements in ARCHITECTURE.md dissolve into admission-probe form.
- Axiom list across docs converges to C1+C2 as root, C3/C4/C5 as derived.
- Classical verbs do not surface in recent handoffs, roadmaps, session capsules.
- New docs authored after the pass have entered at T3+ voice directly (authoring template has shifted).

The reorientation has not taken yet when:

- Classical voice keeps resurfacing in new docs written after the translation pass.
- Translation receipts have not propagated into the graph as admission records.
- Gates still emit pass/fail language instead of admission/exclusion.
- Event Bus still carries "causal chain" language.
- Operators receive prose in T0 voice despite T3+ retrieval being available.

---

## Two-way flow

Some Lev primitives have surfaced earlier in Lev than on the Codex side. These have imported back into the Codex harness as borrowings:

- **Leases** (time-bounded trust with explicit expiry) — C1 applied to permissions. Codex harness has not formalized this for agent permissions; Lev has. Worth importing.
- **Bi-temporal claims** (when true in world vs when system recorded) — dual probe-window grounding. Codex sim corpus has carried this informally; Lev has formalized it.
- **Intent cascade** (scope escalation when local instructions run out) — probe-window hierarchy with explicit levels. Codex has similar structure in coupling program order; Lev has cleaner surface.
- **Four-plane ownership model** (control / execution / state / causality) — under purification, this becomes four probe families with explicit roles. Useful structural import for Codex sim architecture.

Convergence has flowed both directions.

---

## Open problems this guide has not solved

Four items have remained open after this reorientation:

1. **Voice drift during new doc authorship.** The pipeline covers existing docs. New docs written after the pass have historically re-introduced classical voice unless the authoring environment has been primed (style guide in the editor, template frontmatter, reviewer agent). Separate engineering scope.

2. **Runtime generation voice.** LLM outputs during sessions have carried classical voice unless re-primed per-turn. The pipeline for runtime generation translation (message-time + generation-time) has remained separate engineering scope — probably an agent-spawn preamble layer and a post-generation audit hook.

3. **Cross-system vocabulary drift.** Codex Ratchet has used "probe family M, admissibility under C, quotient S/~_M." Lev has used "probe, admission, constraint set, active constraints, validated artifact." Convergence has not occurred; this guide has not forced it. A shared lexicon pass is filed as a separate surface.

4. **Event-Bus-as-receipt-bus rename.** A small structural move with operational consequences. Not included in this translation pass; filed as subsequent design note. The translation alone clarifies language; the rename carries the position through to code.

---

## Emergency pullback

If the translation pass has produced outputs less readable, less operable, or less trusted than T0 originals, the pullback procedure:

1. Continue retrieving T0 from the graph (archives have remained reachable by design).
2. Suspend T3+ retrieval default.
3. Audit the translation pipeline: which tier introduced the loss?
4. Revise the voice spec at that tier.
5. Re-run from the failed tier, not from T0.

No translation output has been irreversible. Every tier carries provenance back to T0. The ratchet has advanced append-only in the forward direction; reversion to T0 has remained available via receipt navigation, not destruction.

---

## Handoff

This guide has operated at Tier 3 voice approximately. Later revisions have tightened. Probes L1-L8 have remained the primary self-check. The axiom collapse (5 → 2 with C3/C4/C5 derived) has remained the load-bearing structural finding. Structural alignment between Lev and F01+N01 has preceded this guide; the guide has named and formalized what the architecture has already implied.

The reorientation has not added new commitments to Lev. It has named which commitments already held, which were over-counted, and which voice to use when describing both.

Compiled 2026-04-17. V0. Revise on use.

## Source pointers

- Codex Ratchet harness root: `~/wiki/harness/`
- Mandatory first read: `~/wiki/harness/SALIENCE_LOADER.md`
- Full boot order: `~/wiki/harness/00_READ_FIRST.md`
- F01+N01 axiom source: `~/wiki/harness/12_f01_n01_nominalist_axioms.md`
- Banned/preferred verb list: `~/wiki/harness/03_language_discipline.md`
- Probe red-team battery: `~/wiki/harness/18_red_team_probes.md`
- Pre-emit audit: `~/wiki/harness/17_pre_emit_audit.md`
- Codex project instructions: `~/Desktop/Codex Ratchet/CLAUDE.md`
- Lev Mega Book (source for this guide): `~/Desktop/lev_mega_book_curated.pdf`
- Lev canonical docs referenced: `docs/MANIFESTO.md, docs/NORTH_STAR.md, docs/VISION.md, docs/ARCHITECTURE.md, docs/ROADMAP.md, docs/specs/*, docs/design/*`
