from typing import Sequence, Optional, Tuple

def backtrack_valid_ordering(
    elems: Sequence[int],
    is_mod_p: bool = False,
    p: int = 1,
    dynamic_sort: bool = False
) -> Optional[Tuple[int, ...]]:
    """
    Exhaustive search for a valid ordering (distinct partial sums).

    :param elems: Elements to sequence (already reduced/cleaned)
    :param is_mod_p: If True, do arithmetic modulo p
    :param p: The modulus (used only if is_mod_p is True)
    :param dynamic_sort: If True, order candidates dynamically at each step to keep running sum small
    """
    n = len(elems)
    if n == 0:
        return ()

    total_sum = sum(elems)
    if is_mod_p:
        total_sum %= p

    used_mask = 0
    seen = set()
    result = [0] * n

    # Fixed order of elements for indexing
    if dynamic_sort:
        order = sorted(elems, key=lambda x: (abs(x), x))
    else:
        order = list(elems)

    def bt(k: int, cur: int) -> bool:
        nonlocal used_mask
        if k == n:
            return True

        if dynamic_sort:
            # Reorder candidates dynamically to stay near 0
            candidates = []
            for i in range(n):
                if not (used_mask & (1 << i)):
                    candidates.append(i)
            candidates.sort(key=lambda idx: abs(cur + order[idx]))
        else:
            candidates = range(n)

        for i in candidates:
            if not dynamic_sort and (used_mask & (1 << i)):
                continue

            x = order[i]
            nxt = cur + x
            if is_mod_p:
                nxt %= p

            if nxt in seen:
                continue

            # Pruning: The final sum (k=n-1) will exactly be total_sum.
            if k < n - 1 and nxt == total_sum:
                continue

            used_mask |= (1 << i)
            seen.add(nxt)
            result[k] = x

            if bt(k + 1, nxt):
                return True

            seen.remove(nxt)
            used_mask &= ~(1 << i)

        return False

    if bt(0, 0):
        return tuple(result)
    return None
