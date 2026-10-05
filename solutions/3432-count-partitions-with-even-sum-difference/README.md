# 3432. Count Partitions with Even Sum Difference

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-partitions-with-even-sum-difference/](https://leetcode.com/problems/count-partitions-with-even-sum-difference/)  
**Topics:** Array, Math, Prefix Sum

---

## 📝 Problem Statement

You are given an integer array `nums` of length `n`.

A **partition** is defined as an index `i` where `0 

	- Left subarray contains indices `[0, i]`.

	- Right subarray contains indices `[i + 1, n - 1]`.

Return the number of **partitions** where the **difference** between the **sum** of the left and right subarrays is **even**.

 
Example 1:

**Input:** nums = [10,10,3,7,6]

**Output:** 4

**Explanation:**

The 4 partitions are:

	- `[10]`, `[10, 3, 7, 6]` with a sum difference of `10 - 26 = -16`, which is even.

	- `[10, 10]`, `[3, 7, 6]` with a sum difference of `20 - 16 = 4`, which is even.

	- `[10, 10, 3]`, `[7, 6]` with a sum difference of `23 - 13 = 10`, which is even.

	- `[10, 10, 3, 7]`, `[6]` with a sum difference of `30 - 6 = 24`, which is even.

Example 2:

**Input:** nums = [1,2,2]

**Output:** 0

**Explanation:**

No partition results in an even sum difference.

Example 3:

**Input:** nums = [2,4,6,8]

**Output:** 3

**Explanation:**

All partitions result in an even sum difference.

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        """
        Calculates the number of valid partitions where (left_sum - right_sum) is even.
        
        Mathematical Insight:
        Let S be the total sum of the array.
        For any partition index i, let L = sum(nums[0..i]) and R = sum(nums[i+1..n-1]).
        Since L + R = S, we have R = S - L.
        The difference is: L - R = L - (S - L) = 2 * L - S.
        
        Since 2 * L is always even, the parity of (2 * L - S) depends entirely on S:
        (2 * L - S) % 2 == S % 2.
        
        Therefore:
        - If the total sum S is even, EVERY partition produces an even difference (n - 1 partitions).
        - If the total sum S is odd, NO partition can produce an even difference (0 partitions).
        """
        total_sum = sum(nums)
        return (len(nums) - 1) if total_sum % 2 == 0 else 0
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the count of partitions $i \in [0, n - 2]$ such that the difference between the sum of the left subarray `nums[0..i]` and the right subarray `nums[i+1..n-1]` is an even number.

A brute-force or prefix-sum approach would compute the sum of each subarray for all $n - 1$ split points and check if $(L - R) \pmod 2 == 0$. However, we can analyze the mathematical structure of the problem:

1. Let $S = \sum_{j=0}^{n-1} nums[j]$ be the total sum of the array.
2. For any partition $i$, let $L$ be the sum of the left subarray, and $R$ be the sum of the right subarray.
3. Because every element belongs to either the left or the right subarray, $L + R = S \implies R = S - L$.
4. The difference between the left and right subarrays is:
   $$\text{diff} = L - R = L - (S - L) = 2L - S$$
5. Looking at the parity of this expression modulo 2:
   $$\text{diff} \pmod 2 = (2L - S) \pmod 2 \equiv -S \equiv S \pmod 2$$

Since $2L$ is guaranteed to be an even number for any integer $L$, $(2L - S)$ has the exact same parity as $S$. The specific partition index $i$ and the individual values within $L$ do not matter at all:
- If the total sum $S$ is **even**, every single valid partition will have an even difference. Since there are $n - 1$ possible split positions ($0 \le i \le n - 2$), the answer is $n - 1$.
- If the total sum $S$ is **odd**, no partition can ever have an even difference. The answer is $0$.

### Step-by-Step Approach

1. Calculate the total sum of the array, $S = \text{sum}(nums)$.
2. Check if $S \pmod 2 == 0$:
   - If `True`, return `len(nums) - 1`.
   - If `False`, return `0`.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. We traverse the array once to compute the total sum.
- **Space Complexity:** $O(1)$ auxiliary space. Only a single variable is used to accumulate the sum.

### Common Pitfalls / Mistakes

1. **Unnecessary Prefix Sum Arrays:** Allocating prefix/suffix arrays or iterating through each index to recompute $(L - R) \% 2$. While $O(n)$ space still passes for small constraints ($n \le 100$), recognizing the invariant $2L - S \equiv S \pmod 2$ demonstrates strong mathematical reasoning in an interview.
2. **Off-by-One on Partition Count:** Forgetting that a partition splits into two non-empty subarrays, meaning the number of partitions is $n - 1$, not $n$.
3. **Negative Numbers Modulo:** In Python, the `%` operator always returns a non-negative result, but in languages like C++ or Java, `(-odd) % 2` yields `-1`. While here values are strictly positive ($nums[i] \ge 1$), always be mindful of parity checks in other languages (e.g., using `(diff % 2 == 0)` or `(diff & 1) == 0`).

### Real Interview Follow-Up Questions

#### 1. What if the array is an infinite stream of numbers and we need to answer this dynamically?
**Answer:** Maintain a running count of total elements $n$ and running sum $S$ modulo 2. For each new element $x$:
- $S \leftarrow (S + x) \pmod 2$
- $n \leftarrow n + 1$
- If $n \ge 2$, return $n - 1$ if $S == 0$ else $0$. This operates in $O(1)$ time and $O(1)$ space per incoming token.

#### 2. What if the condition is changed to "difference is divisible by $k$"?
**Answer:** The equation becomes $(2L - S) \equiv 0 \pmod k \implies 2L \equiv S \pmod k$.
- Parity was special because $2L \equiv 0 \pmod 2$ identically.
- For a general $k$, we must find the number of prefix sums $L$ that satisfy $2L \equiv S \pmod k$.
- This can be solved by maintaining a prefix sum, computing $2L \pmod k$ at each step, and counting matches in $O(n)$ time using a hash map or single pass.
