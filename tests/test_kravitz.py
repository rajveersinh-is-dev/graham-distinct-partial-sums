import sys

sys.path.insert(0, "src")

import random
from itertools import combinations
from kravitz import valid_ordering_kravitz, is_valid_integers, partial_sums, range_width


def test_kravitz_random():
    random.seed(2)
    for _ in range(500):
        n = random.randint(1, 40)
        A = random.sample(range(-100, 101), n)
        A = [x for x in A if x != 0]
        if not A:
            continue
        ordering = valid_ordering_kravitz(A)
        assert is_valid_integers(
            ordering
        ), f"KRAVITZ FAIL: {A} {ordering} {partial_sums(ordering)}"


def test_kravitz_large_stress():
    """
    Formally evaluate the performance of valid_ordering_kravitz for sizes nearing N = 1000 and 3000.
    Ensures that the algorithm scales well without recursion limit violations (since it's iterative).
    """
    random.seed(42)
    for n_size in [1000, 3000]:
        # Generate large inputs
        A = random.sample(range(-5000, 5000), n_size)
        A = [x for x in A if x != 0]

        # Valid ordering should complete efficiently without RecursionError
        try:
            ordering = valid_ordering_kravitz(A)
        except RecursionError:
            assert False, f"Recursion limit hit for N={n_size}"

        assert len(ordering) == len(A), "Ordering length mismatch"


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
                    assert is_valid_integers(
                        ordering
                    ), f"Not valid integers: {p} {subset} {ordering}"
                    w = range_width(ordering)
                    assert w < p, f"Width not less than p: w={w}, p={p}"
                    sums_mod = [s % p for s in partial_sums(ordering)]
                    assert len(sums_mod) == len(
                        set(sums_mod)
                    ), f"Not valid mod p: {sums_mod}"
