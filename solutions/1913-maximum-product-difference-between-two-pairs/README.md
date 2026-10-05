# 1913. Maximum Product Difference Between Two Pairs

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/maximum-product-difference-between-two-pairs/](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/)  
**Topics:** Array, Sorting, Quicksort

---

## 📝 Problem Statement

The **product difference** between two pairs `(a, b)` and `(c, d)` is defined as `(a * b) - (c * d)`.


	- For example, the product difference between `(5, 6)` and `(2, 7)` is `(5 * 6) - (2 * 7) = 16`.



Given an integer array `nums`, choose four **distinct** indices `w`, `x`, `y`, and `z` such that the **product difference** between pairs `(nums[w], nums[x])` and `(nums[y], nums[z])` is **maximized**.

Return *the **maximum** such product difference*.

 
Example 1:

```

**Input:** nums = [5,6,2,7,4]
**Output:** 34
**Explanation:** We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.

```

Example 2:

```

**Input:** nums = [4,2,5,9,7,4,8]
**Output:** 64
**Explanation:** We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.

```

 
**Constraints:**


	- `4 4`

	- `1 4`

---

## 💻 Implementation (python3)

```py
class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        """
        Calculates the maximum product difference between two pairs of elements
        in nums: (largest * second_largest) - (smallest * second_smallest).
        Achieves optimal O(n) time complexity and O(1) space complexity in a single pass.
        """
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            # Update the two largest values
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

            # Update the two smallest values
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return int((max1 * max2) - (min1 * min2))
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to maximize the expression $(nums[w] \times nums[x]) - (nums[y] \times nums[z])$ with four distinct indices. 

Given that all elements are positive integers ($1 \le nums[i] \le 10^4$):
1. To maximize the difference, we must maximize the minuend $(nums[w] \times nums[x])$ and minimize the subtrahend $(nums[y] \times nums[z])$.
2. The product of two positive numbers is maximized when we pick the two largest numbers in the array.
3. The product is minimized when we pick the two smallest numbers in the array.

While sorting the array takes $O(n \log n)$ time and easily yields the elements at `nums[-1], nums[-2]` and `nums[0], nums[1]`, an elite approach reduces this to $O(n)$ time and $O(1)$ auxiliary space using a single pass to track the two largest and two smallest elements.

### Step-by-Step Approach

1. **State Initialization**: 
   - Initialize `max1` (largest) and `max2` (second largest) to $-\infty$.
   - Initialize `min1` (smallest) and `min2` (second smallest) to $+\infty$.

2. **Single-Pass Scan**:
   - Iterate through each number in `nums`:
     - **Largest tracking**: If `num > max1`, the old `max1` drops to `max2`, and `num` becomes the new `max1`. Otherwise, if `num > max2`, update `max2 = num`.
     - **Smallest tracking**: If `num < min1`, the old `min1` drops to `min2`, and `num` becomes the new `min1`. Otherwise, if `num < min2`, update `min2 = num`.

3. **Result Calculation**:
   - Return `(max1 * max2) - (min1 * min2)`.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. We traverse the array exactly once and perform $O(1)$ comparisons and assignments per element.
- **Space Complexity:** $O(1)$ auxiliary space. Only four scalar variables (`max1`, `max2`, `min1`, `min2`) are maintained regardless of array size.

### Common Pitfalls / Mistakes Candidates Make

1. **Sorting Overhead:** Sorting the array (`nums.sort()`) achieves $O(n \log n)$ time. While it passes the constraints, in an interview setting at top-tier companies (Google, Meta), candidates are immediately asked: *"Can we do this in linear time without extra space?"*
2. **Missing Ties / Duplicates:** Writing conditions like `elif num > max2 and num != max1` would fail for arrays with duplicate maximums such as `[5, 5, 1, 1]`. The problem statement allows equal values as long as indices are distinct.
3. **Improper Cascading Updates:** Forgetting to update `max2 = max1` before overwriting `max1` causes the previous maximum to be lost.

### Real Interview Follow-Up Questions

#### 1. What if the array contains negative numbers?
- **Answer:** If negative numbers are allowed, a large positive product can be formed either by two large positive numbers or two large negative numbers (e.g., $(-10) \times (-10) = 100$). Similarly, a small (large negative) product can be formed by multiplying the largest positive number by the most negative number. 
- You would need to consider candidates for the maximum product from `{max1 * max2, min1 * min2}` and candidates for the minimum product from `{min1 * max1, ...}`.

#### 2. What if data is arriving as a real-time stream and cannot fit in memory?
- **Answer:** The single-pass $O(1)$ space solution already works for a streaming architecture. Each incoming number can update the rolling 4 variables in $O(1)$ time and $O(1)$ memory.

#### 3. How would you solve this using parallelism / MapReduce for a distributed dataset?
- **Answer:** The associative nature of finding the top-2 and bottom-2 elements maps directly to a reduce phase:
  - **Map / Worker**: Each partition/chunk finds its local `(max1, max2, min1, min2)`.
  - **Reduce / Combiner**: Merge the local summaries by taking the top-2 from the combined pool of 4 maximums and bottom-2 from the pool of 4 minimums. This reduces the problem in $O(k \log P)$ time across $P$ processors.
