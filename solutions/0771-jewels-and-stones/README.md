# 0771. Jewels and Stones

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/jewels-and-stones/](https://leetcode.com/problems/jewels-and-stones/)  
**Topics:** Hash Table, String

---

## 📝 Problem Statement

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

 
Example 1:
```
**Input:** jewels = "aA", stones = "aAAbbbb"
**Output:** 3

```Example 2:
```
**Input:** jewels = "z", stones = "ZZ"
**Output:** 0

```
 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Counts how many stones are also jewels using an O(1) lookup hash set.
        """
        # Convert jewels into a set for O(1) average-time membership tests.
        jewel_set = set(jewels)
        
        # Count the number of characters in stones that exist in jewel_set.
        return sum(stone in jewel_set for stone in stones)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires us to determine how many characters in `stones` belong to the collection of characters specified in `jewels`. 

A brute-force approach would check each character of `stones` against every character of `jewels`, resulting in an $O(J \times S)$ time complexity (where $J$ is the length of `jewels` and $S$ is the length of `stones`).

To optimize this:
1. Converting `jewels` into a hash set allows $O(1)$ average-time membership checks.
2. We then iterate over each character in `stones` and increment our counter whenever the character is present in the set.

### Step-by-Step Approach

1. **Hash Set Construction**: Build a set `jewel_set` from the characters in `jewels`. This takes $O(J)$ time.
2. **Iteration and Counting**: Iterate through each character in `stones`. Check if `stone in jewel_set`. In Python, `sum(stone in jewel_set for stone in stones)` leverages the fact that boolean `True` evaluates to `1` and `False` evaluates to `0`.
3. **Return Count**: The aggregated sum is the total number of jewels among our stones.

### Complexity Analysis

- **Time Complexity:** $O(J + S)$
  - Building the set from `jewels` takes $O(J)$ time.
  - Iterating through `stones` takes $O(S)$ time with $O(1)$ lookup per character.
  - Overall time complexity is linear: $O(J + S)$.
- **Space Complexity:** $O(J)$ or $O(1)$
  - Storing the unique jewels takes $O(J)$ space.
  - Since the alphabet consists only of English letters (upper and lower case), the set can contain at most $52$ unique characters. Thus, the auxiliary space is strictly bounded by $O(\min(J, |\Sigma|)) = O(1)$ in practice.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Quadratic Lookup in Python:** Writing `sum(stone in jewels for stone in stones)` without converting `jewels` to a `set`. In Python, `in` on a string takes $O(J)$ time, silently degrading performance to $O(J \times S)$.
2. **Case Sensitivity Oversight:** Forgetting that `'a'` and `'A'` are distinct characters (e.g., calling `.lower()` prematurely).
3. **Overcomplicating Data Structures:** Using a full `Counter` / hash map for `jewels` when a simple `set` suffices, as we only need membership testing for jewels, not frequency.

---

### Real Interview Follow-Up Questions

#### 1. What if memory is extremely constrained (e.g., embedded system or $O(1)$ auxiliary space strictly required)?
- **Answer:** Since the character set is bounded by standard ASCII letters ($A-Z, a-z$), we can use a **64-bit integer bitmask** instead of a hash set:
  - Map each character to an index from 0 to 51: 
    - `'a'-'z'` $\to 0 \dots 25$
    - `'A'-'Z'` $\to 26 \dots 51$
  - Set the bit at index $i$: `mask |= (1 << idx)`.
  - Check membership with bitwise AND: `(mask & (1 << idx)) != 0`.
  - This requires strictly $O(1)$ extra memory (a single 64-bit integer).

#### 2. What if `stones` is a massive, unbounded data stream?
- **Answer:** Precompute the `jewel_set` once in memory. As stones stream in, process them one by one or in micro-batches (chunking), maintaining a running count:
  ```python
  jewel_set = set(jewels)
  jewel_count = 0
  for stone in stone_stream:
      if stone in jewel_set:
          jewel_count += 1
  ```
  This requires $O(1)$ additional space beyond the initial set and processes items with minimal latency ($O(1)$ per incoming stone).

#### 3. What if `stones` is stored across a distributed file system (e.g., petabytes of log data)?
- **Answer:** Use a MapReduce / distributed data processing framework (such as Apache Spark):
  - **Broadcast Variable:** Broadcast the `jewel_set` to all worker nodes (since it is small).
  - **Map Phase:** Each worker reads a partition of `stones` and counts occurrences locally.
  - **Reduce Phase:** Sum the partial counts across all workers to produce the final result.
