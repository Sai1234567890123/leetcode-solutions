# 3280. Convert Date to Binary

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/convert-date-to-binary/](https://leetcode.com/problems/convert-date-to-binary/)  
**Topics:** Math, String

---

## 📝 Problem Statement

You are given a string `date` representing a Gregorian calendar date in the `yyyy-mm-dd` format.

`date` can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in `year-month-day` format.

Return the **binary** representation of `date`.

 
Example 1:

**Input:** date = "2080-02-29"

**Output:** "100000100000-10-11101"

**Explanation:**

100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

Example 2:

**Input:** date = "1900-01-01"

**Output:** "11101101100-1-1"

**Explanation:**

11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.

 
**Constraints:**

	- `date.length == 10`

	- `date[4] == date[7] == '-'`, and all other `date[i]`'s are digits.

	- The input is generated such that `date` represents a valid Gregorian calendar date between Jan 1st, 1900 and Dec 31st, 2100 (both inclusive).

---

## 💻 Implementation (python3)

```py
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # Split the date string by '-' into [year, month, day]
        # Convert each segment to an integer, format it as a binary string without prefix,
        # and join them back with '-'
        return "-".join(f"{int(part):b}" for part in date.split("-"))
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires converting a date formatted as `"yyyy-mm-dd"` into its binary representation where each component (year, month, and day) is expressed in base-2 without leading zeros, separated by hyphens.

1. **Deconstruction**: The date string has a fixed format and delimiters (`-`). Splitting by `'-'` cleanly extracts the year, month, and day substrings.
2. **Parsing & Base Conversion**: Parsing each segment as a base-10 integer automatically strips any leading zeros (e.g., `"02"` becomes `2`). Converting each integer to a binary string can be achieved directly via Python's string formatting (`f"{num:b}"`) or `bin(num)[2:]`.
3. **Reassembly**: Join the converted binary strings using `'-'` as the delimiter.

### Step-by-Step Approach

1. Split the string `date` by hyphen `-`, yielding a list of three substrings: `[year, month, day]`.
2. For each part, convert it to an integer using `int(part)` to handle numeric values and remove leading zeros.
3. Convert the integer to its binary representation using `f"{val:b}"` (which omits the `'0b'` prefix produced by the built-in `bin()` function).
4. Re-join the three binary strings with `'-'`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$. The input string length is strictly fixed at 10 characters (`yyyy-mm-dd`). Parsing, converting small numbers (year $\le 2100$, month $\le 12$, day $\le 31$), and string joining operate in constant time.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The output string has a bounded length of at most $12 + 1 + 4 + 1 + 5 = 23$ characters, requiring $\mathcal{O}(1)$ additional memory.

### Common Pitfalls / Mistakes

- **Retaining `'0b'` Prefix**: Using `bin(x)` directly without slicing off the first two characters (`bin(x)[2:]`) produces results like `"0b100000100000-0b10-0b11101"`, which violates the expected output format.
- **Preserving Leading Zeros**: Trying to convert each digit character individually rather than parsing the complete token as an integer leads to incorrect representations (e.g., converting `"02"` as `"0"` and `"10"` instead of `2` $\rightarrow$ `"10"`).

### Real Interview Follow-Up Questions

1. **How would you handle high-throughput streaming date conversions without repeated string allocations?**
   - *Answer:* In languages like C++ or Go, pre-allocate a fixed-size character buffer on the stack (e.g., 24 bytes). Manually extract the digits via simple arithmetic (e.g., `(date[0]-'0')*1000 + ...`), compute the binary representations using bitwise shifts (`>>`) and masks (`& 1`) directly into the buffer, and write out the result. This achieves zero heap allocations.

2. **What if the date format is flexible (e.g., `"dd/mm/yyyy"`, Unix timestamps, or ISO 8601 with timezones)?**
   - *Answer:* Introduce an input validation/parsing layer using a standardized date parser (like `datetime.strptime` or regex pattern matching) to normalize into a uniform internal representation (e.g., a tuple `(year, month, day)` or standard Unix epoch) before applying the binary formatting logic.
