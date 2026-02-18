# 13 — Worklog: continuous show-work chain

This file is the “receipt trail” for NS-PCM.

## Step 1 — Define objects
- \(\omega=\nabla\times u\), \(\xi=\omega/|\omega|\), \(\xi_\varepsilon\)

## Step 2 — Pick functional
- \(\mathcal S_\varepsilon=\int |\omega|^2\Psi(G)\), \(\Psi(G)=G/(1+G)\)

## Step 3 — Differentiate and decompose
- amplitude part + angular part
- identify dissipation terms

## Step 4 — Isolate residue
- obtain Fisher-like term \(J_\varepsilon\)

## Step 5 — Pair functional
- \(\mathcal F_\varepsilon=\int\log(|\omega|^2+\varepsilon^2)\)
- cancels \(J_\varepsilon\) in viscosity, exposes weighted stretching

## Step 6 — Split by directional complexity
- Region A/B split by \(G\le M\) vs \(G>M\)

## Step 7 — Control B
- absorbable by \(\mathcal D_{ang}\)

## Step 8 — Control A_1
- Constantin–Fefferman depletion from local Lipschitz control

## Step 9 — Residue A_2
- \(\mathcal R(\delta)=\int_{|\omega|<\delta}\|S\|_{op}\)
- reduce success to sublevel decay / control

## Step 10 — Conjecture (SSL)
- If \(|\{|\omega|<\delta\}|\le C\delta^\alpha\) with \(\alpha>0\) (or comparable quantitative decay),
  then \(\mathcal R(\delta)\to 0\) sufficiently fast to close the chain.

## Step 11 — Falsifiability
- DNS pipeline measures \(m(\delta)\), \(R(\delta)\), \(J_\varepsilon\) directly.

That’s the program. No skipped steps.
