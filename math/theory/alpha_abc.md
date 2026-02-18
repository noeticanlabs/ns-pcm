# Theoretical α for ABC Flow (Arnold-Beltrami-Childress)

## Exact Solution

ABC flow is a steady solution of the incompressible Euler equations:

```
u = (A sin z + C cos y, B sin x + A cos z, C sin y + B cos x)
```

where A, B, C are constants. The classic case is A = B = C = 1.

## Key Properties

1. **Beltrami Property**: For ABC flow, ω = u (eigenvector of curl with eigenvalue 1)
   - This means the velocity is aligned with vorticity everywhere
   - No stretching term in the vorticity equation
   - The flow is a stationary solution of Euler (but not Navier-Stokes)

2. **Chaotic Streamlines**: For generic (A,B,C), the streamlines are chaotic
   - The flow is integrable only for special parameter values

3. **No Dissipation**: Since ω = u, the vorticity equation reduces to
   - u·∇ω = ω·∇u = 0 (trivial for ω = u)
   - No dynamics in the inviscid case

## Vorticity

Since ω = u for ABC flow:

```
|ω|² = (A sin z + C cos y)² + (B sin x + A cos z)² + (C sin y + B cos x)²
```

For the standard case A = B = C = 1:

```
|ω|² = (sin z + cos y)² + (sin x + cos z)² + (sin y + cos x)²
```

## Zero Set Analysis

We need to solve |ω| = 0:

```
A sin z + C cos y = 0
B sin x + A cos z = 0  
C sin y + B cos x = 0
```

For generic A, B, C, this is a complicated system. Let's analyze special cases.

### Case 1: A = B = C = 0
- Trivial flow u = 0
- α = 3 (everything is zero)

### Case 2: A = B = C ≠ 0
The system becomes:
```
sin z + cos y = 0
sin x + cos z = 0
sin y + cos x = 0
```

This is a nonlinear system. Numerical studies show:
- No exact zeros for generic parameters
- |ω| is bounded away from zero

### Case 3: One parameter zero (e.g., C = 0)
```
u = (A sin z, B sin x + A cos z, B cos x)
ω = u
```

Now we need:
```
A sin z = 0 → sin z = 0 → z = 0, π
B sin x + A cos z = 0 → sin x = ±A/B
B cos x = 0 → cos x = 0 → x = π/2, 3π/2
```

This gives discrete solutions (lines in 3D).

## Generic Behavior

For most ABC parameters:
- **No exact zeros** (|ω| > 0 everywhere)
- **No exact zeros** means no singular zero set
- The minimum of |ω| is typically bounded away from zero

This is similar to the Burgers vortex: a "healthy" vorticity field with no dangerous structures.

## Sublevel Set Analysis

For ABC flow with no zeros:
- The minimum vorticity |ω_min| > 0
- For δ < |ω_min|: m(δ) = 0
- For δ > |ω_min|: m(δ) > 0 and increases

As δ → 0:
- If |ω_min| > 0: m(δ) = 0 for small δ (no zeros)
- The sublevel set appears "all at once" when δ crosses |ω_min|

This gives **α → 0** in the sense that there's no power-law behavior near δ = 0.

## α Summary

| Parameter Regime | Zero Set | Expected α |
|-----------------|----------|-------------|
| A = B = C = 0 | Everything | α = 3 (trivial) |
| A = B = C ≠ 0 | None (numerically) | α → 0 |
| One parameter = 0 | Discrete lines | α → 2 (1D set) |
| Generic | None | α → 0 |

## Physical Interpretation

ABC flow is a **Beltrami flow**:
- Vorticity aligned with velocity everywhere
- No stretching (ω·∇u = 0)
- Structurally stable in some sense

This is actually **good for regularity**:
- No vortex stretching
- No concentration mechanism
- The field is "smooth" in a topological sense

## Relevance to SSL

ABC flow tests a different regime than TG:
- TG: Has zeros (sheets) → α = 1
- Burgers: No zeros → α → 0
- ABC: No zeros (typically) → α → 0

The key insight:
- **Flows with zeros are potentially dangerous** (TG-like)
- **Flows without zeros are safe** (Burgers, ABC-like)

## Summary

| Solution | Has Zeros? | α | SSL Test |
|----------|------------|---|----------|
| Taylor-Green | Yes (planes) | α = 1 | **Yes** - dangerous case |
| Burgers Vortex | No | α → 0 | No - no zeros to test |
| ABC Flow | No (typically) | α → 0 | No - no zeros to test |

The **Taylor-Green vortex is the key test case** for SSL because:
1. It has explicit zeros
2. It gives α = 1 (the dangerous threshold)
3. It's an actual NS solution that can be initialized in DNS
