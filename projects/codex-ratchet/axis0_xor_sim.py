"""
axis0_xor_sim.py
Resolves the Axis-0 stall: Axis-0 = Axis-1 XOR Axis-2 (exact, verified against the repo operator
table igt-pattern-explicit-math-reference.md lines 475-478).
{Ne,Ni} (intuition/N) = terrains where dynamics-axis and frame-axis DISAGREE.
{Se,Si} (sensing/S)   = terrains where they AGREE.
XOR is not linearly separable -> no single scalar readout can realize Axis-0. This is why all 14
tested single-cut readouts collapsed to Axis-1/Axis-2. The Xi bridge (bipartite rho_AB) is a
2-subsystem = 2-axis construction; it must be engineered to compute the parity, with the discrete
{Ne,Ni}=N / {Se,Si}=S lattice as its correctness target. scratch_diagnostic; promotion_allowed=false.
"""
# Axis-1: dissipative {Se,Ni}=0 | unitary {Ne,Si}=1
A1={"Se":0,"Ne":1,"Ni":0,"Si":1}
# Axis-2: direct {Se,Ne}=0 | conjugated {Ni,Si}=1
A2={"Se":0,"Ne":0,"Ni":1,"Si":1}
# Axis-0 target (discrete N/S projection): {Ne,Ni}=N=1 | {Se,Si}=S=0
A0={"Se":0,"Ne":1,"Ni":1,"Si":0}

if __name__=="__main__":
    print("family | Axis1 | Axis2 | XOR | Axis0-target | match")
    allok=True
    for f in ["Se","Ne","Ni","Si"]:
        xor=A1[f]^A2[f]; ok=(xor==A0[f]); allok&=ok
        print(f"  {f:3s}  |   {A1[f]}   |   {A2[f]}   |  {xor}  |      {A0[f]}       | {'OK' if ok else 'NO'}")
    print(f"\nAxis-0 = Axis-1 XOR Axis-2 : {allok}")
    # NOTE: a multivariate leave-one-family-out lstsq fit was considered as a corroborator but is
    # STATISTICALLY VACUOUS (3 training points vs 4 features is underdetermined -> perfect score
    # guaranteed, zero evidential weight). It is deliberately omitted. The XOR identity above is
    # deterministic algebra on the axis labels and needs no statistical support.
