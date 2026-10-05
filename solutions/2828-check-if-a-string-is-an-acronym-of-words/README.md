# 2828. Check if a String Is an Acronym of Words

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/](https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/)  
**Topics:** Array, String

---

## 📝 Problem Statement

Given an array of strings `words` and a string `s`, determine if `s` is an **acronym** of words.

The string `s` is considered an acronym of `words` if it can be formed by concatenating the **first** character of each string in `words` **in order**. For example, `"ab"` can be formed from `["apple", "banana"]`, but it can't be formed from `["bear", "aardvark"]`.

Return `true`* if *`s`* is an acronym of *`words`*, and *`false`* otherwise. *

 
Example 1:

```

**Input:** words = ["alice","bob","charlie"], s = "abc"
**Output:** true
**Explanation:** The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym. 

```

Example 2:

```

**Input:** words = ["an","apple"], s = "a"
**Output:** false
**Explanation:** The first character in the words "an" and "apple" are 'a' and 'a', respectively. 
The acronym formed by concatenating these characters is "aa". 
Hence, s = "a" is not the acronym.

```

Example 3:

```

**Input:** words = ["never","gonna","give","up","on","you"], s = "ngguoy"
**Output:** true
**Explanation: **By concatenating the first character of the words in the array, we get the string "ngguoy". 
Hence, s = "ngguoy" is the acronym.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        # Fast exit: if lengths differ, s cannot be an acronym of words
        if len(words) != len(s):
            return False
        
        # Check if the first character of each word matches the corresponding character in s
        return all(word[0] == char for word, char in zip(words, s))
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
An acronym formed by `words` must have an exact one-to-one character correspondence with the first letter of each word in `words`.
1. **Length Invariant**: For `s` to be an acronym of `words`, the length of `s` must equal the number of elements in `words`. If `len(words) != len(s)`, we can immediately return `False` without inspecting any characters.
2. **Character Matching**: If the lengths match, iterate through both collections simultaneously using `zip` and verify that `word[0] == char` for each pair. Utilizing `all()` short-circuits on the first mismatch, providing optimal average-case runtime.

### Step-by-Step Approach
1. Compare `len(words)` with `len(s)`. Return `False` if they are not equal.
2. Iterate through pairs `(word, char)` from `zip(words, s)`.
3. Verify `word[0] == char`. If any pair does not match, return `False`.
4. If the loop completes without mismatches, return `True`.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ where $N = \min(\text{len}(words), \text{len}(s))$. In the worst case, we compare the first character of each word once. The length check runs in $\mathcal{O}(1)$ time.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space. The `zip` iterator and generator expression inside `all()` evaluate lazily without allocating intermediate lists or strings.

### Common Pitfalls / Mistakes Candidates Make
- **Unnecessary String Concatenation**: Constructing `''.join(w[0] for w in words) == s` allocates $\mathcal{O}(N)$ extra space and requires traversing all words even if the first character mismatches or lengths differ.
- **Missing the Length Check**: Failing to check lengths up front can lead to either index out-of-range errors or having to traverse the entire list when a fast-fail check was possible.
- **Index Out of Bounds on Empty Words**: While constraints guarantee `1 <= words[i].length`, in production code, always consider empty strings (`word and word[0] == char`).

### Real Interview Follow-Up Questions

#### 1. What if `words` is an unbounded or infinite stream?
- **Answer**: You cannot perform `len(words)` up front. Instead, iterate through `s` and the stream concurrently using `itertools.zip_longest`:
  ```python
  from itertools import zip_longest

  sentinel = object()
  for word, char in zip_longest(words_stream, s, fillvalue=sentinel):
      if word is sentinel or char is sentinel or not word or word[0] != char:
          return False
  return True
  ```
  This guarantees early exit on the first mismatch or when either stream terminates prematurely.

#### 2. What if strings contain multi-byte Unicode characters / grapheme clusters (e.g., emojis, combining marks)?
- **Answer**: Standard indexing `word[0]` extracts the first UTF-8 code point, which can break combining characters (e.g., `"e\u0301"` for `é`). In Python, the `unicodedata` module (specifically `unicodedata.normalize('NFC', word)`) or the third-party `regex` module with grapheme cluster matching (`\X`) should be used to extract the true user-perceived first character.
