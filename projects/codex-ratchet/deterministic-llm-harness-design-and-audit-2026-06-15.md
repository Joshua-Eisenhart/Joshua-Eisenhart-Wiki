---
title: Deterministic LLM Harness — Design + Audit (2026-06-15)
created: 2026-06-15
updated: 2026-06-15
type: project
status: design doctrine + verified audit; NOT a built harness
claim_ceiling: exists (doctrine + verified facts). No harness admitted; promotion requires the built+tested llm_harness with passing offline+online runs.
sources:
  - Hermes harness audit (2026-06-15, owner-relayed) — the original recommendation, reproduced + checked below
  - first-hand session reads: scripts/wizard_child_matrix.py, scripts/adaptive_controller.py, system_v5/grok_sim/loop_runner/multi_model_loop.py, scripts/codex_harness_adapter.py, the v7 gate stack
  - levos candidate flow: ratchet_sim_eval_three_engine.flow.yaml (the prune-pipeline stage spec)
tags: [codex-ratchet, harness, deterministic, receipts, inverted-tree, multi-model]
---

# Deterministic LLM Harness — Design + Audit (2026-06-15)

## Bottom line

Hermes recommended adding a small reusable Python harness (`scripts/llm_harness/`) that runs models →
captures real receipts → runs tests/gates → hands verified receipts to Wizard/Codex. **The recommendation
is sound and its facts are verified (below). Do it — but frame it correctly:** the harness is the
engineering of the inverted-tree's **prune / selection** layer. "Deterministic" applies to the
selection (schema, gates, test commands, artifact hashes, accept/reject), NOT to the model outputs
(which are non-deterministic by design — variation is a feature). Four sharpenings turn Hermes'
greenfield design into the right plan: (1) name the determinism as the prune; (2) reconcile the
receipt schema with the existing family + implement the existing candidate-flow stages, don't invent;
(3) wire to the existing `adaptive_controller` (the deterministic prune brain already exists) and treat
migration-out-of-the-monolith as the real work; (4) the audit wave must be multi-model (single-model
method-diverse audit advances but does not close box viii).

## Verified facts (checked this session, not trusted)

| Hermes claim | check | result |
|---|---|---|
| 7 named harness scripts exist | `ls` + `wc -l` | TRUE — all present |
| they compile | `py_compile` ×6 | TRUE — all OK |
| `scripts/llm_harness/` does not exist | `ls -d` | TRUE — absent |
| `wizard_child_matrix.py` is monolithic | line count | TRUE — **2028 lines** (run_wizard_system 1566, codex_harness_adapter 1163, wizard_behavior_harness 416, multi_model_loop 529, claude_terminal_bridge 141) |
| the 3 cited tests pass (65) | `pytest -q` | TRUE — **65 passed in 1.06s** |
| no canonical model-run receipt schema | grep `"schema": "codex_ratchet.*"` | TRUE — 16 schemas exist (sim_result.v1, engine_leg_result.v1/2/3, agreement_result, a2_state_manifest, …) but **no `llm_run_receipt`** |

Not re-checked (trusted from Hermes, low load-bearing): the exact "7 passed" guard count and the
provider-liveness pings (grok-4.3 / gemini CLI / openrouter fusion).

## The gap (real)

The repo has launchers (`wizard_child_matrix`, `multi_model_loop`, `claude_terminal_bridge`), receipt
compilers (`run_wizard_system`), shape validators (`codex_harness_adapter`, `wizard_behavior_harness`),
the v7 gate stack, and the `.claude/` agent roles. What it lacks is **one canonical provider+execution+
receipt layer**. Model-execution code is scattered across the monolith (`wizard_child_matrix`: provider
calls + prompt building + route topology + receipt scoring + truth checks + Wizard topology all mixed)
and the old `multi_model_loop`. Hermes' diagnosis is accurate.

## The design (Hermes' skeleton — kept)

```text
scripts/llm_harness/
  types.py         canonical dataclasses: TaskSpec, ModelJob, ModelReceipt, GateResult, HarnessRun
  providers.py     thin wrappers: Codex/Claude/ClaudeTerminal/OpenRouter/Grok/Gemini/LocalTool — run jobs, write receipts, KNOW NOTHING of Wizard doctrine
  runner.py        subprocess + timeout + stdout/stderr capture + artifact hash + receipt write  (runtime truth begins here)
  gates.py         wrap existing validators: codex_harness_adapter, wizard_behavior_harness, validate_v7_admission, validate_wizard_worker_receipts, pytest/py_compile/sim validators
  orchestrator.py  finder wave -> builder wave -> verifier wave -> audit wave -> arbiter
  cli.py           python -m scripts.llm_harness.cli run task.yaml
```

