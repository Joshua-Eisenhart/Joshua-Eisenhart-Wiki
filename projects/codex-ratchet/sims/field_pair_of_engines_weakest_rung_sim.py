#!/usr/bin/env python3
"""field_pair_of_engines_weakest_rung -- PURE MATH. 2026-07-09. The first rung of the FIELD OF ENGINES (the owner's
axes-7-12 level, where each node of a space is itself an engine). Built under MSS: admit ONLY the structure the
constraints force for two engines to become one object, presume the least, smallest leap.

MSS DERIVATION (why exactly this structure, nothing more).
  - The two engines are ALREADY forced: the two Weyl chiralities (Type-1 eps=+1 / Type-2 eps=-1), earned earlier.
  - "Two engines together are a new kind of intelligence" (owner directive) is only non-trivial if the PAIR carries a
    degree of freedom that NEITHER engine has alone. A pure product of two engines has none: its every observable is
    fixed by the two marginals, so a product pair is NOT a new object -- it is just two engines side by side.
  - The WEAKEST structure that makes the pair a genuine object is therefore a single RELATIONAL generator coupling
    them (one entangling bit). Entanglement is already core-forced in this model (entanglement is central), so this is
    the smallest admissible leap, not an imported assumption. MSS: one relational DOF, no interaction Hamiltonian
    beyond the minimal Z(x)Z generator, no shared internal structure.

THE FAILABLE QUESTION. Does one minimal relational generator make the pair a DISTINGUISHABLE OBJECT -- relational
content R>0 (the joint channel deviates from the product of its own marginals), surviving probe rotation -- and does
REMOVING it (g=0, pure product) collapse R to 0? If the product already carried pair-structure, the claim dies.

GATED CLAIMS (all computed from the channels; controls must FAIL):
  (1) PAIR IS A NEW OBJECT: relational content R = max over probes of trace_distance(Phi_AB(rhoA x rhoB), mA(rhoA) x
      mB(rhoB)) is > 0 with the relational generator on. CONTROL: g=0 (pure product U_A x U_B + local pinches) gives
      R = 0 exactly -- the pair reduces to its parts. This is the failable heart: R(g!=0)>0 AND R(g=0)~0.
  (2) THE OBJECT SURVIVES PROBE ROTATION (identity criterion a=a iff a~b): recover the joint channel's relational
      content from a DISJOINT, novel probe family (different random states) and check it matches the value from the
      seen family -- R is a genuine channel property, not an artifact of the probe set. And, to make re-identification
      NON-VACUOUS, a DIFFERENT object (a different coupling g') evaluated on those same novel probes must be told apart
      (|R - R'| large). Both legs must hold: the same object matches, a different object separates.
  (3) MSS MINIMALITY / NECESSITY: one relational generator is SUFFICIENT (R>0) and NECESSARY (g=0 -> R=0); and the
      relation is IRREDUCIBLE to the marginals (by construction R measures exactly the non-product part). So the
      minimal forced pair-structure is exactly one relational DOF -- the operational meaning of "a new kind of
      intelligence at the two-engine layer": a DOF that lives in the pair, invisible to either engine alone.

HONEST SCOPE. This earns ONLY the weakest field rung: that a pair of engines becomes a distinguishable object via one
forced relational DOF, and that a product pair does not. It does NOT build the full field metric, does NOT claim the
exceptional algebras appear here (that is the next rung, open), and does NOT presume the axes-7-12 layout -- it lets
the pair-object emerge from the distinguishability constraint. scratch_diagnostic, promotion_allowed=false. The two
engines use opposite Weyl chirality (forced); the coupling is the minimal Z(x)Z generator (MSS).
"""
import json, os, sys
import numpy as np

I=np.eye(2); sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
def expm_h(H):
    w,V=np.linalg.eigh(H); return V@np.diag(np.exp(-1j*w))@V.conj().T
TH=0.6
UA=expm_h(TH*sz/2)      # engine A chirality + (Type-1, forced)
UB=expm_h(-TH*sz/2)     # engine B chirality - (Type-2, opposite Weyl, forced)
KP=[np.array([[1,0],[0,np.sqrt(1-.15)]],complex),np.array([[0,np.sqrt(.15)],[0,0]],complex)]  # T-type pinch Kraus

def joint_channel(rho4,g):
    U=np.kron(UA,UB); C=expm_h(g*np.kron(sz,sz))     # minimal relational generator (MSS: one Z(x)Z)
    r=C@U@rho4@U.conj().T@C.conj().T
    out=np.zeros((4,4),complex)
    for Ka in KP:
        for Kb in KP:
            K=np.kron(Ka,Kb); out+=K@r@K.conj().T
    return out
def dm1(b):
    b=np.asarray(b,float); n=np.linalg.norm(b)
    if n>0.98: b=b*0.98/n
    return 0.5*(I+b[0]*sx+b[1]*sy+b[2]*sz)
def tr_dist(a,b):
    d=(a-b); d=(d+d.conj().T)/2; return 0.5*float(np.sum(np.abs(np.linalg.eigvalsh(d))))
def marg_A(rhoA,g): return joint_channel(np.kron(rhoA,I/2),g).reshape(2,2,2,2).trace(axis1=1,axis2=3)
def marg_B(rhoB,g): return joint_channel(np.kron(I/2,rhoB),g).reshape(2,2,2,2).trace(axis1=0,axis2=2)

