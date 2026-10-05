# 1630. Arithmetic Subarrays

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/arithmetic-subarrays/](https://leetcode.com/problems/arithmetic-subarrays/)  
**Topics:** Array, Hash Table, Sorting

---

## 📝 Problem Statement

A sequence of numbers is called **arithmetic** if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence `s` is arithmetic if and only if `s[i+1] - s[i] == s[1] - s[0] `for all valid `i`.

For example, these are **arithmetic** sequences:

```

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```

The following sequence is not **arithmetic**:

```

1, 1, 2, 5, 7
```

You are given an array of `n` integers, `nums`, and two arrays of `m` integers each, `l` and `r`, representing the `m` range queries, where the `ith` query is the range `[l[i], r[i]]`. All the arrays are **0-indexed**.

Return *a list of *`boolean` *elements* `answer`*, where* `answer[i]` *is* `true` *if the subarray* `nums[l[i]], nums[l[i]+1], ... , nums[r[i]]`* can be **rearranged** to form an **arithmetic** sequence, and* `false` *otherwise.*

 
Example 1:

```

**Input:** nums = `[4,6,5,9,3,7]`, l = `[0,0,2]`, r = `[2,3,5]`
**Output:** `[true,false,true]`
**Explanation:**
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is `[5,9,3,7]. This` can be rearranged as `[3,5,7,9]`, which is an arithmetic sequence.
```

Example 2:

```

**Input:** nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
**Output:** [false,true,false,false,true,true]

```

 
**Constraints:**

	- `n == nums.length`

	- `m == l.length`

	- `m == r.length`

	- `2 5 5`

---

## 💻 Implementation (python3)

```py
class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        """
        Determines for each query [left, right] if nums[left...right] can be rearranged
        into an arithmetic progression.
        
        Optimized to O(k) per query without sorting, yielding O(m * n) overall time complexity.
        """
        def is_arithmetic(left: int, right: int) -> bool:
            k = right - left + 1
            if k <= 2:
                # Any sequence of length <= 2 is trivially an arithmetic progression
                return True

            min_val = float('inf')
            max_val = float('-inf')

            for i in range(left, right + 1):
                val = nums[i]
                if val < min_val:
                    min_val = val
                if val > max_val:
                    max_val = val

            # Case 1: All elements must be identical (common difference is 0)
            if min_val == max_val:
                return True

            # Case 2: The span (max - min) must be evenly divisible by (k - 1)
            total_diff = max_val - min_val
            if total_diff % (k - 1) != 0:
                return False

            diff = total_diff // (k - 1)

            # Track visited progression indices to detect duplicates or invalid steps
            seen = [False] * k
            for i in range(left, right + 1):
                val = nums[i]
                offset = val - min_val

                # Must be a multiple of the common difference
                if offset % diff != 0:
                    return False

                step_idx = offset // diff
                # Check for bounds and duplicates
                if step_idx >= k or seen[step_idx]:
                    return False

                seen[step_idx] = True

            return True

        return [is_arithmetic(left, right) for left, right in zip(l, r)]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

An arithmetic sequence of length $k$ has the property that its sorted elements satisfy:
$$a_j = a_0 + j \cdot d \quad \text{for } j \in [0, k-1]$$
where $d$ is the common difference.

A naive approach is to copy each subarray of length $k = r[i] - l[i] + 1$, sort it in $O(k \log k)$ time, and verify that all consecutive differences are equal. Across $m$ queries, this gives $O(m \cdot n \log n)$ time.

We can optimize this to **$O(k)$ per query** without sorting:
1. Find $\min$ and $\max$ in the subarray.
2. If $\min == \max$, all elements in the subarray must be equal; thus, it is a valid arithmetic progression with $d = 0$.
3. Otherwise, the common difference must be:
   $$d = \frac{\max - \min}{k - 1}$$
   If $(\max - \min) \pmod{k - 1} \neq 0$, it is impossible to form an arithmetic sequence.
4. If divisible, we verify that every element $x$ in the subarray satisfies:
   - $(x - \min) \pmod d == 0$
   - Each index $j = (x - \min) / d$ is unique (no duplicate values in a non-zero progression). We can track this using a boolean array `seen` of size $k$.

### Step-by-Step Approach

1. Iterate over each query `(left, right)`.
2. Compute $k = \text{right} - \text{left} + 1$. Subarrays of size $\le 2$ are trivially arithmetic.
3. Compute the minimum and maximum values of the subarray in a single pass.
4. Handle the edge case where $\min = \max$ ($d = 0$).
5. Check if $(\max - \min)$ is divisible by $k - 1$. If not, return `False`.
6. Allocate a boolean array `seen` of size $k$.
7. In a second pass over the subarray, compute the expected index `(val - min) // diff`. If it's not an exact multiple or already visited, return `False`.
8. If all checks pass, return `True`.

### Complexity Analysis

- **Time Complexity:** 
  - Per query: $O(k)$ where $k = r[i] - l[i] + 1 \le n$. We do two linear scans over the subarray and perform $O(1)$ operations per element.
  - Overall Time: $\mathcal{O}(m \cdot n)$, where $m$ is the number of queries and $n$ is the length of `nums`. This is asymptotically optimal as no sorting is required.
- **Space Complexity:** 
  - Auxiliary space per query is $\mathcal{O}(k) \le \mathcal{O}(n)$ for the `seen` array.
  - Overall auxiliary space: $\mathcal{O}(n)$ (excluding the $\mathcal{O}(m)$ space needed to store the output array).

### Common Pitfalls / Mistakes

1. **Division by Zero:** Attempting to compute $d = (\max - \min) / (k - 1)$ when $\max == \min$ causes zero division or issues if modulo is checked without guarding.
2. **Duplicate Elements:** Failing to verify that each index $(x - \min) // d$ appears only once. For instance, `[0, 0, 2]` has $\min=0, \max=2, k=3 \implies d=1$. Both zeros map to index 0. Without duplicate checking, an algorithm could falsely mark this valid.
3. **Overusing Hash Sets:** In Python, creating a `set(nums[left:right+1])` and checking elements takes additional hashing overhead. A boolean array of size $k$ is faster, cache-friendly, and handles duplicates seamlessly.

### Real Interview Follow-Up Questions

#### 1. What if there are massive numbers of queries ($m \gg n$)? Can we precompute?
- **Answer:** If $m \sim 10^5$ and $n \sim 10^5$, $O(m \cdot n)$ is too slow.
  - Note that for a subarray to be arithmetic *in its original order*, adjacent differences must be identical, which can be queried in $O(1)$ using prefix sums of differences.
  - However, because rearranging is permitted, arbitrary range queries are harder. If queries are static, we can use **Mo's Algorithm** with an active frequency map and min/max tracking, or range data structures (like Segment Trees maintaining sum, sum of squares, min, max, and GCD of differences). A hash-based polynomial identity or checking $\sum x$, $\sum x^2$, min, max, and distinct count can achieve $O(\log n)$ or $O(1)$ per query via prefix structures.

#### 2. What if $nums$ is an unbounded stream of numbers and queries arrive dynamically?
- **Answer:** Since queries span a sliding window or arbitrary historical ranges, we can maintain the stream in blocks (Square Root Decomposition) or a persistent Segment Tree. Each segment tree node stores min, max, and a rolling polynomial hash of the multiset of differences, allowing validation in $O(\log n)$ time.

#### 3. How do we handle duplicate values when $d \neq 0$?
- **Answer:** If $d \neq 0$, any duplicate immediately renders the sequence non-arithmetic because an arithmetic progression of length $k$ with $d > 0$ has $k$ strictly distinct values. Using the boolean array `seen[step_idx]` immediately flags duplicates in $O(1)$ time.
