# S5 Flows - Standard Math

Scope: standard mathematical facts for affine terrain flows. This is corpus
material, not an MMM head.

## Affine Flows On The Ball

The layer uses affine differential equations for Bloch vectors:

`dr/dt = A r + b`.

The finite-time map, when `A` is constant, is
`r(t)=exp(tA)r(0)+ integral_0^t exp((t-s)A)b ds`. Fixed points satisfy
`A r_* + b = 0` when the equation is solvable. Matching a fixed point does not
match transient rotation, contraction rates, or basin geometry.

## Quantum-Semigroup Constraint

When the flow is claimed as an open quantum dynamical semigroup, each finite
time map must be CPTP for `t >= 0` and the generator must fit GKSL/Lindblad
structure. A single finite-step ball-preserving affine map is weaker than a
valid semigroup generator.

For ordinary affine ODE validity on a closed ball, invariance can be tested by
tangent/normal boundary conditions of the Nagumo/Brezis type. This is a
mathematical ball-invariance row; it is still weaker than complete positivity
when the row is interpreted as a quantum channel semigroup.

Hamiltonian parts contribute skew/rotation structure; dissipative parts
contribute contraction and translation. Mixtures can preserve some visible
basin facts while changing N01, mirror, or transient signatures.

## Source Anchors

- Registry: `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/round3_discriminator_registry_20260611.md`.
- V. Gorini, A. Kossakowski, E. C. G. Sudarshan, J. Math. Phys. 17, 821-825
  (1976), https://doi.org/10.1063/1.522979.
- G. Lindblad, Comm. Math. Phys. 48, 119-130 (1976),
  https://doi.org/10.1007/BF01608499.
- Ruskai-Szarek-Werner qubit channel geometry:
  https://arxiv.org/abs/quant-ph/0101003.
- H. Brezis, "On a characterization of flow-invariant sets", Comm. Pure Appl.
  Math. 23, 261-263 (1970),
  https://sites.math.rutgers.edu/~brezis/PUBlications/9-journal.pdf.
- M. M. Wolf and J. I. Cirac, "Dividing Quantum Channels", Comm. Math. Phys.
  279, 147-168 (2008), https://arxiv.org/abs/math-ph/0611057.
- Standard affine ODE background: any linear systems text covering constant
  coefficient affine systems and fixed-point/transient decomposition.
