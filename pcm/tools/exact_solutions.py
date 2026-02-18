"""
Exact Navier-Stokes solutions for α validation.

This module generates canonical exact solutions:
1. Taylor-Green vortex - expected α = 1 (sheet-like zeros)
2. Burgers vortex - α → 0 (no zeros)
3. ABC flow - α → 0 (no zeros)

Usage:
    python -m pcm.tools.exact_solutions --type taylor_green --out data/tg.h5 --n 64
    python -m pcm.tools.exact_solutions --type burgers --out data/burgers.h5 --n 64
    python -m pcm.tools.exact_solutions --type abc --out data/abc.h5 --n 64
"""

from __future__ import annotations
import argparse
import numpy as np
from ..io import write_snapshot


def make_taylor_green(n: int, L: float = 2*np.pi, amplitude: float = 1.0) -> np.ndarray:
    """
    Taylor-Green vortex:
    
    u = (sin(x) * cos(y) * cos(z), -cos(x) * sin(y) * cos(z), 0) * amplitude
    ω = (0, 0, -2 * sin(x) * sin(y) * sin(z)) * amplitude
    
    This has sheet-like zero structure (planes where sin(x)=0, sin(y)=0, or sin(z)=0).
    Expected α ≈ 1 (codimension 1).
    """
    x = np.linspace(0, L, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    
    # Velocity field
    u = np.zeros((3, n, n, n), dtype=np.float64)
    
    u[0] = amplitude * np.sin(X) * np.cos(Y) * np.cos(Z)
    u[1] = -amplitude * np.cos(X) * np.sin(Y) * np.cos(Z)
    u[2] = 0.0
    
    # Compute vorticity from velocity (spectral)
    from ..spectral import curl
    omega = curl(u, L)
    
    return omega


def make_burgers(n: int, L: float = 2*np.pi, 
                 gamma: float = 10.0, core_radius: float = 0.2,
                 strain_rate: float = 0.1) -> np.ndarray:
    """
    Burgers vortex (axisymmetric vortex tube):
    
    u_r = -α * r / 2
    u_θ = Γ / (2πr) * [1 - exp(-r²/a²)]
    u_z = α * z
    
    where a = core_radius, Γ = circulation, α = strain_rate
    
    Vorticity: ω = (0, 0, Γ/(πa²) * exp(-r²/a²))
    
    This has NO zeros - vorticity is everywhere positive.
    Expected α → 0 (sublevel set is almost everything for small δ).
    """
    x = np.linspace(0, L, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    
    # Center of domain
    c = L / 2
    
    # Radial distance from center
    R = np.sqrt((X - c)**2 + (Y - c)**2)
    
    # Azimuthal vorticity (in z-direction)
    # ω_z = Γ/(πa²) * exp(-r²/a²)
    omega_z = gamma / (np.pi * core_radius**2) * np.exp(-(R / core_radius)**2)
    
    # Convert to Cartesian components
    # In cylindrical: ω = (0, 0, ω_z)
    # Need to convert to Cartesian: ω_x = -y/R * ω_θ, ω_y = x/R * ω_θ
    
    # For pure z-direction vorticity in Cartesian:
    omega = np.zeros((3, n, n, n), dtype=np.float64)
    
    # For ω in z-direction: ω × r gives velocity contribution
    # But we directly set vorticity, not velocity
    omega[2] = omega_z
    
    return omega


def make_abc(n: int, L: float = 2*np.pi, 
             A: float = 1.0, B: float = 1.0, C: float = 1.0) -> np.ndarray:
    """
    ABC flow (Arnold-Beltrami-Childress):
    
    u_x = A * sin(z) + C * cos(y)
    u_y = B * sin(x) + A * cos(z)
    u_z = C * sin(y) + B * cos(x)
    
    Key property: ω = u (Beltrami condition)
    
    For generic (A,B,C), there are no exact zeros.
    Expected α → 0 (no zeros to test SSL).
    """
    x = np.linspace(0, L, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    
    # Velocity = vorticity (Beltrami)
    u = np.zeros((3, n, n, n), dtype=np.float64)
    
    u[0] = A * np.sin(Z) + C * np.cos(Y)
    u[1] = B * np.sin(X) + A * np.cos(Z)
    u[2] = C * np.sin(Y) + B * np.cos(X)
    
    # For ABC flow, ω = u
    omega = u.copy()
    
    return omega


def main():
    parser = argparse.ArgumentParser(description="Generate exact NS solution vorticity fields")
    parser.add_argument('--type', choices=['taylor_green', 'burgers', 'abc'],
                        required=True, help='Type of exact solution')
    parser.add_argument('--out', required=True, help='Output HDF5 path')
    parser.add_argument('--n', type=int, default=64, help='Grid size')
    parser.add_argument('--L', type=float, default=2*np.pi, help='Domain length')
    
    # Solution-specific parameters
    parser.add_argument('--amplitude', type=float, default=1.0,
                        help='Amplitude for Taylor-Green')
    parser.add_argument('--gamma', type=float, default=10.0,
                        help='Circulation for Burgers')
    parser.add_argument('--core-radius', type=float, default=0.2,
                        help='Core radius for Burgers')
    parser.add_argument('--strain-rate', type=float, default=0.1,
                        help='Strain rate for Burgers')
    parser.add_argument('--A', type=float, default=1.0, help='A parameter for ABC')
    parser.add_argument('--B', type=float, default=1.0, help='B parameter for ABC')
    parser.add_argument('--C', type=float, default=1.0, help='C parameter for ABC')
    
    args = parser.parse_args()
    
    # Generate based on type
    if args.type == 'taylor_green':
        omega = make_taylor_green(args.n, args.L, args.amplitude)
    elif args.type == 'burgers':
        omega = make_burgers(args.n, args.L, args.gamma, args.core_radius, args.strain_rate)
    elif args.type == 'abc':
        omega = make_abc(args.n, args.L, args.A, args.B, args.C)
    
    # Write output
    write_snapshot(args.out, omega=omega, attrs={'L': args.L, 'nu': 1.0, 't': 0.0})
    print(f"Wrote {args.type} vorticity field to {args.out}")


if __name__ == '__main__':
    main()
