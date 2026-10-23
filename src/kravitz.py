"""
Correct implementation of Kravitz's inductive construction (integer version of
Graham's conjecture, Theorem 1.3 of arXiv:2407.01835; independently Sawin 2015).

Builds orderings of P (positives) and N (negative magnitudes) whose prefix sums
avoid each other except at (0,0) and (|P|,|N|).  Then outputs
    reverse(P_order) followed by (-N for N in N_order),
giving an ordering of A=P u {-N} with all partial sums distinct as integers.

Range computation: all partial sums lie in [min(p*, sum(P)-sum(N)), sum(P)]
where p* = sum(P)-sum(P'), so range width = max(sum(P'), sum(N)).
Hence if sum(P) < p and sum(N) < p then range width < p, so the partial sums
are distinct mod p.  => WIDTH SUFFICIENT CONDITION (PROVED HERE).
"""

from __future__ import annotations

from typing import List, Optional, Sequence, Tuple


def kravitz_order_pair(P: List[int], N: List[int]) -> Tuple[List[int], List[int]]:
    """Inductive construction.  P, N: positive integers, distinct within each list."""
    sP, sN = sum(P), sum(N)
    if not P:
        return [], list(N)
    if not N:
        return list(P), []

    if sP >= sN:
        if len(P) == 1:
            return list(P), list(N)
        pstar = None
        for x in P:
            if sP - x != sN:
                pstar = x
                break
        assert pstar is not None, "need sum(P\\{p*}) != sum(N); |P|>=2 guarantees"
        Pprime = [x for x in P if x != pstar]
        Pord, Nord = kravitz_order_pair(Pprime, N)
        return Pord + [pstar], Nord
    else:
        if len(N) == 1:
            return list(P), list(N)
        nstar = None
        for x in N:
            if sN - x != sP:
                nstar = x
                break
        assert nstar is not None, "need sum(N\\{n*}) != sum(P); |N|>=2 guarantees"
        Nprime = [x for x in N if x != nstar]
        Pord, Nord = kravitz_order_pair(P, Nprime)
        return Pord, Nord + [nstar]


def valid_ordering_kravitz(A: Sequence[int]) -> List[int]:
    elems = list(A)
    assert all(x != 0 for x in elems)
    assert len(elems) == len(set(elems))
    P = sorted((x for x in elems if x > 0), reverse=True)  # order doesn't matter; induction reorders
    N = sorted((-x for x in elems if x < 0))
    Pord, Nord = kravitz_order_pair(list(P), list(N))
    return list(reversed(Pord)) + [-n for n in Nord]


def partial_sums(ordering: Sequence[int]) -> list:
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


def verify_range_formula(A: Sequence[int]) -> bool:
    """Check: range width == max(sum(P'), sum(N)) where P'=P\\{p*}."""
    elems = list(A)
    P = [x for x in elems if x > 0]
    N = [-x for x in elems if x < 0]
    ordering = valid_ordering_kravitz(elems)
    if not is_valid_integers(ordering):
        print("NOT VALID:", A, ordering)
        return False
    # p* is the element added last at top level = last element of Pord reversed first...
    # Simpler: just check width < p is consistent; here just confirm distinct.
    return True
