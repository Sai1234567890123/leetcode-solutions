# 3285. Find Indices of Stable Mountains

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-indices-of-stable-mountains/](https://leetcode.com/problems/find-indices-of-stable-mountains/)  
**Topics:** Array

---

## 📝 Problem Statement

There are `n` mountains in a row, and each mountain has a height. You are given an integer array `height` where `height[i]` represents the height of mountain `i`, and an integer `threshold`.

A mountain is called **stable** if the mountain just before it (**if it exists**) has a height **strictly greater** than `threshold`. **Note** that mountain 0 is **not** stable.

Return an array containing the indices of *all* **stable** mountains in **any** order.

 
Example 1:

**Input:** height = [1,2,3,4,5], threshold = 2

**Output:** [3,4]

**Explanation:**

	- Mountain 3 is stable because `height[2] == 3` is greater than `threshold == 2`.

	- Mountain 4 is stable because `height[3] == 4` is greater than `threshold == 2`.

Example 2:

**Input:** height = [10,1,10,1,10], threshold = 3

**Output:** [1,3]

Example 3:

**Input:** height = [10,1,10,1,10], threshold = 10

**Output:** []

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        # Mountain 0 can never be stable because there is no mountain before it.
        # Check each mountain from index 1 to n - 1:
        # Mountain i is stable if height[i - 1] > threshold.
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem defines a "stable" mountain at index $i$ based entirely on the height of its preceding neighbor, mountain $i - 1$. Specifically:
1. Mountain $0$ has no predecessor, so it is never stable.
2. For any index $i \ge 1$, mountain $i$ is stable if and only if `height[i - 1] > threshold`.

Because each mountain's stability depends only on a single localized comparison with the element directly to its left, a single linear scan from index $1$ to $n - 1$ suffices.

### Step-by-Step Approach
1. Iterate through indices $i$ from $1$ up to `len(height) - 1`.
2. At each index $i$, check the condition `height[i - 1] > threshold`.
3. If the condition holds, record index $i$.
4. Return the list of collected indices.

### Complexity Analysis
- **Time Complexity:** $O(n)$, where $n$ is the number of elements in `height`. We perform a single pass over the array and do constant-time $O(1)$ operations at each step.
- **Space Complexity:** $O(1)$ auxiliary space (ignoring the space required for the output array). If the output list is considered, the space used is at most $O(n)$ when all mountains from $1$ to $n - 1$ satisfy the condition.

### Common Pitfalls / Mistakes
- **Checking `height[i]` instead of `height[i - 1]`:** A common reading comprehension error where candidates check if the current mountain's height exceeds the threshold rather than its predecessor's height.
- **Off-by-one errors with index 0:** Including index 0 or starting iteration from 0 and trying to access `height[-1]`, which in Python wraps around to the last element of the list.
- **Strict vs. Non-Strict Inequality:** Using `>=` instead of `>` for the threshold comparison. The problem explicitly states "strictly greater".

### Real Interview Follow-Up Questions

#### 1. What if the input stream is continuous and infinite?
*Answer:* Maintain the previous element's height in a variable (`prev_height`) and a running index counter (`current_index`). For each incoming element in the stream, check if `prev_height > threshold`. If so, yield/emit `current_index`. Then update `prev_height = current_height` and increment `current_index`. This processes an infinite stream in $O(1)$ space and $O(1)$ time per element.

#### 2. What if the array is stored across multiple distributed nodes / partitions?
*Answer:* Each partition can be processed independently in parallel. The only boundary dependency is that the first mountain of partition $P_k$ depends on the last mountain of partition $P_{k-1}$. Passing the last element of each chunk to the subsequent chunk resolves the boundary condition cleanly in map-reduce style.

#### 3. What if a mountain is stable if the *average* height of the last $k$ mountains exceeds the threshold?
*Answer:* Use a sliding window sum of size $k$. Maintain the sum of the last $k$ elements, update it in $O(1)$ time per element by adding the new element and subtracting the element that falls out of the window, and check whether `window_sum > threshold * k` (avoiding floating-point division issues).
