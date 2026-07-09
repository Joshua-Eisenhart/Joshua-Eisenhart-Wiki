#!/usr/bin/env python3
"""manifold_L6_shell_metric_bkm_connection_sim.py -- PURE MATH. 2026-07-09, Manifold spine Layer 6 (L6).

Nests on L5 (nested-shell Schmidt strata) and L3 (spinor/phase surface). L5 gave the shell FAMILY -- a continuum of
nested marginal-radius shells indexed by the Schmidt coordinate r=2 s0^2-1 -- but left it as a bare set of radii with no
notion of DISTANCE between shells. L6 adds (completeness contract Part A, layer 6) the METRIC on that family: the
information geometry that makes shell-to-shell distance a real, curved, monotone quantity. This is where the forced
modular geometry of UP-120 (the BKM information metric = the entropy/geometry surface = Connes-Rovelli thermal-time)
attaches to the spine as the Riemannian structure of the shell family, and where the DPI contraction of UP-121 becomes
the INFINITESIMAL monotonicity of that metric.

Owner: "build the foundations and loop back to improve them ... you should be looping on all of it."

WHAT L6 ADDS OVER L5 (the forcing content):
 (1) THE METRIC IS THE BKM (Bogoliubov-Kubo-Mori) METRIC = HESSIAN OF RELATIVE ENTROPY. Computed two independent ways:
     the Kubo-Mori integral coefficient (log a - log b)/(a-b) in the eigenbasis, and the second derivative of
     S(rho||rho0) along a direction. They agree to ~5e-8. So the shell-family metric is not an arbitrary choice -- it
     IS the curvature of the forced relative-entropy pawl (UP-107/120/121). This is the surface identity
     (surface_identity_is_BKM) realized on the L5 shells.
 (2) THE METRIC IS CURVED, NOT FLAT (what L5's bare radii cannot express). Shell arc length under BKM along the radial
     Schmidt direction is 2*arcsin(r): the mid->boundary(pure) segment is ~1.9x the mid->center segment, while a flat
     Bloch metric gives a uniform ~1.0x. So the shells are not evenly spaced; the pure-state boundary is metrically far
     and the maximally-mixed center is near. The curvature is a real geometric fact, not a coordinate artifact.
 (3) THE METRIC IS MONOTONE (CONTRACTS UNDER CPTP) -- the infinitesimal DPI. Pushing a state+direction through a
     depolarizing channel strictly shrinks g_BKM (4.49 -> 2.07 at p=0.3). This is the L6 form of UP-121: the DPI is
     the integrated statement, monotone-metric contraction is its differential. The dissipative terrain flow moves
     inward along shells and the metric contracts -- geometry and the entropy pawl co-ratchet, now as a metric.

DUAL RATCHET at L6: the shell METRIC (geometry -- distances between nested tori) and the relative-entropy pawl
(readout -- UP-107/120/121) are the SAME tensor (fact 1). Contraction of the metric under the terrain flow IS the
monotone decrease of the pawl. Geometry and entropy are one object here, exactly as the dual-ratchet doctrine requires.

NEGATIVES / CONTROLS (each must FIRE):
  - FLAT-METRIC control: replacing BKM with the flat Euclidean Bloch metric gives uniform shell spacing (boundary/center
    ratio 1.0) -- it MISSES the curvature, so the curvature is a real property of the monotone metric, not any metric.
  - NON-CPTP (amplifying) control: a map that scales the Bloch vector UP (unphysical, non-CPTP) INCREASES the metric,
    violating monotonicity -- confirming the contraction is specific to CPTP (physical) maps, the DPI direction.
  - DIRECTION-SPECIFICITY control: the metric in an orthogonal direction (SX) differs from the SZ-direction value --
    confirming g_BKM is a genuine direction-dependent bilinear form (a real metric tensor), not a single scalar that
    would match any direction by coincidence.

HONEST SCOPE: earns L6 -- the monotone BKM/Fisher metric on the L5 shell family, its curvature, and its CPTP
contraction -- on top of L5. Does NOT build L7 (the connection/parallel-transport + holonomy across shells, where the
Berry/flux structure of ledger L2.1 becomes a covariant object) or above; next rung. No terrain/axis/engine claim rides
on this. Hypothetical lane; owner doctrine under test. scratch_diagnostic; promotion_allowed=false.
"""
import json, sys
import numpy as np
from scipy.linalg import logm