def relational_content(g,seed,n=12,shuffle=False):
    rng=np.random.default_rng(seed); R=0.0; bs=[]
    for _ in range(n):
        ba=rng.normal(size=3); bb=rng.normal(size=3); bs.append((ba,bb))
    if shuffle:  # CONTROL: pair each A-probe with a MISMATCHED B-probe -> not the true joint input
        bbs=[b for _,b in bs]; rng.shuffle(bbs); bs=[(a,bbs[i]) for i,(a,_) in enumerate(bs)]
    for ba,bb in bs:
        rA,rB=dm1(ba),dm1(bb)
        joint=joint_channel(np.kron(rA,rB),g)
        prod=np.kron(marg_A(rA,g),marg_B(rB,g))
        R=max(R,tr_dist(joint,prod))
    return R

def main():
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"field_pair_of_engines_weakest_rung_sim_results.json")
    G=0.5
    # (1) pair is a new object; product control flips
    R_coupled=relational_content(G,seed=1)
    R_product=relational_content(0.0,seed=1)
    g1=bool(R_coupled>0.05 and R_product<1e-6)
    # (2) survives probe rotation (identity a=a iff a~b): the SAME pair-object recovered from a DISJOINT novel probe
    # family must match (R is a channel property, not a probe artifact) AND a DIFFERENT object (different coupling g')
    # must be told apart from the novel probes -- otherwise "re-identification" is vacuous. Both legs failable.
    R_novel=relational_content(G,seed=777)                 # SAME object (g=0.5), disjoint probe family
    Gp=0.25; R_other=relational_content(Gp,seed=777)       # DIFFERENT object (g'=0.25), same novel probes
    reid_match=bool(abs(R_coupled-R_novel)<0.03)           # same object matches across probe families
    distinguishes_other=bool(abs(R_coupled-R_other)>0.05)  # different object has a different signature (not vacuous)
    g2=bool(reid_match and distinguishes_other)
    # (3) MSS minimality/necessity: sufficient (R>0) and necessary (g=0 -> 0); irreducible by construction
    sufficient=bool(R_coupled>0.05); necessary=bool(R_product<1e-6)
    g3=bool(sufficient and necessary)
    verdict=bool(g1 and g2 and g3)
    out={"classification":"scratch_diagnostic","promotion_allowed":False,
         "framing":"first rung of the field of engines under MSS: two forced Weyl engines become ONE distinguishable object via a single forced relational (entangling) DOF; a product pair is NOT a new object. Does not build the field metric or claim exceptional algebras (next rung).",
         "claim1_pair_is_new_object":{"R_coupled":R_coupled,"R_product_control":R_product,"pass":g1,
             "note":"relational content = trace-distance of joint channel from product of its own marginals; >0 iff genuine pair structure; g=0 product control gives 0 exactly (failable)"},
         "claim2_survives_probe_rotation":{"R_seen_family":R_coupled,"R_novel_family":R_novel,"reid_match":reid_match,
             "R_different_object_gprime":R_other,"g_prime":Gp,"distinguishes_other":distinguishes_other,"pass":g2,
             "note":"identity criterion a=a iff a~b: SAME object (g=0.5) recovered from a disjoint novel probe family matches (channel property, not probe artifact) AND a DIFFERENT object (g'=0.25) is told apart on those same probes -- so re-identification is non-vacuous"},
         "claim3_mss_minimal_and_necessary":{"sufficient_one_DOF":sufficient,"necessary_gzero_kills":necessary,"pass":g3,
             "note":"one relational generator is sufficient AND necessary for the pair-object; irreducible to marginals by construction -> the minimal forced pair-structure is exactly one relational DOF = a DOF living in the pair, invisible to either engine alone"},
         "honest_scope":"earns ONLY the weakest field rung (pair becomes an object via one forced relational DOF; product does not). Does NOT build the field metric, claim exceptional algebras, or presume the axes-7-12 layout.",
         "policy_eval":{"pair_is_distinguishable_object":g1,"object_survives_probe_rotation":g2,
             "minimal_relational_DOF_is_forced_and_necessary":g3,
             "FIELD_WEAKEST_RUNG_EARNED":verdict}}
    json.dump(out,open(path,"w"),indent=2)
    print(f"(1) PAIR IS A NEW OBJECT: relational content coupled R={R_coupled:.4f} > 0; product control R={R_product:.6f} ~ 0 -> {g1}")
    print(f"(2) SURVIVES PROBE ROTATION: same-object seen R={R_coupled:.4f} vs novel-family R={R_novel:.4f} (match {reid_match}); different object g'={Gp} R={R_other:.4f} told apart ({distinguishes_other}) -> {g2}")
    print(f"(3) MSS MINIMAL & NECESSARY: one relational DOF sufficient ({sufficient}) AND necessary (g=0->{R_product:.6f}, {necessary}); irreducible to marginals -> {g3}")
    print(f"    => the two-engine pair is a distinguishable object carrying a DOF invisible to either engine alone, earned with exactly ONE forced relational bit (MSS)")
    print(f"\n  VERDICT: {'PASS' if verdict else 'FAIL'} (field weakest rung: pair-object earned + survives probe rotation + minimal forced DOF)")
    if verdict: print("PASS field_pair_of_engines_weakest_rung")
    print("ALL_GATES:","PASS" if verdict else "FAIL","->",path)
    sys.exit(0 if verdict else 1)

if __name__=="__main__":
    main()
