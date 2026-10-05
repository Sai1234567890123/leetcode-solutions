# 1464. Maximum Product of Two Elements in an Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)  
**Topics:** Array, Sorting, Heap (Priority Queue)

---

## 📝 Problem Statement

You are given an array of integers `nums`.

Choose two **different** indices `i` and `j` of that array.

Return the **maximum** value of `(nums[i] - 1) * (nums[j] - 1)`.

 
Example 1:

```

**Input:** nums = [3,4,5,2]
**Output:** 12 
**Explanation:** If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

```

Example 2:

```

**Input:** nums = [1,5,4,5]
**Output:** 16
**Explanation:** Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

```

Example 3:

```

**Input:** nums = [3,7]
**Output:** 12

```

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Finds the maximum value of (nums[i] - 1) * (nums[j] - 1) for two distinct indices i and j.
        Since all nums[i] >= 1, maximizing this expression is equivalent to finding 
        the two largest elements in the array.
        """
        max1 = 0
        max2 = 0
        
        for num in nums:
            if num > max1:
                # num is strictly greater than the current largest.
                # The old largest is now the second largest.
                max2 = max1
                max1 = num
            elif num > max2:
                # num is between max1 and max2 (or equal to max1).
                # Update max2 accordingly.
                max2 = num
                
        return (max1 - 1) * (max2 - 1)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to maximize the expression $(nums[i] - 1) \times (nums[j] - 1)$ for two distinct indices $i$ and $j$. 

Given the constraints that $nums[i] \ge 1$ for all elements:
1. Every term $(nums[k] - 1)$ is non-negative ($\ge 0$).
2. The product of two non-negative terms is maximized when the two individual terms are maximized.
3. Therefore, the problem reduces directly to finding the **two largest elements** in `nums`.

While sorting the array takes $O(n \log n)$ time, we can find the two largest elements in a single pass of $O(n)$ time using two variables (`max1` and `max2`) and $O(1)$ auxiliary space.

---

### Step-by-Step Approach

1. Initialize two variables `max1 = 0` and `max2 = 0` to store the largest and second-largest elements encountered so far. (Using `0` as the initial value is safe since $nums[i] \ge 1$).
2. Iterate through each number `num` in `nums`:
   - If `num > max1`: The current number is larger than our top candidate. Demote `max1` to `max2` and update `max1 = num`.
   - Else if `num > max2`: The current number is not strictly greater than `max1`, but it is greater than `max2` (this naturally handles cases where duplicates of the largest number appear, e.g., `[5, 5]`). Update `max2 = num`.
3. After the loop, return `(max1 - 1) * (max2 - 1)`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `nums`. We traverse the array exactly once, performing constant-time comparisons and assignments at each step.
- **Space Complexity:** $\mathcal{O}(1)$. Only two scalar variables (`max1` and `max2`) are maintained, requiring constant auxiliary memory.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Sorting Overhead:** Sorting the array with `nums.sort()` costs $\mathcal{O}(n \log n)$ time and mutates the input array (or costs $\mathcal{O}(n)$ space if using `sorted()`). While acceptable on LeetCode for $N \le 500$, in a Meta/Google interview, an interviewer will immediately ask for an optimal $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ space solution.
2. **Handling Duplicates Incorrectly:** A common mistake in the two-pointer/two-variable search is using `elif num > max2 and num != max1`. Doing so causes arrays like `[5, 5]` to fail because the second `5` would be ignored, leaving `max2` as `0`.
3. **Negative Numbers Assumption:** If constraints allowed negative numbers, the product could also be maximized by the two smallest (most negative) numbers. While the problem guarantees $nums[i] \ge 1$, explicitly clarifying or mentioning this to the interviewer demonstrates senior-level rigor.

---

### Real Interview Follow-Up Questions

#### 1. What if the array contains negative numbers?
- **Answer:** If $nums[i]$ can be negative, $(nums[i] - 1)$ can be negative. A large positive product could also result from the product of the two *smallest* (most negative) elements. We would track the top two maximums (`max1`, `max2`) AND the bottom two minimums (`min1`, `min2`) in a single pass and return $\max((max1 - 1)(max2 - 1), (min1 - 1)(min2 - 1))$.

#### 2. What if the input arrives as an infinite data stream?
- **Answer:** The two-variable single-pass solution natively supports streaming data. For each incoming number, we update `max1` and `max2` in $\mathcal{O}(1)$ time without needing to store past values, maintaining $\mathcal{O}(1)$ memory.

#### 3. How would you generalize this to finding the product of the top $k$ elements?
- **Answer:** Use a min-heap of size $k$. For each incoming element, push it onto the heap; if the heap exceeds size $k$, pop the smallest element. At the end, the heap contains the $k$ largest elements.
  - **Time Complexity:** $\mathcal{O}(n \log k)$.
  - **Space Complexity:** $\mathcal{O}(k)$.
