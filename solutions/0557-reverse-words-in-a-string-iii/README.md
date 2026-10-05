# 0557. Reverse Words in a String III

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/reverse-words-in-a-string-iii/](https://leetcode.com/problems/reverse-words-in-a-string-iii/)  
**Topics:** Two Pointers, String

---

## 📝 Problem Statement

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 
Example 1:

```

**Input:** s = "Let's take LeetCode contest"
**Output:** "s'teL ekat edoCteeL tsetnoc"

```

Example 2:

```

**Input:** s = "Mr Ding"
**Output:** "rM gniD"

```

 
**Constraints:**

	- `1 4`

	- `s` contains printable **ASCII** characters.

	- `s` does not contain any leading or trailing spaces.

	- There is **at least one** word in `s`.

	- All the words in `s` are separated by a single space.

---

## 💻 Implementation (python3)

```py
class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by single space delimiter into individual words,
        # reverse each word using slicing, and join them back with spaces.
        return ' '.join(word[::-1] for word in s.split(' '))
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires reversing the characters of each word while maintaining the relative order of the words and preserving the spaces.

In Python, strings are immutable, meaning any modification requires constructing a new string or converting the string to a mutable sequence like a list of characters.

There are two primary paradigms:
1. **Pythonic / High-Level Approach**: 
   - Split the sentence into a list of words using the space character as a delimiter: `s.split(' ')`.
   - Reverse each word individually using slicing: `word[::-1]`.
   - Reconstruct the sentence using `' '.join(...)`.
   This is implemented in C under the hood in CPython, making it both optimal in Big-O and practically the fastest.

2. **In-Place Two-Pointer Simulation (Language-Agnostic)**:
   - Convert `s` to a list of characters: `chars = list(s)`.
   - Use two pointers (`start` and `end`) to identify the boundaries of each word.
   - When a space or end-of-string is encountered, reverse the characters in `chars[start:end]` in-place using two pointers.
   - Join the characters back into a string.

---

### Step-by-Step Approach (Split & Join)

1. Use `s.split(' ')` to break down the input string into a list of words.
2. Apply a generator expression `word[::-1] for word in ...` to reverse each word.
3. Join the reversed words using `' '.join(...)` to preserve the original single-space separation.

*(Note: If an interviewer asks to simulate true in-place behavior without helper methods like `split`, convert `s` to `list(s)`, iterate with an index `i`, locate each word's start and end, and swap characters from outer ends inward).*

---

### Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the length of string `s`.
  - Splitting the string takes $O(N)$ time.
  - Reversing all words collectively takes $O(N)$ time because each character is visited and reversed once.
  - Joining the words back into a single string takes $O(N)$ time.
  - Overall Time Complexity: $O(N)$.

- **Space Complexity:** $O(N)$ auxiliary space.
  - Due to Python string immutability, creating the list of words and the resulting string requires $O(N)$ extra memory.

---

### Common Pitfalls / Mistakes

1. **Reversing the Entire String vs. Individual Words:**
   - Candidate writes `s[::-1]`, which reverses the entire sentence including word order (e.g., `"Let's take"` becomes `"ekat s'teL"`).
2. **Handling Multiple or Irregular Spaces:**
   - `s.split()` collapses consecutive spaces, while `s.split(' ')` preserves empty strings representing multiple spaces. Given the constraint that words are separated by exactly one space with no leading/trailing spaces, `s.split(' ')` is safe and exact.
3. **Assuming In-Place String Mutation in Python:**
   - Forgetting that strings in Python cannot be modified in-place; attempting `s[i] = ...` causes a `TypeError`.

---

### Real Interview Follow-Up Questions

#### 1. What if the input string is a mutable character array (like in C++ or `char[]` in Java) and we want $O(1)$ extra space?
**Answer:**
We scan through the array with a pointer. Maintain a `start` pointer marking the beginning of the current word. When the scanning pointer hits a space or reaches the end of the array, reverse the subarray `arr[start...end - 1]` in-place using standard two-pointer swapping (`left`, `right`). Then advance `start` to `end + 1`.

#### 2. What if there are multiple consecutive spaces, leading spaces, or trailing spaces?
**Answer:**
If spaces must be preserved exactly as-is:
Use the two-pointer scan approach on character indices. Only reverse contiguous segments of non-space characters. All spaces remain untouched in their original positions.

#### 3. How would you handle a streaming input where the string cannot fit in memory?
**Answer:**
Read characters from the stream one by one into a small buffer until a space or EOF is encountered. Once a space is reached, output the buffer in reverse order, output the space, clear the buffer, and continue. This guarantees $O(\text{max\_word\_length})$ memory usage instead of $O(N)$.

#### 4. How does this handle Unicode characters (e.g., combining characters, surrogate pairs, grapheme clusters)?
**Answer:**
Standard byte- or character-level slicing (`[::-1]`) can break Unicode grapheme clusters (e.g., emojis or accented characters composed of a base letter + combining mark). To properly reverse words containing grapheme clusters, use a Unicode-aware library (such as Python's `regex` module with `\X` or `grapheme` library) to tokenize into graphemes before reversing.
