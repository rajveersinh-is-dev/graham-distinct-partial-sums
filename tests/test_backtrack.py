import sys
sys.path.insert(0, "src")

import time
from graham_backtrack import backtrack_valid_ordering
from graham_verify import is_valid_mod_p

def is_valid_integers(ordering):
    sums = []
    s = 0
    for x in ordering:
        s += x
        sums.append(s)
    return len(sums) == len(set(sums))

def test_backtrack_symmetric_worst_case():
    """
    Test backtracking on a symmetric worst-case structure for integers.
    A = {1, 2, ..., n, -1, -2, ..., -n}
    This is highly prone to generating zero sums and repeated sums.
    """
    n = 10  # 20 elements total
    A = list(range(1, n + 1)) + list(range(-n, 0))
    ordering = backtrack_valid_ordering(A, dynamic_sort=True)

    assert ordering is not None, "Failed to find ordering for symmetric set"
    assert is_valid_integers(ordering), "Invalid ordering returned"

def test_backtrack_zero_sum_combinations_mod_p():
    """
    Test backtracking on a set mod p that has many zero-sum combinations.
    We take a large prime and include all elements.
    """
    p = 31
    A = list(range(1, p))  # 30 elements
    ordering = backtrack_valid_ordering(A, is_mod_p=True, p=p, dynamic_sort=False)

    assert ordering is not None, "Failed to find ordering for full mod p set"
    assert is_valid_mod_p(ordering, p), "Invalid mod p ordering returned"

def test_backtrack_hard_integer_case():
    """
    Test a challenging, non-symmetric integer set of large size to verify pruning logic handles
    deep search trees efficiently.
    """
    A = [1, 2, 4, 8, 16, 32, -3, -5, -7, -9, -11, -13, 20, 25, 30, -21, -26, -31] # 18 elements
    ordering = backtrack_valid_ordering(A, dynamic_sort=True)

    assert ordering is not None, "Failed to find ordering"
    assert is_valid_integers(ordering), "Invalid integer ordering"
