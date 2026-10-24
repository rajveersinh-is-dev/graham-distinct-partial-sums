import sys
sys.path.insert(0, "src")

import random
from graham_integer import valid_ordering_integers, partial_sums, is_valid, brute_force_valid_ordering


def test_graham_integer_random():
    random.seed(0)
    for _ in range(300):
        n = random.randint(1, 8)
        A = random.sample(range(-12, 13), n)
        A = [x for x in A if x != 0]
        if not A:
            continue
        ordering = valid_ordering_integers(A)
        ok = is_valid(ordering)
        bf_ok = brute_force_valid_ordering(A) is not None
        assert ok and bf_ok, f"FAIL {A} {ordering} {partial_sums(ordering)} {ok} {bf_ok}"

def test_graham_integer_structured():
    for A in ([1, 2, 3], [-5, -2, 1, 3, 7], list(range(1, 11)), list(range(-5, 6))):
        if 0 in A:
            continue
        ordering = valid_ordering_integers(A)
        assert is_valid(ordering), f"{A} -> {ordering} sums: {partial_sums(ordering)}"

from verify_integer_version import verify

def test_verify_integer_version():
    examples = [
        {1, 2, 3},
        {-5, -2, 1, 3, 7},
        {10, -3, 8, -1, 4, -6},
        set(range(1, 11)),
        set(range(-10, 0)) | set(range(1, 11)),
    ]
    for A in examples:
        ordering, sums, ok = verify(A)
        assert isinstance(ordering, list)
        assert isinstance(sums, list)
        assert isinstance(ok, bool)
        assert ok, f"Expected mathematical validity but failed for {A}"
