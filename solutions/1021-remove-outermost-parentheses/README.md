# 1021. Remove Outermost Parentheses

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/remove-outermost-parentheses/](https://leetcode.com/problems/remove-outermost-parentheses/)  
**Topics:** String, Stack, Bracket Sequences

---

## 📝 Problem Statement

A valid parentheses string is either empty `""`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.

	- For example, `""`, `"()"`, `"(())()"`, and `"(()(()))"` are all valid parentheses strings.

A valid parentheses string `s` is primitive if it is nonempty, and there does not exist a way to split it into `s = A + B`, with `A` and `B` nonempty valid parentheses strings.

Given a valid parentheses string `s`, consider its primitive decomposition: `s = P1 + P2 + ... + Pk`, where `Pi` are primitive valid parentheses strings.

Return `s` *after removing the outermost parentheses of every primitive string in the primitive decomposition of *`s`.

 
Example 1:

```

**Input:** s = "(()())(())"
**Output:** "()()()"
**Explanation:** 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

```

Example 2:

```

**Input:** s = "(()())(())(()(()))"
**Output:** "()()()()(())"
**Explanation:** 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

```

Example 3:

```

**Input:** s = "()()"
**Output:** ""
**Explanation:** 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

```

 
**Constraints:**

	- `1 5`

	- `s[i]` is either `'('` or `')'`.

	- `s` is a valid parentheses string.

---

## 💻 Implementation (python3)

```py
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        
        for char in s:
            if char == '(':
                # If depth > 0, this '(' is NOT the outermost opening parenthesis
                # of the current primitive block.
                if depth > 0:
                    res.append(char)
                depth += 1
            else: # char == ')'
                depth -= 1
                # If depth > 0 after decrement, this ')' is NOT the outermost closing parenthesis
                # of the current primitive block.
                if depth > 0:
                    res.append(char)
                    
        return "".join(res)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A primitive valid parentheses string is a valid parentheses substring that cannot be split into smaller non-empty valid parentheses substrings. In terms of depth/balance (where `'('` increments the counter and `')'` decrements it):
- A primitive block starts when `depth == 0` and reaches `depth == 0` again only at the end of the block.
- The outermost opening parenthesis of a primitive component is the one that transitions `depth` from `0` to `1`.
- The outermost closing parenthesis of a primitive component is the one that transitions `depth` from `1` to `0`.
- All other parentheses inside the component are strictly at `depth >= 1` before processing `'('` or after processing `')'`.

Thus, we can track the current nesting `depth`:
1. When encountering `'('`: include it in the result if and only if `depth > 0` before incrementing.
2. When encountering `')'`: decrement `depth` first; include it in the result if and only if `depth > 0` after decrementing.

### Step-by-Step Approach

1. Initialize an empty list `res` to accumulate characters for the final string (joining a list is $O(N)$, whereas string concatenation in a loop can degrade to $O(N^2)$).
2. Initialize `depth = 0`.
3. Iterate through each character `char` in string `s`:
   - If `char == '('`:
     - If `depth > 0`, append `'('` to `res`.
     - Increment `depth` by 1.
   - If `char == ')'`:
     - Decrement `depth` by 1.
     - If `depth > 0`, append `')'` to `res`.
4. Return `"".join(res)`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of string `s`. We traverse the string of length $N$ exactly once. Character appends to the list take amortized $\mathcal{O}(1)$ time, and the final join operation takes $\mathcal{O}(N)$ time.
- **Space Complexity:** $\mathcal{O}(N)$ to store the output characters. Auxiliary space (excluding the output string) is $\mathcal{O}(1)$ as only an integer `depth` is maintained.

### Common Pitfalls / Mistakes Candidates Make

1. **Repeated String Concatenation:** Writing `res += char` inside a loop in Python. Since strings are immutable, this can lead to $\mathcal{O}(N^2)$ time complexity due to repeated memory allocations and copies.
2. **Over-engineering with a Stack:** Storing characters on an explicit `list` as a stack when all we need is the count/depth of parentheses. An explicit stack consumes unnecessary $\mathcal{O}(N)$ auxiliary space.
3. **Off-by-one Depth Tracking:** Appending before vs. after incrementing/decrementing `depth`. Candidates often confuse whether `depth` represents the state before or after the current character is accounted for.

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input arrives as an infinite or large stream?
*Answer:* The algorithm is inherently a single-pass streaming algorithm. Instead of building the entire result in memory, we can yield characters as a generator or write them directly to an output stream / buffer with $\mathcal{O}(1)$ auxiliary memory:
```python
def stream_remove_outer(stream):
    depth = 0
    for char in stream:
        if char == '(':
            if depth > 0:
                yield char
            depth += 1
        elif char == ')':
            depth -= 1
            if depth > 0:
                yield char
```

#### 2. What if the input can contain invalid parentheses strings?
*Answer:* If the string might be invalid:
- `depth` dropping below `0` indicates an unmatched `')'`.
- `depth > 0` at the end of the string indicates unmatched `'('`.
Depending on business requirements, we can either raise an exception, discard the malformed component, or perform a two-pass greedy cleanup (similar to LeetCode 1249: *Minimum Remove to Make Valid Parentheses*).

#### 3. How would you solve this in-place if the string were mutable (e.g., a character array `List[str]`)?
*Answer:* Use the two-pointer technique (read pointer and write pointer).
```python
def removeOuterParenthesesInPlace(s: list[str]) -> int:
    write = 0
    depth = 0
    for char in s:
        if char == '(':
            if depth > 0:
                s[write] = char
                write += 1
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                s[write] = char
                write += 1
    return write  # Returns the new valid length
```
