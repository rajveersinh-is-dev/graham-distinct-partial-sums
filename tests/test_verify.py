import sys

sys.path.insert(0, "src")

import random
from itertools import combinations
from graham_verify import (
    find_valid_ordering_integers,
    find_valid_ordering_mod_p,
    width_condition_holds,
)

try:
    from hypothesis import given, settings, strategies as st
except ImportError:
    st = None  # type: ignore


if st is not None:

    @settings(max_examples=100, deadline=None)
    @given(st.sampled_from([5, 7, 11, 13, 17, 19, 23]), st.data())
    def test_find_valid_ordering_mod_p_hypothesis(p, data):
        elems = list(range(1, p))
        subset = data.draw(
            st.lists(st.sampled_from(elems), min_size=1, max_size=14, unique=True)
        )
        assert find_valid_ordering_mod_p(subset, p) is not None


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
                ord_ = find_valid_ordering_mod_p(subset, p)
                assert ord_ is not None, f"non-sequenceable subset: {subset} for p={p}"


def test_width_condition_vs_brute_force():
    for p in [7, 11, 13]:
        elems = list(range(1, p))
        for r in range(1, min(5, p - 1) + 1):
            for subset in combinations(elems, r):
                w = width_condition_holds(subset, p)
                bf = find_valid_ordering_mod_p(subset, p) is not None
                if w:
                    assert bf, f"WIDTH OK but brute FAIL: {subset} p={p}"


def test_heuristic_mod_p_large():
    # Test heuristic on a larger set where N > 25
    rng = random.Random(42)
    p = 101
    A = rng.sample(range(1, p), 40)
    ordering = find_valid_ordering_mod_p(A, p)
    assert ordering is not None, "Heuristic failed to find an ordering for N=40"

    # Verify validity of the ordering mod p
    seen = set()
    cur = 0
    for x in ordering:
        cur = (cur + x) % p
        assert cur not in seen, f"Duplicate prefix sum {cur} mod {p}"
        seen.add(cur)
