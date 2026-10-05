# 1829. Maximum XOR for Each Query

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/maximum-xor-for-each-query/](https://leetcode.com/problems/maximum-xor-for-each-query/)  
**Topics:** Array, Bit Manipulation, Prefix Sum

---

## 📝 Problem Statement

You are given a **sorted** array `nums` of `n` non-negative integers and an integer `maximumBit`. You want to perform the following query `n` **times**:

	- Find a non-negative integer `k maximumBit` such that `nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k` is **maximized**. `k` is the answer to the `ith` query.

	- Remove the **last **element from the current array `nums`.

Return *an array* `answer`*, where *`answer[i]`* is the answer to the *`ith`* query*.

 
Example 1:

```

**Input:** nums = [0,1,1,3], maximumBit = 2
**Output:** [0,3,2,3]
**Explanation**: The queries are answered as follows:
1st query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
2nd query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
3rd query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
4th query: nums = [0], k = 3 since 0 XOR 3 = 3.

```

Example 2:

```

**Input:** nums = [2,3,4,7], maximumBit = 3
**Output:** [5,2,6,5]
**Explanation**: The queries are answered as follows:
1st query: nums = [2,3,4,7], k = 5 since 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7.
2nd query: nums = [2,3,4], k = 2 since 2 XOR 3 XOR 4 XOR 2 = 7.
3rd query: nums = [2,3], k = 6 since 2 XOR 3 XOR 6 = 7.
4th query: nums = [2], k = 5 since 2 XOR 5 = 7.

```

Example 3:

```

**Input:** nums = [0,1,2,2,5,7], maximumBit = 3
**Output:** [4,3,6,4,6,7]

```

 
**Constraints:**

	- `nums.length == n`

	- `1 5`

	- `1 maximumBit`

	- `nums`​​​ is sorted in **ascending** order.

---

## 💻 Implementation (python3)

```py
class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        # The maximum possible value for a number with `maximumBit` bits is 2^maximumBit - 1.
        # This corresponds to having all of the lowest `maximumBit` bits set to 1.
        max_val = (1 << maximumBit) - 1
        
        # Calculate the cumulative XOR of all elements in nums.
        current_xor = 0
        for num in nums:
            current_xor ^= num
            
        n = len(nums)
        ans = [0] * n
        
        # Process queries from first to last (removing the last element at each step).
        for i in range(n):
            # To maximize (current_xor XOR k), we want (current_xor XOR k) == max_val
            # for the lowest `maximumBit` bits.
            # Using XOR properties: k = current_xor XOR max_val.
            # Note: We take (current_xor & max_val) in case nums contains bits >= maximumBit.
            ans[i] = (current_xor & max_val) ^ max_val
            
            # Remove the last element for the next query by XORing it out.
            current_xor ^= nums[n - 1 - i]
            
        return ans
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

1. **Understanding the XOR Maximization:**
   We are tasked with finding a non-negative integer $k < 2^{\text{maximumBit}}$ that maximizes:
   $$\text{val} = (\text{current\_xor} \oplus k)$$
   Since $k$ has at most $\text{maximumBit}$ bits, we can only manipulate the lowest $\text{maximumBit}$ bits of $\text{current\_xor}$. 
   To maximize the result, every bit from index $0$ to $\text{maximumBit} - 1$ in the result should ideally be set to `1`. 
   The number with all these bits set to `1` is $\text{max\_val} = 2^{\text{maximumBit}} - 1$.

2. **Solving for $k$:**
   If we want the lowest $\text{maximumBit}$ bits of $(\text{current\_xor} \oplus k)$ to equal $\text{max\_val}$, we can use the property of the XOR operation:
   $$\text{current\_xor} \oplus k = \text{max\_val} \implies k = \text{current\_xor} \oplus \text{max\_val}$$
   Because $k$ is strictly bounded by $k < 2^{\text{maximumBit}}$, we isolate the lower bits of $\text{current\_xor}$ via $(\text{current\_xor} \ \& \ \text{max\_val}) \oplus \text{max\_val}$.

3. **Optimizing Queries:**
   In each successive query, the last element is removed from the array.
   Rather than recomputing the prefix XOR in $O(N)$ for each query (which would yield $O(N^2)$ time), we can leverage the self-inverting property of XOR ($A \oplus B \oplus B = A$):
   - First, compute the cumulative XOR sum of the entire array.
   - For each query $i$ from $0$ to $N - 1$, calculate $k$, record it in the result, and then XOR out the current last element: `current_xor ^= nums[n - 1 - i]`.

---

### Step-by-Step Approach

1. **Compute Mask:** Set `max_val = (1 << maximumBit) - 1`.
2. **Compute Total XOR:** Iterate through `nums` and compute the XOR sum of all elements.
3. **Generate Answers:**
   - Pre-allocate a result list `ans` of size $n$.
   - For each query $i \in [0, n - 1]$:
     - Set `ans[i] = (current_xor & max_val) ^ max_val`.
     - Update `current_xor` by removing the element at the current tail: `current_xor ^= nums[n - 1 - i]`.
4. Return `ans`.

---

### Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. Computing the initial total XOR takes $O(N)$, and answering all $N$ queries takes $O(1)$ per query ($O(N)$ total).
- **Space Complexity:** $O(1)$ auxiliary space (excluding the $O(N)$ space required for the output array `ans`).

---

### Common Pitfalls / Mistakes

1. **Recomputing XOR per Query:** Recalculating the XOR sum from scratch for each query leads to a TLE ($O(N^2)$ time).
2. **Ignoring Bit Boundary Constraints:** Missing the constraint $k < 2^{\text{maximumBit}}$ and computing `current_xor ^ max_val` directly without bitmasking when elements might have bits $\ge \text{maximumBit}$.
3. **Off-by-one indexing on element removal:** Forgetting that in Python, removing from the back corresponds to `nums[n - 1 - i]`.

---

### Real Interview Follow-Up Questions

#### 1. What if the array is an infinite stream and we query the current prefix dynamically?
- **Answer:** Maintain a running XOR variable `stream_xor`. Each time a new integer `x` arrives, update `stream_xor ^= x`. The answer at any point in the stream is always `(stream_xor & max_val) ^ max_val` in $O(1)$ time and $O(1)$ extra space.

#### 2. What if removals are arbitrary (not just from the end) or updates/queries interleave?
- **Answer:** If elements can be removed or modified arbitrarily by index, we can maintain the XOR sum using a **Fenwick Tree (Binary Indexed Tree)** or **Segment Tree** supporting point updates and range XOR queries in $O(\log N)$ time per query/update.

#### 3. What if $N$ is extremely large (e.g., $10^9$) and stored in distributed storage (e.g., BigQuery / MapReduce)?
- **Answer:** Prefix XOR is an associative, invertible group operation. We can compute prefix XORs using a distributed **parallel prefix sum (Scan)** pattern across chunks. Each worker computes chunk-level XOR sums, a global scan determines offsets, and each worker answers queries locally in parallel.
