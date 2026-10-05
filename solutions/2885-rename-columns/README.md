# 2885. Rename Columns

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/rename-columns/](https://leetcode.com/problems/rename-columns/)  
**Topics:** 

---

## 📝 Problem Statement

```

DataFrame `students`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+

```

Write a solution to rename the columns as follows:

	- `id` to `student_id`

	- `first` to `first_name`

	- `last` to `last_name`

	- `age` to `age_in_years`

The result format is in the following example.

 
```

Example 1:
Input:
+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+
**Output:**
+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
+------------+------------+-----------+--------------+
**Explanation:** 
The column names are changed accordingly.
```

---

## 💻 Implementation (python3)

```py
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    Renames specific columns of the students DataFrame according to the mapping specifications.
    """
    # Mapping old column names to new column names
    column_mapping = {
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }
    
    # rename() creates a view/copy with updated column metadata without copying underlying data blocks
    return students.rename(columns=column_mapping)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The task requires mapping existing column names in a pandas DataFrame to new, more descriptive names. In pandas, `DataFrame.rename()` is the standard and idiomatic tool for this operation. It takes a dictionary mapping `{old_column_name: new_column_name}`.

Alternative approaches like directly assigning to `df.columns` (e.g., `students.columns = [...]`) are brittle because they depend on the exact order and number of columns remaining constant. Using `df.rename(columns=...)` is declarative, robust to column ordering, and ignores any unspecified columns safely.

### Step-by-Step Approach
1. Define a dictionary mapping existing column names to their target names:
   - `'id'` $\rightarrow$ `'student_id'`
   - `'first'` $\rightarrow$ `'first_name'`
   - `'last'` $\rightarrow$ `'last_name'`
   - `'age'` $\rightarrow$ `'age_in_years'`
2. Call `students.rename(columns=column_mapping)` and return the resulting DataFrame.

### Complexity Analysis
- **Time Complexity:** $O(C)$, where $C$ is the number of columns in the DataFrame. The underlying data arrays/blocks are not copied; only the index/metadata representing the column names is modified. Since $C = 4$ is a small constant, this runs in $O(1)$ time.
- **Space Complexity:** $O(C)$ auxiliary space to allocate the new index metadata and dictionary mapping. In terms of memory consumption, underlying data blocks are shared (copy-on-write or shallow copy depending on the pandas version), so space complexity is $O(1)$.

### Common Pitfalls / Mistakes
1. **Direct list assignment (`df.columns = [...]`)**:
   - If the incoming DataFrame has extra columns or columns in a different order, direct assignment silently mislabels or raises a `ValueError: Length mismatch`.
2. **Mutating inplace vs. Returning**:
   - Forgetting to return the result when using `students.rename(...)` without `inplace=True`.
   - Using `inplace=True` is generally discouraged in modern pandas (and deprecated in future directions) because it can prevent method chaining and often does not actually provide performance benefits due to internal copy semantics.

### Real Interview Follow-Up Questions & Answers

1. **How does column renaming behave under pandas Copy-on-Write (CoW)?**
   - *Answer:* Under Copy-on-Write (standard in pandas 2.0+), renaming columns creates a new DataFrame whose internal block manager references the same underlying NumPy arrays as the original DataFrame. No deep copy of row data occurs until a column's values are mutated.

2. **What if column names are generated dynamically (e.g., prefixing all columns or converting camelCase to snake_case)?**
   - *Answer:* Instead of a dictionary, `rename()` can take a function or lambda:
     ```python
     students.rename(columns=lambda col: f"student_{col}")
     # or string methods
     students.rename(columns=str.lower)
     ```

3. **How would you handle this operation on a distributed/massive dataset (e.g., PySpark or Polars)?**
   - *Answer:* 
     - In **PySpark**: You can use `df.withColumnRenamed("old", "new")` (chained) or `df.toDF(*new_cols)` if replacing all columns. In modern Spark (3.4+), `df.withColumnsRenamed(mapping_dict)` is available.
     - In **Polars**: `df.rename(mapping_dict)` operates in $O(1)$ metadata time, similar to pandas.
