---
title: Hermes Wizard v4.3 Native Loop Bridge
created: 2026-05-16
updated: 2026-06-13
type: runtime_design
runtime: hermes
status: current-adopted-partial
---

# Hermes Wizard v4.3 Native Loop Bridge

## Purpose

This note binds current Wizard v4.3 to Hermes without pretending that any legacy v4.2 runner is Hermes itself.

The goal is a working LLM-alignment tool:
- the wiki carries Josh's goal, language, thinking moves, research state, and evidence rules;
- Hermes loads that frame before acting;
- v4.3 object-preservation / maintenance is the current Wizard path for object-bearing or maintenance scope;
- legacy v4.2 loop/council mechanics are provenance only and must not be named as the current run target;
- external models such as Gemini and Grok are read-only pressure lanes unless they return durable receipts;
- no provider agreement, model confidence, or structural-green wiki probe promotes a claim by itself.

## Authority split

1. Current user request is highest.
2. `~/.hermes/HERMES.md` owns live Hermes control and scaffold rules.
3. `~/.hermes/SOUL.md` owns body voice and anti-collapse method.
4. `hermes-current/` is Hermes's low-entropy wiki front door.
5. This bridge maps current Wizard v4.3 concepts onto Hermes tools and receipts.
6. `wizard/packet-v4-2-current/` is legacy/provenance; it does not supply current Hermes law or a current run target.
7. Legacy Codex Ratchet v4.2 scripts are historical evidence only unless a task explicitly asks for legacy migration/audit.

## Native loop meaning

For Hermes, `wizard auto loop auto` means a finite bounded loop, not an unbounded self-improvement blob.

Each loop iteration must have:
- input hash or unique tick id;
- declared target cluster;
- allowed reads;
- forbidden writes;
- preflight verification;
- Decision -> Failure -> Follow-Up barriers;
- premortem and loophole findings mapped before any apply;
- route-truth check before output;
- one compiled move or one explicit block.

Wizard may generate next prompts or packets, pre-run scouts or audits on those candidates, and auto-run a generated next packet only when the packet is safe, admitted, in scope, and has an explicit finite cap. Generated-packet evidence remains candidate evidence until audited and admitted by the controller.

Stop when:
- the compiled objective is done;
- loop cap is reached;
- no artifact delta appears;
- the same blocker repeats without a smaller action;
- route truth cannot name receipts;
- a premortem finding remains unmapped;
- a wiki probe or schema/route check fails;
- the next task drifts away from the user's actual goal.

## v4.3 route mapping in Hermes

Every v4.3 parent, child, model, tool, cron, or follow-up route resolves to one Hermes action class:

- `controller_local` — useful synthesis only; not worker proof.
- `tool_run` — Hermes tool returned current output.
- `spawn_worker` — delegate/external model/CLI worker returned a durable receipt.
- `enqueue_runner` — cron/background/process route was scheduled or checked.
- `blocked` — concrete blocker named.
- `deferred` — admissible later, intentionally not run now.
- `not_run` — considered but not attempted.
- `superseded` — replaced by fresher receipt.

Do not call controller synthesis a child. Do not call a tool check a subagent. Do not call a Codex script output Hermes-native proof unless Hermes launched it and verified its artifacts.

Top-level loop output must show decision-relevant skipped routes as `not_run`; a route that was intentionally unattempted or skipped cannot silently disappear when it affects the compiled move, FULL/PARTIAL/BLOCKED status, or follow-up choice.

## External model pressure

External models are useful for premortem, falsifier, alternate-frame, and loophole pressure.

Recognized advisory pools:
- Gemini;
- Grok / xAI when an executable or configured provider route is actually available;
- Claude Opus/Sonnet/Haiku;
- Codex read-only sandbox;
- Hermes controller synthesis.

Required receipt fields:
- provider/model or executable;
- route id;
- prompt hash or prompt path;
- read-only scope;
- status/exit code;
- artifact path or captured output;
- conclusion;
- authority boundary.

Provider agreement does not promote wiki truth, repo truth, sim readiness, or Wizard FULL status.

## Premortem join gate

Every substantive Hermes v4.3 loop/tick needs premortem findings mapped before Follow-Up renders options.

Allowed dispositions:
- `out_of_scope`;
- `stop_condition`;
- `required_hardening`;
- `dismissed_by_artifact`.

