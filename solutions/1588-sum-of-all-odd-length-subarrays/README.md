# 1588. Sum of All Odd Length Subarrays

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/sum-of-all-odd-length-subarrays/](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)  
**Topics:** Array, Math, Prefix Sum

---

## 📝 Problem Statement

Given an array of positive integers `arr`, return *the sum of all possible **odd-length subarrays** of *`arr`.

A **subarray** is a contiguous subsequence of the array.

 
Example 1:

```

**Input:** arr = [1,4,2,5,3]
**Output:** 58
**Explanation: **The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```

Example 2:

```

**Input:** arr = [1,2]
**Output:** 3
**Explanation: **There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
```

Example 3:

```

**Input:** arr = [10,11,12]
**Output:** 66

```

 
**Constraints:**

	- `1 

 
**Follow up:**

Could you solve this problem in O(n) time complexity?

---

## 💻 Implementation (python3)

```py
class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        """
        Calculates the sum of all odd-length subarrays in O(n) time and O(1) auxiliary space
        by counting the contribution of each element arr[i] across all valid subarrays.
        """
        n = len(arr)
        total_sum = 0
        
        for i in range(n):
            # Total subarrays containing arr[i]:
            # Number of valid starting positions: (i + 1) (from index 0 to i)
            # Number of valid ending positions: (n - i) (from index i to n - 1)
            total_subarrays = (i + 1) * (n - i)
            
            # Subarrays of odd length have start and end indices of the same parity.
            # Exactly ceil(total_subarrays / 2) = (total_subarrays + 1) // 2 of these
            # subarrays will have an odd length.
            odd_subarrays_count = (total_subarrays + 1) // 2
            
            # Contribution of arr[i] to the total sum
            total_sum += odd_subarrays_count * arr[i]
            
        return total_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A naive approach would be to generate every possible odd-length subarray and sum their elements. For an array of size $n$, generating all subarrays takes $O(n^2)$ time, and computing their sums without prefix sums takes $O(n^3)$ (or $O(n^2)$ with prefix sums).

To achieve the optimal $O(n)$ time complexity, we invert the problem: **Instead of asking "what elements are in each subarray?", we ask "in how many odd-length subarrays does each element $arr[i]$ appear?"**

For an element at index $i$ (0-indexed):
1. **Left choices (start of subarray):** Any index from $0$ to $i$, giving $i + 1$ possibilities.
2. **Right choices (end of subarray):** Any index from $i$ to $n - 1$, giving $n - i$ possibilities.
3. **Total subarrays containing $arr[i]$:** 
   $$\text{total} = (i + 1) \times (n - i)$$

A subarray has an odd length if and only if its length $\text{end} - \text{start} + 1$ is odd, which means $\text{start}$ and $\text{end}$ must have the same parity.
- When $\text{total}$ is even, exactly half ($\text{total} / 2$) of the subarrays are odd-length.
- When $\text{total}$ is odd, both $(i + 1)$ and $(n - i)$ must be odd. Since $i + 1$ is odd, $i$ is even. The range of end indices starts at $i$ (even) and contains an odd number of elements, which means there is one more even-indexed endpoint than odd-indexed endpoints. Thus, the matching parity combinations yield exactly one more odd-length subarray than even-length.

Hence, the number of odd-length subarrays containing index $i$ is always:
$$\text{odd\_count} = \left\lceil \frac{\text{total}}{2} \right\rceil = \left\lfloor \frac{\text{total} + 1}{2} \right\rfloor$$

Each element $arr[i]$ contributes $\text{odd\_count} \times arr[i]$ to the final result.

---

### Step-by-Step Approach

1. Initialize `total_sum = 0` and get $n = \text{len}(arr)$.
2. Iterate through each index $i$ from $0$ to $n - 1$:
   - Calculate total subarrays spanning index $i$: `total = (i + 1) * (n - i)`.
   - Calculate odd-length subarrays containing index $i$: `odd_count = (total + 1) // 2`.
   - Add `odd_count * arr[i]` to `total_sum`.
3. Return `total_sum`.

---

### Complexity Analysis

- **Time Complexity:** $O(n)$. We iterate through the array of length $n$ once, performing $O(1)$ arithmetic operations per element.
- **Space Complexity:** $O(1)$ auxiliary space. We only use a few integer variables for counting and accumulator.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Jumping straight to brute-force $O(n^3)$ or prefix sums $O(n^2)$:** While valid as a starting point, failing to realize the mathematical contribution of each element misses the interview follow-up requirement for $O(n)$.
2. **Incorrect Parity Math:** Splitting into manual cases for even/odd start and end indices often leads to off-by-one errors. Proving that `(total + 1) // 2` universally holds avoids messy conditionals.
3. **Integer Overflow in Other Languages:** In languages like C++ or Java, when $n \approx 10^5$, $(i + 1) \times (n - i)$ can exceed $2^{31} - 1$. Candidates should use 64-bit integers (`long long` / `long`) for intermediate multiplication. (Python handles arbitrary-precision integers automatically).

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the array is an infinite stream and we need the sum of odd-length subarrays for the first $k$ elements dynamically?
**Answer:** 
Notice the formula for the contribution of element $j$ ($0 \le j < k$):
$$\text{odd\_count}(j, k) \approx \frac{(j + 1)(k - j) + 1}{2}$$
This can be expanded as a polynomial in $k$:
$$(j + 1)k - j(j + 1) + 1$$
We can maintain running accumulators for $\sum (j + 1) \cdot arr[j]$ and $\sum j(j + 1) \cdot arr[j]$ with parity correction tracking. With a Fenwick tree (Binary Indexed Tree) or segmented prefix sums, each new streaming element can be processed and the global answer queried in $O(\log k)$ or amortized $O(1)$ time.

#### 2. What if we want the sum of subarrays whose length is a multiple of $k$ (or length $\equiv r \pmod k$)?
**Answer:**
We cannot simply divide by 2. Instead, we can use Fast Fourier Transform (FFT) or dynamic programming / prefix sums with modulo arithmetic:
- Maintain running prefix sums modulo $k$.
- Use counting arrays of size $k$ to track the frequency and weighted sum of prefix sums at each index modulo $k$.
