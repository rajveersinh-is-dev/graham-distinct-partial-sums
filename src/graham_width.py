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

from typing import List, Sequence, Tuple

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
    """Centered reps of A mod p; requires width + unequal condition."""
    reps = [((int(a) % p) - p if (int(a) % p) > p // 2 else (int(a) % p)) for a in A]
    assert all(r != 0 for r in reps), "no zero residues"
    P = sorted([r for r in reps if r > 0])
    N = sorted([-r for r in reps if r < 0])
    sP, sN = sum(P), sum(N)
    assert sP < p and sN < p, "width condition"
    assert sP != sN, "unequal totals"
    Pord, Nord = build_orderings(P, N)
    return list(reversed(Pord)) + [-n for n in Nord]


def partial_sums(ordering: Sequence[int]) -> List[int]:
    """Partial sums.
    
    Args:
        ordering:
    
    Returns:
        The computed result
    
    """
    out, s = [], 0
    for x in ordering:
        s += x
        out.append(s)
    return out


def is_valid_integers(ordering: Sequence[int]) -> bool:
    """Is valid integers.
    
    Args:
        ordering:
    
    Returns:
        The computed result
    
    """
    sums = partial_sums(ordering)
    return len(sums) == len(set(sums))


def range_width(ordering: Sequence[int]) -> int:
    """Range width.
    
    Args:
        ordering:
    
    Returns:
        The computed result
    
    """
    sums = partial_sums(ordering)
    return max(sums) - min(sums) if sums else 0


def is_valid_mod_p(ordering: Sequence[int], p: int) -> bool:
    """Is valid mod p.
    
    Args:
        ordering:
        p:
    
    Returns:
        bool: Result of type bool
    
    """
    seen, s = set(), 0
    for x in ordering:
        s = (s + x) % p
        if s in seen:
            return False
        seen.add(s)
    return True


if __name__ == "__main__":
    import random
    from itertools import combinations

    random.seed(3)

    # Test the construction on integer sets (all nonzero): map via a large p
    # so width condition holds trivially (sumP<p, sumN<p) and unequal.
    print("=== Width construction on random integer sets (p large) ===")
    tested = 0
    fails = 0
    for _ in range(6000):
        n = random.randint(1, 9)
        A = random.sample(range(-14, 15), n)
        A = [x for x in A if x != 0]
        if not A:
            continue
        p = 101  # large enough that width holds
        try:
            ordering = valid_ordering_width(A, p)
        except AssertionError as e:
            # unequal-totals failure: skip (separate case)
            continue
        tested += 1
        sums = partial_sums(ordering)
        if not is_valid_integers(ordering) or range_width(ordering) >= p:
            fails += 1
            print("FAIL:", A, ordering, sums, "range", range_width(ordering))
    print(f"tested {tested} (unequal-totals) sets, failures={fails}")

    # Test mod-p width corollary exhaustively for small p (unequal case).
    print("\n=== Mod-p width corollary, exhaustive small p (unequal totals) ===")
    for p in [5, 7, 11, 13, 17, 19, 23]:
        elems = list(range(1, p))
        cond = 0
        ok = 0
        for r in range(1, min(7, p - 1) + 1):
            for subset in combinations(elems, r):
                reps = [((a % p) - p if (a % p) > p // 2 else (a % p)) for a in subset]
                P = [x for x in reps if x > 0]
                N = [-x for x in reps if x < 0]
                sP, sN = sum(P), sum(N)
                if sP < p and sN < p and sP != sN:
                    cond += 1
                    ordering = valid_ordering_width(subset, p)
                    assert is_valid_mod_p(ordering, p), (p, subset, ordering)
                    ok += 1
        print(f"  p={p}: width&unequal sets={cond}, all distinct-mod-p={ok}")

    # Cross-check against brute force: width&unequal => sequenceable (already implied)
    print("\n=== Cross-check width&unequal vs brute force ===")
    for p in [7, 11, 13]:
        elems = list(range(1, p))
        agree = 0
        for r in range(1, min(6, p - 1) + 1):
            for subset in combinations(elems, r):
                reps = [((a % p) - p if (a % p) > p // 2 else (a % p)) for a in subset]
                P = [x for x in reps if x > 0]
                N = [-x for x in reps if x < 0]
                sP, sN = sum(P), sum(N)
                if sP < p and sN < p and sP != sN:
                    # brute force existence
                    import itertools
                    bf = None
                    for perm in itertools.permutations(reps):
                        seen, ss = set(), 0
                        good = True
                        for x in perm:
                            ss = (ss + x) % p
                            if ss in seen:
                                good = False
                                break
                            seen.add(ss)
                        if good:
                            bf = True
                            break
                    construct_ok = is_valid_mod_p(valid_ordering_width(subset, p), p)
                    assert construct_ok == bf, (p, subset, construct_ok, bf)
                    agree += 1
        print(f"  p={p}: width&unequal sets cross-checked={agree}")
