# 2888. Reshape Data: Concatenate

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/reshape-data-concatenate/](https://leetcode.com/problems/reshape-data-concatenate/)  
**Topics:** 

---

## 📝 Problem Statement

```

DataFrame `df1`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

DataFrame `df2`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

```

Write a solution to concatenate these two DataFrames **vertically** into one DataFrame.

The result format is in the following example.

 
Example 1:

```

Input:
df1
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
+------------+---------+-----+
df2
+------------+------+-----+
| student_id | name | age |
+------------+------+-----+
| 5          | Leo  | 7   |
| 6          | Alex | 7   |
+------------+------+-----+
**Output:**
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
| 5          | Leo     | 7   |
| 6          | Alex    | 7   |
+------------+---------+-----+
Explanation:
The two DataFramess are stacked vertically, and their rows are combined.
```

---

## 💻 Implementation (python3)

```py
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Concatenate the two DataFrames vertically (stacking rows).
    # axis=0 specifies vertical concatenation (along rows).
    # ignore_index=True resets the index of the resulting DataFrame to a default integer index (0, 1, 2, ...),
    # which is often desired when combining tables and prevents duplicate index values from the original DataFrames.
    result_df = pd.concat([df1, df2], axis=0, ignore_index=True)
    return result_df
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to combine two pandas DataFrames, `df1` and `df2`, by stacking them on top of each other. This operation is commonly known as "vertical concatenation" or "union all" in SQL terms. Pandas, being a powerful data manipulation library, provides a dedicated and highly optimized function for this exact purpose: `pd.concat()`.

My thought process was:
1.  **Identify the core operation:** The request is to combine rows from two DataFrames.
2.  **Recall pandas functionality:** The `pd.concat()` function is the primary tool for combining pandas objects (Series or DataFrames) along an axis.
3.  **Determine the axis:** "Vertically" means stacking rows, which corresponds to `axis=0` in pandas (the default behavior for `pd.concat`).
4.  **Consider index handling:** When stacking DataFrames, the original indices might overlap or not be meaningful in the combined DataFrame. The example output implies a fresh, sequential index. Therefore, `ignore_index=True` is a good practice to ensure the resulting DataFrame has a clean, new integer index starting from 0.
5.  **Formulate the call:** Combine these elements into `pd.concat([df1, df2], axis=0, ignore_index=True)`.

## Step-by-Step Approach

1.  **Import pandas:** Ensure `pandas` is imported, which is already part of the starter code.
2.  **Call `pd.concat()`:** Use the `pd.concat()` function.
3.  **Provide DataFrames as a list:** Pass `df1` and `df2` as a list `[df1, df2]` to the first argument of `pd.concat()`. This tells pandas which objects to concatenate.
4.  **Specify `axis=0`:** Although `axis=0` is the default for `pd.concat`, explicitly stating it improves readability and clarifies intent for vertical concatenation.
5.  **Set `ignore_index=True`:** This crucial parameter ensures that the resulting DataFrame has a new, clean integer index (0, 1, 2, ...) rather than retaining the potentially duplicate or non-sequential indices from the original `df1` and `df2`.
6.  **Return the result:** The function returns the newly created concatenated DataFrame.

## Complexity Analysis

*   **Time Complexity:** `O((R1 + R2) * C)`
    *   Where `R1` is the number of rows in `df1`, `R2` is the number of rows in `df2`, and `C` is the number of columns (assuming both DataFrames have the same number of columns, which is typical for vertical concatenation).
    *   The `pd.concat` operation essentially involves copying all data from both input DataFrames into a new DataFrame. This requires iterating through all elements of both DataFrames. Therefore, the time taken is proportional to the total number of elements in the combined DataFrame. This is the optimal time complexity because every piece of data must be processed and copied.

*   **Space Complexity:** `O((R1 + R2) * C)`
    *   A new DataFrame is created to store the combined data. This new DataFrame will have `R1 + R2` rows and `C` columns.
    *   Therefore, the space required is proportional to the size of the resulting DataFrame. This is optimal as the problem requires producing a new DataFrame containing all the data.

## Common Pitfalls / Mistakes

1.  **Forgetting `ignore_index=True`**: If `ignore_index` is not set to `True` (its default is `False`), the resulting DataFrame will retain the original indices from `df1` and `df2`. If both DataFrames have, for example, indices `0, 1, 2`, the concatenated DataFrame will have duplicate index values, which can lead to unexpected behavior when using index-based operations (e.g., `.loc[]`).
2.  **Incorrect `axis` parameter**: Using `axis=1` would attempt to concatenate the DataFrames horizontally (side-by-side), which is not what the problem asks for. While `axis=0` is the default, explicitly stating it is good practice.
3.  **Assuming identical columns**: While the problem example implies identical column structures, in real-world scenarios, `df1` and `df2` might have different columns. `pd.concat` with `axis=0` and default `join='outer'` will handle this by taking the union of all columns and filling missing values with `NaN`. If only common columns are desired, `join='inner'` would be needed.
4.  **Using `df1.append(df2)` (deprecated)**: Older pandas versions had a `DataFrame.append()` method. While it achieved vertical concatenation, it was less efficient than `pd.concat()` for multiple DataFrames and has been deprecated since pandas 1.4.0, with removal planned in a future version. `pd.concat()` is the recommended approach.

## Real Interview Follow-Up Questions

1.  **What if the DataFrames have different columns?**
    *   **Answer:** `pd.concat` handles this by default using `join='outer'`. This means it will take the union of all column names from both DataFrames. Columns present in one DataFrame but not the other will be filled with `NaN` (Not a Number) values in the rows originating from the DataFrame that lacked that column. If you only wanted to keep columns common to both DataFrames, you would specify `join='inner'`.

2.  **How would you handle this if you couldn't use `pd.concat` (e.g., if you were implementing it from scratch or in a language without a direct equivalent)?**
    *   **Answer:** You would typically convert each DataFrame into a more basic data structure, like a list of dictionaries (where each dictionary represents a row) or a list of lists. Then, you would append the rows from the second DataFrame's list to the first DataFrame's list. Finally, you would construct a new DataFrame (or equivalent table structure) from this combined list. This is essentially what `pd.concat` does internally, but optimized in C for performance.

3.  **What if the DataFrames are very large and cannot fit into memory simultaneously?**
    *   **Answer:** This is a common "big data" challenge.
        *   **Chunking/Streaming:** If the data originates from files (e.g., CSV), you could read `df1` in chunks, process each chunk, and write it to a temporary output file. Then, read `df2` in chunks, process each chunk, and *append* it to the same temporary output file. This way, only a portion of the data is in memory at any given time.
        *   **Distributed Computing:** For truly massive datasets, you would use distributed computing frameworks like Apache Spark or Dask. These frameworks are designed to handle data that exceeds the memory capacity of a single machine by distributing the data and computation across a cluster. In Spark, you'd use `union()` or `unionAll()` on Spark DataFrames.
        *   **Database Solutions:** If the data is stored in a database, the most efficient approach is to perform the concatenation directly in the database using SQL's `UNION ALL` operator. Databases are optimized for large-scale data operations.

4.  **What if the order of rows matters?**
    *   **Answer:** `pd.concat` preserves the order of the input DataFrames and the internal order of rows within each DataFrame. `df1`'s rows will appear first, followed by `df2`'s rows, in their original relative order. If a specific sorting is required after concatenation (e.g., by `student_id` or `age`), an additional `result_df.sort_values(by='column_name')` operation would be needed.

5.  **How would you ensure data types are consistent after concatenation, especially if columns have different types in `df1` and `df2` (e.g., 'age' is `int` in `df1` but `float` in `df2` due to `NaN`s)?**
    *   **Answer:** Pandas `pd.concat` will automatically perform type promotion (upcasting) to accommodate all values in a column. For example, if a column named 'value' is `int64` in `df1` and `float64` in `df2`, the resulting 'value' column in the concatenated DataFrame will be `float64`. If one column is numeric and the other is a string, it might become an `object` (string) type.
    *   To ensure specific data types, you should inspect the `dtypes` of the resulting DataFrame (`result_df.dtypes`). If necessary, you can explicitly cast columns using the `.astype()` method after concatenation (e.g., `result_df['age'] = result_df['age'].astype('int64')`). For numerical columns that might contain `NaN`s, pandas 1.0+ introduced nullable integer dtypes (e.g., `Int64` with a capital 'I') which can store `NaN`s while maintaining an integer type, preventing automatic conversion to float.
