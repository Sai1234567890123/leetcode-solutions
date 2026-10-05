# 3190. Find Minimum Operations to Make All Elements Divisible by Three

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/)  
**Topics:** Array, Math

---

## 📝 Problem Statement

You are given an integer array `nums`. In one operation, you can add or subtract 1 from **any** element of `nums`.

Return the **minimum** number of operations to make all elements of `nums` divisible by 3.

 
Example 1:

**Input:** nums = [1,2,3,4]

**Output:** 3

**Explanation:**

All array elements can be made divisible by 3 using 3 operations:

	- Subtract 1 from 1.

	- Add 1 to 2.

	- Subtract 1 from 4.

Example 2:

**Input:** nums = [3,6,9]

**Output:** 0

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Initialize a counter for the total minimum operations required.
        total_operations = 0
        
        # Iterate through each number in the input array.
        for num in nums:
            # Calculate the remainder when the current number is divided by 3.
            # For positive integers, num % 3 will always be 0, 1, or 2.
            remainder = num % 3
            
            # If the remainder is 0, the number is already divisible by 3,
            # so no operations are needed for this specific number.
            #
            # If the remainder is 1 (e.g., num = 1, 4, 7, ...):
            #   - We can subtract 1 from 'num' to make it divisible by 3 (e.g., 1 -> 0, 4 -> 3).
            #     This takes 1 operation.
            #   - Alternatively, we could add 2 to 'num' (e.g., 1 -> 3, 4 -> 6),
            #     but this would take 2 operations, which is not the minimum.
            #
            # If the remainder is 2 (e.g., num = 2, 5, 8, ...):
            #   - We can add 1 to 'num' to make it divisible by 3 (e.g., 2 -> 3, 5 -> 6).
            #     This takes 1 operation.
            #   - Alternatively, we could subtract 2 from 'num' (e.g., 2 -> 0, 5 -> 3),
            #     but this would take 2 operations, which is not the minimum.
            #
            # In both cases where the remainder is not 0 (i.e., remainder is 1 or 2),
            # exactly 1 operation is sufficient and minimum for that number.
            if remainder != 0:
                total_operations += 1
                
        # After checking all numbers in the array, return the accumulated total operations.
        return total_operations
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
