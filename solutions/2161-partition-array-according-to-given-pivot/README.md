# 2161. Partition Array According to Given Pivot

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/partition-array-according-to-given-pivot/](https://leetcode.com/problems/partition-array-according-to-given-pivot/)  
**Topics:** Array, Two Pointers, Simulation

---

## 📝 Problem Statement

You are given a **0-indexed** integer array `nums` and an integer `pivot`. Rearrange `nums` such that the following conditions are satisfied:

	- Every element less than `pivot` appears **before** every element greater than `pivot`.

	- Every element equal to `pivot` appears **in between** the elements less than and greater than `pivot`.

	The **relative order** of the elements less than `pivot` and the elements greater than `pivot` is maintained.
	
		- More formally, consider every `pi`, `pj` where `pi` is the new position of the `ith` element and `pj` is the new position of the `jth` element. If `i i j`.

	
	

Return `nums`* after the rearrangement.*

 
Example 1:

```

**Input:** nums = [9,12,5,10,14,3,10], pivot = 10
**Output:** [9,5,3,10,10,12,14]
**Explanation:** 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

```

Example 2:

```

**Input:** nums = [-3,4,3,2], pivot = 2
**Output:** [-3,2,4,3]
**Explanation:** 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.

```

 
**Constraints:**

	- `1 5`

	- `-106 6`

	- `pivot` equals to an element of `nums`.

---

## 💻 Implementation (python3)

```py
class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        # Initialize three empty lists to categorize elements based on their comparison with the pivot.
        # 'less_than_pivot' will store elements smaller than the pivot.
        # 'equal_to_pivot' will store elements equal to the pivot.
        # 'greater_than_pivot' will store elements larger than the pivot.
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []

        # Iterate through the input array 'nums' exactly once.
        # This single pass is crucial for maintaining the relative order of elements
        # within each of the three categories (less, equal, greater).
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num) # Append to the list for elements less than pivot
            elif num == pivot:
                equal_to_pivot.append(num) # Append to the list for elements equal to pivot
            else: # num > pivot
                greater_than_pivot.append(num) # Append to the list for elements greater than pivot
        
        # Concatenate the three lists in the specified order:
        # 1. All elements less than the pivot.
        # 2. All elements equal to the pivot.
        # 3. All elements greater than the pivot.
        # This concatenation forms the final rearranged array.
        return less_than_pivot + equal_to_pivot + greater_than_pivot
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
