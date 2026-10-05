# 2889. Reshape Data: Pivot

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/reshape-data-pivot/](https://leetcode.com/problems/reshape-data-pivot/)  
**Topics:** 

---

## 📝 Problem Statement

```

DataFrame `weather`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| city        | object |
| month       | object |
| temperature | int    |
+-------------+--------+

```

Write a solution to **pivot** the data so that each row represents temperatures for a specific month, and each city is a separate column.

The result format is in the following example.

 
```

Example 1:
**Input:**
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+
**Output:**
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
+----------+--------+--------------+
Explanation:
The table is pivoted, each column represents a city, and each row represents a specific month.
```

---

## 💻 Implementation (python3)

```py
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Pivots the weather DataFrame so that each row represents a month,
    and each unique city becomes a column with temperature values.
    """
    # Use pandas pivot method:
    # - index: column to become the new DataFrame's index (rows)
    # - columns: column to be reshaped into new column headers
    # - values: column to populate the cell values
    return weather.pivot(index='month', columns='city', values='temperature')
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to reshape a long-format DataFrame (where each observation is a row containing `city`, `month`, and `temperature`) into a wide-format DataFrame (where months are rows, cities are columns, and temperatures fill the matrix).

In pandas, the idiomatic and most performant operation for reshaping data from long to wide format based on unique index/column pairs is `DataFrame.pivot()`.

### Step-by-Step Approach

1. **Identify the axes**:
   - Row axis (`index`): `'month'`
   - Column axis (`columns`): `'city'`
   - Cell values (`values`): `'temperature'`
2. **Execute `weather.pivot(...)`**:
   - `index='month'`: Groups records by month along the vertical axis.
   - `columns='city'`: Creates a distinct column for every unique city found.
   - `values='temperature'`: Populates the intersections with their corresponding temperature values.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of rows in the `weather` DataFrame. Under the hood, pandas builds hash tables for the unique index and column values and distributes the values into the target 2D array.
- **Space Complexity:** $\mathcal{O}(U_{\text{months}} \times U_{\text{cities}})$, where $U_{\text{months}}$ is the number of unique months and $U_{\text{cities}}$ is the number of unique cities. This is the exact memory required to store the resulting wide-format matrix.

### Common Pitfalls / Mistakes

1. **`pivot` vs `pivot_table`**:
   - `pivot()` requires that each `(index, columns)` pair is strictly unique. If there are duplicates (e.g., multiple temperature readings for Jacksonville in January), `pivot()` will raise a `ValueError: Index contains duplicate entries, cannot reshape`.
   - `pivot_table()` supports an aggregation function (`aggfunc='mean'`, `'sum'`, etc.) to resolve duplicate combinations. Since each city-month pair is guaranteed unique here, `pivot()` is faster and more memory-efficient.
2. **Unnecessary `reset_index()`**:
   - Candidates often instinctively chain `.reset_index()`. In LeetCode pandas problems representing tabular outputs with named index columns, retaining the pivoted index matches the expected output representation.

### Real Interview Follow-Up Questions & Answers

#### 1. What if there are duplicate entries for the same (month, city) pair?
**Answer:** Use `pivot_table` instead of `pivot` and provide an aggregation function:
```python
weather.pivot_table(index='month', columns='city', values='temperature', aggfunc='mean')
```
This aggregates multiple observations (e.g., taking the average, min, or max temperature).

#### 2. What if a city has missing data for a certain month?
**Answer:** By default, unobserved pairs will be populated with `NaN`. You can fill missing values either during pivoting (in `pivot_table(..., fill_value=...)`) or afterwards with `.fillna(...)`.

#### 3. How would you handle this at massive scale (e.g., Terabytes of sensor data)?
**Answer:**
- Standard pandas loads all data into memory in a single process.
- For out-of-core or distributed computing, use **PySpark** (`df.groupBy("month").pivot("city").agg(...)`) or **Polars / Dask**.
- When pivoting with a very large number of distinct column categories (e.g., millions of cities), the resulting matrix becomes extremely sparse, potentially causing memory explosion. In that scenario, keep the data in long format (relational) or use a sparse matrix representation (`scipy.sparse` / `scipy.sparse.coo_matrix`).
