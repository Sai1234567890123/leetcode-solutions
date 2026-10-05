# 2824. Count Pairs Whose Sum is Less than Target

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/)  
**Topics:** Array, Two Pointers, Binary Search, Sorting

---

## 📝 Problem Statement

Given a **0-indexed** integer array `nums` of length `n` and an integer `target`, return *the number of pairs* `(i, j)` *where* `0  
Example 1:

```

**Input:** nums = [-1,1,2,3,1], target = 2
**Output:** 3
**Explanation:** There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 Example 2:

```

**Input:** nums = [-6,2,5,-2,-7,-1,3], target = -2
**Output:** 10
**Explanation:** There are 10 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0  
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Sorting allows us to leverage the two-pointer technique.
        # Order of elements does not matter since we only care about the count of pairs.
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            # If the sum of the smallest and largest available elements is less than target,
            # then nums[left] paired with any element from left + 1 to right will also be < target.
            if nums[left] + nums[right] < target:
                count += (right - left)
                left += 1
            else:
                # Sum is too large, decrement right pointer to reduce the sum
                right -= 1
                
        return count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the count of index pairs $(i, j)$ with $0 \le i < j < n$ such that $nums[i] + nums[j] < target$. 

1. **Brute Force Consideration:**
   Checking every pair $(i, j)$ takes $O(n^2)$ time. While $n \le 50$ in the constraints would easily pass with $O(n^2)$, top-tier interviewers expect you to recognize that sorting enables an $O(n \log n)$ solution, which scales to $n = 10^5$.

2. **Order Invariance:**
   Addition is commutative ($nums[i] + nums[j] = nums[j] + nums[i]$). The condition $i < j$ simply ensures we do not count the same pair twice or pair an element with itself. Therefore, the original indices do not matter; only the multiset of values matters.

3. **Two-Pointer Strategy:**
   If we sort `nums` in ascending order:
   - Place `left = 0` and `right = n - 1`.
   - If `nums[left] + nums[right] < target`, then because the array is sorted, pairing `nums[left]` with *any* element at index $k \in [left + 1, right]$ will also yield `nums[left] + nums[k] <= nums[left] + nums[right] < target`.
   - Thus, there are exactly `right - left` valid pairs that include `nums[left]`. We add this to our counter and increment `left` to consider the next candidate.
   - If `nums[left] + nums[right] >= target`, then `nums[right]` is too large to pair even with the smallest remaining number `nums[left]`. Hence, `nums[right]` cannot form a valid pair with any remaining candidate, so we decrement `right`.

---

### Step-by-Step Approach

1. Sort the input array `nums` in non-decreasing order.
2. Initialize two pointers: `left = 0` and `right = len(nums) - 1`, and a variable `count = 0`.
3. Loop while `left < right`:
   - Check if `nums[left] + nums[right] < target`.
   - If `True`: add `right - left` to `count`, and increment `left` by 1.
   - If `False`: decrement `right` by 1.
4. Return `count`.

---

### Complexity Analysis

- **Time Complexity:** $O(n \log n)$
  - Sorting the array takes $O(n \log n)$ time (using Timsort in Python).
  - The two-pointer traversal visits each element at most once, taking $O(n)$ time.
  - Overall dominant time complexity: $O(n \log n)$.

- **Space Complexity:** $O(1)$ auxiliary space (or $O(n)$ if counting the internal space used by Timsort).
  - In Python, `nums.sort()` sorts in-place with up to $O(n)$ space for Timsort's run stack. If in-place modification of the input is disallowed, creating a copy takes $O(n)$ space.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Overlooking Sorting Invariance:** Assuming that because the problem specifies $i < j$, sorting will disrupt the answer. Candidates often fail to see that $i < j$ is merely defining an unordered pair $\{i, j\}$.
2. **Off-by-One in Pointer Count:** Adding `right - left + 1` instead of `right - left`. The element `nums[left]` cannot be paired with itself.
3. **Double Counting:** Advancing both `left` and `right` simultaneously when a condition is met, leading to missed pairs.
4. **Integer Overflow:** In languages like C++ or Java, when numbers can be up to $10^9$ or $-10^9$, checking `nums[left] + nums[right]` can overflow standard 32-bit signed integers. In Python, integers have arbitrary precision, but it's important to mention in an interview.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input array is already sorted?
- **Answer:** If the array is already sorted, the sorting step ($O(n \log n)$) can be skipped, reducing the overall time complexity to $O(n)$ using just the two-pointer loop.

#### 2. What if the array is immutable or we must not modify the input?
- **Answer:** We can create a sorted copy: `sorted_nums = sorted(nums)`. This explicitly costs $O(n)$ extra space, but keeps the input pure.

#### 3. What if data is a continuous stream and we want to query pairs dynamically?
- **Answer:** If numbers arrive via a stream and we must maintain counts:
  - We can maintain a **Self-Balancing Binary Search Tree** (like an AVL or Red-Black Tree with subtree sizes) or a **Fenwick Tree / Segment Tree** (if the coordinate range is bounded or discretized).
  - For each incoming element $x$, we query the tree for the count of elements strictly less than $target - x$, add that to a running total, and then insert $x$ into the data structure in $O(\log N)$ time.
