# 3658. GCD of Odd and Even Sums

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/gcd-of-odd-and-even-sums/](https://leetcode.com/problems/gcd-of-odd-and-even-sums/)  
**Topics:** Math, Number Theory

---

## 📝 Problem Statement

You are given an integer `n`. Your task is to compute the **GCD** (greatest common divisor) of two values:

	
	`sumOdd`: the sum of the smallest `n` positive odd numbers.
	
	
	`sumEven`: the sum of the smallest `n` positive even numbers.
	

Return the GCD of `sumOdd` and `sumEven`.

 
Example 1:

**Input:** n = 4

**Output:** 4

**Explanation:**

	- Sum of the first 4 odd numbers `sumOdd = 1 + 3 + 5 + 7 = 16`

	- Sum of the first 4 even numbers `sumEven = 2 + 4 + 6 + 8 = 20`

Hence, `GCD(sumOdd, sumEven) = GCD(16, 20) = 4`.

Example 2:

**Input:** n = 5

**Output:** 5

**Explanation:**

	- Sum of the first 5 odd numbers `sumOdd = 1 + 3 + 5 + 7 + 9 = 25`

	- Sum of the first 5 even numbers `sumEven = 2 + 4 + 6 + 8 + 10 = 30`

Hence, `GCD(sumOdd, sumEven) = GCD(25, 30) = 5`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        """
        Computes the greatest common divisor of:
        - sumOdd: the sum of the first n positive odd numbers
        - sumEven: the sum of the first n positive even numbers

        Mathematical derivation:
        1. sumOdd = 1 + 3 + ... + (2n - 1) = n^2
        2. sumEven = 2 + 4 + ... + 2n = n * (n + 1)
        3. gcd(sumOdd, sumEven) = gcd(n^2, n * (n + 1))
                                = n * gcd(n, n + 1)
        Since consecutive integers are coprime, gcd(n, n + 1) = 1.
        Therefore, gcd(n^2, n * (n + 1)) = n * 1 = n.
        """
        return n
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the greatest common divisor (GCD) of:
1. `sumOdd`: the sum of the first $n$ positive odd numbers.
2. `sumEven`: the sum of the first $n$ positive even numbers.

Instead of simulating the summation or running the Euclidean algorithm directly, we can analyze the mathematical formulas:
- The sum of the first $n$ positive odd numbers is an arithmetic series:
  $$\text{sumOdd} = \sum_{k=1}^n (2k - 1) = n^2$$
- The sum of the first $n$ positive even numbers is:
  $$\text{sumEven} = \sum_{k=1}^n 2k = 2 \cdot \frac{n(n + 1)}{2} = n(n + 1)$$

Now consider their GCD:
$$\gcd(\text{sumOdd}, \text{sumEven}) = \gcd(n^2, n(n + 1))$$

Using the property $\gcd(a \cdot k, b \cdot k) = k \cdot \gcd(a, b)$:
$$\gcd(n^2, n(n + 1)) = n \cdot \gcd(n, n + 1)$$

Any two consecutive integers $n$ and $n + 1$ are always coprime because:
$$\gcd(n, n + 1) = \gcd(n, (n + 1) - n) = \gcd(n, 1) = 1$$

Thus:
$$\gcd(\text{sumOdd}, \text{sumEven}) = n \cdot 1 = n$$

The result is always $n$ for any integer $n \ge 1$.

---

### Step-by-Step Approach

1. Return $n$ directly in $O(1)$ time and $O(1)$ space.

---

### Complexity Analysis

- **Time Complexity:** $O(1)$. Returning $n$ involves a single operation.
- **Space Complexity:** $O(1)$. No auxiliary memory is used.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Simulation Overkill:** Loop-based summation from $1$ to $n$ to compute the odd and even sums, resulting in $O(n)$ time complexity and potential integer overflow issues in languages with fixed-width integers (e.g., C++/Java if $n$ is large).
2. **Missing the Coprime Property:** Even candidates who use formulas $n^2$ and $n(n+1)$ sometimes call `math.gcd(n**2, n*(n+1))`. While mathematically correct, $n^2$ could overflow 64-bit integers for large $n$ in other languages, whereas the reduction to $n$ works effortlessly.

---

### Real Interview Follow-Up Questions & Answers

1. **What if $n$ is up to $10^{18}$?**
   - The direct $O(1)$ mathematical solution of returning $n$ handles values up to $10^{18}$ immediately, avoiding any 64-bit integer overflow that would occur when evaluating $n^2$ or $n(n+1)$.

2. **What if we asked for the GCD of the first $n$ multiples of $k$ and the first $n$ numbers congruent to $r \pmod k$?**
   - We generalize using the arithmetic series formula: $\text{sum}_1 = k \cdot \frac{n(n+1)}{2}$ and $\text{sum}_2 = n \cdot r + k \cdot \frac{n(n-1)}{2}$. We factor out common terms like $n$ and compute $\gcd(\text{sum}_1 / n, \text{sum}_2 / n)$ using the Euclidean algorithm in $O(\log n)$ time.
