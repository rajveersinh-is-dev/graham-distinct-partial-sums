# Reproducibility

## Computational claims
All computational claims in this project were produced by running the code in
this repository in Python 3.14.6. No floating-point arithmetic is used; all
arithmetic is exact integer/modular arithmetic.

### Files
- `src/graham_width.py` — constructive proof of Theorem 1 (width sufficient condition).
- `src/graham_verify.py` — verification of the integer version of Graham's conjecture and the mod-$p$ brute-force checks.
- `tests/test_width.py` — automated tests (prefix-sum invariant, exhaustive mod-$p$ checks for $p\le 23$, corollary for consecutive sets, backtracking ground truth for the integer version).

### How to reproduce
```
python tests/test_width.py
```
This runs the full test suite and should print "All tests passed."

To run the mod-$p$ exhaustive check and the mod-$p$ width-corollary check,
run `src/graham_width.py` directly (it prints per-prime summaries).

To verify the integer version of Graham's conjecture on random sets, run
`src/graham_verify.py`.

### Random seeds
- `src/graham_verify.py`: `random.seed(1)`.
- `src/graham_width.py`: `random.seed(2)` and `random.seed(3)`.
- `tests/test_width.py`: `random.seed(4)` and `random.seed(5)`.

### Finite scope
All computational claims are finite: exhaustive subset checks for small
primes ($p\le 23$), subset sizes up to 5--7, and thousands of random
instances. None of these computations is claimed to prove the general
conjecture; they support the stated finite results only.

## Mathematical proof
The proof of Theorem 1 is fully self-contained and elementary (Lemma 1 plus
a range argument). It requires no software and can be checked by hand. It is
written in `mathematics/proofs.md` and summarized in `paper/main.tex`.

## Environment
- Python 3.14.6
- No external dependencies (standard library only)
- OS: Windows

## Limitations
The proof covers $\sum P\ne\sum N$; the case $\sum P=\sum N$ is not covered
and remains a small open subcase. Graham's conjecture for arbitrary $|A|$
remains open.
