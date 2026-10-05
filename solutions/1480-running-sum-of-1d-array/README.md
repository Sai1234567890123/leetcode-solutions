# 1480. Running Sum of 1d Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/running-sum-of-1d-array/](https://leetcode.com/problems/running-sum-of-1d-array/)  
**Topics:** Array, Prefix Sum

---

## 📝 Problem Statement

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

 
Example 1:

```

**Input:** nums = [1,2,3,4]
**Output:** [1,3,6,10]
**Explanation:** Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

Example 2:

```

**Input:** nums = [1,1,1,1,1]
**Output:** [1,2,3,4,5]
**Explanation:** Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

Example 3:

```

**Input:** nums = [3,1,2,10,1]
**Output:** [3,4,6,16,17]

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # Perform in-place prefix accumulation to achieve O(1) auxiliary space.
        # nums[i] becomes the sum of all elements from index 0 to i.
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        return nums
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks for the prefix sum array (running sum) of `nums`, where each element at index `i` is the sum of all previous elements up to `i`.

A naive brute-force approach would calculate the sum from `0` to `i` for every index `i`, which requires nested iterations resulting in an $O(n^2)$ time complexity. 

We can optimize this to $O(n)$ using dynamic programming / recurrence relation:
$$\text{runningSum}[i] = \text{runningSum}[i - 1] + nums[i] \quad (\text{for } i \ge 1)$$
with the base case:
$$\text{runningSum}[0] = nums[0]$$

By modifying the input array in place, we can perform this operation using $O(1)$ auxiliary space.

### Step-by-Step Approach
1. Iterate through `nums` starting from index `1` to `len(nums) - 1`.
2. Add the value of the previous element `nums[i - 1]` to the current element `nums[i]`.
3. Return the modified `nums` array.

### Complexity Analysis
- **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. We visit each element starting from index 1 exactly once, doing constant time $O(1)$ work per element.
- **Space Complexity:** $O(1)$ auxiliary space. The calculation is done in place without allocating additional memory for another array. (If modifying input is disallowed, returning a new array would take $O(n)$ total space / $O(1)$ auxiliary space).

### Common Pitfalls / Mistakes Candidates Make
- **Recomputing from scratch:** Using `sum(nums[:i+1])` inside a loop. Slicing and summing each time makes the time complexity $O(n^2)$.
- **Unclear input mutation policy:** In interviews, always ask the interviewer before mutating the input array. Some systems require input immutability for thread safety or functional purity.
- **Integer overflow:** While Python handles arbitrarily large integers automatically, in languages like C++ or Java, prefix sums can exceed the 32-bit signed integer range (`2^31 - 1`). Candidates should check constraints: here, $1000 \times 10^6 = 10^9$, which fits within a standard 32-bit signed integer.

### Real Interview Follow-Up Questions & Answers

#### 1. What if you are not allowed to mutate the input array?
**Answer:** Allocate a new array of size $n$, initialize `res[0] = nums[0]`, and compute `res[i] = res[i - 1] + nums[i]`. Alternatively, use Python's built-in `itertools.accumulate(nums)`. This takes $O(n)$ time and $O(n)$ space.

#### 2. How would you handle a continuous stream of incoming numbers?
**Answer:** Maintain a running state variable `current_sum = 0`. When a new number $x$ arrives:
```python
current_sum += x
yield current_sum
```
This processes each incoming element in $O(1)$ time and $O(1)$ space.

#### 3. How would you handle range sum queries efficiently after computing this?
**Answer:** The running sum array directly enables $O(1)$ range sum queries:
$$\sum_{k=i}^j nums[k] = \text{runningSum}[j] - (\text{runningSum}[i - 1] \text{ if } i > 0 \text{ else } 0)$$
This is the foundational Prefix Sum pattern used heavily in range query problems.

#### 4. How would you parallelize this for an extremely large array (e.g., billions of numbers)?
**Answer:** Use the **Parallel Prefix Sum (Scan) Algorithm** (such as Blelloch Scan or Hillis-Steele Scan). 
1. Divide the array into $P$ chunks processed across $P$ cores.
2. Each core computes the local prefix sum and the total sum of its chunk.
3. Compute prefix sums of the chunk totals across processors.
4. Add the chunk offset to each chunk's local prefix sums in parallel.
This reduces latency from $O(n)$ to $O(n/P + \log P)$.
