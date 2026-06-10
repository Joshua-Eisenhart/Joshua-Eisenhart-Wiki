#!/usr/bin/env julia
# Probe optional Julia package availability for the Lev sim-eval provider lane.
# This script does not install packages. It only reports whether imports work.
using JSON

packages = [
  "DLPack",
  "PythonCall",
  "Attractors",
  "DynamicalSystemsBase",
  "DifferentialEquations",
  "SymbolicSMT",
  "Satisfiability",
  "IntervalArithmetic",
  "TaylorModels",
  "ReachabilityAnalysis",
  "SumOfSquares",
  "JuMP",
  "Graphs",
  "MetaGraphsNext",
  "Catlab",
  "CombinatorialSpaces",
  "Octonions",
  "Quaternions",
  "Grassmann",
  "Yao",
  "QuantumOptics",
  "QuantumToolbox",
  "ITensors",
  "ITensorMPS",
  "Lux",
  "CUDA",
  "KernelAbstractions"
]

results = Dict{String,Any}()
for pkg in packages
    try
        @eval Main eval(Meta.parse("import $pkg"))
        results[pkg] = Dict("available" => true, "error" => nothing)
    catch e
        results[pkg] = Dict("available" => false, "error" => sprint(showerror, e))
    end
end

report = Dict(
  "probe" => "julia_support_probe",
  "julia_version" => string(VERSION),
  "packages" => results
)
println(JSON.json(report, 2))
