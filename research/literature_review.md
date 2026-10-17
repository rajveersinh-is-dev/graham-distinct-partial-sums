# Literature Review

## Primary problem
Graham's distinct partial sums conjecture:
> For every prime $p$ and every $A\subseteq\mathbb F_p\setminus\{0\}$, there is an ordering of $A$ whose partial sums are all distinct.

## Strongest known results (to be verified against primary sources)
- Graham's conjecture (1971), repeated in Erdős–Graham (1980) and as Problem #475 in [2].
- State of the art (per arXiv:2407.01835, 2024):
  - Holds for $|A|\le 12$ (polynomial method / Combinatorial Nullstellensatz; see [7], [8], [13]).
  - Holds for $|A|=p-2$ and $|A|=p-3$ ([13]).
  - New: holds for $|A|\le \lceil \log p/\log\log p\rceil$ via rectification (Lev [14], Bilu–Lev–Ruzsa [1]) + the integer version.
- Integer version: every finite $A\subseteq\mathbb Z\setminus\{0\}$ has a valid ordering (Theorem 1.3 of arXiv:2407.01835).
- Rectification: if $|A|\le \lceil\log p/\log\ell\rceil$ then $A$ is $\ell$-Freiman-isomorphic to a set of integers (Lev [14], Theorem 2.1 of the 2024 paper).

## Related conjectures/questions
- "Two-sided valid orderings" (open question in arXiv:2407.01835): is there always a valid ordering whose reverse is also valid? Equivalent to avoiding zero-sum consecutive blocks in both directions.
- Conjectures by Feng–Sun–Xiang, Dasgupta–Karolyi–Serra–Szegedy (character/determinant formulations implying sequencing results).
- Snevily's conjecture (solved by Arsovski 2011) — related via Latin transversals / permutations with distinct sums $a_i+b_{\pi(i)}$.

## Sources to verify (primary)
1. arXiv:2407.01835 "Rearranging small sets for distinct partial sums" (2024).
2. R. L. Graham, "On sums of integers taken from a fixed sequence" (1971).
3. P. Erdős & R. L. Graham, "Old and new problems and results in combinatorial number theory" (1980).
4. V. Lev, "The rectifiability threshold in abelian groups," Combinatorica 28 (2008).
5. Y. Bilu, V. Lev, I. Ruzsa, "Rectification principles," Discrete Comput. Geom. 19 (1998).
6. S. Costa, M. A. Pellegrini, "Some new results about a conjecture by Brian Alspach," Arch. Math. 115 (2020).
7. S. Costa, S. Della Fiore, M. Ollis, S. Rovner-Frydman, "On sequences in cyclic groups with distinct partial sums," Electron. J. Combin. 29 (2022).
8. J. Hicks, M. Ollis, J. Schmitt, "Distinct partial sums in cyclic groups," J. Combin. Des. 27 (2019).
9. B. Arsovski, "A proof of Snevily's Conjecture," Israel J. Math. 182 (2011) — for context only (solved problem).

## Status classification (pending primary-source verification)
- Confirmed open: the general conjecture (all $|A|$) is open per arXiv:2407.01835.
- Need to verify: whether any 2024–2026 paper has since solved the full conjecture or extended the range beyond $\log p/\log\log p$.

## What remains unresolved
The conjecture for arbitrary $|A|$ (e.g. $|A|$ growing faster than $\log p/\log\log p$, or $|A|$ proportional to $p$ but not $p-2,p-3$).
