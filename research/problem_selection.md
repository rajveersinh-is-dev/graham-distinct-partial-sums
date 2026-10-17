# Problem Selection

## Primary target
**Graham's distinct partial sums conjecture** (Graham 1971; repeated by Erdős & Graham 1980).

**Statement.** For every prime $p$ and every $A\subseteq \mathbb F_p\setminus\{0\}$, there exists an ordering $a_1,\dots,a_n$ ($n=|A|$) of the elements of $A$ such that the partial sums
$$s_k = a_1+\cdots+a_k,\qquad 1\le k\le n,$$
are pairwise distinct (equivalently, no nonempty consecutive block sums to $0$).

An ordering with this property is called *valid*.

## Why this problem
- **Precise, testable statement**: quantifies over primes $p$ and subsets $A$ of the cyclic group $\mathbb F_p$.
- **Confirmed open**: a 2024 preprint ("Rearranging small sets for distinct partial sums", arXiv:2407.01835) states the state of the art as $|A|\le 12$ and $|A|\in\{p-2,p-3\}$, and proves $|A|\le \log p/\log\log p$. The general conjecture (all $|A|$) remains open.
- **Mathematical insight, not computation**: the problem is purely combinatorial/number-theoretic; no large enumeration is needed to state or (ideally) prove it. Small exact checks are useful only for pattern discovery.
- **Plausible entry points**: the integer version (every finite $A\subseteq\mathbb Z\setminus\{0\}$ has a valid ordering) is known; rectification (Bilu-Lev-Ruzsa, Lev) reduces small subsets of $\mathbb F_p$ to the integer case. A new idea could extend the range or handle structured sets.

## Evaluation against selection criteria
| Criterion | Assessment |
|---|---|
| Meaningful new mathematics | A proof for a new range/family would be a genuine theorem in zero-sum/sequencing theory |
| Plausible route to rigorous result | Rectification + integer case gives a mechanism; structured subsets are a natural next step |
| Mathematical depth | Connects to sequencing, complete mappings, polynomial method, zero-sum theory |
| Quality of frontier | Active: 2020–2026 papers (Costa, Della Fiore, Ollis, Hicks, Sawin, etc.) |
| Independence from large-scale computation | Pure reasoning; small exact checks optional |
| Precision/testability | Very precise; finite for fixed $p$ |
| Elegance | Statement is one sentence |
| Portfolio value | Clean additive-combinatorics theorem |

## Candidate pool considered (and rejected/deprioritized)
- Snevily's conjecture — SOLVED (Arsovski 2011).
- Covering systems minimum modulus — SOLVED negatively (Hough 2015): min modulus $\le 10^{16}$.
- Covering systems with all moduli odd (Erdős–Selfridge) — still open, but famous/hard; no plausible entry point.
- Bollobás–Leader subsequence-sums conjecture for $C_n\times C_n$ — open but heavily mined; remaining composite-$n$ cases appear computation-assisted (the $n=8$ case used ~6 hours cloud compute). Deprioritized.
- Graham's pebbling conjecture $\pi(G\square H)\ge\pi(G)\pi(H)$ — open but well-mined/hard.
- Erdős–Turán additive-basis conjecture — famous, hard, no entry point.

## Next step
Read arXiv:2407.01835 in full; verify open status via primary sources; formulate Targets A–E; attempt a proof.
