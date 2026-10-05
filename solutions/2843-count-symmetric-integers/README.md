# 2843.   Count Symmetric Integers

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-symmetric-integers/](https://leetcode.com/problems/count-symmetric-integers/)  
**Topics:** Math, Enumeration

---

## 📝 Problem Statement

You are given two positive integers `low` and `high`.

An integer `x` consisting of `2 * n` digits is **symmetric** if the sum of the first `n` digits of `x` is equal to the sum of the last `n` digits of `x`. Numbers with an odd number of digits are never symmetric.

Return *the **number of symmetric** integers in the range* `[low, high]`.

 
Example 1:

```

**Input:** low = 1, high = 100
**Output:** 9
**Explanation:** There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

```

Example 2:

```

**Input:** low = 1200, high = 1230
**Output:** 4
**Explanation:** There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.

```

 
**Constraints:**

	- `1 4`

---

## 💻 Implementation (python3)

```py
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        Counts the number of symmetric integers in the range [low, high].
        An integer is symmetric if it has 2 * n digits and the sum of the
        first n digits equals the sum of the last n digits.
        """
        count = 0
        
        for num in range(low, high + 1):
            s = str(num)
            length = len(s)
            
            # Numbers with an odd number of digits cannot be symmetric
            if length % 2 != 0:
                continue
            
            half = length // 2
            # Compare the sum of the first half of digits with the second half
            left_sum = sum(int(digit) for digit in s[:half])
            right_sum = sum(int(digit) for digit in s[half:])
            
            if left_sum == right_sum:
                count += 1
                
        return count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem defines a symmetric integer as one having an even number of digits ($2n$) where the sum of the first $n$ digits equals the sum of the last $n$ digits.

Given the constraints ($1 \le \text{low} \le \text{high} \le 10^4$):
- Numbers have at most 5 digits (1 to 10,000).
- Only 2-digit ($10 - 99$) and 4-digit ($1000 - 9999$) numbers can possibly be symmetric because 1-digit, 3-digit, and 5-digit numbers have odd lengths.
- The total range size is at most $10,000$, making a direct linear scan over $[low, high]$ clean, optimal, and practically instantaneous (executing in under 5ms).

For each number:
1. Convert it to a string to easily inspect length and split it into two halves.
2. If the length is odd, skip.
3. Compute the sum of digits in the first half and the sum of digits in the second half.
4. If they match, increment our answer.

### Step-by-Step Approach

1. Initialize `count = 0`.
2. Iterate through every integer `num` from `low` to `high` inclusive.
3. Convert `num` to string `s` and check if `len(s) % 2 == 0`.
4. If even, calculate `half = len(s) // 2`.
5. Sum the numerical values of characters in `s[:half]` and `s[half:]`.
6. If the sums are equal, increment `count`.
7. Return `count`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}((high - low + 1) \times d)$, where $d$ is the maximum number of digits of any number in the range. Since $high \le 10^4$, $d \le 5$, which is bounded by a constant $\mathcal{O}(1)$. Thus, total time is at most $\sim 10^4 \times 5$ basic operations, which executes in $\mathcal{O}(N)$ where $N = high - low + 1 \le 10^4$.
- **Space Complexity:** $\mathcal{O}(d) = \mathcal{O}(1)$ auxiliary space to store the string representation of digits.

---

### Common Pitfalls / Mistakes

1. **Missing Odd-Digit Check:** Forgetting that numbers with an odd number of digits can never be symmetric (e.g., trying to divide 3 digits into two halves).
2. **Integer Arithmetic vs String Slicing:** While pure arithmetic (`% 10` and `/ 10`) avoids string allocations, converting strings for numbers up to $10^4$ is negligible in overhead and significantly less error-prone under interview pressure.
3. **Off-by-one Range Errors:** Forgetting that the problem asks for the inclusive range `[low, high]`, requiring `range(low, high + 1)`.

---

### Real Interview Follow-Up Questions

#### 1. What if $high \le 10^{18}$?
*Candidate Answer:* 
A linear scan would result in Time Limit Exceeded (TLE). We must reframe this as a **Digit DP (Digit Dynamic Programming)** problem.
- We define a function `count_symmetric_up_to(N)`. Then the answer is `count_symmetric_up_to(high) - count_symmetric_up_to(low - 1)`.
- For each fixed even length $2k \le 18$:
  - State: `dp(index, sum_diff, is_less, is_started)`.
  - At indices $0 \le i < k$, add digit to `sum_diff`.
  - At indices $k \le i < 2k$, subtract digit from `sum_diff`.
  - Target: `sum_diff == 0` at the end of the $2k$ digits.
- This reduces the time complexity from $\mathcal{O}(10^{18})$ to $\mathcal{O}(\log_{10}(\text{high}) \times \text{max\_sum}^2)$, easily running in under 50ms.

#### 2. How would you handle a streaming API where numbers arrive continuously?
*Candidate Answer:* 
We can precompute symmetric status or compute on the fly in $\mathcal{O}(d)$ per number. Since $d$ is tiny (e.g., $d \le 18$), each incoming query or check is essentially $\mathcal{O}(1)$. If prefix counts are queried repeatedly, a Fenwick tree (Binary Indexed Tree) or a running prefix sum array can answer range queries in $\mathcal{O}(\log M)$ or $\mathcal{O}(1)$ time.
