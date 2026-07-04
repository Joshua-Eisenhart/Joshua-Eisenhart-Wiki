# Wrong-repo estate work — salvage record (2026-07-04)

## Bottom line

On 2026-07-02 and 2026-07-03, some Claude threads targeted the wrong repo: `~/Desktop/Codex Ratchet` (the stale Desktop clone) instead of the live `~/Codex-Ratchet`. They did a genuine v5 estate-hygiene campaign there — 15 commits on Desktop `main` (`276882150b..2953526d1e`), working tree clean. None of it exists in the live repo. The two repos stay separate by owner rule (never consolidate, delete, or merge). This note banks what was done so it is not lost.

## What was done in the Desktop repo

| Commit | Work |
|---|---|
| `276882150b`, `4db058881b` | Checkpoints: preserve working state; archive claim-language-debt files (not endorsed) |
| `d4830400bb`, `ccb2852bb9` | Evidence recovery: 10 deleted tool receipts + 79 lego results restored from git history; 2 foundation sims rerun; none-placeholder parsing fixed |
| `b485066347` | 13 micro tool probes authored, repaired, runner-executed |
| `f360932de5` | U3 scout sweep: 46 fresh results, 12 honest fail-verdicts; misdirected outputs relocated |
| `629d998ee4`, `8da89b9591` | Lint C1 repair: `tool_lego_fit_probe` and `diagnostic_only`/`comparison_surface`/`companion_index` classifications applied |
| `778e9a3dde` | Night ledger 2026-07-02: six lanes consolidated, lint 1287 → 306 |
| `fa79716ff6` | Concrete-math-object renames for two guard-blocked sims |
| `490dd8a5d8`, `2caba98062` | Bounded review table + C3/C4 second opinions (disclosed `--no-verify`) |
| `2953526d1e` | C4 divergence-log repair batch: 83 files, family eliminated (68 → 0) |

## Key artifacts (in the Desktop repo)

- `system_v5/ops/NIGHT_LEDGER_20260702.md` — consolidation ledger with per-lane honest labels (`exists` / `passes local rerun`), an overclaims-intercepted section, and a 6-item tomorrow queue with prompt seeds and gates.
- `system_v5/ops/BOUNDED_REVIEW_TABLE_20260703.md` — 611 review rows: 32 quarantine, 68 repair, 511 second-opinion; each row names the exact observable a second opinion should check.

## Where the threads broke down

- Sandbox permission failures: `.git/index.lock` creation blocked, `ps` inspection blocked.
- Two commits needed disclosed `--no-verify` (mention-vs-use gate flag).
- The canonical-bucket earning lane blocked on a missing artifact (`/tmp/canonical_bucket_earning_diagnosis.json`) and was honestly recorded as blocked, not done.

## Memory salvage (added 2026-07-04, second pass)

The wrong-repo threads did save their findings to Claude memory — but under the Desktop project key (`~/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/`), which never loads for sessions in the live repo. The 31 files written 2026-07-01 to 2026-07-04 were copied into the live project's memory under `salvaged_desktop_20260704/` (provenance-fenced, unvetted). Highlights: owner doctrine write-ups (entropic monism, nominalist system, finite ordered foundations, causality/FEP, IGT two-engine discovery, least-presumption/weakest-structure, teleological selection cosmology), the CR-sims-through-Lev pilot-wave record, multitier model spawning policy, three-engine sim contract reference, and ten binding feedback rules. Originals remain in place for Desktop-repo sessions.

## Disposition

- Do not merge or cherry-pick: the trees diverged since April 2026.
- The salvage value is the method and the queues: the night-ledger format, the bounded review table with per-row observables, and the 6-item tomorrow queue are directly reusable if the owner wants the same estate lane run on the live repo against its own lint state.
- Session guard: confirm the working directory is `~/Codex-Ratchet` (hyphen) before any Codex Ratchet work.
