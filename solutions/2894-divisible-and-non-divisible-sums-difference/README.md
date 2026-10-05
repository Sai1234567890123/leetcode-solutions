# 2894. Divisible and Non-divisible Sums Difference

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/)  
**Topics:** Math

---

## 📝 Problem Statement

You are given positive integers `n` and `m`.

Define two integers as follows:

	- `num1`: The sum of all integers in the range `[1, n]` (both **inclusive**) that are **not divisible** by `m`.

	- `num2`: The sum of all integers in the range `[1, n]` (both **inclusive**) that are **divisible** by `m`.

Return *the integer* `num1 - num2`.

 
Example 1:

```

**Input:** n = 10, m = 3
**Output:** 19
**Explanation:** In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.

```

Example 2:

```

**Input:** n = 5, m = 6
**Output:** 15
**Explanation:** In the given example:
- Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], num1 is the sum of those integers = 15.
- Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.
We return 15 - 0 = 15 as the answer.

```

Example 3:

```

**Input:** n = 5, m = 1
**Output:** -15
**Explanation:** In the given example:
- Integers in the range [1, 5] that are not divisible by 1 are [], num1 is the sum of those integers = 0.
- Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], num2 is the sum of those integers = 15.
We return 0 - 15 = -15 as the answer.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Calculate the sum of all integers from 1 to n.
        # This is the sum of an arithmetic series: n * (n + 1) / 2.
        # Using integer division (//) as all sums will be integers.
        total_sum_up_to_n = n * (n + 1) // 2

        # Calculate num2: the sum of all integers in the range [1, n] that are divisible by m.
        # These numbers are m, 2*m, 3*m, ..., k*m, where k*m <= n.
        # The largest multiple of m less than or equal to n is found by k = n // m.
        # The sum of these multiples is m * (1 + 2 + ... + k).
        # The sum 1 + 2 + ... + k is another arithmetic series: k * (k + 1) / 2.
        
        # k represents how many multiples of m are there up to n.
        k = n // m 
        
        # num2 is the sum of these multiples.
        sum_divisible_by_m = m * (k * (k + 1) // 2)

        # We need to find num1 - num2.
        # We know that:
        # (sum of all integers from 1 to n) = num1 + num2
        # So, total_sum_up_to_n = num1 + num2
        # This implies num1 = total_sum_up_to_n - num2.
        
        # Substituting num1 into the expression we need to return:
        # num1 - num2 = (total_sum_up_to_n - num2) - num2
        #             = total_sum_up_to_n - 2 * num2
        
        return total_sum_up_to_n - 2 * sum_divisible_by_m
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
