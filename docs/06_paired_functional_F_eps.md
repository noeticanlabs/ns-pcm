# 06 — Paired functional to cancel the residue

Introduce:
\[
\mathcal F_\varepsilon(t) := \int \log(|\omega|^2+\varepsilon^2)\,dx.
\]

Viscous evolution includes:
\[
\frac{d}{dt}\mathcal F_\varepsilon
\le -\nu\int \frac{|\nabla\omega|^2}{|\omega|^2+\varepsilon^2}\,dx + \text{(stretching contribution)}.
\]

Thus \(\mathcal G_\varepsilon = \mathcal S_\varepsilon + \lambda\mathcal F_\varepsilon\) can cancel \(J_\varepsilon\),
but introduces a stretching sensitivity term:
\[
\int \frac{\omega^\top S\omega}{|\omega|^2+\varepsilon^2}\,dx.
\]

So we pivot to controlling this weighted stretching term.
