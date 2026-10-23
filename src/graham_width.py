"""
Correct constructive proof of the WIDTH SUFFICIENT CONDITION (PROVED HERE).

Theorem. Let p be prime and A subset F_p\\{0}. Lift to centered reps A' in
(-(p-1)/2,(p-1)/2). Let P={a' in A': a'>0}, N={-a' : a' in A', a'<0}.
If sum(P) < p, sum(N) < p, and sum(P) != sum(N), then A is sequenceable mod p.

Proof. Build orderings of P and N whose prefix sums avoid each other (except 0)
by always removing an element from the side with strictly larger total.  This
maintains the invariant PrefixSums(P_order) ∩ PrefixSums(N_order) = {0}.
Outputting reverse(P_order) followed by -N_order gives distinct integer partial
sums lying in an interval of width < p (since sumP,p and sumN<p and sumP!=sumN),
hence they are distinct mod p.
"""

from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

import itertools


def build_orderings(P: List[int], N: List[int]) -> Tuple[List[int], List[int]]:
    """Return orderings of P and N (positive ints) with
    PrefixSums(P_order) ∩ PrefixSums(N_order) = {0}.  Requires sum(P) != sum(N)."""
    sP, sN = sum(P), sum(N)
    assert sP != sN, "need unequal totals"
    # Base: one side empty.
    if not P:
        return [], list(N)
    if not N:
        return list(P), []

    if sP > sN:
        # P is the strictly larger side.  If P=[p] then p=sP>sN>=every N-prefix,
        # so p is not an N-prefix and the invariant holds trivially.
        if len(P) == 1:
            return list(P), list(N)
        # Remove p* from P with sum(P\\{p*}) != sN, i.e. p* != sP - sN.
        forbidden = sP - sN
        pstar = None
        for x in P:
            if x != forbidden:
                pstar = x
                break
        assert pstar is not None, "|P|>=2 guarantees a choice != forbidden"
        Pprime = [x for x in P if x != pstar]
        # sum(Pprime) = sP - pstar != sN by choice, so recursion precondition holds.
        Pord, Nord = build_orderings(Pprime, N)
        # Invariant: sP > sN >= every N-prefix, so sP not an N-prefix.
        return Pord + [pstar], Nord
    else:
        # N is the strictly larger side.  If N=[s] then s=sN>sP>=every P-prefix,
        # so s is not a P-prefix and the invariant holds trivially.
        if len(N) == 1:
            return list(P), list(N)
        # Remove n* from N with sum(N\\{n*}) != sP, i.e. n* != sN - sP.
        forbidden = sN - sP
        nstar = None
        for x in N:
            if x != forbidden:
                nstar = x
                break
        assert nstar is not None, "|N|>=2 guarantees a choice != forbidden"
        Nprime = [x for x in N if x != nstar]
        # sum(Nprime) = sN - nstar != sP by choice, so recursion precondition holds.
        Pord, Nord = build_orderings(P, Nprime)
        # Invariant: sN > sP >= every P-prefix, so sN not a P-prefix.
        return Pord, Nord + [nstar]


def valid_ordering_width(A: Sequence[int], p: int) -> List[int]:
    """Centered reps of A mod p; requires width condition."""
    reps = [((int(a) % p) - p if (int(a) % p) > p // 2 else (int(a) % p)) for a in A]
    assert all(r != 0 for r in reps), "no zero residues"
    P = sorted([r for r in reps if r > 0])
    N = sorted([-r for r in reps if r < 0])
    sP, sN = sum(P), sum(N)
    assert sP < p and sN < p, "width condition"

    if sP == sN:
        if not P:
            return []
        pstar = P[0]
        Pprime = P[1:]
        Pord, Nord = build_orderings(Pprime, N)
        Pord.append(pstar)
    else:
        Pord, Nord = build_orderings(P, N)

    return list(reversed(Pord)) + [-n for n in Nord]


def partial_sums(ordering: Sequence[int]) -> List[int]:
    out, s = [], 0
    for x in ordering:
        s += x
        out.append(s)
    return out


def is_valid_integers(ordering: Sequence[int]) -> bool:
    sums = partial_sums(ordering)
    return len(sums) == len(set(sums))


def range_width(ordering: Sequence[int]) -> int:
    sums = partial_sums(ordering)
    return max(sums) - min(sums) if sums else 0


def is_valid_mod_p(ordering: Sequence[int], p: int) -> bool:
    seen, s = set(), 0
    for x in ordering:
        s = (s + x) % p
        if s in seen:
            return False
        seen.add(s)
    return True
