# 04 — Viscous evolution: dissipation + commutators

Differentiate \(\mathcal S_\varepsilon\) and decompose:
\[
\frac{d}{dt}\mathcal S_\varepsilon
= \text{(amplitude part)} + \text{(angular part)}.
\]

Amplitude part (schematic):
\[
\int 2\omega\cdot (\nu\Delta\omega)\,\Psi(G)\,dx
= -2\nu\int |\nabla\omega|^2\Psi(G)\,dx + \mathcal C^{(1)}_\varepsilon.
\]

Angular part uses \(\partial_t G = 2\nabla\xi : \nabla(\partial_t\xi)\) and
produces a negative angular dissipation plus commutators:
\[
\mathcal D_{ang} \sim \nu\int |\omega|^2\frac{|\nabla^2\xi_\varepsilon|^2}{(1+G)^2}\,dx.
\]

Net:
\[
\frac{d}{dt}\mathcal S_\varepsilon \le
-\mathcal D_\omega - \tfrac12\mathcal D_{ang} + \mathcal C_\varepsilon.
\]

The decisive issue: bound \(\mathcal C_\varepsilon\) uniformly in \(\varepsilon\).
