# 0709. To Lower Case

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/to-lower-case/](https://leetcode.com/problems/to-lower-case/)  
**Topics:** String

---

## 📝 Problem Statement

Given a string `s`, return *the string after replacing every uppercase letter with the same lowercase letter*.

 
Example 1:

```

**Input:** s = "Hello"
**Output:** "hello"

```

Example 2:

```

**Input:** s = "here"
**Output:** "here"

```

Example 3:

```

**Input:** s = "LOVELY"
**Output:** "lovely"

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        Converts uppercase ASCII letters in a string to lowercase 
        without relying on built-in conversion functions like s.lower().
        """
        result = []
        for char in s:
            # Check if the character is an uppercase ASCII letter ('A' to 'Z')
            if 'A' <= char <= 'Z':
                # In ASCII, the difference between lowercase and uppercase is 32.
                # Alternatively, bitwise OR with 32 (0b00100000) sets the 6th bit.
                result.append(chr(ord(char) | 32))
            else:
                result.append(char)
                
        return "".join(result)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The trivial approach in Python is calling `return s.lower()`. However, in a technical interview, this problem is specifically used to assess:
1. Understanding of character encodings (ASCII / Unicode).
2. Bitwise operations and arithmetic on character codes.
3. String mutability/immutability and memory management.

In the ASCII table:
- `'A'` is `65` (`0b01000001`) and `'Z'` is `90` (`0b01011010`).
- `'a'` is `97` (`0b01100001`) and `'z'` is `122` (`0b01110010`).

The difference between every uppercase letter and its corresponding lowercase letter is exactly $32$ ($2^5$). Setting the 6th bit (0-indexed bit 5) of an uppercase ASCII character turns it into its lowercase equivalent:
$$\text{ord}(c) \mid 32 = \text{ord}(c) + 32$$

Any character outside the `'A'` to `'Z'` range (e.g., punctuation, numbers, already lowercase characters) should remain unchanged.

### Step-by-Step Approach

1. Initialize a list `result` to collect transformed characters (avoiding $O(N^2)$ string concatenation in languages with immutable strings like Python).
2. Iterate through each character in string `s`.
3. Check if `'A' <= char <= 'Z'`.
   - If yes: append `chr(ord(char) | 32)`.
   - If no: append `char` directly.
4. Join the list into a single string using `"".join(result)` and return it.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of string `s`. We iterate through the string of length $N$ once, performing constant $\mathcal{O}(1)$ operations per character, and the final join operation takes $\mathcal{O}(N)$ time.
- **Space Complexity:** $\mathcal{O}(N)$ auxiliary space to store the output string/list, which is optimal since strings are immutable in Python. If modifying in-place in languages like C/C++ where strings are mutable `char` arrays, auxiliary space would be $\mathcal{O}(1)$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Repeated String Concatenation:** Writing `res += char` inside a loop in Python creates a new string object on each iteration, degrading time complexity to $\mathcal{O}(N^2)$ in worst cases.
2. **Missing Boundary Checks:** Applying `+ 32` or `| 32` indiscriminately to all characters. For example, `'@' | 32` becomes `'`' and `'1' | 32` becomes `'1'`, which corrupts non-alphabetic characters.
3. **Overlooking Locale / Unicode:** Assuming all alphabets behave like standard ASCII (e.g., the German letter `ß` has uppercase `SS`, or Turkish dotted/dotless `I`/`i`). Mentioning this to the interviewer demonstrates senior-level awareness.

---

### Real Interview Follow-Up Questions

#### 1. How would you handle UTF-8 / full Unicode characters?
**Answer:** The simple $+32$ offset only works for the ASCII range (`U+0041` to `U+005A`). Full Unicode requires handling complex casing rules, titlecase, multi-byte characters, and non-1:1 mappings (e.g., Greek sigma $\Sigma \to \sigma$ or $\varsigma$). In production, use Unicode standard lookup tables (e.g., Python's internal `unicodedata` or `str.lower()`).

#### 2. How would you process a massive text file (e.g., 50GB) that doesn't fit in memory?
**Answer:** Stream the file in chunks (e.g., 64KB or 1MB buffers). Transform each buffer in memory using SIMD/vectorized instructions (like AVX-512 vector bitwise OR for ASCII) and write directly to an output stream without loading the entire file into RAM.

#### 3. How can this be optimized using SIMD / parallelism?
**Answer:** In systems programming (C++/Rust), you can load 16, 32, or 64 characters into vector registers (e.g., AVX2 / AVX-512). Use vector range comparison to identify bytes between `65` and `90`, generate a mask, and selectively apply `| 0x20` to only those bytes in parallel, processing dozens of characters per CPU cycle.
