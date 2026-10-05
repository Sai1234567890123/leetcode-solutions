# 3289. The Two Sneaky Numbers of Digitville

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/)  
**Topics:** Array, Hash Table, Math

---

## 📝 Problem Statement

In the town of Digitville, there was a list of numbers called `nums` containing integers from `0` to `n - 1`. Each number was supposed to appear **exactly once** in the list, however, **two** mischievous numbers sneaked in an *additional time*, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size **two** containing the two numbers (in *any order*), so peace can return to Digitville.

 
Example 1:

**Input:** nums = [0,1,1,0]

**Output:** [0,1]

**Explanation:**

The numbers 0 and 1 each appear twice in the array.

Example 2:

**Input:** nums = [0,3,2,1,3,2]

**Output:** [2,3]

**Explanation: **

The numbers 2 and 3 each appear twice in the array.

Example 3:

**Input:** nums = [7,1,5,4,3,4,6,0,9,5,8,2]

**Output:** [4,5]

**Explanation: **

The numbers 4 and 5 each appear twice in the array.

 
**Constraints:**

	`2 
	`nums.length == n + 2`
	0 
	The input is generated such that `nums` contains **exactly** two repeated elements.

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        """
        Finds the two duplicate numbers in nums in O(n) time and O(1) auxiliary space
        using bit manipulation (XOR partitioning).
        """
        n = len(nums) - 2
        
        # Step 1: XOR all elements in nums with all numbers from 0 to n - 1.
        # Elements appearing once in the ideal array and once in nums will cancel out (x ^ x = 0).
        # The two sneaky numbers appear twice in nums and once in the ideal sequence (total 3 times).
        # Thus, xor_all will equal x ^ y, where x and y are the two sneaky numbers.
        xor_all = 0
        for num in nums:
            xor_all ^= num
        for i in range(n):
            xor_all ^= i
            
        # Step 2: Find the lowest set bit (rightmost bit where x and y differ).
        diff_bit = xor_all & (-xor_all)
        
        # Step 3: Partition all numbers into two buckets based on diff_bit.
        # One bucket will isolate x, and the other will isolate y.
        x = 0
        y = 0
        
        for num in nums:
            if num & diff_bit:
                x ^= num
            else:
                y ^= num
                
        for i in range(n):
            if i & diff_bit:
                x ^= i
            else:
                y ^= i
                
        return [x, y]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem states that an ideal list contains numbers from $0$ to $n - 1$ exactly once. Two numbers, say $x$ and $y$, are duplicated, giving us an array of size $n + 2$.

While this can easily be solved with a hash set or frequency array in $O(n)$ time and $O(n)$ space, an interviewer at Google or Meta will immediately push for $O(1)$ auxiliary space without mutating the input array.

This pattern maps directly to the classic **"Two Single Numbers" / XOR partitioning** problem (LeetCode 260):
1. If we XOR all elements in `nums` with every integer from $0$ to $n - 1$:
   - Any number that appears once in the base set and once in `nums` appears an even number of times (2 times) and cancels out ($a \oplus a = 0$).
   - The two sneaky numbers $x$ and $y$ appear once in the base set and twice in `nums` (3 times total, which is odd).
   - Hence, the total XOR reduction results in $XOR = x \oplus y$.
2. Since $x \ne y$, $x \oplus y \ne 0$. There must be at least one bit where $x$ and $y$ differ.
3. We extract the lowest set bit using `diff_bit = XOR & (-XOR)`.
4. We can then partition all numbers (both in `nums` and in the range $[0, n - 1]$) into two groups: those with this bit set and those without.
5. XORing each group independently isolates $x$ and $y$.

---

### Step-by-Step Approach

1. **Calculate $n$**: $n = \text{len}(nums) - 2$.
2. **Compute total XOR**: Iterate through `nums` and the range $[0, n - 1]$, XORing all values together. The result is $x \oplus y$.
3. **Isolate differentiating bit**: Compute `diff_bit = xor_all & (-xor_all)`.
4. **Bucket XOR**:
   - Initialize two accumulators `x = 0` and `y = 0`.
   - Iterate through `nums`: if `num & diff_bit` is non-zero, XOR into `x`; otherwise XOR into `y`.
   - Iterate through $[0, n - 1]$: similarly split into `x` and `y`.
5. **Return Result**: Return `[x, y]`.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(n)$. We perform two linear passes over the array and the range $[0, n - 1]$. Bitwise operations take $\mathcal{O}(1)$ time.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space. Only a few integer variables (`xor_all`, `diff_bit`, `x`, `y`) are used.

---

### Common Pitfalls / Mistakes

1. **Using Hash Sets / Frequency Arrays**: While accepted, this uses $\mathcal{O}(n)$ extra memory. In an interview, failing to recognize the $\mathcal{O}(1)$ space solution signals lack of depth in bit manipulation.
2. **In-place Array Negation**: Negating `nums[abs(x)]` as a visited marker mutates the input array and fails if $0$ is an element (since $-0 = 0$).
3. **Math Overflow**: Using sum $\sum nums$ and sum of squares $\sum nums^2$ works mathematically ($x + y = S$, $x^2 + y^2 = P$), but in languages like C++ or Java, $\sum nums^2$ easily causes 32-bit or 64-bit integer overflows for large $n$. The XOR approach is completely immune to overflow.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input array is a read-only stream and cannot be re-read?
- **Answer**: The bit manipulation approach requires two passes over the data. If the stream is single-pass read-only, we can use the **sum and sum of squares** method:
  $$\Delta_1 = \sum_{k \in nums} k - \sum_{i=0}^{n-1} i = x + y$$
  $$\Delta_2 = \sum_{k \in nums} k^2 - \sum_{i=0}^{n-1} i^2 = x^2 + y^2$$
  From $\Delta_1$ and $\Delta_2$, we compute $xy = \frac{\Delta_1^2 - \Delta_2}{2}$ and $(x - y) = \sqrt{2\Delta_2 - \Delta_1^2}$, allowing us to solve for $x$ and $y$ in a single pass with $\mathcal{O}(1)$ space (using 64-bit or 128-bit integers to prevent overflow).

#### 2. What if $k$ numbers were duplicated instead of 2?
- **Answer**:
  - If $k$ is small and fixed (e.g., $k = 3$), power sums $\sum x^k$ can be used via Newton's identities or matrix methods.
  - If $k$ is arbitrary, a hash set or a Bloom filter (if approximate results / probabilistic membership is allowed) is necessary, requiring $\mathcal{O}(k)$ or $\mathcal{O}(n)$ space.

#### 3. How would you handle this in a distributed setting (e.g., MapReduce / Spark)?
- **Answer**:
  - The XOR operation is both **associative** and **commutative**.
  - In Map phase: Compute local XOR sums for partitions of `nums`.
  - In Reduce phase: Combine local XORs with the range XOR to determine $x \oplus y$ and `diff_bit`.
  - A second MapReduce job computes the XOR sums for the two partitioned buckets in parallel.
