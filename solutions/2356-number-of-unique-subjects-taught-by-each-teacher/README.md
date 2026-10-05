# 2356. Number of Unique Subjects Taught by Each Teacher

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Teacher`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.

```

 

Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in **any order**.

The result format is shown in the following example.

 
Example 1:

```

**Input:** 
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
**Output:**  
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
**Explanation:** 
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.

```

---

## 💻 Implementation (python3)

```py
SELECT 
    teacher_id, 
    COUNT(DISTINCT subject_id) AS cnt
FROM 
    Teacher
GROUP BY 
    teacher_id;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the number of unique subjects taught by each teacher. 
A single teacher (`teacher_id`) can teach the same subject (`subject_id`) across multiple departments (`dept_id`), as observed in Example 1 where teacher `1` teaches subject `2` in both department `3` and department `4`.

To solve this:
1. Group records by each unique `teacher_id` using `GROUP BY teacher_id`.
2. For each group, count the unique instances of `subject_id` using the aggregate function `COUNT(DISTINCT subject_id)`.
3. Alias the aggregated column as `cnt` as requested in the output format.

### Step-by-Step Approach

1. **`SELECT teacher_id`**: Identify each teacher.
2. **`COUNT(DISTINCT subject_id) AS cnt`**: Count only distinct `subject_id` values per group, ignoring duplicates caused by multiple departments.
3. **`FROM Teacher`**: Query the target table.
4. **`GROUP BY teacher_id`**: Aggregate rows belonging to the same teacher.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ or $\mathcal{O}(N)$ depending on index availability and database engine execution strategy:
  - Without an index, the database scans the table ($\mathcal{O}(N)$) and uses a hash aggregation or sort-based aggregation ($\mathcal{O}(N)$ or $\mathcal{O}(N \log N)$) to group by `teacher_id` and compute distinct values.
  - With a composite index on `(teacher_id, subject_id)`, this operation can be satisfied directly via an index scan (Loose Index Scan / Skip Scan) in $\mathcal{O}(K)$ where $K$ is the number of unique `(teacher_id, subject_id)` pairs.
- **Space Complexity:** $\mathcal{O}(U)$, where $U$ is the number of unique teachers, required for maintaining the hash table or temporary buffer for the aggregation.

### Common Pitfalls / Mistakes

- **Forgetting `DISTINCT`**: Using `COUNT(subject_id)` instead of `COUNT(DISTINCT subject_id)` will overcount whenever a teacher teaches the same subject across multiple departments.
- **Incorrect Aliasing**: Forgetting to alias the computed column as `cnt`, which causes automated test harnesses to fail on column header mismatch.
- **Unnecessary Subqueries**: Writing nested subqueries with `SELECT DISTINCT teacher_id, subject_id` and then grouping; while functionally correct, it adds unnecessary syntactic overhead when `COUNT(DISTINCT ...)` is natively supported and optimized.

### Real Interview Follow-Up Questions

1. **How would you optimize this query for a table with hundreds of millions of rows?**
   - **Answer:** Add a composite index on `(teacher_id, subject_id)`. MySQL can leverage this index to perform a Loose Index Scan / Index-Only Scan (`Using index`), avoiding reading table data pages entirely and significantly reducing I/O and memory overhead.

2. **What if the dataset is too massive for a single relational database instance (e.g., distributed DB/BigQuery/Snowflake)?**
   - **Answer:** In distributed systems, `COUNT(DISTINCT)` can be an expensive operation because distinct values must be shuffled to the same reducer/worker. If exact counts are not strictly required at massive scale (e.g., analytics dashboards), an approximation algorithm like **HyperLogLog (HLL)** (e.g., `APPROX_COUNT_DISTINCT`) can be used to achieve $\mathcal{O}(1)$ memory with ~1-2% error rate. If exact counts are required, pre-aggregating or partitioning by `teacher_id` ensures data co-location.

3. **How would you handle teachers who currently do not teach any subjects (if there was a separate `Teachers` table)?**
   - **Answer:** If there is a parent `Teachers` master table and we must include teachers with `0` subjects, we would perform a `LEFT JOIN` from `Teachers` to `Teacher_Subjects` and use `COUNT(DISTINCT subject_id)`. `COUNT` ignores `NULL` values, naturally returning `0` for teachers without assigned subjects.
