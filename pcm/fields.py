from __future__ import annotations
import numpy as np
from typing import Tuple

def omega_magnitude(omega: np.ndarray) -> np.ndarray:
    return np.sqrt(np.sum(omega**2, axis=0))

def xi_epsilon(omega: np.ndarray, eps: float) -> Tuple[np.ndarray, np.ndarray]:
    """Return (xi_eps, r_eps) where r_eps = sqrt(|omega|^2 + eps^2)."""
    mag2 = np.sum(omega**2, axis=0)
    r = np.sqrt(mag2 + eps*eps)
    xi = omega / r[None, ...]
    return xi, r

def G_from_xi(xi: np.ndarray, grad_xi: np.ndarray) -> np.ndarray:
    """Compute G=|∇xi|^2 from grad_xi(3,3,n,n,n) where grad_xi[i,j]=d xi_i/d x_j."""
    G = np.zeros(grad_xi.shape[2:], dtype=np.float64)
    for i in range(3):
        for j in range(3):
            G += grad_xi[i,j]**2
    return G

def Psi_saturated(G: np.ndarray) -> np.ndarray:
    return G/(1.0+G)
