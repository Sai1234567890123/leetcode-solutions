# 1967. Number of Strings That Appear as Substrings in Word

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)  
**Topics:** Array, String

---

## 📝 Problem Statement

Given an array of strings `patterns` and a string `word`, return *the **number** of strings in *`patterns`* that exist as a **substring** in *`word`.

A **substring** is a contiguous sequence of characters within a string.

 
Example 1:

```

**Input:** patterns = ["a","abc","bc","d"], word = "abc"
**Output:** 3
**Explanation:**
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

```

Example 2:

```

**Input:** patterns = ["a","b","c"], word = "aaaaabbbbb"
**Output:** 2
**Explanation:**
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.

```

Example 3:

```

**Input:** patterns = ["a","a","a"], word = "ab"
**Output:** 3
**Explanation:** Each of the patterns appears as a substring in word "ab".

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        """
        Counts the number of strings in `patterns` that appear as substrings in `word`.
        Uses Python's highly-optimized C implementation of the in-operator (Boyer-Moore-Horspool).
        """
        # Sum the boolean results where pattern is found in word
        return sum(1 for pattern in patterns if pattern in word)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to count how many strings in the given list `patterns` exist as substrings within the target string `word`. 

A substring is a contiguous sequence of characters. In Python, checking whether a string $p$ is a substring of $W$ can be directly achieved via the `in` operator (`p in word`). Under the hood, Python utilizes an optimized combination of Boyer-Moore and Horspool algorithms implemented in C, which provides near-optimal performance in practice.

Given the constraints:
- $N = \text{len}(patterns) \le 100$
- $L = \text{len}(patterns[i]) \le 100$
- $M = \text{len}(word) \le 100$

Iterating through each pattern and checking substring inclusion directly is straightforward, clean, and requires no auxiliary memory.

---

### Step-by-Step Approach

1. Initialize a counter (or utilize a generator expression with `sum()`).
2. Iterate through each string `pattern` in `patterns`.
3. Check if `pattern in word`.
4. If true, increment the count by `1`.
5. Return the total count.

---

### Complexity Analysis

- **Time Complexity:** 
  - Let $N$ be the number of patterns, $L$ be the maximum length of a pattern, and $M$ be the length of `word`.
  - In the worst case, searching for a pattern of length $L$ in a string of length $M$ takes $O(L \times M)$ using naive search, or $O(L + M)$ using KMP / Boyer-Moore-Horspool.
  - Across all $N$ patterns, the total time complexity is $O(\sum |pattern_i| \times |word|)$ in the worst-case, which bounded by $O(N \times L \times M) \approx 100 \times 100 \times 100 = 10^6$ operations. This executes in a fraction of a millisecond.
- **Space Complexity:**
  - $O(1)$ auxiliary space since we evaluate patterns on the fly using a generator expression without storing intermediate structures.

---

### Common Pitfalls & Mistakes

1. **Confusing Substring with Subsequence:**
   - A substring must be contiguous (e.g., `"ace"` is a subsequence of `"abcde"`, but NOT a substring). Candidates sometimes jump to two-pointer subsequence checking by mistake.
2. **Over-engineering for Small Constraints:**
   - Jumping straight to implementing an Aho-Corasick automaton or Suffix Automaton without confirming constraints. In an interview, mention the optimal theoretical algorithm first, but code the concise and clean solution if constraints are tiny unless instructed otherwise.
3. **Double Counting Identical Strings:**
   - Notice Example 3: `patterns = ["a", "a", "a"]`, `word = "ab"` gives `3`. Do not deduplicate using `set(patterns)` unless you multiply by the frequency of each pattern.

---

### Real Interview Follow-Up Questions

#### 1. What if `word` is massive (e.g., $10^7$ characters) and queried once?
- **Answer:** Preprocessing `word` is optimal here. Build a **Suffix Automaton** or **Suffix Tree** on `word` in $O(|word|)$ time and $O(|word| \cdot |\Sigma|)$ space. Once built, checking if any pattern $p$ exists in `word` takes only $O(|p|)$ time by traversing the automaton states. Total query time becomes $O(\sum |p_i|)$.

#### 2. What if `patterns` contains millions of short strings (e.g., dictionary lookup on a stream of text)?
- **Answer:** Build an **Aho-Corasick Automaton** (a trie augmented with failure transitions) using all patterns in `patterns`. We can then stream the text `word` through the automaton in $O(|word| + \text{matches})$ time. This finds all occurrences of all patterns simultaneously in a single pass over `word`.

#### 3. What if `patterns` contains many duplicates?
- **Answer:** Use a frequency map / hash map (`collections.Counter(patterns)`). Check each unique pattern once against `word` and add its frequency to the total count if present:
  ```python
  counts = Counter(patterns)
  return sum(freq for pat, freq in counts.items() if pat in word)
  ```