Model roles (the project's actual policy, kept): Codex = sober builder/arbiter/reviewer; Claude =
orchestrator/fresh-audit/role-card executor; Grok/Gemini/OpenRouter = variation + defect finders;
hot/hallucinating models = mutation sources, never authorities; local tools = final mechanical
evidence. **No model accepts its own work.** Build order: canonical types → **fake providers**
(Success/Failure/Timeout/Malformed) → test receipt writing with no network → LocalToolProvider
(py_compile/pytest/validators) → CodexCLIProvider → OpenRouter/Grok/Gemini → Claude bridge LAST
(most brittle auth). This test-first-offline ordering is correct and is the deterministic-harness
discipline done right.

## The four sharpenings (what makes it the RIGHT plan)

### 1. "Deterministic" is the PRUNE, not the variation

LLM outputs are non-deterministic and the project WANTS that — hallucination is the variation source
(blind, "random force from the past"). What the harness makes deterministic + reproducible is the
**selection layer**: the receipt schema, the `prompt_sha256`, the gate stack, the test commands, the
artifact hashes, the accept/reject decision, the replay. So the harness is the engineering of the
inverted-tree's prune over a non-deterministic variation layer:

```text
non-deterministic VARIATION (model threads)  ->  DETERMINISTIC SELECTION (harness: schema + gates + tools + accept/reject)  ->  graveyard / survivor
```

This is the load-bearing reframe Hermes' design supports but does not name. Determinism = every model
run yields a canonical receipt and a reproducible gate verdict on the SAME inputs, even though the
model text differs each time.

### 2. Reconcile the receipt schema; implement the EXISTING flow stages — do not invent

There is schema sprawl (16 `codex_ratchet.*` schemas) but no model-run receipt. The new
`codex_ratchet.llm_run_receipt.v1` should be the ONE canonical model-run record that the existing
`sim_result` / `engine_leg_result` / `agreement_result` receipts sit downstream of, and it must carry
the project's mandatory fields: `classification` / `claim_ceiling` / `promotion_allowed` /
`formal_admission_allowed`, plus F01/N01 lineage where a downstream object is named. And the
orchestrator's waves should **implement the candidate-flow stages that already exist**
(`ratchet_sim_eval_three_engine.flow.yaml`), not invent new ones:

```text
support_probe -> bounded_micro_eval (1 pos / 1 neg / 1 boundary) -> typed_observation
  -> code_owned_scorer (divergence/controls/receipt) -> gateproof -> semantic_control (admit | reject | keep_scratch)
non-negotiables: engines evaluate, semantic_control admits; scratch_diagnostic does not promote; divergence is evidence not auto-failure
```

Map: finder wave -> bounded_micro_eval; verifier wave -> code_owned_scorer + gateproof; arbiter ->
semantic_control.

### 3. Wire to the existing controller; migration is the real work

The deterministic prune BRAIN already exists: `adaptive_controller.py` (zero-token triage → queue →
gate → graveyard, looping). The new `llm_harness` is the **execution / variation feeder** in front of
it, not a free-floating new layer:

```text
llm_harness (run models/tools -> canonical receipts)  ->  adaptive_controller (triage/queue/prune)  ->  gates + 3 engines + SMT (admissibility)  ->  graveyard / survivor
```

**The risk Hermes understates:** adding `scripts/llm_harness/` WITHOUT extracting the provider code out
of the 2028-line `wizard_child_matrix` monolith creates a FOURTH execution surface and makes the sprawl
worse. The hard, load-bearing work is the migration: pull the reusable provider calls into
`providers.py` and make `wizard_child_matrix` CALL it. "Demote legacy" only works if the new layer
actually absorbs the reusable parts. This is the step most likely to stall and should be planned, not
hand-waved.

### 4. The audit wave must be multi-model (box-viii lesson)

Per the 2026-06-15 box-viii finding: a single-model method-diverse audit ADVANCES but does NOT close
admission — a near-identical sim was caught rigged only by the full fleet after a single fresh auditor
passed it. So the orchestrator's audit wave must require codex2 + ≥2 finder models (grok/gemini/
openrouter) for any `accepted` ceiling; a single-model audit caps at `scratch_diagnostic`. Bake the
multi-model requirement into `gates.py`, not into prose.

## MVP ordering (the deterministic core first)

The deterministic, fully-offline-testable core is buildable before any model touches it:

