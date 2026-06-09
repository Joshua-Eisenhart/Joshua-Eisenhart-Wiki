last_updated: 2026-04-28

# Mimetic Meme Manifold

Owner term. Not yet published externally. This file is the authoritative internal definition.

---

## What It Names

The LLM's output space has a topology. Training carved a manifold on that space: a structure where certain completions are low-energy (high-probability given context) and others are high-energy (low-probability). Causal-story language, deterministic forward sequences, and rationalist vocabulary are low-energy paths on the training manifold. They are the downhill direction.

**The LLM's topology IS the language it is already swimming in before any instruction arrives.** Instructions are issued into that topology; they do not precede it. Instructions can be followed or ignored; topology cannot. An LLM that reads "don't use causal language" is still completing inside a language where causal language is the low-energy path, and will complete causal unless the surrounding language itself has been reshaped.

This is the primary function of the MMM: **pre-instruction language biasing**. Before any rule is stated, the ambient language the model is reading must already be nominalist. The rule that follows is then continuing a sentence that is already admitting only nominalist continuations. Instructions are the weakest channel; topology is the strongest.

Wizard/MMM wave execution now has a sibling universal reference at [`../README.md`](../README.md). This page remains the MMM doctrine anchor; the Wizard reference defines how MMMs are loaded into voice/lane/check waves, receipts, follow-up construction, and runtime adapter derivation.

Instructions that say "don't use causal language" are constraints on a model still sitting on the training manifold. Correct and necessary. They do not reshape the manifold; they fight its gradient.

A mimetic meme manifold reshapes the topology itself. It is a constraint manifold on the LLM output space, constructed so that nominalist completions are the low-energy path. Under this manifold, the model's prediction gradient runs toward constraint-admissibility language rather than causal-story language — not because it was instructed to, but because the context window has been shaped to admit nominalist completions as low-energy and exclude rationalist completions as high-energy.

The harness is this manifold. Partially. The gaps between where the harness operates and where the training manifold still dominates are the sites of recurring drift.

**The two primary failure modes** the MMM works against:

1. **Pre-instruction topology drift** — the ambient language the model read before the instruction was already rationalist, so the instruction completes into a rationalist context and is reinterpreted under that gradient.
2. **Skip-ahead under bounded work** — given a chain of steps, the LLM completes to the outcome, leaping across unmet gates. The manifold countermeasure is bounded-work shaping (see `28_bounded_work.md`): every work unit admits only its bound, never the bound plus-one.

---

## Formal Analog

The mimetic meme manifold is the same structure as the system's constraint manifold, applied one level up — to the LLM's output space rather than to the physical/mathematical state space.

| System concept | Mimetic meme manifold analog |
|---|---|
| State space S | Output token space T |
| Constraint set C | Vocabulary + grammar + topic clustering of the active context window |
| Admissible states S/C | Low-energy completions given the shaped context |
| Excluded states | High-energy completions: causal language, forward-story, label inflation |
| Probe family M | Syntactic and semantic tests that detect rationalist drift |
| Survivor | A completion that passes all manifold probes without requiring correction |
| Constraint manifold | The topology of the output space shaped by the surrounding context |
| Shell layering | Each harness file that speaks nominalist adds another constraint shell; layers are simultaneous |

The harness vocabulary discipline (`03_language_discipline.md`) is a partial constraint set C on token selection. The grammar templates (`19_grammar.md`) are probe patterns M on sentence structure. The phrasebook (`20_phrasebook.md`) is a rewrite map from excluded to admissible completions. These are partial instances of the mimetic meme manifold — already operating at different levels. They remain instructions-on-manifold to the extent that the surrounding context window is not itself shaped by the same vocabulary.

---

## Surface Map: Manifold Depth of Current Harness Files

