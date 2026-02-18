# 12 — DNS test protocol for SSL and residues

Goal: measure whether sublevel sets decay as \(\delta\to 0\), and measure the actual obstruction terms.

From DNS snapshot(s), compute:
1) \(|\omega(x)|\) field
2) Sublevel measure: \(m(\delta)=|\{|\omega|<\delta\}|/|\Omega|\)
3) Strain residue: \(R(\delta)=\int_{|\omega|<\delta}\|S\|_{op}dx\)
4) Fisher schedule: \(J_\varepsilon=\int |\nabla\omega|^2/(|\omega|^2+\varepsilon^2)dx\)
5) Gradient sublevel loads: \(Q_1(\delta)=\int_{|\omega|<\delta}|\nabla\omega|dx\), \(Q_2(\delta)=\int_{|\omega|<\delta}|\nabla\omega|^2dx\)

Then:
- Fit \(m(\delta)\sim \delta^\alpha\) over an inertial range of \(\delta\)
- Compare behavior of \(R(\delta)\) and \(J_\varepsilon\) against the needs of the proof chain.

This repo includes:
- `pcm.measure` — produces measurement JSON
- `pcm.fit_alpha` — fits \(\alpha\) with diagnostics
- `pcm.plot` — plots log-log fits and residue curves
