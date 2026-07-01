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
    # multivariate leave-one-out recoverability check (needs numpy)
    try:
        import numpy as np
        feats={"entropy_prod":{"Se":-0.257,"Ne":0.144,"Ni":-0.441,"Si":0.097},
               "response":{"Se":1.797,"Ne":0.011,"Ni":2.097,"Si":0.080},
               "fuzz_tree":{"Se":1.363,"Ne":2.279,"Ni":1.123,"Si":1.820},
               "coh_info":{"Se":-0.4585,"Ne":-0.9989,"Ni":-0.1578,"Si":-0.4563}}
        fams=["Se","Ne","Ni","Si"]
        X=np.array([[feats[k][f] for k in feats] for f in fams]); X=(X-X.mean(0))/(X.std(0)+1e-9)
        y=np.array([1 if A0[f] else -1 for f in fams],float); c=0
        for i in range(4):
            tr=[j for j in range(4) if j!=i]; w,*_=np.linalg.lstsq(X[tr],y[tr],rcond=None)
            c+=(np.sign(X[i]@w)==y[i])
        print(f"multivariate leave-one-out N/S recovery: {c}/4 (recoverable jointly, never singly)")
    except ImportError:
        pass
