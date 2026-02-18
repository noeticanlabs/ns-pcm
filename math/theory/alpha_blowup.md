# Theoretical α for Self-Similar Blowup

## Problem

Derive the expected sublevel set exponent α for a potential self-similar singular solution of the Navier-Stokes equations. This gives insight into what α would look like if blowup occurs.

## Self-Similar Blowup Ansatz

Consider a potential singular solution approaching a singularity at time T. The self-similar ansatz is:

```
ω(x, t) ≈ (T - t)^{-p} · Φ( x / (T - t)^{q} )
```

where:
- `T` = blowup time
- `p` = temporal scaling exponent
- `q` = spatial scaling exponent
- `Φ(y)` = self-similar profile, bounded and non-zero at origin

### Scaling Constraints

For Navier-Stokes, dimensional analysis and scaling invariance give:

```
2p + q = 1  (from scaling of vorticity equation)
```

The simplest scaling is:
- `p = 1/2`, `q = 0` — stationary profile (not physical)
- `p = 1`, `q = -1` — scaling with contraction

Actually, more carefully:

For the vorticity equation:
```
∂ω/∂t + u·∇ω = ω·∇u + νΔω
```

The scaling `x → λx`, `t → λ²t`, `u → u/λ`, `ω → ω` is the Navier-Stokes scaling.

For self-similarity:
```
ω(x, t) = (T - t)^{-α} f( x / (T - t)^{β} )
```

Matching dimensions gives constraints from the equation terms.

## Sublevel Set Analysis

Let `y = x / (T - t)^{q}` be the similarity variable. Then:

```
|ω(x, t)| < δ  ⇔  (T - t)^{-p} |Φ(y)| < δ
            ⇔  |y| < (T - t)^{q} · (δ / p^)
            ⇔  |x| < (T - t)^{q+p} · const
```

The volume where |ω| < δ scales as:

```
|E_δ(t)| ~ (T - t)^{3(q+p)}
```

At fixed time, as δ → 0:

```
m(δ) ~ δ^{3/p}  (approximately)
```

Wait, let me be more precise.

### Near-Singularity Profile

Assume near the singular point (x = 0):

```
|Φ(y)| ~ |y|^{-s}  as y → 0
```

This is the **singularity strength** parameter.

Then:

```
|ω| < δ  ⇔  (T - t)^{-p} · |y|^{-s} < δ
        ⇔  |y| > (δ (T - t)^p)^{-1/s}
        ⇔  |x| > (T - t)^{q} · (δ (T - t)^p)^{-1/s}
```

The sublevel set is the **complement** of a ball — i.e., the region **outside** a sphere of radius r_δ.

This is the opposite of the smooth case!

### Volume Scaling

The volume where |ω| > δ (the "suplevel" set):

```
|{ |ω| > δ }| ~ r_δ³ ~ (T - t)^{3q} · (δ (T - t)^p)^{-3/s}
                = (T - t)^{3q - 3p/s} · δ^{-3/s}
```

Therefore, the sublevel set:

```
m(δ) = 1 - |{ |ω| > δ }| / Volume
     ≈ 1 - C · (T - t)^{3q - 3p/s} · δ^{-3/s}
```

For small δ, this behaves like:

```
m(δ) ~ δ^{3/s}   (when the profile has singularity)
```

## Special Cases

### Case 1: Smooth Profile (s → 0 limit)

If the profile is smooth and non-zero at origin (s = 0, interpreted as |Φ(0)| = const > 0):

```
|ω| < δ  ⇔  (T - t)^{-p} · |Φ(0)| < δ
        ⇔  t > T - (|Φ(0)|/δ)^{1/p}
```

This gives a **threshold time** rather than a volume scaling. The sublevel set fills most of the domain near blowup.

### Case 2: Point Singularity (s = 1)

If |Φ(y)| ~ |y|^{-1} (like a point vortex):

```
m(δ) ~ δ³
```

Same as smooth case — the concentration is not strong enough to affect the exponent.

### Case 3: Strong Singularity (s > 1)

If |Φ(y)| ~ |y|^{-s} with s > 1:

```
m(δ) ~ δ^{3/s}
```

For s → ∞ (essentially constant away from origin):

```
m(δ) ~ δ⁰  (constant — almost all points have small vorticity)
```

### Case 4: Sheet-like Singularity

If the singularity is localized on a 2D surface (like a collapsed sheet):

```
|Φ(y)| ~ |y_n|^{-s}  where y_n is normal coordinate
```

Then:

```
m(δ) ~ δ^{2/s}  (codimension 1)
```

### Case 5: Filament-like Singularity

If the singularity is localized on a 1D curve:

```
|Φ(y)| ~ |y_perp|^{-s}  where y_perp is radial coordinate
```

Then:

```
m(δ) ~ δ^{1/s}  (codimension 2)
```

## Summary of Blowup Scenarios

| Singularity Type | Profile | Sublevel Scaling | α |
|-----------------|---------|------------------|---|
| Smooth/regular | |Φ| ~ const | m → constant | N/A |
| Point (3D) | |Φ| ~ |y|^{-1} | δ³ | 3 |
| Sheet (2D collapse) | |Φ| ~ |y_n|^{-s} | δ^{2/s} | 2/s |
| Filament (1D collapse) | |Φ| ~ |y_perp|^{-s} | δ^{1/s} | 1/s |
| Extreme | |Φ| ~ |y|^{-∞} | δ⁰ | 0 |

## Connection to NS-PCM

The critical question for the SSL hypothesis:

> Does real Navier-Stokes turbulence maintain α > 1 under extreme dynamics?

- If blowup occurs with sheet-like concentration: α → 1 (dangerous)
- If blowup occurs with filament-like concentration: α → 2 (less dangerous)
- If no blowup: α should remain > 1 throughout evolution

The empirical measurement of α(t) during extreme events is the key diagnostic.

## Conclusion

The self-similar blowup analysis reveals that:

1. **Regular (smooth) flow**: α → 3 (our synthetic test)
2. **Filament-dominated**: α → 2
3. **Sheet-dominated**: α → 1  
4. **Extreme concentration**: α → 0

The **dangerous threshold** is α = 1. If real turbulence ever exhibits α ≤ 1 during intense stretching, it would signal potential blowup vulnerability.
