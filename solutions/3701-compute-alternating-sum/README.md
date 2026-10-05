# 3701. Compute Alternating Sum

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/compute-alternating-sum/](https://leetcode.com/problems/compute-alternating-sum/)  
**Topics:** Array, Simulation

---

## 📝 Problem Statement

You are given an integer array `nums`.

The **alternating sum** of `nums` is the value obtained by **adding** elements at even indices and **subtracting** elements at odd indices. That is, `nums[0] - nums[1] + nums[2] - nums[3]...`

Return an integer denoting the alternating sum of `nums`.

 
Example 1:

**Input:** nums = [1,3,5,7]

**Output:** -4

**Explanation:**

	- Elements at even indices are `nums[0] = 1` and `nums[2] = 5` because 0 and 2 are even numbers.

	- Elements at odd indices are `nums[1] = 3` and `nums[3] = 7` because 1 and 3 are odd numbers.

	- The alternating sum is `nums[0] - nums[1] + nums[2] - nums[3] = 1 - 3 + 5 - 7 = -4`.

Example 2:

**Input:** nums = [100]

**Output:** 100

**Explanation:**

	- The only element at even indices is `nums[0] = 100` because 0 is an even number.

	- There are no elements on odd indices.

	- The alternating sum is `nums[0] = 100`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        """
        Computes the alternating sum: nums[0] - nums[1] + nums[2] - nums[3] + ...
        
        Runs in O(N) time and O(1) auxiliary space.
        """
        total = 0
        sign = 1
        
        for num in nums:
            total += sign * num
            # Alternate sign: positive for even index, negative for odd index
            sign = -sign
            
        return total
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the alternating sum of an array `nums`, defined as:
$$\text{Alternating Sum} = nums[0] - nums[1] + nums[2] - nums[3] + \dots$$

Every element at an even index ($0, 2, 4, \dots$) is added, and every element at an odd index ($1, 3, 5, \dots$) is subtracted. 

Instead of slicing the array (`sum(nums[::2]) - sum(nums[1::2])`), which creates intermediate sublists and incurs $O(N)$ auxiliary space, we can iterate through `nums` in a single pass while toggling a multiplier sign (`+1` and `-1`). This achieves optimal $O(N)$ time and strictly $O(1)$ space.

### Step-by-Step Approach

1. Initialize `total = 0` to accumulate the result.
2. Maintain a `sign = 1` variable.
3. For each number `num` in `nums`:
   - Add `sign * num` to `total`.
   - Negate `sign` (`sign = -sign`) so the next element receives the inverted operation.
4. Return `total`.

### Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the length of `nums`. We process each element exactly once in a single sequential pass.
- **Space Complexity:** $O(1)$ auxiliary space. Only a couple of scalar variables (`total`, `sign`) are allocated.

### Common Pitfalls / Mistakes

1. **Memory Allocation via Slicing:** Writing `sum(nums[::2]) - sum(nums[1::2])` in Python creates two new arrays of size $\approx N/2$, taking $O(N)$ additional memory. In performance-critical or memory-constrained scenarios, an in-place single-pass traversal is preferred.
2. **Integer Overflow (in other languages):** While Python handles arbitrarily large integers automatically, in languages like C++ or Java, the alternating sum could potentially exceed 32-bit signed integer limits if elements or lengths are very large. In such languages, check constraints and use 64-bit integers (`long` / `long long`) if needed.
3. **0-based vs 1-based indexing confusion:** The problem specifies `nums[0]` is added (even index). Confusing $0$-th element with "first element" (1-based odd) can cause sign inversion.

### Real Interview Follow-Up Questions

#### 1. What if the input array is an infinite data stream?
- **Answer:** The single-pass accumulator algorithm maps directly to streaming data. We maintain `total` and `sign` across incoming elements without buffering any previous elements, using $O(1)$ memory.

#### 2. What if we are asked to answer range queries $[L, R]$ of alternating sums dynamically with updates?
- **Answer:** This can be solved using a **Fenwick Tree (Binary Indexed Tree)** or a **Segment Tree**. Store the value of each element as $nums[i]$ if $i$ is even, and $-nums[i]$ if $i$ is odd. 
  - A query on range $[L, R]$ is:
    $$\text{sum}(L, R) = \sum_{i=L}^R (-1)^i \cdot nums[i]$$
  - If $L$ is odd, we multiply the range query result by $-1$ to ensure the first element in the range starts with a positive sign.
  - Range queries and point updates take $O(\log N)$ time.

#### 3. How would you parallelize this for massive datasets (e.g., Terabytes in distributed systems / MapReduce)?
- **Answer:** 
  - Each worker node processes a contiguous chunk of size $K$ starting at global offset $i_{start}$.
  - The worker computes the sum with signs relative to the global indices: $(-1)^i \cdot nums[i]$.
  - The master node simply sums the partial results from all workers. Since addition is associative and commutative, this parallelizes seamlessly.
