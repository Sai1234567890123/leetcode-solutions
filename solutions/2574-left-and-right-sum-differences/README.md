# 2574. Left and Right Sum Differences

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/left-and-right-sum-differences/](https://leetcode.com/problems/left-and-right-sum-differences/)  
**Topics:** Array, Prefix Sum

---

## 📝 Problem Statement

You are given a **0-indexed** integer array `nums` of size `n`.

Define two arrays `leftSum` and `rightSum` where:

	- `leftSum[i]` is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, `leftSum[i] = 0`.

	- `rightSum[i]` is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, `rightSum[i] = 0`.

Return an integer array `answer` of size `n` where `answer[i] = |leftSum[i] - rightSum[i]|`.

 
Example 1:

```

**Input:** nums = [10,4,8,3]
**Output:** [15,1,11,22]
**Explanation:** The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

```

Example 2:

```

**Input:** nums = [1]
**Output:** [0]
**Explanation:** The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

```

 
**Constraints:**

	- `1 5`

---

## 💻 Implementation (python3)

```py
class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        """
        Calculates the absolute difference between the sum of elements to the left
        and the sum of elements to the right of each index.
        
        Time Complexity: O(n)
        Auxiliary Space Complexity: O(1) (excluding the output array)
        """
        left_sum = 0
        right_sum = sum(nums)
        answer = []
        
        for num in nums:
            # Exclude current element from right_sum to represent the sum of elements to its right
            right_sum -= num
            
            # Compute the absolute difference between left and right prefix sums
            answer.append(abs(left_sum - right_sum))
            
            # Include current element in left_sum for subsequent elements
            left_sum += num
            
        return answer
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A naive approach would compute the sum of elements to the left and to the right for every index independently, which requires $O(n)$ work per element, leading to an $O(n^2)$ time complexity.

Another common intermediate approach is to precompute two prefix sum arrays: `leftSum` and `rightSum`, each of size $n$, and then compute $|leftSum[i] - rightSum[i]|$ in a third pass. This takes $O(n)$ time and $O(n)$ extra auxiliary space.

We can optimize auxiliary space down to $O(1)$ by observing that:
1. The total sum of the array is known upfront: `total_sum = sum(nums)`.
2. At any index `i`, `rightSum[i]` is simply `total_sum - leftSum[i] - nums[i]`.
3. By maintaining running totals for `left_sum` and `right_sum`, we can compute each element of the result in a single pass without allocating additional auxiliary arrays.

### Step-by-Step Approach

1. Initialize `left_sum = 0` and `right_sum = sum(nums)`.
2. Iterate through each `num` in `nums`:
   - Subtract `num` from `right_sum` so it now holds the sum of strictly right elements.
   - Append `abs(left_sum - right_sum)` to the result list.
   - Add `num` to `left_sum` so it includes `num` for all subsequent positions.
3. Return the result list.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `nums`.
  - Computing the initial `sum(nums)` takes $\mathcal{O}(n)$.
  - The single pass over the array takes $\mathcal{O}(n)$ operations.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.
  - Only two scalar integer variables (`left_sum`, `right_sum`) are used.
  - The output array of size $n$ is required by the problem statement and is not counted toward auxiliary space.

### Common Pitfalls / Mistakes Candidates Make

1. **Off-by-One in Boundaries:** Accidentally including the current element `nums[i]` in either `leftSum[i]` or `rightSum[i]`. At index `0`, `leftSum[0]` must be `0`, and at index `n - 1`, `rightSum[n - 1]` must be `0`.
2. **Allocating Redundant Arrays:** Creating full `leftSum` and `rightSum` arrays when running variables suffice. In an interview, demonstrating memory awareness by maintaining running sums elevates the solution.
3. **Integer Overflow (in other languages):** In languages like C++ or Java, `sum(nums)` can reach $1000 \times 10^5 = 10^8$, which fits comfortably inside a standard 32-bit signed integer (max $\approx 2 \times 10^9$). However, if the constraints were $n \le 10^5$ and $nums[i] \le 10^9$, using a 64-bit integer (`long long` in C++ / `long` in Java) would be strictly required to prevent overflow. Always clarify bounds.

### Real Interview Follow-Up Questions

#### 1. What if the input array is extremely large and cannot fit into memory (streaming data)?
- **Answer:** If `nums` is a stream of unknown or massive length, we cannot compute `right_sum` on a single forward pass without seeing the entire stream first. 
  - If we have two passes available (e.g., stored on disk/SSD), Pass 1 calculates the total sum, and Pass 2 streams through the data again while writing the output directly to a sink/stream using running sums.
  - If only a single pass over the stream is permitted and we must produce outputs on the fly, it is fundamentally impossible because `answer[0]` strictly depends on knowing all elements up to the end of the stream.

#### 2. Can we modify the input array in-place to achieve $\mathcal{O}(1)$ total space?
- **Answer:** Yes, if modifying the input is allowed. We can store the final answers directly in `nums`:
  ```python
  total_sum = sum(nums)
  left_sum = 0
  for i in range(len(nums)):
      num = nums[i]
      right_sum = total_sum - left_sum - num
      nums[i] = abs(left_sum - right_sum)
      left_sum += num
  return nums
  ```

#### 3. How would you parallelize this computation for a massive array across multiple CPU cores?
- **Answer:** We can compute the prefix sums using a parallel prefix sum algorithm (Blelloch scan / work-efficient prefix sum):
  - Phase 1 (Up-Sweep / Reduction): Partition the array into $P$ chunks. Each processor computes the local sum of its chunk, followed by a tree-based reduction to get the global sum.
  - Phase 2 (Down-Sweep): Broadcast prefix offsets to each chunk.
  - Phase 3: Each processor independently computes the answers for its chunk in parallel since `left_sum` at the start of chunk $k$ is known and total sum is known.
