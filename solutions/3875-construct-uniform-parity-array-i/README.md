# 3875. Construct Uniform Parity Array I

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/construct-uniform-parity-array-i/](https://leetcode.com/problems/construct-uniform-parity-array-i/)  
**Topics:** Array, Math

---

## 📝 Problem Statement

You are given an array `nums1` of `n` **distinct** integers.

You want to construct another array `nums2` of length `n` such that the elements in `nums2` are either **all odd or all even**.

For each index `i`, you must choose **exactly one** of the following (in any order):

	- `nums2[i] = nums1[i]`

	- `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`

Return `true` if it is possible to construct such an array, otherwise, return `false`.

 
Example 1:

**Input:** nums1 = [2,3]

**Output:** true

**Explanation:**

	- Choose `nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1`.

	- Choose `nums2[1] = nums1[1] = 3`.

	- `nums2 = [-1, 3]`, and both elements are odd. Thus, the answer is `true`​​​​​​​.

Example 2:

**Input:** nums1 = [4,6]

**Output:** true

**Explanation:**​​​​​​​

	- Choose `nums2[0] = nums1[0] = 4`.

	- Choose `nums2[1] = nums1[1] = 6`.

	- `nums2 = [4, 6]`, and all elements are even. Thus, the answer is `true`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # It is mathematically always possible to construct an array with uniform parity:
        # 1. If all elements in nums1 are even, we can keep nums2[i] = nums1[i] (all even).
        # 2. If all elements in nums1 are odd, we can keep nums2[i] = nums1[i] (all odd).
        # 3. If nums1 contains both even and odd elements:
        #    - There is at least one odd element at some index j.
        #    - For each odd element, set nums2[i] = nums1[i] (odd).
        #    - For each even element at index i, set nums2[i] = nums1[i] - nums1[j] (even - odd = odd).
        #    - Since index i is even and index j is odd, i != j is always satisfied.
        #    - Thus, all elements in nums2 can be made odd.
        # In all possible cases, a valid nums2 can be formed.
        return True
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks whether we can construct an array `nums2` of uniform parity (either all elements are odd or all elements are even) from `nums1` by either keeping `nums2[i] = nums1[i]` or setting `nums2[i] = nums1[i] - nums1[j]` for some $j \neq i$.

Let's analyze the parity arithmetic:
- $\text{even} - \text{odd} = \text{odd}$
- $\text{odd} - \text{odd} = \text{even}$
- $\text{odd} - \text{even} = \text{odd}$
- $\text{even} - \text{even} = \text{even}$

We can partition the input array `nums1` based on the count of odd numbers, denoted as $k$:

1. **Case 1: $k = 0$ (all elements are even)**
   - We can simply choose $nums2[i] = nums1[i]$ for all $i$. All elements in $nums2$ will be even.
   - Result: Always possible (`True`).

2. **Case 2: $k = n$ (all elements are odd)**
   - We can simply choose $nums2[i] = nums1[i]$ for all $i$. All elements in $nums2$ will be odd.
   - Result: Always possible (`True`).

3. **Case 3: $1 \le k < n$ (a mix of odd and even elements)**
   - Since $k \ge 1$, there exists at least one index $j^*$ such that $nums1[j^*]$ is odd.
   - For every element $nums1[i]$ that is already odd, we set $nums2[i] = nums1[i]$ (remains odd).
   - For every element $nums1[i]$ that is even, we set $nums2[i] = nums1[i] - nums1[j^*]$. Since $nums1[i]$ is even and $nums1[j^*]$ is odd, their indices are distinct ($i \neq j^*$), and $\text{even} - \text{odd} = \text{odd}$.
   - Thus, every element in $nums2$ becomes odd.
   - Result: Always possible (`True`).

Because every case results in a valid configuration, it is **always possible** to construct an array of uniform parity. Hence, the function unconditionally returns `True`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ — No computation or iteration over `nums1` is required.
- **Space Complexity:** $\mathcal{O}(1)$ — Requires no additional memory.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Overcomplicating the Implementation:** Iterating through the array, counting parities, and trying to explicitly build `nums2` or simulate the differences. Recognizing mathematical invariants is key to avoiding unnecessary code.
2. **Missing Parity Arithmetic:** Forgetting that an even number minus an odd number results in an odd number, which guarantees that as long as at least one odd number exists, all even numbers can be converted into odd numbers without interfering with existing odd numbers.
3. **Index Collision ($j \neq i$):** Candidates sometimes worry whether $j \neq i$ will be violated. Because an even number and an odd number can never share the same index, $j \neq i$ is inherently guaranteed.

---

### Real Interview Follow-Up Questions

#### 1. What if all values in `nums2` must be strictly positive?
*Answer:* If $nums2[i] > 0$ is required:
- Keeping $nums2[i] = nums1[i]$ requires $nums1[i] > 0$.
- Setting $nums2[i] = nums1[i] - nums1[j]$ requires $nums1[i] > nums1[j]$.
To achieve all positive odd numbers, the smallest odd number in `nums1` must be smaller than all even numbers, or we would have to check if there is an odd number $nums1[j] < nums1[i]$ for each even $nums1[i]$. The minimum odd element would need to be strictly less than all even elements. If this condition fails, we would check if making all numbers even is possible (requiring a minimum odd element smaller than all other odd elements).

#### 2. What if each $j$ can only be used at most once? (Matching / Bipartite Matching)
*Answer:* If each index $j$ can be subtracted at most once, this transitions into a maximum bipartite matching problem or a degree-constrained graph problem. We could model this using the Hopcroft-Karp algorithm or Ford-Fulkerson max-flow.

#### 3. What if `nums1` is a continuous data stream?
*Answer:* Since the answer is unconditionally `True` for any array, for any prefix or window of the stream of length $n \ge 1$, the answer remains `True`. If additional constraints (like positivity) were present, we would maintain running state variables (e.g., minimum odd element, minimum even element) using streaming summary statistics.
