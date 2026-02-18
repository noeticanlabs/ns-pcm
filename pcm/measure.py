from __future__ import annotations
import argparse
import numpy as np

from .io import read_snapshot
from .measurements import default_config, compute_all, MeasureConfig
from .cli_common import save_json

def main():
    ap = argparse.ArgumentParser(description="Measure NS-PCM sublevel sets, residues, and Fisher-like term from an HDF5 snapshot.")
    ap.add_argument("--in", dest="inp", required=True, help="Input HDF5 snapshot path")
    ap.add_argument("--out", dest="out", required=True, help="Output JSON path")
    ap.add_argument("--M", type=float, default=1.0, help="Directional complexity threshold (diagnostic)")
    args = ap.parse_args()

    snap = read_snapshot(args.inp)
    n = snap["omega"].shape[1] if "omega" in snap else snap["u"].shape[1]
    cfg = default_config(n=n, L=float(snap.get("L", 2*np.pi)))
    cfg.M_threshold = float(args.M)

    res = compute_all(snap, cfg)
    save_json(args.out, res)
    print(f"Wrote measurements to {args.out}")

if __name__ == "__main__":
    main()
