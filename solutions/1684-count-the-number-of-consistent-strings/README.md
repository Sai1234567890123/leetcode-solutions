# 1684. Count the Number of Consistent Strings

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-the-number-of-consistent-strings/](https://leetcode.com/problems/count-the-number-of-consistent-strings/)  
**Topics:** Array, Hash Table, String, Bit Manipulation, Counting

---

## 📝 Problem Statement

You are given a string `allowed` consisting of **distinct** characters and an array of strings `words`. A string is **consistent **if all characters in the string appear in the string `allowed`.

Return* the number of **consistent** strings in the array *`words`.

 
Example 1:

```

**Input:** allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
**Output:** 2
**Explanation:** Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

```

Example 2:

```

**Input:** allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
**Output:** 7
**Explanation:** All strings are consistent.

```

Example 3:

```

**Input:** allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
**Output:** 4
**Explanation:** Strings "cc", "acd", "ac", and "d" are consistent.

```

 
**Constraints:**

	- `1 4`

	- `1  26`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        # Construct a bitmask representing the characters present in `allowed`.
        # Each bit from 0 to 25 corresponds to 'a' through 'z'.
        allowed_mask = 0
        for ch in allowed:
            allowed_mask |= 1 << (ord(ch) - ord('a'))
        
        consistent_count = 0
        
        for word in words:
            is_consistent = True
            for ch in word:
                # Check if the bit corresponding to character `ch` is set in allowed_mask.
                if not (allowed_mask & (1 << (ord(ch) - ord('a')))):
                    is_consistent = False
                    break  # Early exit as soon as an invalid character is found
            
            if is_consistent:
                consistent_count += 1
                
        return consistent_count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires checking whether every character in each string in `words` exists within the string `allowed`.

Since the alphabet is strictly lowercase English letters (`'a'` to `'z'`, only 26 unique characters), we have two primary data structure choices for $O(1)$ membership checks:
1. **Hash Set**: Straightforward, but incurs object allocation and hashing overhead.
2. **Bitmask (Bit Vector)**: A single 32-bit integer where the $k$-th bit is $1$ if the $k$-th letter of the alphabet is allowed, and $0$ otherwise. Bitwise operations are executed in a single CPU instruction, requiring $O(1)$ auxiliary space and minimal cache pressure.

Using a bitmask with early termination on the first disallowed character gives the optimal balance of runtime performance and memory footprint.

---

### Step-by-Step Approach

1. **Build `allowed_mask`**:
   - Initialize `allowed_mask = 0`.
   - Iterate through each character `ch` in `allowed`, mapping `'a'` to `0`, `'b'` to `1`, ..., `'z'` to `25`.
   - Set the corresponding bit: `allowed_mask |= 1 << (ord(ch) - ord('a'))`.

2. **Validate Each Word**:
   - For each word in `words`, iterate through its characters.
   - For character `ch`, check if its bit is set in `allowed_mask`: `(allowed_mask & (1 << bit)) != 0`.
   - If any character's bit is `0`, the word is not consistent; break early.
   - If the loop finishes without breaking, increment the `consistent_count`.

3. **Return Result**:
   - Return the accumulated count.

---

### Complexity Analysis

- **Time Complexity**: $O(M + \sum |words[i]|)$, where $M$ is the length of `allowed` (at most 26), and $\sum |words[i]|$ is the total number of characters across all words in `words`.
  - Creating `allowed_mask` takes $O(M)$ time.
  - Checking each character in each word takes $O(1)$ time with bitwise shifts and masking. Early termination reduces the average-case runtime further.
- **Space Complexity**: $O(1)$ auxiliary space. Only a few integer variables are used (`allowed_mask`, loop indices), which is strictly constant regardless of input size.

---

### Common Pitfalls / Mistakes

1. **Checking with String `in` Operator**: Using `ch in allowed` repeatedly without converting `allowed` to a set or bitmask results in an $O(M)$ scan per character, yielding $O(M \times \sum |words[i]|)$ time complexity.
2. **Missing Early Exit**: Iterating over the entire word even after encountering an invalid character hurts performance on long strings.
3. **Overcomplicating with Sets of Sets**: Converting every word to `set(word).issubset(allowed_set)` creates lots of intermediate set objects, which triggers heavy garbage collection overhead in Python.

---

### Real Interview Follow-Up Questions & Answers

1. **What if the character set is arbitrary Unicode (UTF-8 / full UTF-16)?**
   - *Answer*: A 32-bit integer mask can no longer be used. We would switch to a Hash Set (`HashSet<int>` or Python's `set`) storing Unicode code points. If memory is constrained and false positives are tolerable, a Bloom Filter could be used.

2. **How to handle a streaming scenario where `words` arrive continuously over a network?**
   - *Answer*: The `allowed_mask` is precomputed once. Incoming words can be processed in an event-driven stream (e.g., using Kafka/Flink) independently. Because checking each word is completely stateless and read-only with respect to `allowed_mask`, the processing can be embarrassingly parallelized across worker threads or nodes.

3. **What if `words` is massive (billions of strings) stored across a distributed cluster?**
   - *Answer*: This is a classic MapReduce / distributed filtering task. Broadcast the small `allowed_mask` (or hash set) to all worker nodes. Each mapper filters its partition of `words` and emits local counts. A single reducer sums up the partition counts.
