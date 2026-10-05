# 1079. Letter Tile Possibilities

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/letter-tile-possibilities/](https://leetcode.com/problems/letter-tile-possibilities/)  
**Topics:** Hash Table, String, Backtracking, Counting

---

## 📝 Problem Statement

You have `n`  `tiles`, where each tile has one letter `tiles[i]` printed on it.

Return *the number of possible non-empty sequences of letters* you can make using the letters printed on those `tiles`.

 
Example 1:

```

**Input:** tiles = "AAB"
**Output:** 8
**Explanation: **The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

```

Example 2:

```

**Input:** tiles = "AAABBC"
**Output:** 188

```

Example 3:

```

**Input:** tiles = "V"
**Output:** 1

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from collections import Counter
import math

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Calculates the number of possible non-empty sequences of letters using
        Dynamic Programming with Exponential Generating Functions (combinatorics).
        
        dp[len] represents the number of valid sequences of length 'len' formed
        so far. When incorporating a new character with frequency 'count', we can
        choose to use 'j' instances of it (1 <= j <= count). The number of ways to
        interleave 'j' identical characters into a sequence of length 'k' is C(k + j, j).
        """
        counts = Counter(tiles).values()
        
        # dp[i] will store the number of valid sequences of length i
        dp = [0] * (len(tiles) + 1)
        dp[0] = 1  # Base case: 1 way to form an empty sequence
        
        current_len = 0
        for count in counts:
            # Create a copy for the updated state
            next_dp = list(dp)
            for k in range(current_len + 1):
                if dp[k] == 0:
                    continue
                for j in range(1, count + 1):
                    # math.comb(k + j, j) calculates C(k + j, j)
                    next_dp[k + j] += dp[k] * math.comb(k + j, j)
            
            dp = next_dp
            current_len += count
            
        # Sum of sequences of all lengths from 1 to len(tiles)
        return sum(dp[1:])
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the total number of unique non-empty sequences that can be constructed using a multiset of letters from `tiles`.

A standard approach is DFS / Backtracking using character frequencies, which branches at each step on unique characters. While optimal enough for $N \le 7$, it explores each sequence one-by-one, visiting up to $\sum_{k=1}^N P(N, k)$ states (around 13,700 states for $N = 7$).

We can do dramatically better using **Dynamic Programming / Exponential Generating Functions (EGF)**.
Instead of generating individual sequences, we can count sequences of length $L$ directly:
- Suppose we have already formed sequences of length $k$ using a subset of distinct letters.
- Now we introduce a new letter that appears $c$ times.
- If we choose to include $j$ instances ($1 \le j \le c$) of this new letter, they can be placed in any of the $\binom{k + j}{j}$ positions among the $k$ existing characters.
- Thus, the transition is:
  $$\text{dp}[k + j] = \sum \text{dp}[k] \times \binom{k + j}{j}$$

This completely avoids recursion and explores at most $O(U \cdot N^2)$ state transitions (where $U \le 26$ is unique characters, $N \le 7$), taking less than a few hundred CPU cycles.

---

### Step-by-Step Approach

1. **Frequency Count**: Count occurrences of each character using `Counter(tiles)`.
2. **DP Initialization**:
   - Let `dp[i]` denote the number of unique sequences of length `i`.
   - `dp[0] = 1` (the empty sequence).
   - All other entries `dp[1...N]` are initialized to `0`.
3. **Transition**:
   - For each character frequency `count`:
     - Maintain an updated copy `next_dp`.
     - For every existing sequence length $k \in [0, \text{current\_len}]$ and for every choice $j \in [1, \text{count}]$:
       $$\text{next\_dp}[k + j] += \text{dp}[k] \times \binom{k + j}{j}$$
     - Update `dp = next_dp` and increase `current_len` by `count`.
4. **Result**: The total number of valid non-empty sequences is $\sum_{i=1}^N \text{dp}[i]$.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(U \cdot N^2)$, where $N$ is the length of `tiles` ($N \le 7$) and $U$ is the number of unique characters ($U \le \min(N, 26)$). For $N = 7$, this is at most $7 \times 7^2 / 2 \approx 170$ basic operations, which runs in $\mathcal{O}(1)$ time relative to practical limits and is orders of magnitude faster than generating/backtracking.
- **Space Complexity:** $\mathcal{O}(N)$ auxiliary space for the DP array of size $N + 1$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Permutations with Set Deduplication (`itertools.permutations`)**:
   Generating all permutations for each length and inserting into a `set` leads to duplicate computation and $\mathcal{O}(N! \cdot N)$ memory/time overhead.
2. **Backtracking without Frequency Map**:
   Branching over indices of identical characters rather than unique characters leads to duplicate paths, requiring set-based pruning.
3. **Missing Base/Boundary Cases**:
   Forgetting that the question requests *non-empty* sequences (hence excluding length 0).

---

### Real Interview Follow-Up Questions

1. **"What if $N$ was up to $10^5$, but the answer should be modulo $10^9 + 7$?"**
   - *Answer*: This is the classic polynomial multiplication problem using Exponential Generating Functions (EGF). The generating function for a character with count $c_i$ is $P_i(x) = \sum_{j=0}^{c_i} \frac{x^j}{j!}$. We need to compute the polynomial product $P(x) = \prod P_i(x) \pmod{x^{N+1}}$. We can use Number Theoretic Transform (NTT) with divide-and-conquer in $\mathcal{O}(N \log^2 N)$ time.

2. **"What if we need to return the actual sequences in lexicographical order, not just the count?"**
   - *Answer*: For generating actual sequences, DFS backtracking with a frequency array is preferred. Sorting the unique characters initially guarantees that the generated prefixes and sequences are strictly in lexicographical order, avoiding the need for an expensive post-sort.

3. **"Can we parallelize the computation for very large alphabets?"**
   - *Answer*: Yes. The DP / EGF formulation is associative: multiplying independent polynomials can be done pairwise in a tree reduction structure across multiple cores / GPU threads.
