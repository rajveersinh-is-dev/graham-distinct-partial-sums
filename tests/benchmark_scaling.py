import sys
sys.path.insert(0, "src")

import time
import random
from graham_verify import backtrack_valid_ordering, heuristic_valid_ordering_mod_p, width_condition_holds
from graham_width import valid_ordering_width

def benchmark_scaling():
    print("Benchmarking scaling of Mod P sequenceability methods...")

    primes = [31, 101, 1009]
    sizes = [15, 25, 35, 50, 100]

    for p in primes:
        for size in sizes:
            if size >= p:
                continue

            print(f"\nPrime: {p}, Set size: {size}")

            # Generate a random valid set
            rng = random.Random(42 + p + size)
            A = rng.sample(range(1, p), size)

            # 1. Backtracking
            if size <= 25:
                start = time.time()
                res_bt = backtrack_valid_ordering(A, is_mod_p=True, p=p, dynamic_sort=False)
                bt_time = time.time() - start
                print(f"  Backtracking: {'Success' if res_bt else 'Fail'} in {bt_time:.4f}s")
            else:
                print("  Backtracking: Skipped (size > 25)")

            # 2. Heuristic
            start = time.time()
            res_heur = heuristic_valid_ordering_mod_p(A, p, max_restarts=100)
            heur_time = time.time() - start
            print(f"  Heuristic: {'Success' if res_heur else 'Fail'} in {heur_time:.4f}s")

            # 3. Mathematical Width Condition
            if width_condition_holds(A, p):
                start = time.time()
                res_width = valid_ordering_width(A, p)
                width_time = time.time() - start
                print(f"  Width Math Construction: {'Success' if res_width else 'Fail'} in {width_time:.4f}s")
            else:
                print("  Width Math Construction: Skipped (condition not met)")

if __name__ == "__main__":
    benchmark_scaling()
