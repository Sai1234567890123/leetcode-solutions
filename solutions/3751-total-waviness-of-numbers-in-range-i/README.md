# 3751. Total Waviness of Numbers in Range I

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/)  
**Topics:** Math, Dynamic Programming, Enumeration

---

## 📝 Problem Statement

You are given two integers `num1` and `num2` representing an **inclusive** range `[num1, num2]`.

The **waviness** of a number is defined as the total count of its **peaks** and **valleys**:

	- A digit is a **peak** if it is **strictly greater** than both of its immediate neighbors.

	- A digit is a **valley** if it is **strictly less** than both of its immediate neighbors.

	- The first and last digits of a number **cannot** be peaks or valleys.

	- Any number with fewer than 3 digits has a waviness of 0.

Return the total sum of waviness for all numbers in the range `[num1, num2]`.
 
Example 1:

**Input:** num1 = 120, num2 = 130

**Output:** 3

**Explanation:**
In the range `[120, 130]`:

	- `120`: middle digit 2 is a peak, waviness = 1.

	- `121`: middle digit 2 is a peak, waviness = 1.

	- `130`: middle digit 3 is a peak, waviness = 1.

	- All other numbers in the range have a waviness of 0.

Thus, total waviness is `1 + 1 + 1 = 3`.

Example 2:

**Input:** num1 = 198, num2 = 202

**Output:** 3

**Explanation:**
In the range `[198, 202]`:

	- `198`: middle digit 9 is a peak, waviness = 1.

	- `201`: middle digit 0 is a valley, waviness = 1.

	- `202`: middle digit 0 is a valley, waviness = 1.

	- All other numbers in the range have a waviness of 0.

Thus, total waviness is `1 + 1 + 1 = 3`.

Example 3:

**Input:** num1 = 4848, num2 = 4848

**Output:** 2

**Explanation:**

Number `4848`: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

 
**Constraints:**

	- `1 5`

---

## 💻 Implementation (python3)

```py
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        """
        Calculates the total waviness of all numbers in the inclusive range [num1, num2].
        A peak occurs at index i if s[i-1] < s[i] > s[i+1].
        A valley occurs at index i if s[i-1] > s[i] < s[i+1].
        """
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            s = str(num)
            n = len(s)
            
            # Numbers with fewer than 3 digits cannot have peaks or valleys
            if n < 3:
                continue
                
            # Count peaks and valleys for the current number
            for i in range(1, n - 1):
                prev_d, curr_d, next_d = s[i - 1], s[i], s[i + 1]
                if (curr_d > prev_d and curr_d > next_d) or (curr_d < prev_d and curr_d < next_d):
                    total_waviness += 1
                    
        return total_waviness
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem defines the **waviness** of a number as the number of peaks and valleys in its decimal representation:
- A peak occurs at index $i$ if $s[i-1] < s[i] > s[i+1]$.
- A valley occurs at index $i$ if $s[i-1] > s[i] < s[i+1]$.
- Endpoints (first and last digits) cannot be peaks or valleys.
- Numbers with fewer than 3 digits have waviness equal to 0.

Given that this is "Range I" with constraints $1 \le num1 \le num2 \le 10^5$:
- The maximum number of digits is at most 6 (for $10^5$).
- Iterating through each integer in the range $[num1, num2]$ and inspecting the digits takes at most $O((num2 - num1 + 1) \cdot D)$ operations, where $D \le 6$.
- With $D \le 6$ and $(num2 - num1 + 1) \le 10^5$, this results in fewer than $5 \times 10^5$ operations, which executes in less than 50 milliseconds in Python.

### Step-by-Step Approach

1. Initialize `total_waviness = 0`.
2. Loop through each integer `num` from `num1` to `num2` (inclusive).
3. Convert `num` to its string representation `s`.
4. If the length of `s` is strictly less than 3, skip the number as it cannot have any internal peaks or valleys.
5. For each index $i$ from $1$ to $\text{len}(s) - 2$:
   - Check if $s[i]$ is strictly greater than both $s[i-1]$ and $s[i+1]$ (peak).
   - Check if $s[i]$ is strictly less than both $s[i-1]$ and $s[i+1]$ (valley).
   - If either condition holds, increment `total_waviness`.
6. Return `total_waviness`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}((num2 - num1 + 1) \cdot \log_{10}(num2))$.
  - Number of integers evaluated is at most $10^5$.
  - Each integer has at most $d = \lfloor \log_{10}(num2) \rfloor + 1 \le 6$ digits.
  - Overall operations $\le 10^5 \times 5 = 5 \times 10^5$, which easily runs well within the standard 2-second time limit.
- **Space Complexity:** $\mathcal{O}(\log_{10}(num2))$ auxiliary space to store the string representation of each number (at most 6 characters), which is $\mathcal{O}(1)$ auxiliary space.

### Common Pitfalls / Mistakes Candidates Make

1. **Non-Strict Inequalities:** Treating $\ge$ or $\le$ as peaks/valleys. The definition strictly requires `s[i] > s[i-1]` and `s[i] > s[i+1]` (or strictly `<`). Platues (e.g., `1221` where digits repeat) do not count.
2. **Boundary Digits:** Accidentally checking index `0` or index `len(s) - 1`. The problem explicitly states that endpoints can never be peaks or valleys.
3. **Numbers with $< 3$ Digits:** Failing to guard against numbers with 1 or 2 digits, which could cause out-of-bounds errors if using unconstrained loops.

### Real Interview Follow-Up Questions

#### 1. What if $num1, num2 \le 10^{18}$ ("Total Waviness of Numbers in Range II")?
*Answer:* Simulation will TLE. We use **Digit DP**.
- Define `f(N)` as the total waviness of all numbers in $[0, N]$. The answer is `f(num2) - f(num1 - 1)`.
- State in Digit DP: `dp(index, is_less, is_started, prev_digit, prev_prev_digit)`.
- At each step, to track total waviness across combinations, the DP function returns a pair: `(count_of_valid_numbers, total_waviness)`.
- When placing digit $d$, if `is_started` and `prev_prev_digit` is set, we check if `prev_digit` forms a peak or valley with `(prev_prev_digit, d)`. If it does, we add `count` to the total waviness.
- Time Complexity with Digit DP: $\mathcal{O}(18 \times 2 \times 2 \times 10 \times 10 \times 10) \approx \mathcal{O}(1)$ constant operations, running in $\approx 2$ ms.

#### 2. How would you handle a streaming data scenario where ranges $[num1, num2]$ are queried repeatedly?
*Answer:* 
- If $num \le 10^6$, compute a **prefix sum array** `prefix_waviness` where `prefix_waviness[x]` is the waviness of $x$. Any range query is answered in $\mathcal{O}(1)$ time via `prefix_sum[num2] - prefix_sum[num1 - 1]`.
