# 2652. Sum Multiples

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/sum-multiples/](https://leetcode.com/problems/sum-multiples/)  
**Topics:** Math

---

## 📝 Problem Statement

Given a positive integer `n`, find the sum of all integers in the range `[1, n]` **inclusive** that are divisible by `3`, `5`, or `7`.

Return *an integer denoting the sum of all numbers in the given range satisfying the constraint.*

 
Example 1:

```

**Input:** n = 7
**Output:** 21
**Explanation:** Numbers in the range `[1, 7]` that are divisible by `3`, `5,` or `7 `are `3, 5, 6, 7`. The sum of these numbers is `21`.

```

Example 2:

```

**Input:** n = 10
**Output:** 40
**Explanation:** Numbers in the range `[1, 10] that are` divisible by `3`, `5,` or `7` are `3, 5, 6, 7, 9, 10`. The sum of these numbers is 40.

```

Example 3:

```

**Input:** n = 9
**Output:** 30
**Explanation:** Numbers in the range `[1, 9]` that are divisible by `3`, `5`, or `7` are `3, 5, 6, 7, 9`. The sum of these numbers is `30`.

```

 
**Constraints:**

	- `1 3`

---

## 💻 Implementation (python3)

```py
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        """
        Calculates the sum of all integers in [1, n] divisible by 3, 5, or 7
        using the Principle of Inclusion-Exclusion (PIE) in O(1) time and space.
        """
        def sum_multiples_of(k: int) -> int:
            # Number of multiples of k in the range [1, n]
            m = n // k
            # Sum of arithmetic progression: k * (1 + 2 + ... + m) = k * m * (m + 1) // 2
            return k * m * (m + 1) // 2

        # 3, 5, and 7 are pairwise coprime, so:
        # lcm(3, 5) = 15, lcm(3, 7) = 21, lcm(5, 7) = 35, lcm(3, 5, 7) = 105
        return (
            sum_multiples_of(3)
            + sum_multiples_of(5)
            + sum_multiples_of(7)
            - sum_multiples_of(15)
            - sum_multiples_of(21)
            - sum_multiples_of(35)
            + sum_multiples_of(105)
        )
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the sum of all integers from `1` to `n` divisible by `3`, `5`, or `7`.

A straightforward approach is to iterate through each number $i \in [1, n]$ and check if $i \% 3 == 0$ or $i \% 5 == 0$ or $i \% 7 == 0$. While this runs in $O(n)$ time and easily passes the given constraints ($n \le 10^3$), it does not scale if $n \le 10^9$ or $10^{18}$.

To achieve an optimal $O(1)$ time complexity, we can use the **Principle of Inclusion-Exclusion (PIE)** combined with the arithmetic progression sum formula:
1. The sum of multiples of $k$ up to $n$ is:
   $$\text{Count } m = \lfloor n / k \rfloor$$
   $$\text{Sum} = k \cdot (1 + 2 + \dots + m) = k \cdot \frac{m(m + 1)}{2}$$
2. Since 3, 5, and 7 are pairwise coprime:
   - Multiples of both 3 and 5 are multiples of $\text{lcm}(3, 5) = 15$.
   - Multiples of both 3 and 7 are multiples of $\text{lcm}(3, 7) = 21$.
   - Multiples of both 5 and 7 are multiples of $\text{lcm}(5, 7) = 35$.
   - Multiples of 3, 5, and 7 are multiples of $\text{lcm}(3, 5, 7) = 105$.
3. Applying PIE:
   $$\text{Total Sum} = S(3) + S(5) + S(7) - S(15) - S(21) - S(35) + S(105)$$

---

### Step-by-Step Approach

1. Define a helper function `sum_multiples_of(k)` that computes the sum of multiples of $k \le n$ using the formula $k \times \frac{m(m + 1)}{2}$ where $m = \lfloor n / k \rfloor$.
2. Compute the individual sums for single divisors: $S(3)$, $S(5)$, and $S(7)$.
3. Subtract the pairwise intersections to eliminate double-counting: $S(15)$, $S(21)$, and $S(35)$.
4. Add back the triple intersection that was subtracted too many times: $S(105)$.
5. Return the resulting scalar value.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$  
  The formula performs a fixed number of basic arithmetic operations (integer division, multiplication, addition, and subtraction) regardless of the magnitude of $n$.
- **Space Complexity:** $\mathcal{O}(1)$  
  Only a few temporary integer variables are used.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Double Counting Multiples:** Simply calculating $S(3) + S(5) + S(7)$ without accounting for numbers like $15$ (divisible by 3 and 5) or $105$ (divisible by 3, 5, and 7).
2. **Assuming Non-Coprime LCMs are Just Products:** If the divisors were not prime (e.g., 4 and 6), candidates often use $4 \times 6 = 24$ instead of $\text{lcm}(4, 6) = 12$. Always use LCM when numbers are not guaranteed to be pairwise coprime.
3. **Integer Overflow:** In languages like C++ or Java, if $n$ is up to $10^9$, $m \times (m + 1)$ will overflow a 32-bit signed integer. 64-bit integers (`long long` in C++, `long` in Java) must be used.

---

### Real Interview Follow-Up Questions & How to Answer

1. **What if the list of divisors is arbitrary and dynamic, e.g., `divisors: List[int]` of size $K$?**
   - *Answer:* For small $K \le 20$, we can still use the Principle of Inclusion-Exclusion via bitmask iteration over all $2^K - 1$ non-empty subsets. For each subset, calculate the LCM of the elements. If the subset size is odd, add to total; if even, subtract.
   - Time Complexity: $\mathcal{O}(2^K \cdot K \log(\max(\text{divisors})))$.

2. **What if $K$ is large (e.g., $K \approx 10^5$) and $N$ is small/medium?**
   - *Answer:* PIE becomes exponential $\mathcal{O}(2^K)$ and infeasible. Instead, we can use a Sieve of Eratosthenes-like marking approach or dynamic programming / boolean array up to $N$ with time complexity $\mathcal{O}(N \cdot \text{number of unique prime factors})$ or simply $\mathcal{O}(N)$.

3. **How would you scale this for massive $N$ (e.g., $10^{18}$) and large $K$?**
   - *Answer:* If $N$ is up to $10^{18}$, direct iteration is impossible. We would use advanced analytic number theory techniques like the Meissel-Lehmer algorithm or Lucy Hedgehogs algorithm adapted for general divisor summatory functions.
