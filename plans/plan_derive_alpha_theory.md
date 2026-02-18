# Plan: Derive Theoretical α Values for Idealized Vortex Structures

## Objective

Derive expected sublevel set exponents α for canonical vorticity configurations in 3D. This provides theoretical benchmarks to compare against DNS measurements and determine whether real turbulence exhibits filament-like (α ≈ 2), sheet-like (α ≈ 1), or smooth-like (α ≈ 3) behavior.

---

## Background: What is α?

The sublevel set measure is:

```
m(δ) = |{x : |ω(x)| < δ}|
```

For power-law behavior `m(δ) ~ δ^α`, the exponent α encodes the **codimension** of the vorticity support:

| Structure | Codimension | Expected α |
|----------|-------------|------------|
| Regular smooth field (isolated zeros) | 0 (3D balls) | α → 3 |
| Vortex filaments (1D cores) | 2 (tubes) | α → 2 |
| Vortex sheets (2D layers) | 1 (surfaces) | α → 1 |
| Point singularities | 3 | α → 0 |

---

## Derivation Cases

### Case 1: Smooth Generic Field (Reference Baseline)

**Assumption:** Non-degenerate zero at x₀ where ∇ω(x₀) is non-singular.

```
|ω(x)| ≈ |∇ω(x₀)| · |x - x₀|  (linear approximation)
```

The set { |ω| < δ } ≈ ball of radius r = δ / |∇ω|.

```
m(δ) ≈ C · r³ ≈ C' · δ³
```

**Result:** α = 3

---

### Case 2: Vortex Filament (1D Core)

**Model:** Axisymmetric vortex tube with core profile:

```
|ω|(r) = ω_max · f(r/a)
```

where:
- r = radial distance from filament axis
- a = core radius
- f(0) = 1, f(r/a → ∞) → 0 rapidly

For a **generic smooth core** (e.g., Gaussian or exponential decay):
- Near core: |ω| ~ r (linear approximation in r)
- Sublevel set: cylinder of radius r and length L

```
{ |ω| < δ } ≈ π r² L
where r ~ δ (from linear core profile)
```

So:

```
m(δ) ~ δ²
```

**Result:** α = 2

**Note:** This assumes the filament has finite length L. For an infinite filament, the argument holds locally.

---

### Case 3: Vortex Sheet (2D Layer)

**Model:** Tangential discontinuity approximated by smooth hyperbolic tangent layer:

```
ω(x, y, z) = ω_0 · tanh(z/δ_s)
```

where δ_s = sheet thickness.

Near the sheet center (z = 0):
- Taylor expand: |ω| ≈ ω_0 · |z|/δ_s
- Sublevel set: slab of thickness 2z₀ where z₀ ~ δ·δ_s/ω_0

```
m(δ) ~ Area · z₀ ~ A · δ
```

**Result:** α = 1

---

### Case 4: Self-Similar Blowup Ansatz

Consider a potential singular solution:

```
ω(x, t) ≈ (T - t)^{-p} · Φ( x / (T - t)^{q} )
```

If the profile Φ has a singularity at origin:
- |Φ(z)| ~ |z|^{-s} as z → 0

Then near singularity:

```
|ω| < δ  ⇒  |z| < δ^{1/s} · (T - t)^{q/s}
```

Volume scales as:

```
m(δ) ~ (T - t)^{3q/s} · δ^{3/s}
```

The exponent depends on the scaling exponents p, q and singularity strength s.

**Special case:** If singularity is point-like (s = 1, q = 1/2):
```
m(δ) ~ δ³  (same as smooth case)
```

**Special case:** If vorticity concentrates on lower-dimensional set:
```
α < 1 becomes possible
```

---

## Computational Validation Plan

Create synthetic test fields to verify theoretical predictions:

### Test 1: Vortex Filament

```python
# Create isolated vortex filament
# - Axisymmetric tube with known core profile
# - Compute m(δ) numerically
# - Verify α → 2 as resolution increases
```

### Test 2: Vortex Sheet

```python  
# Create planar vortex sheet
# - Hyperbolic tangent layer
# - Compute m(δ) numerically
# - Verify α → 1 as resolution increases
```

### Test 3: Filament Network

```python
# Create multiple crossing filaments
# - Simulates turbulent vortex tangle
# - Measure effective α
# - Should approach 2 (filament-dominated)
```

---

## Deliverables

1. **Mathematical derivations** documented in `/math/theory/`
   - `alpha_filament.md` — Derivation for 1D vortex core
   - `alpha_sheet.md` — Derivation for 2D vortex sheet
   - `alpha_blowup.md` — Self-similar blowup scaling

2. **Synthetic test fields** in `/data/theory/`
   - `filament_n64.h5` — Single vortex filament
   - `sheet_n64.h5` — Planar vortex sheet
   - `tangle_n64.h5` — Filament network

3. **Measurement results** confirming theoretical α values

---

## Success Criteria

- [ ] Derivation for filament gives α = 2 ± 0.1
- [ ] Derivation for sheet gives α = 1 ± 0.1
- [ ] Synthetic tests reproduce these values numerically
- [ ] Clear interpretation guide for comparing DNS to theory

---

## Timeline (Mental Check)

This is a theory + validation task. The plan should execute in logical order:

1. Write derivations (30 min)
2. Implement synthetic field generators (1 hr)
3. Run measurements (30 min)
4. Verify and document (30 min)

Total: ~2.5 hours of focused work.

---

## Files to Create/Modify

| File | Action |
|------|--------|
| `math/theory/alpha_filament.md` | Create |
| `math/theory/alpha_sheet.md` | Create |
| `math/theory/alpha_blowup.md` | Create |
| `pcm/tools/vortex_structures.py` | Create (synthetic generators) |
| `plans/validation_results.md` | Create (measurement confirmations) |
