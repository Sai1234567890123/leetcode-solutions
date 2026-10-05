# 3895. Count Digit Appearances

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/count-digit-appearances/](https://leetcode.com/problems/count-digit-appearances/)  
**Topics:** Array, Math

---

## 📝 Problem Statement

You are given an integer array `nums` and an integer `digit`.

Return the total number of times `digit` appears in the decimal representation of all elements in `nums`.

 
Example 1:

**Input:** nums = [12,54,32,22], digit = 2

**Output:** 4

**Explanation:**

The digit 2 appears once in 12 and 32, and twice in 22. Thus, the total number of times digit 2 appears is 4.

Example 2:

**Input:** nums = [1,34,7], digit = 9

**Output:** 0

**Explanation:**

The digit 9 does not appear in the decimal representation of any element in `nums`, so the total number of times digit 9 appears is 0.

 
**Constraints:**

	- `1 6​​​​​​​`

	- `0

---

## 💻 Implementation (python3)

```py
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        target_char = str(digit)
        total_occurrences = 0
        
        # Iterate over each number in nums and count occurrences of target_char
        for num in nums:
            total_occurrences += str(num).count(target_char)
            
        return total_occurrences
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to determine the total number of times a single decimal `digit` appears across all integers in `nums`.

Each integer $x$ in `nums` has a decimal representation consisting of $\lfloor \log_{10}(|x|) \rfloor + 1$ digits (with 0 having 1 digit). 

There are two primary ways to approach this:
1. **Mathematical Extraction (`% 10` and `// 10`):** Repeatedly take the last digit modulo 10 and divide by 10. While purely arithmetic, handling the edge case of `0` requires an explicit branch or a do-while structure, and in Python, interpreted loop overhead is higher.
2. **String Conversion & Counting:** Convert each number to its string representation and use Python's built-in `.count()`. In Python, this leverages highly optimized C-level string search routines (`fastsearch`), making it both concise and practically faster for standard array sizes.

### Step-by-Step Approach

1. Convert `digit` to its string representation `target_char` once outside the loop to avoid redundant conversions.
2. Maintain a running sum `total_occurrences`.
3. For each number `num` in `nums`:
   - Convert `num` to `str(num)`.
   - Count the frequency of `target_char` within `str(num)` and add it to `total_occurrences`.
4. Return `total_occurrences`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot K)$, where $N$ is the number of elements in `nums` and $K$ is the maximum number of digits in an element (for a 32-bit signed integer, $K \le 10$; for a 64-bit integer, $K \le 19$). Because $K$ is bounded by a small constant, this is strictly linear $\mathcal{O}(N)$ time.
- **Space Complexity:** $\mathcal{O}(K)$ auxiliary space to store the string representation of a single number at any given time. This is $\mathcal{O}(1)$ auxiliary space.

### Common Pitfalls / Mistakes

1. **Handling Zero (`num = 0`):**
   - Candidates using mathematical division loops like `while num > 0:` often miss the case where `num == 0` and `digit == 0`. In such implementations, `0` is skipped, leading to undercounting.
2. **Negative Numbers:**
   - If negative numbers are present, the minus sign `'-'` should not be mistaken for a digit, nor should integer modulo behave unexpectedly (Python's `%` operator with negative numbers has specific floor-division semantics).
3. **Memory Bloat via Premature Aggregation:**
   - Writing `"".join(map(str, nums)).count(str(digit))` creates a massive monolithic string in memory containing all digits of all numbers, which can cause $\mathcal{O}(N \cdot K)$ memory overhead and potentially Memory Limit Exceeded (MLE) on huge datasets.

### Real Interview Follow-Up Questions

#### 1. What if the input is a continuous data stream that cannot fit in memory?
**Answer:** The current approach processes each integer independently. We can process numbers in an online fashion, maintaining only a single 64-bit integer counter `total_occurrences`. Memory footprint remains $\mathcal{O}(1)$.

#### 2. What if instead of an array `nums`, we are asked to count appearances of `digit` in all numbers in a range $[L, R]$ where $0 \le L \le R \le 10^{18}$?
**Answer:** An $\mathcal{O}(N)$ iteration will result in Time Limit Exceeded (TLE). We would use **Digit DP** (or combinatorial counting). 
- Formulate a helper function $f(N)$ that counts digit occurrences in $[0, N]$ in $\mathcal{O}(\log_{10} N)$ time.
- The answer for range $[L, R]$ is simply $f(R) - f(L - 1)$.

#### 3. How can we scale this across a distributed cluster (e.g., billions of numbers in MapReduce/Spark)?
**Answer:**
- **Map Phase:** Each worker node takes a partition of `nums`, computes the local count of `digit`, and outputs a `(digit, local_count)` key-value pair.
- **Reduce Phase:** Aggregates (sums) the partial counts from all workers to produce the final result.
