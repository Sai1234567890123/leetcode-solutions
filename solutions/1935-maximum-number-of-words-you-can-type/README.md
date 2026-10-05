# 1935. Maximum Number of Words You Can Type

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/maximum-number-of-words-you-can-type/](https://leetcode.com/problems/maximum-number-of-words-you-can-type/)  
**Topics:** Hash Table, String

---

## 📝 Problem Statement

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string `text` of words separated by a single space (no leading or trailing spaces) and a string `brokenLetters` of all **distinct** letter keys that are broken, return *the **number of words** in* `text` *you can fully type using this keyboard*.

 
Example 1:

```

**Input:** text = "hello world", brokenLetters = "ad"
**Output:** 1
**Explanation:** We cannot type "world" because the 'd' key is broken.

```

Example 2:

```

**Input:** text = "leet code", brokenLetters = "lt"
**Output:** 1
**Explanation:** We cannot type "leet" because the 'l' and 't' keys are broken.

```

Example 3:

```

**Input:** text = "leet code", brokenLetters = "e"
**Output:** 0
**Explanation:** We cannot type either word because the 'e' key is broken.

```

 
**Constraints:**

	- `1 4`

	- `0

---

## 💻 Implementation (python3)

```py
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Convert broken letters to a hash set for O(1) membership lookup.
        broken_set = set(brokenLetters)
        
        # Split the text into individual words.
        words = text.split(' ')
        typed_words_count = 0
        
        for word in words:
            # A word can be typed if none of its characters are in broken_set.
            # Using any() allows short-circuiting on the first broken character encountered.
            if not any(char in broken_set for char in word):
                typed_words_count += 1
                
        return typed_words_count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks us to determine how many words in a given space-separated string `text` can be typed without using any character present in `brokenLetters`. 

A word cannot be typed if **at least one** of its characters is broken. Conversely, a word can be typed if **none** of its characters are broken.
1. Checking membership in a string of length $B$ takes $O(B)$ time. To optimize repeated lookups, we convert `brokenLetters` into a hash set (or a boolean array/bitmask since the alphabet size is bounded by 26), enabling $O(1)$ lookup time.
2. We then evaluate each word. By using a short-circuiting check (`any(...)`), we can abandon checking a word as soon as the first broken character is found.

### Step-by-Step Approach
1. **Hash Set Construction**: Construct a `set` named `broken_set` from `brokenLetters`.
2. **Word Tokenization**: Split `text` by spaces to obtain the list of words.
3. **Word Validation**:
   - For each word, check if `any(char in broken_set for char in word)`.
   - If `False`, increment our valid word counter.
4. **Return Result**: Return the counter once all words have been inspected.

*Alternative (Space-optimized $O(1)$ auxiliary)*: We can also iterate through `text` character-by-character without splitting, tracking whether the current word has encountered a broken letter, and incrementing the count when a space or end-of-string is reached. In Python, `text.split(' ')` is typically faster due to C-level implementation, but streaming/single-pass is optimal for constrained memory.

### Complexity Analysis
- **Time Complexity**: $O(N + B)$, where $N$ is the length of `text` and $B$ is the length of `brokenLetters`.
  - Converting `brokenLetters` to a set takes $O(B)$ time. Since $B \le 26$, this is effectively $O(1)$.
  - Splitting `text` takes $O(N)$ time.
  - Inspecting characters across all words takes at most $O(N)$ lookups, each taking $O(1)$ average time.
  - Overall Time Complexity: **$O(N)$**.
- **Space Complexity**: $O(N + B)$ auxiliary space.
  - `broken_set` requires $O(B)$ space ($B \le 26$, hence $O(1)$).
  - `text.split(' ')` creates a list of words taking $O(N)$ space.
  - Note: Using a single-pass pointer approach reduces auxiliary space to $O(1)$ (since alphabet size is $\le 26$).

### Common Pitfalls / Mistakes Candidates Make
- **Linear Search in `brokenLetters`**: Checking `char in brokenLetters` without converting `brokenLetters` to a `set`. While $B \le 26$ means this passes LeetCode tests, in an interview, using a set or bitmask demonstrates an understanding of optimal complexity.
- **Handling Whitespace & Splitting**: Using `text.split()` vs `text.split(' ')`. The problem states words are separated by a single space with no leading/trailing spaces, but candidates should be aware that `str.split()` discards consecutive whitespaces, which could be an issue if empty tokens matter in other variations.
- **Inefficient Validation**: Counting all broken characters in a word instead of short-circuiting on the very first broken character found.

### Real Interview Follow-Up Questions & Answers

1. **What if the input `text` is a massive stream of characters (e.g., gigabytes) that cannot fit into memory?**
   - *Answer*: We cannot use `split()`. Instead, we process the stream character by character using two variables: `can_type_current_word = True` and `total_typed = 0`.
   - For each character:
     - If it's a space: if `can_type_current_word` is `True`, increment `total_typed`; reset `can_type_current_word = True`.
     - If it's not a space and it exists in `broken_set`: set `can_type_current_word = False`.
   - At EOF (end of file/stream): if `can_type_current_word` is `True`, increment `total_typed`.
   - Space complexity drops to $O(1)$ auxiliary space.

2. **How would you optimize space if `brokenLetters` consists of only lowercase English letters without using a hash table?**
   - *Answer*: Use a 32-bit integer bitmask. Set the $i$-th bit where $i = \text{ord}(c) - \text{ord}('a')$. Membership test is simply `(mask >> (ord(c) - ord('a'))) & 1`. This provides true $O(1)$ memory, zero heap allocations, and faster CPU cache performance.

3. **What if this function is called billions of times with different `text` strings but the same `brokenLetters`?**
   - *Answer*: Precompute the bitmask or lookup table once and reuse it across queries. If multithreaded, store this lookup table in thread-local storage or pass it as an immutable reference.
