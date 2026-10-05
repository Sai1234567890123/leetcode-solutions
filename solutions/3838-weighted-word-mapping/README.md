# 3838. Weighted Word Mapping

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/weighted-word-mapping/](https://leetcode.com/problems/weighted-word-mapping/)  
**Topics:** Array, String, Simulation

---

## 📝 Problem Statement

You are given an array of strings `words`, where each string represents a word containing lowercase English letters.

You are also given an integer array `weights` of length 26, where `weights[i]` represents the weight of the `ith` lowercase English letter.

The **weight** of a word is defined as the **sum** of the weights of its characters.

For each word, take its weight modulo 26 and map the result to a lowercase English letter using reverse alphabetical order (`0 -> 'z', 1 -> 'y', ..., 25 -> 'a'`).

Return a string formed by concatenating the mapped characters for all words in order.

 
Example 1:

**Input:** words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

**Output:** "rij"

**Explanation:**

	- The weight of `"abcd"` is `5 + 3 + 12 + 14 = 34`. The result modulo 26 is `34 % 26 = 8`, which maps to `'r'`.

	- The weight of `"def"` is `14 + 1 + 2 = 17`. The result modulo 26 is `17 % 26 = 17`, which maps to `'i'`.

	- The weight of `"xyz"` is `7 + 7 + 2 = 16`. The result modulo 26 is `16 % 26 = 16`, which maps to `'j'`.

Thus, the string formed by concatenating the mapped characters is `"rij"`.

Example 2:

**Input:** words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

**Output:** "yyy"

**Explanation:**

Each word has weight 1. The result modulo 26 is `1 % 26 = 1`, which maps to `'y'`.

Thus, the string formed by concatenating the mapped characters is `"yyy"`.

Example 3:

**Input:** words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]

**Output:** "g"

**Explanation:​​​​​​​**

The weight of `"abcd"` is `7 + 5 + 3 + 4 = 19`. The result modulo 26 is `19 % 26 = 19`, which maps to `'g'`.

Thus, the string formed by concatenating the mapped characters is `"g"`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # Pre-compute the character mapping for efficiency and clarity.
        # The problem states: 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'.
        # This means for an index `i`, the character is `chr(ord('z') - i)`.
        # Example:
        # i = 0: chr(ord('z') - 0) = 'z'
        # i = 1: chr(ord('z') - 1) = 'y'
        # i = 25: chr(ord('z') - 25) = 'a'
        char_mapping_table = [chr(ord('z') - i) for i in range(26)]
        
        # Use a list to collect mapped characters, then join them at the end.
        # This is more efficient than repeated string concatenation in Python,
        # which can lead to O(N^2) behavior for N concatenations.
        result_chars = []
        
        # Iterate through each word in the input list.
        for word in words:
            current_word_weight = 0
            # Iterate through each character in the current word.
            for char in word:
                # Calculate the 0-indexed position of the character.
                # 'a' corresponds to index 0, 'b' to 1, ..., 'z' to 25.
                char_index = ord(char) - ord('a')
                
                # Add the corresponding weight from the weights array.
                current_word_weight += weights[char_index]
            
            # Apply modulo 26 to the total word weight.
            # This ensures the result is an index in the range [0, 25].
            mapped_index = current_word_weight % 26
            
            # Look up the mapped character using the pre-computed table.
            mapped_char = char_mapping_table[mapped_index]
            result_chars.append(mapped_char)
            
        # Join all collected characters to form the final result string.
        return "".join(result_chars)
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
