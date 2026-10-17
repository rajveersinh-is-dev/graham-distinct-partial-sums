# Main Results

## Notation
- p: an odd prime; F_p the field of residues mod p.
- For A⊆F_p\\{0}, let A' be the centered representatives in {-(p-1)/2,...,(p-1)/2}\\{0}.
- P := {a'∈A' : a'>0} (positive centered reps).
- N := {-a' : a'∈A', a'<0} (magnitudes of negative centered reps), so A' = P ∪ (-N).
- σ_+(P) := ∑P, σ_-(N) := ∑N.
- An ordering a_1,...,a_n of a finite set in an abelian group is VALID if its partial sums s_k=a_1+...+a_k (1≤k≤n) are pairwise distinct.

## Main theorem (PROVED HERE)

**Theorem 1 (Width sufficient condition).**
Let p be prime and A⊆F_p\\{0}. With P, N as above, if
   σ_+(P) < p,   σ_-(N) < p,   and   σ_+(P) ≠ σ_-(N),
then A is sequenceable modulo p: there is an ordering of A whose partial sums are pairwise distinct mod p.

**Category:** PROVED HERE. Proof in mathematics/proofs.md. Relies on a self-contained integer ordering lemma (Lemma 1 below); does NOT rely on unproved conjectures.

**Significance.** Extends beyond Kravitz's rectification range |A|≤⌈log p/log log p⌉: every set whose centered representatives have positive-sum < p and negative-magnitude-sum < p (with unequal totals) is sequenceable. This includes sets of size up to ~√(2p) (e.g. A={1,...,k} with k(k+1)/2<p), well beyond the rectification range.

**Limitations.** The hypothesis σ_+(P)≠σ_-(N) is technical; the case σ_+(P)=σ_-(N) (centered reps summing to 0) is not covered by the proof and is left as a small open subcase. Computationally it is also sequenceable in all small cases checked.

## Lemma 1 (integer ordering lemma, PROVED HERE)
Let P,N be finite sets of positive integers with ∑P≠∑N. Then there exist orderings of P and of N such that no (nonempty) prefix-sum of P equals a prefix-sum of N, except that the empty prefix-sum 0 is common.

## Corollary (PROVED HERE)
If A={1,2,...,k}⊆F_p^× (viewed mod p) with k(k+1)/2 < p, then A is sequenceable mod p.
(P: all of A since all positive, N empty; need ∑A=k(k+1)/2<p and ∑P≠∑N=0, true since sum>0.)

## Computational verification (COMPUTATIONALLY VERIFIED, finite)
- src/graham_width.py: the construction produces distinct mod-p partial sums for every width-satisfying set for p≤23 (exhaustive), and for thousands of random sets; cross-checked against brute force with complete agreement.
- src/graham_verify.py: Graham's conjecture holds for all subsets of size ≤5 for p=3,5,7,11,13 (brute force); integer version verified on ~4000 random sets via backtracking.

## Open status
Graham's conjecture for arbitrary |A| remains OPEN. Theorem 1 is a rigorous partial result (Final verdict category: C, Rigorous Partial Result).
