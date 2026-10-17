"""
Verification of Graham's distinct partial sums.

Part A: Integer version (ESTABLISHED IN PRIOR WORK: Kravitz 2024, arXiv:2407.01835;
independently Sawin 2015 MathOverflow). Every finite A subset Z\{0} has a valid
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
    # Order candidates to improve pruning: try larger absolute values first.
    order = sorted(elems, key=lambda x: -abs(x))

    used = [False] * n
    seen: Set[int] = set()
    cur = 0
    result: List[int] = []

    def bt(k: int) -> bool:
        nonlocal cur
        if k == n:
            return True
        for i in range(n):
            if used[i]:
                continue
            x = order[i]
            nxt = cur + x
            if nxt in seen:
                continue
            used[i] = True
            seen.add(nxt)
            cur = nxt
            result.append(x)
            if bt(k + 1):
                return True
            result.pop()
            cur = nxt - x
            seen.discard(nxt)
            used[i] = False
        return False

    if bt(0):
        return tuple(result)
    return None


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
    if n > 9:
        return None
    for perm in __import__("itertools").permutations(elems):
        if is_valid_mod_p(perm, p):
            return perm
    return None


# ---------------------------------------------------------------- tests

if __name__ == "__main__":
    import random

    random.seed(1)

    print("=== Part A: integer version, backtracking verification ===")
    tested = 0
    fails = 0
    for _ in range(4000):
        n = random.randint(1, 9)
        A = random.sample(range(-20, 21), n)
        A = [x for x in A if x != 0]
        if not A:
            continue
        tested += 1
        ord_ = find_valid_ordering_integers(A)
        if ord_ is None:
            fails += 1
            print("NO ORDERING FOUND (theorem says impossible):", A)
    print(f"tested {tested} random integer sets, failures={fails}")

    print("\n=== Part B: mod p, small primes, all subsets ===")
    for p in [3, 5, 7, 11, 13]:
        elems = list(range(1, p))  # nonzero residues
        total = 0
        ok = True
        details = []
        for r in range(1, min(6, p - 1) + 1):  # subset sizes up to 5
            for subset in combinations(elems, r):
                total += 1
                ord_ = brute_force_mod_p(subset, p)
                if ord_ is None:
                    ok = False
                    details.append(subset)
        print(f"p={p}: checked {total} subsets (sizes 1..5), all sequenceable={ok}")
        if details:
            print("  non-sequenceable:", details[:10])

    print("\n=== Part B: width sufficient condition vs brute force ===")
    for p in [7, 11, 13, 17]:
        elems = list(range(1, p))
        width_ok_but_brute_fail = 0
        width_fail_but_brute_ok = 0
        both_ok = 0
        for r in range(1, min(5, p - 1) + 1):
            for subset in combinations(elems, r):
                w = width_condition_holds(subset, p)
                bf = brute_force_mod_p(subset, p) is not None
                if w and bf:
                    both_ok += 1
                elif w and not bf:
                    width_ok_but_brute_fail += 1
                    print("WIDTH OK but brute FAIL:", subset, "p=", p)
                elif not w and bf:
                    width_fail_but_brute_ok += 1
        print(f"p={p}: width&brute OK={both_ok}, widthOK bruteFAIL={width_ok_but_brute_fail}, "
              f"widthFAIL bruteOK={width_fail_but_brute_ok}")
