from __future__ import annotations
import numpy as np
import h5py
from typing import Dict, Any, Tuple, Optional

def read_snapshot(path: str) -> Dict[str, Any]:
    """Read an HDF5 snapshot containing either `omega` or `u` datasets.

    Expected:
      omega: (3, n, n, n) or u: (3, n, n, n)
    Optional attrs:
      nu, t, L (domain length, default 2*pi)
    """
    out: Dict[str, Any] = {}
    with h5py.File(path, "r") as f:
        if "omega" in f:
            out["omega"] = np.array(f["omega"], dtype=np.float64)
        if "u" in f:
            out["u"] = np.array(f["u"], dtype=np.float64)
        for k in ["nu", "t", "L"]:
            if k in f.attrs:
                out[k] = float(f.attrs[k])
    if "L" not in out:
        out["L"] = float(2*np.pi)
    if "nu" not in out:
        out["nu"] = float(1.0)
    if "t" not in out:
        out["t"] = float(0.0)
    if ("omega" not in out) and ("u" not in out):
        raise ValueError("Snapshot must contain dataset `omega` or `u`.")
    return out

def write_snapshot(path: str, omega: Optional[np.ndarray]=None, u: Optional[np.ndarray]=None, attrs: Optional[Dict[str, Any]]=None) -> None:
    if omega is None and u is None:
        raise ValueError("Provide omega and/or u.")
    attrs = attrs or {}
    with h5py.File(path, "w") as f:
        if omega is not None:
            f.create_dataset("omega", data=np.asarray(omega), compression="gzip")
        if u is not None:
            f.create_dataset("u", data=np.asarray(u), compression="gzip")
        for k,v in attrs.items():
            f.attrs[k] = v
