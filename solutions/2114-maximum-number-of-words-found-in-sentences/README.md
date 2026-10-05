# 2114. Maximum Number of Words Found in Sentences

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)  
**Topics:** Array, String

---

## 📝 Problem Statement

A **sentence** is a list of **words** that are separated by a single space with no leading or trailing spaces.

You are given an array of strings `sentences`, where each `sentences[i]` represents a single **sentence**.

Return *the **maximum number of words** that appear in a single sentence*.

 
Example 1:

```

**Input:** sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
**Output:** 6
**Explanation:** 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

```

Example 2:

```

**Input:** sentences = ["please wait", "continue to fight", "continue to win"]
**Output:** 3
**Explanation:** It is possible that multiple sentences contain the same number of words. 
In this example, the second and third sentences (underlined) have the same number of words.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        """
        Finds the maximum number of words in a single sentence.
        
        Since words are separated by exactly one space with no leading
        or trailing spaces, the number of words in a sentence is
        equal to (number of spaces) + 1.
        """
        # Using str.count(' ') avoids allocating memory for split lists,
        # running in O(1) auxiliary space and optimal C-level speed.
        return max(s.count(' ') for s in sentences) + 1
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem states that each sentence consists of words separated by a single space, with **no leading or trailing spaces**.

A naive approach would be to use `sentence.split(' ')` and take the length of the resulting list (`len(sentence.split())`). However, creating an array of substrings for each sentence incurs unnecessary memory allocation and garbage collection overhead.

By utilizing the problem constraint (exactly one space between words, no leading/trailing spaces):
$$\text{Word Count} = \text{Space Count} + 1$$

Thus, the sentence with the maximum number of words is simply the sentence with the maximum number of spaces. We can find the maximum space count across all sentences using Python's highly optimized built-in string method `str.count(' ')` and add $1$ at the end.

### Step-by-Step Approach

1. Iterate through each string `s` in `sentences`.
2. For each string, count the occurrences of the space character `' '`.
3. Compute the maximum count among all strings using a generator expression inside `max()`.
4. Add `1` to the result to convert space count to word count and return.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(T)$ where $T$ is the total number of characters across all sentences in the array ($T = \sum |sentences[i]|$). In the worst case, each character is examined once by the Boyer-Moore / memchr-optimized C implementation of `str.count()`.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The generator expression streams one count at a time without allocating intermediate lists or token arrays.

### Common Pitfalls / Mistakes Candidates Make

1. **Using `.split()`:** While functionally correct (`max(len(s.split()) for s in sentences)`), this creates lists of newly allocated strings in memory for every sentence, turning an $\mathcal{O}(1)$ auxiliary space solution into $\mathcal{O}(L)$ space (where $L$ is the maximum sentence length) and increasing cache misses.
2. **Assuming multiple consecutive spaces:** Overcomplicating the logic with regular expressions or custom state machines when the problem guarantees single space separation. Always read constraint guarantees carefully.
3. **Empty strings / Edge cases:** Although constraints specify $1 \le \text{length} \le 100$ and no empty sentences, if an empty string `""` were allowed, `"".count(' ') + 1` would incorrectly yield `1`. Always verify whether empty sentences are possible.

### Real Interview Follow-Up Questions

1. **What if sentences contain multiple consecutive spaces, tabs, or leading/trailing spaces?**
   - *Answer:* The space counting trick no longer holds. We would use a two-pointer approach or iterate through characters with a boolean flag `in_word` to count state transitions from whitespace to non-whitespace in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space, avoiding `.split()`.

2. **What if the input is a massive stream of sentences that cannot fit into memory?**
   - *Answer:* Process the stream lazily sentence-by-sentence. Maintain a running maximum variable `max_words = 0`. For each incoming sentence chunk, compute its word count and update `max_words = max(max_words, words_in_current)`.

3. **How would you parallelize this across multiple cores or a distributed system (e.g., MapReduce/Spark)?**
   - *Answer:* Word counting per sentence is embarrassingly parallel:
     - **Map phase:** Each worker receives a partition of sentences and outputs the local maximum word count for its chunk.
     - **Reduce phase:** A single reducer takes the maximum of the local maximums.
