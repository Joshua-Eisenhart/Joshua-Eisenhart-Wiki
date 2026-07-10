# SINDy / Koopman Article Register - 2026-07-09

This is a research-source register, not Ratchet canon. It records the primary
papers and official software documentation used for the current
system-identification hypothesis.

## Governing-Equation Identification

1. Steven L. Brunton, Joshua L. Proctor, and J. Nathan Kutz, "Discovering
   governing equations from data by sparse identification of nonlinear
   dynamical systems," PNAS 113(15), 2016.
   - DOI: https://doi.org/10.1073/pnas.1517384113
   - Role: original SINDy sparse-library formulation.
   - Relevant boundary: the governing vector field must be sparse in the
     chosen candidate library; library choice and derivative quality remain
     assumptions.

2. Alan A. Kaptanoglu et al., "PySINDy: A comprehensive Python package for
   robust sparse system identification," JOSS 7(69), 3994, 2022.
   - Paper: https://joss.theoj.org/papers/10.21105/joss.03994
   - Official API: https://pysindy.readthedocs.io/en/stable/generated/pysindy.SINDy.html
   - Role: implementation and robust-method surface used by the local
     capability receipt.

3. Steven L. Brunton, Joshua L. Proctor, and J. Nathan Kutz, "Sparse
   Identification of Nonlinear Dynamics with Control."
   - Preprint: https://arxiv.org/abs/1605.06682
   - Role: controlled/input-dependent extension and an explicit bridge to DMD
     and Koopman theory.

## Finite-Time Operator Identification

4. Matthew O. Williams, Ioannis G. Kevrekidis, and Clarence W. Rowley, "A
   Data-Driven Approximation of the Koopman Operator: Extending Dynamic Mode
   Decomposition," Journal of Nonlinear Science 25, 1307-1346, 2015.
   - DOI: https://doi.org/10.1007/s00332-015-9258-5
   - Role: EDMD approximation of Koopman action in a selected observable
     dictionary.
   - Relevant boundary: finite-dimensional closure depends on the observable
     dictionary and does not follow merely from low prediction error.

5. Shaowu Pan et al., "PyKoopman: A Python Package for Data-Driven
   Approximation of the Koopman Operator," JOSS 9(94), 5881, 2024.
   - Paper: https://joss.theoj.org/papers/10.21105/joss.05881
   - Official docs: https://pykoopman.readthedocs.io/en/master/
   - Role: software surface for EDMD, DMD with control, kernel methods, HAVOK,
     and neural DMD.

## Generator / Operator Relation

6. Stefan Klus et al., "Data-driven approximation of the Koopman generator:
   Model reduction, system identification, and control," Physica D 406,
   132416, 2020.
   - Preprint: https://arxiv.org/abs/1909.10638
   - Role: generator EDMD and the mathematical relation between generator
     identification and SINDy-like governing-equation recovery.

## Local Source Repositories

Pinned upstream release checkouts:

```text
/Users/joshuaeisenhart/GitHub/pysindy   v2.1.0  1edf31260fc000692776b1f4259877e8b85e56e5
/Users/joshuaeisenhart/GitHub/pykoopman v1.2.1  61d24f765cd4799a3c84413950f43282977fa0e2
```

These are third-party source checkouts, not wiki authority and not
Codex-Ratchet evidence by themselves. Local API, environment, and simulation
receipts live in the Codex-Ratchet repository.

## Related Research Pages

- [[concepts/sindy-koopman-system-identification-for-qit-engines-2026-07-09]]
- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
- [[concepts/dual-ratchet-geometry-entropy-jordan-research-2026-07-09]]
