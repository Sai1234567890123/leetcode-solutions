# 1512. Number of Good Pairs

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/number-of-good-pairs/](https://leetcode.com/problems/number-of-good-pairs/)  
**Topics:** Array, Hash Table, Math, Counting

---

## 📝 Problem Statement

Given an array of integers `nums`, return *the number of **good pairs***.

A pair `(i, j)` is called *good* if `nums[i] == nums[j]` and `i` 

 
Example 1:

```

**Input:** nums = [1,2,3,1,1,3]
**Output:** 4
**Explanation:** There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

```

Example 2:

```

**Input:** nums = [1,1,1,1]
**Output:** 6
**Explanation:** Each pair in the array are *good*.

```

Example 3:

```

**Input:** nums = [1,2,3]
**Output:** 0

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Calculates the number of good pairs (i, j) where nums[i] == nums[j] and i < j.
        """
        count_map = defaultdict(int)
        good_pairs = 0
        
        for num in nums:
            # Each time we encounter `num`, it forms a good pair with every
            # occurrence of `num` seen previously.
            good_pairs += count_map[num]
            count_map[num] += 1
            
        return good_pairs
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A pair `(i, j)` is "good" if $nums[i] == nums[j]$ and $i < j$.

A naive approach would check every pair $(i, j)$ using two nested loops, running in $O(n^2)$ time. 

However, notice that whenever we encounter an element $x$ at index $j$, it can pair with *every* previous occurrence of $x$ at indices $i < j$. 
- If we have seen $x$ zero times before, it forms $0$ new pairs.
- If we have seen $x$ twice before, it forms $2$ new pairs with those two earlier occurrences.

Alternatively, if a number appears $k$ times in total, the number of distinct pairs we can form from these $k$ occurrences is given by the combination formula:
$$\binom{k}{2} = \frac{k(k - 1)}{2}$$

By maintaining a running frequency counter in a single pass, we can accumulate `count_map[num]` to our total before incrementing its frequency.

---

### Step-by-Step Approach

1. Initialize an empty hash map (or array if values are bounded) `count_map` and a counter `good_pairs = 0`.
2. Iterate through each element `num` in `nums`:
   - Add the current count of `num` from `count_map` to `good_pairs`.
   - Increment `count_map[num]` by 1.
3. Return `good_pairs`.

---

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. We perform a single pass over the array, and dictionary lookups/insertions take $O(1)$ on average.
- **Space Complexity:** $O(u)$, where $u$ is the number of unique elements in `nums`. In the worst case (all elements unique), $u \le n$, giving $O(n)$ space. Given the problem constraints ($nums[i] \le 100$), this space is bounded by $O(1)$ (at most 100 unique integers).

---

### Common Pitfalls / Mistakes

1. **$O(n^2)$ Brute Force:** Implementing two nested loops. While it passes for $n \le 100$, interviewers expect the optimal $O(n)$ hash map solution.
2. **Integer Overflow in other languages:** In languages like C++ or Java, if $n$ is very large (e.g., $10^5$), $k(k-1)/2$ can exceed a 32-bit signed integer (`2^31 - 1`), necessitating 64-bit integers (`long long` / `long`). Python handles arbitrarily large integers automatically.
3. **Double Counting:** Iterating over all pairs without enforcing $i < j$, or forgetting to divide by 2 if computing combinations manually.

---

### Real Interview Follow-Up Questions

#### 1. What if the input arrives as an infinite stream?
- **Answer:** The single-pass approach used in the code already processes elements in a streaming manner. As each element arrives, we increment our answer by its current frequency and update the frequency map. This processes each incoming element in $O(1)$ time and $O(u)$ space.

#### 2. What if memory is extremely constrained?
- **Answer:** If we cannot afford auxiliary hash map storage and modifying the input in-place is allowed, we can sort `nums` in-place in $O(n \log n)$ time and $O(1)$ auxiliary space. Once sorted, identical elements will be adjacent, allowing us to count contiguous runs of identical values and compute $k(k-1)/2$ for each run.

#### 3. How would you distribute this computation across multiple machines (MapReduce / Big Data scale)?
- **Answer:** 
  - **Map Phase:** Each worker node processes a shard of data and emits `(num, 1)` or local frequency sums `(num, local_count)`.
  - **Reduce Phase:** Group by `num` to aggregate the total global frequency $K$ for each unique key. Emit $\frac{K(K - 1)}{2}$.
  - **Global Aggregation:** Sum the resulting values across all keys.
