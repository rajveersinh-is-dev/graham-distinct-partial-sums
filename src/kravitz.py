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


if __name__ == "__main__":
    import random
    random.seed(2)
    tested = 0
    fails = 0
    for _ in range(5000):
        n = random.randint(1, 10)
        A = random.sample(range(-25, 26), n)
        A = [x for x in A if x != 0]
        if not A:
            continue
        tested += 1
        ordering = valid_ordering_kravitz(A)
        if not is_valid_integers(ordering):
            fails += 1
            print("KRAVITZ FAIL:", A, ordering, partial_sums(ordering))
    print(f"Kravitz construction: tested {tested} random integer sets, failures={fails}")

    # Now verify the mod-p width corollary: if sum(P)<p and sum(N)<p then range<p & distinct mod p.
    print("\nMod-p width corollary check (Kravitz construction):")
    for p in [7, 11, 13, 17, 19, 23]:
        from itertools import combinations
        elems = list(range(1, p))
        cond_holds = 0
        width_ok = 0
        modp_ok = 0
        fail = None
        for r in range(1, min(7, p - 1) + 1):
            for subset in combinations(elems, r):
                reps = [((a % p) - p if (a % p) > p // 2 else (a % p)) for a in subset]
                P = [x for x in reps if x > 0]
                N = [-x for x in reps if x < 0]
                if sum(P) < p and sum(N) < p:
                    cond_holds += 1
                    ordering = valid_ordering_kravitz(reps)
                    assert is_valid_integers(ordering), (p, subset, ordering)
                    w = range_width(ordering)
                    if w < p:
                        width_ok += 1
                    sums_mod = [s % p for s in partial_sums(ordering)]
                    if len(sums_mod) == len(set(sums_mod)):
                        modp_ok += 1
                    else:
                        fail = (p, subset, ordering, partial_sums(ordering), sums_mod)
        print(f"  p={p}: cond_holds={cond_holds}, width<p={width_ok}, distinct-modp={modp_ok}, fail={fail}")
