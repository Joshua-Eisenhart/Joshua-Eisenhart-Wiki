# Basins - Negatives

Negatives are first-class controls for future basin sims. They state what the
theory should forbid or deflate.

## Affine / Linear Flow No-Go

A smooth autonomous affine system `dx/dt = A x + b` has equilibria determined
by `A x + b = 0`. When `A` is invertible, there is a unique equilibrium. If `A`
is Hurwitz, that equilibrium is globally attracting on the unconstrained linear
space. This is the generic single-attractor control.

Therefore a plain affine/linear flow should fail any claim of multiple robust
positive-measure attracting basins. If a linear row reports multiple isolated
stable attractors, inspect for smuggled nonlinearity, switching, saturation,
constraints, clipping, projection, hybrid resets, solver artifacts, or
post-processing labels.

Singular affine systems can have continua of equilibria. That is degeneracy,
not generic multistability. It should not be promoted to multiple clean basins
without a separate stability and measure argument.

## Multiple Basins Require Multistability

Multiple positive-measure basins require multiple attracting destinations under
the declared dynamics. In ordinary smooth autonomous finite-dimensional systems,
that is a nonlinear or non-affine phenomenon unless special degeneracy or
piecewise/hybrid structure is introduced.

Designed-fail control: run a stable affine row and require the basin detector to
return one destination on the sampled domain. A detector that invents several
basins in this row is measuring numerical partitions or labels, not dynamics.

Designed-positive contrast: use a nonlinear multistable system, such as a double
well, forced/damped nonlinear oscillator, or coupled nonlinear map, where
coexisting attracting sets are expected.

## Gradient-System No-Go

For a gradient flow `x' = -grad V`, `V` is a Lyapunov function. Under the usual
isolated-critical-point/Morse-Smale-style assumptions, limit behavior is ordered
by descent and recurrent cycles/chaotic attractors are excluded.

This forbids cyclic basin-hopping narratives in a pure gradient system.
Connecting orbits can exist, but their direction is ordered by potential/Morse
index. A closed connection cycle or recurrent attractor outside critical sets is
a red flag unless the system is not actually gradient, the assumptions fail, or
the recurrence lives inside a declared non-gradient component.

Designed-fail control: a gradient double-well may have two basins, but its
connection structure should remain acyclic and energy-descending. It should not
support a ratchet story that needs cyclic recurrence between wells.

## Riddled-Basin Obstruction

Riddled basins are a no-go for clean finite neighborhood decomposition. If every
small neighborhood of typical points in one basin contains positive-measure
points from another basin, then local sampling cannot certify a robust
destination label without extra assumptions.

This does not mean no measure-theoretic basin exists. It means the clean
topological claim fails: open neighborhoods, smooth boundary intuition, and
finite-grid confidence can all break.

Designed-fail control: include a known riddled or intermingled basin example and
require the classifier to lower its claim. Acceptable outputs include
`riddled_boundary_detected`, `clean_partition_blocked`, or `resolution_sensitive`.
Unacceptable output is a smooth, stable two-basin decomposition with no warning.

## Fractal / Wada Boundary Obstruction

Fractal boundaries can make destination prediction resolution-sensitive even
when basin interiors exist. Wada boundaries are stronger multi-basin boundary
structures where three or more basins share the same boundary.

Designed-fail control: a basin-boundary diagnostic should not collapse
`fractal`, `riddled`, `intermingled`, and `Wada` into one label. The sim can
leave the exact class open, but it must preserve the surviving alternatives.

## Computation No-Gos

- A grid basin map is not a certified basin partition.
- A basin fraction is not global unless the sampling domain and measure are
  stated.
- An attracting block proves an attractor handle, not every basin boundary.
- A Conley index proves invariant-set information, not basin volume.
- A complete Lyapunov or Morse-rank certificate proves order/descent structure,
  not scalar attractor quality.
- A same-label attractor in Attractors.jl is a numerical destination ID, not a
  canonical name independent of grid, solver, horizon, and matching procedure.

## Source Anchors

- BU state-space control notes on affine equilibria and eigenvalue stability,
  https://people.bu.edu/johnb/501Lecture14.pdf.
- MIT OCW differential equations notes on stable linear systems,
  https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/mites_1803_s24_topic27.pdf.
- Notre Dame nonlinear systems notes on nonlinear phenomena,
  https://www3.nd.edu/~lemmon/courses/ee580/lectures/chapter1.pdf.
- OSU gradient/Lyapunov notes,
  https://people.math.osu.edu/costin.9/7412-12/p2.pdf.
- Chen et al., "Efficient Morse Decompositions of Vector Fields",
  https://sites.math.rutgers.edu/~mischaik/papers/vfmorsedecomp.pdf.
- P. Ashwin, "Riddled basins and coupled dynamical systems",
  https://empslocal.ex.ac.uk/people/staff/pashwin/PAPERS/Ash_2004_pre.pdf.
- Scholarpedia, "Basin of attraction",
  https://www.scholarpedia.org/article/Basin_of_attraction.
