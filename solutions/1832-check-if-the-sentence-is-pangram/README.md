# 1832. Check if the Sentence Is Pangram

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/check-if-the-sentence-is-pangram/](https://leetcode.com/problems/check-if-the-sentence-is-pangram/)  
**Topics:** Hash Table, String

---

## 📝 Problem Statement

A **pangram** is a sentence where every letter of the English alphabet appears at least once.

Given a string `sentence` containing only lowercase English letters, return* *`true`* if *`sentence`* is a **pangram**, or *`false`* otherwise.*

 
Example 1:

```

**Input:** sentence = "thequickbrownfoxjumpsoverthelazydog"
**Output:** true
**Explanation:** sentence contains at least one of every letter of the English alphabet.

```

Example 2:

```

**Input:** sentence = "leetcode"
**Output:** false

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # A pangram must contain at least 26 characters.
        if len(sentence) < 26:
            return False

        # Bitmask to track seen characters ('a' -> bit 0, 'z' -> bit 25).
        # Target mask has all first 26 bits set: (1 << 26) - 1.
        seen_mask = 0
        target_mask = (1 << 26) - 1

        for char in sentence:
            # Map 'a'..'z' to 0..25 and set the corresponding bit
            seen_mask |= 1 << (ord(char) - ord('a'))
            
            # Early exit: if all 26 letters have been encountered, terminate early
            if seen_mask == target_mask:
                return True

        return seen_mask == target_mask
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A pangram is defined as a sentence that contains every letter of the English alphabet at least once. Since there are 26 letters in the English alphabet:
1. **Early Length Check:** If `len(sentence) < 26`, it is impossible to be a pangram. We can immediately return `False`.
2. **State Representation:** We only need to track the presence of 26 distinct lowercase letters. While a hash set or boolean array works, a **bitmask** represents this tracking in a single 32-bit integer.
3. **Early Exit Optimization:** As soon as all 26 distinct letters are recorded (i.e., `seen_mask == (1 << 26) - 1`), we can terminate early without processing the rest of the string.

### Step-by-Step Approach

1. **Check Base Constraint:** If the length of the string is less than 26, return `False`.
2. **Initialize Bitmask:** Create an integer `seen_mask = 0`. Define `target_mask = (1 << 26) - 1` (a bitmask where the first 26 bits are `1`).
3. **Iterate & Update:**
   - Iterate through each character `char` in `sentence`.
   - Compute bit offset: `ord(char) - ord('a')`.
   - Set the corresponding bit: `seen_mask |= (1 << offset)`.
   - Check if `seen_mask == target_mask`. If so, return `True` immediately.
4. **Final Return:** If loop completes without early termination, check if `seen_mask == target_mask`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ worst-case, where $N$ is the length of `sentence`. 
  - In the best/average case with an early exit, it runs in $\mathcal{O}(K)$ where $K$ is the index where the 26th unique character is found ($26 \le K \le N$).
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.
  - A single integer bitmask uses $O(1)$ memory, unlike a hash set which allocates heap memory.

---

### Common Pitfalls / Mistakes

1. **Using `len(set(sentence)) == 26` without early exit or pre-check:** While Pythonic and clean for competitive programming, computing `set(sentence)` always reads the entire string into memory and constructs a full set, missing the opportunity to return early once 26 unique characters are observed or if `len(sentence) < 26`.
2. **Forgetting Case Sensitivity / Non-alphabet characters:** In general interview contexts, always clarify if input contains uppercase characters, punctuation, spaces, or numbers. If so, filtering or normalization (`char.lower()`) is required.

---

### Real Interview Follow-Up Questions

#### 1. What if the input is an infinite or massive data stream (e.g., streaming logs)?
- **Answer:** The bitmask approach directly supports streaming. Read characters one-by-one from the stream, update the bitmask, and terminate the connection/stream processing as soon as `seen_mask == target_mask`. We never store the stream in memory.

#### 2. What if the alphabet size is very large (e.g., full Unicode / UTF-8)?
- **Answer:** A 32-bit bitmask won't suffice for Unicode.
  - If tracking a sparse set of thousands of required symbols: use a `HashSet` or a bitset / `BitArray`.
  - Maintain a count of remaining required characters decrementing towards zero to keep checking $\mathcal{O}(1)$.

#### 3. How would you optimize this for multi-core processing or very long strings (e.g., gigabytes of text)?
- **Answer:** Split the text into chunks across threads. Each thread computes a local 32-bit integer mask for its chunk. The final result is the bitwise OR of all thread masks: `final_mask = mask_1 | mask_2 | ... | mask_k`. If `final_mask == target_mask`, it's a pangram. This achieves linear speedup with zero lock contention.
