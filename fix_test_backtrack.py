import re

with open('tests/test_backtrack.py', 'r') as f:
    content = f.read()

# For a set of 1..24, it instantly returns the straight sequence because it's a valid integer ordering!
# To make backtracking take time, we need a set that has no valid ordering but takes time to exhaust,
# or one that has a valid ordering very deep in the tree.
# Actually, since it's just testing if it times out, we could mock time, or just pass a set that takes time.
# A set that takes time: [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11]
# wait, my previous test showed that returned instantly too (0.00s) because 0 is checked at the root!
# To make it take time, we need total_sum != 0, and lots of branches.
# Let's use a mock for time to instantly trigger the timeout, it's safer and less flaky.

mock_timeout = '''
import pytest
import time
from unittest.mock import patch

def test_backtrack_timeout_raised():
    """Verify that the backtracking search correctly raises TimeoutError when the limit is exceeded."""
    from graham_backtrack import backtrack_valid_ordering
    elems = list(range(1, 10))
    # We mock time.time so that the second call returns a huge number
    with patch('time.time', side_effect=[0, 100, 200, 300]):
        with pytest.raises(TimeoutError):
            backtrack_valid_ordering(elems, is_mod_p=False, timeout=5.0)

def test_backtrack_two_sided_timeout_raised():
    """Verify that the two-sided backtracking search correctly raises TimeoutError."""
    from graham_backtrack import backtrack_two_sided_valid_ordering
    elems = list(range(1, 10))
    with patch('time.time', side_effect=[0, 100, 200, 300]):
        with pytest.raises(TimeoutError):
            backtrack_two_sided_valid_ordering(elems, is_mod_p=True, p=29, timeout=5.0)
'''

# Remove the old test functions
content = re.sub(r'def test_backtrack_timeout_raised\(\):.*', '', content, flags=re.DOTALL)

content += mock_timeout

with open('tests/test_backtrack.py', 'w') as f:
    f.write(content)
