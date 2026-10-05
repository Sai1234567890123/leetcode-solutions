# 2185. Counting Words With a Given Prefix

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/counting-words-with-a-given-prefix/](https://leetcode.com/problems/counting-words-with-a-given-prefix/)  
**Topics:** Array, String, String Matching

---

## 📝 Problem Statement

You are given an array of strings `words` and a string `pref`.

Return *the number of strings in *`words`* that contain *`pref`* as a **prefix***.

A **prefix** of a string `s` is any leading contiguous substring of `s`.

 
Example 1:

```

**Input:** words = ["pay","**at**tention","practice","**at**tend"], `pref `= "at"
**Output:** 2
**Explanation:** The 2 strings that contain "at" as a prefix are: "**at**tention" and "**at**tend".

```

Example 2:

```

**Input:** words = ["leetcode","win","loops","success"], `pref `= "code"
**Output:** 0
**Explanation:** There are no strings that contain "code" as a prefix.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        """
        Counts the number of strings in 'words' that start with the prefix 'pref'.
        
        Time Complexity: O(N * L), where N is len(words) and L is len(pref).
        Space Complexity: O(1) auxiliary space.
        """
        # Python's str.startswith() is implemented in C and stops comparing
        # as soon as a mismatch occurs or the prefix length is satisfied.
        return sum(1 for word in words if word.startswith(pref))
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to count how many strings in a given array `words` begin with a specific prefix `pref`. 

A string $W$ has prefix $P$ if and only if:
1. $\text{length}(W) \ge \text{length}(P)$
2. $W[0 \dots |P|-1] == P$

In Python, the built-in `str.startswith()` method checks this condition directly in $O(|P|)$ time at the C-level without creating unnecessary substring slices. Summing over a generator expression allows us to count matches in a single pass with $O(1)$ auxiliary memory overhead.

### Step-by-Step Approach

1. Iterate over each `word` in `words`.
2. Check if `word.startswith(pref)` evaluates to `True`.
3. Aggregate the count of matching words using `sum()` with a generator expression.
4. Return the resulting count.

### Complexity Analysis

- **Time Complexity:** $O(N \cdot L)$
  - Let $N$ be the number of words in `words` (`len(words)`).
  - Let $L$ be the length of the prefix `pref` (`len(pref)`).
  - For each word, `startswith(pref)` compares at most $L$ characters before determining a match or mismatch.
  - Total time: $O(N \cdot L)$, which is optimal since every relevant character must be inspected.

- **Space Complexity:** $O(1)$ Auxiliary Space
  - Using a generator expression `(1 for word in words if ...)` avoids materializing an intermediate list in memory.
  - No additional data structures are created.

---

### Common Pitfalls / Mistakes

1. **Unnecessary String Slicing (`word[:len(pref)] == pref`):**
   - While functionally correct, slicing creates a new string object in memory for each word, incurring unnecessary allocation overhead ($O(L)$ space per word). `startswith()` avoids string copying.
2. **Missing Edge Cases (Length Mismatch):**
   - If manual index loops are written, failing to verify that `len(word) >= len(pref)` can result in `IndexOutOfBounds` exceptions in languages like Java/C++. `startswith()` handles this safely.
3. **Over-engineering with Trie for a Single Query:**
   - In an interview, building a Trie for a single `pref` query adds $O(\sum |word|)$ time and space overhead, which is strictly worse than scanning directly. Mention Tries only if multiple prefix queries are expected.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if there are $Q$ prefix queries on the same static list of words?
**Answer:** 
Building a **Trie (Prefix Tree)** or **Radix Tree** is optimal here:
- **Preprocessing:** Insert all words into the Trie in $O(\sum |word|)$ time. Store a `prefix_count` integer at each Trie node, incremented whenever a word passes through that node during insertion.
- **Querying:** For each query prefix $P$, traverse the Trie down $|P|$ edges. If the path exists, return the `prefix_count` at the terminating node in $O(|P|)$ time; otherwise return `0`.
- Total time: $O(\sum |word| + Q \cdot |P|)$ instead of $O(Q \cdot N \cdot |P|)$.

#### 2. What if the dataset is massive (e.g., billions of words) and does not fit in memory?
**Answer:**
- **MapReduce / Distributed Processing:** Partition the words across multiple worker nodes (shards). Each worker counts matches locally in $O(N_{\text{shard}} \cdot |pref|)$, and a central aggregator sums the counts (standard map-reduce pattern).
- **External Sorting:** If queries are frequent, sort words lexicographically on disk. Then, a prefix query can be answered via two binary searches (`bisect_left` for `pref` and `bisect_right` for `pref + \uffff`) on disk blocks/indexes.

#### 3. How to handle streaming words where queries happen concurrently?
**Answer:**
Use a concurrent Trie or a thread-safe hash map on prefixes up to a maximum length:
- If prefixes have a bounded length $L_{\max}$, maintaining a concurrent hash map `prefix -> count` updated on each incoming word allows $O(1)$ read queries.
- For unbounded prefixes, use a Trie with fine-grained node-level locking (e.g., Read-Write locks or Lock-Free Concurrent SkipLists) to allow simultaneous reads and writes without contention bottlenecks.
