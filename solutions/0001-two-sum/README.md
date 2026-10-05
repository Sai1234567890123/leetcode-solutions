# 0001. Two Sum

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)  
**Topics:** Array, Hash Table

---

## 📝 Problem Statement

You are given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

 
Example 1:

```

**Input:** nums = [2,7,11,15], target = 9
**Output:** [0,1]
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

```

Example 2:

```

**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]

```

Example 3:

```

**Input:** nums = [3,3], target = 6
**Output:** [0,1]

```

 
**Constraints:**

	- `2 4`

	- `-109 9`

	- `-109 9`

	- **Only one valid answer exists.**

 
**Follow-up: **Can you come up with an algorithm that is less than `O(n2)` time complexity?

---

## 💻 Implementation (python3)

```py
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a hash map (dictionary in Python) to store numbers and their indices.
        # The key will be the number, and the value will be its index.
        num_map = {} 

        # Iterate through the array with both index and value using enumerate.
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target.
            # If 'num' is one of the numbers, 'complement' is the other.
            complement = target - num

            # Check if the complement already exists in our hash map.
            # If it does, we've found the two numbers that sum up to the target.
            if complement in num_map:
                # Return the index of the complement (which was stored earlier)
                # and the current index 'i'.
                return [num_map[complement], i]
            
            # If the complement is not found, add the current number and its index to the hash map.
            # This makes the current 'num' available as a potential complement for subsequent numbers.
            num_map[num] = i
        
        # According to the problem statement, there will always be exactly one solution.
        # Therefore, this line should theoretically never be reached.
        # It's included for completeness, though the problem guarantees a return within the loop.
        return []
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to find two numbers in an array that sum up to a specific `target` and return their indices. We are guaranteed exactly one solution and cannot use the same element twice. The key challenge is to do this efficiently, ideally better than a brute-force O(n^2) approach.

The brute-force method would involve checking every possible pair of numbers, which means using two nested loops. For an array of size `n`, this would take approximately `n * (n-1) / 2` comparisons, leading to O(n^2) time complexity. Given the constraints (`n` up to 10^4), an O(n^2) solution (10^8 operations) would likely be too slow.

To achieve better performance, we need a faster way to look up numbers. If we iterate through the array once, for each number `x`, we need to quickly determine if its "complement" (`target - x`) exists in the *rest* of the array. A hash map (or dictionary in Python) is an ideal data structure for this, as it provides average O(1) time complexity for both insertions and lookups.

The intuition is as follows:
1.  As we iterate through the `nums` array, for each `num` at index `i`, we calculate the `complement` needed to reach the `target` (i.e., `complement = target - num`).
2.  We then check if this `complement` has already been encountered and stored in our hash map.
    *   If the `complement` is found in the hash map, it means we have found the two numbers that sum to `target`. The hash map stores the index of the `complement`, and `i` is the index of the current `num`. We return these two indices.
    *   If the `complement` is *not* found, it means the current `num` is not the second part of a pair with any previously seen number. In this case, we add the current `num` and its index `i` to the hash map. This way, `num` itself can serve as a `complement` for numbers we encounter later in the array.

This approach ensures that we only store numbers we've already processed, and when a complement is found, its index will always be different from the current index `i` (unless the numbers are identical but at different positions, which is correctly handled).

## Step-by-Step Approach

1.  **Initialize a Hash Map:** Create an empty hash map (e.g., `num_map` in Python). This map will store numbers as keys and their corresponding indices as values.
2.  **Iterate Through `nums`:** Loop through the input array `nums` using `enumerate`. This allows us to access both the index (`i`) and the value (`num`) of each element in a single pass.
3.  **Calculate Complement:** For each `num` in the iteration, calculate the `complement` required to reach the `target`: `complement = target - num`.
4.  **Check for Complement in Map:** Before adding the current `num` to the map, check if the `complement` already exists as a key in `num_map`.
    *   **If `complement` is in `num_map`:** This means we have found the two numbers that sum to `target`. The index of the `complement` is `num_map[complement]`, and the index of the current number is `i`. Return `[num_map[complement], i]`.
5.  **Store Current Number:** If the `complement` is *not* found in `num_map`, add the current `num` and its index `i` to the `num_map`. This makes `num` available as a potential `complement` for any subsequent numbers in the array.
6.  **Guaranteed Solution:** The problem statement guarantees that "exactly one valid answer exists." Therefore, the loop will always find a pair and return the indices, so the code will never reach the end of the function without returning.

## Complexity Analysis

*   **Time Complexity: O(n)**
    *   We iterate through the `nums` array exactly once.
    *   Inside the loop, operations such as calculating the complement, checking for existence in the hash map (`in` operator), and inserting into the hash map are all average O(1) operations. In the worst case, due to hash collisions, these operations could degrade to O(n), but with good hash functions and typical data, the average case holds.
    *   Therefore, the total time complexity is directly proportional to the number of elements in the array, `n`.

*   **Space Complexity: O(n)**
    *   In the worst-case scenario, if no pair is found until the very last element (or if no pair exists, though the problem guarantees one), the hash map might store up to `n-1` elements.
    *   Each element stored in the hash map takes constant space.
    *   Therefore, the space complexity is proportional to the number of elements, `n`.

## Common Pitfalls / Mistakes Candidates Make

1.  **Brute-Force O(n^2) Solution:** The most common mistake is to implement a nested loop solution. While correct, it's not optimal and will fail for larger inputs due to time limits. The problem specifically asks for an algorithm better than O(n^2).
2.  **Using `list.index()`:** Some candidates might try to find the complement using `nums.index(complement)`. This method itself takes O(n) time in the worst case, making the overall solution O(n^2), similar to the brute-force approach. Additionally, `list.index()` returns the *first* occurrence, which can be problematic if `complement` is the current `num` and appears multiple times.
3.  **Incorrectly Handling Duplicates:** If the array contains duplicate numbers (e.g., `nums = [3, 3], target = 6`), some solutions might incorrectly use the same element at the same index. The hash map approach correctly handles this because it stores indices, ensuring that if `nums[i]` is `3` and `target` is `6`, and `3` was previously stored at index `0`, it correctly returns `[0, 1]`.
4.  **Returning Values Instead of Indices:** The problem explicitly asks for the *indices* of the two numbers, not the numbers themselves. Always double-check the required return type.
5.  **Off-by-One Errors:** While less common with `enumerate`, manual index management can lead to errors.

## Real Interview Follow-Up Questions and How to Answer Them!

1.  **Q: What if there are multiple valid solutions? How would you modify your code to return all pairs of indices?**
    *   **A:** If multiple solutions are possible, instead of immediately returning the first pair found, we would store each valid pair in a list (e.g., `solutions = []`). We would continue iterating through the entire array to find all possible pairs. After the loop completes, we would return the `solutions` list. To avoid duplicate pairs (e.g., `[0,1]` and `[1,0]` if order doesn't matter), we might sort the indices within each pair before adding them to the `solutions` list or a `set` of tuples.

2.  **Q: What if the array is sorted? Can you do better than O(n) time complexity?**
    *   **A:** If the array is sorted, we can use the **Two-Pointer technique**.
        *   Initialize two pointers: `left` at the beginning of the array (index 0) and `right` at the end (index `len(nums) - 1`).
        *   While `left < right`:
            *   Calculate `current_sum = nums[left] + nums[right]`.
            *   If `current_sum == target`, we found a pair. Return `[left, right]`.
            *   If `current_sum < target`, we need a larger sum, so increment `left` (`left += 1`).
            *   If `current_sum > target`, we need a smaller sum, so decrement `right` (`right -= 1`).
        *   This approach has **O(n) time complexity** (single pass) and **O(1) space complexity** (no extra data structure needed). While the time complexity is the same as the hash map approach, it's superior in terms of space complexity.

3.  **Q: What if the input array is very large, and we cannot load all of it into memory (streaming data)?**
    *   **A:** This is a memory constraint problem.
        *   The hash map approach, while time-efficient, can consume O(n) space. For truly massive streaming data where `n` is too large for memory, we'd need different strategies.
        *   **External Sorting:** If the data can be sorted externally (e.g., using a merge sort variant that operates on disk), we could then apply the Two-Pointer technique (from Q2) on the sorted data, reading chunks as needed. This is complex and I/O-bound.
        *   **Distributed Processing:** For extremely large datasets, a distributed computing framework (like Apache Spark or Hadoop MapReduce) would be suitable. Data could be partitioned across multiple machines. Each machine could run a variant of the hash map approach on its local chunk, and then a global aggregation step would combine results or look for complements across partitions.
        *   **Limited Memory Hash Map:** If we can only store a fixed-size hash map, we might only find solutions where both numbers appear within that window. This wouldn't guarantee finding *the* solution unless we make assumptions about the data distribution or proximity of the pair.

4.  **Q: What if the numbers can be negative? Does your solution still work?**
    *   **A:** Yes, the hash map solution works perfectly fine with negative numbers. The arithmetic `target - num` correctly handles negative values, and hash maps (dictionaries) in Python can store negative integers as keys without any issues. The problem constraints (`-10^9 <= nums[i] <= 10^9`) already imply that negative numbers are possible.

5.  **Q: What if the problem asked for three numbers that sum to target (3Sum)?**
    *   **A:** The 3Sum problem is a classic extension and is significantly harder.
        *   A naive three-nested-loop approach would be O(n^3).
        *   The standard optimal approach is **O(n^2)**:
            1.  First, **sort the array** (O(n log n)).
            2.  Then, iterate through the array with one pointer (`i`). For each `nums[i]`:
            3.  Treat `target - nums[i]` as a new `sub_target`.
            4.  Apply the **Two-Pointer technique** (as described in Q2) on the *remaining subarray* (`nums[i+1:]`) to find two numbers that sum up to `sub_target`.
            5.  Careful handling of duplicates is crucial to avoid returning redundant triplets.
        *   The overall time complexity becomes O(n log n) for sorting + O(n * n) for the nested loops (one outer loop, one inner two-pointer pass), resulting in an overall **O(n^2)** time complexity. Space complexity would be O(1) if sorting in-place, or O(n) if sorting requires auxiliary space.
