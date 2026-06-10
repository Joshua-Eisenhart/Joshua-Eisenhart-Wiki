#!/usr/bin/env python3
import argparse, importlib, json, platform, shutil, subprocess, sys

PY_MODULES = {
    "jax": "jax",
    "diffrax": "diffrax",
    "dynamiqs": "dynamiqs",
    "netket": "netket",
    "equinox": "equinox",
    "optax": "optax",
    "optimistix": "optimistix",
    "lineax": "lineax",
    "torch": "torch",
    "torch_geometric": "torch_geometric",
    "torchode": "torchode",
    "torchdiffeq": "torchdiffeq",
    "xitorch": "xitorch",
    "pytorch3d": "pytorch3d",
    "cvxpylayers": "cvxpylayers",
    "z3-solver": "z3",
    "cvc5": "cvc5",
    "graphology-python?": "graphology",
}

JULIA_PKGS = ["DLPack", "PythonCall", "Attractors", "DynamicalSystemsBase", "DifferentialEquations", "SymbolicSMT", "IntervalArithmetic", "ReachabilityAnalysis", "SumOfSquares", "Yao", "QuantumOptics", "ITensors", "Lux", "Octonions", "Grassmann", "Graphs", "MetaGraphsNext", "Catlab", "CombinatorialSpaces"]


def py_probe(name, module):
    try:
        m = importlib.import_module(module)
        return {"name": name, "module": module, "installed": True, "version": getattr(m, "__version__", None)}
    except Exception as exc:
        return {"name": name, "module": module, "installed": False, "error": str(exc)}


def julia_probe():
    if not shutil.which("julia"):
        return {"julia_available": False, "packages": []}
    code = """
import Pkg
for p in ARGS
    try
        Base.require(Base.PkgId(Base.UUID("00000000-0000-0000-0000-000000000000"), p))
    catch
    end
end
println(VERSION)
"""
    try:
        out = subprocess.run(["julia", "-e", "println(VERSION)"], capture_output=True, text=True, timeout=20)
        return {"julia_available": out.returncode == 0, "julia_version": out.stdout.strip(), "packages": "run project-specific Pkg.status in Lev worker image"}
    except Exception as exc:
        return {"julia_available": True, "error": str(exc), "packages": []}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    report = {
        "python": sys.version,
        "platform": platform.platform(),
        "python_modules": [py_probe(n,m) for n,m in PY_MODULES.items()],
        "julia": julia_probe(),
        "executables": {name: shutil.which(name) for name in ["julia", "node", "pnpm", "cvc5", "z3", "python"]}
    }
    print(json.dumps(report, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
