# 3498. Reverse Degree of a String

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/reverse-degree-of-a-string/](https://leetcode.com/problems/reverse-degree-of-a-string/)  
**Topics:** String, Simulation

---

## 📝 Problem Statement

Given a string `s`, calculate its **reverse degree**.

The **reverse degree** is calculated as follows:

	- For each character, multiply its position in the *reversed* alphabet (`'a'` = 26, `'b'` = 25, ..., `'z'` = 1) with its position in the string **(1-indexed)**.

	- Sum these products for all characters in the string.

Return the **reverse degree** of `s`.

 
Example 1:

**Input:** s = "abc"

**Output:** 148

**Explanation:**

	
		
			Letter
			Index in Reversed Alphabet
			Index in String
			Product
		
		
			`'a'`
			26
			1
			26
		
		
			`'b'`
			25
			2
			50
		
		
			`'c'`
			24
			3
			72
		
	

The reversed degree is `26 + 50 + 72 = 148`.

Example 2:

**Input:** s = "zaza"

**Output:** 160

**Explanation:**

	
		
			Letter
			Index in Reversed Alphabet
			Index in String
			Product
		
		
			`'z'`
			1
			1
			1
		
		
			`'a'`
			26
			2
			52
		
		
			`'z'`
			1
			3
			3
		
		
			`'a'`
			26
			4
			104
		
	

The reverse degree is `1 + 52 + 3 + 104 = 160`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def reverseDegree(self, s: str) -> int:
        total_reverse_degree = 0  # Initialize the sum for the reverse degree

        # Iterate through the string with both the 0-indexed position (i) and the character (char).
        # For example, for "abc":
        # i=0, char='a'
        # i=1, char='b'
        # i=2, char='c'
        for i, char in enumerate(s):
            # Calculate the 0-indexed position of the character in the standard alphabet.
            # 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
            # This is done by subtracting the ASCII value of 'a' from the character's ASCII value.
            standard_alphabet_pos_0_indexed = ord(char) - ord('a')

            # Calculate the position in the reversed alphabet.
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            # The formula is 26 - (0-indexed standard position).
            reversed_alphabet_pos = 26 - standard_alphabet_pos_0_indexed

            # Calculate the 1-indexed position of the character in the string.
            # If 'i' is the 0-indexed position, the 1-indexed position is 'i + 1'.
            string_pos_1_indexed = i + 1

            # Multiply the reversed alphabet position by the 1-indexed string position
            # and add the product to the total sum.
            total_reverse_degree += reversed_alphabet_pos * string_pos_1_indexed

        return total_reverse_degree
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to calculate a "reverse degree" for a given string `s`. This degree is defined by two components for each character:
1.  Its position in a *reversed* alphabet (where 'a' = 26, 'b' = 25, ..., 'z' = 1).
2.  Its 1-indexed position within the string.

We need to multiply these two values for each character and then sum up all these products.

Let's break down how to calculate each component:

**1. Position in Reversed Alphabet:**
*   The standard 0-indexed position of a character in the alphabet can be found by `ord(char) - ord('a')`. For example:
    *   `ord('a') - ord('a') = 0`
    *   `ord('b') - ord('a') = 1`
    *   `ord('z') - ord('a') = 25`
*   The problem defines the reversed alphabet position as: 'a' = 26, 'b' = 25, ..., 'z' = 1.
*   We can observe a pattern: `reversed_pos = 26 - (standard_0_indexed_pos)`.
    *   For 'a': `26 - 0 = 26` (Correct)
    *   For 'b': `26 - 1 = 25` (Correct)
    *   For 'z': `26 - 25 = 1` (Correct)
    This formula works perfectly.

**2. Position in String (1-indexed):**
*   When iterating through a string in most programming languages (like Python's `enumerate`), we get a 0-indexed position.
*   To convert a 0-indexed position `i` to a 1-indexed position, we simply add 1: `i + 1`.

With these two components defined, the overall process is straightforward: iterate through the string, calculate the product for each character, and accumulate the sum.

## Step-by-Step Approach

1.  Initialize a variable `total_reverse_degree` to `0`. This variable will store the cumulative sum of products.
2.  Iterate through the input string `s`. Python's `enumerate(s)` is ideal here, as it provides both the 0-indexed position (`i`) and the character (`char`) for each element.
3.  Inside the loop, for each character `char` at index `i`:
    a.  Calculate its 0-indexed standard alphabet position: `standard_alphabet_pos_0_indexed = ord(char) - ord('a')`.
    b.  Calculate its reversed alphabet position: `reversed_alphabet_pos = 26 - standard_alphabet_pos_0_indexed`.
    c.  Calculate its 1-indexed position in the string: `string_pos_1_indexed = i + 1`.
    d.  Multiply these two values: `product = reversed_alphabet_pos * string_pos_1_indexed`.
    e.  Add this `product` to `total_reverse_degree`.
4.  After the loop completes, `total_reverse_degree` will hold the final result. Return this value.

## Complexity Analysis

*   **Time Complexity: O(N)**
    *   We iterate through the input string `s` exactly once.
    *   For each character, we perform a constant number of arithmetic operations (subtractions, multiplications, additions) and character-to-ordinal conversions.
    *   If `N` is the length of the string, the total time taken is directly proportional to `N`. This is optimal because we must examine every character in the string to compute the sum.

*   **Space Complexity: O(1)**
    *   We use a single variable `total_reverse_degree` to store the running sum.
    *   No additional data structures are created that scale with the input size `N`.
    *   Therefore, the space complexity is constant. This is optimal.

## Common Pitfalls / Mistakes

1.  **Off-by-one errors:**
    *   **String Indexing:** A common mistake is to use the 0-indexed `i` directly for the string position instead of `i + 1`. The problem explicitly states "1-indexed" for the string position.
    *   **Reversed Alphabet Calculation:** Incorrectly calculating the reversed alphabet position (e.g., `25 - (ord(char) - ord('a'))` instead of `26 - ...`). The range of values is 1 to 26, so 'a' (0-indexed 0) maps to 26, and 'z' (0-indexed 25) maps to 1. The formula `26 - (0-indexed position)` correctly achieves this.
2.  **Case Sensitivity:** Although the problem constraints specify "lowercase English letters", in a real interview, candidates might forget to confirm this or handle mixed-case input. If mixed-case were allowed, converting characters to lowercase (`char.lower()`) before calculation would be necessary.
3.  **Integer Overflow (less common in Python):** In languages like C++ or Java, if the string length `N` were extremely large (e.g., 10^9), the `total_reverse_degree` could exceed the capacity of a standard 32-bit integer. Python handles arbitrary-precision integers automatically, so this is not an issue. For `N=1000`, the maximum sum is `1000 * (26 * 1000) = 2.6 * 10^7`, which fits comfortably within a 32-bit signed integer.

## Real Interview Follow-Up Questions

1.  **What if the string could contain uppercase letters or other characters?**
    *   **Answer:** The current solution assumes strictly lowercase English letters as per constraints. If other characters were possible, we'd need clarification on how to handle them:
        *   **Ignore:** Skip characters that are not lowercase English letters.
        *   **Error:** Raise an error or return a special value if invalid characters are encountered.
        *   **Convert:** For uppercase letters, convert them to lowercase first (e.g., `char.lower()`) before applying the existing logic.
        *   **Extended Mapping:** For other characters (e.g., digits, symbols), a custom mapping or a different definition of "alphabet position" would be required.

2.  **What if the string is very long, say, gigabytes of data (streaming data)?**
    *   **Answer:** The current algorithm is already well-suited for streaming data. It processes characters one by one and only requires constant extra space (for the running sum and index). We don't need to load the entire string into memory.
    *   In a streaming scenario, instead of `enumerate(s)`, we would read characters from an input stream (e.g., a file handle, network buffer). We would manually maintain the `string_pos_1_indexed` counter. The core logic remains the same.

3.  **What if the alphabet size changes (e.g., 50 letters, or a custom alphabet)?**
    *   **Answer:** The constant `26` in `26 - (ord(char) - ord('a'))` is specific to the 26-letter English alphabet.
    *   If we have a custom alphabet (e.g., `custom_alphabet = "abc...xyzABC...XYZ"` of length `L`), we would first need to create a mapping from each character to its 0-indexed position within that custom alphabet.
        *   `char_to_pos = {c: i for i, c in enumerate(custom_alphabet)}`
    *   Then, the `reversed_alphabet_pos` would be `L - char_to_pos[char]`. The rest of the calculation (multiplying by `string_pos_1_indexed` and summing) would remain identical.

4.  **Could this be parallelized for extremely long strings?**
    *   **Answer:** Yes, this problem is "embarrassingly parallel." For a very long string, we could divide it into `K` chunks.
    *   Each chunk would be processed by a separate thread or process. The crucial point is that the `string_pos_1_indexed` for a character depends on its global position in the original string, not just its position within its chunk.
    *   So, if a chunk starts at global 0-indexed position `start_idx`, a character at local 0-indexed position `j` within that chunk would have a global 1-indexed position of `start_idx + j + 1`.
    *   Each thread would calculate a partial sum for its assigned chunk. Finally, these partial sums would be aggregated (summed up) to get the total reverse degree. This approach would significantly speed up computation for very large inputs.
