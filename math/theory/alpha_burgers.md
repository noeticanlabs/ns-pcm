# Theoretical α for Burgers Vortex

## Exact Solution

The Burgers vortex is an exact solution of Navier-Stokes representing an axisymmetric vortex tube undergoing strain:

```
u_r = -α r / 2
u_θ = Γ/(2πr) [1 - exp(-r²/a(t))]  
u_z = α z
```

where:
- α > 0 is the strain rate (constant)
- Γ is the total circulation (constant)
- a(t) = a₀ exp(αt) is the core radius (grows exponentially due to stretching)

## Vorticity

In cylindrical coordinates (r, θ, z):

```
ω_r = 0
ω_θ = ∂u_z/∂r - ∂u_r/∂z = 0 - 0 = 0 (for this flow)
ω_z = (1/r) ∂(r u_θ)/∂r - (1/r) ∂u_r/∂θ
```

Actually, let's compute properly. The vorticity in cylindrical coordinates for axisymmetric flow:

```
ω_r = ∂u_z/∂r - ∂u_r/∂z
ω_θ = 0 (for purely azimuthal velocity)
ω_z = (1/r) ∂(r u_θ)/∂r
```

For our flow:
- u_r = -αr/2 → ∂u_r/∂z = 0
- u_z = αz → ∂u_z/∂r = 0
- So ω_r = 0

For ω_z:
```
u_θ = Γ/(2πr) [1 - exp(-r²/a²)]
r u_θ = Γ/(2π) [1 - exp(-r²/a²)]
∂(r u_θ)/∂r = Γ/(2π) [exp(-r²/a²) · (2r/a²)]
             = Γ/(πa²) r exp(-r²/a²)
             
ω_z = (1/r) · Γ/(πa²) r exp(-r²/a²) = Γ/(πa²) exp(-r²/a²)
```

Wait, I made an error. Let me recompute:

```
∂/∂r [1 - exp(-r²/a²)] = ∂/∂r [-exp(-r²/a²)] = -(-2r/a²) exp(-r²/a²) = (2r/a²) exp(-r²/a²)
```

So:
```
r u_θ = Γ/(2π) [1 - exp(-r²/a²)]
∂(r u_θ)/∂r = Γ/(2π) · (2r/a²) exp(-r²/a²) = Γ/(πa²) r exp(-r²/a²)
```

Then:
```
ω_z = (1/r) · Γ/(πa²) r exp(-r²/a²) = (Γ/πa²) exp(-r²/a²)
```

So the full vorticity is:
```
ω = (0, 0, ω_z) = (0, 0, (Γ/πa²) exp(-r²/a²))
```

In Cartesian components, this is purely in the z-direction.

## Key Property: No Zeros!

The Burgers vortex has **no zeros**:
- ω_z > 0 for all r
- As r → 0: ω_z → Γ/(πa²) (maximum)
- As r → ∞: ω_z → 0 (but never exactly zero)

## Sublevel Set Analysis

This is fundamentally different from previous cases. For the Burgers vortex:

```
|ω| = |Γ/πa²| · exp(-r²/a²)
```

The sublevel set { |ω| < δ } is:
- r > r_δ where exp(-r²/a²) < δ/(Γ/πa²)
- r > a · sqrt(-ln(δ · πa²/Γ))

This is the **exterior** of a cylinder of radius r_δ.

## Volume Scaling

As δ → 0:
- r_δ → ∞ (logarithmically)
- The sublevel set is essentially the **entire domain** outside the core

More precisely, for a domain of radius R:
```
|{ |ω| < δ }| / Volume ≈ 1 - (r_δ/R)²  (for 2D cross-section)
```

As δ → 0:
- r_δ → R (for fixed domain)
- m(δ) → 1 (the entire domain has small vorticity)

## α Analysis

This is a **degenerate case** for the SSL hypothesis:

| Regime | Behavior | α |
|--------|----------|---|
| δ small but not too small | m(δ) ≈ 1 - exp(-2r_δ²/R²) | α → 0 |
| δ → 0 | m(δ) → 1 | α → 0 |

The Burgers vortex gives **α → 0** because:
- There are no zeros
- The vorticity is always positive
- The sublevel set fills the domain as δ → 0

## Physical Interpretation

The Burgers vortex represents a **stable vortex tube**:
- Vorticity concentrated in core
- Smooth exponential decay outside
- No singular zero set

This is actually a **favorable** configuration for regularity:
- The "bad" region (high vorticity) is small
- The "good" region (low vorticity) is large
- The residue term R(δ) is small

## Important Caveat

The SSL hypothesis is designed to control the **singular/zeros** of vorticity. The Burgers vortex has **no zeros**, so it doesn't actually test the SSL mechanism.

However, the Burgers vortex IS relevant because:
1. It shows that not all flows have zeros
2. It demonstrates α → 0 is possible
3. It suggests that flows with stable tube structures are "safe"

## Summary

| Solution | Zero Set | Expected α | Relevance to SSL |
|----------|----------|------------|------------------|
| Burgers Vortex | **None** | α → 0 | Tests non-zero case |

The Burgers vortex is a **positive test case** for Navier-Stokes regularity:
- It has stable vortex tube structure
- No dangerous zero set
- Residue term is controllable

But it doesn't test the SSL hypothesis directly because it has no zeros.
