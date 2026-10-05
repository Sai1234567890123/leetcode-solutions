# 1442. Count Triplets That Can Form Two Arrays of Equal XOR

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)  
**Topics:** Array, Hash Table, Math, Bit Manipulation, Prefix Sum

---

## 📝 Problem Statement

Given an array of integers `arr`.

We want to select three indices `i`, `j` and `k` where `(0 

Let's define `a` and `b` as follows:

	- `a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]`

	- `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`

Note that **^** denotes the **bitwise-xor** operation.

Return *the number of triplets* (`i`, `j` and `k`) Where `a == b`.

 
Example 1:

```

**Input:** arr = [2,3,1,6,7]
**Output:** 4
**Explanation:** The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

```

Example 2:

```

**Input:** arr = [1,1,1,1,1]
**Output:** 10

```

 
**Constraints:**

	- `1 8`

---

## 💻 Implementation (python3)

```py
from collections import defaultdict

class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        """
        Calculates the number of triplets (i, j, k) with 0 <= i < j <= k < len(arr)
        such that XOR(arr[i...j-1]) == XOR(arr[j...k]).
        
        Key Insight:
            XOR(arr[i...j-1]) == XOR(arr[j...k]) 
            <=> XOR(arr[i...k]) == 0
            <=> prefix_xor[i] == prefix_xor[k + 1]
            
        For any such pair (i, k), any j strictly between i and k (i < j <= k)
        forms a valid triplet. There are (k - i) choices for j.
        """
        # count_map[val] stores the frequency of prefix XOR value `val`
        count_map = defaultdict(int)
        # total_idx_map[val] stores the sum of indices where prefix XOR value `val` occurred
        total_idx_map = defaultdict(int)
        
        # Base case: prefix XOR before any element (index 0) is 0
        count_map[0] = 1
        total_idx_map[0] = 0
        
        prefix = 0
        ans = 0
        
        # m represents (k + 1), ranging from 1 to len(arr)
        for m, num in enumerate(arr, start=1):
            prefix ^= num
            
            # If `prefix` has appeared before at indices i_1, i_2, ..., i_c:
            # Each gives (m - 1 - i) valid triplets for this (m - 1) as k.
            # Total for this m = sum((m - 1) - i) = c * (m - 1) - sum(i)
            if prefix in count_map:
                c = count_map[prefix]
                sum_i = total_idx_map[prefix]
                ans += c * (m - 1) - sum_i
            
            # Update prefix XOR tracking
            count_map[prefix] += 1
            total_idx_map[prefix] += m
            
        return ans
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for triplets $(i, j, k)$ such that $0 \le i < j \le k < n$ and:
$$a = arr[i] \oplus \dots \oplus arr[j-1]$$
$$b = arr[j] \oplus \dots \oplus arr[k]$$
with $a == b$.

A crucial property of the bitwise XOR operation is that $a == b \iff a \oplus b = 0$.
Notice that:
$$a \oplus b = (arr[i] \oplus \dots \oplus arr[j-1]) \oplus (arr[j] \oplus \dots \oplus arr[k]) = arr[i] \oplus \dots \oplus arr[k]$$

Thus, $a == b$ is equivalent to saying that the XOR sum of the contiguous subarray from $i$ to $k$ is $0$:
$$arr[i] \oplus \dots \oplus arr[k] = 0$$

If this condition holds for a pair $(i, k)$, where can index $j$ be?
The definition requires $i < j \le k$. For any choice of $j \in \{i + 1, i + 2, \dots, k\}$, the subarray split satisfies $a == b$.
The number of valid choices for $j$ is simply:
$$k - (i + 1) + 1 = k - i$$

Using prefix XORs where $P[x] = arr[0] \oplus \dots \oplus arr[x-1]$ and $P[0] = 0$:
$$arr[i] \oplus \dots \oplus arr[k] = P[k + 1] \oplus P[i] = 0 \iff P[k + 1] = P[i]$$

Letting $m = k + 1$, we need to find pairs $(i, m)$ with $i < m$ such that $P[i] = P[m]$.
For a fixed $m$, each previously seen index $i$ where $P[i] = P[m]$ contributes:
$$(m - 1) - i$$
triplets. If $P[m]$ has previously appeared $c$ times at indices $i_1, i_2, \dots, i_c$, its total contribution at step $m$ is:
$$\sum_{p=1}^{c} ((m - 1) - i_p) = c \cdot (m - 1) - \sum_{p=1}^{c} i_p$$

This allows computing the answer in a single pass using hash maps.

---

### Step-by-Step Approach

1. **Hash Maps Initialization**:
   - `count_map`: tracks how many times each prefix XOR has been encountered.
   - `total_idx_map`: tracks the sum of indices at which each prefix XOR occurred.
   - Initialize with $P[0] = 0$ at index $0$ (`count_map[0] = 1`, `total_idx_map[0] = 0`).

2. **Single Pass Evaluation**:
   - Iterate through `arr` with 1-based index $m \in [1, n]$.
   - Maintain the running prefix XOR: `prefix ^= arr[m - 1]`.
   - If `prefix` already exists in `count_map`, add $c \cdot (m - 1) - \text{sum\_i}$ to the total triplet count.
   - Increment `count_map[prefix]` by 1 and `total_idx_map[prefix]` by $m$.

3. **Return Result**:
   - Return the accumulated count `ans`.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the length of `arr`. We perform a single linear scan with $\mathcal{O}(1)$ average-time hash map lookups and updates.
- **Space Complexity**: $\mathcal{O}(N)$ in the worst case to store distinct prefix XOR values in the hash maps.

---

### Common Pitfalls & Mistakes Candidates Make

1. **Brute Force $\mathcal{O}(N^3)$ or $\mathcal{O}(N^2)$**:
   - Trying to enumerate all three pointers $i, j, k$ directly ($\mathcal{O}(N^3)$), or fixing $i$ and $k$ and using a nested loop ($\mathcal{O}(N^2)$). While $N \le 300$ passes quadratic time, top-tier companies expect the $\mathcal{O}(N)$ prefix-sum reduction.
2. **Missing the Base Case ($P[0] = 0$)**:
   - Failing to initialize $P[0] = 0$ at index $0$ causes subarrays starting at index $0$ (i.e., $i = 0$) whose total XOR is 0 to be omitted.
3. **Off-by-One in Triplet Contribution**:
   - Using $k - i + 1$ instead of $k - i$. Remember, $j$ is strictly greater than $i$, so $j \in [i+1, k]$, giving $(k - (i+1) + 1) = k - i$ possibilities.

---

### Real Interview Follow-Up Questions

#### 1. What if the input array is a continuous stream of integers?
- **Answer**: The single-pass $\mathcal{O}(1)$ state-update approach naturally supports streaming. At each new incoming element, update the cumulative XOR, query the hash tables to update the count, and store the new index and frequency.

#### 2. What if memory is heavily constrained (e.g., embedded systems)?
- **Answer**: If $N$ is small ($N \le 300$), an in-place $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ auxiliary space solution can be used by modifying `arr` to store prefix XORs in-place and checking all pairs $(i, k)$ using two pointers without any hash map.

#### 3. How to handle extremely large arrays that don't fit in a single machine's RAM? (Distributed / MapReduce)
- **Answer**: 
  - Subarray XORs can be computed across partitions: partition the array into chunks, compute local prefix XORs and the global XOR offset for each chunk.
  - Prefix XOR values and their original indices can be emitted as `(prefix_val, index)`.
  - In the reduce phase, group by `prefix_val`, and compute $\sum ((m - 1) - i)$ in one pass over the sorted indices.
