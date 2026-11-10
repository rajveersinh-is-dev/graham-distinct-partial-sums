import sys
sys.path.insert(0, "src")
from graham_backtrack import backtrack_valid_ordering
import time

def test():
    # Construct a set where backtracking takes a long time
    A = list(range(1, 23)) # This has no valid ordering that sums to 0 before the end, wait, A={1,2,..,22} has total sum 253.
    # Actually just to see how long it takes
    start = time.time()
    res = backtrack_valid_ordering(A, is_mod_p=False)
    end = time.time()
    print(f"Time: {end - start:.2f}s")
test()
