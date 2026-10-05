# 1108. Defanging an IP Address

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/defanging-an-ip-address/](https://leetcode.com/problems/defanging-an-ip-address/)  
**Topics:** String

---

## 📝 Problem Statement

Given a valid (IPv4) IP `address`, return a defanged version of that IP address.

A *defanged IP address* replaces every period `"."` with `"[.]"`.

 
Example 1:
```
**Input:** address = "1.1.1.1"
**Output:** "1[.]1[.]1[.]1"

```Example 2:
```
**Input:** address = "255.100.50.0"
**Output:** "255[.]100[.]50[.]0"

```
 
**Constraints:**


	- The given `address` is a valid IPv4 address.

---

## 💻 Implementation (python3)

```py
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # The problem requires replacing every period "." in the IP address with "[.]".
        # Python's built-in string `replace()` method is the most straightforward,
        # efficient, and Pythonic way to achieve this.
        # It takes two arguments: the substring to find, and the substring to replace it with.
        # It returns a new string with all occurrences of the old substring replaced.
        return address.replace(".", "[.]")
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to take a given IPv4 `address` string and replace every occurrence of a period `.` with `[.]`. This is a classic string manipulation task.

My thought process for solving this problem goes as follows:

1.  **Understand the Core Task**: The fundamental operation is a "find and replace" on a string. We need to locate all instances of `.` and substitute them with `[.]`.

2.  **Consider Python's String Capabilities**: Python strings are powerful and come with many built-in methods for manipulation.
    *   **`str.replace()`**: This method is specifically designed for replacing occurrences of a substring with another substring. It's highly optimized as it's implemented in C.
    *   **Iterate and Build**: We could iterate through the input string character by character. If the character is a `.` we append `[.]` to a list of parts; otherwise, we append the character itself. Finally, we join the list of parts into a new string.
    *   **`str.split()` and `str.join()`**: We could split the string by the `.` delimiter, which would give us a list of the numerical parts of the IP address. Then, we can join these parts back together using `[.]` as the new delimiter.

3.  **Choose the Most Optimal/Pythonic Approach**:
    *   `str.replace()` is the most direct, concise, and idiomatic Python solution for this specific problem. It clearly expresses the intent and is typically the most performant for simple replacements due to its C implementation.
    *   The "iterate and build" approach is more verbose and involves more steps (list appends, then a final join), which might introduce slight overhead compared to `replace()`.
    *   The `split()` and `join()` approach is also very good and Pythonic. For this problem, it's conceptually similar to `replace()` in terms of efficiency.

Given the simplicity of the replacement, `str.replace()` is the clear winner for its elegance and efficiency.

## Step-by-Step Approach

1.  The function `defangIPaddr` receives a string `address` as input.
2.  We directly call the `replace()` method on the `address` string.
3.  The first argument to `replace()` is `"."`, which is the substring we want to find.
4.  The second argument is `"[.]"`, which is the substring we want to replace `.` with.
5.  The `replace()` method returns a *new* string with all occurrences of `.` replaced by `[.]`. Strings in Python are immutable, so `replace()` never modifies the original string; it always returns a new one.
6.  This new string is then returned as the result.

## Complexity Analysis

Let `N` be the length of the input `address` string.

*   **Time Complexity**: O(N)
    *   The `str.replace()` method in Python needs to iterate through the entire input string to find all occurrences of the target substring and construct the new string. In the worst case, it scans the string once. Therefore, the time complexity is linear with respect to the length of the input string.

*   **Space Complexity**: O(N)
    *   The `str.replace()` method creates a new string to store the result. The length of the output string will be at most `N + 2 * k`, where `k` is the number of periods in the IP address. For a valid IPv4 address, `k` is always 3. So, the maximum length of the output string is `N + 2*3 = N + 6`. Since `N` is typically small for an IP address (e.g., "255.255.255.255" is 15 characters), `N+6` is still considered O(N) space.

## Common Pitfalls / Mistakes

1.  **Attempting In-Place Modification**: A common mistake for beginners in languages like Python (where strings are immutable) is trying to modify the string in-place. For example, `address[i] = ...` would raise a `TypeError`. String operations always return a new string.
2.  **Inefficient String Concatenation**: If one were to implement this manually by iterating and building the string using repeated `+` or `+=` operations (e.g., `result = ""; for char in address: result += char`), it could lead to O(N^2) time complexity in some languages or Python versions for very long strings, as each `+=` might create a new string and copy contents. Building a list of characters/substrings and then using `"".join(list)` is the more efficient manual approach (O(N)), but `str.replace()` is even better for this specific problem.
3.  **Overthinking Simple Problems**: This is an "Easy" problem. Sometimes candidates try to come up with overly complex solutions (e.g., using regular expressions when `str.replace()` is sufficient) when a direct built-in method is the most optimal and intended solution.

## Real Interview Follow-Up Questions

Here are some common follow-up questions and how to approach them:

1.  **What if the input string could be extremely long (e.g., gigabytes), too large to fit into memory?**
    *   **Answer**: This changes the problem from string manipulation to **stream processing**. We cannot load the entire string into memory. Instead, we would read the input character by character (or in small chunks) from an input stream and write the defanged output to an output stream.
    *   **Approach**:
        ```python
        # Example conceptual code for stream processing
        def defang_ip_stream(input_stream, output_stream):
            while True:
                char = input_stream.read(1) # Read one character at a time
                if not char: # End of stream
                    break
                if char == '.':
                    output_stream.write('[.]') # Write the replacement
                else:
                    output_stream.write(char) # Write the original character
        ```
    *   **Complexity**: Time complexity would still be O(N) (where N is the total length of the stream), but **space complexity would be O(1)** (excluding the output buffer, which is written to a stream), as we only hold a few characters in memory at any given time.

2.  **What if we needed to replace multiple different characters with different strings?** (e.g., `.` with `[.]`, `-` with `_`, ` ` with `+`)
    *   **Answer**:
        *   **Chained `replace()` calls**: For a small, fixed number of replacements, chaining `replace()` calls is simple and often sufficient: `address.replace(".", "[.]").replace("-", "_").replace(" ", "+")`. Be mindful of the order if replacements could overlap (e.g., replacing 'a' with 'b' then 'b' with 'c' would turn 'a' into 'c'). For non-overlapping replacements, order doesn't matter.
        *   **Regular Expressions (`re.sub`)**: For more complex patterns, many replacements, or when the replacements themselves are dynamic, `re.sub` is powerful.
            ```python
            import re
            def multi_replace(text, replacements_dict):
                # replacements_dict = {'.': '[.]', '-': '_', ' ': '+'}
                # Create a regex pattern that matches any key in the dictionary
                # re.escape ensures special regex characters in keys are treated literally
                pattern = re.compile('|'.join(re.escape(key) for key in replacements_dict.keys()))
                def replacer(match):
                    # For each match, return its corresponding replacement value
                    return replacements_dict[match.group(0)]
                return pattern.sub(replacer, text)
            ```
        *   **Manual Iteration**: For very specific control or if regex is disallowed/too complex, one could iterate through the string, building a list of parts, and checking for each character/substring to replace. This is generally less efficient than `re.sub` for many replacements.

3.  **Could this operation be parallelized or done concurrently?**
    *   **Answer**: For a *single* IP address string, the operation is inherently sequential. You need to scan the string from beginning to end. Parallelizing this for a single small string would introduce more overhead than benefit.
    *   However, if you have a *list of many IP addresses* to defang, then yes, the task is **embarrassingly parallel**. Each IP address can be defanged independently.
        *   **Multiprocessing**: In Python, `multiprocessing.Pool` can be used to distribute the `defangIPaddr` function calls across multiple CPU cores. This is suitable for CPU-bound tasks like string manipulation.
        *   **Concurrency (e.g., `threading`, `asyncio`)**: Less effective for CPU-bound tasks in Python due to the Global Interpreter Lock (GIL), which limits true parallel execution of Python bytecode. Multiprocessing is generally preferred for true parallelism.
