import sys
sys.path.insert(0, "src")
from graham_backtrack import backtrack_two_sided_valid_ordering
import time

def test():
    # Construct a set where backtracking two-sided takes a long time
    A = list(range(1, 23))
    start = time.time()
    res = backtrack_two_sided_valid_ordering(A, is_mod_p=True, p=29)
    end = time.time()
    print(f"Time: {end - start:.2f}s, res={res is not None}")
test()
