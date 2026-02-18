from __future__ import annotations
import numpy as np
from typing import Dict, Any, Tuple, Optional

def fit_powerlaw(delta: np.ndarray, m: np.ndarray, fit_range: Tuple[float,float]) -> Dict[str, Any]:
    """Fit m(delta) ~ C * delta^alpha in log-log space over delta in [dmin,dmax]."""
    dmin, dmax = fit_range
    mask = (delta >= dmin) & (delta <= dmax) & (m > 0)
    if np.sum(mask) < 5:
        return {"ok": False, "reason": "Not enough points in fit range with m>0."}
    x = np.log(delta[mask])
    y = np.log(m[mask])
    A = np.vstack([x, np.ones_like(x)]).T
    alpha, logC = np.linalg.lstsq(A, y, rcond=None)[0]
    # R^2
    yhat = alpha*x + logC
    ss_res = float(np.sum((y-yhat)**2))
    ss_tot = float(np.sum((y-np.mean(y))**2)) if len(y)>1 else 0.0
    r2 = 1.0 - ss_res/ss_tot if ss_tot>0 else 1.0
    return {
        "ok": True,
        "alpha": float(alpha),
        "C": float(np.exp(logC)),
        "logC": float(logC),
        "r2": float(r2),
        "npts": int(np.sum(mask)),
        "fit_range": [float(dmin), float(dmax)],
    }

def suggest_fit_range(delta: np.ndarray, m: np.ndarray) -> Tuple[float,float]:
    """Heuristic: avoid extreme ends where m saturates near 1 or hits numerical floor."""
    # keep m in (1e-6, 0.3) band by default
    good = (m > 1e-6) & (m < 0.3)
    if np.sum(good) < 6:
        # fallback: middle 60%
        lo = delta[int(0.2*len(delta))]
        hi = delta[int(0.8*len(delta))]
        return float(lo), float(hi)
    d = delta[good]
    return float(d.min()), float(d.max())