If any finding is `required_hardening`, the compiled move is `harden_then_execute`, not `pass_to_execution`.
If any finding is `stop_condition`, it must appear in the compiled move and visible follow-up option.
If premortem did not run, the run is PARTIAL or BLOCKED.

## Wiki alignment receipt

For wiki-as-LLM-alignment work, each applied tranche should leave a compact matrix in the log or tick receipt:

| Field | Meaning |
|---|---|
| file | touched or audited surface |
| role | front door, router, doctrine, source, research, result, control, log |
| authority class | current, project-current, second-layer doctrine, raw/source, legacy, candidate |
| freshness | fresh-run, snapshot, prior-audit, stale, unknown |
| source support | artifact, repo doc, user note, external model, inferred |
| drift signal | overclaim, stale path, missing index, language collapse, none |
| allowed write | yes/no/deferred |
| claim ceiling | what this surface may honestly claim |
| next action | apply, harden, route, research, block, defer |

This matrix is the minimum shape for turning the wiki into an alignment tool rather than a pile of docs.

## Wiki alignment target

A good Hermes-aligned wiki should let a fresh LLM quickly learn:

1. the live goal of the system;
2. the user's working style and constraints;
3. the language discipline: no primitive identity, equality, causality, or winner-only smoothing;
4. the project state: current vs legacy vs raw vs candidate;
5. the research spine and source-coverage gaps;
6. the evidence/status ladder;
7. what must be read before acting;
8. what must never be promoted without receipts;
9. where the next bounded tranche lives.

### Owner-kernel source-spine target

For user-owned model explanations, a valid Wizard/wiki alignment tranche may be an owner-kernel/source-spine pass, not only a repo/result-family pass. Example current route:

- [[entropic-monism-axis0-field-compression-spine]] — central preserved owner-kernel route for entropic monism, Axis0, JK fuzz, and doctrine/admission separation.
- [[cross-field-toe-genealogy]] — preserves politics/personality/evolution/consciousness/gravity/physics convergence without physics-first collapse.
- [[field-wide-compression-geometry]] — finite bookkeeping proposal for field-wide compression that expands as it runs.

The bridge rule is: preserve owner-source wording first, separate source-processing/model-spine from proof/admission, preserve surviving variants, then route the next bounded formalization or research tranche. Do not let a clean wiki probe or polished page promote the model to empirical physics.

## System maintenance tranche discipline

Hermes/Wizard/system maintenance runs as bounded tranches:

```text
inventory -> patch one cluster -> verify -> log -> queue next tranche
```

The maintenance loop must not rewrite the whole corpus in one run. It should patch the smallest high-salience surface that makes future agents load the right model, run the wiki probe or relevant validator, record the receipt, and leave the next tranche explicit.

Prompt-size guard: keep `~/.hermes/HERMES.md` and `~/.hermes/SOUL.md` lean. Compact runtime rails may live there when unavoidable, but procedures, maintenance queues, run harnesses, and long rationale belong in skills and wiki notes.

Worker routing: codex2 is preferred for heavy reading and patching. Hermes stays the controller/verifier/editor. Grok, Gemini, and Claude Code Sonnet are pressure/scout/review routes when useful and available. Conserve Opus for high-stakes synthesis or adversarial review.

Operational observations are maintenance notes, not central Wizard doctrine:
- PATH-aware Hermes CLI checks should use a login zsh, for example `zsh -lc 'hermes --version'`.
- Docs extraction routes may be blocked without Firecrawl configuration; record that as a blocked route or maintenance observation, not as a Wizard limitation.

## Non-adoptions

This note does not by itself:
- rewrite HERMES or SOUL;
- enable a new Hermes runtime mode;
- authorize live config/MCP/credential/gateway changes;
- make Grok available when no route exists;
- make Codex Ratchet runner state clean;
- make any Wizard run FULL.

## First bounded application

The first useful application is not another broad doc dump.

Patch the highest-salience front doors so models enter correctly:
- root `index.md` should name Hermes/wiki as the LLM alignment front door;
- `hermes-current/active-plans.md` should point at this bridge;
- `wiki-wizard-v4-2-autoloop-control.md` should carry Grok/Gemini route truth and premortem disposition requirements;
- the `hermes-wizard` skill should load this bridge for current **v4.3** loop work: v4.3 preflight first when scoped, then legacy v4.2 provenance.
