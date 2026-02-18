from __future__ import annotations
import argparse
import numpy as np
from ..io import write_snapshot

def make_synthetic_u(n: int, L: float, seed: int=0) -> np.ndarray:
    """Create a simple divergence-free synthetic velocity field using a few Fourier modes."""
    rng = np.random.default_rng(seed)
    x = np.linspace(0, L, n, endpoint=False)
    X,Y,Z = np.meshgrid(x,x,x, indexing="ij")
    u = np.zeros((3,n,n,n), dtype=np.float64)

    # Superpose a few incompressible-looking modes (not a full projection, but reasonably smooth)
    for _ in range(6):
        k = rng.integers(1, 5, size=3)
        phase = rng.uniform(0, 2*np.pi)
        amp = rng.normal(0, 1)
        # Use a vector potential A and set u = curl A for divergence-free field
        A = np.zeros((3,n,n,n), dtype=np.float64)
        A[0] = amp*np.sin(k[0]*X + k[1]*Y + k[2]*Z + phase)
        A[1] = amp*np.cos(k[0]*X - k[1]*Y + k[2]*Z + phase)
        A[2] = amp*np.sin(k[0]*X + k[1]*Y - k[2]*Z + phase)
        # finite-diff curl of A for simplicity
        dx = L/n
        dAy_dz = (np.roll(A[1], -1, axis=2) - np.roll(A[1], 1, axis=2))/(2*dx)
        dAz_dy = (np.roll(A[2], -1, axis=1) - np.roll(A[2], 1, axis=1))/(2*dx)
        dAz_dx = (np.roll(A[2], -1, axis=0) - np.roll(A[2], 1, axis=0))/(2*dx)
        dAx_dz = (np.roll(A[0], -1, axis=2) - np.roll(A[0], 1, axis=2))/(2*dx)
        dAx_dy = (np.roll(A[0], -1, axis=1) - np.roll(A[0], 1, axis=1))/(2*dx)
        dAy_dx = (np.roll(A[1], -1, axis=0) - np.roll(A[1], 1, axis=0))/(2*dx)
        u[0] += dAz_dy - dAy_dz
        u[1] += dAx_dz - dAz_dx
        u[2] += dAy_dx - dAx_dy

    # normalize
    u /= (np.sqrt(np.mean(u**2)) + 1e-12)
    return u

def main():
    ap = argparse.ArgumentParser(description="Generate a synthetic HDF5 snapshot with velocity u.")
    ap.add_argument("--out", required=True, help="Output HDF5 path")
    ap.add_argument("--n", type=int, default=64, help="Grid size")
    ap.add_argument("--L", type=float, default=2*np.pi, help="Domain length")
    ap.add_argument("--nu", type=float, default=1.0, help="Viscosity (meta)")
    ap.add_argument("--seed", type=int, default=0, help="Seed")
    args = ap.parse_args()

    u = make_synthetic_u(args.n, args.L, args.seed)
    write_snapshot(args.out, u=u, attrs={"L": args.L, "nu": args.nu, "t": 0.0})
    print(f"Wrote synthetic snapshot to {args.out}")

if __name__ == "__main__":
    main()
