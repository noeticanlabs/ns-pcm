# Theoretical α for Vortex Filament

## Problem

Derive the expected sublevel set exponent α for a canonical 3D vortex filament — an axisymmetric tube with finite core radius where vorticity is concentrated along a 1D curve.

## Model: Axisymmetric Vortex Filament

Consider an isolated straight vortex filament aligned with the z-axis. The vorticity field is:

```
ω(r, φ, z) = ω_θ(r) e_θ
```

where:
- `r = sqrt(x² + y²)` is radial distance from filament axis
- `ω_θ(r)` is the azimuthal vorticity component
- The filament is aligned along the z-direction

### Core Profile

A generic smooth vortex filament has a core profile that is:

- Maximum at the axis: `ω_θ(0) = ω_max`
- Decays rapidly away from axis
- For smooth cores: `ω_θ(r) ≈ ω_max · (r/a)` near r=0 (linear in r)
- For specific models (Gaussian, exponential): `ω_θ(r) = ω_max · exp(-r²/a²)`

Near the axis, we can always Taylor expand:

```
ω_θ(r) = ω'_θ(0) · r + O(r²)
```

where `ω'_θ(0) = ω_max / a` defines the core scale `a`.

## Sublevel Set Analysis

The sublevel set is:

```
E_δ = { x ∈ ℝ³ : |ω(x)| < δ }
```

For our axisymmetric filament:

```
|ω(x)| = |ω_θ(r)| < δ
```

This defines a cylinder of radius `r_δ` where `|ω_θ(r_δ)| = δ`.

### Near-Axis Asymptotics

Using the linear approximation near the axis:

```
|ω| ≈ ω_max · (r/a)
```

Solving for r:

```
r_δ ≈ a · (δ / ω_max)
```

### Volume Scaling

The sublevel set is a cylinder of radius `r_δ` and length `L` (filament length):

```
|E_δ| = π r_δ² · L
      = π a² L · (δ / ω_max)²
      = C · δ²
```

where `C = π a² L / ω_max²` is a constant depending on filament geometry.

## Result

For a **vortex filament with smooth core**:

```
m(δ) = |E_δ| / Volume ~ δ²
```

Therefore:

```
α_filament = 2
```

## Physical Interpretation

- **Codimension 2**: A 1D curve in 3D has codimension 2
- The sublevel set volume scales as δ^(3-codim) = δ^(3-2) = δ¹
- Wait — let me reconsider...

Actually, more carefully:

- The set `{ |ω| < δ }` near a filament traces out a **tube** of radius ~ δ
- The cross-sectional area scales as δ²
- Length is independent of δ

So the volume scales as δ², giving α = 2.

This matches the geometric fact that filaments have **codimension 2** in 3D space.

## Generalization: Curved Filaments

For a curved filament with local radius of curvature R_curv >> a:

- Same local analysis applies
- α = 2 holds locally
- Globally, the same scaling holds if filament is long enough

## Generalization: Filament with Non-Smooth Core

If the core has a singularity (e.g., point vortex limit):

```
|ω| ~ r^{-s}   as r → 0
```

Then:

```
r_δ ~ δ^{1/s}
|E_δ| ~ δ^{2/s}
```

So:

```
α = 2/s
```

For the regular case s = 1 → α = 2.

## Summary

| Core Type | Near-axis behavior | α |
|-----------|-------------------|---|
| Smooth (generic) | |ω| ~ r | **2** |
| Gaussian | |ω| ~ exp(-r²) | 2 (near zero) |
| Point singularity | |ω| ~ r^{-s} | 2/s |

The canonical vortex filament gives **α = 2**.

This is distinct from:
- Smooth 3D field: α = 3
- Vortex sheet: α = 1
