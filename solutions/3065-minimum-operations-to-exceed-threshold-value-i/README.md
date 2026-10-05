# 3065. Minimum Operations to Exceed Threshold Value I

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/)  
**Topics:** Array

---

## 📝 Problem Statement

You are given a **0-indexed** integer array `nums`, and an integer `k`.

In one operation, you can remove one occurrence of the smallest element of `nums`.

Return *the **minimum** number of operations needed so that all elements of the array are greater than or equal to* `k`.

 
Example 1:

```

**Input:** nums = [2,11,10,1,3], k = 10
**Output:** 3
**Explanation:** After one operation, nums becomes equal to [2, 11, 10, 3].
After two operations, nums becomes equal to [11, 10, 3].
After three operations, nums becomes equal to [11, 10].
At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
It can be shown that 3 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.

```

Example 2:

```

**Input:** nums = [1,1,2,4,9], k = 1
**Output:** 0
**Explanation:** All elements of the array are greater than or equal to 1 so we do not need to apply any operations on nums.
```

Example 3:

```

**Input:** nums = [1,1,2,4,9], k = 9
**Output:** 4
**Explanation:** only a single element of nums is greater than or equal to 9 so we need to apply the operations 4 times on nums.

```

 
**Constraints:**

	- `1 9`

	- `1 9`

	- The input is generated such that there is at least one index `i` such that `nums[i] >= k`.

---

## 💻 Implementation (python3)

```py
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations to ensure all elements are >= k.
        Each operation removes the smallest element, so every element strictly less
        than k must be removed.
        """
        # Count elements strictly less than k
        return sum(1 for x in nums if x < k)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem states that in each step, we remove one occurrence of the smallest element in `nums` until all remaining elements are greater than or equal to `k`.

Notice the invariant:
- If there is any element $x < k$, it must eventually be removed.
- Since we always remove the *smallest* element, every element strictly less than $k$ will be removed before any element greater than or equal to $k$ is touched.
- Once all elements strictly less than $k$ have been removed, the minimum element remaining in the array will be at least $k$, satisfying the condition.

Thus, the problem reduces to simply counting how many elements in `nums` are strictly less than `k`.

### Step-by-Step Approach

1. Iterate through the array `nums`.
2. Maintain a count of elements where `x < k`.
3. Return the total count.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of `nums`. We inspect each element in the array exactly once.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The calculation uses a generator expression evaluated on the fly without allocating additional memory buffers.

### Common Pitfalls / Mistakes Candidates Make

1. **Overcomplicating with a Min-Heap / Priority Queue:** Candidates often see "remove the smallest element" and immediately jump to `heapq`. While `heapify` followed by popping while `heap[0] < k` works, it takes $\mathcal{O}(N + M \log N)$ time, which is strictly worse than the optimal linear scan $\mathcal{O}(N)$.
2. **Sorting the Array:** Another suboptimal instinct is sorting `nums` ($\mathcal{O}(N \log N)$) and using binary search (`bisect_left`). While functionally correct, sorting introduces unnecessary time and space overhead compared to a single $\mathcal{O}(N)$ pass.
3. **Strict vs. Non-Strict Inequality:** Confusing `< k` with `<= k`. The problem requires all remaining elements to be *greater than or equal to* $k$, meaning elements equal to $k$ do not need to be removed.

### Real Interview Follow-Up Questions

#### 1. What if `nums` is already sorted?
- **Answer:** If the array is sorted, we can use binary search (`bisect_left`) to find the first index where `nums[i] >= k`. The index directly gives the number of elements strictly less than $k$.
- **Time Complexity:** $\mathcal{O}(\log N)$.
- **Space Complexity:** $\mathcal{O}(1)$.

#### 2. How would you handle a streaming input where numbers arrive continuously?
- **Answer:**
  - If $k$ is fixed ahead of time, we don't need to store the numbers. We maintain a running counter `less_than_k_count` and increment it whenever an incoming stream item is strictly less than $k$.
  - If $k$ can be queried dynamically or varies over time, we can maintain an Order Statistic Tree (or a Fenwick Tree / Segment Tree over discretized values) to query the count of numbers smaller than any given $k$ in $\mathcal{O}(\log U)$ time, where $U$ is the number of unique elements.

#### 3. What if the dataset is massive and distributed across multiple machines (MapReduce / Big Data)?
- **Answer:** Counting elements satisfying a predicate is an embarrassingly parallel problem:
  - **Map phase:** Each worker counts the number of elements $< k$ in its local chunk.
  - **Reduce phase:** Sum the local counts from all mappers to produce the final answer.
