# Research Log

## 2026-01-?? (session start)
- Environment: git 2.53.0, gh 2.96.0 authenticated to daveaddams91-dev (repo scope), Python 3.14.6. Empty working dir; initialized git repo on branch main.
- Explored candidate open problems (Open Problem Garden + web search).
- Rejected: Snevily's conjecture (solved, Arsovski 2011), covering-systems min modulus (solved, Hough 2015), Bollobás–Leader subsequence sums (heavily mined/computation-assisted), Graham pebbling (well-mined/hard), Erdős–Turán (famous/hard).
- Selected: Graham's distinct partial sums conjecture (confirmed open via arXiv:2407.01835).
- Created README.md, research/*.md, mathematics/definitions.md.

## Verification of prior work (computationally)
- src/graham_verify.py: integer version of Graham's conjecture verified on ~4000 random sets via backtracking (all have valid orderings; 0 failures). Confirms Theorem 1.3 of arXiv:2407.01835 empirically.
- Graham's conjecture mod p verified by brute force for all subsets of size ≤5, p=3,5,7,11,13.

## New result: width sufficient condition (PROVED HERE)
- Developed Theorem 1: if centered reps of A have positive-sum <p, negative-magnitude-sum <p, and unequal totals, then A is sequenceable mod p.
- Proof: self-contained Lemma 1 (integer ordering via "remove from larger total side") + range bound <p + distinct-integers ⇒ distinct-mod-p.
- src/graham_width.py: implements the construction; verified on 5842 random integer sets (0 failures), exhaustively for all width-satisfying subsets p≤23, and cross-checked against brute force (complete agreement).
- mathematics/main_results.md, mathematics/proofs.md written.

## Remaining work
- Write LaTeX paper (paper/main.tex + references.bib).
- Add tests/ (test_width.py).
- docs/reproducibility.md.
- Create public GitHub repo, commit, push.
- Honest limitations: σ_+(P)=σ_-(N) case uncovered; full conjecture still open.
