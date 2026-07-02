# julia_engine.jl -- the 16-stage engine in Julia (fourth independent route).
#
# Contract: reads engines/targets.json for model constants, emits
# engines/julia_results.json in the shared schema; validate with
# python3 validate_engines.py.
#
# Run:  julia --project=. julia_engine.jl        (needs JSON: ] add JSON)
# Written against Julia 1.10; uses only LinearAlgebra (exp of dense matrix)
# and JSON. Pure functions, exact rationals unnecessary here (float64 contract).
# STATUS: authored in a sandbox without Julia; the FIRST laptop run of
# validate_engines.py after this emits julia_results.json is its test. If it
# disagrees with the oracle, that disagreement is a finding (CLAUDE.md rule 1).
# scratch_diagnostic; promotion_allowed=false.

using LinearAlgebra
using JSON

const HERE = @__DIR__
const C = JSON.parsefile(joinpath(HERE, "targets.json"))["model_constants"]
const G, KAP, Q, TH, T_FLOW = C["G"], C["KAP"], C["Q"], C["TH"], C["T_FLOW"]
const PROBE = C["PROBE"]

const I2 = Matrix{ComplexF64}(I, 2, 2)
const sx = ComplexF64[0 1; 1 0]
const sy = ComplexF64[0 -im; im 0]
const sz = ComplexF64[1 0; 0 -1]
const sp = 0.5 * (sx + im * sy)
const sm = 0.5 * (sx - im * sy)
const H0 = (sx + sy + sz) / sqrt(3.0)

sL(A) = kron(Matrix{ComplexF64}(I, 2, 2), A)          # rho -> A*rho on vec(rho) (column-stacking)
sR(A) = kron(transpose(A), Matrix{ComplexF64}(I, 2, 2)) # rho -> rho*A
sD(L) = sL(L) * sR(L') - 0.5 * (sL(L' * L) + sR(L' * L))
sC(H) = -im * (sL(H) - sR(H))

const TERR = Dict(0 => (+1, "damp", +1), 1 => (+1, "depol", 0), 2 => (+1, "damp", -1),
                  3 => (+1, "proj", 0), 4 => (-1, "damp", -1), 5 => (-1, "depol", 0),
                  6 => (-1, "damp", +1), 7 => (-1, "proj", 0))
const NATIVE = Dict(0 => ("Ti", "Fi"), 1 => ("Ti", "Fi"), 4 => ("Ti", "Fi"), 5 => ("Ti", "Fi"),
                    2 => ("Te", "Fe"), 3 => ("Te", "Fe"), 6 => ("Te", "Fe"), 7 => ("Te", "Fe"))

function terrain_super(ti)
    eps, kind, pole = TERR[ti]
    Ls = G * sC(eps * H0)
    if kind == "damp"
        Ls += KAP * sD(pole > 0 ? sp : sm)
    elseif kind == "depol"
        Ls += 0.5 * KAP * (sD(sx) + sD(sy))
    else
        Ls += KAP * sD(sz)
    end
    return Ls
end

function op_super(name)
    P0 = 0.5 * (I2 + sz); P1 = 0.5 * (I2 - sz)
    Qp = 0.5 * (I2 + sx); Qm = 0.5 * (I2 - sx)
    E4 = Matrix{ComplexF64}(I, 4, 4)
    name == "Ti" && return (1 - Q) * E4 + Q * (sL(P0) * sR(P0) + sL(P1) * sR(P1))
    name == "Te" && return (1 - Q) * E4 + Q * (sL(Qp) * sR(Qp) + sL(Qm) * sR(Qm))
    U = exp(-im * TH / 2 * (name == "Fi" ? sx : sz))
    return sL(U) * sR(U')
end

vecr(rho) = reshape(transpose(rho), 4)      # match python column-stacking vec(rho)=rho.T.reshape(4)
unvec(v) = transpose(reshape(v, 2, 2))
bloch(rho) = [real(tr(rho * s)) for s in (sx, sy, sz)]

function main()
    probe = 0.5 * (I2 + PROBE[1] * sx + PROBE[2] * sy + PROBE[3] * sz)
    pv = vecr(probe)
    stages = []
    for t in 0:7, o in NATIVE[t]
        Ts = terrain_super(t); Os = op_super(o)
        flow = exp(T_FLOW * Ts)
        down = bloch(unvec(Os * (flow * pv)))
        up = bloch(unvec(flow * (Os * pv)))
        push!(stages, Dict("t" => t, "op" => o, "bloch_down" => down, "bloch_up" => up,
                           "order_gap" => norm(down - up)))
    end
    terrains = []
    for t in 0:7
        Ls = terrain_super(t)
        LI = unvec(Ls * vecr(I2))
        fp = unvec(exp(8.0 * Ls) * pv); fp /= real(tr(fp))
        push!(terrains, Dict("t" => t, "nonunital" => Int(norm(LI) > 1e-9),
                             "fixed_z" => real(tr(fp * sz))))
    end
    open(joinpath(HERE, "julia_results.json"), "w") do f
        JSON.print(f, Dict("substrate" => "julia", "stages" => stages,
                           "terrains" => terrains), 1)
    end
    println("julia_results.json written (16 stages)")
end

main()
