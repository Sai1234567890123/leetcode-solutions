# 2149. Rearrange Array Elements by Sign

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/rearrange-array-elements-by-sign/](https://leetcode.com/problems/rearrange-array-elements-by-sign/)  
**Topics:** Array, Two Pointers, Simulation

---

## 📝 Problem Statement

You are given a **0-indexed** integer array `nums` of **even** length consisting of an **equal** number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

	- Every **consecutive pair** of integers have **opposite signs**.

	- For all integers with the same sign, the **order** in which they were present in `nums` is **preserved**.

	- The rearranged array begins with a positive integer.

Return *the modified array after rearranging the elements to satisfy the aforementioned conditions*.

 
Example 1:

```

**Input:** nums = [3,1,-2,-5,2,-4]
**Output:** [3,-2,1,-5,2,-4]
**Explanation:**
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

```

Example 2:

```

**Input:** nums = [-1,1]
**Output:** [1,-1]
**Explanation:**
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].

```

 
**Constraints:**

	- `2 5`

	- `nums.length` is **even**

	- `1 5`

	- `nums` consists of **equal** number of positive and negative integers.

 
It is not required to do the modifications in-place.

---

## 💻 Implementation (python3)

```py
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # Pre-allocate output array to avoid repeated append/resize overhead
        result = [0] * n
        
        # Positive integers start at even indices: 0, 2, 4, ...
        # Negative integers start at odd indices: 1, 3, 5, ...
        pos_idx = 0
        neg_idx = 1
        
        # Single pass: place each number into its designated slot preserving relative order
        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2
            else:
                result[neg_idx] = num
                neg_idx += 2
                
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires:
1. Alternating signs starting with a positive number.
2. Preserving the relative order of numbers with the same sign (stability).
3. An equal count of positive and negative numbers.

Because the result array must alternate starting with a positive integer:
- All positive numbers will naturally land at even indices: `0, 2, 4, ...`
- All negative numbers will land at odd indices: `1, 3, 5, ...`

Rather than separating the numbers into two temporary lists (e.g., `pos = [...]` and `neg = [...]`) and merging them (which requires $O(n)$ auxiliary space before creating the answer array, totaling $2n$ allocations), we can pre-allocate the answer array of size $n$ and use two pointers (`pos_idx = 0` and `neg_idx = 1`) in a single pass. As we encounter elements in the input array sequentially, placing them into the corresponding next available even or odd index inherently preserves their original order.

### Step-by-Step Approach

1. Initialize `result = [0] * n`.
2. Initialize pointer `pos_idx = 0` for the next positive integer slot.
3. Initialize pointer `neg_idx = 1` for the next negative integer slot.
4. Iterate through `nums` element by element:
   - If `num > 0`, assign `result[pos_idx] = num` and advance `pos_idx += 2`.
   - If `num < 0`, assign `result[neg_idx] = num` and advance `neg_idx += 2`.
5. Return `result`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$
  We iterate through the array of length $n$ exactly once. Each insertion and pointer update takes $\mathcal{O}(1)$ time.
- **Space Complexity:** $\mathcal{O}(n)$
  $\mathcal{O}(n)$ space is required to store and return the rearranged output array. Beyond the output array, only $\mathcal{O}(1)$ auxiliary space is used for the index pointers.

---

### Common Pitfalls / Mistakes

1. **Attempting an In-Place Swap:**
   Candidates often try to solve this in-place with $\mathcal{O}(1)$ extra space using standard two-pointer partitioning (like in QuickSort). However, standard partition algorithms are **not stable** and destroy the relative order of elements, violating the stability requirement. Stable in-place rearrangement is mathematically proven to require $\mathcal{O}(n^2)$ time or complex block-interchange algorithms which are inefficient and error-prone. The problem explicitly states that in-place modification is not required.
2. **Two-Pass Separation Overhead:**
   Extracting all positives into one list and negatives into another before interleaving them works, but it causes extra cache misses and allocates triple the memory needed ($pos$ array, $neg$ array, and $result$ array). The single-pass two-pointer approach is cleaner and more cache-friendly.

---

### Real Interview Follow-Up Questions

#### 1. What if the number of positive and negative elements is unequal?
**Answer:**
We can still use the two pointers until one sign runs out (i.e., `pos_idx >= n` or `neg_idx >= n`). Once one runs out, we append all remaining elements of the other sign to the end of the array, maintaining their relative order.

#### 2. Can we solve this in-place with $\mathcal{O}(1)$ extra space while maintaining stability?
**Answer:**
Achieving both $\mathcal{O}(1)$ auxiliary space and stability requires either:
- **$\mathcal{O}(n^2)$ Time:** Whenever an element is in the wrong position, find the next required element and perform a cyclic right shift (insertion sort approach).
- **$\mathcal{O}(n \log^2 n)$ Time:** Using divide-and-conquer block rotations (e.g., using Gries-Mills or reversal algorithm for array rotation).
In production and standard technical interviews, trading $\mathcal{O}(n)$ auxiliary memory for $\mathcal{O}(n)$ linear runtime is the universally preferred solution.

#### 3. How would you handle this in a distributed or streaming environment where data doesn't fit in memory?
**Answer:**
In a streaming scenario, elements arrive in a stream $S$. We can maintain two bounded FIFO queues (or disk-backed buffers): `pos_queue` and `neg_queue`.
- Push incoming items to their respective queue based on sign.
- Whenever both `pos_queue` and `neg_queue` are non-empty, dequeue one from `pos_queue` followed by one from `neg_queue` and emit them to the output stream.
- This maintains stability and stream order while consuming memory proportional only to the temporary skew between positive and negative arrival rates.
