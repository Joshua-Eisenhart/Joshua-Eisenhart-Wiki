# S3 Probes Child Receipt - Wave 2 - 2026-06-11

## Route

- route_id: `s3-probes-wave2-child-lane`
- lane_scope: populate only `/Users/joshuaeisenhart/wiki/codex-ratchet-research/s3-probes/**`
- repo_files_edited: no
- git_add_commit: not run

## Files Changed

- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/s3-probes/standard-math.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/s3-probes/alternatives.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/s3-probes/negatives.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/s3-probes/distillate.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/s3-probes/child-receipt-wave2-20260611.md`

## Per-File Line Counts After Edit

- `alternatives.md`: 83 lines
- `child-receipt-wave2-20260611.md`: 70 lines
- `distillate.md`: 75 lines
- `negatives.md`: 90 lines
- `standard-math.md`: 88 lines

## Source List

- Renes, Blume-Kohout, Scott, Caves, "Symmetric Informationally Complete
  Quantum Measurements", arXiv:quant-ph/0310075,
  https://arxiv.org/abs/quant-ph/0310075
- Scott and Grassl, "SIC-POVMs: A new computer study", arXiv:0910.5784,
  https://arxiv.org/abs/0910.5784
- Brierley, Weigert, Bengtsson, "All Mutually Unbiased Bases in Dimensions Two
  to Five", arXiv:0907.4097, https://arxiv.org/abs/0907.4097
- Szollosi, "The problem of mutually unbiased bases in dimension 6",
  https://math.bme.hu/~matolcsi/proceedingsmub0904.pdf
- McNulty and Weigert, "Mutually Unbiased Bases in Composite Dimensions - A
  Review", Quantum 10, 2051 (2026),
  https://quantum-journal.org/papers/q-2026-04-01-2051/
- Chien and Waldron, "A characterisation of projective unitary equivalence of
  finite frames", arXiv:1312.5393, https://arxiv.org/abs/1312.5393
- D'Ariano, Lo Presti, Perinotti, "Classical randomness in quantum
  measurements", J. Phys. A 38 (2005),
  https://wordpress.qubit.it/wp-content/uploads/publications-dariano/extrpovm_JPA.pdf
- Czerwinski, "Quantum state tomography with informationally complete POVMs
  generated in the time domain", arXiv:2010.13777,
  https://arxiv.org/abs/2010.13777

## Gemini Command Status

- command:
  `gemini -m auto-gemini-3 -p 'Bounded cross-check for Codex Ratchet S3 probes: verify concise claims only. Are these bounded math claims broadly correct? (1) Qubit POVMs can be represented by positive weighted Bloch effects summing to identity; extremal nontrivial qubit POVMs have at most four rank-one outcomes. (2) SIC-POVMs are conjectured in all finite complex dimensions; known evidence includes exact/numerical constructions, but universal existence is open. (3) Complete MUB sets of d+1 bases exist in prime-power dimensions, so d=2,3,4,5 have complete sets; d=6 complete set existence is open and only three are known from standard product constructions. (4) IC POVM means POVM effects span Hermitian operator space; equal rank/outcome count does not imply unitary/relabel equivalence. Return: OK/CORRECT with any caveats and stable references/identifiers if you can.'`
- status: available; exited 0
- stdout summary: Gemini returned `OK/CORRECT`, agreed with the four bounded
  claims, cited D'Ariano et al. for extremal POVMs, Zauner/Wootters-Fields/
  Prugovecki-style references, and cautioned that very recent claimed proofs
  should not be treated as consensus without controller admission.
- stderr/setup notes observed: `Ripgrep is not available. Falling back to
  GrepTool.` and `Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using
  GOOGLE_API_KEY.`

## Blockers / Open Items

- Local `lev timetravel search` was unavailable in this shell:
  `zsh:1: command not found: lev`. Direct web/literature lookup was used
  instead.
- Recent claimed all-d SIC or d=6 MUB resolution papers were not admitted here;
  this lane keeps the conservative stable-literature status.
- The files are research registers only. No probe row, canonicalizer, sim, or
  admission artifact was created.
