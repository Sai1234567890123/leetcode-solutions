# 3194. Minimum Average of Smallest and Largest Elements

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/](https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/)  
**Topics:** Array, Two Pointers, Sorting

---

## 📝 Problem Statement

You have an array of floating point numbers `averages` which is initially empty. You are given an array `nums` of `n` integers where `n` is even.

You repeat the following procedure `n / 2` times:

	- Remove the **smallest** element, `minElement`, and the **largest** element `maxElement`, from `nums`.

	- Add `(minElement + maxElement) / 2` to `averages`.

Return the **minimum** element in `averages`.

 
Example 1:

**Input:** nums = [7,8,3,4,15,13,4,1]

**Output:** 5.5

**Explanation:**

	
		
			step
			nums
			averages
		
		
			0
			[7,8,3,4,15,13,4,1]
			[]
		
		
			1
			[7,8,3,4,13,4]
			[8]
		
		
			2
			[7,8,4,4]
			[8,8]
		
		
			3
			[7,4]
			[8,8,6]
		
		
			4
			[]
			[8,8,6,5.5]
		
	

The smallest element of averages, 5.5, is returned.

Example 2:

**Input:** nums = [1,9,8,3,10,5]

**Output:** 5.5

**Explanation:**

	
		
			step
			nums
			averages
		
		
			0
			[1,9,8,3,10,5]
			[]
		
		
			1
			[9,8,3,5]
			[5.5]
		
		
			2
			[8,5]
			[5.5,6]
		
		
			3
			[]
			[5.5,6,6.5]
		
	

Example 3:

**Input:** nums = [1,2,3,7,8,9]

**Output:** 5.0

**Explanation:**

	
		
			step
			nums
			averages
		
		
			0
			[1,2,3,7,8,9]
			[]
		
		
			1
			[2,3,7,8]
			[5]
		
		
			2
			[3,7]
			[5,5]
		
		
			3
			[]
			[5,5,5]
		
	

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # Sort the array to efficiently pair the i-th smallest
        # and i-th largest elements together.
        nums.sort()
        
        n = len(nums)
        # Minimize the sum directly to avoid redundant floating-point divisions,
        # then divide the minimum sum by 2 at the end.
        min_sum = min(nums[i] + nums[n - 1 - i] for i in range(n // 2))
        
        return min_sum / 2.0
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to repeatedly pair the current minimum and maximum elements in an array, compute their average, and return the minimum average among all pairs.

If we sort the array in ascending order:
- The 1st pair is `(nums[0], nums[n - 1])` (the absolute smallest and largest).
- The 2nd pair is `(nums[1], nums[n - 2])` (the second smallest and second largest).
- In general, the $i$-th pair will always be `(nums[i], nums[n - 1 - i])` for $0 \le i < n / 2$.

Since dividing by $2.0$ preserves relative ordering (i.e., if $a + b < c + d$, then $(a + b)/2 < (c + d)/2$), we can simply find the minimum sum of the symmetric pairs `nums[i] + nums[n - 1 - i]` and perform the division by $2.0$ once at the very end. This reduces floating-point operations and mitigates any potential precision drift.

### Step-by-Step Approach

1. **Sort `nums` in ascending order**: Sorting takes $O(n \log n)$ time.
2. **Evaluate symmetric pairs**: Iterate $i$ from $0$ to $n / 2 - 1$, pairing `nums[i]` with `nums[n - 1 - i]`.
3. **Find the minimum pair sum**: Track the minimum value of `nums[i] + nums[n - 1 - i]`.
4. **Return result**: Divide the minimum sum by $2.0$ and return it.

### Complexity Analysis

- **Time Complexity:** $O(n \log n)$ where $n$ is the length of `nums`. Sorting takes $O(n \log n)$, and the symmetric pairing pass takes $O(n)$. Given $n \le 50$, this is virtually instantaneous.
  *(Note: If the range of values is strictly bounded, Counting Sort can achieve $O(n + \max(\text{nums}))$, which is $O(n)$ time).*
- **Space Complexity:** $O(1)$ auxiliary space if sorted in place (or $O(n)$ depending on Python's Timsort internal stack allocation).

---

### Common Pitfalls / Mistakes

1. **Simulating the process destructively:** Using operations like `nums.pop(nums.index(min(nums)))` and `nums.pop(nums.index(max(nums)))` inside a loop leads to an $O(n^2)$ time complexity due to repeated linear scans and array shifts.
2. **Premature Floating-Point Conversion:** Computing floats on every iteration can accumulate slight precision issues. Deferring the division to the end avoids this.
3. **Integer Division:** In languages like C++, Java, or Python 2, doing `(a + b) / 2` without casting to float would perform integer division, truncating fractional parts (e.g., $11 / 2 = 5$ instead of $5.5$).

---

### Real Interview Follow-Up Questions

#### 1. What if the range of elements is small (e.g., $nums[i] \le 100$) and $n$ is large?
**Answer:** We can optimize the time complexity to $O(n + K)$ (where $K$ is the maximum element value) by using **Counting Sort / Frequency Array**. We then use two pointers on the frequency array to pair elements from the smallest and largest ends without full comparison-based sorting.

#### 2. What if $nums$ is an unbounded data stream and $n$ is not known in advance?
**Answer:** The current problem requires knowledge of the complete sorted order across the entire dataset to pair smallest with largest. If data arrives as a stream, you would need to either:
- Buffer the stream if $n$ is finite and known at the end of the stream, or
- Maintain balanced heaps / balanced BSTs, though pairing elements symmetrically requires two-sided access (which heaps don't support efficiently without maintaining both min-heap and max-heap with synchronization or a balanced BST like an AVL / Red-Black Tree).

#### 3. How can we optimize memory if $nums$ cannot fit in RAM (External Memory / Big Data)?
**Answer:** Use **External Merge Sort** to sort the array stored on disk in chunks. Once sorted, read elements from the start of the file and end of the file simultaneously using two file pointers moving inward to compute the minimum pair average in a single streaming pass with $O(1)$ extra memory.
