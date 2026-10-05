# 1662. Check If Two String Arrays are Equivalent

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)  
**Topics:** Array, String

---

## 📝 Problem Statement

Given two string arrays `word1` and `word2`, return* *`true`* if the two arrays **represent** the same string, and *`false`* otherwise.*

A string is **represented** by an array if the array elements concatenated **in order** forms the string.

 
Example 1:

```

**Input:** word1 = ["ab", "c"], word2 = ["a", "bc"]
**Output:** true
**Explanation:**
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
```

Example 2:

```

**Input:** word1 = ["a", "cb"], word2 = ["ab", "c"]
**Output:** false

```

Example 3:

```

**Input:** word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
**Output:** true

```

 
**Constraints:**

	- `1 3`

	- `1 3`

	- `1 3`

	- `word1[i]` and `word2[i]` consist of lowercase letters.

---

## 💻 Implementation (python3)

```py
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        # Pointers for word1: word index and character index
        w1_idx, c1_idx = 0, 0
        # Pointers for word2: word index and character index
        w2_idx, c2_idx = 0, 0
        
        len1, len2 = len(word1), len(word2)
        
        # Traverse both arrays simultaneously without concatenating
        while w1_idx < len1 and w2_idx < len2:
            # If characters at current positions do not match, return False
            if word1[w1_idx][c1_idx] != word2[w2_idx][c2_idx]:
                return False
            
            # Advance character pointer in word1
            c1_idx += 1
            # If end of current string in word1 is reached, move to the next string
            if c1_idx == len(word1[w1_idx]):
                w1_idx += 1
                c1_idx = 0
                
            # Advance character pointer in word2
            c2_idx += 1
            # If end of current string in word2 is reached, move to the next string
            if c2_idx == len(word2[w2_idx]):
                w2_idx += 1
                c2_idx = 0
                
        # Both arrays must be completely consumed at the same time
        return w1_idx == len1 and w2_idx == len2
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The trivial approach is to concatenate all strings in `word1` and `word2` (e.g., `"".join(word1) == "".join(word2)`). While concise, this requires $O(N + M)$ extra space to store the concatenated strings in memory, where $N$ and $M$ are the total number of characters in `word1` and `word2`. Moreover, if the very first characters differ, string concatenation wastes time building the full strings before performing the check.

In an interview setting at top-tier tech companies (like Google or Meta), the interviewer will almost certainly ask: *"Can you do this in $O(1)$ auxiliary space with early exit?"*

To achieve this:
1. Maintain two pointers for each array:
   - One pointer tracking the index of the current word in the array (`w_idx`).
   - Another pointer tracking the character position within that current word (`c_idx`).
2. Compare the characters at each step. If they ever mismatch, return `False` immediately.
3. Advance the character pointer; once it hits the length of the current string, reset it to `0` and advance the word pointer.
4. When the loop ends, return `True` only if both word pointers have reached the end of their respective arrays (confirming that neither array had trailing characters).

### Complexity Analysis

- **Time Complexity:** $O(\min(N, M))$
  - In the worst case (when the strings are equal or differ at the very end), we inspect each character once: $O(N + M)$ where $N$ is the total number of characters in `word1` and $M$ is the total number of characters in `word2`.
  - In the best/average case where a mismatch occurs early, the algorithm exits immediately in $O(1)$ or $O(k)$ steps.
- **Space Complexity:** $O(1)$ auxiliary space
  - We only store four integer pointer variables (`w1_idx`, `c1_idx`, `w2_idx`, `c2_idx`), avoiding allocating memory for joined strings.

---

### Common Pitfalls / Mistakes

1. **Memory Allocation via Join:** Relying on `"".join(word1) == "".join(word2)` is acceptable for an initial pass, but failing to recognize the $O(N + M)$ memory footprint shows a lack of optimization awareness for large-scale systems.
2. **Missing Trailing Characters:** Forgetting to check `w1_idx == len(word1) and w2_idx == len(word2)` after the while-loop. If `word1 = ["a"]` and `word2 = ["a", "b"]`, a naive pointer check without verifying that both reached the end might return `True`.
3. **Index Out of Bounds:** Not resetting the character pointer to `0` when incrementing the word pointer, leading to `IndexError`.

---

### Real Interview Follow-Up Questions & Answers

#### 1. "What if the inputs are unbounded streams of characters or strings?"
**Answer:** The two-pointer / generator pattern is naturally suited for streaming. We can replace list indexing with Python generators (`yield from s` for each string `s` in the stream) and pair them with `itertools.zip_longest(stream1, stream2, fillvalue=None)`. This keeps memory strictly bounded ($O(1)$ extra space) while streaming infinite or massive inputs.

#### 2. "How would you handle very large files stored on disk that cannot fit into RAM?"
**Answer:** Read both files in fixed-size buffers (e.g., 4KB or 64KB chunks). Compare the chunk buffers byte-by-byte using an offset pointer. When a chunk is exhausted, read the next block from disk. This bounds memory usage to $O(B)$ where $B$ is the buffer size.

#### 3. "Can this comparison be parallelized for very large arrays?"
**Answer:** If the character counts are huge and random access across strings is available, we could precompute prefix sums of character lengths to find the total length first (checking if `total_len1 == total_len2`). Then, parallel workers can verify disjoint segments of indices $[i, j]$. However, because character comparisons are cheap and CPU cache-friendly, the synchronization and prefix-sum overhead usually makes sequential traversal faster unless string sizes are in gigabytes and distributed across machines.
