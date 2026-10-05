# 3794. Reverse String Prefix

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/reverse-string-prefix/](https://leetcode.com/problems/reverse-string-prefix/)  
**Topics:** Two Pointers, String

---

## 📝 Problem Statement

You are given a string `s` and an integer `k`.

Reverse the first `k` characters of `s` and return the resulting string.

 
Example 1:

**Input:** s = "abcd", k = 2

**Output:** "bacd"

**Explanation:**​​​​​​​

The first `k = 2` characters `"ab"` are reversed to `"ba"`. The final resulting string is `"bacd"`.

Example 2:

**Input:** s = "xyz", k = 3

**Output:** "zyx"

**Explanation:**

The first `k = 3` characters `"xyz"` are reversed to `"zyx"`. The final resulting string is `"zyx"`.

Example 3:

**Input:** s = "hey", k = 1

**Output:** "hey"

**Explanation:**

The first `k = 1` character `"h"` remains unchanged on reversal. The final resulting string is `"hey"`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # Reverse the prefix of length k, and append the remaining suffix unchanged
        return s[:k][::-1] + s[k:]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks to reverse the first $k$ characters of a given string $s$ while leaving the remaining suffix untouched.
In Python, strings are immutable, so any transformation produces a new string. We can leverage Python's slicing mechanics:
1. `s[:k]` extracts the prefix of length $k$.
2. `[::-1]` reverses that prefix in $O(k)$ time.
3. `s[k:]` extracts the remaining characters starting from index $k$ in $O(n - k)$ time.
4. Concatenating them produces the final result in $O(n)$ total time.

### Step-by-Step Approach
1. Slice the string from index $0$ to $k$ and reverse it using the step parameter `[::-1]`.
2. Slice the string from index $k$ to the end (`s[k:]`).
3. Concatenate both pieces and return the result.

### Complexity Analysis
- **Time Complexity:** $O(n)$, where $n$ is the length of `s`. Slicing and reversing the prefix takes $O(k)$, slicing the suffix takes $O(n - k)$, and concatenating them takes $O(n)$.
- **Space Complexity:** $O(n)$ auxiliary space to allocate and return the newly formed string of length $n$.

### Common Pitfalls / Mistakes Candidates Make
- **Off-by-one errors:** Forgetting that slice indexing is exclusive at the upper bound (e.g., slicing `s[:k-1]` instead of `s[:k]`).
- **Boundary checks:** Attempting manual indexing without checking if $k \ge n$ (Python slicing handles $k > n$ automatically, but in languages like C++ or Java, `std::min(k, n)` is required to prevent out-of-bounds exceptions).
- **Mutating strings in place:** Forgetting that strings in Python are immutable and trying to do `s[i], s[j] = s[j], s[i]`. If in-place modification is required, one must convert the string to a `list` first.

### Real Interview Follow-Up Questions

#### 1. What if the input string is very large (e.g., gigabytes) and cannot fit entirely in memory?
**Answer:** Treat the string as a stream or file. Read the first $k$ bytes into memory or a buffer, reverse them, and write them directly to the output stream. Then, stream the rest of the file in fixed-size chunks (e.g., 64KB) directly to the output without loading the whole file into memory.

#### 2. What if $s$ is mutable (like a character array `list[str]` or `char[]` in C++) and we must do this with $O(1)$ extra space?
**Answer:** Use the classic two-pointer technique:
Initialize `left = 0` and `right = k - 1`. While `left < right`, swap `s[left]` and `s[right]`, then increment `left` and decrement `right`. This runs in $O(k)$ time and uses $O(1)$ auxiliary space.

#### 3. What if $k$ can be larger than the length of $s$?
**Answer:** Python slicing automatically bounds the slice at `len(s)` if `k > len(s)`. In other languages, explicitly clamp $k$: `k = min(k, len(s))`.
