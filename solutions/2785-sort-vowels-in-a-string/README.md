# 2785. Sort Vowels in a String

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/sort-vowels-in-a-string/](https://leetcode.com/problems/sort-vowels-in-a-string/)  
**Topics:** String, Sorting

---

## 📝 Problem Statement

Given a **0-indexed** string `s`, **permute** `s` to get a new string `t` such that:

	- All consonants remain in their original places. More formally, if there is an index `i` with `0 

Return *the resulting string*.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

 
Example 1:

```

**Input:** s = "lEetcOde"
**Output:** "lEOtcede"
**Explanation:** 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.

```

Example 2:

```

**Input:** s = "lYmpH"
**Output:** "lYmpH"
**Explanation:** There are no vowels in s (all characters in s are consonants), so we return "lYmpH".

```

 
**Constraints:**

	- `1 5`

	- `s` consists only of letters of the English alphabet in **uppercase and lowercase**.

---

## 💻 Implementation (python3)

```py
class Solution:
    def sortVowels(self, s: str) -> str:
        # Vowels ordered by their ASCII values:
        # 'A' (65) < 'E' (69) < 'I' (73) < 'O' (79) < 'U' (85) <
        # 'a' (97) < 'e' (101) < 'i' (105) < 'o' (111) < 'u' (117)
        VOWELS_SORTED = "AEIOUaeiou"
        vowel_set = set(VOWELS_SORTED)
        
        # Count frequency of each vowel in s (Counting Sort approach: O(1) auxiliary space)
        vowel_counts = [0] * len(VOWELS_SORTED)
        vowel_to_idx = {char: i for i, char in enumerate(VOWELS_SORTED)}
        
        for ch in s:
            if ch in vowel_set:
                vowel_counts[vowel_to_idx[ch]] += 1
        
        # Reconstruct the string: preserve consonants, place vowels in ASCII order
        result = list(s)
        current_vowel_idx = 0
        
        for i, ch in enumerate(result):
            if ch in vowel_set:
                # Advance to the next available vowel in ASCII order
                while vowel_counts[current_vowel_idx] == 0:
                    current_vowel_idx += 1
                
                result[i] = VOWELS_SORTED[current_vowel_idx]
                vowel_counts[current_vowel_idx] -= 1
                
        return "".join(result)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires us to preserve the relative positions of all consonants while sorting all vowels in non-decreasing order by their ASCII values.

Notice that:
1. The uppercase vowels (`A, E, I, O, U`) have smaller ASCII values (`65, 69, 73, 79, 85`) than the lowercase vowels (`a, e, i, o, u` with values `97, 101, 105, 111, 117`).
2. There are only $10$ distinct vowel characters in total.

While we could extract all vowels into a list and sort them in $O(V \log V)$ time (where $V \le N$), the fixed size of the vowel alphabet ($|\Sigma_{\text{vowels}}| = 10$) makes **Counting Sort** optimal. We can count the occurrences of each vowel in $O(N)$ time, and then replace each vowel in the original string sequentially with the lowest available vowel from our frequency map in $O(N)$ time.

### Step-by-Step Approach

1. **Predefine the Vowel Order**: Define the sorted order string `VOWELS_SORTED = "AEIOUaeiou"`.
2. **Frequency Count**: Traverse the string `s` once and maintain counts of each of the $10$ vowels.
3. **In-place Replacement**: Convert `s` to a list of characters (since Python strings are immutable). Traverse the characters again:
   - If the character is a consonant, leave it untouched.
   - If the character is a vowel, consume the next available vowel from the frequency count and overwrite the character.
4. **Return**: Join the list back into a string.

### Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the length of `s`.
  - Counting vowels takes one pass: $O(N)$.
  - Reconstructing the string takes another pass: $O(N)$.
  - Pointer advances across the 10 vowels take $O(1)$ operations in total.
  - Overall time complexity is strictly linear, outperforming $O(N \log N)$ sorting.

- **Space Complexity:** $O(N)$ to construct the mutable output array and final string (required in Python as strings are immutable). The auxiliary space for the counting array is $O(1)$ because the alphabet of vowels is fixed at $10$ elements.

### Common Pitfalls / Mistakes

1. **Incorrect ASCII Order Assumption**: Assuming uppercase and lowercase letters interleave (e.g., `'a'`, `'A'`, `'e'`, `'E'`). In ASCII, all uppercase letters come before all lowercase letters (`'A'-'Z'` are $65-90$, `'a'-'z'` are $97-122$).
2. **Missing Uppercase Vowels**: Overlooking that the input may contain uppercase vowels.
3. **Inefficient Sorting / String Concatenation**: Using repetitive string concatenation (`+`) instead of building a list and calling `"".join()`, which leads to an $O(N^2)$ runtime in languages without rope-based string optimization.

### Real Interview Follow-Up Questions

1. **What if the input is a massive stream of characters rather than an in-memory string?**
   - *Answer*: Since we cannot know the first vowel to output until we have seen all vowels in the stream, we cannot output the characters in a single pass without buffering. However, we could write the stream to a temporary file while keeping the 10 vowel counts in memory ($O(1)$ memory). On a second pass through the temporary file, we stream out the modified characters one by one.

2. **What if the alphabet was arbitrary Unicode characters instead of 10 ASCII vowels?**
   - *Answer*: If the set of vowels is large or dynamic, a fixed-size counting array is not practical. We would extract the vowels into a list, sort them using Timsort ($O(V \log V)$), and use a two-pointer approach or an iterator to place them back.

3. **Can we do this in-place with $O(1)$ extra space if the language supports mutable strings (e.g., C++)?**
   - *Answer*: Yes, in C++ `std::string` is mutable. We can record frequencies of vowels in an array of size 10 ($O(1)$ auxiliary space) and overwrite the `std::string` in-place, achieving true $O(1)$ auxiliary memory.
