import sys
sys.path.insert(0, "src")

import random
from itertools import combinations
from graham_verify import find_valid_ordering_integers, brute_force_mod_p, width_condition_holds


def test_integer_version_random():
    random.seed(1)
    tested = 0
    fails = 0
    for _ in range(400):
        n = random.randint(1, 9)
        A = random.sample(range(-20, 21), n)
        A = [x for x in A if x != 0]
        if not A:
            continue
        tested += 1
        ord_ = find_valid_ordering_integers(A)
        assert ord_ is not None, f"NO ORDERING FOUND (theorem says impossible): {A}"

def test_mod_p_small_primes():
    for p in [3, 5, 7, 11, 13]:
        elems = list(range(1, p))
        for r in range(1, min(6, p - 1) + 1):
            for subset in combinations(elems, r):
                ord_ = brute_force_mod_p(subset, p)
                assert ord_ is not None, f"non-sequenceable subset: {subset} for p={p}"

def test_width_condition_vs_brute_force():
    for p in [7, 11, 13]:
        elems = list(range(1, p))
        for r in range(1, min(5, p - 1) + 1):
            for subset in combinations(elems, r):
                w = width_condition_holds(subset, p)
                bf = brute_force_mod_p(subset, p) is not None
                if w:
                    assert bf, f"WIDTH OK but brute FAIL: {subset} p={p}"
