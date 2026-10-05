# 2396. Strictly Palindromic Number

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/strictly-palindromic-number/](https://leetcode.com/problems/strictly-palindromic-number/)  
**Topics:** Math, Two Pointers, Brainteaser

---

## 📝 Problem Statement

An integer `n` is **strictly palindromic** if, for **every** base `b` between `2` and `n - 2` (**inclusive**), the string representation of the integer `n` in base `b` is **palindromic**.

Given an integer `n`, return `true` *if *`n`* is **strictly palindromic** and *`false`* otherwise*.

A string is **palindromic** if it reads the same forward and backward.

 
Example 1:

```

**Input:** n = 9
**Output:** false
**Explanation:** In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.

```

Example 2:

```

**Input:** n = 4
**Output:** false
**Explanation:** We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.

```

 
**Constraints:**

	- `4 5`

---

## 💻 Implementation (python3)

```py
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # The problem asks if an integer 'n' is strictly palindromic.
        # An integer 'n' is strictly palindromic if its string representation
        # is palindromic for *every* base 'b' between 2 and n-2 (inclusive).

        # Let's analyze the condition "for every base b between 2 and n-2".
        # This is a very strong condition. If we can find even *one* base 'b'
        # in this range for which 'n' is NOT palindromic, then 'n' is not
        # strictly palindromic, and we can immediately return False.

        # Consider the base b = n-2. This base is always within the required range
        # [2, n-2] for n >= 4.
        #
        # Case 1: n = 4
        # The range of bases to check is [2, n-2] = [2, 4-2] = [2, 2].
        # So, we only need to check base b=2.
        # Convert 4 to base 2:
        # 4 // 2 = 2, remainder 0
        # 2 // 2 = 1, remainder 0
        # 1 // 2 = 0, remainder 1
        # Reading remainders in reverse gives "100".
        # Is "100" a palindrome? No.
        # Therefore, for n=4, it is not strictly palindromic.

        # Case 2: n > 4
        # Consider base b = n-2.
        # We want to convert 'n' to base 'n-2'.
        # Using integer division and modulo:
        # n = q * (n-2) + r
        # We can write n as: n = 1 * (n-2) + 2
        # So, when n is divided by (n-2), the quotient (q) is 1 and the remainder (r) is 2.
        # This means the representation of 'n' in base 'n-2' is "12".
        # For example:
        # If n=5, b=n-2=3. 5 in base 3 is "12". (1*3 + 2 = 5)
        # If n=6, b=n-2=4. 6 in base 4 is "12". (1*4 + 2 = 6)
        # If n=9, b=n-2=7. 9 in base 7 is "12". (1*7 + 2 = 9)
        #
        # The string "12" is clearly not a palindrome (since '1' != '2').
        # This holds true for all n > 4, because '1' and '2' are valid digits
        # in any base b >= 3 (and n-2 >= 3 for n > 4).

        # Conclusion:
        # For n=4, its representation in base 2 ("100") is not palindromic.
        # For n > 4, its representation in base n-2 ("12") is not palindromic.
        # In both cases, we found at least one base 'b' in the required range
        # [2, n-2] for which 'n' is not palindromic.
        # Therefore, no integer 'n' (within the given constraints 4 <= n <= 10^5)
        # can be strictly palindromic. The function must always return False.

        return False
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