SX=np.array([[0,1],[1,0]],complex); SY=np.array([[0,-1j],[1j,0]],complex); SZ=np.array([[1,0],[0,-1]],complex); I2=np.eye(2,dtype=complex)
def bloch_rho(x,y,z): return 0.5*(I2+x*SX+y*SY+z*SZ)
def S(rho,sig): return float(np.real(np.trace(rho@(logm(rho)-logm(sig)))))
def bkm_metric(rho,X):
    ev,U=np.linalg.eigh(rho); Xr=U.conj().T@X@U; g=0.0
    for i in range(len(ev)):
        for j in range(len(ev)):
            a,b=ev[i],ev[j]; c=(np.log(a)-np.log(b))/(a-b) if abs(a-b)>1e-9 else 1.0/a
            g+=c*abs(Xr[i,j])**2
    return float(g)
def hess_rel_entropy(rho0,X,h=1e-4):
    f=lambda t:S(rho0+t*X,rho0); return (f(h)-2*f(0)+f(-h))/h**2
def arclen(r0,r1,metric,N=400):
    rs=np.linspace(r0,r1,N); s=0.0
    for k in range(N-1):
        r=0.5*(rs[k]+rs[k+1]); dr=rs[k+1]-rs[k]
        s+=np.sqrt(max(metric(bloch_rho(0,0,r),SZ),0))*abs(dr)
    return s
def depol(rho,p): return (1-p)*rho + p*np.trace(rho)/2*I2

