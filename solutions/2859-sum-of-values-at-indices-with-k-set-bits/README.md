# 2859. Sum of Values at Indices With K Set Bits

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/](https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/)  
**Topics:** Array, Bit Manipulation

---

## 📝 Problem Statement

You are given a **0-indexed** integer array `nums` and an integer `k`.

Return *an integer that denotes the **sum** of elements in *`nums`* whose corresponding **indices** have **exactly** *`k`* set bits in their binary representation.*

The **set bits** in an integer are the `1`'s present when it is written in binary.

	- For example, the binary representation of `21` is `10101`, which has `3` set bits.

 
Example 1:

```

**Input:** nums = [5,10,1,5,2], k = 1
**Output:** 13
**Explanation:** The binary representation of the indices are: 
0 = 0002
1 = 0012
2 = 0102
3 = 0112
4 = 1002 
Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
Hence, the answer is nums[1] + nums[2] + nums[4] = 13.
```

Example 2:

```

**Input:** nums = [4,3,2,1], k = 2
**Output:** 1
**Explanation:** The binary representation of the indices are:
0 = 002
1 = 012
2 = 102
3 = 112
Only index 3 has k = 2 set bits in its binary representation.
Hence, the answer is nums[3] = 1.

```

 
**Constraints:**

	- `1 5`

	- `0

---

## 💻 Implementation (python3)

```py
class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        """
        Calculates the sum of elements at indices that have exactly k set bits.
        """
        total_sum = 0
        for i, val in enumerate(nums):
            # int.bit_count() is introduced in Python 3.10 and runs in O(1) time
            # utilizing hardware POPCNT instructions where available.
            if i.bit_count() == k:
                total_sum += val
                
        return total_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem requires us to iterate over the given array `nums` and identify indices `i` whose binary representation contains exactly `k` set bits (`1`s). For every such index, we accumulate `nums[i]` into a running total.

Counting the number of set bits in an integer is commonly known as the **Hamming Weight** or **popcount** operation. In Python 3.10+, `int.bit_count()` performs this operation efficiently, translating directly to low-level hardware instructions (like `POPCNT` on x86/x64 architectures).

### Step-by-Step Approach
1. Initialize an accumulator variable `total_sum = 0`.
2. Iterate through `nums` using `enumerate` to access both index `i` and value `val`.
3. Check if `i.bit_count() == k`:
   - If true, add `val` to `total_sum`.
4. Return `total_sum`.

### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of `nums`.
  - We visit each index from $0$ to $N - 1$ once.
  - For each index $i < N$, counting its set bits takes $\mathcal{O}(\log(\text{max\_index})) = \mathcal{O}(1)$ time since standard integers are bounded (e.g., at most 32 bits or 64 bits).
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.
  - Only a single accumulator variable `total_sum` is maintained.

### Common Pitfalls / Mistakes Candidates Make
1. **Misreading the Problem:** Counting the set bits of the values (`nums[i]`) rather than the indices (`i`).
2. **Inefficient Bit Counting:** Converting index to string using `bin(i).count('1')`. While this passes for small constraints, string allocations inside a hot loop add overhead. `i.bit_count()` or Brian Kernighan’s algorithm (`i &= (i - 1)`) is much cleaner and faster.
3. **Integer Overflow:** In languages like C++ or Java, sum can overflow if constraints allow large sums (use `long` / `int64_t` if necessary). In Python, integers have arbitrary precision, so overflow is not an issue.

### Real Interview Follow-Up Questions & Answers

#### 1. What if $N$ is massive (e.g., $N = 10^9$) and $k$ is small, but `nums` is given as a function or sparse generator?
**Answer:** Instead of scanning all $N$ indices and filtering by $k$ bits, we can directly generate numbers with exactly $k$ set bits in ascending order using Gosper's Hack:
```python
def next_combination(x: int) -> int:
    lowest_bit = x & -x
    left_bits = x + lowest_bit
    changed_bits = x ^ left_bits
    right_bits = (changed_bits >> 2) // lowest_bit
    return left_bits | right_bits
```
This iterates strictly through the valid indices in $\mathcal{O}\left(\binom{B}{k}\right)$ time where $B \approx \log_2(N)$, skipping all indices that do not have $k$ set bits.

#### 2. How would you handle a streaming dataset where elements arrive continuously?
**Answer:** Maintain a counter for the current index `stream_index`. Whenever a new element arrives, check `stream_index.bit_count() == k`, add to total, and increment `stream_index`. This processes each element in $\mathcal{O}(1)$ time and $\mathcal{O}(1)$ memory.

#### 3. How would you parallelize this across multiple cores / distributed workers?
**Answer:** Since each index evaluation and lookup is independent, we can divide the index range $[0, N-1]$ into $P$ contiguous chunks (Map step). Each worker computes the local sum for its assigned chunk. A single aggregation step (Reduce) sums the results from all workers.
