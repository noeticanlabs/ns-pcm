# Plan: Derive α from Exact Navier-Stokes Solutions

## Objective

Derive the expected sublevel set exponent α for canonical exact solutions of 3D Navier-Stokes:
- Taylor-Green vortex
- Burgers vortex (axisymmetric)
- Beltrami (ABC) flows

This provides **benchmark predictions** to compare against DNS measurements and validate (or invalidate) the SSL corridor.

---

## Why Exact Solutions Matter

Exact solutions give us:
1. **Known vorticity structure** — we know the exact field
2. **Theoretical α prediction** — we can compute analytically what α should be
3. **Verification** — if DNS matches these, the framework is consistent

---

## Case 1: Taylor-Green Vortex

### Exact Solution

The Taylor-Green vortex is:

```
u = (sin x cos y cos z, -cos x sin y cos z, 0) · U(t)
p = -(1/8)(cos 2x + cos 2y)(1 + cos² z) · U(t)²
```

where U(t) = exp(-2νt).

### Vorticity

```
ω = ∇ × u = (0, 0, sin x sin y sin z) · U(t)
```

Vorticity is purely in the z-direction, with magnitude:

```
|ω| = |U(t)| · |sin x sin y sin z|
```

### Zero Set Structure

The vorticity vanishes when:
- sin x = 0, OR
- sin y = 0, OR
- sin z = 0

This is a **union of three families of planes**:
- x = 0, π, 2π, ...
- y = 0, π, 2π, ...
- z = 0, π, 2π, ...

### Codimension Analysis

Near a generic intersection (where all three vanish):
- This is a **point** (0D) in 3D
- Codimension 3 → α = 3

Near a line intersection (where two vanish, one doesn't):
- This is a **curve** (1D) in 3D
- Codimension 2 → α = 2

Near a surface (where one vanishes):
- This is a **plane** (2D) in 3D
- Codimension 1 → α = 1

### Expected α

The Taylor-Green vortex has mixed structure:
- Most zeros are at surfaces (planes) → α ≈ 1 locally
- But the overall scaling depends on the measure of each type

**Prediction:** α ≈ 1–2 (sheet-like behavior dominates in early time)

---

## Case 2: Burgers Vortex

### Exact Solution

The axisymmetric Burgers vortex (stretched vortex tube):

```
u_r = -α r / 2
u_θ = Γ/(2πr) [1 - exp(-r²/a(t))]  
u_z = α z

with a(t) = a₀ exp(α t)
```

where α > 0 is the strain rate, Γ is circulation.

### Vorticity

In cylindrical coordinates (r, θ, z):

```
ω_r = 0
ω_θ = Γ/(πa²) · exp(-r²/a²)  (azimuthal vorticity)
ω_z = α
```

The magnitude:

```
|ω| = sqrt( ω_θ² + α² )
```

For r ≪ a (near axis):
- ω_θ ≈ (Γ/πa²) · (1 - r²/a²)
- |ω| ≈ sqrt( (Γ/πa²)² + α² ) ≈ const

For r ≫ a (far from core):
- ω_θ → 0 exponentially
- |ω| → α

### Zero Set Structure

The vorticity has:
- **No zeros near the core** (|ω| > 0 everywhere)
- **Asymptotic approach to α** at infinity

For the sublevel set analysis, the relevant scale is:
- The core radius a(t)
- The circulation Γ

### Expected α

Since this is an **isolated vortex tube** (no zeros in the interior):
- The sublevel set is the **complement** of the core
- For r ≫ a: |ω| ≈ α (constant)
- For r → ∞: |ω| → α

This is different from previous cases — Burgers vortex doesn't have zeros!

**Alternative analysis:** Consider set where |ω| < δ for small δ:
- This happens when ω_θ is small, i.e., far from the tube core
- The region is essentially the entire domain outside the tube
- Volume fraction → 1 as δ → 0

**Prediction:** α → 0 (sublevel set is almost everything for small δ)

---

## Case 3: ABC Flow (Beltrami)

### Exact Solution

ABC (Arnold-Beltrami-Childress) flow:

```
u = (A sin z + C cos y, B sin x + A cos z, C sin y + B cos x)
```

For A = B = C = 1 (classic case):

```
u = (sin z + cos y, sin x + cos z, sin y + cos x)
```

### Properties

- **Beltrami**: u · ω = 0 (but u = ω for ABC!)
- Actually: ω = u for ABC flow (eigenvector of curl with eigenvalue 1)
- No dissipation in the inviscid limit

### Vorticity

Since ω = u for ABC:

```
|ω| = |u| = sqrt( (sin z + cos y)² + (sin x + cos z)² + (sin y + cos x)² )
```

### Zero Set

The zeros occur where |u| = 0:

Three equations:
1. sin z + cos y = 0
2. sin x + cos z = 0
3. sin y + cos x = 0

These define a **complex periodic structure** — the ABC flow has chaotic streamlines but no simple zero set.

### Expected α

The ABC flow has:
- No true zeros (|ω| > 0 everywhere for generic parameters)
- Complex, space-filling structure

**Prediction:** For generic ABC, α → 0 (no zeros → sublevel set is whole domain as δ → 0)

---

## Summary Table

| Solution | Zero Set Structure | Expected α | Notes |
|----------|-------------------|------------|-------|
| Taylor-Green | Planes (sheets) + lines + points | α ≈ 1–2 | Mixed codimension |
| Burgers Vortex | No zeros (tube core) | α → 0 | Sublevel = whole domain |
| ABC Flow | No zeros (Beltrami) | α → 0 | Space-filling |

---

## Physical Interpretation

1. **Taylor-Green**: Has sheet-like zeros → α ≈ 1 (dangerous for regularity)
2. **Burgers**: No zeros → different regime (not testing SSL)
3. **ABC**: No zeros → different regime (not testing SSL)

### Key Insight

The Taylor-Green vortex is actually the **most relevant test case** because:
- It has explicit zeros
- It's a solution of Navier-Stokes
- It can undergo self-similar decay

The fact that TG gives α ≈ 1–2 suggests the SSL mechanism must handle sheet-like structures.

---

## Deliverables

1. **Mathematical derivations** in `/math/theory/`
   - `alpha_taylor_green.md`
   - `alpha_burgers.md`
   - `alpha_abc.md`

2. **Synthetic implementations** in `/pcm/tools/`
   - `exact_solutions.py` — generators for TG, Burgers, ABC

3. **Validation measurements**
   - Run pipeline on exact solutions
   - Compare measured α to theoretical predictions

---

## Success Criteria

- [ ] Taylor-Green: Derive α theoretically, verify with simulation
- [ ] Burgers: Confirm α → 0 behavior (no zeros)
- [ ] ABC: Confirm α → 0 behavior (no zeros)
- [ ] Clear interpretation: which exact solutions actually test SSL?
