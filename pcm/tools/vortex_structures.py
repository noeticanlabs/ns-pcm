"""
Synthetic vortex structures for theoretical α validation.

This module generates canonical vorticity fields:
1. Vortex filament (1D core) - expected α ≈ 2
2. Vortex sheet (2D layer) - expected α ≈ 1  
3. Vortex tangle (network) - intermediate α

Usage:
    python -m pcm.tools.vortex_structures --type filament --out data/filament.h5 --n 64
    python -m pcm.tools.vortex_structures --type sheet --out data/sheet.h5 --n 64
    python -m pcm.tools.vortex_structures --type tangle --out data/tangle.h5 --n 64
"""

from __future__ import annotations
import argparse
import numpy as np
from ..io import write_snapshot


def make_vortex_filament(n: int, L: float, core_radius: float = 0.1, 
                         amplitude: float = 10.0, seed: int = 0) -> np.ndarray:
    """
    Create an isolated vortex filament aligned with z-axis.
    
    The vorticity is axisymmetric with a smooth core profile:
        ω_θ(r) = ω_max * exp(-r² / a²)
    
    where r is radial distance from filament axis and a is core radius.
    
    This should give α ≈ 2 (codimension 2).
    """
    rng = np.random.default_rng(seed)
    
    # Create coordinate grid
    x = np.linspace(0, L, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    
    # Cylindrical coordinates (filament along z-axis at origin)
    R = np.sqrt(X**2 + Y**2)
    
    # Vortex profile: Gaussian core
    # ω = ω_max * exp(-r²/a²) in azimuthal direction
    # In Cartesian: ω has only θ component, which in Cartesian means:
    # ω_x = -y/R * ω_θ, ω_y = x/R * ω_θ, ω_z = 0
    
    omega = np.zeros((3, n, n, n), dtype=np.float64)
    
    # Avoid division by zero at R=0
    R_safe = np.where(R > 0, R, 1e-10)
    
    # Azimuthal vorticity magnitude
    omega_theta = amplitude * np.exp(-(R_safe / core_radius)**2)
    
    # Convert to Cartesian components (azimuthal direction)
    # e_θ = (-sin φ, cos φ, 0) where φ = atan2(y, x)
    # In terms of x, y: e_θ = (-y/R, x/R, 0)
    omega[0] = -Y / R_safe * omega_theta  # x-component
    omega[1] = X / R_safe * omega_theta   # y-component
    omega[2] = 0.0                         # z-component
    
    # Handle axis
    mask_axis = (R < 1e-6)
    omega[:, mask_axis] = 0
    
    return omega


def make_vortex_sheet(n: int, L: float, sheet_thickness: float = 0.05,
                      amplitude: float = 10.0, seed: int = 0) -> np.ndarray:
    """
    Create a planar vortex sheet in the xy-plane.
    
    The vorticity is concentrated in a thin layer around z=0:
        ω_x(z) = ω_0 * tanh(z / δ)
    
    This should give α ≈ 1 (codimension 1).
    """
    rng = np.random.default_rng(seed)
    
    # Create coordinate grid
    x = np.linspace(0, L, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    
    # Center of domain
    z_center = L / 2
    
    # Distance from sheet
    z_dist = np.abs(Z - z_center)
    
    # Vortex sheet profile: tanh layer
    # Vorticity is in x-direction, varying across z
    omega = np.zeros((3, n, n, n), dtype=np.float64)
    
    # ω = ω_0 * tanh(z/δ) in x-direction
    omega[0] = amplitude * np.tanh((Z - z_center) / sheet_thickness)
    omega[1] = 0.0
    omega[2] = 0.0
    
    return omega


def make_vortex_tangle(n: int, L: float, num_filaments: int = 5,
                       core_radius: float = 0.08, amplitude: float = 8.0,
                       seed: int = 0) -> np.ndarray:
    """
    Create a random vortex tangle (multiple crossing filaments).
    
    This simulates a more complex vortex network, giving an intermediate α
    between 2 (pure filaments) and 3 (smooth field).
    """
    rng = np.random.default_rng(seed)
    
    # Create coordinate grid
    x = np.linspace(0, L, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    
    omega = np.zeros((3, n, n, n), dtype=np.float64)
    
    # Generate random filaments
    for _ in range(num_filaments):
        # Random orientation (unit vector)
        direction = rng.randn(3)
        direction = direction / np.linalg.norm(direction)
        
        # Random position in domain
        center = rng.uniform(0, L, size=3)
        
        # Project coordinates onto direction
        # Use a simple approach: create filament along one axis, then rotate
        # Filament along z-axis (simplest)
        R = np.sqrt((X - center[0])**2 + (Y - center[1])**2)
        R_safe = np.where(R > 0, R, 1e-10)
        
        # Gaussian core profile
        omega_theta = amplitude * np.exp(-(R_safe / core_radius)**2)
        
        # Direction in xy-plane (for this simplified version)
        # This creates filaments roughly in xy-plane
        omega_fil = np.zeros((3, n, n, n), dtype=np.float64)
        omega_fil[0] = - (Y - center[1]) / R_safe * omega_theta
        omega_fil[1] = (X - center[0]) / R_safe * omega_theta
        omega_fil[2] = 0.0
        
        # Add to total
        omega += omega_fil
    
    # Handle axis singularities
    omega = np.where(np.isfinite(omega), omega, 0.0)
    
    return omega


def make_smooth_reference(n: int, L: float, seed: int = 0) -> np.ndarray:
    """
    Create a smooth random vorticity field as reference.
    
    This uses the existing synthetic generator for comparison.
    Should give α ≈ 3 (generic smooth field).
    """
    from .synthetic import make_synthetic_u
    
    # Generate velocity and compute vorticity
    u = make_synthetic_u(n, L, seed)
    
    # Compute curl (vorticity) in spectral space
    from ..spectral import curl
    omega = curl(u, L)
    
    return omega


def main():
    parser = argparse.ArgumentParser(description="Generate synthetic vortex structures")
    parser.add_argument('--type', choices=['filament', 'sheet', 'tangle', 'smooth'],
                        required=True, help='Type of vortex structure')
    parser.add_argument('--out', required=True, help='Output HDF5 path')
    parser.add_argument('--n', type=int, default=64, help='Grid size')
    parser.add_argument('--L', type=float, default=2*np.pi, help='Domain length')
    parser.add_argument('--seed', type=int, default=0, help='Random seed')
    
    # Structure-specific parameters
    parser.add_argument('--core-radius', type=float, default=0.1,
                        help='Filament core radius (for filament/tangle)')
    parser.add_argument('--thickness', type=float, default=0.05,
                        help='Sheet thickness (for sheet)')
    parser.add_argument('--amplitude', type=float, default=10.0,
                        help='Vorticity amplitude')
    parser.add_argument('--num-filaments', type=int, default=5,
                        help='Number of filaments (for tangle)')
    
    args = parser.parse_args()
    
    # Generate based on type
    if args.type == 'filament':
        omega = make_vortex_filament(args.n, args.L, args.core_radius, 
                                     args.amplitude, args.seed)
    elif args.type == 'sheet':
        omega = make_vortex_sheet(args.n, args.L, args.thickness,
                                   args.amplitude, args.seed)
    elif args.type == 'tangle':
        omega = make_vortex_tangle(args.n, args.L, args.num_filaments,
                                    args.core_radius, args.amplitude, args.seed)
    elif args.type == 'smooth':
        omega = make_smooth_reference(args.n, args.L, args.seed)
    
    # Write output
    write_snapshot(args.out, omega=omega, attrs={'L': args.L, 'nu': 1.0, 't': 0.0})
    print(f"Wrote {args.type} vorticity field to {args.out}")


if __name__ == '__main__':
    main()
