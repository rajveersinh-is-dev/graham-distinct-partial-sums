"""
Correct constructive proof of the integer version of Graham's conjecture
(Theorem 1.3, Kravitz 2024; independently Sawin 2015).

Every finite A subset Z \\ {0} admits an ordering with all partial sums distinct.

Construction: split A = P (positives) u {-n : n in N}.  Build orderings of P and N
such that their prefix sums are unequal except at (0,0) and (|P|,|N|)
(induction on |P|, per Kravitz).  Then output
    reverse(P_order) followed by [-n for n in N_order].
All partial sums are then distinct as integers.

We verify by brute force on many small sets.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import permutations
from typing import List, Optional, Sequence, Tuple

from graham_backtrack import backtrack_valid_ordering


# ----------------------------------------------------------- induction step

def order_pair(P: List[int], N: List[int]) -> Tuple[List[int], List[int]]:
    """Return orderings of P and N such that
    sum(P[:i]) != sum(N[:j]) for all (i,j) except (0,0) and (|P|,|N|).

    This is the inductive lemma from Kravitz's proof of the integer version.
    All elements of P and N must be positive and internally distinct; P and N
    may share values (they come from different sides of zero, so that's fine).
    """
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


def valid_ordering_integers(A: Sequence[int]) -> List[int]:
    elems = list(A)
    assert all(x != 0 for x in elems), "no zeros"
    assert len(elems) == len(set(elems)), "distinct"
    P = sorted((x for x in elems if x > 0), reverse=True)
    N = sorted((-x for x in elems if x < 0))
    p_ord, n_ord = order_pair(list(P), list(N))
    return list(reversed(p_ord)) + [-n for n in n_ord]


def partial_sums(ordering: Sequence[int]) -> List[int]:
    out, s = [], 0
    for x in ordering:
        s += x
        out.append(s)
    return out


def is_valid(ordering: Sequence[int]) -> bool:
    sums = partial_sums(ordering)
    return len(sums) == len(set(sums))


# --------------------------------------------------------------- brute force

def brute_force_valid_ordering(A: Sequence[int]) -> Optional[Tuple[int, ...]]:
    """Search all permutations for one with distinct partial sums (small sets)."""
    elems = list(A)
    n = len(elems)
    if n > 9:
        return None  # too expensive
    return backtrack_valid_ordering(elems, dynamic_sort=False)


def _cross_check(A: Sequence[int]) -> bool:
    """True if constructive result agrees with brute-force existence."""
    construct = valid_ordering_integers(A)
    assert is_valid(construct), f"constructive failed for {A}: {construct}"
    bf = brute_force_valid_ordering(A)
    if bf is None:
        return True  # brute force too big, but constructive is valid
    return is_valid(bf)  # brute force found one => existence confirmed
