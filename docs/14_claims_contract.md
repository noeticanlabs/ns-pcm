# 14 — Claims contract (truth table)

This file is a hard boundary that prevents accidental overclaiming.

| ID | Claim | Depends on | Status |
|---:|------|------------|--------|
| C1 | Saturated functional \(\mathcal S_\varepsilon\) is well-defined, smooth for \(\varepsilon>0\) | definitions | **Proved** |
| C2 | Viscous evolution of \(\mathcal S_\varepsilon\) yields dissipation + explicit Fisher residue \(J_\varepsilon\) | commutator calculus | **Proved** |
| C3 | Region split by \(G\le M\), \(G>M\) controls stretching on B and A_1 | CF depletion + saturation | **Proved** |
| C4 | Remaining obstruction equals \(\mathcal R(\delta)=\int_{|\omega|<\delta}\|S\|_{op}\) | decomposition | **Proved** |
| C5 | Sublevel Set Lemma (SSL): \(|\{|\omega|<\delta\}|\le C\delta^\alpha\) for some \(\alpha>0\) | none | **Conjecture / Empirical** |
| C6 | If SSL holds (or comparable quantitative decay), the NS-PCM inequality chain closes | C1–C5 | **Conditional** |
| C7 | Global regularity of 3D NS follows from C6 | NS-PCM chain | **Conditional** |

**Allowed public summary:**  
“NS-PCM reduces remaining control to a quantitative sublevel-set property of vorticity; this repo provides the derivation and DNS tests.”

**Not allowed:**  
“NS-PCM solves Navier–Stokes” (unless C5 is proved).
