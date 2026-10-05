# 2006. Count Number of Pairs With Absolute Difference K

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/)  
**Topics:** Array, Hash Table, Counting

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `k`, return *the number of pairs* `(i, j)` *where* `i 

The value of `|x|` is defined as:

	- `x` if `x >= 0`.

	- `-x` if `x 

 
Example 1:

```

**Input:** nums = [1,2,2,1], k = 1
**Output:** 4
**Explanation:** The pairs with an absolute difference of 1 are:
- [**1**,**2**,2,1]
- [**1**,2,**2**,1]
- [1,**2**,2,**1**]
- [1,2,**2**,**1**]

```

Example 2:

```

**Input:** nums = [1,3], k = 3
**Output:** 0
**Explanation:** There are no pairs with an absolute difference of 3.

```

Example 3:

```

**Input:** nums = [3,2,1,5,4], k = 2
**Output:** 3
**Explanation:** The pairs with an absolute difference of 2 are:
- [**3**,2,**1**,5,4]
- [**3**,2,1,**5**,4]
- [3,**2**,1,5,**4**]

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from collections import defaultdict

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        """
        Counts the number of pairs (i, j) with i < j such that |nums[i] - nums[j]| == k.
        
        Uses a single-pass hash map approach similar to Two Sum.
        Time Complexity: O(N)
        Space Complexity: O(min(N, M)) where M is the range of values in nums.
        """
        freq = defaultdict(int)
        pair_count = 0
        
        for num in nums:
            # Check how many previous numbers satisfy |num - prev| == k
            # That is, prev == num - k or prev == num + k
            pair_count += freq[num - k] + freq[num + k]
            
            # Record current number's frequency for future pairs
            freq[num] += 1
            
        return pair_count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the number of index pairs $(i, j)$ with $i < j$ such that $|nums[i] - nums[j]| = k$.

A brute-force solution checks all pairs $(i, j)$, running in $O(N^2)$ time. However, this is fundamentally an adaptation of the classic **Two Sum** problem:
For every element $x = nums[j]$, we are looking for earlier elements $nums[i]$ such that:
$$nums[i] = x - k \quad \text{or} \quad nums[i] = x + k$$

By maintaining a running frequency map of elements seen so far as we iterate through `nums`:
1. For each element `num`, we add the count of previously seen occurrences of `num - k` and `num + k` to our total answer.
2. We then increment the count of `num` in our frequency map.
This naturally enforces the constraint $i < j$ without double counting.

---

### Step-by-Step Approach

1. Initialize `freq = defaultdict(int)` to store counts of elements seen so far.
2. Initialize `pair_count = 0`.
3. Loop through each number `num` in `nums`:
   - Add `freq[num - k]` to `pair_count`.
   - Add `freq[num + k]` to `pair_count`.
   - Increment `freq[num]` by 1.
4. Return `pair_count`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
  - We traverse the array of length $N$ once.
  - Hash map lookups and insertions are $\mathcal{O}(1)$ on average.
- **Space Complexity:** $\mathcal{O}(\min(N, U))$
  - Where $U$ is the range of unique values in `nums`.
  - Given the constraint $nums[i] \le 100$, the hash map will hold at most 100 keys, making space effectively $\mathcal{O}(1)$ auxiliary space.

---

### Common Pitfalls / Mistakes candidates make

1. **Double Counting when $k = 0$:**
   - If $k = 0$, `num - k` and `num + k` are identical, leading to double-counting. Although the constraint specifies $k \ge 1$, always clarify or guard against $k = 0$.
2. **Counting with full array frequencies prematurely:**
   - Pre-computing frequencies of the entire array and doing `freq[x] * freq[x + k]` works, but one must be careful to only iterate in one direction (e.g., only check `x + k`, not both `x - k` and `x + k`) to avoid counting each pair twice. The single-pass approach avoids this cleanly.
3. **Using an $O(N^2)$ approach due to small constraints:**
   - While $N \le 200$ passes with $O(N^2)$, top-tier interviewers expect candidates to immediately recognize the $O(N)$ hash map pattern.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if $k = 0$?
- If $k = 0$, we are finding pairs of identical elements.
- In the single-pass loop:
  ```python
  if k == 0:
      pair_count += freq[num]
  else:
      pair_count += freq[num - k] + freq[num + k]
  freq[num] += 1
  ```
- Alternatively, if using global frequencies: for each value, add $\frac{count \times (count - 1)}{2}$.

#### 2. What if the input array is already sorted?
- We can achieve $\mathcal{O}(1)$ auxiliary space using a **Two-Pointer / Sliding Window** technique.
- Maintain two pointers `left` and `right`. Advance `right`, and advance `left` to keep `nums[right] - nums[left] <= k`. When duplicates exist, handle runs of identical elements in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ extra space.

#### 3. What if data arrives as an infinite stream?
- The single-pass algorithm presented is naturally an online algorithm. Each incoming element is processed in $\mathcal{O}(1)$ time against the stateful hash table.
- If memory is bounded, an eviction policy (e.g., sliding window of the last $W$ elements) or a fixed-size frequency array (since $nums[i] \in [1, 100]$) can be used.
