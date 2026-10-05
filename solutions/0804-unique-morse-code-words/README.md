# 0804. Unique Morse Code Words

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/unique-morse-code-words/](https://leetcode.com/problems/unique-morse-code-words/)  
**Topics:** Array, Hash Table, String

---

## 📝 Problem Statement

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

	- `'a'` maps to `".-"`,

	- `'b'` maps to `"-..."`,

	- `'c'` maps to `"-.-."`, and so on.

For convenience, the full table for the `26` letters of the English alphabet is given below:

```

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
```

Given an array of strings `words` where each word can be written as a concatenation of the Morse code of each letter.

	- For example, `"cab"` can be written as `"-.-..--..."`, which is the concatenation of `"-.-."`, `".-"`, and `"-..."`. We will call such a concatenation the **transformation** of a word.

Return *the number of different **transformations** among all words we have*.

 
Example 1:

```

**Input:** words = ["gin","zen","gig","msg"]
**Output:** 2
**Explanation:** The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

```

Example 2:

```

**Input:** words = ["a"]
**Output:** 1

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        # Predefined Morse code representations for characters 'a' through 'z'
        morse_table = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        
        # Base ASCII value for 'a' to map characters to morse_table indices
        ord_a = ord('a')
        
        # Use a set to collect distinct transformations
        seen_transformations = set()
        
        for word in words:
            # Map each character to its Morse code and join
            transformation = "".join(morse_table[ord(char) - ord_a] for char in word)
            seen_transformations.add(transformation)
            
        return len(seen_transformations)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the number of distinct Morse code encodings among a list of words.
Because each character maps deterministically to a short Morse string, the encoding of any word is simply the concatenation of the Morse strings corresponding to its individual characters.

To count *unique* transformations:
1. Translate each character $c$ using an $O(1)$ lookup: the index in our pre-defined table is `ord(c) - ord('a')`.
2. Concatenate these Morse strings to form the word's Morse representation.
3. Insert each representation into a hash set. Hash sets automatically deduplicate identical entries.
4. The final answer is simply the cardinality (length) of the set.

### Step-by-Step Approach

1. **Predefine Morse Table**: Store the 26 Morse code strings in an indexed array where index `0` corresponds to `'a'`, index `1` to `'b'`, ..., and index `25` to `'z'`.
2. **Initialize Set**: Create an empty hash set `seen_transformations`.
3. **Process Each Word**:
   - For each word in `words`, iterate through each character `char`.
   - Convert `char` to index via `ord(char) - ord('a')`.
   - Concatenate the Morse codes using `''.join(...)` for optimal string allocation in Python.
   - Insert the resulting string into `seen_transformations`.
4. **Return Result**: Return `len(seen_transformations)`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(S)$, where $S$ is the sum of the lengths of all words in `words` ($S = \sum |word|$). 
  - Each character is looked up in $\mathcal{O}(1)$ time.
  - A character's Morse representation is at most 4 characters long. Thus, for a word of length $L$, building the Morse string takes $\mathcal{O}(L)$ time, and hashing/inserting it into the set takes $\mathcal{O}(L)$ time on average.
  - Across all words, total time is linear with respect to the total number of characters, which is at most $100 \times 12 = 1200$ operations.
- **Space Complexity:** $\mathcal{O}(S)$ auxiliary space.
  - In the worst case where every word has a unique Morse transformation, the set will store all $N$ transformed strings, each of length at most $4L$.

### Common Pitfalls / Mistakes Candidates Make

1. **String Concatenation in a Loop (`+=`):** In Python and languages like Java, doing `s += morse[c]` creates a new string object each iteration, leading to unnecessary $\mathcal{O}(L^2)$ intermediate string allocations per word. Using `"".join(...)` is cleaner, idiomatic, and runs in $\mathcal{O}(L)$.
2. **Dictionary vs Array Lookup:** While using a `dict` mapping `'a' -> ".-"` works, an indexed array with `ord(c) - ord('a')` achieves a lower constant factor and eliminates hash overhead during character lookup.
3. **Not Recognizing Ambiguity of Morse Code:** Morse code is not a prefix-free code (e.g., `"gin"` and `"zen"` produce the exact same sequence). Candidates sometimes assume decoding is 1-to-1; recognizing that collisions are intentional and expected here is key.

### Real Interview Follow-Up Questions

#### 1. What if the input stream is massive (Streaming Data)?
*Answer:* If we have millions of streaming words and memory is bounded:
- If we only need an approximate count of unique transformations, we can use a **HyperLogLog (HLL)** cardinality estimator, which tracks unique items with negligible memory (e.g., ~1.5 KB with ~1% error rate).
- If exact counts are required and memory is exceeded, we can stream and partition words by hash onto external storage (MapReduce / distributed hash partition) or use a persistent Key-Value store (like RocksDB or Redis sets).

#### 2. Could we use a Trie instead of a Hash Set?
*Answer:* Yes. Since Morse code only consists of two characters (`.` and `-`), a binary Trie where each node has at most two children (`left = '.'`, `right = '-'`) can store transformations.
- **Benefits:** Common prefixes are shared, reducing memory when words share large initial segments of Morse code. Insertion and lookup are strictly $\mathcal{O}(L)$ with no hash collisions.
- **Drawback in Python:** Python object overhead per Trie node often outweighs the raw memory saved compared to native string hashing unless implemented at a lower level or with a compact array.

#### 3. Reverse Problem: Can we decode an ambiguous Morse string back to English words?
*Answer:* If given a Morse string and a dictionary of valid English words, find all valid original word sequences.
- This is a classic backtracking / dynamic programming problem. We can insert dictionary words into a Trie (or pre-encode words into Morse and build a Morse Trie), then perform DFS on the Morse string matching valid word endings. Memoization can prevent re-exploring overlapping sub-problems.
