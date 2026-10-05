# 2997. Minimum Number of Operations to Make Array XOR Equal to K

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/)  
**Topics:** Array, Bit Manipulation

---

## 📝 Problem Statement

You are given a **0-indexed** integer array `nums` and a positive integer `k`.

You can apply the following operation on the array **any** number of times:

	- Choose **any** element of the array and **flip** a bit in its **binary** representation. Flipping a bit means changing a `0` to `1` or vice versa.

Return *the **minimum** number of operations required to make the bitwise *`XOR`* of **all** elements of the final array equal to *`k`.

**Note** that you can flip leading zero bits in the binary representation of elements. For example, for the number `(101)2` you can flip the fourth bit and obtain `(1101)2`.

 
Example 1:

```

**Input:** nums = [2,1,3,4], k = 1
**Output:** 2
**Explanation:** We can do the following operations:
- Choose element 2 which is 3 == (011)2, we flip the first bit and we obtain (010)2 == 2. nums becomes [2,1,2,4].
- Choose element 0 which is 2 == (010)2, we flip the third bit and we obtain (110)2 = 6. nums becomes [6,1,2,4].
The XOR of elements of the final array is (6 XOR 1 XOR 2 XOR 4) == 1 == k.
It can be shown that we cannot make the XOR equal to k in less than 2 operations.

```

Example 2:

```

**Input:** nums = [2,0,2,0], k = 0
**Output:** 0
**Explanation:** The XOR of elements of the array is (2 XOR 0 XOR 2 XOR 0) == 0 == k. So no operation is needed.

```

 
**Constraints:**

	- `1 5`

	- `0 6`

	- `0 6`

---

## 💻 Implementation (python3)

```py
from typing import List
from functools import reduce
from operator import xor

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Calculates the minimum number of bit flips required across the array
        to make the bitwise XOR of all elements equal to k.
        """
        # Compute the XOR sum of all elements in the array
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # The differing bits between total_xor and k indicate the minimum flips needed.
        # Flipping a bit in any number flips that bit in the total XOR.
        # Thus, each differing bit requires exactly one flip.
        diff = total_xor ^ k
        
        # Return the number of set bits (popcount / Hamming weight)
        return diff.bit_count()
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

Let $X$ denote the bitwise XOR sum of all numbers in `nums`:
$$X = \text{nums}[0] \oplus \text{nums}[1] \oplus \dots \oplus \text{nums}[n-1]$$

Each operation allows us to flip a single bit in any chosen element. Bitwise XOR has the associative and commutative properties, and flipping bit $b$ in any element will flip bit $b$ of the cumulative XOR sum $X$, leaving all other bit positions unchanged.

Because each flip alters exactly one bit position in the cumulative XOR sum, we can consider each bit position independently:
1. If the $b$-th bit of $X$ matches the $b$-th bit of $k$, zero operations are needed for this bit position.
2. If the $b$-th bit of $X$ differs from the $b$-th bit of $k$, exactly one flip of that bit (in any element) is required to reconcile them.

Thus, each differing bit between $X$ and $k$ requires exactly one operation, and no single operation can resolve multiple bit positions. The minimum number of operations is therefore the Hamming distance between $X$ and $k$, which is simply the number of set bits (population count) in:
$$\text{diff} = X \oplus k$$

---

### Step-by-Step Approach

1. **Calculate the Cumulative XOR**:
   - Iterate through `nums` and compute `total_xor = nums[0] ^ nums[1] ^ ... ^ nums[n-1]`.
2. **Find the Bitwise Difference**:
   - Compute `diff = total_xor ^ k`. A bit is set in `diff` if and only if `total_xor` and `k` differ at that position.
3. **Count Mismatched Bits**:
   - Return the count of set bits in `diff` using Python's built-in `diff.bit_count()`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
  We iterate through the array of length $N$ exactly once to compute the cumulative XOR. The subsequent bitwise XOR and `.bit_count()` run in $\mathcal{O}(1)$ time since numbers are bounded by $\approx 10^6$ (at most 20 bits).
- **Space Complexity:** $\mathcal{O}(1)$
  Only a single integer accumulator is maintained, using constant auxiliary space.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Simulating Bit Flips on Elements**: Trying to greedily choose *which* specific element in `nums` to flip. The problem asks for the minimum count of operations across the entire array, not the specific indices modified. Any element can absorb any bit flip.
2. **Dynamic Programming Overkill**: Attempting bitmask DP or knapsack-style DP. Recognizing the linear independence of bit positions in XOR simplifies this to a single reduction.
3. **Inefficient Bit Counting**: Writing a manual while loop with bit shifts (`while diff > 0: count += diff & 1; diff >>= 1`) without mentioning hardware-level bit counting (`POPCNT` / `bit_count()`).

---

### Real Interview Follow-Up Questions

#### 1. What if the input array is an infinite stream of numbers and $k$ is fixed?
*Answer:* Maintain a single running integer `stream_xor`. For each incoming element $x$, update `stream_xor ^= x`. At any query point, the answer is `(stream_xor ^ k).bit_count()` in $\mathcal{O}(1)$ time and $\mathcal{O}(1)$ space.

#### 2. What if we have multiple queries $(k_i)$ on a static array `nums`?
*Answer:* Precompute the cumulative XOR sum $X$ once in $\mathcal{O}(N)$ time. For each query $k_i$, answer in $\mathcal{O}(1)$ by evaluating `(X ^ k_i).bit_count()`.

#### 3. What if there is a constraint that each element can only have at most one bit flipped?
*Answer:* If the number of differing bits $d = (X \oplus k)\text{.bit\_count()}$ exceeds $N$ (the length of `nums`), it is impossible (return $-1$). Otherwise, because $d \le N$, we can flip one distinct differing bit on $d$ distinct elements, yielding the same answer $d$.

#### 4. How would you handle this in a distributed setting (e.g., MapReduce / Spark)?
*Answer:* XOR is associative and commutative. In the Map/Partition stage, compute the XOR of each shard locally. In the Reduce stage, XOR the partition results together into a single global XOR value, then compute `(global_xor ^ k).bit_count()`.
