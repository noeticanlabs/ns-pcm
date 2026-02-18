from __future__ import annotations
import numpy as np
from typing import Tuple

def _kgrid(n: int, L: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # numpy fftfreq gives cycles per unit; multiply by 2*pi for angular wave numbers
    k1 = 2*np.pi*np.fft.fftfreq(n, d=L/n)
    kx, ky, kz = np.meshgrid(k1, k1, k1, indexing="ij")
    return kx, ky, kz

def grad_scalar(f: np.ndarray, L: float) -> np.ndarray:
    """Spectral gradient of scalar field f(n,n,n) -> (3,n,n,n)."""
    n = f.shape[0]
    kx, ky, kz = _kgrid(n, L)
    F = np.fft.fftn(f)
    gx = np.fft.ifftn(1j*kx*F).real
    gy = np.fft.ifftn(1j*ky*F).real
    gz = np.fft.ifftn(1j*kz*F).real
    return np.stack([gx, gy, gz], axis=0)

def grad_vector(v: np.ndarray, L: float) -> np.ndarray:
    """Spectral gradient of vector field v(3,n,n,n) -> (3,3,n,n,n) where out[i,j]=d v[i]/d x_j"""
    assert v.ndim == 4 and v.shape[0] == 3
    n = v.shape[1]
    kx, ky, kz = _kgrid(n, L)
    ks = [kx, ky, kz]
    out = np.zeros((3,3,n,n,n), dtype=np.float64)
    for i in range(3):
        Vi = np.fft.fftn(v[i])
        for j in range(3):
            out[i,j] = np.fft.ifftn(1j*ks[j]*Vi).real
    return out

def curl(u: np.ndarray, L: float) -> np.ndarray:
    """Curl of velocity field u(3,n,n,n) -> omega(3,n,n,n)"""
    gu = grad_vector(u, L)  # du_i/dx_j
    # omega = (d u_z/dy - d u_y/dz, d u_x/dz - d u_z/dx, d u_y/dx - d u_x/dy)
    ox = gu[2,1] - gu[1,2]
    oy = gu[0,2] - gu[2,0]
    oz = gu[1,0] - gu[0,1]
    return np.stack([ox, oy, oz], axis=0)

def strain(u: np.ndarray, L: float) -> np.ndarray:
    """Strain tensor S = (∇u + ∇u^T)/2 as array (3,3,n,n,n)."""
    gu = grad_vector(u, L)
    S = 0.5*(gu + np.swapaxes(gu, 0, 1))
    return S

def opnorm_sym_3x3_field(S: np.ndarray) -> np.ndarray:
    """Operator norm of symmetric 3x3 field S(3,3,n,n,n) -> (n,n,n).
    For symmetric matrices, op norm is max |eigenvalue|.
    """
    assert S.shape[0] == 3 and S.shape[1] == 3
    n = S.shape[2]
    # reshape to (N,3,3)
    N = n*n*n
    A = np.empty((N,3,3), dtype=np.float64)
    for i in range(3):
        for j in range(3):
            A[:,i,j] = S[i,j].reshape(-1)
    # eigenvalues for symmetric matrices
    w = np.linalg.eigvalsh(A)  # (N,3)
    op = np.max(np.abs(w), axis=1)
    return op.reshape((n,n,n))

def grad_omega_norm2(omega: np.ndarray, L: float) -> np.ndarray:
    """Compute |∇omega|^2 pointwise where ∇omega is (3 components each with 3 spatial derivs).
    omega: (3,n,n,n). returns (n,n,n)
    """
    go = grad_vector(omega, L)  # d omega_i / d x_j
    # sum_{i,j} go[i,j]^2
    s = np.zeros(go.shape[2:], dtype=np.float64)
    for i in range(3):
        for j in range(3):
            s += go[i,j]**2
    return s
