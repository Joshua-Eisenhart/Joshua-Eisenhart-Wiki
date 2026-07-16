# TOOLS, SOLVERS, LIBRARIES & REPOS
_Regenerated 2026-07-11 04:06 UTC. Versions read from the live environment._

## Solver & library versions (this environment)
- **numpy**: 2.3.5
- **scipy**: 1.17.0
- **sympy**: not present
- **sklearn**: 1.8.0
- **pysindy**: not present
- **z3**: not present
- **cvc5**: not present
- **mpmath**: not present

Python: 3.12.13. Env: constraintcore (conda). Numba cache: /tmp/numba_cache.

## Dependency contract
THREE-ENGINE DEPENDENCY CONTRACT (load-bearing gates): z3 AND cvc5 must agree on the same
structural claim with erased controls that flip it; numpy/scipy/mpmath are CONTROL-LANE only, never load-bearing; at
least one tool outside the array baseline must gate a verdict. Sims carry NO jargon -- pure real math and structure;
a rosetta layer maps earned structure to labels afterward.

## Repos (source of truth)
- **codex-ratchet repo** (system_v7/constraint_core/): the v7 sim runner + working docs. Provenance and live code, not a truth database.
- **Wiki** (Joshua-Eisenhart/Joshua-Eisenhart-Wiki, projects/codex-ratchet/): synced reports, ledger, changelog, sims.
- **leviathan** (github.com/lev-os/leviathan): a CS-version reference of many concepts; REFERENCE not canon.
- This bundle mirrors the audit-engine sim set; the codex app consumes these zips + runs its own sims.

## How the pieces run
- `run_all.py` -- the full harness (each sim is a subprocess; a row PASSES on a 'contains' string match). No jargon in sims.
- `sims_and_scripts/` -- 150 python sim files (some are withdrawn scaffolds, not registered).
- `panel_adversarial_review.py` -- cross-family LLM panel (Gemini/Grok/Qwen/GLM) as an ADVISORY adversarial reviewer; never gates.
- `MODEL_LAYER_LEDGER.md` / `CHANGELOG_HARDENING.md` -- append-only rung record + hardening log.
