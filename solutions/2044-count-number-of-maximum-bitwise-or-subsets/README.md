# 2044. Count Number of Maximum Bitwise-OR Subsets

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)  
**Topics:** Array, Backtracking, Bit Manipulation, Enumeration

---

## 📝 Problem Statement

Given an integer array `nums`, find the **maximum** possible **bitwise OR** of a subset of `nums` and return *the **number of different non-empty subsets** with the maximum bitwise OR*.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`. Two subsets are considered **different** if the indices of the elements chosen are different.

The bitwise OR of an array `a` is equal to `a[0] **OR** a[1] **OR** ... **OR** a[a.length - 1]` (**0-indexed**).

 
Example 1:

```

**Input:** nums = [3,1]
**Output:** 2
**Explanation:** The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]

```

Example 2:

```

**Input:** nums = [2,2,2]
**Output:** 7
**Explanation:** All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.

```

Example 3:

```

**Input:** nums = [3,2,1,5]
**Output:** 6
**Explanation:** The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
```

 
**Constraints:**

	- `1 5`

---

## 💻 Implementation (python3)

```py
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        # The bitwise OR operation is monotonically non-decreasing.
        # Therefore, the maximum possible OR value is the OR of all elements.
        max_or = 0
        for num in nums:
            max_or |= num

        n = len(nums)

        def dfs(index: int, current_or: int) -> int:
            # Pruning optimization:
            # If the current OR has already reached max_or, adding any combination
            # of the remaining elements will still result in max_or.
            # There are (n - index) remaining elements, so there are 2^(n - index) such subsets.
            if current_or == max_or:
                return 1 << (n - index)

            # Base case: reached the end without achieving max_or
            if index == n:
                return 0

            # Branch 1: Include nums[index]
            include = dfs(index + 1, current_or | nums[index])
            # Branch 2: Exclude nums[index]
            exclude = dfs(index + 1, current_or)

            return include + exclude

        return dfs(0, 0)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

1. **Monotonicity of Bitwise OR**:
   For any two non-negative integers $a$ and $b$, $a \mid b \ge a$ and $a \mid b \ge b$. Since adding elements via bitwise OR can only set new bits (never clear existing ones), the maximum possible bitwise OR across any subset is always achieved by taking the bitwise OR of **all** elements in the array.
   
2. **Search & Pruning (Subtree Skipping)**:
   Given $n \le 16$, the total number of subsets is $2^{16} = 65,536$. A brute-force traversal over all subsets is very fast, but we can optimize it significantly:
   - If the current subset's bitwise OR reaches `max_or` at element index $i$, **any** choice we make for the remaining $(n - i)$ elements will keep the bitwise OR equal to `max_or`.
   - Therefore, there is no need to recurse further; we can directly count all $2^{n - i}$ configurations branching from this node and prune the subtree.

---

### Step-by-Step Approach

1. **Calculate Maximum OR**: Compute the bitwise OR of all numbers in `nums`, storing it in `max_or`.
2. **Backtracking DFS**:
   - Define a recursive helper function `dfs(index, current_or)`.
   - **Pruning Check**: If `current_or == max_or`, return $2^{n - \text{index}}$ (using bit shift `1 << (n - index)`).
   - **Base Case**: If `index == n`, return $0$ (the subset did not achieve `max_or`).
   - **Transitions**:
     - Include current element: `dfs(index + 1, current_or | nums[index])`
     - Exclude current element: `dfs(index + 1, current_or)`
   - Return the sum of both branches.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(2^n)$ in the worst-case scenario where the maximum OR is only achieved by the full set. However, with the early-stopping pruning optimization, the effective search tree is drastically pruned, running in $\ll 2^n$ steps on average and taking well under a millisecond for $n = 16$.
- **Space Complexity**: $\mathcal{O}(n)$ due to the recursion call stack, which reaches a maximum depth of $n \le 16$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Recomputing the Maximum**: Trying to dynamically track the maximum OR across subsets rather than pre-computing the full array's OR in $\mathcal{O}(n)$ first.
2. **Missing the Pruning Optimization**: Exploring all $2^n$ leaves even after reaching `max_or`. While $n=16$ passes brute-force, demonstrating the $2^{n - \text{index}}$ mathematical jump showcases strong competitive programming and algorithmic maturity.
3. **Double Counting Empty Subsets**: Since $nums[i] \ge 1$, the empty set yields an OR of $0$, which cannot equal `max_or` unless `max_or == 0` (impossible under constraints $nums[i] \ge 1$).

---

### Real Interview Follow-Up Questions

#### 1. What if $N$ is up to 40?
- **Answer**: $2^{40} \approx 10^{12}$, which is too large for plain recursion. We can use a **Meet-in-the-Middle** approach:
  - Split the array into two halves of size $\le 20$.
  - Generate all $2^{20}$ OR values and their frequencies for both halves.
  - Since bitwise OR has at most $\approx 2^{17} \approx 131,072$ unique values (given constraints on values), we can combine counts using Fast Walsh-Hadamard Transform (FWHT) or SOS (Sum Over Subsets) DP.

#### 2. What if $N$ is very large (e.g., $10^5$), but $nums[i] < 2^{16}$?
- **Answer**: Use Dynamic Programming.
  - Let `dp[mask]` be the number of subsets having bitwise OR equal to `mask`.
  - Iterate through elements, updating the frequency table `dp` of achievable masks.
  - Total time complexity: $\mathcal{O}(N + U \cdot \log U)$ using FWHT/SOS DP or $\mathcal{O}(N \cdot \text{distinct masks})$.

#### 3. How would you handle a streaming input of numbers?
- **Answer**:
  - Maintain the frequency of bits set at each position across the stream.
  - If a new number introduces new set bits, `max_or` increases, invalidating previous subset counts. If `max_or` doesn't change, we can incrementally update subset counts using a mask DP table in memory.
