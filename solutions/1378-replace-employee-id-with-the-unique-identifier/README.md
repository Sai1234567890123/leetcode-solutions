# 1378. Replace Employee ID With The Unique Identifier

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Employees`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.

```

 

Table: `EmployeeUNI`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.

```

 

Write a solution to show the **unique ID **of each user, If a user does not have a unique ID replace just show `null`.

Return the result table in **any** order.

The result format is in the following example.

 
Example 1:

```

**Input:** 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
**Output:** 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
**Explanation:** 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.

```

---

## 💻 Implementation (python3)

```py
SELECT 
    eu.unique_id, 
    e.name
FROM 
    Employees AS e
LEFT JOIN 
    EmployeeUNI AS eu 
ON 
    e.id = eu.id;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem requires returning the unique identifier (`unique_id`) alongside each employee's `name`. Crucially, if an employee does not have a corresponding entry in `EmployeeUNI`, the result should still include the employee with a `null` value for `unique_id`. 

This is the canonical definition of a `LEFT OUTER JOIN` (or simply `LEFT JOIN`):
- The `Employees` table serves as the primary/left table to ensure every single employee is retained in the output.
- The `EmployeeUNI` table is joined on the matching attribute `id`.
- Unmatched rows in `Employees` will automatically yield `NULL` for columns originating from `EmployeeUNI`.

### Step-by-Step Approach
1. Designate `Employees` as the left table (aliased as `e`) so no employees are filtered out.
2. Perform a `LEFT JOIN` with `EmployeeUNI` (aliased as `eu`) matching on `e.id = eu.id`.
3. Select `eu.unique_id` and `e.name` in the `SELECT` list as specified by the problem schema.

### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N + M)$ on average, where $N$ is the number of rows in `Employees` and $M$ is the number of rows in `EmployeeUNI`. Since `id` is a primary key (indexed) in both tables, the query optimizer performs an index lookup for each row of `Employees`, resulting in optimal $\mathcal{O}(N \log M)$ or $\mathcal{O}(N)$ lookup performance depending on the join algorithm (e.g., Index Nested Loop Join or Hash Join).
- **Space Complexity:** $\mathcal{O}(N)$ auxiliary space required to buffer/stream the resulting dataset back to the client.

### Common Pitfalls / Mistakes Candidates Make
1. **Using an `INNER JOIN`:** Using `INNER JOIN` or implicit joins via `WHERE e.id = eu.id` will drop employees who don't have an entry in `EmployeeUNI` (such as Alice and Bob in Example 1).
2. **Reversing the Join Direction:** Performing `EmployeeUNI LEFT JOIN Employees` will drop employees that do not exist in `EmployeeUNI`.
3. **Ambiguous Column Names:** Forgetting to qualify column names when joining tables with identically named columns (like `id`).

### Real Interview Follow-Up Questions & Answers

#### 1. What if `EmployeeUNI` contains multiple `unique_id`s for a single `id` (1-to-many relationship)?
- **Issue:** A standard `LEFT JOIN` would duplicate rows for an employee who has multiple unique IDs.
- **Solution:** Clarify business requirements. If only one ID is needed (e.g., the latest or smallest), use a window function or aggregation:
  ```sql
  SELECT 
      MIN(eu.unique_id) AS unique_id,
      e.name
  FROM Employees e
  LEFT JOIN EmployeeUNI eu ON e.id = eu.id
  GROUP BY e.id, e.name;
  ```

#### 2. How does the database engine optimize this query at scale (e.g., 100M+ rows)?
- **Indexes:** Ensure an index exists on `EmployeeUNI(id)`. Since `(id, unique_id)` is a composite primary key with `id` as the leading column, an index is already present (B-tree index in InnoDB).
- **Join Strategy:** For large datasets where neither table fits entirely into memory, the optimizer may choose a **Hash Join** (if supported, e.g., MySQL 8.0.18+) or a **Block Nested Loop / Sort-Merge Join**.

#### 3. How would you handle this at distributed scale (e.g., Sharded databases / BigQuery / Spark)?
- If data is distributed across nodes, joining on `id` can cause network shuffles unless both tables are co-located (sharded/partitioned by `id`). 
- Ensuring both tables use `id` as the distribution/partition key eliminates data shuffling over the network (colocated join / map-side join).
