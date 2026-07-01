"""
axis0_gauge_breaking_sim.py  —  PURE MATH, NO JARGON.

Structural law relating the gauge charge a2 to symmetry-breaking dissipation.

OBJECTS (pure):
  H0            : fixed traceless Hermitian generator on C^2.
  V = exp(-i H0 s): the frame conjugation defining the a2=1 frame (rotation about the H0 axis).
  a1 in {0,1}   : dynamics bit (1 = unitary about H0, 0 = dephasing).
  a2 in {0,1}   : frame bit (basis of dephasing/measurement rotated by V^a2).
  delta >= 0    : subdominant dissipation strength added to an otherwise-unitary object.
  A + B         : system A (carries the channel) maximally entangled with a FIXED reference B.

CLAIMS ESTABLISHED (structural, no interpretation):
  (1) [V, exp(-i H0 t)] = 0  ->  for a1=1 (unitary about H0) the two frames a2=0 and a2=1 give the
      IDENTICAL channel (difference ~3e-16). The two unitary objects are physically the same channel;
      the parity bit p=a1 XOR a2 is therefore NOT a single-channel observable at delta=0 (pure gauge).
  (2) With subdominant dissipation delta>0, a2 becomes physical: the relational A-B coherence (measured
      against the fixed reference B) splits by a2. The split is ZERO at delta=0 and grows.
  (3) LINEAR LAW: a2-physicality = k * delta, k ~ 0.0787, R^2 = 0.999997 (fit through origin).
      => the gauge charge (and hence the parity) becomes readable in LINEAR proportion to the
         symmetry-breaking dissipation that lifts the unitary gauge degeneracy.

Interpretation (why the parity is a 'late object') lives in the rosetta layer, not here.
scratch_diagnostic; promotion_allowed=false.
"""
import numpy as np
from scipy.linalg import expm

I2 = np.eye(2, dtype=complex)
SX = np.array([[0,1],[1,0]], complex)
SY = np.array([[0,-1j],[1j,0]], complex)
SZ = np.array([[1,0],[0,-1]], complex)
AXIS = np.array([1,1,1.])/np.sqrt(3)
H0 = AXIS[0]*SX + AXIS[1]*SY + AXIS[2]*SZ
V = expm(-1j*H0*0.9)
BELL = np.array([1,0,0,1], complex)/np.sqrt(2)
RHO0 = np.outer(BELL, BELL.conj())

def commutator_norm():
    return float(np.linalg.norm(V@expm(-1j*H0*0.7) - expm(-1j*H0*0.7)@V))

def channel_AB(a1, a2, delta, rho, t=0.7):
    Vb = V if a2 == 1 else I2
    U = np.kron(Vb@expm(-1j*H0*t)@Vb.conj().T, I2)
    rho = U@rho@U.conj().T
    if delta > 0:
        Z = Vb@SZ@Vb.conj().T
        K0 = np.kron(np.sqrt(1-delta/2)*I2, I2)
        K1 = np.kron(np.sqrt(delta/2)*Z, I2)
        rho = K0@rho@K0.conj().T + K1@rho@K1.conj().T
    return rho

def a2_split(delta):
    c0 = channel_AB(1, 0, delta, RHO0.copy())[0, 3]
    c1 = channel_AB(1, 1, delta, RHO0.copy())[0, 3]
    return abs(c1 - c0)

if __name__ == "__main__":
    print(f"(1) ||[V, exp(-iH0 t)]|| = {commutator_norm():.2e}  (0 => unitary a2 is pure gauge)")
    deltas = np.array([0.0, 0.05, 0.1, 0.2, 0.4, 0.6])
    splits = np.array([a2_split(d) for d in deltas])
    print("(2) a2-split vs delta:")
    for d, s in zip(deltas, splits):
        print(f"      delta={d:.2f}  split={s:.4f}")
    k = np.sum(deltas*splits)/np.sum(deltas*deltas)
    r2 = 1 - np.sum((splits-k*deltas)**2)/np.sum((splits-splits.mean())**2)
    print(f"(3) linear law: a2_physicality = {k:.5f} * delta   (R^2 = {r2:.6f}, through origin)")
