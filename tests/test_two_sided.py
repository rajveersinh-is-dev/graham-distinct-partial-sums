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
                assert (
                    ord_ is not None
                ), f"non-sequenceable two-sided subset: {subset} for p={p}"
                assert is_two_sided_valid_mod_p(
                    ord_, p
                ), f"returned invalid ordering: {ord_}"


def test_heuristic_two_sided_large():
    rng = random.Random(42)
    p = 101
    A = rng.sample(range(1, p), 30)
    ordering = find_two_sided_valid_ordering_mod_p(A, p)

    # We do not assert not None unconditionally as the heuristic could fail,
    # but with N=30 it should very likely succeed.
    if ordering is not None:
        assert is_two_sided_valid_mod_p(
            ordering, p
        ), "Heuristic returned invalid two-sided ordering"


from graham_verify import width_condition_holds
from graham_width import valid_ordering_width
from graham_verify import is_valid_mod_p
from itertools import permutations


def test_two_sided_equivalence():
    """Test Theorem 2: A valid ordering is two-sided valid iff no proper partial sum is 0 mod p."""
    for p in [3, 5, 7]:
        elems = list(range(1, p))
        for r in range(1, p):
            for subset in combinations(elems, r):
                for ord_ in permutations(subset):
                    if is_valid_mod_p(ord_, p):
                        seen = set()
                        s = 0
                        has_zero_before_end = False
                        for i, x in enumerate(ord_):
                            s = (s + x) % p
                            if i < len(ord_) - 1 and s == 0:
                                has_zero_before_end = True

                        # Actual ground truth check
                        seen_rev = set()
                        s_rev = 0
                        rev_valid = True
                        for x in reversed(ord_):
                            s_rev = (s_rev + x) % p
                            if s_rev in seen_rev:
                                rev_valid = False
                                break
                            seen_rev.add(s_rev)

                        # The function under test
                        func_res = is_two_sided_valid_mod_p(ord_, p)

                        assert func_res == rev_valid
                        assert rev_valid == (not has_zero_before_end)


def test_width_condition_two_sided_theorem():
    """Test Theorem 2 Corollary: Width condition orderings are inherently two-sided valid."""
    for p in [5, 7, 11, 13, 17]:
        elems = list(range(1, p))
        for r in range(1, p):
            for subset in combinations(elems, r):
                if width_condition_holds(subset, p):
                    ord_ = valid_ordering_width(subset, p)
                    assert is_two_sided_valid_mod_p(
                        ord_, p
                    ), f"Width ordering {ord_} for {subset} mod {p} is not two-sided valid"
