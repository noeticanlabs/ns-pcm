# NS-PCM (Navier–Stokes Polarization Coherence Method) — Reproducible Research Program

**Status:** research program repository (proof-conditional + falsifiable).  
**Primary goal:** reduce the remaining bottleneck in the NS-PCM inequality chain to a **measurable hypothesis** (Sublevel Set Lemma, SSL) and measure the **actual obstruction terms** directly in DNS data.

This repository is intentionally split into:
- **Docs**: continuous derivation (no skips), what is proved vs conjectured, claims contract.
- **Math**: theorem-shaped lemmas + explicit conjectures (SSL).
- **Code**: DNS I/O, measurements (sublevel sets, strain residue, Fisher-like term), fitting tools, plots.
- **Tests**: sanity checks on synthetic fields.

> **Important honesty clause**  
> This repository does **not** claim to solve the Clay Millennium problem.  
> It provides an explicit conditional chain: if **SSL** holds (or a comparable quantitative sublevel decay), then the remaining residue in NS-PCM closes.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Example: generate synthetic field snapshot
python -m pcm.tools.synthetic --out data/synth.h5 --n 64

# Measure sublevel distribution m(delta) and residue terms
python -m pcm.measure --in data/synth.h5 --out out/measure.json

# Fit alpha (power law exponent) from m(delta) ~ delta^alpha
python -m pcm.fit_alpha --in out/measure.json --out out/fit.json

# Plot results
python -m pcm.plot --measure out/measure.json --fit out/fit.json --out out/plots
```

## Data format (HDF5)

The code expects HDF5 snapshots containing either:
- `omega` dataset of shape `(3, n, n, n)` (vorticity), **or**
- `u` dataset of shape `(3, n, n, n)` (velocity), from which `omega = curl u` is computed.

Optional attributes:
- `nu` (viscosity)
- `t` (time)

## What gets measured (the important stuff)

- **Sublevel measure:** `m(delta) = |{x: |omega(x)| < delta}| / |domain|`
- **Residue term:** `R(delta) = ∫_{|ω|<δ} ||S||_op dx` (strain operator norm over sublevel set)
- **Fisher-like term:** `J_eps = ∫ |∇ω|^2 / (|ω|^2 + eps^2) dx` for a schedule of `eps`
- Additional diagnostics: `Q1(delta)=∫_{|ω|<δ}|∇ω| dx`, `Q2(delta)=∫_{|ω|<δ}|∇ω|^2 dx`

These correspond directly to the last obstruction in the proof chain.

## Folder map

- `docs/` — continuous derivation, claims contract, and proof/conjecture boundary
- `math/` — lemmas and conjectures, theorem-shaped
- `pcm/` — Python module: I/O, spectral derivatives, measurements, fitters
- `scripts/` — convenience wrappers
- `tests/` — basic tests for consistency

## License

See `LICENSE`. (Research use; **no** warranty.)
