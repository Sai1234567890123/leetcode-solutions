# 2886. Change Data Type

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/change-data-type/](https://leetcode.com/problems/change-data-type/)  
**Topics:** 

---

## 📝 Problem Statement

```

DataFrame `students`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+

```

Write a solution to correct the errors:

The `grade` column is stored as floats, convert it to integers.

The result format is in the following example.

 
```

Example 1:
Input:
DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
Output:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
+------------+------+-----+-------+
**Explanation:** 
The data types of the column grade is converted to int.
```

---

## 💻 Implementation (python3)

```py
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # Cast the 'grade' column from float to standard integer type
    students['grade'] = students['grade'].astype(int)
    return students
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
In pandas, columns are represented by `Series`, which have an underlying NumPy array or pandas ExtensionArray with a specific data type (`dtype`). 

To convert the data type of an existing column, the idiomatic and most efficient approach is the `.astype()` method. Casting `students['grade']` to `int` converts the float values to 64-bit or 32-bit integers (depending on platform defaults), truncating any decimal portions (e.g., `73.0` becomes `73`).

### Step-by-Step Approach
1. Access the `grade` column using dictionary-style indexing: `students['grade']`.
2. Apply `.astype(int)` to convert the float representations to integers.
3. Reassign the result back to `students['grade']` to update the DataFrame in-place without copying unrelated columns.
4. Return the modified `students` DataFrame.

### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of rows in the DataFrame. Every element in the column must be converted to an integer.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space if updated in place, or $\mathcal{O}(N)$ temporary space to allocate the new integer array for the column during the type conversion.

### Common Pitfalls / Mistakes Candidates Make
1. **Handling `NaN` / Missing Values:**
   - Standard NumPy `int` (`int32` / `int64`) cannot represent `NaN` (Not a Number). If the column contains missing values, casting with `.astype(int)` will raise a `ValueError: Cannot convert non-finite values (NA or inf) to integer`.
   - In production scenarios where missing values can exist, pandas' nullable integer type (`'Int64'`, capitalized) should be used instead: `students['grade'].astype('Int64')`.
2. **Chained Indexing Warnings:**
   - Using `students.grade = ...` or chained indexing can trigger pandas' `SettingWithCopyWarning`. Using explicit column assignment `students['grade'] = ...` avoids this.
3. **Rounding vs. Truncation:**
   - Note that `.astype(int)` truncates floating point numbers (e.g., `73.9` becomes `73`). If rounding is required prior to casting, `.round().astype(int)` must be called.

### Real Interview Follow-Up Questions

#### 1. What if the dataset has millions of rows and memory is constrained?
- **Answer:** Use smaller integer types based on the range of values. For grades (typically $0$ to $100$), an 8-bit unsigned integer `np.uint8` or `np.int8` takes only 1 byte per row, compared to 8 bytes for standard 64-bit integers.
  ```python
  students['grade'] = students['grade'].astype('int8')
  ```

#### 2. How do you handle non-numeric dirty data (e.g., string characters like `"A+"`, `""`, or `"N/A"`)?
- **Answer:** Use `pd.to_numeric` with `errors='coerce'`, which replaces unparseable strings with `NaN`, followed by either filling with a default value (`.fillna(0)`) or converting to nullable integer `'Int64'`:
  ```python
  students['grade'] = (
      pd.to_numeric(students['grade'], errors='coerce')
      .fillna(0)
      .astype(int)
  )
  ```

#### 3. How would you do this across multiple columns simultaneously?
- **Answer:** Pass a dictionary to `DataFrame.astype()`:
  ```python
  students = students.astype({'grade': int, 'age': int})
  ```
