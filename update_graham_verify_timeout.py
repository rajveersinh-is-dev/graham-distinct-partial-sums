import re

with open('src/graham_verify.py', 'r') as f:
    content = f.read()

# Update find_two_sided_valid_ordering_mod_p to catch TimeoutError
find_two_sided_valid_ordering_mod_p_new = '''def find_two_sided_valid_ordering_mod_p(
    A: Sequence[int], p: int
) -> Optional[Tuple[int, ...]]:
    """
    Find a two-sided valid ordering mod p. Uses a hybrid approach:
    1. Deterministic mathematical construction if width condition holds (Theorem 2 Corollary).
    2. Exhaustive search for small sets (N <= 25).
    3. Randomized greedy heuristic for larger sets.
    """
    elems = tuple(sorted(set(a % p for a in A if a % p != 0)))
    n = len(elems)
    if n == 0:
        return ()

    if width_condition_holds(elems, p):
        # By Theorem 2 Corollary, width orderings are inherently two-sided valid.
        return tuple(valid_ordering_width(elems, p))

    if n <= 25:
        try:
            return backtrack_two_sided_valid_ordering(elems, is_mod_p=True, p=p, timeout=5.0)
        except TimeoutError:
            # Fall back to heuristic if backtracking takes too long
            return heuristic_two_sided_valid_ordering_mod_p(elems, p)
    else:
        return heuristic_two_sided_valid_ordering_mod_p(elems, p)'''

content = re.sub(
    r'def find_two_sided_valid_ordering_mod_p.*?return heuristic_two_sided_valid_ordering_mod_p\(elems, p\)',
    find_two_sided_valid_ordering_mod_p_new,
    content,
    flags=re.DOTALL
)

# Update find_valid_ordering_mod_p to catch TimeoutError
find_valid_ordering_mod_p_new = '''def find_valid_ordering_mod_p(A: Sequence[int], p: int) -> Optional[Tuple[int, ...]]:
    """
    Find a valid ordering mod p. Uses a hybrid approach:
    1. Deterministic mathematical construction if width condition holds.
    2. Exhaustive search for small sets (N <= 25).
    3. Randomized greedy heuristic for larger sets.
    """
    elems = tuple(sorted(set(a % p for a in A if a % p != 0)))
    n = len(elems)
    if n == 0:
        return ()

    if width_condition_holds(elems, p):
        return tuple(valid_ordering_width(elems, p))

    if n <= 25:
        # Exhaustive search works reasonably well for N <= 25 with optimizations
        try:
            return backtrack_valid_ordering(elems, is_mod_p=True, p=p, dynamic_sort=False, timeout=5.0)
        except TimeoutError:
            return heuristic_valid_ordering_mod_p(elems, p)
    else:
        # Fall back to heuristic for larger sets
        return heuristic_valid_ordering_mod_p(elems, p)'''

content = re.sub(
    r'def find_valid_ordering_mod_p.*?return heuristic_valid_ordering_mod_p\(elems, p\)',
    find_valid_ordering_mod_p_new,
    content,
    flags=re.DOTALL
)


with open('src/graham_verify.py', 'w') as f:
    f.write(content)
