# Basins - Standard Math

Scope: standard mathematical facts for attractors, basins, Conley structure,
attractor lattices, Milnor basins, basin boundaries, and computational basin
methods. This is corpus material, not admitted sim evidence.

## Attractors And Basins

An attractor is not just an invariant set. In the Conley/Kalies-Mischaikow-
Vandervorst setting, the safe criterion is that the set is realized by an
attracting neighborhood, trapping region, or attracting block. For a map, an
attracting block can be stated as `f(cl N) subset int N`; the associated
attractor is the long-time invariant object captured by that block.

The basin or domain of attraction for an attractor `A` is the set of initial
conditions whose forward limit behavior is captured by `A`. A common compact
map formulation is `D(A) = {x : omega(x) subset A}`. This is a destination
criterion, not a statement that the basin is smooth, open, connected, or easy
to compute.

Multiple basins mean multiple attracting destinations under a stated evolution
rule and stated phase-space region. Same fixed point, same basin fraction, or
same local stability does not prove same attractor. Basin claims must name the
sampling region, topology/measure, and admissible destination test.

## Conley Theory

Conley theory gives the standard decomposition vocabulary:

- `isolated invariant set`: the maximal invariant set inside an isolating
  neighborhood;
- `Conley index`: a topological invariant for isolated invariant sets;
- `attractor-repeller pair`: the basic split between an attracting set and its
  complementary repelling structure inside an invariant set;
- `Morse decomposition`: a finite ordered decomposition of recurrent pieces
  plus the connecting dynamics between them;
- `complete Lyapunov function`: a global scalar witness that is constant on
  recurrent pieces and decreases along gradient-like motion outside them.

Conley's fundamental theorem separates compact dynamics into chain-recurrent
structure and gradient-like motion. That is the right language when a basin sim
needs to distinguish recurrent blocks, connection order, and attraction basins
instead of treating every destination label as a free-standing preference.

Morse decompositions are order objects. They support claims like "this recurrent
piece precedes that one in the connection graph" or "the gradient-like part
descends between blocks." They do not by themselves prove basin volume, basin
smoothness, or scalar attractor quality.

## Attractor Lattice

Kalies, Mischaikow, and Vandervorst show that attractors, repellers, and
attracting neighborhoods carry bounded distributive lattice structure. The safe
term is `bounded distributive lattice`, not automatic Boolean algebra.

For noninvertible maps, the lattice operations on attractors require care:
joins can be unions, while meets are naturally recovered through an attracting
neighborhood/block operation such as `omega(intersection)` rather than naive
set intersection in every setting.

Attracting blocks and attracting neighborhoods are computationally important
because they can be represented at finite resolution. A finite attractor lattice
can be lifted to an index-lattice or attracting-block representation, which then
supports finite Morse representations. This is a computable handle, not a proof
that the full infinite attractor lattice was enumerated.

Boolean-algebra language is admissible only under an explicit Booleanization,
regular-closed-set, or finite block context with the needed assumptions named.
Do not write "the attractor lattice is Boolean" as the default theorem.

## Milnor And Measure Basins

Milnor attractors weaken the basin criterion from open/asymptotically stable
basins to positive-measure realms of attraction. A closed set `A` can be a
Milnor attractor when its realm/basin has positive measure and no smaller closed
subset captures the same realm up to measure-zero error.

This distinction matters for Codex Ratchet basin work. A positive-measure basin
does not imply Lyapunov stability, open neighborhoods, robustness to noise, or a
clean topological partition. Milnor language is useful when the sim observable
is measure-theoretic survival rather than topological attraction.

## Basin Boundaries

Fractal basin boundaries mean the prediction barrier sits on a complicated
boundary. Riddled or intermingled basins are stronger obstructions: every small
neighborhood of typical points in one basin may contain positive-measure points
from another basin. In such a case, finite-resolution neighborhood tests cannot
certify a clean destination label without extra assumptions.

Keep the boundary taxonomy separated:

- `fractal boundary`: complicated boundary geometry;
- `riddled basin`: basin pierced throughout by positive-measure complement;
- `intermingled basins`: two positive-measure basins mutually penetrate;
- `Wada boundary`: three or more basins share the same boundary set.

These are not interchangeable labels. A basin sim that treats them as the same
will overclaim decomposition quality.

## Computational Side

Attractors.jl supplies numerical basin machinery: `AttractorsViaRecurrences`,
`AttractorsViaProximity`, `AttractorsViaFeaturizing`, `basins_fractions`,
`basins_of_attraction`, global continuation, and boundary diagnostics such as
basin entropy, fractality tests, uncertainty exponents, Wada tests, and edge
tracking.

The safe readout is numerical unless paired with proof machinery. Grid/sample
basin maps estimate destinations and fractions under a chosen domain, solver,
grid, transient horizon, and sampler. They are not certified basin enclosures by
default.

Set-oriented and interval-box approaches can give outer approximations to
invariant sets, chain-recurrent sets, or global attractors. Conley-style finite
graph methods can build isolating blocks and Morse decompositions from outer
approximations. SOS/SDP methods can give guaranteed outer approximations for
some polynomial global attractor problems. None of these automatically produces
every individual basin boundary.

Complete-Lyapunov or Morse-rank certificates are admissible as recurrence/order
certificates: they rank recurrent or Morse components by a descent/connection
order. They do not prove "better attractor" unless tied to a named observable
such as basin fraction, convergence time, distance-to-boundary, minimal shock,
or certified enclosure.

## Source Anchors

- C. Conley, `Isolated Invariant Sets and the Morse Index`, AMS CBMS 38, 1978,
  https://pubs.ams.org/ebooks/cbms/038.
- D. E. Norton, "The Fundamental Theorem of Dynamical Systems",
  https://dml.cz/bitstream/handle/10338.dmlcz/118787/CommentatMathUnivCarolRetro_36-1995-3_20.pdf.
- K. Mischaikow, "Conley Index Theory",
  https://eudml.org/doc/208946.
- W. D. Kalies, K. Mischaikow, R. C. A. M. Vandervorst, "Lattice Structures
  for Attractors I", https://www.aimsciences.org/article/doi/10.3934/jcd.2014.1.307.
- W. D. Kalies, K. Mischaikow, R. C. A. M. Vandervorst, "Lattice Structures
  for Attractors II", https://arxiv.org/abs/1409.5405.
- W. D. Kalies, D. Kasti, R. C. A. M. Vandervorst, "An Algorithmic Approach to
  Lattices and Order in Dynamics", https://www.math.fau.edu/files/kalies_papers/order.pdf.
- W. D. Kalies, K. Mischaikow, R. C. A. M. Vandervorst, "An Algorithmic
  Approach to Chain Recurrence", https://www.math.fau.edu/files/kalies_papers/aacr.pdf.
- J. Milnor, "On the Concept of Attractor",
  https://scispace.com/pdf/on-the-concept-of-attractor-43a8vrm8t2.pdf.
- J. A. Yorke et al., "Riddled Basins",
  https://www.worldscientific.com/doi/pdf/10.1142/S0218127492000446.
- P. Ashwin, "Riddled basins and coupled dynamical systems",
  https://empslocal.ex.ac.uk/people/staff/pashwin/PAPERS/Ash_2004_pre.pdf.
- Scholarpedia, "Basin of attraction",
  https://www.scholarpedia.org/article/Basin_of_attraction.
- Attractors.jl docs,
  https://juliadynamics.github.io/DynamicalSystemsDocs.jl/attractors/dev/tutorial/.
- Attractors.jl repository,
  https://github.com/JuliaDynamics/Attractors.jl.
