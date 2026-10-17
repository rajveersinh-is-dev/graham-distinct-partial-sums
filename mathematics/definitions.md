# Formal definitions for Graham's distinct partial sums conjecture

## Setting
- $p$: a prime.
- $\mathbb F_p$: the field of residues modulo $p$.
- For a finite sequence/sequence-without-repetition $A = (a_1,\dots,a_n)$ of elements of an abelian group $G$, an ordering is a listing of the elements of $A$ (a permutation).

## Validity
An ordering $a_1,\dots,a_n$ of a finite set $A$ (in an abelian group) is **valid** if its partial sums
$$s_k = a_1 + a_2 + \cdots + a_k,\qquad 1\le k\le n$$
are pairwise distinct.

Equivalently, no nonempty consecutive block sums to zero:
$$a_{i+1}+\cdots+a_j \ne 0 \quad\text{for all } 1\le i<j\le n.$$

A set $A$ is **sequenceable** (admits a valid ordering) if such an ordering exists.
An ordering is **two-sided valid** if both it and its reverse are valid; equivalently there is no zero-sum consecutive block in either direction (the same condition, since reversing preserves the set of consecutive blocks — actually two-sided means both the ordering and its reverse have distinct partial sums; for subsets this is the same as "no proper nonempty consecutive block sums to 0" in the forward direction, since the reverse condition is the same set of blocks read backward... need care).

## The conjecture (Graham 1971; Erdos & Graham 1980)
**Conjecture.** For every prime $p$ and every $A\subseteq \mathbb F_p\setminus\{0\}$, $A$ is sequenceable.

## Known results
- **Integer version (theorem, Kravitz 2024; independently Sawin 2015):** Every finite $A\subseteq \mathbb Z\setminus\{0\}$ is sequenceable. In fact there is a valid ordering with all positive elements preceding all negative elements.
- **Small sets:** holds for $|A|\le 12$ (polynomial method / Combinatorial Nullstellensatz; Hicks-Ollis-Schmitt 2019 and references).
- **Large sets:** holds for $|A|\in\{p-2,p-3\}$ (Hicks-Ollis-Schmitt 2019).
- **Rectification range (Kravitz 2024):** holds for $|A|\le \lceil\log p/\log\log p\rceil$, via Lev's rectification theorem + the integer version.

## Status
**Confirmed open:** the conjecture for arbitrary $|A|$ is open (state of the art per arXiv:2407.01835).

## Related open question (Kravitz 2024, Remark 1)
Is every $A\subseteq\mathbb F_p\setminus\{0\}$ orderable with a two-sided valid ordering?
