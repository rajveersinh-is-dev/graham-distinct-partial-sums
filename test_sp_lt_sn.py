import sys
sys.path.insert(0, "src")
from graham_width import valid_ordering_width
A = [1, -2, -3]  # P={1}, N={2,3}. sP=1, sN=5. p=11.
ord = valid_ordering_width(A, 11)
print(f"ord: {ord}")
s = 0
for x in ord:
    s += x
    print(f"s: {s}")
