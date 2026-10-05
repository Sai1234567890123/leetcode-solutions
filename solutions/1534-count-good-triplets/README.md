# 1534. Count Good Triplets

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-good-triplets/](https://leetcode.com/problems/count-good-triplets/)  
**Topics:** Array, Enumeration

---

## 📝 Problem Statement

Given an array of integers `arr`, and three integers `a`, `b` and `c`. You need to find the number of good triplets.

A triplet `(arr[i], arr[j], arr[k])` is **good** if the following conditions are true:


	- `0 

Where `|x|` denotes the absolute value of `x`.

Return* the number of good triplets*.

 
Example 1:

```

**Input:** arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
**Output:** 4
**Explanation:** There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

```

Example 2:

```

**Input:** arr = [1,1,2,2,3], a = 0, b = 0, c = 1
**Output:** 0
**Explanation: **No triplet satisfies all conditions.

```

 
**Constraints:**


	- `3

---

## 💻 Implementation (python3)

```py
class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        
        # Iterate over middle index j and left index i
        for j in range(1, n - 1):
            for i in range(j):
                # Prune early: if |arr[i] - arr[j]| > a, no k can make this triplet valid
                if abs(arr[i] - arr[j]) <= a:
                    val_i = arr[i]
                    val_j = arr[j]
                    for k in range(j + 1, n):
                        val_k = arr[k]
                        if abs(val_j - val_k) <= b and abs(val_i - val_k) <= c:
                            count += 1
                            
        return count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A triplet `(arr[i], arr[j], arr[k])` requires $i < j < k$ and three conditions:
1. $|arr[i] - arr[j]| \le a$
2. $|arr[j] - arr[k]| \le b$
3. $|arr[i] - arr[k]| \le c$

Given the constraint $N \le 100$, an unoptimized brute force evaluates $\approx \frac{N^3}{6} \approx 166,666$ triplets. 

Notice that condition (1) depends **only** on $i$ and $j$. If condition (1) fails, there is no need to examine any $k$. By placing the check $|arr[i] - arr[j]| \le a$ before the innermost loop over $k$, we prune a vast majority of the search space, bringing real-world execution down to a fraction of a millisecond.

---

### Step-by-Step Approach

1. **Outer loop ($j$)**: Fix the middle element index $j$ from $1$ to $n - 2$.
2. **Second loop ($i$)**: Iterate through all elements to the left ($0 \le i < j$).
3. **Branch Pruning**: Evaluate $|arr[i] - arr[j]| \le a$. If false, immediately continue to the next $i$.
4. **Inner loop ($k$)**: Iterate through all elements to the right ($j < k < n$) and verify:
   - $|arr[j] - arr[k]| \le b$
   - $|arr[i] - arr[k]| \le c$
5. Increment the counter whenever all criteria are satisfied.

---

### Complexity Analysis

- **Time Complexity:** 
  - **Worst Case:** $O(N^3)$ when all conditions are satisfied (e.g., $arr$ is filled with identical values and $a, b, c \ge 0$).
  - **Average Case:** Drastically faster due to early pruning at the $i$-$j$ level. For $N = 100$, operations are well under $10^5$, well within Python's typical $\sim 10^7$ ops/sec budget.
- **Space Complexity:** $O(1)$ auxiliary space as we only use a few integer variables.

---

### Common Pitfalls & Mistakes

1. **Checking all conditions in the innermost loop:** Running all 3 conditions inside the $k$-loop without pruning wastes cycles.
2. **Index out-of-bounds / Incorrect ranges:** Mismanaging the triplet order ($i < j < k$). Triplet order is strict; elements cannot be reused or reordered.
3. **Negative differences:** Forgetting to take the absolute value (`abs(x - y)`).

---

### Real Interview Follow-Up Questions

#### 1. What if $N$ scales up to $10^4$ or $10^5$, but element values are bounded $0 \le arr[i] \le M$ (e.g., $M \le 1000$)?
**Answer:** We can optimize the runtime from $O(N^3)$ down to $O(N^2 + N \cdot M)$ or $O(N^2 \log M)$ using a **Prefix Sum / Fenwick Tree (Binary Indexed Tree)**:
- Notice that for a fixed $j$, both $i < j$ and $k > j$ must satisfy:
  - $arr[i] \in [\max(0, arr[j] - a), \min(M, arr[j] + a)]$
  - $arr[k] \in [\max(0, arr[j] - b), \min(M, arr[j] + b)]$
  - $|arr[i] - arr[k]| \le c \implies arr[i] \in [arr[k] - c, arr[k] + c]$
- Thus, for a fixed pair $(j, k)$, valid values for $arr[i]$ lie in the intersection interval:
  $$[\max(0, arr[j] - a, arr[k] - c), \min(M, arr[j] + a, arr[k] + c)]$$
- By maintaining the frequencies of elements seen so far ($0 \le i < j$) in a prefix sum array of size $M + 1$, the count of valid $i$'s can be retrieved in $O(1)$ per $k$.
- Total time complexity: $O(N^2 + N \cdot M)$ and space $O(M)$.

#### 2. How to handle a continuous data stream where elements arrive dynamically?
**Answer:**
- In a stream, new elements act as $k$.
- We can maintain a historical 2D count structure or sliding window frequency map of valid $(i, j)$ pairs.
- If memory is bounded, use an approximate streaming algorithm (e.g., Count-Min Sketch or reservoir sampling) depending on whether an exact count or approximation is required.
