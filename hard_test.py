import sys
sys.path.insert(0, "src")
from graham_backtrack import backtrack_valid_ordering
import time

def test():
    # Construct a set where backtracking fails but takes a long time
    A = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11]
    start = time.time()
    res = backtrack_valid_ordering(A, is_mod_p=False)
    end = time.time()
    print(f"Time: {end - start:.2f}s")
test()
