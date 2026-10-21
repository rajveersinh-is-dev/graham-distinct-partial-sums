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


# ----------------------------------------------------------- induction step

def order_pair(P: List[int], N: List[int]) -> Tuple[List[int], List[int]]:
    """Return orderings of P and N such that
    sum(P[:i]) != sum(N[:j]) for all (i,j) except (0,0) and (|P|,|N|).

    This is the inductive lemma from Kravitz's proof of the integer version.
    All elements of P and N must be positive and internally distinct; P and N
    may share values (they come from different sides of zero, so that's fine).
    """
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
        p_ord, n_ord = order_pair(Pprime, N)
        return p_ord + [pstar], n_ord
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
        p_ord, n_ord = order_pair(P, Nprime)
        return p_ord, n_ord + [nstar]


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
    for perm in permutations(elems):
        if is_valid(perm):
            return perm
    return None


def _cross_check(A: Sequence[int]) -> bool:
    """True if constructive result agrees with brute-force existence."""
    construct = valid_ordering_integers(A)
    assert is_valid(construct), f"constructive failed for {A}: {construct}"
    bf = brute_force_valid_ordering(A)
    if bf is None:
        return True  # brute force too big, but constructive is valid
    return is_valid(bf)  # brute force found one => existence confirmed


if __name__ == "__main__":
    import random

    random.seed(0)
    tested = 0
    failures = 0
    for _ in range(3000):
        n = random.randint(1, 8)
        A = random.sample(range(-12, 13), n)
        A = [x for x in A if x != 0]
        if not A:
            continue
        tested += 1
        ordering = valid_ordering_integers(A)
        sums = partial_sums(ordering)
        ok = is_valid(ordering)
        bf_ok = brute_force_valid_ordering(A) is not None
        if not ok or not bf_ok:
            failures += 1
            print("FAIL", A, ordering, sums, ok, bf_ok)
    print(f"tested {tested} random integer sets, failures={failures}")
    # also some structured sets
    for A in ([1,2,3], [-5,-2,1,3,7], list(range(1,11)), list(range(-5,6))):
        if 0 in A:
            continue
        ordering = valid_ordering_integers(A)
        print(A, "->", ordering, "sums:", partial_sums(ordering), "valid:", is_valid(ordering))
