# 02 — Direction field and regularization

The vorticity direction field \(\xi = \omega/|\omega|\) is undefined at \(\omega=0\).
Introduce a smooth regularization:
\[
r_\varepsilon := \sqrt{|\omega|^2+\varepsilon^2},\qquad
\xi_\varepsilon := \omega/r_\varepsilon.
\]
Then \(|\xi_\varepsilon|\le 1\) and \(\xi_\varepsilon\to \xi\) away from zeros.

Directional complexity:
\[
G_\varepsilon := |\nabla \xi_\varepsilon|^2.
\]

Key viscous identity (pure viscosity, or viscous piece of dynamics):
\[
\partial_t \xi_\varepsilon
= \nu (I-\xi_\varepsilon\otimes\xi_\varepsilon)\Delta\xi_\varepsilon
+ \frac{2\nu}{r_\varepsilon}(I-\xi_\varepsilon\otimes\xi_\varepsilon)(\nabla r_\varepsilon\cdot \nabla\xi_\varepsilon)
+ \cdots
\]
The first term is angular diffusion. The second is amplitude-gradient drift.
The whole program is about building a functional where this drift is controlled.
