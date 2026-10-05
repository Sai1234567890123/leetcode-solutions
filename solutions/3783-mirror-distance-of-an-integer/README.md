# 3783. Mirror Distance of an Integer

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/mirror-distance-of-an-integer/](https://leetcode.com/problems/mirror-distance-of-an-integer/)  
**Topics:** Math

---

## 📝 Problem Statement

You are given an integer `n`.

Define its **mirror distance** as: `abs(n - reverse(n))`​​​​​​​ where `reverse(n)` is the integer formed by reversing the digits of `n`.

Return an integer denoting the mirror distance of `n`​​​​​​​.

`abs(x)` denotes the absolute value of `x`.

 
Example 1:

**Input:** n = 25

**Output:** 27

**Explanation:**

	- `reverse(25) = 52`.

	- Thus, the answer is `abs(25 - 52) = 27`.

Example 2:

**Input:** n = 10

**Output:** 9

**Explanation:**

	- `reverse(10) = 01` which is 1.

	- Thus, the answer is `abs(10 - 1) = 9`.

Example 3:

**Input:** n = 7

**Output:** 0

**Explanation:**

	- `reverse(7) = 7`.

	- Thus, the answer is `abs(7 - 7) = 0`.

 
**Constraints:**

	- `1 9`

---

## 💻 Implementation (python3)

```py
class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Store the original value of n, as n will be modified during the reversal process.
        original_n = n
        
        reversed_n = 0
        # Iterate through the digits of n to reverse it.
        # This loop continues as long as there are digits left in n.
        while n > 0:
            # Get the last digit of n using the modulo operator.
            digit = n % 10
            
            # Build the reversed number:
            # 1. Multiply reversed_n by 10 to shift its existing digits one position to the left.
            # 2. Add the current 'digit' to the rightmost position.
            reversed_n = reversed_n * 10 + digit
            
            # Remove the last digit from n by performing integer division.
            n //= 10
            
        # The mirror distance is defined as the absolute difference between the original number
        # and its reversed version.
        return abs(original_n - reversed_n)
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
