last_updated: 2026-04-16

# PyTorch as Ratchet Architecture

The computational graph IS the ratchet. Not a tool used by the ratchet. Not a convenient library. The architecture itself.

---

## Three-Part Identity

**Forward pass = space of possible survivors.**
Running the forward pass is not computation of an answer. It is the enumeration of paths that are not yet excluded. Each tensor operation is a candidate. Numerical results are provisional — they are what survived gradient-aware propagation up to this point.

**Backward pass = constraint elimination.**
The backward pass is where the constraint manifold acts. Gradients are not optimization signals in the classical sense. They are admissibility derivatives: which inputs are load-bearing under the current loss structure, and which have zero gradient (redundant under current constraints). High gradient = this quantity is coupled with constraint satisfaction. Zero gradient = decoupled, effectively invisible to the manifold.

**Autograd graph = manifold topology.**
The computational graph PyTorch builds during the forward pass is not a bookkeeping artifact. It is the topology of the constraint manifold — which quantities are downstream of which constraints, which are separated by which operations. When you manipulate that graph (detach, clone, custom backward), you are editing the manifold topology itself.

---

## Why Numpy Is a Category Error

Numpy operates on coordinates. A numpy array is a Cartesian grid. It imports Platonic/Cartesian ontology — objects at positions, no relational structure, no constraint flow.

PyTorch computational graphs are relational — edges, not coordinates. This is not a style preference. It is the correct ontological substrate for constraint-based geometry.

Using numpy for geometry is not a fallback. It is a category error: you are computing on a different kind of object (Cartesian) than the one the system requires (relational-constrained). Classical results from numpy arrays are useful as **baselines** only — they show what survives without constraint. They are not answers.

The contamination test: if your geometry sim uses `np.dot` or `np.einsum` as load-bearing operations, it is a classical baseline by construction. It cannot serve as evidence for nonclassical geometry, regardless of how the result looks.

---

## Axis 0 Implication

Axis 0 is not a scalar I_c. It is ∇I_c on shell topology, flowing backward through torus shells via autograd. The reason Axis 0 was blocked for so long: I_c was computed as a number (numpy-compatible), not as a gradient field. A gradient field requires the computational graph. Scalars do not carry manifold information.

---

## Practical Rules

- All new computation: PyTorch tensors, not numpy arrays
- PyG message passing is the dynamics — not decoration
- Autograd is the constraint flow — not a separate analytical step
- Clifford rotors encoded as torch operations, not matrix multiply
- TopoNetX provides topology that shapes the graph structure
- If you must use numpy: label it `classical_baseline` in the sim classification field

---

See [02_constraint_admissibility_primer.md](02_constraint_admissibility_primer.md) for elimination vs. generation.
See [05_four_sim_kinds.md](05_four_sim_kinds.md) for classical vs. nonclassical sim classification.
