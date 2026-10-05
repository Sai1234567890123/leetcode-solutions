# 3427. Sum of Variable Length Subarrays

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/sum-of-variable-length-subarrays/](https://leetcode.com/problems/sum-of-variable-length-subarrays/)  
**Topics:** Array, Prefix Sum

---

## 📝 Problem Statement

You are given an integer array `nums` of size `n`. For **each** index `i` where `0 subarray `nums[start ... i]` where `start = max(0, i - nums[i])`.

Return the total sum of all elements from the subarray defined for each index in the array.

 
Example 1:

**Input:** nums = [2,3,1]

**Output:** 11

**Explanation:**

	
		
			i
			Subarray
			Sum
		
		
			0
			`nums[0] = [2]`
			2
		
		
			1
			`nums[0 ... 1] = [2, 3]`
			5
		
		
			2
			`nums[1 ... 2] = [3, 1]`
			4
		
		
			**Total Sum**
			 
			11
		
	

The total sum is 11. Hence, 11 is the output.

Example 2:

**Input:** nums = [3,1,1,2]

**Output:** 13

**Explanation:**

	
		
			i
			Subarray
			Sum
		
		
			0
			`nums[0] = [3]`
			3
		
		
			1
			`nums[0 ... 1] = [3, 1]`
			4
		
		
			2
			`nums[1 ... 2] = [1, 1]`
			2
		
		
			3
			`nums[1 ... 3] = [1, 1, 2]`
			4
		
		
			**Total Sum**
			 
			13
		
	

The total sum is 13. Hence, 13 is the output.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        n = len(nums)
        # Build prefix sum array where prefix[k] = sum(nums[0 ... k-1])
        # prefix array will have size n + 1 with prefix[0] = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        total_sum = 0
        for i in range(n):
            # As specified in the problem statement
            start = max(0, i - nums[i])
            # Range sum for nums[start ... i] in O(1) time
            total_sum += prefix[i + 1] - prefix[start]
            
        return total_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires calculating the sum of elements in a variable-length subarray `nums[start ... i]` for each index `i` from `0` to `n - 1`, where `start = max(0, i - nums[i])`.

A naive brute-force approach iterates through every index `i`, then iterates from `start` to `i` to compute the sum. In the worst case, this leads to an $O(n^2)$ time complexity.

To optimize this to $O(n)$, we can precompute the **prefix sums** of `nums`. 
With a 1-indexed prefix sum array where `prefix[k] = nums[0] + nums[1] + ... + nums[k - 1]`:
$$\sum_{j = \text{start}}^{i} \text{nums}[j] = \text{prefix}[i + 1] - \text{prefix}[\text{start}]$$

Using prefix sums, each of the $n$ subarray sums can be evaluated in $O(1)$ time, yielding an optimal $O(n)$ overall runtime.

---

### Step-by-Step Approach

1. **Prefix Sum Precomputation**:
   - Initialize an array `prefix` of length $n + 1$ with zeros.
   - For each index $i \in [0, n - 1]$, compute `prefix[i + 1] = prefix[i] + nums[i]`.
2. **Compute Subarray Sums**:
   - Initialize `total_sum = 0`.
   - For each index $i \in [0, n - 1]$:
     - Determine the start index: `start = max(0, i - nums[i])`.
     - Add `prefix[i + 1] - prefix[start]` to `total_sum`.
3. **Return Result**:
   - Return `total_sum`.

---

### Complexity Analysis

- **Time Complexity:** $O(n)$
  - Generating the prefix sum array takes a single pass over `nums` ($O(n)$).
  - Iterating through each index $i$ and querying the range sum via prefix array takes $O(1)$ per index, leading to $O(n)$ for the second loop.
  - Overall Time Complexity: $\mathcal{O}(n)$.

- **Space Complexity:** $O(n)$
  - An auxiliary prefix sum array of size $n + 1$ is used to store cumulative sums.
  - Overall Auxiliary Space Complexity: $\mathcal{O}(n)$.

---

### Common Pitfalls / Mistakes

1. **Off-by-one errors with Prefix Sums**:
   - Forgetting that standard prefix arrays are usually size $n + 1$ so that `prefix[0] = 0`. Without the leading 0, querying a subarray starting at index `0` requires special branch handling.
2. **Boundary of `start`**:
   - Forgetting to bound `start` with `max(0, ...)`, which could result in negative indices that wrap around in Python.
3. **Integer Overflow in other languages (C++/Java)**:
   - While Python handles arbitrarily large integers automatically, in languages like C++ or Java, the sum of multiple subarrays could exceed the 32-bit signed integer maximum ($2^{31} - 1$). In such languages, `long long` / `long` should be used for `total_sum`.

---

### Real Interview Follow-Up Questions

#### 1. What if memory is extremely constrained and we must achieve $O(1)$ extra space?
- **Answer:** We can mutate `nums` in-place to store prefix sums (`nums[i] += nums[i - 1]`), calculate the total sum using in-place values, and optionally restore the original array if mutability is a constraint.

#### 2. What if `nums` is an incoming data stream of unknown/infinite length?
- **Answer:** 
  - Subarray definitions depend on `start = max(0, i - nums[i])`. At step $i$, we need values up to $nums[i]$ steps in the past.
  - If $nums[i]$ is bounded by a constant window size $W$, we can maintain a circular buffer or sliding prefix sum of size $W$.
  - If $nums[i]$ can be arbitrarily large, each index contributes to future answers. We can frame the problem using a difference array / contribution approach: how many times does `nums[k]` appear in future queries? Index $k$ is included in query $i$ iff $k \ge \max(0, i - nums[i]) \iff i - nums[i] \le k \le i$.

#### 3. How can we optimize this if `nums` is updated frequently (Point Updates and Range Queries)?
- **Answer:** If `nums` undergoes frequent updates, a static prefix sum array would require $O(n)$ time to update. A **Fenwick Tree (Binary Indexed Tree)** or **Segment Tree** can support both point updates and range sum queries in $O(\log n)$ time.
