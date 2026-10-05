# 1281. Subtract the Product and Sum of Digits of an Integer

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)  
**Topics:** Math

---

## 📝 Problem Statement

Given an integer number `n`, return the difference between the product of its digits and the sum of its digits.
 
Example 1:

```

**Input:** n = 234
**Output:** 15 
**Explanation:** 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

```

Example 2:

```

**Input:** n = 4421
**Output:** 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        Calculates the difference between the product and sum of the digits of n.
        Uses arithmetic operations to achieve O(1) auxiliary space without string conversion.
        """
        digit_product = 1
        digit_sum = 0
        
        while n > 0:
            # Extract the least significant digit
            digit = n % 10
            digit_product *= digit
            digit_sum += digit
            # Remove the least significant digit
            n //= 10
            
        return digit_product - digit_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the difference:
$$\text{Result} = (\prod_{i} d_i) - (\sum_{i} d_i)$$
where $d_i$ represents the digits of the positive integer $n$.

Rather than converting $n$ to a string (which allocates unnecessary heap memory), we can process each digit directly via arithmetic operations:
1. `n % 10` extracts the lowest order digit.
2. `n //= 10` removes the lowest order digit.
3. We maintain running variables `digit_product` initialized to `1` (multiplicative identity) and `digit_sum` initialized to `0` (additive identity).

### Step-by-Step Approach

1. Initialize `digit_product = 1` and `digit_sum = 0`.
2. Loop while $n > 0$:
   - Compute `digit = n % 10`.
   - Update `digit_product = digit_product * digit`.
   - Update `digit_sum = digit_sum + digit`.
   - Update `n = n // 10`.
3. Return `digit_product - digit_sum`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_{10} n)$
  In each iteration, $n$ is divided by $10$. The loop executes $\lfloor \log_{10} n \rfloor + 1$ times (the number of digits in $n$). For the given constraint $n \le 10^5$, this loop runs at most 6 times, which runs in well under a microsecond ($\mathcal{O}(1)$ practical time).
- **Space Complexity:** $\mathcal{O}(1)$
  Only two scalar accumulator variables (`digit_product` and `digit_sum`) and one loop variable are used. No additional strings, lists, or recursion stacks are allocated.

### Common Pitfalls / Mistakes Candidates Make

1. **String Conversion Overhead:** Converting `str(n)` creates string objects and list allocations if candidates use list comprehensions (e.g., `[int(c) for c in str(n)]`). While accepted for Easy problems, interviewers at Meta/Google evaluate memory consciousness and prefer pure numerical manipulation.
2. **Multiplication by Zero Initializer:** Initializing `digit_product = 0` instead of `1`, leading to a product that is permanently zero.
3. **Handling Inputs with Zero:** If the problem allowed $n = 0$, a standard `while n > 0:` loop wouldn't execute, requiring a base check. However, here $1 \le n \le 10^5$. If any intermediate digit is `0`, the product correctly becomes `0`.

### Real Interview Follow-Up Questions

#### 1. What if $n$ is extremely large and does not fit in a 64-bit integer (e.g., streamed over a network)?
*Answer:* Read the input as a stream of characters/bytes. Process each incoming character $c \in ['0', '9']$ on the fly:
- `digit = ord(c) - ord('0')`
- `digit_sum += digit`
- `digit_product *= digit`
- **Optimization:** If `digit == 0`, `digit_product` becomes `0` and will stay `0` forever, so we can stop multiplying and only accumulate `digit_sum` for the rest of the stream.

#### 2. What if $n$ can be negative?
*Answer:* Take the absolute value $|n|$ first, or define with the interviewer whether the negative sign applies to the leading digit or if digit manipulation is only defined on the magnitude of the number. Typically, $|n|$ is used.

#### 3. How would you handle potential integer overflow in languages like C++ or Java?
*Answer:* The maximum number of digits for a 64-bit unsigned integer is 20. The maximum product would be at most $9^{20} \approx 1.2 \times 10^{19}$, which fits within an unsigned 64-bit integer (`uint64_t`). For arbitrary-precision inputs, BigInteger arithmetic or early termination on encountering a `0` prevents unnecessary overhead.
