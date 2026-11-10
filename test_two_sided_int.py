from itertools import permutations

def is_valid_integers(ordering):
    seen = set()
    s = 0
    for x in ordering:
        s += x
        if s in seen:
            return False
        seen.add(s)
    return True

def is_two_sided_valid_integers(ordering):
    return is_valid_integers(ordering) and is_valid_integers(ordering[::-1])

for subset in [ (1, 2, -3), (1, 2, 3, -6), (1, -1, 2), (-1, -2, 3, 4) ]:
    for ord_ in permutations(subset):
        if is_valid_integers(ord_):
            has_zero = any(sum(ord_[:i+1]) == 0 for i in range(len(ord_)-1))
            is_two = is_two_sided_valid_integers(ord_)
            assert is_two == (not has_zero)

print("Integer version confirmed!")
