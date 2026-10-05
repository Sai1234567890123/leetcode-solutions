# 1614. Maximum Nesting Depth of the Parentheses

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)  
**Topics:** String, Stack, Bracket Sequences

---

## 📝 Problem Statement

Given a **valid parentheses string** `s`, return the **nesting depth** of* *`s`. The nesting depth is the **maximum** number of nested parentheses.

 
Example 1:

**Input:** s = "(1+(2*3)+((8)/4))+1"

**Output:** 3

**Explanation:**

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

**Input:** s = "(1)+((2))+(((3)))"

**Output:** 3

**Explanation:**

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

**Input:** s = "()(())((()()))"

**Output:** 3

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Calculates the maximum nesting depth of a valid parentheses string.
        
        Time Complexity: O(n) where n is the length of the string s.
        Space Complexity: O(1) auxiliary space.
        """
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
                
        return max_depth
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the maximum nesting depth in a guaranteed valid parentheses string (VPS). 
- Every `'('` increases the nesting level by 1.
- Every `')'` decreases the nesting level by 1.
- Any other character (digits, operators, whitespace) does not affect the nesting structure.

Because the input is guaranteed to be a valid parentheses string, we don't need a stack data structure to check matching types or track balanced states. An integer counter tracking the `current_depth` as we iterate from left to right is sufficient. The answer will be the highest value `current_depth` reaches during the traversal.

### Step-by-Step Approach

1. Initialize `current_depth = 0` and `max_depth = 0`.
2. Iterate through each character `char` in string `s`:
   - If `char == '('`: Increment `current_depth` by 1 and update `max_depth = max(max_depth, current_depth)`.
   - If `char == ')'`: Decrement `current_depth` by 1.
   - Ignore all other characters.
3. Return `max_depth`.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the length of `s`. We scan the string once character by character.
- **Space Complexity:** $O(1)$ auxiliary space. Only two integer variables (`current_depth` and `max_depth`) are maintained.

### Common Pitfalls / Mistakes

1. **Unnecessary Stack Allocation:** Candidates often reach for an explicit `stack = []` because of the word "parentheses". While correct, pushing/popping introduces $O(n)$ space and allocation overhead when a simple counter is $O(1)$ space.
2. **Assuming String is Invalid:** Writing complex validation logic when the problem explicitly specifies that the string is a **valid parentheses string**. Always read input guarantees.
3. **Resetting Depth Incorrectly:** Misunderstanding depth by resetting to 0 at the wrong time (e.g., when encountering numbers or operators).

### Real Interview Follow-Up Questions & Answers

#### 1. What if the string is NOT guaranteed to be valid?
- **Answer:** If the string may contain mismatched or unbalanced parentheses (e.g., `"())("` or `"(("`):
  - If we only have `'('` and `')'`, we check if `current_depth < 0` at any point (too many closing parentheses) and verify `current_depth == 0` at the end (no unclosed parentheses). If invalid, return -1 or raise an exception.
  - If there are multiple bracket types (`()`, `[]`, `{}`), we must use an explicit stack to verify opening/closing types match.

#### 2. How would you handle a continuous data stream of infinite length?
- **Answer:** The $O(1)$ space counter approach naturally supports streaming. The function can accept an iterator or generator yielding chunks or characters:
  ```python
  def maxDepthStream(stream_iter) -> int:
      current_depth = max_depth = 0
      for char in stream_iter:
          if char == '(':
              current_depth += 1
              max_depth = max(max_depth, current_depth)
          elif char == ')':
              current_depth -= 1
      return max_depth
  ```
  This processes chunks without buffering the full stream into memory.

#### 3. How to parallelize this for massive files (e.g., a multi-gigabyte JSON or Lisp file)?
- **Answer:** We can use a map-reduce pattern using prefix sums:
  - **Map step:** For a chunk of text, calculate:
    1. Net change in depth $\Delta = \text{count}('(') - \text{count}(')')$.
    2. Minimum prefix depth within the chunk (to detect validity/underflow).
    3. Peak depth within the chunk relative to its start.
  - **Reduce step:** Combine chunk summaries sequentially:
    - Compute starting depth for chunk $k$ as the prefix sum of $\Delta$ across chunks $0 \dots k-1$.
    - The global max depth is $\max(\text{start\_depth}_k + \text{peak\_depth}_k)$.
