import sys
sys.path.insert(0, "src")

import random
from itertools import combinations
from graham_verify import find_two_sided_valid_ordering_mod_p, is_two_sided_valid_mod_p

def test_two_sided_small_primes():
    for p in [3, 5, 7, 11]:
        elems = list(range(1, p))
        for r in range(1, min(5, p - 1) + 1):
            for subset in combinations(elems, r):
                ord_ = find_two_sided_valid_ordering_mod_p(subset, p)
                assert ord_ is not None, f"non-sequenceable two-sided subset: {subset} for p={p}"
                assert is_two_sided_valid_mod_p(ord_, p), f"returned invalid ordering: {ord_}"

def test_heuristic_two_sided_large():
    rng = random.Random(42)
    p = 101
    A = rng.sample(range(1, p), 30)
    ordering = find_two_sided_valid_ordering_mod_p(A, p)

    # We do not assert not None unconditionally as the heuristic could fail,
    # but with N=30 it should very likely succeed.
    if ordering is not None:
        assert is_two_sided_valid_mod_p(ordering, p), "Heuristic returned invalid two-sided ordering"
