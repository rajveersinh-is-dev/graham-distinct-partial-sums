def test():
    for p in [3, 5, 7, 11]:
        from itertools import permutations
        elems = list(range(1, p))
        from itertools import combinations
        for r in range(1, p):
            for subset in combinations(elems, r):
                for ord_ in permutations(subset):
                    seen = set()
                    s = 0
                    forward_valid = True
                    has_zero_before_end = False
                    for i, x in enumerate(ord_):
                        s = (s + x) % p
                        if s in seen:
                            forward_valid = False
                            break
                        seen.add(s)
                        if i < len(ord_) - 1 and s == 0:
                            has_zero_before_end = True

                    if not forward_valid:
                        continue

                    seen_rev = set()
                    s_rev = 0
                    rev_valid = True
                    for x in reversed(ord_):
                        s_rev = (s_rev + x) % p
                        if s_rev in seen_rev:
                            rev_valid = False
                            break
                        seen_rev.add(s_rev)

                    assert rev_valid == (not has_zero_before_end)
test()
print("Theorem confirmed!")
