# 3925. Concatenate Array With Reverse

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/concatenate-array-with-reverse/](https://leetcode.com/problems/concatenate-array-with-reverse/)  
**Topics:** Array, Simulation

---

## 📝 Problem Statement

You are given an integer array `nums` of length `n`.

Construct a new array `ans` of length `2 * n` such that the first `n` elements are the same as `nums`, and the next `n` elements are the elements of `nums` in reverse order.

Formally, for `0 

	- `ans[i] = nums[i]`

	- `ans[i + n] = nums[n - i - 1]`

Return an integer array `ans`.

 
Example 1:

**Input:** nums = [1,2,3]

**Output:** [1,2,3,3,2,1]

**Explanation:**

The first `n` elements of `ans` are the same as `nums`.

For the next `n = 3` elements, each element is taken from `nums` in reverse order:

	- `ans[3] = nums[2] = 3`

	- `ans[4] = nums[1] = 2`

	- `ans[5] = nums[0] = 1`

Thus, `ans = [1, 2, 3, 3, 2, 1]`.

Example 2:

**Input:** nums = [1]

**Output:** [1,1]

**Explanation:**

The array remains the same when reversed. Thus, `ans = [1, 1]`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        # Pythonic solution: concatenate the original list with its reversed version.
        # nums[::-1] creates a new list that is the reverse of nums.
        # This operation is efficient, typically O(n) time and O(n) space for the new list.
        # The '+' operator concatenates two lists, creating a third new list.
        # This operation is also efficient, typically O(n) time and O(n) space for the new list.
        return nums + nums[::-1]
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to construct a new array `ans` of length `2 * n` from a given array `nums` of length `n`. The first `n` elements of `ans` should be identical to `nums`, and the subsequent `n` elements should be `nums` in reverse order.

My initial thought is to directly implement the rules:
1. Determine the length `n` of `nums`.
2. Create an empty result array `ans` of size `2 * n`.
3. Copy elements from `nums` to the first half of `ans` (i.e., `ans[i] = nums[i]` for `0 <= i < n`).
4. Copy elements from `nums` in reverse order to the second half of `ans` (i.e., `ans[i + n] = nums[n - i - 1]` for `0 <= i < n`).

While this loop-based approach is perfectly valid and works, Python offers highly optimized and concise ways to perform list manipulations. Specifically, list slicing (`[::-1]`) can create a reversed copy of a list, and the `+` operator can concatenate two lists. Leveraging these built-in features often leads to cleaner and equally efficient code in Python. The key insight is recognizing that these high-level operations abstract away the underlying element-by-element copying, making the solution more readable and less prone to indexing errors.

## Step-by-Step Approach

The chosen solution utilizes Python's list slicing and concatenation features for maximum conciseness and readability.

1.  **Reverse `nums`**: We create a reversed copy of the input list `nums` using the slice notation `nums[::-1]`. This slice effectively creates a new list containing all elements of `nums` but in reverse order. For example, if `nums = [1, 2, 3]`, `nums[::-1]` will result in `[3, 2, 1]`.
2.  **Concatenate Lists**: We then use the list concatenation operator `+` to combine the original `nums` list with its newly created reversed counterpart. This operation creates a third new list that contains all elements of `nums` followed by all elements of `nums` reversed. For `nums = [1, 2, 3]`, this would be `[1, 2, 3] + [3, 2, 1]`, resulting in `[1, 2, 3, 3, 2, 1]`.
3.  **Return Result**: This newly concatenated list, which satisfies all problem requirements, is then returned.

## Complexity Analysis

*   **Time Complexity: O(n)**
    *   `nums[::-1]`: Creating a reversed copy of a list of length `n` takes O(n) time because each element needs to be visited and copied into the new list.
    *   `nums + nums[::-1]`: Concatenating two lists (one of length `n` and one of length `n`) takes O(n) time because all `2 * n` elements need to be copied into the final result list.
    *   Therefore, the total time complexity is O(n) + O(n) = O(n).

*   **Space Complexity: O(n)**
    *   `nums[::-1]`: This operation creates a new list of length `n` to store the reversed elements.
    *   The `+` operator then creates another new list of length `2 * n` for the final result.
    *   Thus, the total auxiliary space used is proportional to `n` (for the reversed list and the final concatenated list). This is optimal because we must construct and return a new array of length `2 * n`.

## Common Pitfalls / Mistakes

1.  **Modifying the Original List:** A common mistake in Python is to use `nums.reverse()` or `nums.extend(...)` directly on the input `nums`. `nums.reverse()` modifies the list in-place and returns `None`, which is not what we want. `nums.extend(nums[::-1])` would modify the original `nums` list, which is generally bad practice for function inputs unless explicitly stated. The `+` operator and `[::-1]` slice both create *new* lists, preserving the original `nums`.
2.  **Inefficient Reversal:** Manually reversing a list using a loop and `list.insert(0, element)` would be very inefficient (O(N^2)) because `insert(0, ...)` requires shifting all existing elements. Python's `[::-1]` slice is implemented efficiently in C and is the preferred way for creating a reversed copy.
3.  **Off-by-One Errors (in manual loop approach):** If one were to implement a loop-based solution, correctly mapping the reverse index (`nums[n - 1 - i]`) can be a source of off-by-one errors. Python's high-level operations abstract this complexity away.
4.  **Misunderstanding `reversed()` vs. `[::-1]`:** `reversed(nums)` returns an *iterator*, not a list. To get a list from it, you'd need `list(reversed(nums))`. While functionally similar to `nums[::-1]` in terms of result, `[::-1]` is often more concise for creating a reversed copy.

## Real Interview Follow-Up Questions

1.  **What if `nums` contains very large objects instead of integers? How would your solution's memory footprint change?**
    *   **Answer:** Python lists store references to objects, not the objects themselves. When `nums[::-1]` is created, it creates a new list of references. Similarly, `nums + nums[::-1]` creates another new list of references. The actual large objects are *not* duplicated in memory. Therefore, the space complexity for the *list structures* (the references) remains O(N). The total memory used by the *objects themselves* remains O(N) (assuming the original objects are not duplicated). This is an important distinction: shallow copies of lists of objects are efficient in terms of object memory.

2.  **Can you solve this without creating an explicit reversed copy of `nums`? (e.g., if memory is extremely constrained and even a temporary `N`-sized list is an issue)**
    *   **Answer:** Yes, we can construct the `ans` array by iterating through `nums` twice, once forward and once backward, without explicitly creating `nums[::-1]`.
    ```python
    class Solution:
        def concatWithReverse_manual(self, nums: list[int]) -> list[int]:
            n = len(nums)
            ans = [0] * (2 * n) # Pre-allocate space for the result array

            # Populate the first n elements (original order)
            for i in range(n):
                ans[i] = nums[i]

            # Populate the next n elements (reversed order)
            for i in range(n):
                # The element at index 'i' in the reversed sequence
                # corresponds to 'nums[n - 1 - i]' in the original sequence.
                # This element is placed at 'ans[i + n]'.
                ans[i + n] = nums[n - 1 - i]

            return ans
    ```
    This approach still uses O(N) space for the final `ans` array, which is unavoidable as we need to return a `2N` length array. However, it avoids the *intermediate* O(N) space used by `nums[::-1]`, potentially offering a slight constant factor improvement in memory usage.

3.  **What if `n` is extremely large, such that `2 * n` elements cannot fit into memory at once? How would you handle this?**
    *   **Answer:** This scenario points to a "streaming" or "out-of-core" data problem.
        *   **Generator/Iterator:** Instead of returning a list, we could return a generator that yields elements one by one. This approach has O(1) additional space complexity (beyond the input `nums` itself) because it doesn't construct the full `ans` list in memory.
            ```python
            class Solution:
                def concatWithReverse_generator(self, nums: list[int]): # Return type would be Iterator[int]
                    n = len(nums)
                    # Yield original elements
                    for i in range(n):
                        yield nums[i]
                    # Yield reversed elements
                    for i in range(n - 1, -1, -1): # Iterate from n-1 down to 0
                        yield nums[i]
            ```
        *   **File I/O / Disk Storage:** If `nums` itself is too large to fit in memory, it would need to be read from a file or database. We would then write the output directly to another file or stream. This would involve reading the first half of `nums` and writing it, then either seeking back to the beginning of the input (if supported by the data source) or reading `nums` into a temporary file/database to then read it in reverse and write the second half. This is a common pattern for big data processing.

4.  **How would you handle this if the input `nums` was a singly linked list instead of an array?**
    *   **Answer:** With a singly linked list, direct random access (like `nums[i]`) is not possible.
        *   **Option 1 (Store in Array/List):** The most straightforward way would be to traverse the linked list once, storing all its values into a temporary Python list (O(N) space). Once all values are in the list, the problem reduces to the original array problem, and we can use `temp_list + temp_list[::-1]` to construct the result. If the output also needs to be a linked list, we'd then convert this new list back into a linked list. This uses O(N) space for the temporary list.
        *   **Option 2 (Using a Stack):** Traverse the linked list, pushing each node's value onto a stack. Then, construct the first `n` part of the result by traversing the original linked list again. For the second `n` part, pop elements from the stack. This also uses O(N) space for the stack.
        *   **Option 3 (Two Pointers + Reverse Second Half - More Complex):** This is more involved. You could find the middle of the list, reverse the second half of the list in-place, and then interleave or concatenate. However, for this specific problem (concatenate with *reverse* of original), reversing a portion of the list in-place isn't directly helpful without storing the first half or traversing it again. The stack or temporary array approach is simpler and more robust for this problem with a singly linked list.
