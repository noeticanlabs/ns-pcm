# 00 — Overview

NS-PCM is a research program for 3D incompressible Navier–Stokes regularity built around a **polarization / direction field** viewpoint of vorticity.

Core objects:
- Vorticity: \(\omega = \nabla \times u\)
- Direction field: \(\xi = \omega/|\omega|\) (singular when \(\omega=0\))
- Regularized direction: \(\xi_\varepsilon = \omega/\sqrt{|\omega|^2+\varepsilon^2}\)
- Directional complexity: \(G = |\nabla \xi_\varepsilon|^2\)

Core engineering goal:
1) isolate the last obstruction term in the inequality chain,
2) reduce it to a **measure-theoretic hypothesis** (SSL),
3) make that hypothesis directly testable in DNS.

This repo includes both:
- The **proof-conditional chain** (with explicit boundary between proved and conjectured),
- A **measurement pipeline** to test the conjectured hypothesis and the obstruction terms.

See:
- `docs/11_what_is_proved_vs_conjectured.md`
- `docs/14_claims_contract.md`
