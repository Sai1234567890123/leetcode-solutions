# 2657. Find the Prefix Common Array of Two Arrays

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/)  
**Topics:** Array, Hash Table, Bit Manipulation

---

## 📝 Problem Statement

You are given two **0-indexed **integer** **permutations `A` and `B` of length `n`.

A **prefix common array** of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.

Return *the **prefix common array** of *`A`* and *`B`.

A sequence of `n` integers is called a **permutation** if it contains all integers from `1` to `n` exactly once.

 
Example 1:

```

**Input:** A = [1,3,2,4], B = [3,1,2,4]
**Output:** [0,2,3,4]
**Explanation:** At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

```

Example 2:

```

**Input:** A = [2,3,1], B = [3,1,2]
**Output:** [0,1,3]
**Explanation:** At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        # Since numbers are from 1 to n, size n + 1 is sufficient.
        freq = [0] * (n + 1)
        common_count = 0

        for i in range(n):
            # Process element from array A
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1

            # Process element from array B
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1

            ans[i] = common_count

        return ans
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires us to determine the count of common elements between the prefixes $A[0 \dots i]$ and $B[0 \dots i]$ for every index $i \in [0, n - 1]$.

A naive approach would compare sets of elements in $A[0 \dots i]$ and $B[0 \dots i]$ at each step $i$, yielding an $O(n^2)$ time complexity. However, we are given a key constraint: **both $A$ and $B$ are permutations of integers from $1$ to $n$**.

Because each number appears at most once in $A$ and at most once in $B$:
- Any number can appear at most twice in total across the combined prefixes $A[0 \dots i]$ and $B[0 \dots i]$.
- A number belongs to the intersection of the two prefixes if and only if it has been encountered in both arrays—meaning its combined frequency reaches exactly `2`.

By maintaining a running frequency array and a counter of elements with frequency equal to 2, we can compute each prefix count incrementally in $O(1)$ time per index.

---

### Step-by-Step Approach

1. Initialize a frequency array `freq` of size $n + 1$ with zeros (since values are 1-indexed from $1$ to $n$).
2. Initialize `common_count = 0` and an output array `ans` of length $n$.
3. Iterate $i$ from $0$ to $n - 1$:
   - Increment `freq[A[i]]`. If `freq[A[i]] == 2`, increment `common_count`.
   - Increment `freq[B[i]]`. If `freq[B[i]] == 2`, increment `common_count`.
   - Assign `ans[i] = common_count`.
4. Return `ans`.

---

### Complexity Analysis

- **Time Complexity:** $O(n)$
  We iterate through the arrays of length $n$ once. In each iteration, array lookups and increments run in $O(1)$ time. Thus, the total time is strictly linear.
- **Space Complexity:** $O(n)$
  We use an auxiliary frequency array of size $n + 1$. The output array `ans` takes $O(n)$ space, which is required for the return value.
  *(Note: Since $n \le 50$, this can also be solved using a 64-bit bitmask in $O(1)$ auxiliary space).*

---

### Common Pitfalls / Mistakes

1. **Recomputing intersections from scratch ($O(n^2)$):** Converting slices `set(A[:i+1]) & set(B[:i+1])` at each step results in redundant work and sub-optimal $O(n^2)$ time.
2. **Off-by-one errors:** The values in $A$ and $B$ are $1$-indexed (range $1$ to $n$). Sizing the frequency array to $n$ instead of $n + 1$ causes an `IndexError`.
3. **Double counting when $A[i] == B[i]$:** If $A[i] = B[i]$, the frequency jumps from 0 to 2 in the same iteration. Processing $A[i]$ first (freq becomes 1) and $B[i]$ second (freq becomes 2) correctly increments `common_count` exactly once.

---

### Real Interview Follow-Up Questions

#### 1. What if memory is extremely constrained? Can we achieve $O(1)$ auxiliary space?
**Answer:** Yes. Since $n \le 50$ (or generally $n \le 64$), we can use bit manipulation. 
- Maintain two bitmasks: `mask_A` and `mask_B`.
- At step $i$, set the $k$-th bit: `mask_A |= (1 << A[i])` and `mask_B |= (1 << B[i])`.
- The common count at step $i$ is simply the population count of the bitwise AND: `bin(mask_A & mask_B).count("1")` or `(mask_A & mask_B).bit_count()`.

#### 2. What if $A$ and $B$ are not permutations and can contain duplicate values?
**Answer:** If arrays contain duplicates, the frequency criterion changes. A number is in the common intersection if its count in both prefixes is at least 1 (or $\min(\text{count}_A, \text{count}_B)$ for multiset intersection).
- If tracking unique common elements: Maintain two boolean arrays / hash sets `seen_A` and `seen_B`. When $A[i]$ appears for the first time in $A$, check if it's already in `seen_B`.
- If tracking multiset intersection: Maintain separate counts `count_A` and `count_B`. When $A[i]$ is processed, if `count_A[A[i]] <= count_B[A[i]]`, increment the common count.

#### 3. How would you handle a streaming / distributed scenario?
**Answer:** If $A$ and $B$ are streams of data arriving concurrently:
- We can publish incoming numbers to a message broker (e.g., Kafka) keyed by their value.
- An in-memory distributed cache (like Redis) or stateful stream processing engine (like Apache Flink) maintains the state per value.
- When an event causes a key to exist in both partitions/streams up to a timestamp, an output event is emitted.
