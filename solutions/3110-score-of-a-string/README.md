# 3110. Score of a String

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/score-of-a-string/](https://leetcode.com/problems/score-of-a-string/)  
**Topics:** String

---

## 📝 Problem Statement

You are given a string `s`. The **score** of a string is defined as the sum of the absolute difference between the **ASCII** values of adjacent characters.

Return the **score** of* *`s`.

 
Example 1:

**Input:** s = "hello"

**Output:** 13

**Explanation:**

The **ASCII** values of the characters in `s` are: `'h' = 104`, `'e' = 101`, `'l' = 108`, `'o' = 111`. So, the score of `s` would be `|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13`.

Example 2:

**Input:** s = "zaz"

**Output:** 50

**Explanation:**

The **ASCII** values of the characters in `s` are: `'z' = 122`, `'a' = 97`. So, the score of `s` would be `|122 - 97| + |97 - 122| = 25 + 25 = 50`.

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def scoreOfString(self, s: str) -> int:
        total_score = 0  # Initialize the total score to accumulate differences.
        
        # Iterate through the string from the first character up to the second-to-last character.
        # This ensures that for each index 'i', 's[i+1]' is a valid index,
        # allowing us to consider all adjacent pairs (s[i], s[i+1]).
        # The loop will run 'len(s) - 1' times, covering all adjacent pairs.
        for i in range(len(s) - 1):
            # Get the ASCII (or Unicode) value of the current character s[i].
            # Python's ord() function returns the Unicode code point, which
            # is equivalent to ASCII for ASCII characters.
            char1_ascii = ord(s[i])
            
            # Get the ASCII (or Unicode) value of the next character s[i+1].
            char2_ascii = ord(s[i+1])
            
            # Calculate the absolute difference between their ASCII values
            # and add this difference to the total score.
            total_score += abs(char1_ascii - char2_ascii)
            
        return total_score
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
