from __future__ import annotations
import argparse
import numpy as np

from .cli_common import load_json, save_json
from .fit import fit_powerlaw, suggest_fit_range

def main():
    ap = argparse.ArgumentParser(description="Fit alpha in m(delta) ~ delta^alpha from measurement JSON.")
    ap.add_argument("--in", dest="inp", required=True, help="Input measurement JSON")
    ap.add_argument("--out", dest="out", required=True, help="Output fit JSON")
    ap.add_argument("--dmin", type=float, default=None, help="Fit range min delta (absolute)")
    ap.add_argument("--dmax", type=float, default=None, help="Fit range max delta (absolute)")
    args = ap.parse_args()

    meas = load_json(args.inp)
    delta = np.array(meas["sublevel"]["delta_abs"], dtype=float)
    m = np.array(meas["sublevel"]["m"], dtype=float)

    if args.dmin is None or args.dmax is None:
        dmin, dmax = suggest_fit_range(delta, m)
    else:
        dmin, dmax = float(args.dmin), float(args.dmax)

    fit = fit_powerlaw(delta, m, (dmin, dmax))
    fit["meta"] = meas.get("meta", {})
    save_json(args.out, fit)
    print(f"Wrote fit to {args.out}: {fit}")

if __name__ == "__main__":
    main()
