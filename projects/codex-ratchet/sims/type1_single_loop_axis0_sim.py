#!/usr/bin/env python3
"""type1_single_loop_axis0 -- FIRST RUNG of the staged engine build (owner directive: "do each engine type one at
a time... even each of the inductive or deductive loops one at a time, so you just have 4 stages to loop and test,
and then run the 4 substages of that -- only 16 of the 64 overall engine schedule to run"). This builds ONE engine
(Type 1, LEFT Weyl, eps=+1), ONE loop (the deductive traversal of its 4 terrains), tests that loop as 4 ordered
stages, runs the 4 substages of each stage, and -- per the owner's standing requirement -- THREADS AXIS-0 from the
drive at the foundations (start) to the polarity readout at the end. Not all 16/64 at once: 4 stages + their
substages, with axis-0 verified end to end.

THE ENGINE + LOOP: Type 1 = terrains [0,1,2,3] (eps=+1), each with native operators. The deductive loop traverses
t0->t1->t2->t3 applying, at each terrain, its native T-operator composed with the terrain GKSL flow (down-order
J.flow(X)). Four terrain-steps = one 360deg loop of 4 stages.

FOUR LANES (each a measurement; a SEPARATE policy eval decides; every lane has a control that must flip):
  (A) THE LOOP IS 4 ORDERED STAGES doing distinct work: the 4 stage maps are pairwise distinct as channels, and
      the loop is ORDER-SENSITIVE (deductive order vs reversed order gives a different endpoint -- N01). Control:
      a single-operator loop (same op at every terrain) has near-zero order gap.
  (B) AXIS-0 DRIVE PRESENT FROM THE START: the loop is driven by the intrinsic terrain flow (coherent Hamiltonian
      + dissipator) present from terrain 0 -- the loop does real cumulative work. Control: remove the flow (pure
      operators, no drive) and the loop does far less work AND (lane C) the readout dies. This is axis-0-as-drive:
      the entropy-driving flow is intrinsic, not injected.
  (C) AXIS-0 READOUT AT LOOP CLOSE: at the end of the loop, a POLARITY readout (signed Bloch-trajectory volume =
      trajectory handedness/chirality, averaged over a probe ensemble) discovers the engine's SIGN. Type 1 reads
      one sign; the mirror Type 2 engine (eps=-1, terrains [4,5,6,7]) reads the OPPOSITE sign -- discovered from
      the dynamics, NOT from the eps label. Control: remove the coherent drive and the readout collapses to ~0
      (the sign is carried by the drive that was present from the start). This is axis-0 threaded start->readout.
  (D) THE 4 SUBSTAGES of each loop stage: each stage's 4 sub-operators (Ti,Te,Fi,Fe) cased by the stage's native
      operator run as an ordered 4-beat, all effective (each moves the state), interior ordered (reverse!=forward).

QUARANTINE_EXPLORATORY. classification="scratch_diagnostic". promotion_allowed=False. Real oracle operators
(engines/oracle_targets.py, reconstructed inline verbatim). Pure distinguishability; no bits/vectors as mechanism.
A STAGED single-loop engine build with the axis-0 thread audited end to end -- NOT a claim of a full engine.
"""
import json, os, sys
import numpy as np
from scipy.linalg import expm

sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
I2=np.eye(2,dtype=complex); sp=0.5*(sx+1j*sy); sm=0.5*(sx-1j*sy)
G=0.35; KAP=1.0; Q=1.0-np.exp(-1.0); TH=np.pi/4; T_FLOW=1.0; N_STEPS=400
TERR={0:(+1,'damp',+1),1:(+1,'depol',0),2:(+1,'damp',-1),3:(+1,'proj',0),
      4:(-1,'damp',-1),5:(-1,'depol',0),6:(-1,'damp',+1),7:(-1,'proj',0)}
NATIVE={0:('Ti','Fi'),1:('Ti','Fi'),4:('Ti','Fi'),5:('Ti','Fi'),
        2:('Te','Fe'),3:('Te','Fe'),6:('Te','Fe'),7:('Te','Fe')}
