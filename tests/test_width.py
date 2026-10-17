# Tests for Graham width construction

import sys
sys.path.insert(0, "src")

from graham_width import (
    valid_ordering_width,
    partial_sums,
    is_valid_mod_p,
    is_valid_integers,
    range_width,
    build_orderings,
)

from itertools import combinations


def centered_rep(a, p):
    r = a % p
    return r - p if r > p // 2 else r


def test_build_orderings_invariant():
    """Lemma 1: prefix sums of P_order and N_order share only 0."""
    import random
    random.seed(4)
    for _ in range(2000):
        P = random.sample(range(1, 30), random.randint(1, 8))
        N = random.sample(range(1, 30), random.randint(1, 8))
        if sum(P) == sum(N):
            continue
        Pord, Nord = build_orderings(P, N)
        prefP = {0}
        s = 0
        for x in Pord:
            s += x
            prefP.add(s)
        prefN = {0}
        s = 0
        for x in Nord:
            s += x
            prefN.add(s)
        inter = prefP & prefN
        assert inter == {0}, (P, N, Pord, Nord, inter)


def test_width_construction_modp_exhaustive():
    """Exhaustive: every width-satisfying subset for small p is sequenceable mod p via construction."""
    for p in [5, 7, 11, 13, 17, 19]:
        elems = list(range(1, p))
        count = 0
        for r in range(1, min(7, p - 1) + 1):
            for subset in combinations(elems, r):
                reps = [centered_rep(a, p) for a in subset]
                P = [x for x in reps if x > 0]
                N = [-x for x in reps if x < 0]
                if sum(P) < p and sum(N) < p and sum(P) != sum(N):
                    ordering = valid_ordering_width(subset, p)
                    assert is_valid_mod_p(ordering, p), (p, subset, ordering)
                    count += 1
    assert count > 0


def test_corollary_consecutive():
    """A={1,...,k}, k(k+1)/2 < p => sequenceable."""
    for p in [7, 11, 13, 17, 19, 23]:
        k = 1
        while k * (k + 1) // 2 < p:
            A = list(range(1, k + 1))
            ordering = valid_ordering_width(A, p)
            assert is_valid_mod_p(ordering, p), (p, k, ordering)
            k += 1


def test_integer_version_backtracking_ground_truth():
    """Ground truth: every small nonzero integer set has a valid ordering (backtracking)."""
    def bt(A):
        elems = tuple(sorted(set(A), key=lambda x: -abs(x)))
        elems = tuple(x for x in elems if x != 0)
        n = len(elems)
        if n == 0:
            return True
        used = [False] * n
        seen = set()
        cur = 0
        def rec(k):
            nonlocal cur
            if k == n:
                return True
            for i in range(n):
                if used[i]:
                    continue
                nxt = cur + elems[i]
                if nxt in seen:
                    continue
                used[i] = True
                seen.add(nxt)
                old = cur
                cur = nxt
                if rec(k + 1):
                    return True
                cur = old
                seen.discard(nxt)
                used[i] = False
            return False
        return rec(0)

    import random
    random.seed(5)
    for _ in range(3000):
        A = random.sample(range(-14, 15), random.randint(1, 9))
        A = [x for x in A if x != 0]
        assert bt(A), A  # ground truth: always sequenceable


if __name__ == "__main__":
    test_build_orderings_invariant()
    test_width_construction_modp_exhaustive()
    test_corollary_consecutive()
    test_integer_version_backtracking_ground_truth()
    print("All tests passed.")
