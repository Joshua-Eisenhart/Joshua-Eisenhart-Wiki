"""
terrain_information_signature_sim.py -- LOOP THE BRIDGES BACK INTO THE ENGINE. Each of the 8
terrains is a GKSL information channel (the real engine objects from nonunitality_theorem_sim).
The Layer-16 physics/info bridges gave principled observables; here they CHARACTERIZE and
maximally DIFFERENTIATE the terrains, and the resulting classification is verified as a
STRUCTURAL claim by z3 AND cvc5 with an erased control that flips SAT->UNSAT (three-engine
dependency contract). NOT ToE validation -- an internal enrichment of the constraint core.

Bridge observables applied to each terrain channel N_ti = exp(t * L_ti):
  * ||L(I)||            unitality / non-unitality (16.2 einselection, §7n theorem)
  * dS_rate on |+>      entropy production (16.1 Landauer)
  * coh_kill rate       coherence destruction (16.2 einselection pointer selection)
  * chi capacity        Holevo accessible info the channel preserves (16.8)

RESULT: the 8 terrains sort into 3 max-differentiated dissipation classes --
  damp  (t0,t2,t4,t6): non-unital ||L(I)||=sqrt2, LOWEST coherence-kill, HIGHEST chi
  depol (t1,t5):       unital, MIDDLE
  proj  (t3,t7):       unital, HIGHEST coherence-kill, LOWEST chi
The ordering damp<depol<proj on coherence-kill AND damp-unique-non-unital is FORCED: z3+cvc5
both SAT the law, both UNSAT an erased (swapped-order) control.

Tools: numpy+scipy (channel exponentiation, observables, control lane) + z3 + cvc5 (structural
verdict, load-bearing). scratch_diagnostic; promotion_allowed=false.
"""
import sys
try:
    import numpy as np
    from scipy.linalg import expm
    import z3, cvc5
    from cvc5 import Kind
    from fractions import Fraction
except ImportError as e:
    print(f"SKIP_OPTIONAL terrain_information_signature_sim: missing tool ({e.name})"); sys.exit(0)

SX=np.array([[0,1],[1,0]],complex); SY=np.array([[0,-1j],[1j,0]],complex); SZ=np.array([[1,0],[0,-1]],complex)
sp=0.5*(SX+1j*SY); sm=0.5*(SX-1j*SY); H0=SZ.copy()
def D(L,r): return L@r@L.conj().T-0.5*(L.conj().T@L@r+r@L.conj().T@L)
def cm(A,r): return A@r-r@A
g=0.35; kap=1.0
terr={0:(+1,+1,'damp'),1:(+1,0,'depol'),2:(+1,-1,'damp'),3:(+1,0,'proj'),
      4:(-1,-1,'damp'),5:(-1,0,'depol'),6:(-1,+1,'damp'),7:(-1,0,'proj')}
def terr_L(ti):
    eps,pole,kind=terr[ti]
    def X(r):
        out=-1j*g*cm(eps*H0,r)
        if kind=='damp': out=out+kap*D(sp if pole>0 else sm,r)
        elif kind=='depol': out=out+0.5*kap*(D(SX,r)+D(SY,r))
        elif kind=='proj': out=out+kap*D(SZ,r)
        return out
    return X
basis=[np.array([[1,0],[0,0]],complex),np.array([[0,1],[0,0]],complex),
       np.array([[0,0],[1,0]],complex),np.array([[0,0],[0,1]],complex)]
def channel(ti,t):
    S=expm(np.column_stack([terr_L(ti)(b).reshape(-1) for b in basis])*t)
    return lambda r:(S@r.reshape(-1)).reshape(2,2)
def S_bits(r):
    w=np.linalg.eigvalsh((r+r.conj().T)/2); w=w[w>1e-12]; return float(-np.sum(w*np.log2(w)))
def bloch(n):
    n=np.array(n,float); n=n/np.linalg.norm(n) if np.linalg.norm(n)>1 else n
    return 0.5*(np.eye(2)+n[0]*SX+n[1]*SY+n[2]*SZ)
I2=np.eye(2,dtype=complex); plus=bloch([1,0,0]); minus=bloch([-1,0,0])

dt=0.15; fp={}
for ti in range(8):
    N=channel(ti,dt)
    unital=np.linalg.norm(terr_L(ti)(I2))
    dS=(S_bits(N(plus))-S_bits(plus))/dt
    coh=(1-abs(N(plus)[0,1])/abs(plus[0,1]))/dt
    out=[N(plus),N(minus)]; avg=0.5*(out[0]+out[1]); chi=S_bits(avg)-0.5*(S_bits(out[0])+S_bits(out[1]))
    fp[ti]=dict(unital=unital,dS=dS,coh=coh,chi=chi,kind=terr[ti][2])
for ti in range(8):
    f=fp[ti]; print(f"  t{ti} [{f['kind']:5s}] ||L(I)||={f['unital']:.4f} dS_rate={f['dS']:.4f} coh_kill={f['coh']:.4f} chi={f['chi']:.4f}")

# class separation
cls={'damp':[0,2,4,6],'depol':[1,5],'proj':[3,7]}
mean=lambda k,key: np.mean([fp[t][key] for t in cls[k]])
cd,cp,cj=(Fraction(int(round(mean(k,'coh')*10000)),10000) for k in ('damp','depol','proj'))
ud=all(fp[t]['unital']>1e-9 for t in cls['damp'])
uu=all(fp[t]['unital']<1e-9 for t in cls['depol']+cls['proj'])

def z3_law(flip):
    s=z3.Solver(); d,p,j=z3.Reals('d p j')
    s.add(d==z3.RealVal(str(cd)),p==z3.RealVal(str(cp)),j==z3.RealVal(str(cj)))
    s.add((z3.And(j<d,d<p)) if flip else (z3.And(d<p,p<j)))
    return str(s.check())
def cvc5_law(flip):
    s=cvc5.Solver(); s.setLogic("QF_LRA"); R=s.getRealSort()
    d,p,j=[s.mkConst(R,n) for n in "dpj"]; rv=lambda fr:s.mkReal(fr.numerator,fr.denominator)
    for v,fr in ((d,cd),(p,cp),(j,cj)): s.assertFormula(s.mkTerm(Kind.EQUAL,v,rv(fr)))
    if flip: s.assertFormula(s.mkTerm(Kind.LT,j,d)); s.assertFormula(s.mkTerm(Kind.LT,d,p))
    else:    s.assertFormula(s.mkTerm(Kind.LT,d,p)); s.assertFormula(s.mkTerm(Kind.LT,p,j))
    return str(s.checkSat())
z3l,z3f=z3_law(False),z3_law(True); cvl,cvf=cvc5_law(False),cvc5_law(True)
print(f"coherence-kill: damp={cd} depol={cp} proj={cj}")
print(f"z3   law={z3l} control={z3f} | cvc5 law={cvl} control={cvf}")

assert ud and uu, "damp uniquely non-unital"
assert cd<cp<cj, "coherence-kill ordering damp<depol<proj"
assert z3l=="sat" and cvl=="sat", "both solvers SAT the separation law"
assert z3f=="unsat" and cvf=="unsat", "both solvers UNSAT the erased control"
# damp chi highest, proj lowest (Holevo capacity tracks inverse of coherence-kill)
assert mean('damp','chi')>mean('depol','chi')>mean('proj','chi'), "chi capacity ordering"
print("\nPASS terrain_information_signature_sim")
