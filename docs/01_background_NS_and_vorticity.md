# 01 — Navier–Stokes and vorticity

In \(\mathbb T^3\) with viscosity \(\nu>0\), incompressible Navier–Stokes:
\[
\partial_t u + (u\cdot\nabla)u + \nabla p = \nu \Delta u,\quad \nabla\cdot u = 0.
\]
Vorticity \(\omega = \nabla\times u\) satisfies
\[
\partial_t \omega + (u\cdot\nabla)\omega = (\omega\cdot\nabla)u + \nu\Delta \omega.
\]
Enstrophy identity:
\[
\frac{d}{dt}\frac12\|\omega\|_2^2 + \nu\|\nabla\omega\|_2^2
= \int \omega^\top S\,\omega\,dx,
\]
where \(S = (\nabla u + (\nabla u)^\top)/2\) is the strain.

The right-hand side is the “vortex stretching” term, the classical obstacle.

NS-PCM reframes control of stretching via direction-field geometry.
