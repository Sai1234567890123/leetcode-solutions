# 1920. Build Array from Permutation

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/build-array-from-permutation/](https://leetcode.com/problems/build-array-from-permutation/)  
**Topics:** Array, Simulation

---

## 📝 Problem Statement

Given a **zero-based permutation** `nums` (**0-indexed**), build an array `ans` of the **same length** where `ans[i] = nums[nums[i]]` for each `0 

A **zero-based permutation** `nums` is an array of **distinct** integers from `0` to `nums.length - 1` (**inclusive**).

 
Example 1:

```

**Input:** nums = [0,2,1,5,3,4]
**Output:** [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
```

Example 2:

```

**Input:** nums = [5,0,1,2,3,4]
**Output:** [4,5,0,1,2,3]
**Explanation:** The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
```

 
**Constraints:**

	- `1 

 
**Follow-up:** Can you solve it without using an extra space (i.e., `O(1)` memory)?

---

## 💻 Implementation (python3)

```py
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Phase 1: Encode both the original value and the target value into each element.
        # We use the property that all numbers are in the range [0, n-1].
        # Each nums[i] will store two pieces of information:
        # 1. The original value of nums[i] (which can be retrieved by nums[i] % n).
        # 2. The target value for ans[i], which is nums[nums[i]] (this will be stored as a multiple of n,
        #    and can be retrieved by nums[i] // n after encoding).
        # The formula used is: new_nums[i] = (original_nums[i]) + (target_value * n)
        for i in range(n):
            # original_val_at_i: This is the original value of nums[i].
            # We use nums[i] % n to get the original value, in case nums[i] was already encoded
            # in a previous iteration (though for the current index i, nums[i] is still its original value
            # before this line, but it's good practice to use % n for consistency and robustness).
            original_val_at_i = nums[i] % n 
            
            # value_to_store_at_i: This is the value that should become ans[i], i.e., nums[nums[i]].
            # We need to access nums[original_val_at_i]. Since original_val_at_i is an index,
            # nums[original_val_at_i] might have already been encoded if original_val_at_i < i.
            # So, we retrieve its original value using % n.
            value_to_store_at_i = nums[original_val_at_i] % n
            
            # Encode the target value into nums[i] by adding (value_to_store_at_i * n).
            # nums[i] now effectively holds: (original_nums[i] % n) + (value_to_store_at_i * n)
            nums[i] += value_to_store_at_i * n
        
        # Phase 2: Decode the array.
        # Now, each nums[i] contains (original_nums[i] % n) + (ans[i] * n).
        # To get ans[i], we simply perform integer division by n.
        for i in range(n):
            nums[i] //= n
            
        return nums
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
