# 1859. Sorting the Sentence

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/sorting-the-sentence/](https://leetcode.com/problems/sorting-the-sentence/)  
**Topics:** String, Sorting, Bubble Sort

---

## 📝 Problem Statement

A **sentence** is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be **shuffled** by appending the **1-indexed word position** to each word then rearranging the words in the sentence.

	- For example, the sentence `"This is a sentence"` can be shuffled as `"sentence4 a3 is2 This1"` or `"is2 sentence4 This1 a3"`.

Given a **shuffled sentence** `s` containing no more than `9` words, reconstruct and return *the original sentence*.

 
Example 1:

```

**Input:** s = "is2 sentence4 This1 a3"
**Output:** "This is a sentence"
**Explanation:** Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

```

Example 2:

```

**Input:** s = "Myself2 Me1 I4 and3"
**Output:** "Me Myself and I"
**Explanation:** Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.

```

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def sortSentence(self, s: str) -> str:
        # Split the shuffled sentence into individual word-number tokens
        words = s.split()
        
        # Preallocate a list to place words directly into their correct 0-indexed positions
        n = len(words)
        reconstructed = [None] * n
        
        for word in words:
            # The last character represents the 1-indexed position
            pos = int(word[-1]) - 1
            # The actual word content excludes the trailing numeric digit
            reconstructed[pos] = word[:-1]
            
        # Join the sorted words with single spaces
        return " ".join(reconstructed)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to place words back into their original 1-indexed order. Each word in the input string has its original position appended as its last character. Because the problem statement guarantees there are at most 9 words, each index is a single digit (`'1'` through `'9'`).

Instead of sorting the words using a generic comparison-based sorting algorithm ($O(K \log K)$, where $K$ is the number of words), we can use a **bucket/direct-placement approach** running in $O(N)$ time, where $N$ is the total length of the string:
1. Break the input into individual tokens.
2. Direct index access: each token's position is explicitly given by its last character.
3. Strip the index digit and insert the word directly into a preallocated array at `int(word[-1]) - 1`.
4. Join the sorted tokens with a single space.

### Step-by-Step Approach

1. **Tokenize:** Use `s.split()` to split the sentence by spaces into an array of words.
2. **Preallocate:** Allocate an array `reconstructed` of length equal to the number of words.
3. **Scatter / Place:** Iterate through each word:
   - Extract the position index: `pos = int(word[-1]) - 1`.
   - Extract the word slice: `word[:-1]`.
   - Assign: `reconstructed[pos] = word[:-1]`.
4. **Join:** Use `" ".join(reconstructed)` to produce the reconstructed sentence.

### Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the total number of characters in the input string `s`.
  - Splitting the string takes $O(N)$ time.
  - Slicing and placing each word into the array takes $O(N)$ overall across all words.
  - Joining the reconstructed array takes $O(N)$ time.
  - Note: Using direct placement gives $O(N)$ compared to $O(N + K \log K)$ with `sort(key=...)`.
- **Space Complexity:** $O(N)$ to store the split words, the result array, and the final output string.

### Common Pitfalls / Mistakes

1. **1-based vs 0-based Indexing:** Forgetting to subtract `1` from the digit (`int(word[-1]) - 1`) leading to an `IndexError`.
2. **Double-digit positions (Assumption Risk):** While this problem specifies $\le 9$ words, in real interviews, the interviewer might remove this constraint. Parsing only `word[-1]` will fail if positions can be $\ge 10$ (e.g., `"word10"`). Always clarify the bounds or use regex/trailing digit parsing.
3. **Inefficient String Concatenation:** Concatenating strings repeatedly in a loop using `+` in languages like Java or Python can lead to $O(N^2)$ behavior due to string immutability. Using a list and `.join()` avoids this.

### Real Interview Follow-Up Questions

#### 1. What if the sentence can contain more than 9 words (e.g., up to $10^5$ words)?
- **Answer:** The position can span multiple digits at the end of the word. We should iterate backwards from the end of the token while characters are digits (`isdigit()`), slice the number, convert it to an integer, and take the rest of the string as the word:
  ```python
  i = len(word) - 1
  while i >= 0 and word[i].isdigit():
      i -= 1
  pos = int(word[i + 1:]) - 1
  actual_word = word[:i + 1]
  ```

#### 2. Can we do this in $O(1)$ auxiliary space?
- **Answer:** In languages with mutable strings (like C++ `std::string` or a `char[]`), yes. We can do cycle-sort in-place or swap tokens in-place, then remove the digits and shift characters in $O(N)$ time and $O(1)$ auxiliary space. In Python, strings are immutable, so $O(N)$ space is required to construct the output.

#### 3. What if the input is a continuous stream of words arriving out-of-order?
- **Answer:** If words arrive as a stream, we can use a hash map or preallocated fixed-size buffer to store incoming words at their respective indices. If the goal is to emit the sentence once complete, we track the total expected count (or detect the maximum index seen and verify all indices from $1$ to $K$ are filled) and yield the result.