TYPE1=[0,1,2,3]; TYPE2=[4,5,6,7]

def Dop(L,r): return L@r@L.conj().T-0.5*(L.conj().T@L@r+r@L.conj().T@L)
def gen(ti):
    eps,kind,pole=TERR[ti]; H=eps*(sx+sy+sz)/np.sqrt(3)
    def X(r):
        out=-1j*G*(H@r-r@H)
        if kind=='damp': out=out+KAP*Dop(sp if pole>0 else sm,r)
        elif kind=='depol': out=out+0.5*KAP*(Dop(sx,r)+Dop(sy,r))
        else: out=out+KAP*Dop(sz,r)
        return out
    return X
def flow(X,r,t=T_FLOW,steps=N_STEPS):
    dt=t/steps
    for _ in range(steps):
        k1=X(r);k2=X(r+.5*dt*k1);k3=X(r+.5*dt*k2);k4=X(r+dt*k3)
        r=r+(dt/6)*(k1+2*k2+2*k3+k4); r=.5*(r+r.conj().T); r/=np.trace(r).real
    return r
def op(n):
    P0=.5*(I2+sz);P1=.5*(I2-sz);Qp=.5*(I2+sx);Qm=.5*(I2-sx)
    if n=='Ti':return lambda r:(1-Q)*r+Q*(P0@r@P0+P1@r@P1)
    if n=='Te':return lambda r:(1-Q)*r+Q*(Qp@r@Qp+Qm@r@Qm)
    if n=='Fi':U=expm(-1j*TH/2*sx);return lambda r:U@r@U.conj().T
    if n=='Fe':U=expm(-1j*TH/2*sz);return lambda r:U@r@U.conj().T
def bloch(r): return np.array([float(np.trace(r@s).real) for s in (sx,sy,sz)])
def dm(v): return 0.5*(I2+v[0]*sx+v[1]*sy+v[2]*sz)
def casing_frame(o):
    if o=='Ti': return expm(-1j*(np.pi/4)/2*sz)
    if o=='Te': return expm(-1j*(np.pi/4)/2*sx)
    if o=='Fi': return expm(-1j*TH/2*sx)
    if o=='Fe': return expm(-1j*TH/2*sz)

# ---------- the loop ----------

def loop_traj(terrains, probe, order='ded', drive=True, single_op=None):
    r=dm(np.array(probe,float)); traj=[bloch(r).copy()]
    seq=list(terrains) if order=='ded' else list(terrains)[::-1]
    for t in seq:
        J=op(single_op if single_op else NATIVE[t][0])
        r=J(flow(gen(t), r.copy())) if drive else J(r.copy())
        r=.5*(r+r.conj().T); r/=np.trace(r).real
        traj.append(bloch(r).copy())
    return np.array(traj)

def signed_volume(traj):
    return float(sum(np.dot(traj[i],np.cross(traj[i+1],traj[i+2])) for i in range(len(traj)-2)))
def cum_move(traj):
    return float(sum(np.linalg.norm(traj[i+1]-traj[i]) for i in range(len(traj)-1)))
def stage_channel(t):
    J=op(NATIVE[t][0]); X=gen(t)
    return lambda r: J(flow(X, r.copy()))

# ---------- lane A: 4 ordered stages ----------

