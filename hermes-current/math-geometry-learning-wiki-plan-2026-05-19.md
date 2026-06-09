# Math and Geometry Learning Wiki Plan — 2026-05-19

Purpose: make the wiki useful for learning the mathematics and geometry of Josh's system, including screenshot-derived math, G-structures, manifold layers, operators, entropy, terrain tables, and source-doc geometry.

Status: active planning/control note.

## Correction being preserved

The wiki should teach the system's math and geometry. It should not only say how a repo sim or queue row uses a term.

A reader should be able to open the wiki and learn:

- what the mathematical object is
- what problem it solves
- how it appears in the system
- how it relates to neighboring math
- what examples make it concrete
- what is known, candidate, speculative, stale, or repo-proven
- what source screenshots/docs support it

Screenshot math is source material. It needs OCR/vision extraction, concept routing, and explanation. It should not remain buried as image filenames.

## Screenshot source root

Primary screenshot source root already mirrored into the wiki:

`/Users/joshuaeisenhart/wiki/raw/articles/system-v5-reference-docs/Screenshots`

Observed 2026-05-19: 26 image files.

Examples observed:

- `Common Operators.png`
- `Topology.png`
- `Terrain.png`
- `Sim shape.png`
- `Yin and yang.png`
- `Can it operate directly on leftjright Weyt spinors.png`
- `The actuel candidene math we've been ceeling la lunt thit, once, in one table.png`
- multiple dated March 28 screenshots

Do not rewrite raw screenshots. Extract into derived source cards, concept pages, and curriculum maps.

## Sample extraction receipts from 2026-05-19

### `Common Operators.png`

Readable content includes:

- density operators: `rho in D(H)`
- Bloch-sphere / Pauli representation: `rho = 1/2 (I + r · sigma)`
- Hamiltonian: `H_0 = 1/2 (n_x sigma_x + n_y sigma_y + n_z sigma_z)`
- projective/dephasing map: `Pi_P(rho) = sum_k P_k rho P_k`
- quantum filter / normalized operation: `F_Q(rho) = F rho F† / Tr(F rho F†)`
- lowering/raising dissipators `D_-(rho)`, `D_+(rho)` using `sigma_-`, `sigma_+` and anticommutators
- projector dissipator/dephasing-like operator `D_P(rho) = sum_j (P_j rho P_j - 1/2(P_j rho + rho P_j))`
- ladder operators: `sigma_± = 1/2 (sigma_x ± i sigma_y)`
- visible label: `Inward Terrains`

Concept pages suggested:

- density operators and state space
- Bloch vectors and Pauli coordinates
- Pauli matrices as system operators
- Hamiltonian vector fields / Pauli Hamiltonians
- projectors and dephasing maps
- quantum filters and normalized updates
- Lindblad dissipators
- ladder operators and raising/lowering maps
- inward terrain operators
- terrain-to-operator dictionary

### `Topology.png`

Readable content includes large topology/terrain tables:

- Type-1 and Type-2 full charts
- topology labels: `Se`, `Ne`, `Ni`, `Si`
- terrain labels such as `Se-in`, `Ne-in`, `Ni-in`, `Si-in`, `Se-out`, etc.
- loop classes: `Outer / Major`, `Inner / Minor`
- order families: `Deductive`, `Inductive`
- stage tokens: examples `TiSe`, `NeTi`, `NiFe`, `FeSi`, `SeFi`, `SiTe`, `TeNi`, `FiNe`
- Axis 6 signs: `UP`, `DOWN`
- signed operators: examples `Ti↑`, `Ti↓`, `Fe↑`, `Fe↓`, `Fi↑`, `Te↓`
- result/pattern tokens: `WIN`, `LOSE`, `win`, `lose`, `LOSEwin`, `WINlose`, etc.

Concept pages suggested:

- topology chart grammar
- inner/outer terrain loops
- major/minor loop distinction
- inductive vs deductive order families
- stage-token algebra
- signed operators and Axis 6 orientation
- WIN/LOSE pattern grammar
- topology-aligned comparison
- IGT terrain grammar as symbolic/correlation layer

