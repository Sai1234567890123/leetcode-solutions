# 1741. Find Total Time Spent by Each Employee

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-total-time-spent-by-each-employee/](https://leetcode.com/problems/find-total-time-spent-by-each-employee/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Employees`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
(emp_id, event_day, in_time) is the primary key (combinations of columns with unique values) of this table.
The table shows the employees' entries and exits in an office.
event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
in_time and out_time are between 1 and 1440.
It is guaranteed that no two events on the same day intersect in time, and in_time  

Write a solution to calculate the total time **in minutes** spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is `out_time - in_time`.

Return the result table in **any order**.

The result format is in the following example.

 
Example 1:

```

**Input:** 
Employees table:
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+
**Output:** 
+------------+--------+------------+
| day        | emp_id | total_time |
+------------+--------+------------+
| 2020-11-28 | 1      | 173        |
| 2020-11-28 | 2      | 30         |
| 2020-12-03 | 1      | 41         |
| 2020-12-09 | 2      | 27         |
+------------+--------+------------+
**Explanation:** 
Employee 1 has three events: two on day 2020-11-28 with a total of (32 - 4) + (200 - 55) = 173, and one on day 2020-12-03 with a total of (42 - 1) = 41.
Employee 2 has two events: one on day 2020-11-28 with a total of (33 - 3) = 30, and one on day 2020-12-09 with a total of (74 - 47) = 27.

```

---

## 💻 Implementation (python3)

```py
SELECT 
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM 
    Employees
GROUP BY 
    event_day,
    emp_id;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the total time spent by each employee on each day. 
- For each visit/session, the duration spent inside the office is given by `out_time - in_time`.
- An employee can have multiple visits on the same day.
- Therefore, we need to group the records by the unique combination of the day (`event_day`) and the employee (`emp_id`).
- For each group, we compute the aggregate sum of durations: `SUM(out_time - in_time)`.
- Rename `event_day` to `day` and the computed sum to `total_time` to match the expected schema.

### Step-by-Step Approach

1. **Projection and Renaming**:
   - Select `event_day` aliased as `day`.
   - Select `emp_id`.
   - Compute `SUM(out_time - in_time)` aliased as `total_time`.
2. **Grouping**:
   - `GROUP BY event_day, emp_id` ensures that all entries for a specific employee on a specific day are combined into a single aggregated row.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$ or $\mathcal{O}(N \log N)$ where $N$ is the number of rows in `Employees`. 
  - If a composite index on `(event_day, emp_id)` exists, MySQL can perform a loose index scan or an ordered index scan in $\mathcal{O}(N)$ time without an explicit sorting phase.
  - Without an index covering the `GROUP BY` columns, MySQL utilizes an in-memory or on-disk temporary table / hash aggregate, running in $\mathcal{O}(N)$ average time (or $\mathcal{O}(N \log N)$ if filesort is required).
- **Space Complexity**: $\mathcal{O}(U)$, where $U$ is the number of unique `(event_day, emp_id)` pairs, needed to maintain the hash table or temporary buffer for grouping.

### Common Pitfalls / Mistakes

1. **Incorrect Column Names**: Renaming `event_day` to `day` is required by the problem's expected output schema. Missing the alias will cause test failures.
2. **Over-complicating with CTEs/Window Functions**: Some candidates mistakenly attempt window functions (`SUM(...) OVER(PARTITION BY ...)`) which produce multiple duplicate rows instead of collapsing rows via `GROUP BY`.
3. **Handling Overnight Shifts**: The problem states `in_time` and `out_time` are between 1 and 1440 on the same `event_day`. If shifts crossed midnight, dates and durations would need to be normalized or split across days (a common interview extension).

### Real Interview Follow-Up Questions

1. **What if shifts cross midnight (e.g., in at 23:00, out at 02:00 next day)?**
   - *Answer*: If `in_time > out_time`, the event spans across two days. We would either:
     - Split the event into two records: `(event_day, in_time, 1440)` and `(event_day + 1, 0, out_time)` using a `UNION ALL` or `LATERAL JOIN`.
     - Or store `in_time` and `out_time` as full `DATETIME` / `TIMESTAMP` types and calculate overlaps day-by-day.

2. **How to optimize performance at scale (billions of rows)?**
   - *Answer*:
     - **Partitioning**: Range-partition the `Employees` table by `event_day` (e.g., monthly or daily partitions).
     - **Clustered / Covering Index**: An index on `(event_day, emp_id, in_time, out_time)` allows index-only scans (covering index) avoiding table lookups entirely.
     - **Rollup Tables / Materialized Views**: For analytics dashboards, pre-aggregate data at the end of each day via an ETL / batch job or incrementally via stream processing (e.g., Apache Flink / Kafka).

3. **What if intervals can overlap?**
   - *Answer*: If intervals overlap (i.e. bad/dirty data), a simple `SUM(out_time - in_time)` would double-count time. We would first need to merge overlapping intervals (classic LeetCode 56 "Merge Intervals" logic) using window functions (`LAG` to track current max `out_time`) before summing durations.
