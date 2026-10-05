# 2942. Find Words Containing Character

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-words-containing-character/](https://leetcode.com/problems/find-words-containing-character/)  
**Topics:** Array, String

---

## 📝 Problem Statement

You are given a **0-indexed** array of strings `words` and a character `x`.

Return *an **array of indices** representing the words that contain the character *`x`.

**Note** that the returned array may be in **any** order.

 
Example 1:

```

**Input:** words = ["leet","code"], x = "e"
**Output:** [0,1]
**Explanation:** "e" occurs in both words: "l**ee**t", and "cod**e**". Hence, we return indices 0 and 1.

```

Example 2:

```

**Input:** words = ["abc","bcd","aaaa","cbc"], x = "a"
**Output:** [0,2]
**Explanation:** "a" occurs in "**a**bc", and "**aaaa**". Hence, we return indices 0 and 2.

```

Example 3:

```

**Input:** words = ["abc","bcd","aaaa","cbc"], x = "z"
**Output:** []
**Explanation:** "z" does not occur in any of the words. Hence, we return an empty array.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Initialize an empty list to store the indices of words that contain character x.
        result_indices = []
        
        # Iterate through the 'words' array along with their corresponding indices.
        # The 'enumerate' function is used to get both the index (i) and the word itself.
        for i, word in enumerate(words):
            # Check if the character 'x' is present within the current 'word'.
            # Python's 'in' operator for strings efficiently performs this check.
            if x in word:
                # If 'x' is found in the 'word', append its current index to our result list.
                result_indices.append(i)
                
        # After iterating through all words, return the list of collected indices.
        return result_indices
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
