# 2485. Find the Pivot Integer

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-the-pivot-integer/](https://leetcode.com/problems/find-the-pivot-integer/)  
**Topics:** Math, Prefix Sum

---

## 📝 Problem Statement

Given a positive integer `n`, find the **pivot integer** `x` such that:

	- The sum of all elements between `1` and `x` inclusively equals the sum of all elements between `x` and `n` inclusively.

Return *the pivot integer *`x`. If no such integer exists, return `-1`. It is guaranteed that there will be at most one pivot index for the given input.

 
Example 1:

```

**Input:** n = 8
**Output:** 6
**Explanation:** 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

```

Example 2:

```

**Input:** n = 1
**Output:** 1
**Explanation:** 1 is the pivot integer since: 1 = 1.

```

Example 3:

```

**Input:** n = 4
**Output:** -1
**Explanation:** It can be proved that no such integer exist.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Sum of integers from 1 to n: S = n * (n + 1) / 2
        # Sum from 1 to x: x * (x + 1) / 2
        # Sum from x to n: S - (x - 1) * x / 2
        # Setting them equal:
        # x * (x + 1) / 2 = S - x * (x - 1) / 2
        # => x^2 = S = n * (n + 1) / 2
        total_sum = n * (n + 1) // 2
        
        # Calculate the integer square root
        x = math.isqrt(total_sum)
        
        # If total_sum is a perfect square, x is the pivot integer
        if x * x == total_sum:
            return x
            
        return -1
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for an integer $x \in [1, n]$ such that the sum of integers from $1$ to $x$ equals the sum from $x$ to $n$.

Let's represent the conditions mathematically:
1. The sum from $1$ to $x$ is given by the arithmetic progression formula:
   $$\text{Sum}(1, x) = \frac{x(x + 1)}{2}$$

2. The sum from $x$ to $n$ is:
   $$\text{Sum}(x, n) = \text{Sum}(1, n) - \text{Sum}(1, x - 1) = \frac{n(n + 1)}{2} - \frac{(x - 1)x}{2}$$

Setting both sides equal:
$$\frac{x(x + 1)}{2} = \frac{n(n + 1)}{2} - \frac{(x - 1)x}{2}$$

Multiplying through by $2$:
$$x(x + 1) + x(x - 1) = n(n + 1)$$
$$x^2 + x + x^2 - x = n(n + 1)$$
$$2x^2 = n(n + 1)$$
$$x^2 = \frac{n(n + 1)}{2}$$

This means that a valid pivot integer $x$ exists if and only if the total sum $\frac{n(n + 1)}{2}$ is a perfect square. If it is, $x = \sqrt{\frac{n(n + 1)}{2}}$. Otherwise, no such integer exists, and we return `-1`.

### Step-by-Step Approach

1. Compute the total sum of integers from $1$ to $n$: `total_sum = n * (n + 1) // 2`.
2. Compute the integer square root of `total_sum` using `math.isqrt(total_sum)`. This avoids floating-point inaccuracies that can occur with `math.sqrt`.
3. Check if `x * x == total_sum`.
   - If true, return `x`.
   - If false, return `-1`.

### Complexity Analysis

- **Time Complexity:** $O(1)$. Computing the sum, calculating `math.isqrt()`, and basic arithmetic operations execute in strictly $O(1)$ time.
- **Space Complexity:** $O(1)$. Only a few variables (`total_sum`, `x`) are allocated.

### Common Pitfalls / Mistakes Candidates Make

1. **Floating-point precision issues:** Using `math.sqrt(total_sum)` and checking `x.is_integer()` can result in precision errors for large values of $n$ (though $n \le 1000$ in this problem, in real interviews or scaled constraints, floating-point representations can fail). `math.isqrt` guarantees exact integer square root.
2. **$O(n)$ linear scan / Two Pointers / Binary Search:** While binary searching or a prefix sum array works and passes with $O(n)$ or $O(\log n)$, jumping straight to the $O(1)$ closed-form algebraic derivation demonstrates mathematical maturity expected at Google and Meta.
3. **Integer Overflow:** In languages like C++ or Java, `n * (n + 1)` could overflow a standard 32-bit signed integer if $n$ were larger (up to $10^9$). Using 64-bit integers (`long long` in C++) is crucial in those languages. Python handles arbitrarily large integers natively.

### Real Interview Follow-Up Questions

- **Follow-up 1: What if $n$ is up to $10^{18}$?**
  - *Answer:* The mathematical relation $x^2 = \frac{n(n + 1)}{2}$ still holds. For $n \approx 10^{18}$, $n(n + 1)$ is $\approx 10^{36}$, requiring 128-bit integers or big-integer arithmetic. We compute the integer square root using integer Newton's method or binary search over $[1, n]$ in $O(\log n)$ operations.

- **Follow-up 2: What if the array is an arbitrary non-decreasing sequence of integers $A$ instead of $1 \dots n$?**
  - *Answer:* If elements can be arbitrary non-negative numbers, the closed-form equation doesn't apply. Instead:
    - We compute prefix sums.
    - We can use binary search or two pointers in $O(n)$ time or $O(\log n)$ time (if searching for a split point where sum equals total sum).
