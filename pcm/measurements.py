from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from typing import Dict, Any, List, Tuple, Optional

from .spectral import curl, strain, opnorm_sym_3x3_field, grad_vector, grad_omega_norm2
from .fields import omega_magnitude, xi_epsilon, G_from_xi, Psi_saturated

@dataclass
class MeasureConfig:
    deltas: np.ndarray
    eps_schedule: np.ndarray
    M_threshold: float = 1.0  # for optional diagnostics
    L: float = 2*np.pi

def default_config(n: int, L: float=2*np.pi) -> MeasureConfig:
    # delta bins in logspace relative to omega_rms
    deltas = np.logspace(-4, -0.3, 28)  # relative scale; later scaled by omega_rms
    eps_schedule = np.logspace(-6, -1, 18)
    return MeasureConfig(deltas=deltas, eps_schedule=eps_schedule, M_threshold=1.0, L=L)

def compute_all(snapshot: Dict[str, Any], config: MeasureConfig) -> Dict[str, Any]:
    L = float(snapshot.get("L", config.L))
    nu = float(snapshot.get("nu", 1.0))
    t = float(snapshot.get("t", 0.0))

    if "omega" in snapshot:
        omega = np.asarray(snapshot["omega"], dtype=np.float64)
        u = snapshot.get("u", None)
    else:
        u = np.asarray(snapshot["u"], dtype=np.float64)
        omega = curl(u, L)

    n = omega.shape[1]
    vol = L**3
    dx = L/n
    dV = dx**3

    om = omega_magnitude(omega)
    omega_rms = float(np.sqrt(np.mean(om**2)))

    # If u isn't provided, approximate strain from omega? Better: require u for residue.
    if u is None:
        # We can reconstruct u from omega in Fourier for divergence-free fields up to mean;
        # that's doable, but to keep code minimal we instead compute grad u from a pseudo-inverse:
        # Here: raise with clear message; user should provide u for residue measurement.
        # Still allow sublevel m(delta) and Fisher J_eps.
        have_u = False
    else:
        have_u = True
        u = np.asarray(u, dtype=np.float64)

    grad_om2 = grad_omega_norm2(omega, L)

    out: Dict[str, Any] = {
        "meta": {"n": int(n), "L": L, "nu": nu, "t": t, "omega_rms": omega_rms},
        "sublevel": {},
        "fisher": {},
        "notes": [],
    }

    # sublevel bins use absolute deltas = rel * omega_rms (fallback to 1 if rms=0)
    scale = omega_rms if omega_rms > 0 else 1.0
    deltas_abs = config.deltas * scale

    # strain opnorm field if possible
    if have_u:
        S = strain(u, L)
        Sop = opnorm_sym_3x3_field(S)  # (n,n,n)
    else:
        Sop = None
        out["notes"].append("u not provided: strain residue R(delta)=∫_{|ω|<δ}||S|| cannot be computed. Provide dataset `u` for full NS-PCM measurements.")

    # compute sublevel curves
    m = []
    R = []
    Q1 = []
    Q2 = []
    for delta in deltas_abs:
        mask = om < float(delta)
        m.append(float(np.mean(mask)))
        # gradient loads on sublevel
        g = np.sqrt(grad_om2)
        Q1.append(float(np.sum(g[mask])*dV))
        Q2.append(float(np.sum(grad_om2[mask])*dV))
        if Sop is not None:
            R.append(float(np.sum(Sop[mask])*dV))
        else:
            R.append(None)

    out["sublevel"]["delta_abs"] = deltas_abs.tolist()
    out["sublevel"]["delta_rel"] = config.deltas.tolist()
    out["sublevel"]["m"] = m
    out["sublevel"]["Q1_grad_omega"] = Q1
    out["sublevel"]["Q2_grad_omega2"] = Q2
    out["sublevel"]["R_strain_opnorm"] = R

    # Fisher schedule
    Jeps = []
    for eps_rel in config.eps_schedule:
        eps = float(eps_rel * scale)
        denom = om**2 + eps*eps
        Jeps.append(float(np.sum(grad_om2/denom)*dV))
    out["fisher"]["eps_abs"] = (config.eps_schedule*scale).tolist()
    out["fisher"]["eps_rel"] = config.eps_schedule.tolist()
    out["fisher"]["J"] = Jeps

    # Optional NS-PCM functional S_eps proxy at one epsilon
    eps0 = float((1e-3)*scale)
    xi, _ = xi_epsilon(omega, eps0)
    gxi = grad_vector(xi, L)
    G = G_from_xi(xi, gxi)
    Psi = Psi_saturated(G)
    S_eps = float(np.sum((om**2)*Psi)*dV)
    out["nspcm"] = {"eps0_abs": eps0, "S_eps0": S_eps, "mean_Psi": float(np.mean(Psi)), "mean_G": float(np.mean(G))}

    return out
