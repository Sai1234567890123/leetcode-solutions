# 2890. Reshape Data: Melt

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/reshape-data-melt/](https://leetcode.com/problems/reshape-data-melt/)  
**Topics:** 

---

## 📝 Problem Statement

```

DataFrame `report`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| product     | object |
| quarter_1   | int    |
| quarter_2   | int    |
| quarter_3   | int    |
| quarter_4   | int    |
+-------------+--------+

```

Write a solution to **reshape** the data so that each row represents sales data for a product in a specific quarter.

The result format is in the following example.

 
Example 1:

```

Input:
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
**Output:**
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+
**Explanation:**
The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.

```

---

## 💻 Implementation (python3)

```py
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """
    Reshapes the DataFrame from wide to long format using pandas.melt.
    
    Parameters:
        report (pd.DataFrame): DataFrame containing product quarterly sales.
        
    Returns:
        pd.DataFrame: Reshaped DataFrame with columns ['product', 'quarter', 'sales'].
    """
    return report.melt(
        id_vars=['product'],
        value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
        var_name='quarter',
        value_name='sales'
    )
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks to convert data from a **wide format** (where each quarter has its own column) into a **long format** (where quarters become values in a single categorical column, and the corresponding values become a single metric column). 

In data manipulation with pandas, the canonical and most efficient operation for wide-to-long transformation is `pd.melt()` (or the DataFrame method `DataFrame.melt()`).

### Step-by-Step Approach

1. **Identify Identifier Variables (`id_vars`)**:
   - The column `product` identifies each entity that will stay as an identifier in the melted DataFrame.
2. **Identify Value Variables (`value_vars`)**:
   - The columns to unpivot are `quarter_1`, `quarter_2`, `quarter_3`, and `quarter_4`.
3. **Set Target Column Names**:
   - `var_name='quarter'`: Renames the variable column storing the original column headers.
   - `value_name='sales'`: Renames the value column storing the data values.
4. Pandas' `melt()` preserves the relative order of rows per variable by default, perfectly matching the desired output where all entries for `quarter_1` appear first, followed by `quarter_2`, and so forth.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \times K)$, where $N$ is the number of rows in the input DataFrame and $K$ is the number of unpivoted columns ($K = 4$). Every cell in the unpivoted columns is visited once and transferred to the new DataFrame.
- **Space Complexity:** $\mathcal{O}(N \times K)$ auxiliary space to allocate and return the newly reshaped DataFrame of size $(N \times K) \times 3$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Confusing `melt` with `pivot` / `pivot_table`**:
   - `pivot` reshapes from **long to wide**.
   - `melt` reshapes from **wide to long**.
2. **Forgetting Column Renaming**:
   - Leaving default column names (`variable` and `value`) instead of renaming them to `quarter` and `sales`.
3. **Using Iterative Approaches**:
   - Using `iterrows()` or list comprehensions to build the long table manually. This introduces significant Python interpreter overhead and fails vectorization benchmarks in real production environments.

---

### Real Interview Follow-Up Questions

#### 1. What if there are hundreds of quarters or dynamic quarterly columns?
**Answer:** Instead of hardcoding `value_vars=['quarter_1', ...]`, dynamically filter columns:
```python
quarter_cols = [col for col in report.columns if col.startswith('quarter_')]
return report.melt(id_vars=['product'], value_vars=quarter_cols, var_name='quarter', value_name='sales')
```
Or simply omit `value_vars` if all other columns aside from `id_vars` should be melted.

#### 2. How would you handle this if the DataFrame does not fit into memory (e.g., 50GB dataset)?
**Answer:**
- **Chunking:** Read and process the data in chunks using `pd.read_csv(..., chunksize=100_000)` and melt each chunk individually before streaming the output to disk/database.
- **Dask / Polars:** Use Polars (via lazy execution `pl.LazyFrame.unpivot()`) or Dask (`dd.melt()`) which provide out-of-core and parallel processing capabilities with significantly lower memory footprints.

#### 3. How do you reverse this operation?
**Answer:** Use `pivot`:
```python
df.pivot(index='product', columns='quarter', values='sales').reset_index()
```