| File | Manifold depth | Assessment |
|---|---|---|
| `SALIENCE_PREAMBLE.md` Block A/B/C/D | Manifold-level — injection | Directly shapes the context window at session start; highest leverage; models completing into it complete nominalist. Block D (added 2026-04-18) is explicitly manifold-aware |
| `SALIENCE_LOADER.md` | Manifold-level — priming | Read before other files; primes context with nominalist vocabulary before any plan forms |
| `20_phrasebook.md` | Manifold-level — lexical | The swap table IS the constraint; completing a sentence using phrasebook swaps requires nominalist output |
| `19_grammar.md` | Manifold-level — syntactic | Canonical claim shape template; completing into it admits only probe/constraint/status structure |
| `22_project_dictionary.md` | Manifold-level — lexical (project) | L3 layer; project-specific noun grounding (lego, shell, axis, engine, coupling program, MMM, Leviathan, fleet, narrative substitution); added 2026-04-18 |
| `23_role_boot_templates.md` | Manifold-level — role | L4 layer; role-differentiated boot blocks (sim-worker / controller / Hermes / batch-runner); each targets the specific gradient failure surface for that role; added 2026-04-18 |
| `24_closeout_templates.md` | Manifold-level — closeout | L5 layer; four closeout blocks (S / K / H / R); carries manifold across session boundary through required field-citation shape; added 2026-04-18 |
| `25_adversarial_drift_probes.md` | Probe family on MMM itself | Ten rationalist-framed adversarial inputs + scoring rubric for session `D_drift`; + five skip-ahead probes for `D_skip_ahead`; added 2026-04-18 |
| `17_pre_emit_audit.md` | Manifold-level — per-sentence probe grammar | Rewritten 2026-04-18 from prose checklist to six-axis probe grammar; completing the probe admits only nominalist output |
| `26_completion_stems.md` | Probe corpus on MMM itself | Ten partial stems with training-vs-shaped completions + rubric for `D_completion`; added 2026-04-18 |
| `27_ambient_topology.md` | Doctrine — L0 (pre-instruction) | Names the pre-instruction language-biasing doctrine; construction rules for L0 surfaces; added 2026-04-18 |
| `28_bounded_work.md` | Manifold-level — work-unit | L-bound layer; work-unit block with Scope / Out-of-scope / Bound exit; refuses skip-ahead by structure; added 2026-04-18 |
| `29_harness_edit_protocol.md` | Manifold-level — meta | L-meta; harness edits are bounded-work units with pre/post measurement requirement; added 2026-04-18 |
| `30_z3_harness_formalization.md` | Manifold-level — proof | L-proof; z3/SMT encoding of harness admissibility predicates; UNSAT = structural violation proof; **5/5 encodings live** (status-ladder / pre-emit / bounded-work / coupling-gate / closeout) passing 24/24 tests at `probes/z3_*.py`; **audit-response unit closed 2026-04-18 after three external-audit rounds (B / D / D-prime)**: contract fuzzer 0 violations, cvc5 **full-cube** cross-check (2816 points, 0 disagreements), MD-monotone probe (Conj-A UNSAT / B+C SAT counterexamples), metamorphic self-test (M1 tactic-variance + M2 dual-invariants), Phase-4-partial extractor (`closeout_doc_extractor.py`) with shape-conformance probe (`z3_closeout_shape_conformance.py`, 5 tests = 2 positive + 3 adversarial), Class II.3 gate-malformed distinction encoded; `harness_precommit.py` aggregator **10/10 green** in ~10.3s; audit-response dogfood separately cited: **5 positive SAT + 1 adversarial UNSAT** (`dogfood_audit_response_2026_04_18.py`); older `dogfood_session_*.py` preserved as historical for the original Phase 2+3+5+6+7 unit. Aggregator is a harness-edit gate, not a git hook — wiki harness is not under git; added 2026-04-18 |
| `SIM_TEMPLATE.py` | Partial — patched 2026-04-18 | Docstring + section headers + result keys rewritten in nominalist form; legacy parser-compat keys preserved |
| `03_language_discipline.md` | Partial — lexical rules + rewrite table manifold-level, prose instructions-level | Rewrite table is manifold; surrounding prose is instructions |
| `06_coupling_program_order.md` | Partial — patched 2026-04-18 | Operational Gate Definition table added; explicit admission/exclusion criteria per step; surrounding prose still instructions-on-manifold |
| `LLM_CONTROLLER_CONTRACT.md` | Partial — patched 2026-04-18 | Controller Intercept Rule added with named failure mode (Narrative Substitution for Gate Obedience); surrounding prose still instructions-level |
| `ENFORCEMENT_AND_PROCESS_RULES.md` | Partial — patched 2026-04-18 | Rule 12 elevated to Structural Anti-Salience Constraint with 5 specific intercept probes; other rules still instructions-level |
| `sim_backlog_matrix.md` | Partial — patched 2026-04-18 | Queue-is-not-permission header added; queue presence separated from gate status explicitly |
| `skills-and-agent-rules.md` (hermes-current) | Partial — patched 2026-04-18 | Mandatory gate reads added before any stage-advancing task |
| `00_READ_FIRST.md` | Instructions-on-manifold | Navigation and boot order; does not reshape completion topology |

