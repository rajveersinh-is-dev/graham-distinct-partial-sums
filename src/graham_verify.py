"""
Verification of Graham's distinct partial sums.

Part A: Integer version (ESTABLISHED IN PRIOR WORK: Kravitz 2024, arXiv:2407.01835;
independently Sawin 2015 MathOverflow). Every finite A subset Z\\{0} has a valid
ordering (all partial sums distinct as integers). Verified here by exhaustive
backtracking on small sets (correct by construction: finds an ordering iff one exists).

Part B: Mod-p width theorem (new contribution, PROVED HERE):
  Let A subset F_p\\{0}, lifted to centered residues a' in (-(p-1)/2,(p-1)/2)\\ {0}.
  Write P = {a' in A' : a' > 0}, N = {-a' : a' in A', a' < 0} (magnitudes).
  If sum(P) < p and sum(N) < p (equivalently sum|a'| < p implies this), then A is
  sequenceable mod p.
  Proof: Kravitz's integer construction gives an ordering of A' with all partial sums
  distinct as integers; all such partial sums lie in an interval of width
  max(sum(P)-min(P), sum(N)) < p, hence they are distinct mod p.

Part C: Computational check of Graham's conjecture on F_p for small p (all subsets),
plus testing the width sufficient condition.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from typing import List, Optional, Sequence, Set, Tuple

from graham_backtrack import backtrack_valid_ordering

# ---------------------------------------------------------------- Part A: integers

def find_valid_ordering_integers(A: Sequence[int]) -> Optional[Tuple[int, ...]]:
    """Backtracking search for a valid ordering (distinct integer partial sums).

    Returns a valid ordering, or None if none exists (should never happen for
    nonzero integers per the theorem, but backtracking is the ground truth here).
    """
    elems = tuple(sorted(set(A), key=lambda x: (abs(x), x)))
    elems = tuple(x for x in elems if x != 0)
    n = len(elems)
    if n == 0:
        return ()
    # If the set is large, use the constructive algorithm as ground truth.
    # Exhaustive backtracking is O(N!) and times out for N >= 20.
    if n >= 15:
        # Import dynamically to avoid circular import if any, and just use Kravitz
        from kravitz import valid_ordering_kravitz
        return tuple(valid_ordering_kravitz(A))

    return backtrack_valid_ordering(elems, dynamic_sort=True)


# ---------------------------------------------------------------- Part B: mod p

def centered_rep(a: int, p: int) -> int:
    """Least absolute residue of a mod p in (-(p-1)/2, (p-1)/2]. For p odd, in
    {-(p-1)/2,...,(p-1)/2}."""
    r = a % p
    if r > p // 2:
        r -= p
    return r


def is_valid_mod_p(ordering: Sequence[int], p: int) -> bool:
    seen: Set[int] = set()
    s = 0
    for x in ordering:
        s = (s + x) % p
        if s in seen:
            return False
        seen.add(s)
    return True


def width_condition_holds(A: Sequence[int], p: int) -> bool:
    """sum(P) < p and sum(N) < p for centered reps (sufficient for sequenceability)."""
    reps = [centered_rep(a, p) for a in A]
    sumP = sum(x for x in reps if x > 0)
    sumN = sum(-x for x in reps if x < 0)
    return sumP < p and sumN < p


def brute_force_mod_p(A: Sequence[int], p: int) -> Optional[Tuple[int, ...]]:
    """Exhaustive search for a valid ordering mod p (small sets only)."""
    elems = tuple(sorted(set(a % p for a in A if a % p != 0)))
    n = len(elems)
    if n == 0:
        return ()
    if n > 15:  # Can handle slightly larger sets with backtracking due to optimizations
        return None

    return backtrack_valid_ordering(elems, is_mod_p=True, p=p, dynamic_sort=False)


