# 2433. Find The Original Array of Prefix Xor

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/find-the-original-array-of-prefix-xor/](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/)  
**Topics:** Array, Bit Manipulation

---

## 📝 Problem Statement

You are given an **integer** array `pref` of size `n`. Find and return *the array *`arr`* of size *`n`* that satisfies*:

	- `pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`.

Note that `^` denotes the **bitwise-xor** operation.

It can be proven that the answer is **unique**.

 
Example 1:

```

**Input:** pref = [5,2,0,3,1]
**Output:** [5,7,2,3,2]
**Explanation:** From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

```

Example 2:

```

**Input:** pref = [13]
**Output:** [13]
**Explanation:** We have pref[0] = arr[0] = 13.

```

 
**Constraints:**

	- `1 5`

	- `0 6`

---

## 💻 Implementation (python3)

```py
class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        # Using the property of XOR:
        # If pref[i] = pref[i - 1] ^ arr[i], then arr[i] = pref[i - 1] ^ pref[i].
        # We iterate backwards to modify the array in-place, achieving O(1) auxiliary space.
        for i in range(len(pref) - 1, 0, -1):
            pref[i] ^= pref[i - 1]
            
        return pref
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem defines the prefix XOR array as:
$$\text{pref}[i] = \text{arr}[0] \oplus \text{arr}[1] \oplus \dots \oplus \text{arr}[i]$$

Notice the recursive relationship between consecutive elements of `pref`:
$$\text{pref}[i] = \text{pref}[i - 1] \oplus \text{arr}[i] \quad \text{for } i \ge 1$$
$$\text{pref}[0] = \text{arr}[0]$$

Recall the fundamental algebraic properties of bitwise XOR ($\oplus$):
1. **Self-inverse:** $X \oplus X = 0$
2. **Identity:** $X \oplus 0 = X$
3. **Associativity and Commutativity**

Applying XOR with $\text{pref}[i - 1]$ to both sides of the equation:
$$\text{pref}[i - 1] \oplus \text{pref}[i] = \text{pref}[i - 1] \oplus (\text{pref}[i - 1] \oplus \text{arr}[i])$$
$$\text{pref}[i - 1] \oplus \text{pref}[i] = (\text{pref}[i - 1] \oplus \text{pref}[i - 1]) \oplus \text{arr}[i]$$
$$\text{pref}[i - 1] \oplus \text{pref}[i] = 0 \oplus \text{arr}[i] = \text{arr}[i]$$

Thus, we can directly compute:
$$\text{arr}[i] = \text{pref}[i - 1] \oplus \text{pref}[i] \quad (i \ge 1)$$
$$\text{arr}[0] = \text{pref}[0]$$

To achieve strictly $O(1)$ auxiliary space without allocating a new array, we can mutate `pref` in-place by iterating **backwards** from $n - 1$ down to $1$. Iterating backwards ensures we compute `pref[i] ^= pref[i - 1]` before `pref[i - 1]` is overwritten.

---

### Step-by-Step Approach

1. **Iterate Backwards:** Traverse from index $i = n - 1$ down to $1$.
2. **Compute In-Place:** At each step, update `pref[i] ^= pref[i - 1]`.
3. **Base Case:** `pref[0]` naturally remains unchanged, which matches $\text{arr}[0] = \text{pref}[0]$.
4. **Return:** Return the mutated `pref` array.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `pref`. We iterate through the array once and perform an $\mathcal{O}(1)$ bitwise operation at each index.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The modification is done entirely in-place without allocating additional memory buffers (or $\mathcal{O}(n)$ total space if including output space / if caller requires non-destructive modification).

---

### Common Pitfalls / Mistakes Candidates Make

1. **Overcomplicating the XOR Relationship:** Trying to maintain a running cumulative XOR variable or building prefix arrays from scratch, which is unnecessary and often leads to off-by-one errors.
2. **In-place Forward Iteration Bug:** Attempting in-place modification while iterating forward ($0 \to n-1$). Overwriting `pref[i - 1]` destroys the value needed to compute subsequent elements `pref[i]`.
3. **Premature Allocation:** Allocating an additional array when not strictly required. In production code, clarify whether modifying input in-place is permitted; demonstrating you know both in-place and non-destructive versions signals senior engineering maturity.

---

### Real Interview Follow-Up Questions

#### 1. What if modifying the input `pref` in-place is not allowed?
*Answer:* Allocate a new array `arr = [0] * n`, set `arr[0] = pref[0]`, and compute `arr[i] = pref[i - 1] ^ pref[i]` for $i \in [1, n-1]$. This requires $\mathcal{O}(n)$ additional space while maintaining $\mathcal{O}(n)$ time.

#### 2. How would you handle a streaming input where values of `pref` arrive one at a time?
*Answer:* We only need the immediately preceding prefix XOR to compute the next element. Maintain a single state variable `prev_pref` initialized to `0`. For each incoming element `curr_pref`, output `curr_pref ^ prev_pref`, then update `prev_pref = curr_pref`. This requires $\mathcal{O}(1)$ memory buffer.

#### 3. How can this be parallelized for massive arrays ($n \approx 10^9$) across multiple CPU cores or GPU?
*Answer:* Computing $\text{arr}[i] = \text{pref}[i - 1] \oplus \text{pref}[i]$ is an **embarrassingly parallel (map-style)** operation. Unlike prefix scan (which has data dependencies across the entire prefix), decoding prefix XOR only depends on adjacent pairs $(pref[i-1], pref[i])$. We can shard the array into contiguous chunks across cores with an overlap of 1 element at the boundary, allowing perfect linear scalability without synchronization barriers.
