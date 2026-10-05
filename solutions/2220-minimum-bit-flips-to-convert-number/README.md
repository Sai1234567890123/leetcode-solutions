# 2220. Minimum Bit Flips to Convert Number

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/minimum-bit-flips-to-convert-number/](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/)  
**Topics:** Bit Manipulation

---

## 📝 Problem Statement

A **bit flip** of a number `x` is choosing a bit in the binary representation of `x` and **flipping** it from either `0` to `1` or `1` to `0`.

	- For example, for `x = 7`, the binary representation is `111` and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get `110`, flip the second bit from the right to get `101`, flip the fifth bit from the right (a leading zero) to get `10111`, etc.

Given two integers `start` and `goal`, return* the **minimum** number of **bit flips** to convert *`start`* to *`goal`.

 
Example 1:

```

**Input:** start = 10, goal = 7
**Output:** 3
**Explanation:** The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 1010 -> 1011.
- Flip the third bit from the right: 1011 -> 1111.
- Flip the fourth bit from the right: 1111 -> 0111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.
```

Example 2:

```

**Input:** start = 3, goal = 4
**Output:** 3
**Explanation:** The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
- Flip the first bit from the right: 011 -> 010.
- Flip the second bit from the right: 010 -> 000.
- Flip the third bit from the right: 000 -> 100.
It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.

```

 
**Constraints:**

	- `0 9`

 
**Note:** This question is the same as 461: Hamming Distance.

---

## 💻 Implementation (python3)

```py
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Calculates the minimum number of bit flips to convert start to goal.
        This is equivalent to finding the Hamming distance between the two numbers.
        """
        # XOR produces a 1 at each bit position where start and goal differ.
        diff = start ^ goal
        
        # Brian Kernighan's Algorithm to count set bits:
        # diff & (diff - 1) clears the lowest set bit.
        flips = 0
        while diff > 0:
            diff &= diff - 1
            flips += 1
            
        return flips
        
        # Note: In Python 3.10+, this can also be directly written as:
        # return (start ^ goal).bit_count()
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the minimum number of bit flips needed to transform `start` into `goal`. A bit flip is required at every index where the bit in `start` differs from the bit in `goal`.

1. **XOR Property**: The bitwise exclusive OR (`^`) of two bits yields `1` if and only if the bits are different ($0 \oplus 1 = 1$, $1 \oplus 0 = 1$), and `0` if they are the same ($0 \oplus 0 = 0$, $1 \oplus 1 = 0$).
2. Therefore, `start ^ goal` produces an integer whose set bits (bits equal to `1`) correspond exactly to the positions where flips are needed.
3. The problem reduces to counting the number of set bits (also known as the **Hamming weight** or **population count**) of `start ^ goal`.

### Step-by-Step Approach

1. Compute `diff = start ^ goal`.
2. Count the number of set bits in `diff`. While Python 3.10+ provides `(start ^ goal).bit_count()`, implementing **Brian Kernighan's Algorithm** is standard and demonstrates algorithmic mastery in an interview setting:
   - In each iteration, `diff &= (diff - 1)` clears the least significant set bit (rightmost 1).
   - Increment the counter by 1.
   - Continue until `diff` becomes 0.
   - The loop runs strictly $k$ times, where $k$ is the number of bits that need to be flipped ($k \le 30$ since $10^9 < 2^{30}$).

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(k)$ where $k$ is the number of bit flips required. Since numbers are bounded by $10^9 < 2^{30}$, $k \le 30$. In the worst case, this is $\mathcal{O}(\log(\max(\text{start}, \text{goal})))$, which is strictly bounded by 30 operations, effectively $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space as we only use a few integer variables (`diff`, `flips`).

---

### Common Pitfalls / Mistakes Candidates Make

1. **Converting to Binary Strings**: Candidates frequently do `bin(start)` and `bin(goal)`, pad with zeros to equalize lengths, and compare character-by-character. While technically functional, it incurs string allocation overhead ($\mathcal{O}(\log N)$ space) and signals unfamiliarity with standard bit manipulation.
2. **Checking Every Bit**: Iterating 30 or 32 times with `diff & 1` and `diff >>= 1` is common, but Brian Kernighan's algorithm (`diff &= (diff - 1)`) is faster because it skips runs of zeros.
3. **Integer Overflow Assumption**: While Python handles arbitrarily large integers automatically, candidates interviewing in C++ or Java might incorrectly assume arithmetic shifts instead of logical shifts if using signed types, or forget edge cases like negative values (though constraints specify non-negative here).

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if this needs to run at ultra-high frequency (billions of calls/sec)?
**Answer:** In hardware, this is supported directly via the `POPCNT` instruction (e.g., `__builtin_popcount` in GCC/Clang or Python's C-implemented `int.bit_count()`). At the software level, we can use a precomputed 8-bit lookup table (256 entries) to check 8 bits at a time, or use bit-parallel SWAR (SIMD within a register) algorithms.

#### 2. What if the inputs are arbitrary-length bit strings (e.g., 100,000 bits each)?
**Answer:** 
- Instead of using native 64-bit integer operations directly, process the streams in 64-bit or 256-bit (AVX-2/AVX-512) chunks.
- XOR corresponding 64-bit words and accumulate `popcount` over the chunks. This utilizes vectorized hardware instructions for $\mathcal{O}(N / W)$ throughput, where $W$ is the word size (64 or 256).

#### 3. How would you handle a streaming scenario where `start` and `goal` are being received bit-by-bit?
**Answer:** Maintain a single counter. At each step, read a bit from `stream_start` and a bit from `stream_goal`. If `bit_start != bit_goal`, increment the counter. This requires $\mathcal{O}(1)$ memory and processes each bit in $\mathcal{O}(1)$ time.
