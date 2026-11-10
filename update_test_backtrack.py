import re

with open('tests/test_backtrack.py', 'r') as f:
    content = f.read()

new_tests = '''
import pytest

def test_backtrack_timeout_raised():
    """Verify that the backtracking search correctly raises TimeoutError when the limit is exceeded."""
    # A constructed set that requires a lot of backtracking when searching for a valid ordering
    # We set a very short timeout to ensure it triggers
    from graham_backtrack import backtrack_valid_ordering
    elems = list(range(1, 24))  # large enough to take time if exhaustive
    with pytest.raises(TimeoutError):
        # Even with timeout 0.0, the first check will trigger it
        backtrack_valid_ordering(elems, is_mod_p=False, timeout=0.0001)

def test_backtrack_two_sided_timeout_raised():
    """Verify that the two-sided backtracking search correctly raises TimeoutError."""
    from graham_backtrack import backtrack_two_sided_valid_ordering
    elems = list(range(1, 24))
    with pytest.raises(TimeoutError):
        backtrack_two_sided_valid_ordering(elems, is_mod_p=True, p=29, timeout=0.0001)
'''

content += new_tests

with open('tests/test_backtrack.py', 'w') as f:
    f.write(content)
