# 2194. Cells in a Range on an Excel Sheet

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/](https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/)  
**Topics:** String

---

## 📝 Problem Statement

A cell `(r, c)` of an excel sheet is represented as a string `""` where:

	`` denotes the column number `c` of the cell. It is represented by **alphabetical letters**.

	
		- For example, the `1st` column is denoted by `'A'`, the `2nd` by `'B'`, the `3rd` by `'C'`, and so on.

	
	
	- `` is the row number `r` of the cell. The `rth` row is represented by the **integer** `r`.

You are given a string `s` in the format `":"`, where `` represents the column `c1`, `` represents the row `r1`, `` represents the column `c2`, and `` represents the row `r2`, such that `r1 

Return *the **list of cells*** `(x, y)` *such that* `r1 

 
Example 1:

```

**Input:** s = "K1:L2"
**Output:** ["K1","K2","L1","L2"]
**Explanation:**
The above diagram shows the cells which should be present in the list.
The red arrows denote the order in which the cells should be presented.

```

Example 2:

```

**Input:** s = "A1:F1"
**Output:** ["A1","B1","C1","D1","E1","F1"]
**Explanation:**
The above diagram shows the cells which should be present in the list.
The red arrow denotes the order in which the cells should be presented.

```

 
**Constraints:**

	- `s.length == 5`

	- `'A'

---

## 💻 Implementation (python3)

```py
class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        # Unpack indices based on the fixed format "<col1><row1>:<col2><row2>"
        c1, r1 = s[0], int(s[1])
        c2, r2 = s[3], int(s[4])
        
        result = []
        
        # Outer loop iterates through columns alphabetically from c1 to c2
        for col_code in range(ord(c1), ord(c2) + 1):
            col_char = chr(col_code)
            # Inner loop iterates through rows numerically from r1 to r2
            for row in range(r1, r2 + 1):
                result.append(f"{col_char}{row}")
                
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for all cell coordinates in a rectangular grid bounded by two corner cells, `c1r1` and `c2r2`.
The output order specified by the problem is column-by-column:
- We iterate through columns from `c1` to `c2`.
- Within each column, we iterate through rows from `r1` to `r2`.

Given the input format is strictly fixed (`s.length == 5`), we can parse:
- `c1 = s[0]`, `r1 = int(s[1])`
- `c2 = s[3]`, `r2 = int(s[4])`

We then use two nested loops: the outer loop advances ASCII values of characters from `ord(c1)` to `ord(c2)`, and the inner loop iterates from integer `r1` to `r2`.

### Step-by-Step Approach

1. Extract column characters `s[0]`, `s[3]` and integer row values `int(s[1])`, `int(s[4])`.
2. Initialize an empty list `result`.
3. Loop over integer ASCII codes from `ord(c1)` up to `ord(c2)` (inclusive).
4. For each column character `chr(col_code)`, loop over row numbers from `r1` to `r2` (inclusive).
5. Append the formatted cell string `f"{col_char}{row}"` to `result`.
6. Return `result`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}((c_2 - c_1 + 1) \times (r_2 - r_1 + 1))$. Since there are at most $26$ letters ('A' through 'Z') and at most $9$ single-digit rows ('1' through '9'), the maximum number of cells is $26 \times 9 = 234$. Thus, the time complexity is bounded by $\mathcal{O}(1)$ runtime in practice.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The output list requires $\mathcal{O}(K)$ space where $K$ is the number of cells in the range (at most $234$).

### Common Pitfalls / Mistakes

1. **Ordering Inversion:** Iterating rows in the outer loop and columns in the inner loop (row-major vs column-major). The problem requires traversing down each column before moving to the next column.
2. **Inclusive Range Bounds:** Forgetting `+ 1` in Python's `range()` function, which excludes the upper bound by default.
3. **Hardcoding Delimiter Index:** Assuming variable lengths without checking constraints. While here `len(s) == 5` is guaranteed, in more generalized problems multi-character column names (like `AA`) and multi-digit row numbers (like `100`) must be split by `':'` dynamically.

### Real Interview Follow-Up Questions

1. **Follow-Up 1: What if columns can exceed 'Z' (e.g., "A1:AA10" or "Z99:AAA105")?**
   - *Answer:* We convert base-26 bijective Excel column strings to integers (similar to LeetCode 171: Excel Sheet Column Number) and vice versa (LeetCode 168: Excel Sheet Column Title). We parse the input by splitting on `':'` and using regular expressions or pointer scanning to separate letters and digits. We then iterate from `start_col_int` to `end_col_int`.

2. **Follow-Up 2: What if the range is extremely large and cannot fit into memory (e.g., millions of cells)?**
   - *Answer:* Instead of materializing the entire list into memory, return a generator or stream (`yield f"{col_char}{row}"`). This reduces the space complexity to $\mathcal{O}(1)$ memory regardless of range size.

3. **Follow-Up 3: What if cells must be processed concurrently across multiple workers?**
   - *Answer:* Partition the total number of columns (or cells) across worker threads or distributed nodes. Since each cell coordinate is independent, worker $i$ can process column range $[c_{start_i}, c_{end_i}]$ without synchronization until final aggregation.
