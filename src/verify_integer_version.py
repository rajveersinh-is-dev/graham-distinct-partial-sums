"""Module for mathematical computation and analysis."""

# Exact-arithmetic verification of Graham's distinct partial sums
# Integer version (Theorem 1.3, Kravitz 2024 / Sawin 2015):
#   Every finite A subset Z \ {0} admits an ordering with all partial sums distinct.
#
# Construction (positives decreasing, then negatives increasing in magnitude):
#   Split A = P (positive) ∪ {-n : n in N} (negative).
#   Order P decreasing: p_1 > p_2 > ... > p_|P|.
#   Order N increasing: n_1 < n_2 < ... < n_|N|.
#   Output: p_|P|, p_|P|-1, ..., p_1, -n_1, -n_2, ..., -n_|N|
#   (equivalently smallest positive first, ..., largest positive, then smallest-magnitude negative, ...)
# The inductive lemma guarantees prefix sums of P and of N collide only at endpoints,
# hence all partial sums of the full ordering are distinct as integers.
#
# This module: construct the ordering and verify all partial sums are distinct.

from __future__ import annotations

from typing import Iterable, List, Tuple



def valid_ordering_integers(A: Iterable[int]) -> List[int]:
    """Return a valid ordering of a finite set of nonzero integers.

    All elements must be nonzero and distinct (A is a set).
    The returned ordering has pairwise-distinct partial sums.
    """
    elems = list(A)
    if any(x == 0 for x in elems):
        raise ValueError("A must not contain 0")
    if len(elems) != len(set(elems)):
        raise ValueError("A must be a set (no duplicates)")
    P = sorted((x for x in elems if x > 0), reverse=True)  # decreasing
    N = sorted((-x for x in elems if x < 0))              # increasing magnitudes
    # Output: positives smallest-first (reverse of P), then negatives -n_1,...,-n_|N|
    ordering: List[int] = list(reversed(P)) + [-n for n in N]
    return ordering


def partial_sums(ordering: Iterable[int]) -> List[int]:
    """Partial sums.
    
    Args:
        ordering:
    
    Returns:
        The computed result
    
    """
    out: List[int] = []
    s = 0
    for x in ordering:
        s += x
        out.append(s)
    return out


def is_valid(ordering: Iterable[int]) -> bool:
    """Is valid.
    
    Args:
        ordering:
    
    Returns:
        The computed result
    
    """
    sums = partial_sums(ordering)
    return len(sums) == len(set(sums))


def verify(A: Iterable[int]) -> Tuple[List[int], List[int], bool]:
    """Check whether the condition holds.
    
    Args:
        A:
    
    Returns:
        tuple: Result of type tuple
    
    """
    ordering = valid_ordering_integers(A)
    sums = partial_sums(ordering)
    return ordering, sums, is_valid(ordering)


if __name__ == "__main__":
    # Demonstrate on a few sets.
    examples = [
        {1, 2, 3},
        {-5, -2, 1, 3, 7},
        {10, -3, 8, -1, 4, -6},
        set(range(1, 11)),
        set(range(-10, 0)) | set(range(1, 11)),
    ]
    for A in examples:
        ordering, sums, ok = verify(A)
        print(f"A = {sorted(A)}")
        print(f"  ordering = {ordering}")
        print(f"  partial sums = {sums}")
        print(f"  valid = {ok}")
        print()
