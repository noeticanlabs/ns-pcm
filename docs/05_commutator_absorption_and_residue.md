# 05 — Absorption and the Fisher-like residue

Careful commutator bookkeeping yields an inequality of the form:
\[
\frac{d}{dt}\mathcal S_\varepsilon
\le -\mathcal D_\omega - \tfrac12\mathcal D_{ang}
+ C\nu\|\omega\|_2^2
+ C\nu\int \frac{|\nabla\omega|^2}{|\omega|^2+\varepsilon^2}\,dx.
\]

The last term is the explicit obstruction:
\[
J_\varepsilon := \int \frac{|\nabla\omega|^2}{|\omega|^2+\varepsilon^2}\,dx.
\]

Everything else is absorbable by selecting parameters (e.g., region split threshold \(M\)).
So NS-PCM reduces to controlling \(J_\varepsilon\) (or an equivalent residue) uniformly.
