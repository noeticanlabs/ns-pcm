#!/usr/bin/env bash
set -euo pipefail

IN="${1:-data/synth.h5}"
OUTDIR="${2:-out}"

mkdir -p "$OUTDIR"

python -m pcm.measure --in "$IN" --out "$OUTDIR/measure.json"
python -m pcm.fit_alpha --in "$OUTDIR/measure.json" --out "$OUTDIR/fit.json"
python -m pcm.plot --measure "$OUTDIR/measure.json" --fit "$OUTDIR/fit.json" --out "$OUTDIR/plots"

echo "Done. See $OUTDIR"
