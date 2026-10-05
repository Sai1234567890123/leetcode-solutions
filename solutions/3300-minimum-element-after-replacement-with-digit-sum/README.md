# 3300. Minimum Element After Replacement With Digit Sum

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/)  
**Topics:** Array, Math

---

## 📝 Problem Statement

You are given an integer array `nums`.

You replace each element in `nums` with the **sum** of its digits.

Return the **minimum** element in `nums` after all replacements.

 
Example 1:

**Input:** nums = [10,12,13,14]

**Output:** 1

**Explanation:**

`nums` becomes `[1, 3, 4, 5]` after all replacements, with minimum element 1.

Example 2:

**Input:** nums = [1,2,3,4]

**Output:** 1

**Explanation:**

`nums` becomes `[1, 2, 3, 4]` after all replacements, with minimum element 1.

Example 3:

**Input:** nums = [999,19,199]

**Output:** 10

**Explanation:**

`nums` becomes `[27, 10, 19]` after all replacements, with minimum element 10.

 
**Constraints:**

	- `1 4`

---

## 💻 Implementation (python3)

```py
class Solution:
    def minElement(self, nums: list[int]) -> int:
        """
        Calculates the minimum element after replacing each number with its digit sum.
        Time Complexity: O(N * D) where N is the length of nums and D is the max digits (~5).
        Space Complexity: O(1) auxiliary space.
        """
        min_sum = float('inf')
        
        for num in nums:
            digit_sum = 0
            curr = num
            # Extract digits arithmetically to avoid string conversion overhead
            while curr > 0:
                digit_sum += curr % 10
                curr //= 10
            
            if digit_sum < min_sum:
                min_sum = digit_sum
                # Optimization: 1 is the theoretical minimum digit sum for any positive integer
                if min_sum == 1:
                    return 1
                    
        return min_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires us to transform each integer in the array into the sum of its decimal digits and return the smallest resulting value. 

Instead of modifying the array in-place or creating an intermediate array of transformed values, we can maintain a running minimum. As we process each number, we compute its digit sum and update the minimum. 

Since all numbers are positive integers ($nums[i] \ge 1$), the minimum possible sum of digits is `1` (achieved by powers of 10: 1, 10, 100, etc.). We can apply an early-exit optimization: if we ever encounter a digit sum of `1`, we can immediately return `1` without processing the remainder of the array.

### Step-by-Step Approach

1. Initialize `min_sum` to infinity (`float('inf')`).
2. Iterate through each integer `num` in `nums`:
   - Compute the sum of digits arithmetically using `digit_sum += curr % 10` and `curr //= 10` until `curr` becomes 0.
   - Update `min_sum = min(min_sum, digit_sum)`.
   - Check if `min_sum == 1`. If true, return `1` immediately.
3. Return `min_sum` after the loop terminates.

### Complexity Analysis

- **Time Complexity:** $O(N \cdot D)$, where $N$ is the number of elements in `nums` and $D$ is the maximum number of digits per element. With $nums[i] \le 10^4$, $D \le 5$, meaning $D$ is a small constant ($O(1)$). Thus, the effective time complexity is $O(N)$, which is optimal as every element must be inspected at least once in the worst case.
- **Space Complexity:** $O(1)$ auxiliary space. We only use a few integer variables (`min_sum`, `digit_sum`, `curr`), requiring no extra memory allocation.

### Common Pitfalls / Mistakes

- **String Conversion Overhead:** Using `sum(int(d) for d in str(num))` is functionally correct in Python, but allocates string and iterator objects in each iteration. Arithmetic extraction (`% 10` and `// 10`) is faster and adheres to lower-level production-grade standards.
- **Forgetting Edge Cases for 0:** While constraints specify $nums[i] \ge 1$, if $0$ were allowed, a standard `while curr > 0` would yield `digit_sum = 0`, which is correct, but candidates often overlook handling 0 if negative numbers or 0 are introduced.
- **Unnecessary Array Allocation:** Using `min(sum(int(d) for d in str(x)) for x in nums)` is clean in Python, but creates generator expressions and avoids early pruning optimizations.

### Real Interview Follow-Up Questions

#### 1. What if the input array is an unbounded stream of integers?
**Answer:** The current solution already operates in a streaming fashion. We can maintain `min_sum` in $O(1)$ state. For every incoming integer, compute its digit sum and update `min_sum`. If `min_sum` hits 1, we can either signal completion early or maintain 1 as an invariant minimum.

#### 2. What if $nums[i]$ can be as large as a 64-bit integer ($10^{18}$)?
**Answer:** The approach remains identical. The number of digits $D$ increases from 5 to at most 19, which is still trivial for the $O(\log_{10}(\text{num}))$ arithmetic extraction loop. No integer overflow issues occur because digit sums for 64-bit integers cannot exceed $19 \times 9 = 171$.

#### 3. How would you parallelize this across multiple CPU cores or distributed machines?
**Answer:** The digit sum operation is a map-reduce problem. 
- **Map:** Partition the array into chunks across threads/workers. Each worker computes the minimum digit sum for its partition.
- **Reduce:** Find the global minimum across the worker results. An atomic flag can be set if any worker encounters `1`, allowing other workers to abort computation early.
