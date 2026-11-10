import time
import sys
sys.path.insert(0, "src")
from graham_backtrack import backtrack_valid_ordering
from itertools import combinations
import pytest

def test_backtrack_timeout():
    elems = list(range(1, 20))
    # This should take a long time to fail if we just search without a timeout?
    # Actually wait, let's just test with a custom timeout param if we add it.