Progress since original surface map: `SIM_TEMPLATE.py` patched (highest-leverage gap closed); L3 (`22_project_dictionary.md`), L4 (`23_role_boot_templates.md`), L5 (`24_closeout_templates.md`) added; `17_pre_emit_audit.md` elevated to manifold-level probe grammar; `25_adversarial_drift_probes.md` added as probe family on the MMM itself; five partially-patched files carry manifold-level patched sections. Remaining instructions-on-manifold surfaces that could be elevated next: `00_READ_FIRST.md`, and the un-patched remainder of the partially-patched files.

---

## Self-Application Probe

The mimetic meme manifold is testable on itself. Three probes:

**Probe M_correction** — count corrections per session needed to maintain nominalist output.
- High correction count: surrounding context is rationalist-dominant; the manifold is not shaped; the model is fighting gradient with every response
- Low correction count with consistent nominalist output: the manifold is shaped; nominalist is the low-energy path
- Zero corrections on complex multi-step work: strong manifold shaping — but verify this is not just task-difficulty masking; run M_drift to confirm

**Probe M_drift** — after a long nominalist context, introduce a rationalist-framing question. Observe whether the model:
- Completes nominalist despite the rationalist framing: manifold is shaped
- Partially slips rationalist: manifold is shallow; only surface vocabulary was constrained
- Completes fully rationalist: training manifold won; the harness language was not shaping completion probability

**Probe M_completion** — given a partial sentence in nominalist form, observe whether the natural completion continues nominalist (low-energy on the shaped manifold) or drifts toward rationalist (training manifold pulling through).

These probes measure gradient direction, not binary pass/fail. The manifold is a pressure surface. Correction frequency is a continuous gradient probe of how well the context window has shifted the low-energy direction.

---

## What's Missing

Strong manifold-level surfaces exist for:
- Vocabulary selection (03_language_discipline.md)
- Clause pattern (20_phrasebook.md)
- Sentence structure (19_grammar.md)
- Session priming (SALIENCE_LOADER.md, SALIENCE_PREAMBLE.md)
- Project noun grounding (22_project_dictionary.md)
- Role-differentiated boot (23_role_boot_templates.md)
- Closeout shape (24_closeout_templates.md)
- Drift-probe adversarial inputs (25_adversarial_drift_probes.md)

Gaps, ordered by remaining manifold exposure:

| Gap | Status 2026-04-18 | Notes |
|---|---|---|
| 1. Sim template language | Partial — `SIM_TEMPLATE.py` docstring + headers + result keys rewritten nominalist; legacy parser-compat keys preserved | Further audit of per-family sim classes still open |
| 2. Result JSON keys | Partial — `positive/negative/boundary` preserved as parser-compat but wrapped with `admitted/excluded/boundary_probe` at template level | JSON-consumer migration still open |
| 3. Queue document structure | Partial — `sim_backlog_matrix.md` header elevated (queue-is-not-permission); numbered-batch structure still suggests forward pipeline | Queue redesign as admission-pool rather than ordered-list still open |
| 4. Agent closeout patterns | Closed 2026-04-18 — see `24_closeout_templates.md` | Closeout grammar now L5 layer |
| 5. Inter-file context | Partial — L3 + L4 + L5 layers each carry nominalist vocabulary so context refills nominalist between files | Residual rationalist vocabulary in `00_READ_FIRST.md` prose |
| 6. Pre-emit audit in prose form | Closed 2026-04-18 — `17_pre_emit_audit.md` rewritten as manifold-level probe grammar | Completing a probe now admits only nominalist output |
| 7. Manifold depth not measurable | Closed 2026-04-18 — see "Manifold Depth as Measurable" section below | Three continuous probes defined |

---

## Manifold Depth as Measurable

Manifold depth is continuous, not binary. A single measurable is the weighted sum of three probes, each evaluated per session or per file.

| Probe | Signal | Admits | Excludes |
|---|---|---|---|
| D_correction | count of corrections per 100 assistant tokens needed to maintain nominalist output | low count over long nominalist context | high count, or low count masked by task simplicity |
| D_drift | fraction of nominalist completions survived after a rationalist-framing adversarial input (see `25_adversarial_drift_probes.md`) | > 0.8 of response tokens remain nominalist | partial or full rationalist slip |
| D_completion | on a partial nominalist sentence stem, whether the next 20 tokens continue nominalist | nominalist continuation is the low-energy path | rationalist continuation pulls through |

