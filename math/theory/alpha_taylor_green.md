# Theoretical α for Taylor-Green Vortex

## Exact Solution

The Taylor-Green vortex is an exact solution of incompressible Navier-Stokes:

```
u₁ = U(t) · cos x · sin y · sin z
u₂ = -U(t) · sin x · cos y · sin z  
u₃ = 0
```

where U(t) = exp(-2νt) decays exponentially in time.

## Vorticity

Computing ω = ∇ × u:

```
ω₁ = ∂u₃/∂y - ∂u₂/∂z = 0 - 0 = 0
ω₂ = ∂u₁/∂z - ∂u₃/∂x = U(t) · cos x · sin y · cos z - 0 = U · cos x · sin y · cos z
ω₃ = ∂u₂/∂x - ∂u₁/∂y = U(t) · sin x · cos y · sin z + U(t) · sin x · cos y · sin z 
    = 2U · sin x · sin y · sin z
```

Actually, let me recompute more carefully:

```
∂u₂/∂x = ∂(-U sin x cos y sin z)/∂x = -U cos x cos y sin z
∂u₁/∂y = ∂(U cos x sin y sin z)/∂y = U cos x cos y sin z
```

So:

```
ω₃ = ∂u₂/∂x - ∂u₁/∂y = -U cos x cos y sin z - U cos x cos y sin z 
    = -2U cos x cos y sin z
```

And:

```
ω₁ = ∂u₃/∂y - ∂u₂/∂z = 0 - ∂(-U sin x cos y sin z)/∂z 
    = U sin x cos y cos z
```

Wait, let me use the standard form. The classic TG vortex is:

```
u = (sin x cos y cos z, -cos x sin y cos z, 0) · U(t)
```

This gives:

```
ω = (0, 0, 2 sin x sin y sin z) · U(t)
```

So ω is purely in the z-direction with magnitude:

```
|ω| = 2|U(t)| · |sin x sin y sin z|
```

## Zero Set Structure

The vorticity vanishes when:
- sin x = 0 (i.e., x = 0, π, 2π, ...)
- OR sin y = 0 (i.e., y = 0, π, 2π, ...)
- OR sin z = 0 (i.e., z = 0, π, 2π, ...)

This is a **union of three families of parallel planes**:
- X-planes: x = kπ
- Y-planes: y = kπ  
- Z-planes: z = kπ

## Codimension Analysis

At a generic point where none of the sines vanish, |ω| > 0.

The zero set has three types of regions:

### 1. Triple intersections (points)
Where all three sin x = sin y = sin z = 0:
- This happens at (x,y,z) = (kπ, lπ, mπ)
- These are **isolated points** in 3D
- Codimension = 3 → α = 3

### 2. Double intersections (lines)
Where two vanish, one doesn't:
- e.g., sin x = sin y = 0 but sin z ≠ 0
- This gives lines: x = kπ, y = lπ, z arbitrary
- These are **curves** in 3D
- Codimension = 2 → α = 2

### 3. Single intersections (planes)
Where only one vanishes:
- e.g., sin x = 0, but sin y, sin z ≠ 0
- This gives planes: x = kπ, with y,z varying
- These are **surfaces** in 3D
- Codimension = 1 → α = 1

## Geometric Volume Analysis

In one period cell [0, 2π]³:
- Each family of planes divides space into regions
- The measure of each structure type:
  - **Points**: 0 measure (countable)
  - **Lines**: 0 measure (1D in 3D)
  - **Surfaces**: 2D measure in 3D → codimension 1

The dominant structure is the **planes** (codimension 1).

## Expected α

For the Taylor-Green vortex:

| Region Type | Codimension | α | Measure in Space |
|------------|-------------|---|------------------|
| Points | 3 | 3 | Zero |
| Lines | 2 | 2 | Zero |
| Planes | 1 | 1 | Non-zero (surfaces) |

The **effective α** is determined by the thickest structure:
- **α = 1** (plane-dominated)

This is because:
- The sublevel set { |ω| < δ } consists of neighborhoods around each plane
- Near a plane: |ω| ≈ |x - plane| (linear)
- Volume of δ-neighborhood of a plane = area × δ
- → m(δ) ~ δ

## Special Case: Early vs Late Time

At t = 0 (U(0) = 1):
- Maximum vorticity = 2
- Sublevel behavior as above

As t → ∞ (U → 0):
- |ω| → 0 everywhere
- The field becomes small but the structure remains the same

## Conclusion

The Taylor-Green vortex has:

- **Sheet-like zero structure** (union of planes)
- **Expected α = 1** (codimension 1)

This is the **dangerous case** for the SSL mechanism:
- If TG-like structures persist in real turbulence
- And α → 1 or below
- Then the residue term may not decay fast enough

## Physical Interpretation

The Taylor-Green vortex represents a prototypical "layer-like" vorticity structure. Its α = 1 prediction is a strong test:

- **DNS shows α > 1**: TG-like structures are unstable/rare in real turbulence
- **DNS shows α ≈ 1**: Sheet-like structures are significant
- **DNS shows α < 1**: Severe concentration (blowup warning)

This makes TG an excellent **diagnostic test case** for the SSL hypothesis.
