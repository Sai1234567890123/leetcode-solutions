# 2882. Drop Duplicate Rows

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/drop-duplicate-rows/](https://leetcode.com/problems/drop-duplicate-rows/)  
**Topics:** 

---

## 📝 Problem Statement

```

DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+

```

There are some duplicate rows in the DataFrame based on the `email` column.

Write a solution to remove these duplicate rows and keep only the **first** occurrence.

The result format is in the following example.

 
```

Example 1:
**Input:**
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
**Output: ** 
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
**Explanation:**
Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.

```

---

## 💻 Implementation (python3)

```py
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows based on the 'email' column, keeping the first occurrence.
    
    :param customers: pd.DataFrame containing customer details.
    :return: pd.DataFrame with duplicate emails removed.
    """
    # drop_duplicates with subset=['email'] identifies duplicates strictly on the email column.
    # keep='first' ensures that the first occurrence is retained (default behavior).
    return customers.drop_duplicates(subset=['email'], keep='first')
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
In data processing and relational data systems, deduplicating records based on a natural unique key (such as an email address) is a routine operation. 

Pandas provides a high-performance vector-optimized method: `DataFrame.drop_duplicates()`.
- The `subset` parameter allows us to specify which column(s) should be used to evaluate uniqueness. Here, `subset=['email']`.
- The `keep` parameter dictates which duplicate to retain. The problem explicitly specifies keeping the **first** occurrence, which aligns with `keep='first'` (the default value in pandas).

### Step-by-Step Approach
1. Call `.drop_duplicates()` on the `customers` DataFrame.
2. Pass `subset=['email']` so that uniqueness is determined only by the `email` column, ignoring differences in `customer_id` or `name`.
3. Explicitly set `keep='first'` to make the intent clear and production-ready.
4. Return the resulting DataFrame.

### Complexity Analysis
- **Time Complexity:** $O(N)$ on average, where $N$ is the number of rows in the DataFrame. Under the hood, Pandas uses a C-optimized hash table (via `khash`) to track observed values in the specified column subset.
- **Space Complexity:** $O(N)$ in the worst case to store the hash table of seen emails and create the resulting filtered DataFrame. (If modifying in-place with `inplace=True`, memory overhead drops, but returning a new DataFrame is standard for pure functions).

### Common Pitfalls / Mistakes Candidates Make
1. **Omitting `subset`:** Calling `customers.drop_duplicates()` without parameters checks for duplicates across *all* columns. In this problem, `customer_id` is unique across rows, so failing to specify `subset=['email']` results in no rows being dropped.
2. **Mutating In-Place Incorrectly:** Running `customers.drop_duplicates(..., inplace=True)` and returning it returns `None`, which fails tests and causes bugs.
3. **Index Inconsistencies:** Depending on downstream expectations, some pipelines require resetting the index using `.reset_index(drop=True)`. However, LeetCode's Pandas runner expects the original indices preserved unless specified.
4. **Case Sensitivity:** In production systems, emails are often case-insensitive (`John@example.com` vs `john@example.com`). If not normalized beforehand, standard hash-based deduplication will treat them as distinct.

### Real Interview Follow-Up Questions & Answers

#### 1. What if the dataset is 500 GB and does not fit into RAM?
- **Chunking (Pandas):** Process the data in chunks (`pd.read_csv(..., chunksize=...)`), maintaining a global Bloom Filter or a Redis/RocksDB set of seen email hashes.
- **Distributed Processing:** Use Apache Spark (`df.dropDuplicates(["email"])`) or Polars with lazy streaming (`pl.scan_csv(...).unique(subset=["email"], keep="first")`). Spark will partition by the hash of the email and execute local deduplication per partition.

#### 2. How should we handle case-insensitivity or whitespace padding?
- Normalize before deduplicating:
  ```python
  customers['email_clean'] = customers['email'].str.strip().str.lower()
  customers = customers.drop_duplicates(subset=['email_clean'], keep='first').drop(columns=['email_clean'])
  ```

#### 3. How do you handle streaming data where emails arrive continuously?
- In a real-time event-streaming architecture (e.g., Apache Flink or Kafka Streams), use a state store (e.g., RocksDB-backed state) with a Time-To-Live (TTL) to deduplicate incoming events over a sliding or tumbling time window.
