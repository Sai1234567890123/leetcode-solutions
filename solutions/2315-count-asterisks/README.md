# 2315. Count Asterisks

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-asterisks/](https://leetcode.com/problems/count-asterisks/)  
**Topics:** String

---

## 📝 Problem Statement

You are given a string `s`, where every **two** consecutive vertical bars `'|'` are grouped into a **pair**. In other words, the 1st and 2nd `'|'` make a pair, the 3rd and 4th `'|'` make a pair, and so forth.

Return *the number of *`'*'`* in *`s`*, **excluding** the *`'*'`* between each pair of *`'|'`.

**Note** that each `'|'` will belong to **exactly** one pair.

 
Example 1:

```

**Input:** s = "l|*e*et|c**o|*de|"
**Output:** 2
**Explanation:** The considered characters are underlined: "l|*e*et|c**o|*de|".
The characters between the first and second '|' are excluded from the answer.
Also, the characters between the third and fourth '|' are excluded from the answer.
There are 2 asterisks considered. Therefore, we return 2.
```

Example 2:

```

**Input:** s = "iamprogrammer"
**Output:** 0
**Explanation:** In this example, there are no asterisks in s. Therefore, we return 0.

```

Example 3:

```

**Input:** s = "yo|uar|e**|b|e***au|tifu|l"
**Output:** 5
**Explanation:** The considered characters are underlined: "yo|uar|e**|b|e***au|tifu|l". There are 5 asterisks considered. Therefore, we return 5.
```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def countAsterisks(self, s: str) -> int:
        asterisk_count = 0
        inside_pair = False

        for char in s:
            if char == '|':
                # Toggle state: entering or exiting a pair of '|'
                inside_pair = not inside_pair
            elif char == '*' and not inside_pair:
                # Count asterisks only when outside any '|' pair
                asterisk_count += 1

        return asterisk_count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires counting `'*'` characters in a string while ignoring any asterisks that fall inside a pair of vertical bars (`'|'`).
Because vertical bars are guaranteed to appear in matched pairs (1st with 2nd, 3rd with 4th, etc.), this can be modeled as a simple **finite state machine (FSM)** with two states:
1. `OUTSIDE_PAIR` (initial state)
2. `INSIDE_PAIR`

Every time we encounter a `'|'`, we toggle our state:
- If we are `OUTSIDE_PAIR`, encountering `'|'` transitions us into `INSIDE_PAIR`.
- If we are `INSIDE_PAIR`, encountering `'|'` transitions us back into `OUTSIDE_PAIR`.

When we encounter `'*'`, we only increment our counter if we are currently in the `OUTSIDE_PAIR` state.

---

### Step-by-Step Approach

1. Initialize `asterisk_count = 0` to store the total valid asterisks.
2. Initialize a boolean flag `inside_pair = False`.
3. Iterate through each character `char` in the string `s`:
   - If `char == '|'`, flip `inside_pair` (`inside_pair = not inside_pair`).
   - If `char == '*'` and `inside_pair` is `False`, increment `asterisk_count` by 1.
4. Return `asterisk_count`.

---

### Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the length of string `s`. We perform a single pass over the string with $O(1)$ work per character.
- **Space Complexity:** $O(1)$ auxiliary space. We only use two variables: an integer counter and a boolean flag.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Using `.split('|')` carelessly:**
   A common Pythonic one-liner is `sum(part.count('*') for part in s.split('|')[::2])`. While functionally correct and $O(N)$ time, it creates multiple intermediate substrings and a list of size $O(N)$, violating the $O(1)$ auxiliary space requirement.
2. **Off-by-one errors with pair indices:**
   Tracking indices of `'|'` or using regex can introduce unnecessary complexity and potential indexing bugs. A simple boolean toggle is cleaner and less error-prone.
3. **Assuming odd counts of `'|'`:**
   The problem constraints guarantee that each `'|'` belongs to exactly one pair (i.e., total count of `'|'` is always even). If an interviewer relaxes this constraint, error handling or explicit state recovery would be required.

---

### Real Interview Follow-Up Questions

#### 1. What if the input stream is massive (e.g., gigabytes/terabytes) and cannot fit into memory?
**Answer:** The current approach processes the input character-by-character (or chunk-by-chunk). We can stream the input line by line or in fixed-size buffers (e.g., 4KB / 64KB) while maintaining `inside_pair` and `asterisk_count` across chunks. Memory usage remains $O(1)$.

#### 2. How would you parallelize this across multiple cores / MapReduce?
**Answer:**
We can partition the text into chunks:
- For each chunk, compute:
  1. Total number of `'|'` in the chunk.
  2. Number of `'*'` outside pairs *assuming the chunk started outside a pair*.
  3. Number of `'*'` outside pairs *assuming the chunk started inside a pair*.
- In a reduction step (prefix sum / scan):
  - Determine whether the start of chunk $i$ is inside or outside a pair based on the parity of total `'|'` in chunks $0 \dots i-1$.
  - Pick the precomputed asterisk count for each chunk based on its starting state and sum them up.

#### 3. What if there are escape sequences (e.g., `\|` or `\\*`)?
**Answer:** Introduce an `escaped` boolean flag. If the preceding character was an unescaped backslash `\`, treat the current character as a literal character rather than a delimiter/target.
