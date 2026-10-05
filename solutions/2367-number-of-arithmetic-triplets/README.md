# 2367. Number of Arithmetic Triplets

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/number-of-arithmetic-triplets/](https://leetcode.com/problems/number-of-arithmetic-triplets/)  
**Topics:** Array, Hash Table, Two Pointers, Enumeration

---

## 📝 Problem Statement

You are given a **0-indexed**, **strictly increasing** integer array `nums` and a positive integer `diff`. A triplet `(i, j, k)` is an **arithmetic triplet** if the following conditions are met:

	- `i 

Return *the number of unique **arithmetic triplets**.*

 
Example 1:

```

**Input:** nums = [0,1,4,6,7,10], diff = 3
**Output:** 2
**Explanation:**
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 

```

Example 2:

```

**Input:** nums = [4,5,6,7,8,9], diff = 2
**Output:** 2
**Explanation:**
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

```

 
**Constraints:**

	- `3

---

## 💻 Implementation (python3)

```py
class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        """
        Finds the number of unique arithmetic triplets (i, j, k) such that
        nums[j] - nums[i] == diff and nums[k] - nums[j] == diff.
        
        Leverages the strictly increasing property of nums using a 3-pointer
        sliding approach to achieve O(n) time and O(1) auxiliary space.
        """
        triplet_count = 0
        i = 0
        j = 0
        n = len(nums)

        # k acts as the rightmost element in the triplet (nums[k])
        for k in range(n):
            # Advance j until nums[k] - nums[j] <= diff
            while j < k and nums[k] - nums[j] > diff:
                j += 1
            
            # If a valid middle element nums[j] is found
            if nums[k] - nums[j] == diff:
                # Advance i until nums[j] - nums[i] <= diff
                while i < j and nums[j] - nums[i] > diff:
                    i += 1
                
                # If a valid leftmost element nums[i] is found
                if nums[j] - nums[i] == diff:
                    triplet_count += 1
                    
        return triplet_count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for triplets `(i, j, k)` with `i < j < k` such that `nums[j] - nums[i] == diff` and `nums[k] - nums[j] == diff`.
A key observation is that the array is **strictly increasing**, which provides two critical properties:
1. All elements are unique.
2. If `nums[k]` increases, any matching `nums[j]` and `nums[i]` must also move forward (monotonically non-decreasing indices).

There are two primary approaches to consider:
1. **Hash Set Approach ($O(n)$ time, $O(n)$ space)**:
   Store all numbers in a hash set. For every element $x \in nums$, check if $x - \text{diff} \in \text{set}$ and $x + \text{diff} \in \text{set}$. Since all elements are unique and ordered, each such element $x$ uniquely defines an arithmetic triplet centered at $x$.
2. **Three-Pointer Approach ($O(n)$ time, $O(1)$ auxiliary space)**:
   Since the input is already sorted, we can maintain three pointers `i`, `j`, and `k`. For every `k`, we advance `j` until `nums[k] - nums[j] <= diff`. If an exact match is found, we then advance `i` until `nums[j] - nums[i] <= diff`. Because `i`, `j`, and `k` only move from left to right across the array, each pointer traverses the array at most once.

The three-pointer approach is optimal in both time and auxiliary space.

---

### Step-by-Step Approach

1. Initialize two pointers, `i = 0` and `j = 0`, and the counter `triplet_count = 0`.
2. Iterate `k` from `0` to `n - 1`, treating `nums[k]` as the potential end element of the triplet.
3. While `nums[k] - nums[j] > diff` and `j < k`, increment `j`.
4. If `nums[k] - nums[j] == diff`, we have found a valid middle element. We then move `i` while `nums[j] - nums[i] > diff` and `i < j`.
5. If `nums[j] - nums[i] == diff`, all conditions for an arithmetic triplet are satisfied: increment `triplet_count`.
6. Return `triplet_count`.

---

### Complexity Analysis

- **Time Complexity:** $O(n)$. Each pointer (`i`, `j`, and `k`) traverses the array from index `0` to `n - 1` without ever resetting or moving backwards. The total number of pointer increments across the entire loop is bounded by $3n$, yielding linear time complexity.
- **Space Complexity:** $O(1)$ auxiliary space. We only use a few integer variables (`i`, `j`, `k`, `triplet_count`) to track indices and results.

---

### Common Pitfalls / Mistakes

1. **Brute Force $O(n^3)$**: Candidates often start with 3 nested loops checking every combination. While it passes the constraints for $n \le 200$, it will not pass Google/Meta interviews without being optimized to $O(n)$.
2. **Ignoring the "Strictly Increasing" Constraint**: Failing to notice that elements are distinct and sorted leads candidates to miss the $O(1)$ space two/three-pointer optimization and resort solely to hash maps or binary searches ($O(n \log n)$).
3. **Bound Checks**: Forgetting to ensure `j < k` or `i < j` before accessing array indices or comparing values.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the array contains duplicates (non-decreasing instead of strictly increasing)?
- **Answer:** If duplicates exist, multiple identical values can form distinct index triplets. We would need to count the frequency of each value. 
  - Using a hash map: For each unique value $x$, if both $x - \text{diff}$ and $x + \text{diff}$ exist, the number of triplets centered at $x$ is `count[x - diff] * count[x] * count[x + diff]`.
  - Using two/three pointers: When matches are found, count identical consecutive elements for `i`, `j`, and `k`, then add `count_i * count_j * count_k` to the total.

#### 2. What if the input array is unsorted?
- **Answer:** The three-pointer technique requires sorted order. If unsorted, the hash set approach is superior: insert elements into a hash set in $O(n)$ time and auxiliary space, then iterate through the elements checking `x - diff in seen and x + diff in seen`. This keeps the runtime at $O(n)$ without having to sort the array in $O(n \log n)$.

#### 3. How would you handle a streaming dataset where elements arrive continuously?
- **Answer:** Maintain a sliding window or hash table of recently seen elements with a TTL (or within a buffer size). As a new number $z$ arrives:
  - Check if $z - \text{diff}$ and $z - 2 \cdot \text{diff}$ were already observed.
  - If handling out-of-order streams, check both directions: $(z - 2d, z - d, z)$, $(z - d, z, z + d)$, and $(z, z + d, z + 2d)$.