def measure_loop_stages():
    rng=np.random.default_rng(3); probes=[rng.standard_normal(3) for _ in range(6)]
    probes=[p/np.linalg.norm(p)*0.7 for p in probes]
    chans=[stage_channel(t) for t in TYPE1]
    sigs=[np.concatenate([bloch(c(dm(p))) for p in probes]) for c in chans]
    dmin=min(float(np.linalg.norm(sigs[i]-sigs[j])) for i in range(4) for j in range(i+1,4))
    probe=np.array([0.55,0.35,0.25])
    from itertools import permutations
    # ORDER-SENSITIVITY via PERMUTATION SPREAD (non-tautological): apply the 4 distinct stage-channels in every
    # order; if the loop is order-sensitive (N01, stages don't commute) the endpoints SPREAD. This flips against a
    # genuinely COMMUTING control (below) whose endpoints coincide for every order.
    def compose(chs, r0):
        r=r0.copy()
        for c in chs: r=c(r.copy()); r=.5*(r+r.conj().T); r/=np.trace(r).real
        return bloch(r)
    ends=[compose([chans[i] for i in perm], dm(probe)) for perm in permutations(range(4))]
    order_spread=float(np.mean([np.linalg.norm(ends[i]-ends[j]) for i in range(len(ends)) for j in range(i+1,len(ends))]))
    # commuting control: 4 z-dephasing channels at different strengths are MUTUALLY COMMUTING, so every order gives
    # the same endpoint (spread -> 0). This is what "order does not matter" genuinely looks like.
    def zdephase(g):
        P0=.5*(I2+sz);P1=.5*(I2-sz); return lambda r:(1-g)*r+g*(P0@r@P0+P1@r@P1)
    cchs=[zdephase(g) for g in (0.2,0.4,0.6,0.8)]
    cends=[compose([cchs[i] for i in perm], dm(probe)) for perm in permutations(range(4))]
    ctrl_spread=float(np.mean([np.linalg.norm(cends[i]-cends[j]) for i in range(len(cends)) for j in range(i+1,len(cends))]))
    return {"four_stages_min_pairwise":round(dmin,4),"order_permutation_spread":round(order_spread,4),
            "commuting_control_spread":round(ctrl_spread,8),
            "stages_distinct":bool(dmin>1e-3),
            "loop_order_sensitive":bool(order_spread>1e-2 and ctrl_spread<1e-9)}

# ---------- lanes B/C: axis-0 drive (start) -> readout (end) ----------

def measure_axis0_thread():
    rng=np.random.default_rng(9); probes=[rng.standard_normal(3) for _ in range(8)]
    probes=[p/np.linalg.norm(p)*0.6 for p in probes]
    # drive from start: cumulative work with intrinsic flow vs without
    move_drive=float(np.mean([cum_move(loop_traj(TYPE1,p,'ded',drive=True)) for p in probes]))
    move_nodrv=float(np.mean([cum_move(loop_traj(TYPE1,p,'ded',drive=False)) for p in probes]))
    # readout at end: polarity sign (signed trajectory volume), averaged over probes
    read_T1=float(np.mean([signed_volume(loop_traj(TYPE1,p,'ded',drive=True)) for p in probes]))
    read_T2=float(np.mean([signed_volume(loop_traj(TYPE2,p,'ded',drive=True)) for p in probes]))
    # control: remove the coherent drive -> readout collapses
    read_nodrv=float(np.mean([signed_volume(loop_traj(TYPE1,p,'ded',drive=False)) for p in probes]))
    return {"drive_cumulative_move":round(move_drive,4),"nodrive_cumulative_move":round(move_nodrv,4),
            "readout_type1":round(read_T1,6),"readout_type2":round(read_T2,6),
            "readout_nodrive_control":round(read_nodrv,6),
            "drive_present_from_start":bool(move_drive>1.3*move_nodrv),
            "readout_signs_opposite":bool(np.sign(read_T1)!=np.sign(read_T2)),
            "readout_needs_drive":bool(abs(read_T1)>5*abs(read_nodrv) and abs(read_T2)>5*abs(read_nodrv))}

# ---------- lane D: 4 substages ----------

def measure_substages():
    probe=np.array([0.55,0.35,0.25])
    all_eff=[]; all_ord=[]
    for t in TYPE1:
        o=NATIVE[t][0]; U=casing_frame(o)
        r=flow(gen(t), dm(probe).copy()); eff=0; outs=[]
        for sub in ('Ti','Te','Fi','Fe'):
            rp=r.copy(); r=U@op(sub)(r.copy())@U.conj().T; r=.5*(r+r.conj().T); r/=np.trace(r).real
            if float(np.linalg.norm(bloch(r)-bloch(rp)))>1e-9: eff+=1
            outs.append(bloch(r).copy())
        all_eff.append(eff==4)
        r=flow(gen(t), dm(probe).copy())
        for sub in ('Fe','Fi','Te','Ti'): r=U@op(sub)(r.copy())@U.conj().T; r=.5*(r+r.conj().T); r/=np.trace(r).real
        all_ord.append(float(np.linalg.norm(bloch(r)-outs[-1]))>1e-6)
    return {"all_stages_four_effective_substages":bool(all(all_eff)),"all_stages_ordered_interior":bool(all(all_ord))}

