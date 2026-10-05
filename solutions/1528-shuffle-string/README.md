# 1528. Shuffle String

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/shuffle-string/](https://leetcode.com/problems/shuffle-string/)  
**Topics:** Array, String

---

## 📝 Problem Statement

You are given a string `s` and an integer array `indices` of the **same length**. The string `s` will be shuffled such that the character at the `ith` position moves to `indices[i]` in the shuffled string.

Return *the shuffled string*.

 
Example 1:

```

**Input:** s = "codeleet", `indices` = [4,5,6,7,0,2,1,3]
**Output:** "leetcode"
**Explanation:** As shown, "codeleet" becomes "leetcode" after shuffling.

```

Example 2:

```

**Input:** s = "abc", `indices` = [0,1,2]
**Output:** "abc"
**Explanation:** After shuffling, each character remains in its position.

```

 
**Constraints:**

	- `s.length == indices.length == n`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        # Since Python strings are immutable, we initialize a list of the same length.
        n = len(s)
        res = [''] * n
        
        # Place each character at its target index.
        for char, target_idx in zip(s, indices):
            res[target_idx] = char
            
        # Join the list into the final restored string.
        return ''.join(res)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to place each character `s[i]` into the position specified by `indices[i]`. 

Because strings in Python are immutable, we cannot modify `s` in-place directly. The most straightforward and optimal way is to allocate a list of characters of size $n$, populate each character at its respective target index, and finally join the list into a string.

### Step-by-Step Approach

1. **Pre-allocate**: Initialize a list `res` of length $n$ with placeholder characters (`''`).
2. **Scatter**: Iterate simultaneously through `s` and `indices` using `zip`. For each character `char` at index `i`, assign `res[target_idx] = char`.
3. **Assemble**: Join `res` into a single string using `''.join(res)` and return it.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of the string `s`.
  - Iterating over the characters takes $\mathcal{O}(n)$.
  - Array lookups and writes are $\mathcal{O}(1)$.
  - Joining a list of $n$ characters into a string takes $\mathcal{O}(n)$.
  - Total Time: $\mathcal{O}(n)$.

- **Space Complexity:** $\mathcal{O}(n)$
  - We allocate an auxiliary list of length $n$ to hold the characters before joining.
  - The returned string also takes $\mathcal{O}(n)$ space.
  - Total Auxiliary Space: $\mathcal{O}(n)$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Repeated String Concatenation**: Trying to build strings via repeated concatenation (`res += char` or splicing) can degrade performance to $\mathcal{O}(n^2)$ due to Python's string immutability.
2. **Confusing Source and Target Indices**: Misinterpreting `indices[i]` as "the character from `indices[i]` goes to position `i`" instead of "the character at `i` goes to `indices[i]`".
3. **Sorting Overhead**: Writing `"".join([char for _, char in sorted(zip(indices, s))])` is valid and concise, but it costs $\mathcal{O}(n \log n)$ time complexity instead of the optimal $\mathcal{O}(n)$.

---

### Real Interview Follow-Up Questions & Answers

#### 1. Can we do this in $\mathcal{O}(1)$ auxiliary space?
*Answer:* In languages with mutable strings (like C++ or C), or if we are allowed to mutate an input `list[str]` in Python, we can achieve $\mathcal{O}(1)$ auxiliary space using **Cycle Sort**:
- Iterate from `i = 0` to `n - 1`. While `indices[i] != i`:
  - Swap `s[i]` with `s[indices[i]]`.
  - Swap `indices[i]` with `indices[indices[i]]`.
- Each swap puts at least one element into its correct final position, resulting in an $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ extra space algorithm.

#### 2. What if $n$ is extremely large (e.g., streaming or cannot fit into memory)?
*Answer:* If the data is partitioned across multiple nodes:
- We can treat `(indices[i], s[i])` as key-value pairs.
- Distribute keys across partitions via range partitioning or a MapReduce shuffle phase where the reducer writes the chunk in sequence to disk/output stream.

#### 3. What if `indices` contains invalid indices (out of bounds, duplicates, or negative values)?
*Answer:* In a real-world scenario, validate `indices` first:
- Check that `len(s) == len(indices)`.
- Use a boolean visited array / bitset or check that `0 <= idx < n` and verify it forms a valid permutation of `0` to `n - 1`. If invalid, throw an `InvalidArgumentException`.
