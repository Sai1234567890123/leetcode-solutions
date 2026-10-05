# 2000. Reverse Prefix of Word

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/reverse-prefix-of-word/](https://leetcode.com/problems/reverse-prefix-of-word/)  
**Topics:** Two Pointers, String, Stack

---

## 📝 Problem Statement

Given a **0-indexed** string `word` and a character `ch`, **reverse** the segment of `word` that starts at index `0` and ends at the index of the **first occurrence** of `ch` (**inclusive**). If the character `ch` does not exist in `word`, do nothing.

	- For example, if `word = "abcdefd"` and `ch = "d"`, then you should **reverse** the segment that starts at `0` and ends at `3` (**inclusive**). The resulting string will be `"dcbaefd"`.

Return *the resulting string*.

 
Example 1:

```

**Input:** word = "abcdefd", ch = "d"
**Output:** "dcbaefd"
**Explanation:** The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

```

Example 2:

```

**Input:** word = "xyxzxe", ch = "z"
**Output:** "zxyxxe"
**Explanation:** The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

```

Example 3:

```

**Input:** word = "abcd", ch = "z"
**Output:** "abcd"
**Explanation:** "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the first occurrence of ch
        idx = word.find(ch)
        
        # If ch is not found, return the original word unchanged
        if idx == -1:
            return word
            
        # Reverse the prefix from index 0 to idx (inclusive), then append the remainder
        return word[:idx + 1][::-1] + word[idx + 1:]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks us to reverse the segment of `word` from index `0` up to the first occurrence of `ch` (inclusive). If `ch` is not in `word`, we leave it unchanged.

1. **Locate the Target Character**: The built-in `word.find(ch)` scans the string from left to right and returns the index of the *first* occurrence in $O(n)$ time, or `-1` if it is not present.
2. **Handle Non-existence**: If `find` returns `-1`, we immediately return `word`.
3. **Prefix Reversal**: If the character exists at index `idx`, the prefix to reverse is `word[:idx + 1]`. Slicing with `[::-1]` produces the reversed prefix. The unreversed suffix is `word[idx + 1:]`. Concatenating these two pieces gives the final result.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$, where $n$ is the length of `word`.
  - Finding the index takes $\mathcal{O}(n)$ in the worst case.
  - Slicing and reversing the prefix takes $\mathcal{O}(idx) \le \mathcal{O}(n)$ time.
  - Constructing the final string takes $\mathcal{O}(n)$ time.
  - Overall time complexity is strictly linear.
- **Space Complexity**: $\mathcal{O}(n)$. Strings in Python are immutable, so constructing the result requires $\mathcal{O}(n)$ auxiliary space to allocate the new string. No additional memory beyond the output string is used.

### Common Pitfalls / Mistakes Candidates Make
1. **Using `word.rfind(ch)` instead of `word.find(ch)`**: The problem specifies the *first* occurrence, not the last.
2. **Off-by-one errors**: Forgetting that Python slices `word[:idx]` exclude the element at `idx`. To include `ch`, the slice must be `word[:idx + 1]`.
3. **Handling missing character**: Forgetting to check if `ch` exists, which causes an exception if using `word.index(ch)` without a `try-except` block. `word.find(ch)` safely returns `-1`.

### Real Interview Follow-Up Questions

#### 1. In-Place Reversal (Memory Constraints / Mutable Strings)
* **Question**: What if the input is a mutable character array (`list[str]`) and you must do this in $\mathcal{O}(1)$ auxiliary space?
* **Answer**: We find the index of `ch`, then use a two-pointer approach (`left = 0`, `right = idx`) swapping characters `arr[left], arr[right] = arr[right], arr[left]` and moving inward until `left >= right`.

#### 2. Streaming Data
* **Question**: What if characters arrive one by one as a stream, and we don't know when/if `ch` will arrive?
* **Answer**: Buffer incoming characters into an array until `ch` is observed. Once `ch` arrives, reverse the buffered array, emit all buffered characters, and thereafter stream subsequent characters directly without buffering. If the stream ends without `ch`, emit the buffer in its original order.

#### 3. Large Files / Out-of-Memory String
* **Question**: Suppose `word` is a 100 GB string stored on disk. How would you reverse the prefix?
* **Answer**: Stream chunks from disk until `ch` is located at byte offset $K$. The prefix is of size $K$. Read the prefix backward in reverse chunk blocks (from chunk containing byte $K$ down to 0) to write to the output destination, and then stream the remaining file sequentially. Memory usage remains bounded by chunk size $\mathcal{O}(B)$.
