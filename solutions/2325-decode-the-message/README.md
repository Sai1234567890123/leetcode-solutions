# 2325. Decode the Message

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/decode-the-message/](https://leetcode.com/problems/decode-the-message/)  
**Topics:** Hash Table, String

---

## 📝 Problem Statement

You are given the strings `key` and `message`, which represent a cipher key and a secret message, respectively. The steps to decode `message` are as follows:

	- Use the **first** appearance of all 26 lowercase English letters in `key` as the **order** of the substitution table.

	- Align the substitution table with the regular English alphabet.

	- Each letter in `message` is then **substituted** using the table.

	- Spaces `' '` are transformed to themselves.

	- For example, given `key = "**hap**p**y** **bo**y"` (actual key would have **at least one** instance of each letter in the alphabet), we have the partial substitution table of (`'h' -> 'a'`, `'a' -> 'b'`, `'p' -> 'c'`, `'y' -> 'd'`, `'b' -> 'e'`, `'o' -> 'f'`).

Return *the decoded message*.

 
Example 1:

```

**Input:** key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
**Output:** "this is a secret"
**Explanation:** The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "**the** **quick** **brown** **f**o**x** **j**u**mps** o**v**er the **lazy** **d**o**g**".

```

Example 2:

```

**Input:** key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
**Output:** "the five boxing wizards jump quickly"
**Explanation:** The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "**eljuxhpwnyrdgtqkviszcfmabo**".

```

 
**Constraints:**

	- `26

---

## 💻 Implementation (python3)

```py
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Map space to space by default
        mapping = {' ': ' '}
        curr_code = ord('a')
        
        # Build the substitution cipher table from the first appearance of each letter
        for ch in key:
            if ch not in mapping:
                mapping[ch] = chr(curr_code)
                curr_code += 1
                # Early exit if all 26 letters have been mapped
                if curr_code > ord('z'):
                    break
        
        # Decode the message using the substitution mapping
        return "".join(mapping[ch] for ch in message)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires constructing a 1-to-1 substitution cipher using the first occurrence of each distinct lowercase English letter in `key`.
1. Letters are mapped sequentially to `'a'`, `'b'`, `'c'`, ..., `'z'` in the order they first appear.
2. Spaces `' '` map to spaces `' '`.
3. Any subsequent appearances of an already mapped character in `key` are ignored.
4. Once the mapping is established, every character in `message` is replaced by its corresponding mapped value.

We can achieve optimal runtime and space by scanning `key` character-by-character to populate a hash map (or fixed-size array). Once all 26 letters are assigned, we can stop scanning `key` early. Then, we transform `message` using this dictionary and assemble the decoded string.

### Step-by-Step Approach

1. **Initialize Mapping**:
   - Initialize a dictionary `mapping` containing `{' ': ' '}`.
   - Maintain an ASCII code pointer `curr_code = ord('a')`.
2. **Build Substitution Table**:
   - Iterate through each character `ch` in `key`.
   - If `ch` is not in `mapping`, assign `mapping[ch] = chr(curr_code)` and increment `curr_code` by 1.
   - If `curr_code > ord('z')`, all 26 letters have been registered, so we can break early.
3. **Decode Message**:
   - Use a generator expression `(mapping[ch] for ch in message)` combined with `"".join(...)` to build the decoded output string in $O(N)$ time.

### Complexity Analysis

- **Time Complexity**: 
  - Building the mapping takes at most $O(\min(K, 26 + \text{spaces})) \le O(K)$ where $K$ is the length of `key`.
  - Decoding `message` takes $O(M)$ where $M$ is the length of `message`, because dictionary lookups and list joining run in linear time.
  - Overall Time Complexity: $\mathcal{O}(K + M)$, which is strictly optimal.
- **Space Complexity**:
  - The hash map contains at most 27 entries (26 lowercase letters + 1 space), requiring $\mathcal{O}(1)$ auxiliary space.
  - The output string takes $\mathcal{O}(M)$ space.
  - Overall Space Complexity: $\mathcal{O}(1)$ auxiliary space (excluding output).

### Common Pitfalls / Mistakes Candidates Make

1. **Repeated Key Characters**: Overwriting mapping when a character is seen again in `key` instead of checking `if ch not in mapping:`.
2. **Space Character Handling**: Forgetting that spaces can appear anywhere in `key` or `message` and must be preserved as spaces without consuming an alphabet slot.
3. **String Concatenation in Loops**: Doing `res += mapping[ch]` inside a loop creates an intermediate string at each step, resulting in an avoidable $\mathcal{O}(M^2)$ time complexity. Always use `"".join(...)`.

### Real Interview Follow-Up Questions

1. **What if the message is a continuous stream of characters?**
   - *Answer*: If `message` is an infinite stream (e.g., iterator/generator), we cannot buffer the whole string in memory. Instead, process chunks (e.g., buffers of 4KB/8KB) using `sys.stdin.read(chunk_size)` and yield decoded chunks directly to the output stream.

2. **What if the alphabet size is much larger (e.g., full Unicode / UTF-8)?**
   - *Answer*: A fixed 26-element alphabet assumption no longer holds. We would dynamically index into the desired target character set (e.g., code points `0` to `N - 1`), and the hash map size would scale with the number of unique characters in the key: $\mathcal{O}(U)$ auxiliary space, where $U$ is the number of unique characters.

3. **Can we make this even faster in Python using built-ins?**
   - *Answer*: Yes, Python's `str.maketrans()` and `str.translate()` are implemented in C. We could construct a translation table and call `message.translate(table)`, which avoids Python-level loop overhead for very large strings.
