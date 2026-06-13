# S4 Operators - Standard Math

Scope: standard mathematical facts for qubit operator/channel alphabets. This
is corpus material, not an MMM head.

## Qubit Channels As Affine Maps

A qubit density matrix can be written as `rho=(I+r.sigma)/2` with Bloch vector
`r` in the unit ball. A trace-preserving Hermiticity-preserving linear map acts
on Bloch vectors as an affine map `r -> M r + c`, where `M` is real and `c` is
the non-unital translation.

For the map to be a quantum channel, positivity on the Bloch ball is not enough.
Complete positivity is checked by the Choi matrix. In the round-3 registry this
means an affine row that maps the ball into itself can still be rejected if its
Choi matrix has a negative eigenvalue.

## Unital, Non-Unital, And Pauli Geometry

Unital channels have `c=0` and send the maximally mixed state to itself. Pauli
channels are diagonal in a Pauli basis after allowed unitary conventions and
form the familiar tetrahedral complete-positivity region in diagonal
contraction coordinates. Depolarizing and dephasing rows live in this unital
geometry.

Non-unital channels have `c != 0`. Amplitude damping is the standard close
neighbor: it contracts transverse directions and translates toward a pole. It
cannot be silently classified as a Pauli channel because the translation and
fixed-point structure are load-bearing.

## Source Anchors

- Registry: `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/round3_discriminator_registry_20260611.md`.
- M. B. Ruskai, S. Szarek, E. Werner, "An Analysis of Completely-Positive
  Trace-Preserving Maps on 2x2 Matrices", Linear Algebra Appl. 347, 159-187
  (2002), https://arxiv.org/abs/quant-ph/0101003.
- M.-D. Choi, "Completely positive linear maps on complex matrices", Linear
  Algebra and its Applications 10, 285-290 (1975),
  https://doi.org/10.1016/0024-3795(75)90075-0.
- A. Fujiwara and P. Algoet, "One-to-one parametrization of quantum channels",
  Phys. Rev. A 59, 3290-3294 (1999),
  https://doi.org/10.1103/PhysRevA.59.3290.
- V. Gorini, A. Kossakowski, E. C. G. Sudarshan, "Completely positive
  dynamical semigroups of N-level systems", J. Math. Phys. 17, 821-825 (1976),
  https://doi.org/10.1063/1.522979.
- G. Lindblad, "On the generators of quantum dynamical semigroups", Comm.
  Math. Phys. 48, 119-130 (1976), https://doi.org/10.1007/BF01608499.
- J. Watrous, The Theory of Quantum Information, author site:
  https://cs.uwaterloo.ca/~watrous/TQI/.
