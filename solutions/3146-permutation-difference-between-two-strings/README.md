# 3146. Permutation Difference between Two Strings

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/permutation-difference-between-two-strings/](https://leetcode.com/problems/permutation-difference-between-two-strings/)  
**Topics:** Hash Table, String

---

## 📝 Problem Statement

You are given two strings `s` and `t` such that every character occurs at most once in `s` and `t` is a permutation of `s`.

The **permutation difference** between `s` and `t` is defined as the **sum** of the absolute difference between the index of the occurrence of each character in `s` and the index of the occurrence of the same character in `t`.

Return the **permutation difference** between `s` and `t`.

 
Example 1:

**Input:** s = "abc", t = "bac"

**Output:** 2

**Explanation:**

For `s = "abc"` and `t = "bac"`, the permutation difference of `s` and `t` is equal to the sum of:

	- The absolute difference between the index of the occurrence of `"a"` in `s` and the index of the occurrence of `"a"` in `t`.

	- The absolute difference between the index of the occurrence of `"b"` in `s` and the index of the occurrence of `"b"` in `t`.

	- The absolute difference between the index of the occurrence of `"c"` in `s` and the index of the occurrence of `"c"` in `t`.

That is, the permutation difference between `s` and `t` is equal to `|0 - 1| + |1 - 0| + |2 - 2| = 2`.

Example 2:

**Input:** s = "abcde", t = "edbac"

**Output:** 12

**Explanation:** The permutation difference between `s` and `t` is equal to `|0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # Precompute the index of each character in string s.
        # Since each character appears at most once, a hash map provides O(1) lookups.
        s_indices = {char: idx for idx, char in enumerate(s)}
        
        # Calculate the sum of absolute differences between indices in s and t.
        total_diff = 0
        for idx_t, char in enumerate(t):
            total_diff += abs(s_indices[char] - idx_t)
            
        return total_diff
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the sum of absolute index differences between identical characters in two strings, $s$ and $t$. 
We are given that all characters in $s$ are unique, and $t$ is a permutation of $s$.

A brute-force approach would search for each character of $s$ in $t$ using linear search (`t.index(c)`), which takes $O(n)$ time per character, yielding $O(n^2)$ total time. 

To optimize:
1. We can precompute the position of each character in string $s$ using a hash map (or a fixed-size array of size 26 for lowercase English letters). This allows $O(1)$ index lookups.
2. We then iterate through string $t$ with its indices, look up the corresponding index in $s$, and accumulate $|index_s[c] - index_t[c]|$.

### Step-by-Step Approach

1. Create a hash map `s_indices` mapping each character in $s$ to its index.
2. Initialize `total_diff = 0`.
3. Iterate through $t$ using `enumerate(t)`, obtaining each character `char` and its index `idx_t`.
4. Add `abs(s_indices[char] - idx_t)` to `total_diff`.
5. Return `total_diff`.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the length of string $s$ (and $t$). Constructing the dictionary takes $O(n)$ time, and iterating over $t$ takes $O(n)$ time. With $n \le 26$, this executes in a few microseconds.
- **Space Complexity:** $O(|\Sigma|)$ or $O(1)$ auxiliary space, where $\Sigma$ is the alphabet size. Since the strings consist of unique lowercase English letters, the hash map holds at most 26 key-value pairs.

### Common Pitfalls / Mistakes Candidates Make

1. **Using `str.index()` inside a loop:** Calling `s.find(char)` or `t.index(char)` inside a loop degrades time complexity to $O(n^2)$. Even though $n \le 26$ makes it pass the LeetCode judge, interviewers at top-tier companies (Google/Meta) expect the asymptotically optimal $O(n)$ solution.
2. **Assuming 1-based indexing:** The problem is 0-indexed by default; shifting indices doesn't change $|(i + 1) - (j + 1)| = |i - j|$, but it's best to adhere strictly to the convention.

### Real Interview Follow-Up Questions

#### 1. What if characters can appear multiple times? (Handling Duplicates)
- **Answer:** If duplicates exist, the problem must clarify how occurrences match.
  - *Greedy / Order-preserving match:* The $k$-th occurrence of character $c$ in $s$ maps to the $k$-th occurrence in $t$. We can store a queue or list of indices for each character and pop/iterate through them in order ($O(n)$ time).
  - *Minimum Weight Matching:* If any occurrence of $c$ in $s$ can match any occurrence in $t$ to minimize the total permutation difference, sorting their index lists and pairing the $k$-th smallest indices is proven optimal by the rearrangement inequality ($O(n \log n)$ time).

#### 2. What if strings are extremely large and cannot fit entirely into memory (Streaming Data)?
- **Answer:** If $s$ arrives as a stream, we can't compute index differences on the fly without knowing where characters end up in $t$. However, we can stream $s$ to record `(char, index)` pairs into external storage (like an LSM-tree or distributed key-value store, or partitioned across machines by hash of character). Then, as $t$ streams in, we query the precomputed index for each character. If the alphabet is small (e.g., ASCII/Unicode subset), the hash map itself easily fits in memory even if the stream length is billions (assuming unique characters, max stream length is alphabet size).
