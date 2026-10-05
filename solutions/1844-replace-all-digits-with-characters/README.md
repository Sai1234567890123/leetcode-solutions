# 1844. Replace All Digits with Characters

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/replace-all-digits-with-characters/](https://leetcode.com/problems/replace-all-digits-with-characters/)  
**Topics:** String

---

## 📝 Problem Statement

You are given a **0-indexed** string `s` that has lowercase English letters in its **even** indices and digits in its **odd** indices.

You must perform an operation `shift(c, x)`, where `c` is a character and `x` is a digit, that returns the `xth` character after `c`.

	- For example, `shift('a', 5) = 'f'` and `shift('x', 0) = 'x'`.

For every **odd** index `i`, you want to replace the digit `s[i]` with the result of the `shift(s[i-1], s[i])` operation.

Return `s`* *after replacing all digits. It is **guaranteed** that* *`shift(s[i-1], s[i])`* *will never exceed* *`'z'`.

**Note** that `shift(c, x)` is **not** a preloaded function, but an operation *to be implemented* as part of the solution.

 
Example 1:

```

**Input:** s = "a1c1e1"
**Output:** "abcdef"
**Explanation: **The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
```

Example 2:

```

**Input:** s = "a1b2c3d4e"
**Output:** "abbdcfdhe"
**Explanation: **The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def replaceDigits(self, s: str) -> str:
        # Convert string to a mutable list of characters
        res = list(s)
        
        # Iterate over all odd indices
        for i in range(1, len(res), 2):
            # Shift the preceding character by the digit value at the current index
            res[i] = chr(ord(res[i - 1]) + int(res[i]))
            
        return "".join(res)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires us to transform a string where even-indexed characters are lowercase English letters and odd-indexed characters are numeric digits representing shift offsets. For each odd index `i`, we need to shift the character at `i - 1` forward in the alphabet by `s[i]` positions.

In Python:
1. Strings are immutable, so we cannot mutate `s` directly in-place. Converting `s` into a list of characters allows $O(1)$ in-place modifications.
2. The ASCII value of a character can be retrieved using `ord()`, and converted back to a character using `chr()`.
3. To compute `shift(c, x)`, we can use `chr(ord(c) + int(x))`.
4. We step through indices `1, 3, 5, ...` up to `len(s) - 1`, replace each digit, and finally join the list into a string.

### Step-by-Step Approach

1. Convert `s` to a list of individual characters, `res = list(s)`.
2. Iterate through the odd indices `range(1, len(res), 2)`.
3. For each index `i`:
   - Compute the new character: `chr(ord(res[i - 1]) + int(res[i]))`.
   - Update `res[i]` with this new character.
4. Join `res` back into a string and return it.

### Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the length of string `s`.
  - Converting the string to a list takes $O(N)$ time.
  - The loop runs $N / 2$ times, each performing $O(1)$ operations (integer conversion, `ord`, `chr`, and list assignment).
  - Joining the list takes $O(N)$ time.
  - Overall time complexity is linear: $O(N)$.

- **Space Complexity:** $O(N)$ auxiliary space.
  - Python strings are immutable, so creating a mutable list of characters requires $O(N)$ space.
  - If the language allowed mutable strings (e.g., in-place `std::string` in C++), auxiliary space would be $O(1)$.

### Common Pitfalls / Mistakes

- **String Concatenation in a Loop:** Using `s += ...` in a loop results in $O(N^2)$ time complexity due to repeated memory allocations and copies. Always build a list and use `''.join(...)` or modify a list in-place.
- **Off-by-One / Loop Bound Errors:** Ensure the loop starts at index `1` and steps by `2`. Single-character inputs (`len(s) == 1`) should not enter the loop and should return as-is.
- **Forgetting Character Type Conversion:** Attempting `ord(res[i])` instead of `int(res[i])` would add the ASCII value of the digit (e.g., `'1'` has ASCII 49) rather than its numerical value.

### Real Interview Follow-Up Questions

1. **What if the shift causes the character to wrap around past `'z'`?**
   - *Answer:* If wrap-around is allowed, we can use modulo arithmetic relative to `'a'`:
     `chr(ord('a') + (ord(res[i - 1]) - ord('a') + int(res[i])) % 26)`.
2. **How would you handle a streaming input (e.g., reading from a large file or network socket)?**
   - *Answer:* We can maintain a small buffer of size 2 (or process pairs as they arrive). Read the letter, yield or write it immediately, then read the digit, apply the shift using the stored letter, and yield/write the shifted character. This requires $O(1)$ auxiliary memory.
3. **What if the digits can be multi-digit numbers (e.g., `a12b3`)?**
   - *Answer:* We would use a two-pointer or tokenizer approach: parse the character, then parse all consecutive digit characters into an integer, shift the character accordingly, and repeat.
