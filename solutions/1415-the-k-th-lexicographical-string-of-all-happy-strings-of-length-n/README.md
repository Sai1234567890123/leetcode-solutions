# 1415. The k-th Lexicographical String of All Happy Strings of Length n

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)  
**Topics:** String, Backtracking

---

## 📝 Problem Statement

A **happy string** is a string that:

	- consists only of letters of the set `['a', 'b', 'c']`.

	- `s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is 1-indexed).

For example, strings **"abc", "ac", "b"** and **"abcbabcbcb"** are all happy strings and strings **"aa", "baa"** and **"ababbc"** are not happy strings.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order.

Return *the kth string* of this list or return an **empty string** if there are less than `k` happy strings of length `n`.

 
Example 1:

```

**Input:** n = 1, k = 3
**Output:** "c"
**Explanation:** The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

```

Example 2:

```

**Input:** n = 1, k = 4
**Output:** ""
**Explanation:** There are only 3 happy strings of length 1.

```

Example 3:

```

**Input:** n = 3, k = 9
**Output:** "cab"
**Explanation:** There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Total number of happy strings of length n is 3 * 2^(n - 1)
        total_strings = 3 * (1 << (n - 1))
        
        # If k exceeds the total possible happy strings, return ""
        if k > total_strings:
            return ""
        
        # Convert k to 0-indexed for easier partition arithmetic
        k -= 1
        
        result = []
        
        # Determine the first character:
        # Each first character ('a', 'b', 'c') roots a subtree of size 2^(n - 1)
        block_size = 1 << (n - 1)
        first_char_index = k // block_size
        result.append(['a', 'b', 'c'][first_char_index])
        k %= block_size
        
        # Determine the remaining n - 1 characters
        # At each step, there are 2 choices (excluding the immediately preceding character)
        for i in range(1, n):
            block_size >>= 1
            choice_index = k // block_size
            k %= block_size
            
            # The two candidate characters in lexicographical order
            prev_char = result[-1]
            candidates = [ch for ch in ['a', 'b', 'c'] if ch != prev_char]
            
            result.append(candidates[choice_index])
            
        return "".join(result)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A brute-force or backtracking approach generates all happy strings up to the $k$-th one. While that easily passes LeetCode's constraints ($n \le 10$), an interviewer at Google or Meta will look for whether you can construct the answer directly without generating invalid or unnecessary strings.

We can view the happy strings as paths in a decision tree:
1. **First Character**: There are 3 choices: `'a'`, `'b'`, `'c'`. Each choice is the prefix for exactly $2^{n-1}$ strings.
2. **Subsequent Characters**: For each subsequent position, the character cannot match the preceding character, leaving exactly 2 choices. Each subtree from here has size $2^{\text{remaining}-1}$.

Because the choices are ordered lexicographically at every step, this problem can be solved in $O(n)$ time via **combinatorial number system / direct math indexing** (similar to finding the $k$-th permutation).

### Step-by-Step Approach

1. **Upper Bound Check**: Calculate the total number of happy strings: $3 \times 2^{n-1}$. If $k > 3 \times 2^{n-1}$, no such string exists; return `""`.
2. **0-Indexing**: Convert $k$ to a 0-indexed integer ($k \leftarrow k - 1$).
3. **First Character**:
   - Subtree size for each initial character is $2^{n-1}$.
   - The index of the first character among `['a', 'b', 'c']` is $\lfloor k / 2^{n-1} \rfloor$.
   - Update $k \leftarrow k \pmod{2^{n-1}}$.
4. **Subsequent Positions ($i = 1$ to $n-1$)**:
   - The subtree size is halved: $\text{block\_size} = 2^{n - 1 - i}$.
   - The two available characters are those in `['a', 'b', 'c']` different from `result[i - 1]`, sorted alphabetically.
   - Choose the character at index $\lfloor k / \text{block\_size} \rfloor$.
   - Update $k \leftarrow k \pmod{\text{block\_size}}$.
5. Assemble and return the characters as a string.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(n)$.
  At each step from $1$ to $n$, we perform $O(1)$ arithmetic operations and character lookups. Generating the final string of length $n$ takes $\mathcal{O}(n)$ time.
- **Space Complexity**: $\mathcal{O}(n)$.
  $\mathcal{O}(n)$ auxiliary space to store the list of characters before joining them into the final output string (which is optimal since the output string itself requires $\mathcal{O}(n)$ space).

### Common Pitfalls / Mistakes Candidates Make

1. **Off-by-one errors with $k$**: Forgetting to convert $1$-indexed $k$ to $0$-indexed makes integer division $\lfloor k / \text{block\_size} \rfloor$ incorrect on boundary values.
2. **Using standard backtracking ($O(2^n)$)**: While accepted under the constraint $n \le 10$, backtracking fails if $n$ is scaled up (e.g., $n = 60, k \le 10^{18}$). Top candidates identify the direct $O(n)$ construction.
3. **Improper candidate ordering**: When picking between the remaining two valid characters, failing to maintain alphabetical order will produce an incorrect lexicographical sequence.

### Real Interview Follow-Up Questions

#### 1. What if $n$ is up to 60 and $k \le 10^{18}$?
- **Answer**: The $O(n)$ combinatorial solution handles this out of the box because Python supports arbitrary-precision integers, and 64-bit integer types in languages like C++/Java can hold up to $2^{62}$. Backtracking would time out instantly ($2^{60} \approx 10^{18}$ operations).

#### 2. What if the alphabet size is $M$ instead of 3 (e.g., lowercase English letters $a-z$)?
- **Answer**: 
  - For the first character, there are $M$ choices, each with $(M-1)^{n-1}$ strings.
  - For subsequent characters, there are $M-1$ choices.
  - The block size transitions from $(M-1)^{n-1}$ down to $(M-1)^0$, dividing and moduloing by powers of $(M-1)$ at each step.

#### 3. What if strings cannot contain certain forbidden adjacent pairs (arbitrary transition graph)?
- **Answer**: This generalizes to finding the $k$-th path in a Directed Acyclic Graph (DAG) or finite state machine. We would use dynamic programming: compute $dp[i][c]$ (number of valid suffix strings of length $i$ starting with character $c$). Then, reconstruct the path greedily in $O(n \cdot |\Sigma|)$ by checking prefix counts.
