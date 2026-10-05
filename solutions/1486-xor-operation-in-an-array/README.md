# 1486. XOR Operation in an Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/xor-operation-in-an-array/](https://leetcode.com/problems/xor-operation-in-an-array/)  
**Topics:** Math, Bit Manipulation

---

## 📝 Problem Statement

You are given an integer `n` and an integer `start`.

Define an array `nums` where `nums[i] = start + 2 * i` (**0-indexed**) and `n == nums.length`.

Return *the bitwise XOR of all elements of* `nums`.

 
Example 1:

```

**Input:** n = 5, start = 0
**Output:** 8
**Explanation:** Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.

```

Example 2:

```

**Input:** n = 4, start = 3
**Output:** 8
**Explanation:** Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def xor_prefix(k: int) -> int:
            """Helper function to compute XOR from 0 to k in O(1)."""
            rem = k % 4
            if rem == 0:
                return k
            elif rem == 1:
                return 1
            elif rem == 2:
                return k + 1
            else:
                return 0

        # We can express start + 2 * i as: 2 * (start // 2 + i) + (start % 2)
        # 1. Least Significant Bit (LSB):
        # Each element has the same LSB, which is (start & 1).
        # When XORed n times, it contributes 1 if both (start & 1) and (n & 1) are 1.
        lsb = (n & start & 1)

        # 2. Higher bits:
        # Shifting right by 1, the sequence becomes consecutive integers:
        # s, s + 1, s + 2, ..., s + n - 1, where s = start // 2.
        s = start >> 1
        higher_bits_xor = xor_prefix(s + n - 1) ^ xor_prefix(s - 1)

        # Combine the higher bits shifted back left by 1 and the LSB
        return (higher_bits_xor << 1) | lsb
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the XOR sum of an arithmetic progression:
$$\text{nums}[i] = \text{start} + 2i \quad \text{for } 0 \le i < n$$

While an $O(n)$ loop is the most straightforward approach and passes the given constraints, a Senior/Staff-level solution recognizes that bitwise XOR over structured arithmetic sequences can be solved in **$O(1)$ time and $O(1)$ space** by exploiting bitwise properties.

Let's decompose each term $\text{nums}[i]$:
$$\text{nums}[i] = 2 \cdot (\lfloor \text{start} / 2 \rfloor + i) + (\text{start} \bmod 2)$$

1. **Least Significant Bit (LSB)**:
   - Every term in the sequence has the same parity as $\text{start}$.
   - Thus, the LSB of every element is $\text{start} \ \& \ 1$.
   - XORing a bit $b$ an odd number of times gives $b$; an even number of times gives $0$.
   - Therefore, the final LSB is simply $(n \ \& \ 1) \ \& \ (\text{start} \ \& \ 1)$.

2. **Higher Bits (bits shifted right by 1)**:
   - If we divide each term by 2 (right-shift by 1), the sequence becomes consecutive integers:
     $$s, s + 1, s + 2, \dots, s + n - 1, \quad \text{where } s = \lfloor \text{start} / 2 \rfloor$$
   - The XOR sum of consecutive integers from $s$ to $s + n - 1$ is:
     $$\text{XOR}(s, s + n - 1) = \text{xorPrefix}(s + n - 1) \oplus \text{xorPrefix}(s - 1)$$
   - The cumulative XOR from $0$ to $k$ ($\text{xorPrefix}(k)$) repeats every 4 values:
     - $k \equiv 0 \pmod 4 \implies k$
     - $k \equiv 1 \pmod 4 \implies 1$
     - $k \equiv 2 \pmod 4 \implies k + 1$
     - $k \equiv 3 \pmod 4 \implies 0$

Combining the two parts gives the answer in $O(1)$ operations:
$$\text{result} = (\text{higher\_bits\_xor} \ll 1) \mid \text{lsb}$$

---

### Step-by-Step Approach

1. Define a helper function `xor_prefix(k)` that returns $\bigoplus_{j=0}^k j$ in $O(1)$ using the modulo 4 pattern.
2. Determine `lsb = n & start & 1`.
3. Set $s = \text{start} \gg 1$. Compute the range XOR for $s$ through $s + n - 1$ as `xor_prefix(s + n - 1) ^ xor_prefix(s - 1)`.
4. Shift the range XOR left by 1 and bitwise OR with `lsb`.

---

### Complexity Analysis

- **Time Complexity:** $O(1)$. We perform a constant number of arithmetic and bitwise operations regardless of the magnitude of $n$ or $\text{start}$.
- **Space Complexity:** $O(1)$. Only a few auxiliary scalar variables are used.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Overlooking the $O(1)$ solution**: Candidates usually write the $O(n)$ loop and stop there. In a top-tier interview (Google/Meta), presenting the $O(1)$ mathematical approach demonstrates deep mastery of bit manipulation.
2. **Off-by-one with `xor_prefix`**: Forgetting that XOR from $A$ to $B$ is $\text{xorPrefix}(B) \oplus \text{xorPrefix}(A - 1)$ and accidentally using $\text{xorPrefix}(A)$ which excludes $A$.
3. **Handling $k < 0$ in `xor_prefix`**: If $s = 0$, $s - 1 = -1$. In Python, `-1 % 4 == 3`, which correctly yields `0` in our helper, but in languages like C++/Java, negative modulo must be handled cleanly.

---

### Real Interview Follow-Up Questions

1. **What if the step size is an arbitrary integer $k$ instead of $2$?**
   - *Answer*: If $k$ is an arbitrary integer, the consecutive-integer reduction no longer directly applies to the higher bits. However, you can analyze each bit position $b \in [0, 62]$ independently. The $b$-th bit turns on periodically, which can be computed in $O(\log(\text{max\_val}))$ using floor division / counting multiples or using algorithms like the Digit DP / XOR sum of arithmetic progressions (often solvable using the Euclidean-like technique for $\sum \lfloor (ai + b)/m \rfloor$).

2. **What if $n$ is up to $10^{18}$?**
   - *Answer*: The standard $O(n)$ loop will Time Out (`TLE`), whereas this $O(1)$ mathematical solution handles $n = 10^{18}$ seamlessly within a few nanoseconds without integer overflow issues in Python (or using 64-bit unsigned integers in C++/Java).
