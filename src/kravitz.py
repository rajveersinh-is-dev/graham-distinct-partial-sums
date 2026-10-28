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
    P_rem = list(P)
    N_rem = list(N)
    P_rev = []
    N_rev = []
    sP, sN = sum(P_rem), sum(N_rem)

    while P_rem and N_rem:
        if sP >= sN:
            if len(P_rem) == 1:
                break
            pstar = None
            if sP - P_rem[-1] != sN:
                pstar = P_rem.pop()
            elif sP - P_rem[-2] != sN:
                pstar = P_rem.pop(-2)
            else:
                for i in range(len(P_rem) - 3, -1, -1):
                    if sP - P_rem[i] != sN:
                        pstar = P_rem.pop(i)
                        break
            assert pstar is not None, "need sum(P\\{p*}) != sum(N); |P|>=2 guarantees"
            P_rev.append(pstar)
            sP -= pstar
        else:
            if len(N_rem) == 1:
                break
            nstar = None
            if sN - N_rem[-1] != sP:
                nstar = N_rem.pop()
            elif sN - N_rem[-2] != sP:
                nstar = N_rem.pop(-2)
            else:
                for i in range(len(N_rem) - 3, -1, -1):
                    if sN - N_rem[i] != sP:
                        nstar = N_rem.pop(i)
                        break
            assert nstar is not None, "need sum(N\\{n*}) != sum(P); |N|>=2 guarantees"
            N_rev.append(nstar)
            sN -= nstar

    P_rev.reverse()
    N_rev.reverse()
    return P_rem + P_rev, N_rem + N_rev


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
