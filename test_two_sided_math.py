def is_valid_mod_p(ordering, p):
    seen = set()
    s = 0
    for x in ordering:
        s = (s + x) % p
        if s in seen:
            return False
        seen.add(s)
    return True

def test():
    for p in [3, 5, 7, 11]:
        from itertools import permutations
        elems = list(range(1, p))
        from itertools import combinations
        for r in range(1, p):
            for subset in combinations(elems, r):
                for ord_ in permutations(subset):
                    if is_valid_mod_p(ord_, p):
                        s = 0
                        has_zero = False
                        for i, x in enumerate(ord_[:-1]):
                            s = (s + x) % p
                            if s == 0:
                                has_zero = True
                        is_two = is_valid_mod_p(ord_[::-1], p)
                        if is_two == has_zero:
                            print(f"Failed for {ord_}: is_two={is_two}, has_zero={has_zero}")
test()
print("Done")
