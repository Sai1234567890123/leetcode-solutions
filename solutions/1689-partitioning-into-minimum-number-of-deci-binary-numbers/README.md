# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/)  
**Topics:** String, Greedy

---

## 📝 Problem Statement

A decimal number is called **deci-binary** if each of its digits is either `0` or `1` without any leading zeros. For example, `101` and `1100` are **deci-binary**, while `112` and `3001` are not.

Given a string `n` that represents a positive decimal integer, return *the **minimum** number of positive **deci-binary** numbers needed so that they sum up to *`n`*.*

 
Example 1:

```

**Input:** n = "32"
**Output:** 3
**Explanation:** 10 + 11 + 11 = 32

```

Example 2:

```

**Input:** n = "82734"
**Output:** 8

```

Example 3:

```

**Input:** n = "27346209830709182346"
**Output:** 9

```

 
**Constraints:**

	- `1 5`

	- `n` consists of only digits.

	- `n` does not contain any leading zeros and represents a positive integer.

---

## 💻 Implementation (python3)

```py
class Solution:
    def minPartitions(self, n: str) -> int:
        # The problem asks for the minimum number of positive deci-binary numbers
        # that sum up to `n`. A deci-binary number is one where each digit is either 0 or 1.

        # Intuition:
        # Consider a specific digit position in `n`. For example, if `n` has a '3' in its
        # tens place, it means the sum of the tens digits of the deci-binary numbers must
        # result in '3' (possibly with carries from the units place, but we'll see why
        # carries don't complicate this particular problem).
        # Since each deci-binary number can only have a '0' or '1' at any given digit position,
        # to achieve a '3' in the tens place, we must have at least three deci-binary numbers
        # that each contribute a '1' to their tens place. This implies that the total number
        # of deci-binary numbers needed must be at least the value of the largest digit in `n`.

        # Example: n = "32"
        # The largest digit is '3'. We claim the answer is 3.
        # We can construct three deci-binary numbers:
        # 1. For the tens place ('3'): We need three '1's.
        # 2. For the units place ('2'): We need two '1's.
        #
        # Let's form the numbers:
        # d1: has '1' in tens (since 1 <= 3), '1' in units (since 1 <= 2) -> "11"
        # d2: has '1' in tens (since 2 <= 3), '1' in units (since 2 <= 2) -> "11"
        # d3: has '1' in tens (since 3 <= 3), '0' in units (since 3 > 2) -> "10"
        #
        # Summing these: 11 + 11 + 10 = 32. This works, and we used 3 numbers.

        # Proof of optimality:
        # Let `D` be the maximum digit in `n`.
        # To form the digit `D` at its specific position `p`, we need to sum `D` ones
        # at that position. Since each deci-binary number can contribute at most '1'
        # to any digit position, we must use at least `D` deci-binary numbers.
        # Thus, the minimum count is `>= D`.

        # Proof of sufficiency:
        # We can always construct `D` deci-binary numbers. For each digit position `i` in `n`,
        # let `n_i` be the digit at that position. We construct `D` deci-binary numbers,
        # `d_1, d_2, ..., d_D`. For each `d_j` (where `j` ranges from 1 to `D`),
        # set its `i`-th digit to '1' if `j <= n_i`, and '0' otherwise.
        # When these `D` numbers are summed, at each position `i`, exactly `n_i` of them
        # will have a '1', and the rest will have '0'. The sum at position `i` will be `n_i`.
        # Since `D` (the maximum digit) is at most 9, no carries will be generated
        # between digit positions. The total sum will be exactly `n`.
        # Each `d_j` will be a valid deci-binary number. Since `n` is positive, `D >= 1`,
        # and `d_1` will always be a positive deci-binary number.

        # Therefore, the minimum number of positive deci-binary numbers required is
        # simply the largest digit present in the input string `n`.

        max_digit = 0
        # Iterate through each character (digit) in the input string `n`.
        for char_digit in n:
            # Convert the character digit to an integer.
            digit = int(char_digit)
            # Update max_digit if the current digit is greater.
            if digit > max_digit:
                max_digit = digit
                # Optimization: If we find '9', it's the largest possible digit,
                # so we can immediately return 9 as it must be the maximum.
                if max_digit == 9:
                    return 9
        
        # After checking all digits, max_digit will hold the largest digit found.
        return max_digit
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
