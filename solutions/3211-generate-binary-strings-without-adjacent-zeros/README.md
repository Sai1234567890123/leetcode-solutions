# 3211. Generate Binary Strings Without Adjacent Zeros

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/)  
**Topics:** String, Backtracking, Bit Manipulation

---

## 📝 Problem Statement

You are given a positive integer `n`.

A binary string `x` is **valid** if all substrings of `x` of length 2 contain **at least** one `"1"`.

Return all **valid** strings with length `n`**, **in *any* order.

 
Example 1:

**Input:** n = 3

**Output:** ["010","011","101","110","111"]

**Explanation:**

The valid strings of length 3 are: `"010"`, `"011"`, `"101"`, `"110"`, and `"111"`.

Example 2:

**Input:** n = 1

**Output:** ["0","1"]

**Explanation:**

The valid strings of length 1 are: `"0"` and `"1"`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def validStrings(self, n: int) -> list[str]:
        result: list[str] = []
        path: list[str] = []

        def backtrack(index: int) -> None:
            # Base case: reached the required string length
            if index == n:
                result.append("".join(path))
                return

            # Option 1: We can always append '1'
            path.append('1')
            backtrack(index + 1)
            path.pop()

            # Option 2: We can append '0' only if the preceding character is not '0'
            # (or if this is the first character being placed)
            if not path or path[-1] != '0':
                path.append('0')
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for all binary strings of length $n$ containing no adjacent zeros (i.e., the substring `"00"` is not permitted).

This condition means:
- If the current character is `'0'`, the next character **must** be `'1'`.
- If the current character is `'1'`, the next character can be either `'0'` or `'1'`.
- For the first character (at index 0), we can choose either `'0'` or `'1'`.

The number of valid binary strings of length $n$ without consecutive zeros follows the Fibonacci sequence:
- $n = 1 \implies 2$ strings ($F_3$)
- $n = 2 \implies 3$ strings ($F_4$)
- $n = 3 \implies 5$ strings ($F_5$)
- $n = k \implies F_{k+2}$ strings

Since $n \le 18$, $F_{20} = 6,765$, which is very small. A standard backtracking (DFS) approach that builds each valid string character-by-character without ever exploring invalid branches will be optimal.

### Step-by-Step Approach

1. Maintain a dynamic list `path` representing the current prefix of the binary string being built.
2. Define a recursive helper function `backtrack(index)`:
   - **Base Case:** If `index == n`, a full valid string is formed. Join the characters in `path` into a string and append to `result`.
   - **Recursive Step:**
     - Always explore placing `'1'` because `'1'` never violates the `"no two adjacent zeros"` rule.
     - Explore placing `'0'` only if `path` is empty (index 0) or the last character in `path` is `'1'`.
   - Backtrack by popping from `path` after each recursive exploration to restore state.

### Complexity Analysis

- **Time Complexity:** $O(n \cdot F_{n+2})$, where $F_k$ is the $k$-th Fibonacci number.
  - The number of valid strings generated is exactly $F_{n+2}$.
  - Generating each string takes $O(1)$ amortized steps per node in the recursion tree (no dead ends are ever explored).
  - Copying each valid string of length $n$ into the result list takes $O(n)$ time.
  - For $n = 18$, $F_{20} = 6,765$, leading to around $18 \times 6,765 \approx 1.2 \times 10^5$ operations, running in a few milliseconds.
- **Space Complexity:** $O(n)$ auxiliary space (excluding the output list).
  - The recursion stack reaches a maximum depth of $n$.
  - The `path` buffer holds at most $n$ characters at any point.

### Common Pitfalls / Mistakes Candidates Make

1. **Generating All $2^n$ Strings and Filtering:** Candidates often generate all $2^n$ combinations and filter with `"00" not in s`. For $n = 18$, $2^{18} = 262,144$, which does pass LeetCode constraints, but in a real interview (e.g., at Meta or Google), generating dead-end states is viewed as suboptimal compared to pruning-by-construction.
2. **String Immutability Overhead:** Concatenating strings (`s + "0"`) at every recursive step creates intermediate string objects. Using a shared mutable list (`path.append()` and `path.pop()`) is idiomatic and avoids unnecessary allocations.

### Real Interview Follow-Up Questions

1. **What if $n$ is large (e.g., $n = 10^9$) and we only need to return the count of valid strings modulo $10^9 + 7$?**
   - *Answer:* The count is simply the Fibonacci number $F_{n+2}$. We can compute this in $O(\log n)$ time using $2 \times 2$ matrix exponentiation:
     $$\begin{pmatrix} F_{k+1} \\ F_k \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^k \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

2. **What if we need to return the $k$-th lexicographically valid string without generating all of them?**
   - *Answer:* We can determine each bit one by one using a combinatorics / digit DP approach:
     - At each position, count how many valid strings would be formed if we choose `'0'` (which requires the next character to be `'1'`).
     - If $k$ is within that count, choose `'0'`.
     - Otherwise, subtract that count from $k$ and choose `'1'`.
     - This solves the query in $O(n)$ time.

3. **What if the output doesn't fit into memory (e.g., streaming/generator)?**
   - *Answer:* Convert `backtrack` into a Python generator using `yield` and `yield from`. This allows the caller to iterate over solutions one at a time using $O(n)$ total memory.
