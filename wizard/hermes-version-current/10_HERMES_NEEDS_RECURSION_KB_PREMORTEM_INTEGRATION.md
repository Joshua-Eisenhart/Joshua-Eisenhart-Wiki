---
title: Hermes needs recursion, compiled KB, PageIndex retrieval, and strong premortem integration
created: 2026-05-05
updated: 2026-05-05
type: integration_plan
runtime: hermes
status: live-scout
---

# Hermes needs recursion, compiled KB, PageIndex retrieval, and strong premortem integration

## Trigger

Josh pointed Hermes at four repos and corrected the current trajectory:

- `https://github.com/Q00/rlm-forge`
- `https://github.com/Q00/ouroboros`
- `https://github.com/VectifyAI/PageIndex`
- `https://github.com/VectifyAI/OpenKB`

He also stated that Wizard keeps getting updated and that premortem is an essential skill that needs strong integration.

## Scout receipts

Local shallow clones were created under:

`/tmp/hermes-repo-scout-20260505-133045/`

Checked commits:

- `Q00/rlm-forge` — `main ca0d903`
- `Q00/ouroboros` — `main f302040`
- `VectifyAI/PageIndex` — `main 46244ae`
- `VectifyAI/OpenKB` — `main 798731b`

Smoke check:

`python3 -m compileall -q .` passed for all four cloned repos.

This is only a syntax/import-shape smoke check. It is not installation, runtime integration, test-suite proof, or API credential proof.

## What each repo contributes to Hermes

### 1. RLM-FORGE

Source claims checked:

- README: “A tiny recursive-runtime forge for Hermes Agent.”
- Architecture: Ouroboros owns recursion; Hermes performs bounded inner calls; TraceGuard refuses unsupported synthesis.
- RLM-FORGE is not a new model architecture; it is a runtime-hosted recursive execution loop.
- TraceGuard validates that parent synthesis only claims facts backed by accepted child evidence handles.

Hermes import:

- Use RLM-FORGE as the model for **evidence-gated recursive subcalls**.
- Parent synthesis must cite accepted child evidence handles.
- Recursive shape alone is not evidence; only accepted child evidence is.
- This directly answers the Hermes Wizard weakness: parent-reported child summaries are useful but must not become verified child proof without handles.

Do not import blindly:

- Do not make Hermes call Ouroboros from inside every normal task.
- Do not treat RLM as a quality win by default; RLM-FORGE itself says the contribution is the runtime path plus deterministic evidence enforcement, not one-fixture superiority.

### 2. Ouroboros

Source claims checked:

- README: specification-first workflow engine; interview -> seed -> execute -> evaluate; ambiguity gate; evaluation feeds next generation.
- Hermes runtime guide: `ouroboros setup --runtime hermes` installs Ouroboros skills into Hermes and registers MCP server; `ooo` can dispatch inside Hermes.
- RLM-FORGE architecture: Ouroboros owns recursion, state mutation, scheduling, retry, and termination; Hermes returns one structured JSON envelope for one bounded node.

Hermes import:

- Use Ouroboros as an optional **outer recursion/specification controller** pattern.
- Keep Hermes as the bounded inner runtime when a stronger outer loop is needed.
- Import the separation: outer scaffold owns recursion and mutation; inner Hermes call owns one bounded node.
- This is especially relevant to Wizard v4.1 child/subchild proof: Hermes needs evidence handles and replayable traces, not only narrative summaries.

Do not import blindly:

- Do not let Ouroboros replace Hermes `HERMES.md`, `SOUL.md`, or the Hermes Wizard docs.
- Do not run `ooo` setup or mutate config without explicit user approval.

### 3. PageIndex

Source claims checked:

- README: vectorless, reasoning-based RAG; no vector DB; no chunking; hierarchical tree index; LLM reasons over document tree.
- PageIndex retrieval uses document structures, node IDs, summaries, and tree search.
- It is available self-hosted, via cloud API, and via MCP/API.

Hermes import:

- Use PageIndex as the model for **structure-first long-document retrieval**.
- Replace blind chunking / vector-only retrieval for long docs with document trees and node IDs.
- For Josh’s wiki/harness, PageIndex is most relevant to large PDFs, papers, and long high-entropy docs before they enter `hermes-current/`.

Do not import blindly:

- Do not add cloud/API/MCP credentials or hosted PageIndex use without explicit approval.
- Do not treat PageIndex search as proof; retrieval still needs evidence status and source citations.

### 4. OpenKB

Source claims checked:

- README: OpenKB compiles raw documents into a structured, interlinked wiki-style knowledge base.
- Knowledge compounds over time instead of being re-derived on every query.
- Architecture: `raw/` -> conversions/PageIndex -> `wiki/` with `index.md`, `log.md`, `AGENTS.md`, `sources/`, `summaries/`, `concepts/`, `explorations/`, `reports/`.
- Commands include `openkb add`, `query`, `chat`, `watch`, `lint`, `status`.
- Lint checks cover broken links, orphans, missing entries, and index sync.

