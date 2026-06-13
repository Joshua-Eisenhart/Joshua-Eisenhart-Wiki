# Basins Child Receipt - 2026-06-11

## Route

- route_id: `basins-tier1-research`
- lane_scope: populate only `/Users/joshuaeisenhart/wiki/codex-ratchet-research/basins/**`
- repo_receipt_scope: `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/wiki_corpus_basins_20260611.md`
- git_add_commit: not run
- lev_timetravel: unavailable in this shell (`lev: command not found`)

## Child Lanes

- `019eb863-4cf8-7e01-807c-628a9b3bd539` / Harvey:
  Conley theory, attractor-repeller structure, Morse decompositions, complete
  Lyapunov functions, and Kalies-Mischaikow-Vandervorst attractor lattices.
- `019eb863-6777-7403-b545-637be36e1861` / Bernoulli:
  Milnor attractors, measure basins, riddled/fractal/intermingled basins,
  linear/affine and gradient-system negative controls.
- `019eb863-80dc-7093-8ce5-e55c0f9b09b9` / Bohr:
  Attractors.jl, interval/set-oriented approximations, basin-fraction methods,
  complete-Lyapunov/Morse-rank computational cautions.

## Child Receipt Summaries

Harvey used live web sources and returned the key caution that `bounded
distributive lattice` is the safe attractor-lattice term; `Boolean algebra`
requires extra assumptions. It also supplied the Conley language for compact
dynamics: chain recurrence, gradient-like complement, attractor-repeller pairs,
Morse decompositions, Conley index, and complete Lyapunov functions.

Bernoulli used live web sources and returned the negative controls: generic
stable affine/linear systems should have one attracting equilibrium, nonlinear
or non-affine structure is needed for ordinary multistability, gradient systems
impose Lyapunov descent/acyclic connection order, and riddled basins obstruct
clean local basin decomposition.

Bohr used live web sources and returned computational cautions: Attractors.jl
basin maps and basin fractions are numerical/grid/sample estimates unless
paired with proof machinery; interval-box, Conley, SOS, and complete-Lyapunov
methods certify different objects and should not be collapsed into basin-volume
proof.

## External Cross-Check

Gemini CLI was attempted with a bounded claim-check prompt. It initially hit
quota retry messages, then returned `OK / CORRECT` for the conservative claims:
Milnor-positive-measure basins, Conley decomposition, bounded distributive
attractor/block lattices, riddled-basin obstruction, affine/linear monostability
as the generic control, and Attractors.jl as numerical basin mapping unless
paired with interval/Conley certificates.

## Files Changed

- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/basins/standard-math.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/basins/alternatives.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/basins/negatives.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/basins/distillate.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/basins/child-receipt-20260611.md`

## Source List

- Conley, `Isolated Invariant Sets and the Morse Index`,
  https://pubs.ams.org/ebooks/cbms/038.
- Norton, "The Fundamental Theorem of Dynamical Systems",
  https://dml.cz/bitstream/handle/10338.dmlcz/118787/CommentatMathUnivCarolRetro_36-1995-3_20.pdf.
- Kalies-Mischaikow-Vandervorst, "Lattice Structures for Attractors I",
  https://www.aimsciences.org/article/doi/10.3934/jcd.2014.1.307.
- Kalies-Mischaikow-Vandervorst, "Lattice Structures for Attractors II",
  https://arxiv.org/abs/1409.5405.
- Kalies-Kasti-Vandervorst, "An Algorithmic Approach to Lattices and Order in
  Dynamics", https://www.math.fau.edu/files/kalies_papers/order.pdf.
- Kalies-Mischaikow-Vandervorst, "An Algorithmic Approach to Chain Recurrence",
  https://www.math.fau.edu/files/kalies_papers/aacr.pdf.
- Milnor, "On the Concept of Attractor",
  https://scispace.com/pdf/on-the-concept-of-attractor-43a8vrm8t2.pdf.
- Young, "What are SRB measures, and which dynamical systems have them?",
  https://cims.nyu.edu/~lsy/papers/SRBsurvey.pdf.
- Ashwin, "Riddled basins and coupled dynamical systems",
  https://empslocal.ex.ac.uk/people/staff/pashwin/PAPERS/Ash_2004_pre.pdf.
- Attractors.jl docs,
  https://juliadynamics.github.io/DynamicalSystemsDocs.jl/attractors/dev/tutorial/.

## Open Items

- No sim, queue movement, admission artifact, or canonical Ratchet theorem was
  created.
- Gemini cross-check completed after quota retries and is counted as an
  advisory external cross-check, not source authority.
