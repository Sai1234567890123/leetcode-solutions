# 3541. Find Most Frequent Vowel and Consonant

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/](https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/)  
**Topics:** Hash Table, String, Counting

---

## 📝 Problem Statement

You are given a string `s` consisting of lowercase English letters (`'a'` to `'z'`). 

Your task is to:

	- Find the vowel (one of `'a'`, `'e'`, `'i'`, `'o'`, or `'u'`) with the **maximum** frequency.

	- Find the consonant (all other letters excluding vowels) with the **maximum** frequency.

Return the sum of the two frequencies.

**Note**: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
The **frequency** of a letter `x` is the number of times it occurs in the string.
 
Example 1:

**Input:** s = "successes"

**Output:** 6

**Explanation:**

	- The vowels are: `'u'` (frequency 1), `'e'` (frequency 2). The maximum frequency is 2.

	- The consonants are: `'s'` (frequency 4), `'c'` (frequency 2). The maximum frequency is 4.

	- The output is `2 + 4 = 6`.

Example 2:

**Input:** s = "aeiaeia"

**Output:** 3

**Explanation:**

	- The vowels are: `'a'` (frequency 3), `'e'` ( frequency 2), `'i'` (frequency 2). The maximum frequency is 3.

	- There are no consonants in `s`. Hence, maximum consonant frequency = 0.

	- The output is `3 + 0 = 3`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Define the set of vowels for O(1) membership check
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Count frequency of each character in s
        freq = Counter(s)
        
        max_vowel_freq = 0
        max_consonant_freq = 0
        
        # Find maximum frequency among vowels and consonants
        for char, count in freq.items():
            if char in vowels:
                if count > max_vowel_freq:
                    max_vowel_freq = count
            else:
                if count > max_consonant_freq:
                    max_consonant_freq = count
                    
        return max_vowel_freq + max_consonant_freq
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks for the sum of the maximum frequency of any vowel and the maximum frequency of any consonant in a lowercase English string `s`.

1. **Character Frequency Counting**: A character frequency map (or hash map) efficiently tallies occurrences of all characters.
2. **Classification**:
   - Vowels: `{'a', 'e', 'i', 'o', 'u'}`.
   - Consonants: Any lowercase letter from `'a'` through `'z'` that is not in the vowel set.
3. **Tracking Maxima**: Maintain two tracking variables, `max_vowel_freq` and `max_consonant_freq`, initialized to `0`. As we iterate through the frequencies of each unique character, update the respective tracker.
4. **Result**: Return `max_vowel_freq + max_consonant_freq`. If there are no vowels or no consonants, their respective tracker remains `0`, naturally satisfying the problem specification.

### Step-by-Step Approach
1. Store vowels in a hash set for $O(1)$ lookups.
2. Compute character frequencies using Python's `collections.Counter(s)` in a single pass.
3. Traverse the frequency table (which has at most 26 entries) and update:
   - `max_vowel_freq` if the character is in `vowels`.
   - `max_consonant_freq` otherwise.
4. Return `max_vowel_freq + max_consonant_freq`.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the length of string `s`. Counting characters takes $\mathcal{O}(N)$ time. The subsequent loop runs at most 26 times (the size of the English alphabet), which is $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space. The alphabet contains only 26 distinct lowercase letters, so the frequency hash map consumes a constant upper-bound of memory regardless of $N$.

### Common Pitfalls / Mistakes Candidates Make
- **Empty Vowel/Consonant Case**: Forgetting to default to `0` when a string has no vowels (e.g., `"rhythm"`) or no consonants (e.g., `"aeiou"`). Initializing trackers to `0` avoids `ValueError` when taking `max()` on empty sequences.
- **Handling Case Sensitivity**: Assuming uppercase letters could appear without checking the constraints. The problem guarantees only lowercase `'a'`-`'z'`.
- **Inefficient Passes**: Calling `s.count(char)` for each letter, which takes $\mathcal{O}(26 \times N)$, instead of a single $\mathcal{O}(N)$ pass.

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input is a massive data stream that cannot fit into memory?
**Answer**:
We can maintain a fixed-size frequency array of size 26 (or hash map) on the fly. As chunks of the stream arrive, we increment counts. Since space is bounded by $\mathcal{O}(|\Sigma|) = \mathcal{O}(26) = \mathcal{O}(1)$, it handles infinite streams with zero memory pressure. At any point, we can query the max vowel and consonant in $\mathcal{O}(1)$ time.

#### 2. What if Unicode / Internationalization (i18n) is introduced (e.g., accented vowels `á`, `é`, or other languages)?
**Answer**:
We would need a locale-aware definition of vowels and consonants. In Python, the `unicodedata` module can normalize characters (e.g., NFKD decomposition) to strip accents, or we can use a locale-specific vowel dictionary/regex class. Note that alphabet size would no longer be strictly 26, but the algorithm remains $\mathcal{O}(N)$ time and $\mathcal{O}(U)$ space where $U$ is the number of unique Unicode code points.

#### 3. How would you handle multithreaded / distributed processing (MapReduce)?
**Answer**:
Split string `s` into $K$ chunks. Each worker computes a local `Counter` of character frequencies. The reducer merges the counters (summing up frequencies per letter) and performs the final max-vowel and max-consonant aggregation.