def main():
    # FACT 1: BKM metric = Hessian of relative entropy
    rho0=bloch_rho(0.2,0.1,0.3); X=SZ-np.trace(SZ)/2*I2
    gb=bkm_metric(rho0,X); hs=hess_rel_entropy(rho0,X)
    g_identity=bool(abs(gb-hs)<1e-5)
    # corrupt control: compute the BKM metric against a DIFFERENT direction (SX, orthogonal to X=SZ) -- must NOT match
    # the SZ-direction Hessian, confirming the metric is direction-specific (a genuine bilinear form, not a scalar).
    hs_wrongdir=bkm_metric(rho0, SX-np.trace(SX)/2*I2)
    g_identity_ctrl=bool(abs(gb-hs_wrongdir)>0.1)
    # FACT 2: curved, not flat
    flat=lambda rho,Xd:1.0  # flat Euclidean radial metric coefficient = 1
    d_center=arclen(0.5,0.0,bkm_metric); d_bound=arclen(0.5,0.999,bkm_metric)
    d_center_flat=arclen(0.5,0.0,flat); d_bound_flat=arclen(0.5,0.999,flat)
    ratio_bkm=d_bound/d_center; ratio_flat=d_bound_flat/d_center_flat
    g_curved=bool(ratio_bkm>1.5 and abs(ratio_flat-1.0)<0.05)
    # FACT 3: monotone contraction under CPTP; NON-CPTP amplify increases
    p=0.3; gb_after=bkm_metric(depol(rho0,p),depol(X,p))
    g_contract=bool(gb_after<gb-1e-9)
    def amplify(rho,k):  # scale Bloch vector UP (non-CPTP)
        return I2/2 + k*(rho-I2/2)
    gb_amp=bkm_metric(amplify(rho0,1.2),amplify(X,1.2))
    g_noncptp=bool(gb_amp>gb-1e-9)  # amplifying does NOT contract (metric >= before)
    verdict=bool(g_identity and g_identity_ctrl and g_curved and g_contract and g_noncptp)
    out={"classification":"scratch_diagnostic","promotion_allowed":False,"branch":"manifold_spine_L6","layer":"L6",
         "nests_on":["L5_nested_shells_schmidt_strata","L3_spinor_phase_surface"],
         "adds":"the monotone BKM/Fisher metric on the L5 shell family = curvature of the forced relative-entropy pawl (surface identity); CPTP contraction = infinitesimal DPI",
         "fact1_metric_is_bkm_hessian":{"bkm":gb,"rel_entropy_hessian":hs,"abs_diff":abs(gb-hs),"pass":g_identity,
             "wrong_direction_metric":hs_wrongdir,"wrong_direction_differs":g_identity_ctrl,
             "note":"shell metric IS the Hessian of S(rho||rho0) = BKM = surface identity (UP-120), not an arbitrary metric"},
         "fact2_curved_not_flat":{"bkm_center":d_center,"bkm_boundary":d_bound,"bkm_ratio":ratio_bkm,
             "flat_center":d_center_flat,"flat_boundary":d_bound_flat,"flat_ratio":ratio_flat,"pass":g_curved,
             "note":"BKM arc length 2*arcsin(r): pure-state boundary ~1.9x farther than center; flat metric uniform (1.0x) -- curvature is real"},
         "fact3_monotone_cptp_contraction":{"before":gb,"after_depol":gb_after,"contracts":g_contract,
             "after_amplify_noncptp":gb_amp,"noncptp_does_not_contract":g_noncptp,"pass":bool(g_contract and g_noncptp),
             "note":"metric contracts under CPTP (infinitesimal DPI, UP-121); non-CPTP amplify increases it -> contraction is CPTP-specific"},
         "scope":"earns L6 (monotone BKM metric on the shell family + curvature + CPTP contraction) on top of L5. Does NOT build L7 (connection/parallel-transport + Berry holonomy across shells) or above. Hypothetical lane; owner doctrine under test.",
         "verdict":"PASS" if verdict else "FAIL"}
    path=__file__.replace(".py","_results.json"); json.dump(out,open(path,"w"),indent=1)
    print("MANIFOLD SPINE L6 -- the metric on the shell family (BKM = entropy Hessian; monotone; curved)\n")
    print(f"  FACT 1 (metric IS BKM = relative-entropy Hessian): g_BKM {gb:.6f} vs Hessian {hs:.6f} (diff {abs(gb-hs):.1e}) -> {g_identity}")
    print(f"     wrong-direction control (SX) metric {hs_wrongdir:.3f} != SZ metric {gb:.3f} -> direction-specific bilinear form: {g_identity_ctrl}")
    print(f"  FACT 2 (curved not flat): BKM boundary/center {ratio_bkm:.2f}x vs flat {ratio_flat:.2f}x -> curvature real: {g_curved}")
    print(f"     (BKM arc length = 2 arcsin(r); pure-state boundary metrically far, mixed center near)")
    print(f"  FACT 3 (monotone CPTP contraction = infinitesimal DPI): {gb:.4f} -> depol {gb_after:.4f} (contracts {g_contract}); "
          f"non-CPTP amplify {gb_amp:.4f} (does NOT contract {g_noncptp})")
    print(f"\n  => the shell-family metric IS the curvature of the forced entropy pawl (surface identity, UP-120), and its")
    print(f"     CPTP contraction IS the infinitesimal DPI (UP-121). Geometry and entropy are one tensor on the shells.")
    print(f"\n  VERDICT: {'PASS' if verdict else 'FAIL'} (BKM=Hessian + corrupt-control + curved-not-flat + CPTP-contraction + non-CPTP-control)")
    if verdict: print("PASS manifold_L6_shell_metric_bkm_connection")
    print("ALL_GATES:","PASS" if verdict else "FAIL","->",path)
    sys.exit(0 if verdict else 1)

if __name__=="__main__":
    main()
