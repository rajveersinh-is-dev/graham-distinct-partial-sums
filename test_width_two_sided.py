import sys
sys.path.insert(0, "src")
from graham_width import valid_ordering_width
from graham_verify import is_two_sided_valid_mod_p, width_condition_holds
from itertools import combinations

def test():
    for p in [5, 7, 11, 13, 17, 19]:
        elems = list(range(1, p))
        for r in range(1, p):
            for subset in combinations(elems, r):
                if width_condition_holds(subset, p):
                    ord_ = valid_ordering_width(subset, p)
                    if not is_two_sided_valid_mod_p(ord_, p):
                        print(f"Failed for {subset} mod {p}, ordering {ord_}")
                        return
    print("All width condition orderings are two-sided valid!")

test()
