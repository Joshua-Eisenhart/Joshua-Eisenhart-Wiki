# Basins - Alternatives

Source status: finite external research plus child cross-check receipts. Evidence
ceiling: corpus register, not result evidence.

## Rival Decomposition Frameworks

The basin criterion is not the only honest way to decompose dynamics. Choose the
framework by the observable being tested.

## Basin / Attractor Decomposition

Use basin decomposition when the question is destination classification:

- which initial conditions approach which attracting set;
- how large a basin is under a stated measure and domain;
- whether two systems preserve the same destination partition;
- how much shock or perturbation is needed to leave an attractor's basin.

This is the right tool for multistability, basin fractions, nonlocal stability,
basin boundaries, and designed-fail controls that ask whether more than one
positive-measure destination exists.

It is the wrong tool when the observable is time-average statistics without a
single topological attractor, transient recurrence order without attraction, or
symbolic connection structure independent of basin volume.

## SRB / Physical Measures

Use SRB or physical-measure language when the question is statistical behavior
for a positive-measure set of initial conditions. The object is an invariant
measure and its basin of time-average convergence, not necessarily a clean
topological basin of a set.

SRB measures are especially appropriate for chaotic dissipative attractors where
orbits from a large basin have coherent statistics. They answer "what statistics
do typical trajectories see?" better than "which geometric destination label did
this point reach?"

Do not replace basin decomposition with SRB decomposition when the sim needs
finite destination labels or geometric basin boundaries. Do not replace SRB with
basins when the claim is about time averages, ergodic components, or physical
statistics.

## Ergodic Decomposition

Use ergodic decomposition when the invariant-measure space is the object. It
splits invariant measures into ergodic components. That is measure-level
structure, not initial-condition basin geometry by itself.

This is useful for statistical mixtures, non-ergodic invariant sets, and
questions about whether a simulated long-run distribution is a blend of simpler
ergodic behaviors. It does not automatically certify multiple attracting basins.

## Chain-Recurrence Classes

Use chain recurrence when attraction is too coarse and the question is
approximate return structure. Conley's decomposition uses the chain-recurrent
set as the recurrent core and treats the complement as gradient-like.

This is the right tool when finite perturbation or finite grid resolution can
move among apparent states, or when the sim needs recurrence classes and
connection order rather than destination basins.

Chain-recurrence classes do not equal basins. A class can be recurrent without
being an attractor, and an attractor's basin includes points outside the
recurrent set that flow into it.

## Isolating Neighborhoods

Use isolating neighborhoods when the claim is local invariant-set existence or
Conley index structure. The criterion is maximal invariance inside a
neighborhood, not attraction from a surrounding basin.

This is the right tool for proving that a recurrent set exists inside a box,
that an index is nontrivial, or that a finite outer approximation supports a
Morse set. It is not the same as a trapping region.

## Trapping Regions And Attracting Blocks

Use trapping regions or attracting blocks when the claim needs attraction
direction. A block such as `f(cl N) subset int N` gives a forward-invariant
capture region whose invariant core is an attractor.

This is the right tool for certified attractor existence, basin-entry tests,
finite block lifts, and attractor-lattice computations. It is stronger than a
mere isolating neighborhood because it carries attraction direction.

## Practical Selection Rule

- Destination labels and nonlocal stability: use basin/attractor decomposition.
- Typical long-run statistics: use SRB or physical measures.
- Invariant-measure mixture: use ergodic decomposition.
- Recurrence and gradient-like order: use chain recurrence and Conley/Morse.
- Local invariant-set proof: use isolating neighborhoods and Conley index.
- Certified attraction handle: use trapping regions, attracting blocks, and
  attractor lattices.

## Source Anchors

- Lai-Sang Young, "What are SRB measures, and which dynamical systems have
  them?", https://cims.nyu.edu/~lsy/papers/SRBsurvey.pdf.
- D. E. Norton, "The Fundamental Theorem of Dynamical Systems",
  https://dml.cz/bitstream/handle/10338.dmlcz/118787/CommentatMathUnivCarolRetro_36-1995-3_20.pdf.
- W. D. Kalies, K. Mischaikow, R. C. A. M. Vandervorst, "An Algorithmic
  Approach to Chain Recurrence", https://www.math.fau.edu/files/kalies_papers/aacr.pdf.
- W. D. Kalies, D. Kasti, R. C. A. M. Vandervorst, "An Algorithmic Approach to
  Lattices and Order in Dynamics", https://www.math.fau.edu/files/kalies_papers/order.pdf.
