# Hermes Memory Maintenance — 2026-06-05

Purpose: preserve the live injected Hermes memory/profile state before compression, then record the intended steady-state: memory is a compact bootstrap/index; the wiki carries long-form detail; skills enforce the workflow.

Status: active maintenance receipt.

## Trigger

Josh asked Hermes to take care of Hermes memory and update the tools/skills to run it. The wiki was already being used as one solution to the Hermes memory problem.

## Live memory system state checked

Command: `zsh -lc 'hermes memory status; hermes profile show default; hermes config path'`

Observed:
- Built-in memory is active.
- No external memory provider is active.
- Active profile: `default` at `/Users/joshuaeisenhart/.hermes`.
- Gateway running.
- Skills installed: 177.
- Config path: `/Users/joshuaeisenhart/.hermes/config.yaml`.
- Live memory files found:
  - `/Users/joshuaeisenhart/.hermes/memories/MEMORY.md`
  - `/Users/joshuaeisenhart/.hermes/memories/USER.md`

## Current MEMORY.md snapshot before compression

```text
Wiki harness: use /Users/joshuaeisenhart/wiki/hermes-current/ as Hermes frame-loader via harness-bootstrap. For wiki/MMM continuation, recover prior Hermes terminal/session history and log state before judging current work.
§
Wiki roles: hermes-current=Hermes spine; harness=engine doctrine; whole wiki=KB/corpus. Wizard v4.2 MMM target: /Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/.
§
Codex Ratchet: nothing has canon. Scratch carrier is nested PEPS2D/Hopfield (not PEPS3D). JAX+Julia parallel. Goal=dual-stacked QIT engines with L/R chirality. IGT pattern ref: codex-ratchet-sim-planning/references/igt-engine-structure.md. LLMs collapse 8 terrains→4 and miss composition order — always give explicit math.
§
Codex Ratchet execution: preserve geometry-family coverage and work bounded micro-lego → pairwise coupling → small assembly; trace failures back to micro sims.
§
Codex Ratchet Git index can de-index/mass-delete; when unstable avoid plain status, verify with low-level ls-files/diff.
§
JK fuzz/entropic monism: fuzz is retrocausal finite-possibility field in spacetime. Space/time/entropy/dark energy/gravity/entanglement-info are one; spacetime has chirality.
§
python3 only. `codex2`=`CODEX_HOME=$HOME/.codex-second codex` (GPT-5.5 xhigh; add `--skip-git-repo-check` for non-git dirs); Hermes Codex route resolves 1.1M. Gemini unreliable for wiki writes; use codex2. Gemini API exposes 3.5-flash/3.1-pro-preview/pro-latest, not 3.2-pro. Run LLM agents sequentially. "work on wiki" = update wiki pages, not sims.
§
Jean-Patrick Smith: Leviathan/parallel projects, lev os GitHub repo.
§
Keep bot/config boundaries strict; Hermes uses Hermes transport. In steward logs, cycle_end means still alive; exited means actual shutdown.
§
lev_mega_book_curated.pdf is a separate-but-connected source: treat it as a runtime/control-plane bridge source adjacent to the system, not as a replacement for the constraint-first mathematical spine or root doctrine pages.
§
Wizard baseline: v4.3=object-preservation preflight (repo validator sole authority, never fork); v4.2=council runtime. Hermes owns v4.3 packet+harness doc+skill. Claude/Codex v4.3 skills=reference only.
```

## Current USER.md snapshot before compression

