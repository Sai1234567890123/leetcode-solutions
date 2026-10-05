# 1431. Kids With the Greatest Number of Candies

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)  
**Topics:** Array

---

## 📝 Problem Statement

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `ith` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return *a boolean array *`result`* of length *`n`*, where *`result[i]`* is *`true`* if, after giving the *`ith`* kid all the *`extraCandies`*, they will have the **greatest** number of candies among all the kids**, or *`false`* otherwise*.

Note that **multiple** kids can have the **greatest** number of candies.

 
Example 1:

```

**Input:** candies = [2,3,5,1,3], extraCandies = 3
**Output:** [true,true,true,false,true] 
**Explanation:** If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

```

Example 2:

```

**Input:** candies = [4,2,1,1,2], extraCandies = 1
**Output:** [true,false,false,false,false] 
**Explanation:** There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

```

Example 3:

```

**Input:** candies = [12,1,12], extraCandies = 10
**Output:** [true,false,true]

```

 
**Constraints:**

	- `n == candies.length`

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Precompute the current maximum number of candies any kid has.
        max_candies = max(candies)
        
        # A kid can have the greatest number of candies if their current candies + extraCandies >= max_candies.
        # Alternatively: candies[i] >= max_candies - extraCandies
        threshold = max_candies - extraCandies
        
        # Construct the result list using a list comprehension.
        return [candy >= threshold for candy in candies]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks whether giving all `extraCandies` to a particular kid allows them to have the greatest (or tied for greatest) number of candies among all kids.

To determine this for any kid $i$:
1. We first identify the current maximum candies any kid has: $M = \max(\text{candies})$.
2. If kid $i$ receives all `extraCandies`, their total becomes $\text{candies}[i] + \text{extraCandies}$.
3. For this total to be the greatest among all kids, it must be at least $M$:
   $$\text{candies}[i] + \text{extraCandies} \ge M \iff \text{candies}[i] \ge M - \text{extraCandies}$$

By precomputing $M$ once, we can answer the query for each kid in $O(1)$ time.

### Step-by-Step Approach

1. **Find Maximum:** Traverse the `candies` array once using `max(candies)` to find the largest value.
2. **Compute Threshold:** Calculate `threshold = max_candies - extraCandies`. Any kid with at least this many candies can reach or exceed the maximum.
3. **Generate Output:** Iterate through `candies` and evaluate `candy >= threshold`, collecting the results into a boolean list.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the number of kids (`len(candies)`).
  - Finding the maximum takes $O(n)$ time.
  - The list comprehension performs a single pass over $n$ elements, taking $O(n)$ time.
  - Overall time complexity is strictly linear $O(n)$.
- **Space Complexity:** $O(1)$ auxiliary space.
  - The output array requires $O(n)$ space to store the result, which is mandatory per problem specifications. No other non-trivial memory is allocated.

### Common Pitfalls / Mistakes Candidates Make

1. **Recomputing `max` inside the loop:** Writing `[c + extraCandies >= max(candies) for c in candies]` results in an $O(n^2)$ time complexity because `max()` is called on every iteration.
2. **Strict Inequality:** Using `>` instead of `>=`. The problem explicitly states: *"multiple kids can have the greatest number of candies"*, meaning ties count as having the greatest number.
3. **Overcomplicating the logic:** Simulating the addition for each kid and finding the new maximum each time, which degrades both readability and performance.

### Real Interview Follow-Up Questions

1. **What if `candies` is a continuous data stream where elements arrive in real-time?**
   - *Answer:* In a streaming context, the global maximum may change as new elements arrive. If queries must be answered retroactively, we cannot output a definitive boolean until the stream ends or a window expires. If we only need to answer for the *current* window or dynamic stream, we can maintain a sliding window maximum using a monotonic deque in $O(1)$ amortized time per element.

2. **What if `extraCandies` can be split among multiple kids?**
   - *Answer:* The question changes fundamentally. If the goal is to make as many kids as possible reach the maximum, or reach a target, this becomes a greedy or binary search on answer problem.

3. **What if the array is too large to fit in memory (e.g., distributed across multiple machines in MapReduce / Spark)?**
   - *Answer:*
     - **Pass 1 (Reduce):** Find the global maximum candy count across all partitions by computing the local max on each mapper and reducing to find the global max.
     - **Pass 2 (Map):** Broadcast the global max (and `extraCandies`) to all worker nodes. Each worker can then independently transform its partition of candies into the boolean output.
