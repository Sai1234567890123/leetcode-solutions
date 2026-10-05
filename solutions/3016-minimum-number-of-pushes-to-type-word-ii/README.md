# 3016. Minimum Number of Pushes to Type Word II

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/)  
**Topics:** Hash Table, String, Greedy, Sorting, Counting

---

## 📝 Problem Statement

You are given a string `word` containing lowercase English letters.

Telephone keypads have keys mapped with **distinct** collections of lowercase English letters, which can be used to form words by pushing them. For example, the key `2` is mapped with `["a","b","c"]`, we need to push the key one time to type `"a"`, two times to type `"b"`, and three times to type `"c"` *.*

It is allowed to remap the keys numbered `2` to `9` to **distinct** collections of letters. The keys can be remapped to **any** amount of letters, but each letter **must** be mapped to **exactly** one key. You need to find the **minimum** number of times the keys will be pushed to type the string `word`.

Return *the **minimum** number of pushes needed to type *`word` *after remapping the keys*.

An example mapping of letters to keys on a telephone keypad is given below. Note that `1`, `*`, `#`, and `0` do **not** map to any letters.

 
Example 1:

```

**Input:** word = "abcde"
**Output:** 5
**Explanation:** The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.

```

Example 2:

```

**Input:** word = "xyzxyzxyzxyz"
**Output:** 12
**Explanation:** The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.

```

Example 3:

```

**Input:** word = "aabbccddeeffgghhiiiiii"
**Output:** 24
**Explanation:** The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
"f" -> one push on key 7
"g" -> one push on key 8
"h" -> two pushes on key 9
"i" -> one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.

```

 
**Constraints:**

	- `1 5`

	- `word` consists of lowercase English letters.

---

## 💻 Implementation (python3)

```py
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequency of each letter in the input string
        counts = Counter(word)
        
        # Step 2: Sort frequencies in descending order to assign the most frequent
        # letters to the keypad slots that require the fewest pushes.
        sorted_freqs = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        # Step 3: Keys 2 through 9 give us 8 available keys.
        # The first 8 letters require 1 push, the next 8 require 2 pushes, and so on.
        for idx, freq in enumerate(sorted_freqs):
            pushes_per_char = (idx // 8) + 1
            total_pushes += freq * pushes_per_char
            
        return total_pushes
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

We have 8 distinct keys available (keys `2` through `9`). When multiple letters are assigned to a single key, the $k$-th letter mapped to that key requires $k$ presses to type.

To minimize the total number of presses for the entire string:
1. The most frequently occurring characters should require the minimum number of presses.
2. Since we have 8 distinct keys, we can assign 8 characters to the "first slot" (1 press each) across all 8 keys.
3. The next 8 most frequent characters can be placed in the "second slot" (2 presses each).
4. The subsequent 8 characters take the "third slot" (3 presses each).
5. The remaining characters (at most 2 in standard English alphabet) take the "fourth slot" (4 presses each).

This is a classic greedy problem where the optimal substructure dictates matching the largest character frequencies with the smallest press multipliers.

---

### Step-by-Step Approach

1. **Frequency Count**: Count the frequency of each unique character in `word`.
2. **Sort Frequencies**: Sort these frequencies in descending order.
3. **Calculate Weighted Pushes**:
   - Iterate over the sorted frequencies with an index `idx` (0-indexed).
   - The number of pushes required for the character at `idx` is `(idx // 8) + 1`.
   - Accumulate `freq * ((idx // 8) + 1)` into the total.
4. **Return Result**: Return the accumulated sum.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$, where $N$ is the length of `word`.
  - Counting character frequencies takes $\mathcal{O}(N)$ time.
  - Sorting the frequencies takes $\mathcal{O}(|\Sigma| \log |\Sigma|)$ time, where $|\Sigma|$ is the size of the alphabet ($26$). Since $|\Sigma| \le 26$, this step takes $\mathcal{O}(1)$ time.
  - Overall Time Complexity: $\mathcal{O}(N)$.

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.
  - The frequency table and sorted array store at most $26$ elements, which is independent of the input size $N$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Trying to Map Explicit Keys**: Overcomplicating the solution by attempting to assign specific characters to specific key numbers (e.g., mapping 'a' to '2', 'b' to '3'). The problem only asks for the minimum push count, not the actual layout.
2. **Dynamic Programming / Backtracking**: Candidates sometimes overthink this as a partition or knapsack DP problem. Because slots on keys are interchangeable and independent, a greedy approach is provably optimal.
3. **Off-by-one with Key Count**: Keys are `2` through `9`, which is $9 - 2 + 1 = 8$ keys, not $9$ or $10$.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input `word` is a massive stream that does not fit in memory?
**Answer**:
- If the stream is too large for memory, we do not need to store the string. Because the alphabet size $|\Sigma| = 26$ is tiny, we only need a fixed array of size 26 in memory to maintain frequency counters.
- We process the stream character by character, incrementing the counter in $\mathcal{O}(1)$ space and $\mathcal{O}(N)$ streaming time. At the end of the stream, we perform the same greedy calculation.

#### 2. What if the keys have different base physical costs (e.g., thumb reach ergonomics)?
**Answer**:
- If each key $j \in [1, K]$ has an intrinsic cost $c_j$, the push cost for the $k$-th press on key $j$ becomes $k \times c_j$.
- Instead of simple integer division `idx // 8`, we can use a min-heap to dynamically pull the currently cheapest available key press slot, or precompute and sort the lowest available push costs across all keys.

#### 3. What if we are using an arbitrary alphabet with millions of unique characters (e.g., Unicode)?
**Answer**:
- When $|\Sigma|$ is large, sorting all $|\Sigma|$ frequencies takes $\mathcal{O}(|\Sigma| \log |\Sigma|)$.
- If we only need the top frequencies or if $|\Sigma|$ exceeds memory, we can use an external sort or a counting sort (if frequencies are bounded), or use Quickselect if we only need to group frequencies into buckets.