### Candidate math table screenshot

Readable content includes:

- statement that the actual candidate math is one table
- terrain names: Funnel, Cannon, Vortex, Spiral, Pit, Source, Hill, Citadel
- Jungian labels: Se, Ne, Ni, Si
- Type 1 / Type 2
- Lindblad matrices `L`
- Hamiltonian matrices `H`
- master equation form: `d rho / dt = -i(H rho - rho H) + L rho L† - 1/2(L†L rho + rho L†L)`
- note: the only thing changing between Type 1 and Type 2 is the sign of the Hamiltonian matrix

Concept pages suggested:

- eight terrains as operator families
- Lindblad matrix terrain candidates
- Hamiltonian sign flip and Type 1/Type 2 distinction
- open quantum systems primer
- master equation primer
- terrain dynamics under Hamiltonian plus dissipator
- candidate-vs-canonical math table fencing

## Curriculum map: math and geometry of the system

This should become a reader-facing curriculum, not just a result ledger.

### Layer 1 — Foundations and state spaces

Pages to create/deepen:

- distinguishability and identity-as-probe
- state spaces and admissible states
- density operators
- Hilbert spaces and projective spaces
- Bloch sphere / Bloch ball
- Pauli coordinates
- Weyl spinors
- left/right Weyl spinor distinction
- chirality
- spin groups and Clifford algebras

### Layer 2 — Manifold and carrier geometry

Pages to create/deepen:

- manifolds as support/carrier spaces
- nested Hopf tori
- Hopf fibration
- fiber bundles
- bundle towers
- foliations
- tangent/cotangent bundles
- support manifolds vs dynamics on support
- shell / layer geometry
- G-structures
- reductions of structure group
- torsion, curvature, connection, holonomy
- obstructions and refinements
- coexistence of manifold layers

### Layer 3 — Operators and dynamics

Pages to create/deepen:

- Hamiltonians
- Pauli Hamiltonians
- projectors
- filters / normalized quantum updates
- dephasing maps
- Lindblad operators
- Lindblad master equation
- dissipators
- raising/lowering operators
- signed operators
- terrain operators
- commutator and anticommutator
- noncommutation as constraint, not decoration

### Layer 4 — Entropy, information, and admissibility

Pages to create/deepen:

- entropy as downstream measurement, not primitive ontology
- von Neumann entropy
- relative entropy
- mutual information
- entanglement entropy
- channel capacity
- coarse graining
- distinguishability loss
- admissibility under constraints
- negative controls and entropy baselines
- entropy tables from source docs

### Layer 5 — Topology and higher structure

Pages to create/deepen:

- topology as survivor structure
- homology / cohomology
- persistent homology
- cell complexes
- hypergraphs and simplicial complexes
- sheaves or presheaf-like gluing if warranted
- obstruction theory
- topology-aligned terrain comparison
- G-structure/topology interface

### Layer 6 — Terrain / symbolic / IGT correlation layer

Pages to create/deepen:

- terrain grammar
- eight terrain names and their candidate operators
- IGT win/lose grammar
- stage-token algebra
- inner/outer loops
- inductive/deductive families
- Axis 6 signed orientation
- yin/yang symbolic layer
- I-Ching / hexagram state-space as symbolic/correlation layer

Fencing: this layer can be valuable and highly connected, but symbolic correlation is not automatically math anchor or proof.

### Layer 7 — System integration and repo application

Pages to create/deepen:

- how manifold layers, operators, entropy, and terrains fit together
- candidate vs canonical math surfaces
- what current sims actually support
- what remains source-derived / screenshot-derived / proposal-only
- tool witnesses: z3, cvc5, sympy, Clifford, geomstats, e3nn, rustworkx, XGI, TopoNetX, GUDHI, PyG, PyTorch/autograd

## 2026-05-19 root-constraint attractor-basin correction

