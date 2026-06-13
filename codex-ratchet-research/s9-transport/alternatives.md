# S9 Transport - Alternatives

Source registry: `system_v6/receipts/round3_discriminator_registry_20260611.md`.
Evidence ceiling: finite alternative-space research, not result evidence.

## Canonicalizer

The registry reduces candidates to:

`(f_simplified, F=f'(eta), c1, leaf_holonomy_vector[0,pi/6,pi/4,pi/3,pi/2], annular_flux_vector, validity_class, path_ordered_loop_signature when scoped)`.

For ordinary one-form candidates, alias requires equality of curvature density
and full leaf-holonomy vector under the S2/S9 convention map. Equal `c1` is
co-survival, not alias.

## Candidate Families

- `S9.R3.0_committed_hopf`: `f=cos(2eta)`. Control.
- `S9.R3.1_c1_small_density_bump`:
  `f=cos(2eta)+epsilon*sin(2eta)^2`, `epsilon in {1/20,-1/20}`. Closest
  same-Chern density neighbor; killed by curvature density before holonomy if
  implemented correctly.
- `S9.R3.2_one_leaf_match_pi6`:
  `f=cos(2eta)+epsilon*(cos(2eta)-1/2)`. Matches at `pi/6`; expanded spectrum
  should separate it.
- `S9.R3.3_one_leaf_match_pi4`:
  `f=cos(2eta)+epsilon*cos(2eta)`. Matches at `pi/4`; expanded spectrum should
  separate it.
- `S9.R3.4_two_leaf_match_pi6_pi4`:
  `f=cos(2eta)+epsilon*cos(2eta)*(cos(2eta)-1/2)`. Two leaf anchors survive;
  annular flux and off-anchor holonomy are the expected teeth.
- `S9.R3.5_path_ordered_loop_neighbor`: same local `c1` row plus two named
  quaternionic loop families. Heavy-local because it tests transport identity,
  not coefficient identity.

## Classification Bounds

The standard topology row bounds the Chern class. The registry uses finer
transport rows. One- and two-leaf matches remain `open` until the expanded
spectrum and annular flux rows run. Path-ordered signatures are required before
matrix-valued loop families can be compared.
