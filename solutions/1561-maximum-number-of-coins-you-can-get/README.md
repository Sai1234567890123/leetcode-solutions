# 1561. Maximum Number of Coins You Can Get

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/maximum-number-of-coins-you-can-get/](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/)  
**Topics:** Array, Math, Greedy, Sorting, Game Theory

---

## 📝 Problem Statement

There are `3n` piles of coins of varying size, you and your friends will take piles of coins as follows:

	- In each step, you will choose **any **`3` piles of coins (not necessarily consecutive).

	- Of your choice, Alice will pick the pile with the maximum number of coins.

	- You will pick the next pile with the maximum number of coins.

	- Your friend Bob will pick the last pile.

	- Repeat until there are no more piles of coins.

Given an array of integers `piles` where `piles[i]` is the number of coins in the `ith` pile.

Return the maximum number of coins that you can have.

 
Example 1:

```

**Input:** piles = [2,4,1,2,7,8]
**Output:** 9
**Explanation: **Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with **7** coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with **2** coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, **2**, 8), (2, **4**, 7) you only get 2 + 4 = 6 coins which is not optimal.

```

Example 2:

```

**Input:** piles = [2,4,5]
**Output:** 4

```

Example 3:

```

**Input:** piles = [9,8,7,6,5,1,2,3,4]
**Output:** 18

```

 
**Constraints:**

	- `3 5`

	- `piles.length % 3 == 0`

	- `1 4`

---

## 💻 Implementation (python3)

```py
class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        """
        Greedy strategy:
        To maximize our share, we want Bob to take the smallest possible piles.
        For each round of 3 piles, Alice takes the largest remaining, we take the
        second largest remaining, and Bob takes the smallest remaining pile.
        
        Given 3n piles:
        - Bob gets the smallest n piles.
        - Out of the remaining 2n largest piles, Alice and we alternate picking 
          from the top.
        - Therefore, we receive elements at indices: n, n + 2, n + 4, ..., 3n - 2.
        """
        piles.sort()
        n = len(piles) // 3
        # piles[n::2] selects every second element starting from index n up to the end.
        return sum(piles[n::2])
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to choose triplets such that we maximize the sum of the second-largest element of each triplet, while Alice takes the largest and Bob takes the smallest.

To maximize our total coins:
1. **Minimize Bob's gain:** Bob must take one pile per round. To waste as little coin value as possible on Bob, we should give Bob the absolute smallest piles across the entire game. If there are $3n$ piles, Bob will take the smallest $n$ piles.
2. **Maximize our gain:** For the remaining $2n$ largest piles, in each step, Alice should take the largest available pile, and we should take the second-largest available pile.
   
By sorting the array in ascending order:
- The first $n$ elements (indices $0$ to $n - 1$) are assigned to Bob.
- The remaining $2n$ elements (indices $n$ to $3n - 1$) are divided between us and Alice in pairs. In each pair, we get the smaller element and Alice gets the larger element.
- Thus, Alice gets indices $3n - 1, 3n - 3, \dots, n + 1$, and we get indices $3n - 2, 3n - 4, \dots, n$.

### Step-by-Step Approach

1. Sort the `piles` array in ascending order.
2. Calculate $n = \text{len}(piles) // 3$, which represents the total number of rounds.
3. Sum every second element starting from index $n$ to the end of the array (i.e., `piles[n::2]`).
4. Return the computed sum.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M \log M)$ where $M$ is the length of `piles` ($M = 3n$). Sorting dominates the runtime. Python's Timsort operates in $\mathcal{O}(M \log M)$ time, and the slicing/summation takes $\mathcal{O}(M)$ time.
  *(Note: Since the maximum value in `piles` is bounded by $10^4$, Counting Sort can alternatively be used to achieve $\mathcal{O}(M + K)$ linear time, where $K = \max(\text{piles})$).*
- **Space Complexity:** $\mathcal{O}(M)$ or $\mathcal{O}(1)$ auxiliary space depending on the sorting implementation. In Python, Timsort requires $\mathcal{O}(M)$ auxiliary space in the worst case.

---

### Common Pitfalls / Mistakes

1. **Greedy Suboptimal Grouping:** Trying to form triplets greedily from local windows (e.g., adjacent triplets `(i, i+1, i+2)`) instead of globally routing the $n$ smallest elements to Bob.
2. **Off-by-One / Indexing Errors:** Miscalculating the starting index or step size when iterating over our share of the piles.
3. **Simulating using Deque/Pointers:** While maintaining two pointers (`left` for Bob, `right` for Alice, `right - 1` for us) works in $\mathcal{O}(M)$ after sorting, building and mutating explicit queue/stack structures incurs unnecessary overhead compared to direct index stepping.

---

### Real Interview Follow-Up Questions

#### 1. What if the values are bounded such that $piles[i] \le 10^4$? Can we do better than $\mathcal{O}(M \log M)$?
**Answer:** Yes. Since $K = \max(piles) \le 10^4 \ll M \log M$ when $M = 10^5$, we can use **Counting Sort** (or Bucket Sort). We create a frequency array of size $10^4 + 1$, count frequencies in $\mathcal{O}(M)$, and then iterate backwards to pick $n$ elements (our shares) while skipping Alice's and ignoring Bob's. This reduces the time complexity to $\mathcal{O}(M + K)$.

#### 2. What if the input is a massive stream of coin piles that cannot fit into memory?
**Answer:** If $3n$ is known upfront, finding the top $2n$ elements would typically require an external sort or a selection algorithm (e.g., Quickselect) on disk. However, if the coin values have a bounded range (e.g., 32-bit integers or known finite range), streaming into an external histogram / distributed count-min sketch or external merge sort allows determining the exact threshold values with minimal memory.

#### 3. What if there are $k$ friends picking in a specific order instead of 3?
**Answer:** The logic generalizes directly. If there are $k \times n$ piles and $k$ players where player $P$ picks the $r$-th largest pile in each round ($1 \le r \le k$):
- Players picking after player $P$ absorb the smallest piles.
- Player $P$ and players picking before $P$ divide the largest piles.
- After sorting, we isolate the top $(k - r + 1) \times n$ elements and select every $(k - r + 1)$-th element corresponding to our turn.