Formal-sim correction from live Codex Ratchet goal tuning:

The geometric constraint manifold / attractor-basin surface must be rebuilt from the two root constraints explicitly, not only implicitly. Future LLM workers must see this as a first-class gate:

- `F01_FINITUDE`: finite carriers, witnesses, registries, cell complexes, or bounded probe surfaces.
- `N01_NONCOMMUTATION`: order-sensitive noncommuting composition with finite witnesses.

A manifold, basin, gauge, engine, axis, or layer claim does not advance unless both roots are explicitly tested and independently ablated.

This changes the math/geometry wiki lane too. Educational pages should explain G-structures, manifold layers, operators, entropy, terrains, and basins as candidate realizations or consequences under F01 + N01 pressure, not as assumed primitives.

### Basin/manifold claim checklist

Any basin/manifold page or sim-facing concept needs:

- admissibility predicate
- state space
- update rule
- basin boundary
- stability invariant
- escape/failure cases
- at least one killed non-manifold explanation
- root-off, F01-only, and N01-only ablations

Similarity, clustering, repeated motifs, or model agreement is not convergence.



### Existing G-structure variant sim work correction

Correction: the G-structure variants are not merely future possibilities. Existing result surfaces include v4 classical-baseline tower/obstruction sims and v5 formal scouts for nested symbolic G-reduction live state, reduction permutation compatibility, semantic nesting/order falsifiers, semantic family permutation falsifiers, semantic layer/operator coupling, root-manifold holonomy chart invariance, and full thirteen-layer active G-structure both-chiral source-native composition. Most recent v5 surfaces are `formal_scout` with `promotion_allowed=false`; they should guide educational routing and negative-control design without promoting final manifold/final G-structure claims. See [[g-structure-tower#Variant-specific sim work already exists]].

### Multiple G-structures correction

There are multiple G-structures involved, not one generic `G-structure`. The curriculum must distinguish smooth/frame, Riemannian/O(n), oriented/SO(n), Spin, almost-complex/U(n), symplectic/Sp-type, Kähler, contact, Sasakian, Hopf/principal-bundle, and associated Weyl-spinor bundle structures where relevant. Each has its own carrier, obstruction logic, observables, and F01+N01 admission tests. See [[g-structure-tower#Multiple G-structures, not one ladder]].

### Retune targets for the first 40 pages

The first-40 curriculum pages should include root-constraint sections where relevant:

- Which part is finite / bounded?
- Which composition is noncommuting / order-sensitive?
- What is the ablation if F01 is off?
- What is the ablation if N01 is off?
- What would make this page merely an analogy rather than an admitted layer?

Especially affected pages:

- `manifolds-as-support-carriers`
- `nested-hopf-tori`
- `fiber-bundles`
- `bundle-towers-and-layered-support`
- `g-structures`
- `g-structure-reductions-and-obstructions`
- `coexistence-of-manifold-layers`
- `hamiltonians`
- `commutators-and-noncommutation`
- `lindblad-master-equation`
- `entropy-as-downstream-measurement`
- `topology-as-survivor-structure`
- `terrain-operator-families`

### Formal-sim goal now running

The live formal-sim campaign goal is to prove or kill whether `F01_FINITUDE` plus `N01_NONCOMMUTATION` forces a layered finite noncommutative geometry and central emergent ratchet / attractor-basin surface.

Key requirements from that goal:

- gauge symmetry, quaternion/SU(2)/Spin carriers, Hopf/S3 structure, cellular finite gradations, and ring-checkerboard models are candidate realizations, not primitives
- separate gauge representatives from gauge-invariant observables
- test whether cellular/ring-checkerboard carriers solve the non-infinite-gradation problem
- PyTorch-native 8/16/32/64 qubit-site tensor-network scouts should record bond/rank assumptions, contraction order, observables, stability invariants, and failure modes
- z3/cvc5/SymPy/Clifford/rustworkx/XGI/TopoNetX/GUDHI/PyTorch/PyG/e3nn/auto_LiRPA/le-wm claims need canonical receipts when load-bearing
- every loop needs premortem plus hard negatives: root-off, F01-only, N01-only, gauge-broken/transplanted, quaternion-vs-complex, cellular-vs-continuous, ring-checkerboard ablation, pressure-off, reverse/order-shuffle, symmetric-flux, cross-shell transplant, null/tool-stub, classical baseline, and apparent-basin-without-manifold

Wiki consequence: do not write basin/manifold educational pages as if the attractor basin is already granted. Teach the math, then state whether and how F01 + N01 force or fail to force the structure.

## Page template for math concept pages

Each math/geometry concept page should use this shape:

1. What this is
2. Why it matters generally
3. Minimal example
4. Mathematical definition / formulas
5. Intuition
6. How it appears in Josh's system
7. Source/screenshot anchors
8. Research/tool connections
9. What is proven / simulated / candidate / speculative
10. Related pages and next reading

## Parallel worker plan

This is a large parallel task. When Sonnet high / Claude Code is available, use workers.

Parent lanes:

1. Screenshot OCR/vision parent
   - children each process 1-3 screenshots
   - output exact formulas, visible labels, concept candidates, page suggestions

2. G-structure/manifold parent
   - children process source docs and existing wiki pages for G-structures, manifolds, bundles, Hopf tori, foliations, obstruction/refinement

3. Operator/dynamics parent
   - children process Hamiltonian, Lindblad, Pauli, projector, dissipator, terrain operator screenshots/docs

4. Entropy/information parent
   - children process entropy tables, distinguishability loss, mutual information, entanglement, channel/capacity source docs

5. Terrain/symbolic parent
   - children process IGT, topology tables, win/lose grammar, yin-yang/I-Ching symbolic docs

6. Curriculum synthesis parent
   - turns receipts into an ordered learning path and page queue

## Child receipt format

Each child should return:

- source paths read/analyzed
- whether source is screenshot/doc/thread/result/code
- OCR/formula extraction
- plain-English explanation
- mathematical background needed
- system-specific interpretation
- status fence: educational / candidate / source-derived / repo-supported / stale / speculative
- pages to create/deepen
- dependencies: what reader should read first
- open questions / needed research

## Immediate next tranche

Before large worker launch:

1. make a screenshot manifest with dimensions, filenames, and rough topic labels
2. process all 26 screenshots through vision/OCR workers
3. create a screenshot-source ledger
4. create first five educational concept pages from the clearest screenshots:
   - density operators and Bloch vectors
   - Lindblad operators and dissipators
   - Hamiltonian sign flip and terrain types
   - topology/terrain chart grammar
   - G-structures and manifold-layer reductions
5. route those pages into the broader math curriculum map

## First 40 math/geometry learning pages

User-approved first set size: 40 pages. This is a good first curriculum batch for the math/geometry wiki lane. These should be educational pages first, with source/screenshot/repo application fenced as later sections.

### A. State spaces, spinors, and identity foundation

1. `distinguishability-and-identity-as-probe`
   - teach: identity as probe-relative distinguishability, not primitive equality
2. `state-spaces-and-admissible-states`
   - teach: state spaces, admissible subsets, constraints as selection
3. `hilbert-spaces-and-projective-state-spaces`
   - teach: Hilbert space, rays/projective states, why phase/gauge matters
4. `density-operators`
   - teach: mixed states, positive trace-one operators, measurement/readout
5. `bloch-vectors-and-pauli-coordinates`
   - teach: Bloch ball/sphere, Pauli expansion, geometric intuition
6. `weyl-spinors`
   - teach: two-component spinors, chirality, relation to Lorentz/spin structure
7. `left-right-weyl-spinor-distinction`
   - teach: left/right chirality as a structural split, not a label only
8. `chirality-and-orientation`
   - teach: handedness, sign, orientation, and why chirality is load-bearing
9. `clifford-algebras-and-spin-groups`
   - teach: Clifford generators, rotors/spin groups, why they carry geometry
10. `pauli-matrices-as-system-generators`
   - teach: sigma_x/y/z as operators, coordinates, rotations, and probes

### B. Manifold, bundle, and G-structure geometry

11. `manifolds-as-support-carriers`
   - teach: manifolds as support spaces where fields/operators live
12. `nested-hopf-tori`
   - teach: Hopf tori, nested carrier geometry, why support order matters
13. `hopf-fibration`
   - teach: S3 -> S2 fibers, phase circles, spinor/Bloch relation
14. `fiber-bundles`
   - teach: base, fiber, total space, local triviality, gluing
15. `bundle-towers-and-layered-support`
   - teach: stacked bundles/layers, runs-on relations, support order
16. `foliations-and-shell-families`
   - teach: decomposing spaces into leaves/shells, local families
17. `connections-curvature-and-holonomy`
   - teach: parallel transport, curvature, loop memory/phase
18. `g-structures`
   - teach: frame-bundle reductions, structure groups, geometric constraints
19. `g-structure-reductions-and-obstructions`
   - teach: when reductions exist/fail, obstruction/refinement logic
20. `coexistence-of-manifold-layers`
   - teach: when layers can jointly live on the same support without contradiction

### C. Operators and dynamics

21. `hamiltonians`
   - teach: generators of unitary dynamics and energy-like structure
22. `pauli-hamiltonians`
   - teach: H = n · sigma / 2, Bloch rotations, vector-generator view
23. `commutators-and-noncommutation`
   - teach: commutator, incompatibility, noncommutation as constraint
24. `anticommutators-and-dissipative-terms`
   - teach: anticommutator role in Lindblad equations
25. `projectors-and-measurement-maps`
   - teach: projectors, subspace selection, measurement/dephasing
26. `dephasing-and-projection-channels`
   - teach: Pi_P(rho), loss of off-diagonal distinguishability
27. `quantum-filters-and-normalized-updates`
   - teach: F rho F† / Tr(F rho F†), selected update maps
28. `lindblad-operators`
   - teach: open-system jump/noise operators
29. `lindblad-master-equation`
   - teach: Hamiltonian + dissipator equation, trace preservation
30. `raising-and-lowering-operators`
   - teach: sigma_±, transitions, source/sink-like behavior

### D. Entropy, topology, and terrain grammar

31. `entropy-as-downstream-measurement`
   - teach: entropy is a readout of admissible/coarse-grained structure, not primitive ontology
32. `von-neumann-entropy`
   - teach: S(rho), spectra, mixedness, quantum uncertainty
33. `relative-entropy-and-distinguishability-loss`
   - teach: divergence, distinguishability, constraint pressure
34. `mutual-information-and-correlations`
   - teach: shared information, correlation structure, reduced-state cautions
35. `entanglement-entropy`
   - teach: bipartitions, reduced states, why full structure matters
36. `topology-as-survivor-structure`
   - teach: topology as invariant/surviving relation under transformations
37. `homology-and-persistent-homology`
   - teach: holes, persistence, shape under scale/filtration
38. `terrain-operator-families`
   - teach: eight terrain names as candidate operator/dynamics families
39. `topology-terrain-chart-grammar`
   - teach: Se/Ne/Ni/Si, inner/outer, major/minor, inductive/deductive tables
40. `win-lose-stage-token-algebra`
   - teach: WIN/LOSE grammar, stage tokens, symbolic/correlation status fences

### Batch rule

Do not create all 40 as thin stubs. Process them in sub-batches of 5-8 pages. Each page should be readable enough to teach the topic, with at least one example, one system connection, and a status fence.

Related notes:

- [[source-corpus-deep-reading-parallel-plan-2026-05-19]]
- [[wiki-ingest-queue-and-priorities]]
- [[read-only-source-doc-processing-ledger-2026-05-18]]

Write mode: controller-maintained.
