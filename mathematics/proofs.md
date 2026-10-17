# Proofs

## Notation (recap)
p prime; A⊆F_p\\{0}; centered reps A'; P={a'>0}; N={-a':a'<0}; σ_+=∑P, σ_-=∑N.

## Lemma 1 (integer ordering lemma)
**Statement.** Let P,N be finite sets of positive integers with σ_+(P)≠σ_-(N). Then there exist orderings of P and of N such that no nonempty prefix-sum of P equals a prefix-sum of N (the empty prefix-sum 0 is common to both).

**Proof.** Induction on |P|+|N|, removing an element from the side with strictly larger total.

Base: if one side is empty, say N=∅, then the only prefix-sum of N is 0 (empty); every nonempty prefix-sum of P is positive, hence nonzero, so the sets of nonempty prefix-sums are disjoint. Similarly if P=∅.

Inductive step: assume σ_+(P)>σ_-(N) (the other case is symmetric). Since σ_+(P)>0, P is nonempty. Choose p*∈P with p*≠σ_+(P)-σ_-(N); this is possible because:
- if |P|≥2, at most one element of P equals σ_+(P)-σ_-(N), so another choice exists;
- if |P|={p} is a singleton, then σ_+(P)=p>σ_-(N) and p≠p-σ_-(N) since σ_-(N)>0.

Set P'=P\\{p*}. Then σ_+(P')=σ_+(P)-p*≠σ_-(N) by the choice of p*, so the induction hypothesis applies to (P',N): there are orderings of P' and N whose nonempty prefix-sums are disjoint.

Now order P as (ordering of P') followed by p*. The nonempty prefix-sums of this P-ordering are: the nonempty prefix-sums of P' (already disjoint from all prefix-sums of N) together with the full sum σ_+(P). Since σ_+(P)>σ_-(N) and every nonempty prefix-sum of N is at most σ_-(N), we have σ_+(P)>σ_-(N)≥(every nonempty prefix-sum of N), so σ_+(P) is not a prefix-sum of N. Thus no nonempty prefix-sum of P equals a prefix-sum of N. The case σ_-(N)>σ_+(P) is symmetric (remove from N). ∎

## Theorem 1 (width sufficient condition)
**Statement.** Let p be prime, A⊆F_p\\{0}, with centered reps A', P, N as above. If σ_+(P)<p, σ_-(N)<p, and σ_+(P)≠σ_-(N), then A is sequenceable mod p.

**Proof.**
Step 1 (integer orderings). By Lemma 1, choose orderings of P and N whose nonempty prefix-sums are disjoint (only the empty sum 0 is shared). Denote them P_ord and N_ord.

Step 2 (construct the ordering of A'). Output
      a_1,...,a_n := reverse(P_ord) followed by (-n for n in N_ord).
   All entries are nonzero centered integers.

Step 3 (distinct integer partial sums). Let S_k=a_1+...+a_k (integer partial sums).
   - Positive phase (reverse(P_ord)): entries are positive, so these partial sums are strictly increasing, hence mutually distinct, and all lie in (0, σ_+(P)].
   - Negative phase (-N_ord): entries are negative, so these partial sums are strictly decreasing, hence mutually distinct.
   - Cross-phase: a positive-phase partial sum equals a negative-phase partial sum iff
        (∑P - q) = (∑P - n)   for q a (proper-or-empty) prefix-sum of P_ord and n a nonempty prefix-sum of N_ord,
     iff q=n. By Lemma 1, no nonempty prefix-sum of P_ord equals a prefix-sum of N_ord, and q=0 (empty P-prefix) would require n=0 which is not a nonempty N-prefix. So no cross-phase collision.
   Hence all S_1,...,S_n are distinct integers.

Step 4 (range bound). Every partial sum lies in [m, M] where M=σ_+(P) and m=min(1, σ_+(P)-σ_-(N)):
   - positive phase ⊆(0,σ_+(P)]⊆[1,σ_+(P)];
   - negative phase ⊆[σ_+(P)-σ_-(N), σ_+(P)).
   So all partial sums lie in an interval of width at most
        W := σ_+(P) - min(1, σ_+(P)-σ_-(N)).
   If σ_+(P)>σ_-(N), then σ_+(P)-σ_-(N)≥1 (integers), so min(1,...)=1 and W=σ_+(P)-1<p-1<p.
   If σ_-(N)>σ_+(P), then σ_+(P)-σ_-(N)≤-1, so min(1,...)=σ_+(P)-σ_-(N) and W=σ_-(N)<p.
   In either case W<p.

Step 5 (mod p). The S_k are distinct integers in an interval of width W<p. If S_i≡S_j (mod p) for i≠j, then p | (S_i-S_j), so |S_i-S_j|≥p, contradicting |S_i-S_j|≤W<p. Hence S_i≢S_j (mod p) for all i≠j. So the partial sums are distinct mod p. ∎

## Corollary
If A={1,2,...,k}⊆F_p^× with k(k+1)/2<p, then A is sequenceable mod p (take N=∅, σ_+=k(k+1)/2<p, σ_+=σ_-+...≠0=σ_-).