```text
1. types.py + the llm_run_receipt.v1 schema (reconciled with the existing family)
2. fake providers (Success/Failure/Timeout/Malformed) + runner.py -> prove receipt writing, timeouts, artifact hashing with NO network
3. LocalToolProvider (py_compile / pytest / validate_v7_admission / json-schema) + gates.py wrapper -> prove the deterministic prune verdict
4. wire to adaptive_controller's queue + the candidate-flow stages
   --- everything above is deterministic and offline-testable ---
5. CodexCLIProvider, then OpenRouter/Grok/Gemini, then Claude bridge (brittle auth) LAST
6. EXTRACT the reusable provider code out of wizard_child_matrix into providers.py (the migration)
7. only then run real multi-model tasks; the audit wave is multi-model-mandatory
```

Steps 1-4 are the "deterministic harness" the research was after; steps 5-7 bolt the non-deterministic
variation on after the deterministic core is proven.

## Honest status + open questions

- **Status:** `exists` — verified audit + design doctrine. No harness is built; nothing is admitted.
  Promotion to `runs`/`passes local rerun` requires the offline core (steps 1-4) actually built and
  green, then the online providers.
- This doc is a SINGLE-AUTHOR assessment (Claude), grounded in verified facts + first-hand reads, NOT a
  fleet-reviewed design. Treat the four sharpenings as proposals to pressure-test, not settled.
- **Open:** (a) does `llm_run_receipt.v1` supersede or wrap the worker/matrix receipts, or sit beside
  them? (b) is the right MVP a NEW package, or first an extraction of `providers.py` from
  `wizard_child_matrix` with no new top-level package? (the extraction-first reading reduces the
  fourth-surface risk). (c) how does the harness's `semantic_control` verdict relate to the existing
  `adaptive_controller` stage-gate — one authority or two? Hold these; do not collapse.

## 2026-06-15 real-fleet review CORRECTION (7/7 non-Claude models via OpenRouter)

A real multi-model fleet (grok-4.3, gemini-3.5-flash, qwen3.7-max, kimi-k2.6, glm-5.1, deepseek-v3.2,
minimax-m3 — all responded) adversarially reviewed the plan above and INVERTED its ordering. The
sharpening #1-#4 above stand, but the build SEQUENCE is corrected:

- **CONVERGENT (3+ models): extract the monolith FIRST.** Wiring to `adaptive_controller` / locking
  the schema before extracting provider code out of the 2028-line `wizard_child_matrix.py` leaks
  implicit global state into the "deterministic" gates AND creates a parallel-system trap where
  harness and monolith diverge so the migration never lands. Move extraction to the FRONT (was L7).
- **CONVERGENT: determinism is asserted, not earned.** Construct it across two NON-substitutable
  layers: (a) canonicalize generated code (AST-parse/format) before hashing + semantic-equivalence
  (not raw-byte) test comparison (deepseek); (b) run every gate in a hermetic sandbox
  (`PYTHONHASHSEED=0`, mocked time/random, blocked network I/O) with the sandbox-config-hash embedded
  in the receipt (qwen). Need BOTH.
- **AXIOM-LEVEL (grok + minimax): schema-against-fakes violates `a=a iff a~b`.** Locking the schema
  before observing real output means the probe is not calibrated to the variation it discriminates.
  Derive `llm_run_receipt.v1` from the UNION of (i) the real interface surface (static-analysis dump
  of `wizard_child_matrix` + `adaptive_controller`) and (ii) an empirical corpus of 100+ real
  OpenRouter/codex response shapes (success/refusal/partial/malformed/rate-limited/tool-call/
  reasoning-split/error). Fakes CONFORM to that schema, they do not define it.
- **HELD divergences (do not collapse):** kimi's executor-as-notary FORGERY threat (split the
  executor from the receipt-builder; a disposable write-isolated sandbox streams append-only
  observations to a SEPARATE notary — threat model is adversarial forgery, not generic hygiene);
  refactor-first (architecture extraction) vs empirics-first (response corpus) are TWO distinct
  preflight tasks, not one "move it earlier."

**Corrected order:** extract-interface + observe-response-corpus (two preflights) -> DERIVE the
schema from the real surface -> build the determinism harness (canonicalization + hermetic sandbox +
executor/notary split) -> wire the controller -> real-provider runs. Do NOT lock the schema until
both the extracted interface and the response corpus exist.

## Verdict

Hermes is correct: the pieces exist, the canonical provider+receipt layer is missing, and a small
provider-based Python harness with canonical receipts is the right improvement — NOT a Wizard rewrite.
Build the deterministic offline core first (schema + fake providers + local-tool gate), wire it to the
existing controller + candidate-flow stages, make the audit wave multi-model, and treat extracting the
provider code out of the monolith as the load-bearing migration. The determinism lives in the prune,
not the model.
