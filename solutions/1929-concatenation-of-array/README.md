# 1929. Concatenation of Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/concatenation-of-array/](https://leetcode.com/problems/concatenation-of-array/)  
**Topics:** Array, Simulation

---

## 📝 Problem Statement

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 

Specifically, `ans` is the **concatenation** of two `nums` arrays.

Return *the array *`ans`.

 
Example 1:

```

**Input:** nums = [1,2,1]
**Output:** [1,2,1,1,2,1]
**Explanation:** The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```

Example 2:

```

**Input:** nums = [1,3,2,1]
**Output:** [1,3,2,1,1,3,2,1]
**Explanation:** The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

```

 
**Constraints:**

	- `n == nums.length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        Concatenates the input list `nums` with itself.
        
        In Python, list multiplication (`nums * 2`) or concatenation (`nums + nums`)
        is implemented at the C-level (CPython `list_repeat`), allocating memory
        in a single block and performing a fast memory copy (memcpy).
        """
        return nums + nums
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires constructing an array `ans` of length $2n$ where the first half ($0 \le i < n$) is identical to `nums`, and the second half ($n \le i < 2n$) is also identical to `nums`.

In Python, this is the canonical list concatenation operation. Using `nums + nums` (or `nums * 2`) relies on the underlying CPython implementation (`list_concat` / `list_repeat`), which calculates the target size, performs a single heap allocation, and uses `memcpy` under the hood.

For interviewers who want to see explicit array allocation and indexing (as you would in C++ or Java):
```python
n = len(nums)
ans = [0] * (2 * n)
for i in range(n):
    ans[i] = nums[i]
    ans[i + n] = nums[i]
return ans
```

### Step-by-Step Approach

1. Take the input array `nums` of length $n$.
2. Return the concatenation of `nums` with itself: `nums + nums`.
   - Python allocates an array of size $2n$.
   - The elements of the first copy are copied into `ans[0...n-1]`.
   - The elements of the second copy are copied into `ans[n...2n-1]`.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. We must copy each of the $n$ elements twice into the new array.
- **Space Complexity:** $O(n)$ auxiliary space to store the resulting array of size $2n$ (or $O(1)$ extra space if output space is excluded from auxiliary space calculations).

### Common Pitfalls / Mistakes Candidates Make

1. **Repeatedly Appending in a Loop without Pre-allocation:**
   Doing `ans = []; for x in nums: ans.append(x)` twice causes multiple dynamic array resizings and reallocations, which introduces overhead despite remaining $O(n)$ amortized.
2. **In-place Modification Misinterpretation:**
   Modifying `nums` in-place using `nums.extend(nums)` when the signature expects returning a new list. While mutating in-place can be valid if specified, the problem states "create an array `ans`". Modifying the original input without explicit permission is an anti-pattern in production code.

### Real Interview Follow-Up Questions & Answers

#### 1. What if $n$ is very large (e.g., billions of elements) and cannot fit into memory twice?
- **Answer:** Use an iterator/generator instead of materializing the entire list in memory:
  ```python
  from itertools import chain
  def get_concatenation_stream(nums):
      return chain(nums, nums)
  ```
  This provides an $O(1)$ space streaming interface that yields elements on demand.

#### 2. What if we are asked to perform the operation in-place on the existing array?
- **Answer:** If the array is dynamically sized (like Python's `list` or C++'s `std::vector`), we can reserve/resize capacity to $2n$ and copy elements to `nums[i + n] = nums[i]`. In Python, `nums.extend(nums)` achieves this in-place.

#### 3. How does this behave if elements are mutable objects?
- **Answer:** Both `nums + nums` and `nums * 2` perform **shallow copies** of the references. Modifying a mutable element (e.g., an inner list or dict) at `ans[i]` would also reflect at `ans[i + n]`. If deep independence is required, `copy.deepcopy` or explicit reconstruction would be necessary.
