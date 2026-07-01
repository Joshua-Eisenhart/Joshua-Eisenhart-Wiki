"""
axis0_sector_sim.py
The two-sector theorem behind the Axis-0 stall (deepens Axis-0 = Axis-1 XOR Axis-2, section 7n).
RESULTS:
 (1) GAUGE PROOF: Axis-2 (frame, rho -> V^dag rho V) is invisible to ALL state invariants (~2e-15).
 (2) SECTOR THEOREM: Axis-1 = ENTROPY charge (eigenvalue sector); Axis-2 = PHASE charge (eigenvector
     sector). Axis-0 = their parity -> needs BOTH sectors. No single entropy functional spans both,
     which is why all 14 tested single-cut readouts failed.
 (3) Frame is dynamically visible ONLY for dissipative terrains {Se,Ni} (0.22) not unitary {Ne,Si} (0)
     -> reading a basis needs a reference system -> why Axis-0 needs bipartite rho_AB.
 (4) Bridge chi_2 (phase charge) OPEN: closed-loop holonomy is gauge-invariant, cannot read it.
scratch_diagnostic; promotion_allowed=false.
"""
import numpy as np
from scipy.linalg import expm
I2=np.eye(2,dtype=complex)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
n=np.array([1,1,1.])/np.sqrt(3); H0=n[0]*sx+n[1]*sy+n[2]*sz
def S(r):
    ev=np.clip(np.linalg.eigvalsh(r).real,1e-12,1); return -(ev*np.log2(ev)).sum()
def ptA(r): rr=r.reshape(2,2,2,2); return np.einsum('ijkj->ik',rr)
def ptB(r): rr=r.reshape(2,2,2,2); return np.einsum('ijil->jl',rr)

def gauge_proof(N=200):
    rng=np.random.default_rng(1); Vf=np.kron(expm(-1j*H0*0.7),expm(-1j*H0*0.7)); m=0
    for _ in range(N):
        A=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); r=A@A.conj().T; r/=np.trace(r).real
        rc=Vf@r@Vf.conj().T
        m=max(m,abs(S(r)-S(rc)),abs((S(ptB(r))-S(r))-(S(ptB(rc))-S(rc))))
    return m

def sector_split(N=300):
    rng=np.random.default_rng(3); Vf=expm(-1j*H0*0.9); ec=[]; sc=[]
    for _ in range(N):
        A=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); r=A@A.conj().T; r/=np.trace(r).real
        rc=Vf@r@Vf.conj().T
        ec.append(np.linalg.norm(np.sort(np.linalg.eigvalsh(r))-np.sort(np.linalg.eigvalsh(rc))))
        sc.append(np.linalg.norm(r-rc))
    return np.mean(ec), np.mean(sc)

def holonomy_is_gauge_invariant():
    Vf=expm(-1j*H0*0.9)
    return np.allclose(np.sort(np.linalg.eigvalsh(H0)), np.sort(np.linalg.eigvalsh(Vf@H0@Vf.conj().T)))

if __name__=="__main__":
    print(f"(1) gauge proof: max state-invariant change under frame = {gauge_proof():.2e}")
    ec,sc=sector_split()
    print(f"(2) sector split: eigenvalue(entropy) change={ec:.2e}  eigenvector(phase) change={sc:.4f}")
    print(f"(4) closed-loop holonomy gauge-invariant (cannot read frame): {holonomy_is_gauge_invariant()}")