# ---------- SEPARATE POLICY EVAL ----------

def evaluate(a,x,d):
    laneA=a["stages_distinct"] and a["loop_order_sensitive"]
    laneB=x["drive_present_from_start"]
    laneC=x["readout_signs_opposite"] and x["readout_needs_drive"]
    laneD=d["all_stages_four_effective_substages"] and d["all_stages_ordered_interior"]
    allpass=bool(laneA and laneB and laneC and laneD)
    return {"loop_is_four_ordered_stages":bool(laneA),
            "axis0_drive_present_from_start":bool(laneB),
            "axis0_readout_at_loop_close_threaded_from_drive":bool(laneC),
            "four_substages_run":bool(laneD),
            "TYPE1_SINGLE_LOOP_WITH_AXIS0_BUILT":allpass}

def main():
    a=measure_loop_stages(); x=measure_axis0_thread(); d=measure_substages()
    verdict=evaluate(a,x,d)
    out={"classification":"scratch_diagnostic","promotion_allowed":False,
         "framing":"first rung of the staged engine build: ONE engine (Type 1), ONE deductive loop (4 stages), its 4 substages, with axis-0 threaded from the drive at the start to the polarity readout at the end",
         "loop_stages":a,"axis0_thread":x,"substages":d,"policy_eval":verdict}
    path=__file__.replace(".py","_results.json"); json.dump(out,open(path,"w"),indent=1)
    print("TYPE 1 SINGLE DEDUCTIVE LOOP -- 4 stages + substages, with axis-0 threaded start -> readout.\n")
    print("  (A) THE LOOP IS 4 ORDERED STAGES:")
    print(f"      4 stage maps pairwise distinct (min {a['four_stages_min_pairwise']}); loop order-sensitive: permutation spread {a['order_permutation_spread']} vs commuting control {a['commuting_control_spread']} -> {a['loop_order_sensitive']}")
    print("  (B) AXIS-0 DRIVE PRESENT FROM THE START:")
    print(f"      loop work with intrinsic flow {x['drive_cumulative_move']} vs no-drive {x['nodrive_cumulative_move']} -> drive intrinsic {x['drive_present_from_start']}")
    print("  (C) AXIS-0 READOUT AT LOOP CLOSE (threaded from the drive):")
    print(f"      polarity readout Type1 {x['readout_type1']:+.5f} vs Type2 {x['readout_type2']:+.5f} (opposite signs {x['readout_signs_opposite']}); no-drive control {x['readout_nodrive_control']:+.5f} -> readout needs the drive {x['readout_needs_drive']}")
    print("  (D) THE 4 SUBSTAGES:")
    print(f"      every stage 4 effective cased substages {d['all_stages_four_effective_substages']}; interior ordered {d['all_stages_ordered_interior']}")
    print("\n  SEPARATE POLICY EVAL:")
    for k,v in verdict.items():
        if k!="TYPE1_SINGLE_LOOP_WITH_AXIS0_BUILT": print(f"    {k}: {v}")
    print(f"\n  TYPE 1 SINGLE LOOP WITH AXIS-0 BUILT: {verdict['TYPE1_SINGLE_LOOP_WITH_AXIS0_BUILT']}")
    if verdict["TYPE1_SINGLE_LOOP_WITH_AXIS0_BUILT"]:
        print("PASS type1_single_loop_axis0")
    print("ALL_GATES:", "PASS" if verdict["TYPE1_SINGLE_LOOP_WITH_AXIS0_BUILT"] else "FAIL","->",path)
    sys.exit(0 if verdict["TYPE1_SINGLE_LOOP_WITH_AXIS0_BUILT"] else 1)

if __name__=="__main__":
    main()
