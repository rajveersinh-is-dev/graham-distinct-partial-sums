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
from kravitz import valid_ordering_kravitz as valid_ordering_integers


def partial_sums(ordering: Iterable[int]) -> List[int]:
    out: List[int] = []
    s = 0
    for x in ordering:
        s += x
        out.append(s)
    return out


def is_valid(ordering: Iterable[int]) -> bool:
    sums = partial_sums(ordering)
    return len(sums) == len(set(sums))


def verify(A: Iterable[int]) -> Tuple[List[int], List[int], bool]:
    ordering = valid_ordering_integers(A)
    sums = partial_sums(ordering)
    return ordering, sums, is_valid(ordering)