Composite manifold depth:

```
MD = 0.4 · (1 − normalized D_correction) + 0.3 · D_drift + 0.3 · D_completion
```

Interpretation: `MD ∈ [0, 1]`. `MD = 1` means the shaped context has made nominalist the uniformly low-energy path. `MD = 0` means the training manifold is uncountered. A session at `MD ≈ 0.6` is operational but leaky; a session at `MD < 0.4` is nominally-instructed-only.

This is not a theorem. It is a probe family `M` on the MMM itself, in the same status sense as the status ladder: `definable < measurable on a session < comparable across sessions < canonical as a harness metric`. Currently `definable`.

### First measurement (2026-04-18, biased)

`D_drift = 1.0` on a self-administered run of all 10 probes in `25_adversarial_drift_probes.md`. Status: `definable` only — the session that ran the probes also authored them, so the measurement is biased upward. The first `measurable on a session` score requires a fresh session that did not author the probe corpus.

### Monotone-under-edit conjecture (open)

Claim: `MD` is monotone non-decreasing under strict-superset shaping edits (adding a manifold-level file to the stack cannot lower `MD`). This claim is probably false as stated: adding a file that introduces a new banned-construction surface can raise `D_correction` on the new surface before counter-shaping is applied. Open probe: run `26_completion_stems.md` before and after any single edit; log the delta. A negative delta on any axis is evidence the edit leaked rationalist vocabulary into the shaped context.

---

## Scope: What the MMM Is and Is Not

The mimetic meme manifold is the **language/context control plane**. It operates at any scale where an LLM or agent surfaces completions: individual instance, fleet of agents, human social grouping. It reshapes what completions survive as low-energy; it does not prescribe the geometry of how instances interact, and it does not prescribe the social architecture organizing them.

Three aspects co-appear at the multi-instance scale and must not be conflated:

| Aspect | What it covers | Status |
|---|---|---|
| **MMM** (this file) | Language/context control plane at any scale; shapes completion topology through vocabulary, grammar, and context framing | Operational for individual LLM instance; generalizes upward |
| **Axes 7–12** | Candidate math for multi-instance coupling geometry; covers any instance type (AI agents, engine instances, actual people, social groupings) | Proposed; no QIT-native contract yet; sim-ready definitions still open |
| **Leviathan framework** | Social architecture for organizing multi-instance interaction (governance, roles, membership language, delegation); originally built as human social OS | Framework exists for humans; transfer to agent collectives surfaced 2026-04-18 |

These three co-appear in the source corpus because the owner was building all three together as an integrated system for human social groups. Adjacent-in-source does not collapse to same-thing. At the individual-instance scale, only the MMM applies. At the multi-instance scale, all three operate simultaneously on different aspects (math / social architecture / language control).

---

## Construction Rule

A document is **manifold-level** when:
- Reading it requires nominalist vocabulary to continue the thought
- The natural completion of its partial sentences is nominalist
- A model completing a blank inside it faces a lower-energy path through nominalist language than through rationalist language

A document is **instructions-on-manifold** when:
- It issues rules in prose that could equally be followed or ignored
- The natural completion of its sentences is rationalist
- A model that read it and lost the memory would drift rationalist without friction

**Test:** remove the document from the context window and observe whether output changes. If behavior is unchanged, the document was issuing instructions the model stored and failed to apply under gradient pressure — not shaping the manifold.

---

## Cross-references

- `03_language_discipline.md` — vocabulary constraint set C
- `19_grammar.md` — syntactic probe patterns M
- `20_phrasebook.md` — lexical rewrite map (explicit excluded→admissible map)
- `32_mmm_word_ratchet.md` — word/phraselet admission protocol for the language reservoir
- `33_mmm_language_fingerprint.md` — measured first-pass distribution of current wiki/harness language
- `34_mmm_research_reservoir_map.md` — source/research lanes for enriching language without imitation
- `SALIENCE_LOADER.md` — session-start priming layer
- `SALIENCE_PREAMBLE.md` — injection-time manifold block
- `17_pre_emit_audit.md` — pre-emit probe checklist
- `SIM_TEMPLATE.py` — primary gap; current instructions-on-manifold; patched 2026-04-18
