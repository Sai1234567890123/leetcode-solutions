# 2108. Find First Palindromic String in the Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-first-palindromic-string-in-the-array/](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)  
**Topics:** Array, Two Pointers, String

---

## 📝 Problem Statement

Given an array of strings `words`, return *the first **palindromic** string in the array*. If there is no such string, return *an **empty string** *`""`.

A string is **palindromic** if it reads the same forward and backward.

 
Example 1:

```

**Input:** words = ["abc","car","ada","racecar","cool"]
**Output:** "ada"
**Explanation:** The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

```

Example 2:

```

**Input:** words = ["notapalindrome","racecar"]
**Output:** "racecar"
**Explanation:** The first and only string that is palindromic is "racecar".

```

Example 3:

```

**Input:** words = ["def","ghi"]
**Output:** ""
**Explanation:** There are no palindromic strings, so the empty string is returned.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        """
        Finds and returns the first palindromic string in the given array.
        Returns an empty string if no palindrome is found.
        """
        def is_palindrome(s: str) -> bool:
            # Two-pointer approach to avoid allocating extra memory for reversed strings
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
                
        return ""
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A palindrome is a string that reads the exact same forward and backward. The problem asks for the *first* palindrome in the given list of strings, which directly implies an early-exit linear scan:
1. Iterate over each word in the order it appears in `words`.
2. Check if the current word is a palindrome.
3. If it is, immediately return it (preserving the "first" occurrence requirement).
4. If no such string is found after checking all words, return an empty string `""`.

While in Python one could simply do `word == word[::-1]`, creating a reversed string slice takes $O(L)$ auxiliary space for each word of length $L$. Using a two-pointer technique to compare characters from both ends moving inward achieves $O(1)$ auxiliary space and allows early termination as soon as a mismatch is detected.

### Step-by-Step Approach

1. Define a helper function `is_palindrome(s)`:
   - Initialize two pointers: `left = 0` and `right = len(s) - 1`.
   - Loop while `left < right`:
     - If `s[left] != s[right]`, return `False` immediately.
     - Increment `left` and decrement `right`.
   - If the loop finishes without mismatches, return `True`.
2. Iterate through each `word` in `words`:
   - If `is_palindrome(word)` evaluates to `True`, return `word`.
3. If the loop completes without finding a palindrome, return `""`.

### Complexity Analysis

- **Time Complexity:** 
  - **Worst Case:** $O(N \times L)$, where $N$ is the number of words in `words` and $L$ is the maximum length of a word. In the worst case (e.g., no palindrome exists, or words are near-palindromes that fail on the last check), every character of every word is inspected at most once.
  - **Best Case:** $O(1)$ if the first word is a palindrome of length 1.
- **Space Complexity:** $O(1)$ auxiliary space. The two-pointer comparison does not allocate additional string copies or data structures.

### Common Pitfalls / Mistakes Candidates Make

- **Using `word == word[::-1]` blindly:** While concise and Pythonic, it creates an entirely new string copy of length $L$ in memory. In interviews, senior interviewers will ask about the memory implications and prefer the $O(1)$ auxiliary space two-pointer approach.
- **Not stopping at the first match:** Some candidates collect all palindromes in a list and then return `palindromes[0]`. This wastes time and memory instead of returning eagerly.
- **Off-by-one errors in two-pointer logic:** Ensuring the loop termination condition is `left < right` rather than `left <= right` saves an unnecessary middle-element self-comparison on odd-length strings.

### Real Interview Follow-Up Questions & Answers

1. **What if the input is a continuous data stream where we cannot store all words?**
   - *Answer:* The two-pointer check can be executed on each word as it arrives from the stream. As soon as the first palindrome is detected, we can return/yield it and terminate or stop listening, consuming $O(1)$ memory.

2. **What if characters can be Unicode or include punctuation and case insensitivity (like LeetCode 125: Valid Palindrome)?**
   - *Answer:* We would adjust the two pointers to skip non-alphanumeric characters (`isalnum()`) and compare normalized characters (e.g., using `casefold()` or `lower()`).

3. **How would you parallelize this for billions of words across distributed machines (e.g., MapReduce / Spark)?**
   - *Answer:* Because we need the *first* palindrome in the original order, we must partition the dataset while tracking chunk indices. Each worker finds the first palindrome (if any) in its chunk along with its global index. A coordinator then picks the palindrome with the minimum global index.
