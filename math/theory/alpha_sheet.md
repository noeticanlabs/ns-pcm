# Theoretical α for Vortex Sheet

## Problem

Derive the expected sublevel set exponent α for a canonical 2D vortex sheet — a surface across which vorticity is concentrated, modeled as a smooth layer with rapid variation across thickness.

## Model: Planar Vortex Sheet

Consider a planar vortex sheet aligned with the xy-plane. The vorticity is:

```
ω(x, y, z) = ω_s(z) e_x  (or any fixed in-plane direction)
```

where `ω_s(z)` is a function that rapidly transitions across z = 0.

### Sheet Profile

A smooth approximation to a discontinuity is the **hyperbolic tangent** layer:

```
ω_s(z) = ω_0 · tanh(z / δ_s)
```

where:
- `ω_0` = maximum vorticity jump across sheet
- `δ_s` = sheet thickness (small parameter)

As `δ_s → 0`, this approaches a true discontinuity (the classical vortex sheet).

## Sublevel Set Analysis

The sublevel set is:

```
E_δ = { x ∈ ℝ³ : |ω(x)| < δ }
```

For our planar sheet:

```
|ω(x, y, z)| = |ω_s(z)| < δ
```

This defines a **slab** (two parallel planes) centered on z = 0.

### Near-Center Asymptotics

Near z = 0, Taylor expand tanh:

```
tanh(z/δ_s) ≈ z/δ_s for |z| << δ_s
```

So:

```
|ω(z)| ≈ ω_0 · |z| / δ_s
```

Solving for the boundary:

```
|z| < z_δ where z_δ = δ_s · (δ / ω_0)
```

### Volume Scaling

The sublevel set is a slab of thickness `2z_δ` and infinite area (in the idealization):

```
|E_δ| = Area · (2z_δ)
      = A · 2δ_s · (δ / ω_0)
      = C · δ
```

where `C = 2Aδ_s/ω_0` is constant.

In a periodic domain of size L³, the fractional measure is:

```
m(δ) = |E_δ| / L³ ~ δ
```

## Result

For a **vortex sheet with smooth transition**:

```
m(δ) ~ δ
```

Therefore:

```
α_sheet = 1
```

## Physical Interpretation

- **Codimension 1**: A 2D surface in 3D has codimension 1
- The sublevel set volume scales as δ^(3-codim) = δ^(3-1) = δ²
- But we need to account for the thickness scaling...

Actually, more carefully:
- The set `{ |ω| < δ }` traces out a **slab** of thickness ~ δ
- Area is independent of δ
- Volume scales as δ¹

This gives α = 1, matching the **codimension 1** nature of sheets.

## Comparison with Other Structures

| Structure | Codimension | Geometric Scaling | α (theoretical) |
|-----------|-------------|------------------|-----------------|
| Smooth field | 0 | Ball: r ~ δ → V ~ δ³ | 3 |
| Vortex sheet | 1 | Slab: thickness ~ δ → V ~ δ | 1 |
| Vortex filament | 2 | Cylinder: area ~ δ² → V ~ δ² | 2 |
| Point | 3 | Point: V ~ δ⁰ | 0 |

## Generalization: Curved Sheet

For a non-planar, curved vortex sheet with local radius of curvature R >> δ_s:

- Same local analysis applies
- α = 1 holds locally
- Global topology may affect the constant but not the exponent

## Generalization: Multiple Sheets

If the flow contains multiple sheets at different orientations:

- The sublevel set is a union of slabs
- Local analysis still gives α = 1 near each sheet
- Global α is determined by the "most singular" structure present

## Summary

| Sheet Type | Profile | α |
|------------|---------|---|
| Smooth tanh layer | ω ~ tanh(z/δ) | **1** |
| Exponential layer | ω ~ exp(-|z|/δ) | 1 (near zero) |
| Discontinuity limit | δ_s → 0 | 1 |

The canonical vortex sheet gives **α = 1**.

This is the **dangerous case** for NS regularity:
- If real turbulence is sheet-dominated (α ≈ 1)
- The residue term R(δ) may not decay fast enough to close the estimate
- This would indicate potential blowup vulnerability
