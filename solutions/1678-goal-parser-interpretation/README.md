# 1678. Goal Parser Interpretation

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/goal-parser-interpretation/](https://leetcode.com/problems/goal-parser-interpretation/)  
**Topics:** String

---

## 📝 Problem Statement

You own a **Goal Parser** that can interpret a string `command`. The `command` consists of an alphabet of `"G"`, `"()"` and/or `"(al)"` in some order. The Goal Parser will interpret `"G"` as the string `"G"`, `"()"` as the string `"o"`, and `"(al)"` as the string `"al"`. The interpreted strings are then concatenated in the original order.

Given the string `command`, return *the **Goal Parser**'s interpretation of *`command`.

 
Example 1:

```

**Input:** command = "G()(al)"
**Output:** "Goal"
**Explanation:** The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

```

Example 2:

```

**Input:** command = "G()()()()(al)"
**Output:** "Gooooal"

```

Example 3:

```

**Input:** command = "(al)G(al)()()G"
**Output:** "alGalooG"

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def interpret(self, command: str) -> str:
        """
        Interprets the Goal parser command by parsing valid tokens in a single pass.
        
        Token Mappings:
        - "G"    -> "G"
        - "()"   -> "o"
        - "(al)" -> "al"
        """
        res = []
        i = 0
        n = len(command)
        
        while i < n:
            if command[i] == 'G':
                res.append('G')
                i += 1
            elif command[i + 1] == ')':
                # Token is "()"
                res.append('o')
                i += 2
            else:
                # Token is "(al)"
                res.append('al')
                i += 4
                
        return "".join(res)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires translating specific substrings into predefined tokens:
- `"G"` $\to$ `"G"`
- `"()"` $\to$ `"o"`
- `"(al)"` $\to$ `"al"`

While Python's built-in `str.replace()` could solve this problem in one line (`command.replace("()", "o").replace("(al)", "al")`), in an interview setting, especially at top-tier companies, implementing a deterministic single-pass lexical scanner / parser demonstrates a stronger grasp of memory, pointers, and parsing mechanics.

Notice that the grammar is LL(1) (or distinguishable by looking ahead at most one character past `(`):
- If `command[i] == 'G'`, it must be `"G"`.
- If `command[i] == '('`, checking `command[i + 1]` uniquely disambiguates:
  - If `command[i + 1] == ')'`, the token is `"()"`.
  - If `command[i + 1] == 'a'`, the token must be `"(al)"`.

### Step-by-Step Approach

1. Initialize a dynamic array (`res = []`) to accumulate translated strings, and an index pointer `i = 0`.
2. Iterate while `i < len(command)`:
   - If `command[i] == 'G'`, append `'G'` to `res` and increment `i` by 1.
   - Else if `command[i + 1] == ')'`, append `'o'` and increment `i` by 2.
   - Else (meaning the substring is `"(al)"`), append `'al'` and increment `i` by 4.
3. Join the resulting list into a single string with `"".join(res)`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of `command`. Every character is examined at most a constant number of times, and pointer `i` strictly advances forward. Joining the list takes linear time.
- **Space Complexity:** $\mathcal{O}(N)$ to store the output string and internal buffer list. No extra auxiliary space beyond the output is needed ($\mathcal{O}(1)$ auxiliary space).

### Common Pitfalls / Mistakes Candidates Make

1. **Repeated String Concatenation:** Using `result += "..."` inside the loop in Python. In Python, strings are immutable, so repeated concatenation results in $\mathcal{O}(N^2)$ time complexity due to creating new string allocations on each step. Using a list and `"".join()` guarantees $\mathcal{O}(N)$.
2. **Out-of-Bounds Indexing:** Checking `command[i + 1]` without ensuring the string input conforms to the grammar. While the problem guarantees a valid command, candidates should always verify or mention bounds-checking defensively.
3. **Regex Overkill:** Reaching for heavy regular expressions (`re.sub`). While concise, it adds unnecessary overhead for a simple deterministic finite automaton (DFA).

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input stream is infinite or too large to fit in memory (Streaming Data)?
*Answer:* A generator / iterator pattern can be used. Instead of building the whole output string in memory, yield characters or tokens as they are parsed from an input buffer (e.g., chunks of 4096 bytes). Since the grammar only requires a lookahead of 1 character (looking at `i + 1`), a buffer of size 4 is sufficient to emit parsed output continuously in $\mathcal{O}(1)$ auxiliary memory.

#### 2. How would you generalize this parser if there were hundreds of different command mappings?
*Answer:* Construct a **Trie** (Prefix Tree) or use the **Aho-Corasick** automaton representing all valid token strings. Walk the Trie character by character. When a terminal node is reached, emit the mapped value and reset to the root. This keeps the time complexity linear with respect to the input text length, regardless of the number of dictionary patterns.
