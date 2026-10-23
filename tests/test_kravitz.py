import sys
sys.path.insert(0, "src")

import random
from itertools import combinations
from kravitz import valid_ordering_kravitz, is_valid_integers, partial_sums, range_width

def test_kravitz_random():
    random.seed(2)
    for _ in range(500):
        n = random.randint(1, 10)
        A = random.sample(range(-25, 26), n)
        A = [x for x in A if x != 0]
        if not A:
            continue
        ordering = valid_ordering_kravitz(A)
        assert is_valid_integers(ordering), f"KRAVITZ FAIL: {A} {ordering} {partial_sums(ordering)}"

def test_modp_width_corollary():
    for p in [7, 11, 13, 17]:
        elems = list(range(1, p))
        for r in range(1, min(7, p - 1) + 1):
            for subset in combinations(elems, r):
                reps = [((a % p) - p if (a % p) > p // 2 else (a % p)) for a in subset]
                P = [x for x in reps if x > 0]
                N = [-x for x in reps if x < 0]
                if sum(P) < p and sum(N) < p:
                    ordering = valid_ordering_kravitz(reps)
                    assert is_valid_integers(ordering), f"Not valid integers: {p} {subset} {ordering}"
                    w = range_width(ordering)
                    assert w < p, f"Width not less than p: w={w}, p={p}"
                    sums_mod = [s % p for s in partial_sums(ordering)]
                    assert len(sums_mod) == len(set(sums_mod)), f"Not valid mod p: {sums_mod}"
