# 3099. Harshad Number

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/harshad-number/](https://leetcode.com/problems/harshad-number/)  
**Topics:** Math

---

## 📝 Problem Statement

An integer divisible by the **sum** of its digits is said to be a **Harshad** number. You are given an integer `x`. Return* the sum of the digits *of* *`x`* *if* *`x`* *is a **Harshad** number, otherwise, return* *`-1`*.*

 
Example 1:

**Input:** x = 18

**Output:** 9

**Explanation:**

The sum of digits of `x` is `9`. `18` is divisible by `9`. So `18` is a Harshad number and the answer is `9`.

Example 2:

**Input:** x = 23

**Output:** -1

**Explanation:**

The sum of digits of `x` is `5`. `23` is not divisible by `5`. So `23` is not a Harshad number and the answer is `-1`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        """
        Determines if x is a Harshad number.
        A Harshad number is divisible by the sum of its digits.
        Returns the digit sum if it is a Harshad number, else -1.
        """
        digit_sum = 0
        temp = x
        
        # Calculate sum of digits mathematically without string conversion
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
            
        # Check divisibility condition
        if x % digit_sum == 0:
            return digit_sum
        
        return -1
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
A Harshad (or Niven) number is an integer divisible by the sum of its digits. 
To determine if $x$ satisfies this property:
1. Extract each digit of $x$ and compute their total sum.
2. Check if the original number $x$ is divisible by this computed sum using the modulo operator (`x % digit_sum == 0`).
3. Return `digit_sum` if true, or `-1` if false.

Instead of converting $x$ to a string (`str(x)`), we use standard arithmetic operations (`% 10` and `// 10`), which avoids heap allocations and is preferred in high-performance environments.

### Step-by-Step Approach
1. Initialize `digit_sum = 0` and copy $x$ into a temporary variable `temp` to preserve the original value of $x$.
2. In a loop while `temp > 0`:
   - Add the last digit (`temp % 10`) to `digit_sum`.
   - Remove the last digit by integer division (`temp //= 10`).
3. After the loop, check if `x % digit_sum == 0`.
   - If divisible, return `digit_sum`.
   - Otherwise, return `-1`.

### Complexity Analysis
- **Time Complexity:** $O(\log_{10} x)$
  The number of iterations equals the number of digits in $x$, which is $\lfloor \log_{10} x \rfloor + 1$. For $x \le 100$, this loop runs at most 3 times, effectively $O(1)$.
- **Space Complexity:** $O(1)$
  Only a few integer variables (`digit_sum`, `temp`) are used. No additional auxiliary memory or string allocation is required.

### Common Pitfalls / Mistakes Candidates Make
1. **Mutating the input directly:** Modifying `x` during the digit-sum loop without storing its initial value, leading to an incorrect modulo check at the end (`temp % digit_sum` instead of `x % digit_sum`).
2. **Division by Zero:** For positive integers ($x \ge 1$), `digit_sum` is guaranteed to be $\ge 1$. However, if constraints allowed $x = 0$, `digit_sum` would be `0`, resulting in a `ZeroDivisionError`.
3. **Inefficient String Conversions:** Using `sum(int(c) for c in str(x))` is acceptable for quick scripting, but in an interview setting, showing fluency with bitwise/arithmetic digit manipulation demonstrates a stronger grasp of fundamental computer science principles.

### Real Interview Follow-Up Questions & Answers

#### 1. How would you handle very large inputs (e.g., $x$ represented as a string with $10^6$ digits)?
*Answer:* When $x$ has millions of digits, it cannot fit into standard fixed-width integer registers. 
- The digit sum can still be computed in a single linear pass $O(N)$ over the string by summing `int(ch)`.
- To check $x \pmod{\text{digit\_sum}} == 0$, we can compute the modulo using Horner's method / streaming remainder arithmetic:
  ```python
  rem = 0
  for ch in x_str:
      rem = (rem * 10 + int(ch)) % digit_sum
  return digit_sum if rem == 0 else -1
  ```
  This keeps space complexity $O(1)$ beyond the input storage.

#### 2. What if numbers are streamed continuously?
*Answer:* If an arbitrary-precision integer is streamed digit-by-digit, we can buffer the digits into a disk/memory-mapped file or count the frequency of each digit $[0-9]$ to compute `digit_sum` on stream termination, then make a second pass to compute the stream modulo as shown above.

#### 3. How would this extend to arbitrary bases (e.g., base $B$)?
*Answer:* Instead of modulo and division by 10, use `% B` and `// B`. A number can be a Harshad number in one base (e.g., base 10) but not in another (e.g., base 2 or base 16).
