import sys
sys.path.insert(0, "src")

import time
import random
import pytest
from graham_verify import find_valid_ordering_mod_p, width_condition_holds, is_valid_mod_p

@pytest.mark.parametrize("p, size", [
    (101, 15),
    (101, 30),
    (101, 50),
    (101, 80),
    (1009, 15),
    (1009, 30),
    (1009, 50),
    (1009, 100),
    (1009, 250),
])
def test_hybrid_find_valid_ordering_mod_p_benchmark(p, size):
    if size >= p:
        pytest.skip(f"Size {size} >= prime {p}")

    rng = random.Random(42 + p + size)
    A = rng.sample(range(1, p), size)

    start = time.time()
    ordering = find_valid_ordering_mod_p(A, p)
    elapsed = time.time() - start

    assert ordering is not None, f"Failed to find valid ordering for p={p}, size={size}"
    assert len(ordering) == len(set(a % p for a in A if a % p != 0)), "Length mismatch"
    assert is_valid_mod_p(ordering, p), f"Invalid ordering for p={p}, size={size}"

    print(f"\\np={p}, size={size}: time={elapsed:.4f}s (width_condition={width_condition_holds(A, p)})")
