# Graham's Distinct Partial Sums Conjecture -- Research Project

## The problem (exact statement)
**Graham's conjecture (1971; repeated by Erdős & Graham 1980).**
For every prime $p$ and every $A\subseteq\mathbb F_p\setminus\{0\}$, the
elements of $A$ can be ordered $a_1,\dots,a_{|A|}$ so that the partial sums
$s_k=a_1+\cdots+a_k$ are pairwise distinct modulo $p$.

Such an ordering is called *valid*. The conjecture asks whether every
$A\subseteq\mathbb F_p\setminus\{0\}$ is sequenceable.

## Why it matters
A natural finite-field question about ordering elements to avoid zero-sum
consecutive blocks. Connected to group sequencing, complete mappings, Latin
transversals, and the Hall--Paige conjecture. Simple one-sentence statement;
genuinely open.

## Existing results
- Known: $|A|\le 12$; $|A|\in\{p-2,p-3\}$ (Hicks–Ollis–Schmitt 2019);
  $|A|\le\lceil\log p/\log\log p\rceil$ (Kravitz 2024, via rectification +
  the integer version).
- Integer version (theorem): every finite $A\subseteq\mathbb Z\setminus\{0\}$
  has a valid ordering (Kravitz 2024; Sawin 2015).
- Solved and therefore NOT our target: Snevily's conjecture (Arsovski 2011);
  covering-systems minimum modulus (Hough 2015).

## Strongest result obtained (this project)
**Theorem 1 (width sufficient condition — PROVED HERE).** If the centered
representatives of $A$ satisfy $\sum P<p$ (positives) and $\sum N<p$
(negative magnitudes), then $A$ is sequenceable mod $p$.

This covers sets of size up to $\sim\sqrt{2p}$ (e.g. $\{1,\dots,k\}$ with
$k(k+1)/2<p$), beyond the rectification range.

## Proof strategy
1. Lemma 1: order positive and negative-magnitude parts so their prefix sums
   avoid each other (induction, always removing from the larger-total side).
2. Output reverse(positive part) then negative part; integer partial sums are
   distinct (within-phase monotone, cross-phase avoided by Lemma 1).
3. The integer partial sums lie in an interval of width $<p$ (using
   $\sum P<p$ and $\sum N<p$).
4. Distinct integers in an interval of width $<p$ are distinct mod $p$.

## Novelty qualification
Theorem 1, Lemma 1, and Corollary are PROVED HERE (original to this project).
The integer version and rectification are ESTABLISHED IN PRIOR WORK. The
general conjecture remains OPEN.

## Repository map
- `README.md` — this overview
- `paper/main.tex` — LaTeX paper
- `paper/references.bib` — references
- `mathematics/definitions.md` — definitions
- `mathematics/main_results.md` — theorem statements with evidence categories
- `mathematics/proofs.md` — complete proofs
- `research/` — problem selection, literature review, known results, research log
- `src/` — exact-arithmetic construction and verification
- `tests/` — automated test suite
- `docs/reproducibility.md` — how to reproduce
- `LICENSE`, `.gitignore`, `CHANGELOG.md`

## Dependencies
Python 3.14.6, standard library only.

## Reproduce
```
python tests/test_width.py
```
Should print "All tests passed."

## Known limitations
- Graham's conjecture for arbitrary $|A|$ remains open.

## Final verdict category
C — Rigorous Partial Result (a new sufficient condition proved rigorously;
the original conjecture remains open).
