"""
Test candidate constructions for the width sufficient condition:
  Given A subset F_p\\{0}, centered reps A', P=positives, N=negative magnitudes.
  Condition: sum(P) < p and sum(N) < p.
  Find an ordering of A' (as integers) with distinct partial sums AND range < p,
  which then implies distinct mod p.

Constructions tested:
  C1: P in decreasing order, then -N with N increasing.
  C2: P in increasing order, then -N with N decreasing.
  C3: P increasing, then -N increasing.
  C4: P decreasing, then -N decreasing.
"""

from __future__ import annotations

from itertools import combinations
from typing import List, Optional, Sequence, Tuple


def centered_rep(a: int, p: int) -> int:
    r = a % p
    if r > p // 2:
        r -= p
    return r


def partial_sums(ordering: Sequence[int]) -> List[int]:
    out, s = [], 0
    for x in ordering:
        s += x
        out.append(s)
    return out


def is_valid_integers(ordering: Sequence[int]) -> bool:
    sums = partial_sums(ordering)
    return len(sums) == len(set(sums))


def range_width(ordering: Sequence[int]) -> int:
    sums = partial_sums(ordering)
    return max(sums) - min(sums) if sums else 0


def construct_C(P: List[int], N: List[int]) -> List[int]:
    # P decreasing, then -N with N increasing
    return sorted(P, reverse=True) + [-n for n in sorted(N)]


def construct_C2(P: List[int], N: List[int]) -> List[int]:
    # P increasing, then -N with N decreasing
    return sorted(P) + [-n for n in sorted(N, reverse=True)]


def construct_C3(P: List[int], N: List[int]) -> List[int]:
    # P increasing, then -N increasing
    return sorted(P) + [-n for n in sorted(N)]


def construct_C4(P: List[int], N: List[int]) -> List[int]:
    # P decreasing, then -N decreasing
    return sorted(P, reverse=True) + [-n for n in sorted(N, reverse=True)]


CONSTRUCTORS = {"C1": construct_C, "C2": construct_C2, "C3": construct_C3, "C4": construct_C4}


def run_constructor(name, p, max_subset=5):
    elems = list(range(1, p))
    total = 0
    cond_holds = 0
    works = 0
    fails: List[Tuple] = []
    for r in range(1, min(max_subset, p - 1) + 1):
        for subset in combinations(elems, r):
            total += 1
            reps = [centered_rep(a, p) for a in subset]
            P = [x for x in reps if x > 0]
            N = [-x for x in reps if x < 0]
            if sum(P) < p and sum(N) < p:
                cond_holds += 1
                ordering = CONSTRUCTORS[name](P, N)
                if is_valid_integers(ordering) and range_width(ordering) < p:
                    works += 1
                else:
                    fails.append((subset, P, N, ordering, partial_sums(ordering), range_width(ordering)))
    return total, cond_holds, works, fails


def test_constructions():
    for name in CONSTRUCTORS:
        print(f"=== {name} ===")
        for p in [7, 11, 13, 17, 19]:
            total, cond_holds, works, fails = run_constructor(name, p, max_subset=6)
            print(f"  p={p}: subsets={total}, cond_holds={cond_holds}, works={works}, fails={len(fails)}")
            if fails:
                print("    first fail:", fails[0])
        print()