```text
Foundational frame: support-ordered constraints; Weyl spinors on nested Hopf tori; a=a iff a~b. Anti-teleology: viable futures pressure present; JK fuzz/Axis0/gravity stay open, nuanced.
§
Autoresearch/sim: mass-parallel bounded packets are valid; admission per packet/profile, never whole-chain blur.
§
Sims: full tensor/entanglement/chirality. Goal=QIT engines (dual stacked, 720° spinor, L/R, IGT). No canon. 2 root constraints (F01,N01); minimality=method not axiom.
§
Prefs: answer-first, non-log synthesis; keep Hermes lean; external workers for heavy work: codex2 primary, Claude Sonnet/high usable heavily, Grok/Gemini contrast, conserve Opus.
§
Execution prefs: exact bounded order; sim tools first as classical probes; classical baselines ok; z3 explicitly. Use codex2 for heavy lifting.
§
Hermes+wiki=entropy-refinery; hermes-current/ front door read-first.md; memory is bootstrap/index. Preserve owner explanatory prompts verbatim as source artifacts; summaries must not replace owner-kernel.
§
When ingesting LEV/Leviathan runtime material, keep it separate from the core constraint/geometry doctrine: it is adjacent architecture/control/memory/process language, not a replacement vocabulary for the theorem/maths spine.
```

## Compression plan

Keep injected memory to compact pointers only. Long-form detail belongs here, in the `hermes-current/` spine, project pages, raw owner prompt artifacts, or skills.

Planned MEMORY.md shape:
- wiki/harness pointer and roles
- Codex Ratchet compact steering pointer
- environment/tool routing compact pointer
- bot/profile boundary pointer
- Wizard baseline pointer

Planned USER.md shape:
- foundational frame pointer
- sim/execution preference pointer
- communication/tooling preference pointer
- owner-source preservation pointer
- LEV/Leviathan separation pointer

## Post-compression state

After preserving this snapshot and wiring it into the spine, injected memory was compressed.

Observed readback after compression:

`MEMORY.md` now carries 8 compact entries:
- wiki memory spine pointer to `read-first.md` and `hermes-memory-offload.md`
- Codex Ratchet compact pointer: no canon, nested PEPS2D/Hopfield scratch, JAX+Julia, QIT dual L/R goal, explicit 8-terrain math, bounded micro→coupling→assembly
- Codex Ratchet Git index instability warning
- JK fuzz / entropic monism compact pointer
- tools pointer: `python3`, codex2 expanded command, Gemini unreliability, wiki work = pages not sims
- bot/config boundary pointer
- `lev_mega_book_curated.pdf` adjacent runtime/control-plane source boundary
- Wizard v4.3/v4.2 baseline pointer

`USER.md` now carries 5 compact entries:
- foundational frame
- execution/sim preferences
- answer/tooling preferences
- Hermes+wiki as entropy-refinery plus owner-prompt preservation rule
- LEV/Leviathan vocabulary separation rule

Memory-tool reported usage during compression:
- `MEMORY.md`: reduced to about 61% / 1,358 chars, 8 entries.
- `USER.md`: reduced to about 72% / 998 chars, 5 entries.

## Tool/skill updates made

Patched or verified these skills carry the memory workflow:
- `memory-offload-to-wiki-harness`: now explicitly inventories live built-in memory files (`MEMORY.md`, `USER.md`), checks profile/provider scope, writes `memory-maintenance-YYYY-MM-DD.md`, and preserves first / compresses second.
- `memory-offload-to-wiki-harness/scripts/snapshot_memory_to_wiki.py`: added helper script to generate dated memory snapshots from the active Hermes profile into `wiki/hermes-current/`.
- `capture`: now says Hermes memory/wiki continuity work should write dated receipts under `/Users/joshuaeisenhart/wiki/hermes-current/` when no `.lev/` workstream applies.
- `harness-bootstrap`: already requires `hermes-current/` first and points to memory offload when memory pressure/preservation is in scope.
- `lean-hermes-control-and-accounting-skills`: already supports the global rule: keep prompt lean, use capture/offload skills at transition points.

## Verification requirements

After compression and skill patches:
- read back `/Users/joshuaeisenhart/.hermes/memories/MEMORY.md`
- read back `/Users/joshuaeisenhart/.hermes/memories/USER.md`
- run `wiki_probe.py --wiki-root /Users/joshuaeisenhart/wiki --output /tmp/wiki_probe_memory_maint_post_20260605.json`
- verify no conflict markers/control bytes in touched files

## Related

- [[hermes-memory-offload]]
- [[read-first]]
- [[skills-and-agent-rules]]
- [[active-plans]]
- [[about-me-and-how-to-work-with-me]]
- [[environment-and-rules]]
