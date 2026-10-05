# 3731. Find Missing Elements

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-missing-elements/](https://leetcode.com/problems/find-missing-elements/)  
**Topics:** Array, Hash Table, Sorting

---

## 📝 Problem Statement

You are given an integer array `nums` consisting of **unique** integers.

Originally, `nums` contained **every integer** within a certain range. However, some integers might have gone **missing** from the array.

The **smallest** and **largest** integers of the original range are still present in `nums`.

Return a **sorted** list of all the missing integers in this range. If no integers are missing, return an **empty** list.

 
Example 1:

**Input:** nums = [1,4,2,5]

**Output:** [3]

**Explanation:**

The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. Among these, only 3 is missing.

Example 2:

**Input:** nums = [7,8,6,9]

**Output:** []

**Explanation:**

The smallest integer is 6 and the largest is 9, so the full range is `[6,7,8,9]`. All integers are already present, so no integer is missing.

Example 3:

**Input:** nums = [5,1]

**Output:** [2,3,4]

**Explanation:**

The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. The missing integers are 2, 3, and 4.

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        """
        Finds all missing integers between min(nums) and max(nums) in sorted order.
        
        Time Complexity: O(N log N + M) where N = len(nums), M = number of missing elements.
        Auxiliary Space Complexity: O(1) beyond sorting overhead and the returned result.
        """
        # Sort the array to process elements in increasing order
        nums.sort()
        
        missing = []
        
        # Traverse adjacent elements and collect integers in gaps
        for i in range(len(nums) - 1):
            # For any gap between nums[i] and nums[i + 1], append all missing values
            for val in range(nums[i] + 1, nums[i + 1]):
                missing.append(val)
                
        return missing
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires us to identify all missing numbers in the contiguous range $[\min(nums), \max(nums)]$. 

We are guaranteed that:
1. All elements in `nums` are unique.
2. The minimum and maximum values of the original complete range are present in `nums`.
3. The output must be sorted.

A direct observation is that after sorting `nums`, any gap between two consecutive numbers `nums[i]` and `nums[i + 1]` (i.e., when `nums[i + 1] - nums[i] > 1`) represents missing integers. By iterating through each consecutive pair and collecting all integers strictly between them (`range(nums[i] + 1, nums[i + 1])`), the missing values are naturally collected in ascending order without requiring an extra sorting step or a hash set.

### Step-by-Step Approach

1. **Sort `nums` in ascending order**: This arranges the boundaries and allows us to easily detect missing numbers between adjacent elements.
2. **Iterate through adjacent pairs**: For each index `i` from `0` to `len(nums) - 2`:
   - If `nums[i + 1] - nums[i] > 1`, there is a gap.
   - Iterate through `val` from `nums[i] + 1` up to `nums[i + 1] - 1` and append each `val` to `missing`.
3. **Return the result**: The `missing` list already contains the elements in sorted order.

### Complexity Analysis

- **Time Complexity**: 
  - Sorting takes $O(N \log N)$ where $N$ is the number of elements in `nums`.
  - Traversing the array and appending elements takes $O(N + M)$ time, where $M$ is the number of missing elements ($M = (\max(nums) - \min(nums) + 1) - N$).
  - Overall Time Complexity: $\mathcal{O}(N \log N + M)$. Since outputting $M$ elements is mandatory, this is asymptotically optimal.
  
- **Space Complexity**: 
  - $\mathcal{O}(1)$ auxiliary space (ignoring the space used by Python's Timsort which is $O(N)$, and the output list which requires $O(M)$ space).

---

### Common Pitfalls / Mistakes

1. **Iterating through the full range using a Hash Set without considering range width**:
   - Creating a `set(nums)` and looping `for x in range(min_val, max_val + 1)` has $O(N + R)$ time complexity and $O(N)$ extra space. If $R \gg N$, this incurs unnecessary overhead compared to jumping directly over consecutive pairs.
2. **Missing Off-by-One Errors**:
   - Forgetting that the gap is strictly between `nums[i]` and `nums[i + 1]` (e.g., using `nums[i]` instead of `nums[i] + 1`).
3. **Not maintaining sorted order**:
   - Using an unordered set subtraction approach (e.g., `set(range(...)) - set(nums)`) requires an additional sort at the end, wasting both memory and computation.

---

### Real Interview Follow-Up Questions

#### 1. What if the range $[\min, \max]$ is massive (e.g., $10^{14}$) and the list of missing numbers cannot fit into memory?
*Answer:* Instead of returning individual missing numbers, return a list of **intervals / ranges** (e.g., `[[start, end], ...]`). The sorting approach scales directly to this format in $O(N \log N)$ time and $O(1)$ extra space by appending `[nums[i] + 1, nums[i + 1] - 1]` whenever `nums[i + 1] - nums[i] > 1`.

#### 2. What if `nums` is an incoming stream of numbers and we need to query the count of missing elements at any time?
*Answer:* Maintain the minimum, maximum, and a count of unique seen numbers (e.g., using a Fenwick Tree, Segment Tree, or a running min/max alongside a HashSet/BitSet). The total missing elements count at any instant is `(max_val - min_val + 1) - count_unique`.

#### 3. Can this be solved in linear time $O(N)$?
*Answer:* Yes, if the range $R = \max(nums) - \min(nums) + 1$ is within $O(N)$, we can use a Boolean array (or in-place cyclic sort / marking indices negative) to mark present elements in $O(N)$ time and then collect the missing ones in $O(N)$.
