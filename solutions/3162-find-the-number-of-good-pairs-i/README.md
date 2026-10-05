# 3162. Find the Number of Good Pairs I

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-the-number-of-good-pairs-i/](https://leetcode.com/problems/find-the-number-of-good-pairs-i/)  
**Topics:** Array, Hash Table

---

## 📝 Problem Statement

You are given 2 integer arrays `nums1` and `nums2` of lengths `n` and `m` respectively. You are also given a **positive** integer `k`.

A pair `(i, j)` is called **good** if `nums1[i]` is divisible by `nums2[j] * k` (`0 

Return the total number of **good** pairs.

 
Example 1:

**Input:** nums1 = [1,3,4], nums2 = [1,3,4], k = 1

**Output:** 5

**Explanation:**
The 5 good pairs are `(0, 0)`, `(1, 0)`, `(1, 1)`, `(2, 0)`, and `(2, 2)`.

Example 2:

**Input:** nums1 = [1,2,4,12], nums2 = [2,4], k = 3

**Output:** 2

**Explanation:**

The 2 good pairs are `(3, 0)` and `(3, 1)`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from collections import Counter
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Finds the number of good pairs (i, j) such that nums1[i] is divisible by nums2[j] * k.
        Utilizes frequency mapping and sieve/multiple counting to achieve optimal performance,
        scalable to large constraints (LeetCode 3164).
        """
        # Step 1: Pre-filter nums1. Only elements divisible by k can form a valid pair.
        # Store frequency of nums1[i] // k.
        freq1 = Counter()
        for x in nums1:
            if x % k == 0:
                freq1[x // k] += 1
                
        # If no elements in nums1 are divisible by k, no good pairs can exist.
        if not freq1:
            return 0
            
        freq2 = Counter(nums2)
        max_val = max(freq1.keys())
        good_pairs = 0
        
        # Step 2: Iterate over unique values in nums2 and count matching multiples.
        for val, count in freq2.items():
            # Check all multiples of val up to the maximum element in freq1
            for multiple in range(val, max_val + 1, val):
                if multiple in freq1:
                    good_pairs += count * freq1[multiple]
                    
        return good_pairs
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A pair `(i, j)` is good if:
$$\text{nums1}[i] \pmod{\text{nums2}[j] \times k} == 0$$

This condition is mathematically equivalent to two statements:
1. $\text{nums1}[i]$ must be divisible by $k$.
2. $\frac{\text{nums1}[i]}{k}$ must be divisible by $\text{nums2}[j]$.

While the constraints for this problem are small ($n, m \le 50$), allowing a direct $O(n \times m)$ brute-force comparison, in technical interviews at top-tier companies (Google, Meta), interviewers frequently use this variant as a stepping stone to **LeetCode 3164: Find the Number of Good Pairs II** where $n, m \le 10^5$ and values reach $10^6$. Implementing the scalable, optimal approach right away highlights engineering foresight and algorithmic depth.

Instead of pairwise comparisons:
1. Divide every eligible element in `nums1` by $k$, keeping track of frequencies.
2. Group duplicates in `nums2` using a frequency map.
3. For each distinct value in `nums2`, step through its multiples up to $\max(\text{nums1} / k)$. Sum the product of frequencies.

### Step-by-Step Approach

1. **Filtering & Scaling**:
   - Check if $\text{nums1}[i] \pmod k == 0$. If so, increment the frequency of $\frac{\text{nums1}[i]}{k}$ in a hash map `freq1`.
   - If `freq1` is empty, immediately return `0`.
2. **Frequency Mapping**:
   - Count frequencies of elements in `nums2` using `freq2`.
3. **Harmonic Multiple Counting**:
   - Let $M = \max(\text{freq1.keys()})$.
   - For each unique $(val, count)$ in `freq2`:
     - Iterate through $val, 2 \times val, 3 \times val, \dots \le M$.
     - If the multiple exists in `freq1`, increment the answer by $\text{freq2}[val] \times \text{freq1}[multiple]$.

### Complexity Analysis

- **Time Complexity**:
  - Filtering `nums1`: $O(n)$
  - Counting `nums2`: $O(m)$
  - Harmonic multiple loop: $\sum_{v \in \text{nums2}} \frac{M}{v} \le \sum_{v=1}^{M} \frac{M}{v} = O(M \ln M)$, where $M = \max(\text{nums1}) / k$.
  - Total Time Complexity: $O(n + m + M \ln M)$. For the constraints given ($M \le 50$), this runs in virtually under a millisecond and scales gracefully to $M = 10^6$.
- **Space Complexity**:
  - $O(U_1 + U_2)$ where $U_1$ and $U_2$ are the numbers of unique elements in `nums1` and `nums2` respectively. This is $O(n + m)$ auxiliary space.

### Common Pitfalls / Mistakes

1. **ZeroDivisionError or Modulo by Zero**:
   - While $k \ge 1$ and elements are $\ge 1$, in generalized divisor problems candidates often forget to guard against $k = 0$ or divisor $= 0$.
2. **Checking $x \pmod{(y \times k)}$ Directly without $x \pmod k == 0$ Pre-check**:
   - When scaling up to large arrays, multiplying $y \times k$ first for all combinations causes quadratic time complexity.
3. **Double Counting Multiples**:
   - If iterating over non-unique elements of `nums2`, identical values re-traverse the same multiples. Using `Counter` on `nums2` ensures each unique factor is processed once.

### Real Interview Follow-Up Questions & Answers

#### 1. What if $n, m \le 10^5$ and $\text{nums1}[i], \text{nums2}[j] \le 10^6$ (Find the Number of Good Pairs II)?
- **Answer**: The solution provided above is already $O(n + m + M \ln M)$. For $M = 10^6$, $M \ln M \approx 1.4 \times 10^7$ operations, which easily passes within the 2-second time limit. Alternatively, if $M \gg n$, one can compute all divisors of each $x \in \text{nums1}$ in $O(n \sqrt{x})$ time and look up divisors in `freq2`.

#### 2. How would you handle a streaming scenario where `nums1` is fixed, but `nums2` arrives continuously in a stream?
- **Answer**: Pre-calculate the divisors for all elements in `nums1 // k`. Maintain a global hash map `divisor_count` mapping each divisor to how many elements in `nums1 // k` it divides. When a new element $y$ arrives from `nums2`, query `divisor_count[y]` in $O(1)$ time.

#### 3. What if memory is severely constrained ($O(1)$ auxiliary space required)?
- **Answer**: If auxiliary memory cannot be used (e.g., embedded devices), fall back to two nested loops: iterate over all $i \in [0, n-1]$ and $j \in [0, m-1]$, evaluating `nums1[i] % (nums2[j] * k) == 0`. This uses $O(1)$ space at the expense of $O(n \times m)$ time.