Hermes import:

- Use OpenKB as a concrete model for the **wiki entropy-refinery loop** Hermes has already been building.
- The key shape is: raw intake -> compiled wiki -> concept pages -> lint/reports -> query/chat over accumulated knowledge.
- This strongly matches `hermes-current/` + wiki as long-form memory spine.

Do not import blindly:

- Do not replace Josh’s existing wiki shape with OpenKB’s generated layout.
- Do not run `openkb watch` or auto-compile into the live wiki without a sandbox and explicit approval.

## Integration architecture for Hermes

Hermes should treat the four repos as four separate layers, not one blob:

```text
OpenKB / PageIndex         = source ingestion + structure-first retrieval
Hermes current/wiki spine  = current authority and low-entropy memory surface
Hermes Wizard              = Decision -> Failure -> Follow-Up compiler
Premortem                  = mandatory Failure hardening lens for consequential moves
RLM-FORGE / Ouroboros      = optional recursive trace/evidence controller for child proof
```

The current gap is not “Hermes needs more tools” in the abstract. The current gap is:

1. Hermes needs stronger child/subchild evidence handles.
2. Hermes needs document-tree retrieval for long docs and PDFs.
3. Hermes needs a compiled-KB/lint loop for the wiki.
4. Hermes Wizard needs premortem as a required Failure member, not an optional label.
5. Hermes needs to track upstream Wizard updates as a live dependency, not assume this session’s adaptation is final.

## Strong premortem integration

Premortem should be a required Failure Council member for any substantive Hermes Wizard run that changes docs, skills, runtime behavior, repo state, or user-facing strategy.

Minimum premortem output inside Wizard:

```yaml
premortem:
  future_failure_story: <how this failed later>
  hidden_assumption: <the unspoken bet>
  early_warning_signs:
    - <observable warning>
  prevention:
    - <specific hardening action>
  disposition:
    out_of_scope | stop_condition | required_hardening | dismissed_by_artifact
```

Join gate:

- Follow-Up Council must not render prompt options until every open premortem finding is mapped to one of the four dispositions.
- If a premortem finding maps to `required_hardening`, the compiled move is `harden_then_execute`, not `pass_to_execution`.
- If a premortem finding maps to `stop_condition`, that condition must appear in the compiled move and follow-up option.
- If the premortem route did not run, the run is partial and must say why.

## Immediate adoption plan

### Phase 1 — Docs/skills, no runtime mutation

Status: done/started in this session.

- Create this integration note.
- Patch `hermes-wizard` to make premortem mandatory for substantive Failure Council runs.
- Patch `premortem` skill to state its Wizard join-gate role more strongly.
- Add a Hermes Wizard skill reference for the repo scan and integration plan.

### Phase 2 — Sandbox probes

Do only after explicit approval.

- Create a sandbox OpenKB knowledge base from a small subset of `~/wiki/raw/papers` or a throwaway test corpus.
- Run PageIndex on one long PDF and inspect node/tree outputs.
- Test whether Ouroboros can be configured with Hermes without mutating main Hermes config, preferably under a throwaway profile or temp home.
- Test RLM-FORGE TraceGuard locally without API keys if the no-API demo path is available.

### Phase 3 — Hermes integration design

- Decide whether PageIndex/OpenKB become skills, MCP tools, or external CLI helpers.
- Decide whether Ouroboros/RLM-FORGE become optional external controller modes rather than Hermes default behavior.
- Add validator gates so any recursive child proof must carry stable evidence handles.

## Current recommendation

The initial sandbox proof packet has now run. See `11_HERMES_WIZARD_LOOP_SANDBOX_RESULTS.md` for the loop-smoke 0003-0012 evidence summary.

Current state:

1. PageIndex/OpenKB patterns are useful as structure-first retrieval/lint models, with scoped corpora and role/provenance classification.
2. Whole-wiki retrieval is useful broad corpus search, not authority/admission by itself.
3. TraceGuard direct evidence-handle gating is usable now.
4. Premortem is a hard Failure barrier for consequential loop changes.
5. Autoresearch/refinery output stays candidate input until audited/admitted.
6. Ouroboros/RLM package-level recursive runtime remains blocked until pinned dependency compatibility is proven in an isolated environment.
7. Boundedness is per profile/admission path, not a serial scheduling rule; the next safe loop is a mass-parallel batch of independent bounded profiles with per-profile ADMIT/HOLD/BLOCK.

Do not install or wire these into live Hermes yet. Build the next non-sim Hermes cleanup loop as a sandbox docs/skills/MMM batch runner first, with one batch receipt, one human summary, raw worker evidence, and no live writes unless a later apply step is explicitly approved.
