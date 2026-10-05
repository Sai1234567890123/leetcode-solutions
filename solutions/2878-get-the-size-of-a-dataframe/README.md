# 2878. Get the Size of a DataFrame

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/get-the-size-of-a-dataframe/](https://leetcode.com/problems/get-the-size-of-a-dataframe/)  
**Topics:** 

---

## 📝 Problem Statement

```

DataFrame `players:`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+

```

Write a solution to calculate and display the **number of rows and columns** of `players`.

Return the result as an array:

`[number of rows, number of columns]`

The result format is in the following example.

 
Example 1:

```

Input:
+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+
Output:
[10, 5]
**Explanation:**
This DataFrame contains 10 rows and 5 columns.

```

---

## 💻 Implementation (python3)

```py
import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    """
    Returns the number of rows and columns of the input DataFrame as a list [rows, columns].
    
    `players.shape` returns a tuple (n_rows, n_columns) in O(1) time.
    We convert this tuple directly to a list to match the return type specification.
    """
    return list(players.shape)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

In pandas, every `DataFrame` object maintains metadata about its dimensions. The attribute `df.shape` returns a Python tuple containing the dimensionality in the form `(number of rows, number of columns)`. 

Rather than computing the length of the DataFrame `len(df)` and the number of columns `len(df.columns)` independently, accessing the `.shape` attribute provides an instantaneous, cached lookup. Converting this tuple into a list satisfies the required return type signature `List[int]`.

### Step-by-Step Approach

1. Access the `shape` property on the `players` DataFrame, which gives `(num_rows, num_cols)`.
2. Wrap the resulting tuple in `list(...)` to convert `(rows, cols)` to `[rows, cols]`.
3. Return the list.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$  
  The `.shape` attribute is pre-computed and stored in memory as part of the DataFrame's metadata block. Querying it and casting a 2-element tuple to a list takes strict constant time, irrespective of whether the DataFrame has $10$ rows or $10^8$ rows.
  
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space  
  A fixed-size list with exactly 2 integers is allocated, requiring constant additional memory.

### Common Pitfalls / Mistakes Candidates Make

1. **Iterating Through the DataFrame:** Counting rows or columns via iteration (e.g., iterating through `iterrows()` or `itertuples()`) degrades an $\mathcal{O}(1)$ metadata access into an $\mathcal{O}(N)$ operation with massive overhead.
2. **Confusing `.size` with `.shape`:** In pandas, `df.size` returns the total number of elements ($rows \times columns$), not the dimensions.
3. **Missing the Return Type:** `df.shape` returns a `tuple` (e.g., `(10, 5)`), while the problem asks for a list `[10, 5]`. Forgetting the `list()` cast may cause type assertion errors in strict test runners.
4. **Handling Empty DataFrames:** An empty DataFrame with pre-defined columns (e.g., 0 rows, 5 columns) will correctly return `[0, 5]` using `list(df.shape)`. Manually doing conditional checks can introduce unnecessary edge-case bugs.

### Real Interview Follow-Up Questions & Answers

#### 1. What if the dataset does not fit into memory (e.g., a 100 GB CSV or Parquet file)?
- **Answer:** If we only need the dimensions without loading the entire dataset into RAM:
  - **Parquet:** Read metadata only using `pyarrow.parquet.read_metadata(file_path)`. The Parquet file footer stores `num_rows` and `num_columns` directly, achieving $\mathcal{O}(1)$ time and memory without scanning data.
  - **CSV:** Stream the file in chunks using `pd.read_csv(file_path, chunksize=N)` and aggregate `sum(chunk.shape[0] for chunk in reader)`, reading the column count once from the first chunk. Alternatively, count newline characters via memory-mapped file (`mmap`) or command-line utilities like `wc -l`.

#### 2. How does Pandas track DataFrame dimensions under the hood?
- **Answer:** A pandas DataFrame is powered by a `BlockManager` (or `ArrayManager` in newer versions). It maintains an axis indexing system: `axes[0]` represents the `Index` (rows) and `axes[1]` represents the columns `Index`. The `.shape` property simply returns `(len(self.index), len(self.columns))`, which are tracked internally and updated only when data is mutated.

#### 3. How do distributed data engines (like PySpark or Dask) handle getting the size?
- **Answer:** In PySpark or Dask, DataFrames are lazily evaluated across partitions. 
  - Column count is cheap ($\mathcal{O}(1)$) because the schema is known upfront (`len(df.columns)`).
  - Row count (`df.count()`) is an **action** requiring an $\mathcal{O}(N)$ scan/shuffle across all worker nodes to count records per partition unless cached or backed by a metadata-aware format (e.g., Delta Lake or Parquet).
