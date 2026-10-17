# Known Results (verified against primary sources)

## ESTABLISHED IN PRIOR WORK

### Graham's conjecture (open)
R. L. Graham, "On sums of integers taken from a fixed sequence," Proc. Washington State Univ. Conf. Number Theory (1971), 22-40; repeated in P. Erdős & R. L. Graham, "Old and new problems and results in combinatorial number theory," L'Enseignement Mathématique (1980), as Problem #475 (also in T. Bloom's Erdős Problems collection).

**Statement.** For every prime p and every A⊆F_p\\{0}, there is an ordering a_1,...,a_|A| of A whose partial sums s_k=a_1+...+a_k are pairwise distinct.

**Status:** CONFIRMED OPEN. State of the art (Kravitz 2024, arXiv:2407.01835):
- holds for |A|≤12 (polynomial method / Combinatorial Nullstellensatz; Hicks-Ollis-Schmitt 2019 and references);
- holds for |A|=p-2 and |A|=p-3 (Hicks-Ollis-Schmitt 2019);
- Kravitz (2024): holds for |A|≤⌈log p/log log p⌉, via rectification (Lev 2008; Bilu-Lev-Ruzsa 1998) + the integer version below.
The general conjecture (all |A|) remains open.

### Integer version (theorem)
**Theorem (Kravitz 2024, independently Sawin 2015 MathOverflow).** Every finite A⊆Z\\{0} admits an ordering with all partial sums distinct (as integers).

**Category:** ESTABLISHED IN PRIOR WORK (Kravitz arXiv:2407.01835; Sawin mathoverflow.net/q/202857). We cite it; we do not reprove it.

## Rectification (prior work)
Lev, "The rectifiability threshold in abelian groups," Combinatorica 28 (2008), 491-497: if |A|≤⌈log p/log ℓ⌉ then A⊆F_p is ℓ-Freiman-isomorphic to a set of integers. Bilu-Lev-Ruzsa, Discrete Comput. Geom. 19 (1998), 343-353.

## Solved problems (NOT our target, recorded to avoid duplication)
- Snevily's conjecture: solved by Arsovski, Israel J. Math. 182 (2011), 505-508.
- Covering systems minimum modulus (Erdős): solved negatively by Hough, Ann. of Math. 181 (2015), 361-382 (min modulus ≤10^16).
- Cameron–Erdős sum-free count: proved by Green and Sapozhenko (2003).
- Erdős sum-free deviation (n/3 + Ω(n)): solved by Bedert (2025, arXiv:2502.08624).

## Related open questions (Kravitz 2024, Remarks)
- Two-sided valid orderings: is every A⊆F_p\\{0} orderable with both it and its reverse valid?
- Sequencing of H×Z and other groups (Costa–Della Fiore et al.).

## Status classification
Graham's conjecture (general |A|): CONFIRMED OPEN (per arXiv:2407.01835, state of the art explicitly described as |A|≤12, |A|∈{p-2,p-3}, and the new log-range bound). No 2024-2026 solution of the full conjecture found.
