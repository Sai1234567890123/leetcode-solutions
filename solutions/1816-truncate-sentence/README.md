# 1816. Truncate Sentence

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/truncate-sentence/](https://leetcode.com/problems/truncate-sentence/)  
**Topics:** Array, String

---

## 📝 Problem Statement

A **sentence** is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of **only** uppercase and lowercase English letters (no punctuation).

	- For example, `"Hello World"`, `"HELLO"`, and `"hello world hello world"` are all sentences.

You are given a sentence `s`​​​​​​ and an integer `k`​​​​​​. You want to **truncate** `s`​​​​​​ such that it contains only the **first** `k`​​​​​​ words. Return `s`​​​​*​​ after **truncating** it.*

 
Example 1:

```

**Input:** s = "Hello how are you Contestant", k = 4
**Output:** "Hello how are you"
**Explanation:**
The words in s are ["Hello", "how", "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".

```

Example 2:

```

**Input:** s = "What is the solution to this problem", k = 4
**Output:** "What is the solution"
**Explanation:**
The words in s are ["What", "is", "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".
```

Example 3:

```

**Input:** s = "chopper is not a tanuki", k = 5
**Output:** "chopper is not a tanuki"

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Truncates the sentence to only the first k words.
        
        Since words are separated by exactly one space, the k-th word ends
        immediately before the k-th space character.
        """
        space_count = 0
        for i, char in enumerate(s):
            if char == ' ':
                space_count += 1
                # When we reach the k-th space, the first k words have ended
                if space_count == k:
                    return s[:i]
        
        # If the string contains fewer than or exactly k spaces, return s
        return s
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A naive approach would be to split the sentence using `s.split()`, take the first `k` elements, and join them back with `" ".join(...)`. While functionally correct, splitting creates an array of substrings for the entire sentence, allocating unnecessary memory for words beyond the $k$-th word.

Because the problem guarantees:
1. Words are separated by a **single** space.
2. There are **no leading or trailing** spaces.

Every space character directly signifies the end of a word. Therefore, the first $k$ words are terminated by the $k$-th space. By iterating through the string and counting space characters, we can immediately return the prefix `s[:i]` when the $k$-th space is encountered. If no $k$-th space is found (meaning the sentence has exactly $k$ words), we simply return the entire string `s`.

### Step-by-Step Approach

1. Initialize a counter `space_count = 0`.
2. Iterate through each character and its index `i` in the string `s`.
3. Whenever a space character `' '` is encountered:
   - Increment `space_count`.
   - If `space_count == k`, return the slice `s[:i]`.
4. If the loop completes without finding `k` spaces, it means the sentence has exactly $k$ words (as per the constraint $1 \le k \le \text{number of words}$), so return `s`.

### Complexity Analysis

- **Time Complexity:** $O(N)$ where $N$ is the length of string `s`. In the worst case (e.g., $k$ equals the total word count), we scan the string once. Slicing the string `s[:i]` takes $O(L)$ where $L \le N$. Thus, overall time complexity is strictly linear $O(N)$.
- **Space Complexity:** $O(1)$ auxiliary space. Unlike `split()` which allocates $O(N)$ additional memory for intermediate word arrays, this approach only maintains an integer counter. The returned substring of length $\le N$ is required for the output.

### Common Pitfalls / Mistakes candidates make in interviews

1. **Over-allocating with `split()` and `join()`:** While concise in Python (`" ".join(s.split()[:k])`), it shows a lack of awareness of memory overhead and object allocation, which interviewers at top-tier companies notice.
2. **Off-by-one errors with spaces:** Thinking the $k$-th word needs $k$ spaces. The $k$-th word is preceded by $k - 1$ spaces and followed by the $k$-th space. Counting to $k$ identifies the boundary correctly.
3. **Handling the boundary condition where $k == \text{total words}$:** If candidates assume there will always be a $k$-th space, they may hit an index out of bounds or fail to return the full string when $k$ equals the number of words.

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input has arbitrary, consecutive whitespace characters and leading/trailing spaces?
*Answer:* A simple single-space count will fail. We can track state transitions (whether we are currently inside a word or in whitespace). We increment the word count only when transitioning from whitespace to a non-whitespace character. Once the word count exceeds $k$, the truncation point is right before the current word started (or right after the $k$-th word ended).

#### 2. How would you handle a streaming input where the sentence is extremely large (e.g., gigabytes) or comes from an infinite network stream?
*Answer:* We read chunks from the stream character by character (or in buffered blocks). We stream each character directly to the output buffer/stream until we count $k$ spaces, at which point we terminate reading and close the output stream. This achieves $O(1)$ memory usage.

#### 3. What if $s$ is mutable (e.g., a character array `List[str]` in Python or `char[]` in C++) and we must perform the operation in-place with $O(1)$ space?
*Answer:* We locate the index of the $k$-th space and truncate in-place (in C/C++, by placing a null terminator `'\0'` at that index; in Python, `del s[i:]`). No new string or array is allocated.
