from __future__ import annotations
import argparse, os
import numpy as np
import matplotlib.pyplot as plt

from .cli_common import load_json

def main():
    ap = argparse.ArgumentParser(description="Plot NS-PCM measurements and alpha fit.")
    ap.add_argument("--measure", required=True, help="measurement JSON")
    ap.add_argument("--fit", required=False, help="fit JSON (optional)")
    ap.add_argument("--out", required=True, help="output directory for plots")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    meas = load_json(args.measure)
    delta = np.array(meas["sublevel"]["delta_abs"], dtype=float)
    m = np.array(meas["sublevel"]["m"], dtype=float)

    # plot m(delta)
    plt.figure()
    plt.loglog(delta, m, marker="o")
    plt.xlabel("delta")
    plt.ylabel("m(delta) = measure{|omega|<delta}")
    plt.title("Sublevel measure")
    plt.grid(True, which="both")
    plt.savefig(os.path.join(args.out, "m_delta.png"), dpi=200)
    plt.close()

    # plot residue R(delta) if present
    R = meas["sublevel"].get("R_strain_opnorm", None)
    if R is not None and any(r is not None for r in R):
        Rv = np.array([np.nan if r is None else float(r) for r in R], dtype=float)
        plt.figure()
        plt.loglog(delta, Rv, marker="o")
        plt.xlabel("delta")
        plt.ylabel("R(delta) = ∫_{|ω|<δ} ||S||_op dx")
        plt.title("Strain residue on sublevel sets")
        plt.grid(True, which="both")
        plt.savefig(os.path.join(args.out, "R_delta.png"), dpi=200)
        plt.close()

    # plot Fisher J(eps)
    eps = np.array(meas["fisher"]["eps_abs"], dtype=float)
    J = np.array(meas["fisher"]["J"], dtype=float)
    plt.figure()
    plt.loglog(eps, J, marker="o")
    plt.xlabel("eps")
    plt.ylabel("J_eps = ∫ |∇ω|^2/(|ω|^2+eps^2) dx")
    plt.title("Fisher-like schedule")
    plt.grid(True, which="both")
    plt.savefig(os.path.join(args.out, "J_eps.png"), dpi=200)
    plt.close()

    # overlay fit if provided
    if args.fit:
        fit = load_json(args.fit)
        if fit.get("ok", False):
            alpha = fit["alpha"]; C = fit["C"]
            dmin, dmax = fit["fit_range"]
            dd = np.logspace(np.log10(dmin), np.log10(dmax), 100)
            mm = C*(dd**alpha)
            plt.figure()
            plt.loglog(delta, m, marker="o", label="data")
            plt.loglog(dd, mm, label=f"fit alpha={alpha:.3f}, R^2={fit['r2']:.3f}")
            plt.xlabel("delta"); plt.ylabel("m(delta)")
            plt.title("Power-law fit")
            plt.grid(True, which="both")
            plt.legend()
            plt.savefig(os.path.join(args.out, "m_fit.png"), dpi=200)
            plt.close()

    print(f"Wrote plots to {args.out}")

if __name__ == "__main__":
    main()
