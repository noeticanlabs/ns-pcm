import os, json, tempfile, subprocess, sys

def run(cmd):
    r = subprocess.run([sys.executable, "-m"] + cmd, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr

def test_pipeline_smoke():
    with tempfile.TemporaryDirectory() as td:
        h5 = os.path.join(td, "s.h5")
        outm = os.path.join(td, "measure.json")
        outf = os.path.join(td, "fit.json")
        run(["pcm.tools.synthetic", "--out", h5, "--n", "32"])
        run(["pcm.measure", "--in", h5, "--out", outm])
        run(["pcm.fit_alpha", "--in", outm, "--out", outf])
        with open(outm, "r") as f:
            m = json.load(f)
        assert "sublevel" in m and "m" in m["sublevel"]
