# S6/S7 Topologies - Distillate

Status: wave-2 populated MMM register.

Scope: MMM-register language only. This page is for exclusion phrases and naming
discipline; it is not a math proof, admission receipt, or sim result.

## Allowed Register

- "Under this finite graph probe, these support graphs have not been
  distinguished."
- "Same graph isomorphism class under the named checker/proof."
- "Same cover relation under the named projection."
- "Same quotient action under the named finite group action."
- "Same boundary-cost profile under the named observable."
- "Excluded by failed action well-definedness."
- "Excluded by failed lift/descent check."
- "Excluded by global-cycle/twist witness despite local neighborhood match."
- "Co-survives this probe; not an alias."
- "Topology identity remains probe-relative."

## Forbidden Register

- Do not write "the graph is a Mobius strip" without the finite strip, gluing
  rule, and probe.
- Do not write "this is a lens space" for a grid quotient unless a finite
  sphere/cell model and free cyclic action are supplied.
- Do not write "same topology" when only node count, degree distribution, local
  neighborhoods, or cost profile matched.
- Do not reify "torus", "Klein", "lens", or "cover" as discovered abstractions.
  They are labels for named finite constructions.
- Do not use area-law or Lieb-Robinson citations as topology classifiers.
- Do not let a successful cost scout imply manifold, holographic, or physical
  identity.

## Names As Labels

- `torus-grid`: label for `C_m square C_n` or an equivalent explicit periodic
  grid construction.
- `shear-torus`: label for a periodic grid with a named shift in the boundary
  identification.
- `mobius-grid`: label for a finite strip with a named reflection/twist
  boundary identification.
- `klein-grid`: label for a finite grid with one periodic and one twisted
  identification, or another explicitly equivalent finite rule.
- `lens-style-cyclic-quotient`: label for a cyclic quotient probe that has not
  earned lens-space descent.
- `lens-descent`: reserve for rows with a well-defined cyclic action on the
  supplied support/cell model and the required descent checks.
- `same-cost`: label for one observable, never a support-identity claim.

## Exclusion Language

- If local neighborhoods match but cycle/twist differs: "locality probe
  co-survived; global topology alias excluded by cycle/twist witness."
- If cover count matches but projection fails: "cover cardinality co-survived;
  cover relation excluded by failed projection/lift check."
- If orbit sizes match but edges do not descend: "orbit multiset co-survived;
  quotient action excluded by adjacency/incidence failure."
- If a grid quotient is called lens without lens data: "lens name demoted to
  cyclic quotient label until action/descent receipt exists."
- If boundary-cost profiles match: "cost profile co-survived; topology identity
  remains open or excluded by separate topology probe."

## Carry Forward

- Keep identity statements in the form `same X under probe M`.
- Treat every topology name as a handle for a finite construction and a receipt,
  not as an object imported wholesale from smooth topology.
- Let negative controls be first-class: the designed-fail rows are how future
  topology aliases avoid becoming prose aliases.
