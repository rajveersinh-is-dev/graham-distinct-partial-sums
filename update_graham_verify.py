import re

with open('src/graham_verify.py', 'r') as f:
    content = f.read()

# Update is_two_sided_valid_mod_p to use the O(n) pass
is_two_sided_valid_mod_p_new = '''def is_two_sided_valid_mod_p(ordering: Sequence[int], p: int) -> bool:
    """
    Check if an ordering is valid mod p in both forward and reversed directions.
    By Theorem 2, a forward-valid ordering is two-sided valid iff no proper partial sum is 0 mod p.
    """
    seen: Set[int] = set()
    s = 0
    has_zero_proper_prefix = False
    n = len(ordering)

    for i, x in enumerate(ordering):
        s = (s + x) % p
        if s in seen:
            return False
        seen.add(s)
        if i < n - 1 and s == 0:
            has_zero_proper_prefix = True

    return not has_zero_proper_prefix'''

content = re.sub(
    r'def is_two_sided_valid_mod_p\(.*?\) -> bool:.*?return is_valid_mod_p\(ordering, p\) and is_valid_mod_p\(ordering\[::-1\], p\)',
    is_two_sided_valid_mod_p_new,
    content,
    flags=re.DOTALL
)

# Update find_two_sided_valid_ordering_mod_p to use width condition
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
        return backtrack_two_sided_valid_ordering(elems, is_mod_p=True, p=p)
    else:
        return heuristic_two_sided_valid_ordering_mod_p(elems, p)'''

content = re.sub(
    r'def find_two_sided_valid_ordering_mod_p\(.*?\).*?return heuristic_two_sided_valid_ordering_mod_p\(elems, p\)',
    find_two_sided_valid_ordering_mod_p_new,
    content,
    flags=re.DOTALL
)

with open('src/graham_verify.py', 'w') as f:
    f.write(content)
