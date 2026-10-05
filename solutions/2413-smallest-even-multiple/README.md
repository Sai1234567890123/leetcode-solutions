# 2413. Smallest Even Multiple

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/smallest-even-multiple/](https://leetcode.com/problems/smallest-even-multiple/)  
**Topics:** Math, Number Theory

---

## 📝 Problem Statement

Given a **positive** integer `n`, return *the smallest positive integer that is a multiple of **both** *`2`* and *`n`.
 
Example 1:

```

**Input:** n = 5
**Output:** 10
**Explanation:** The smallest multiple of both 5 and 2 is 10.

```

Example 2:

```

**Input:** n = 6
**Output:** 6
**Explanation:** The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """
        Returns the smallest positive integer that is a multiple of both 2 and n (i.e., lcm(2, n)).
        If n is already even, the answer is n.
        If n is odd, the answer is 2 * n.
        """
        # If n is odd (n & 1 == 1), shift left by 1 (multiply by 2).
        # If n is even (n & 1 == 0), shift left by 0 (keep n as is).
        return n << (n & 1)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the smallest positive integer that is a multiple of both `2` and `n`. In mathematical terms, this is simply the **Least Common Multiple (LCM)** of `2` and `n`: $\text{lcm}(2, n)$.

Recall the relationship between LCM and GCD:
$$\text{lcm}(a, b) = \frac{a \times b}{\gcd(a, b)}$$

For $a = 2$:
1. If $n$ is **even**, $\gcd(2, n) = 2$, which gives $\text{lcm}(2, n) = \frac{2 \times n}{2} = n$.
2. If $n$ is **odd**, $\gcd(2, n) = 1$, which gives $\text{lcm}(2, n) = \frac{2 \times n}{1} = 2n$.

Thus:
- If $n \% 2 == 0$, the answer is $n$.
- If $n \% 2 \neq 0$, the answer is $2 \times n$.

This can be written cleanly using branchless bit manipulation:
`(n & 1)` evaluates to `1` when $n$ is odd and `0` when $n$ is even. Shifting $n$ left by `(n & 1)` bits computes $n \times 2^1 = 2n$ for odd numbers, and $n \times 2^0 = n$ for even numbers.

---

### Step-by-Step Approach

1. **Parity Check**: Check the least significant bit of $n$ using `n & 1`.
2. **Conditional Scaling**:
   - If `n & 1 == 0` (even), shift $n$ by $0$ bits $\rightarrow n$.
   - If `n & 1 == 1` (odd), shift $n$ by $1$ bit $\rightarrow 2n$.
3. Return the result.

---

### Complexity Analysis

- **Time Complexity:** $O(1)$. Bitwise AND and shift operations run in constant time.
- **Space Complexity:** $O(1)$. No auxiliary memory is used.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Over-engineering with Loops**: Writing a `while` loop that increments by $1$ or $2$ until finding a multiple of both $2$ and $n$. While it passes the small constraints ($n \le 150$), it demonstrates weak mathematical maturity and fails under larger constraints.
2. **Importing Full Math Libraries**: Using `math.lcm(2, n)` is valid in Python 3.9+, but in an interview setting, demonstrating the mathematical derivation ($n$ vs $2n$) is expected and preferred.
3. **Integer Overflow in Other Languages**: In languages like C++ or Java, if $n$ could be near `INT_MAX`, `2 * n` could overflow a 32-bit signed integer. In Python, integers have arbitrary precision, but mentioning potential overflow shows Senior/Staff-level awareness.

---

### Real Interview Follow-Up Questions

#### 1. What if the problem asks for $\text{lcm}(k, n)$ for an arbitrary $k$?
- **Answer**: Use the Euclidean algorithm to compute $\gcd(k, n)$ in $O(\log(\min(k, n)))$ time, then return $(k \times n) // \gcd(k, n)$. To avoid intermediate overflow in fixed-width integer languages, divide before multiplying: $(k // \gcd(k, n)) \times n$.

#### 2. How would you handle a high-throughput stream of integers?
- **Answer**: Since the operation is branchless $O(1)$ (`n << (n & 1)`), it is easily vectorizable using SIMD instructions (e.g., AVX-512 / NEON) to process multiple elements per CPU cycle.

#### 3. What if $n$ can be negative or zero?
- **Answer**: Multiples are typically defined for non-zero integers. If $n = 0$, technically $\text{lcm}(2, 0)$ is undefined or $0$ depending on convention. If $n < 0$, since the question asks for the *smallest positive integer*, the result must be positive, so we should first take $|n|$.
