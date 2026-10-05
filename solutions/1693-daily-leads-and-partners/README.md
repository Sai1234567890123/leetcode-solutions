# 1693. Daily Leads and Partners

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/daily-leads-and-partners/](https://leetcode.com/problems/daily-leads-and-partners/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `DailySales`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
The name consists of only lowercase English letters.

```

 

For each `date_id` and `make_name`, find the number of **distinct** `lead_id`'s and **distinct** `partner_id`'s.

Return the result table in **any order**.

The result format is in the following example.

 
Example 1:

```

**Input:** 
DailySales table:
+-----------+-----------+---------+------------+
| date_id   | make_name | lead_id | partner_id |
+-----------+-----------+---------+------------+
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |
+-----------+-----------+---------+------------+
**Output:** 
+-----------+-----------+--------------+-----------------+
| date_id   | make_name | unique_leads | unique_partners |
+-----------+-----------+--------------+-----------------+
| 2020-12-8 | toyota    | 2            | 3               |
| 2020-12-7 | toyota    | 1            | 2               |
| 2020-12-8 | honda     | 2            | 2               |
| 2020-12-7 | honda     | 3            | 2               |
+-----------+-----------+--------------+-----------------+
**Explanation:** 
For 2020-12-8, toyota gets leads = [0, 1] and partners = [0, 1, 2] while honda gets leads = [1, 2] and partners = [1, 2].
For 2020-12-7, toyota gets leads = [0] and partners = [1, 2] while honda gets leads = [0, 1, 2] and partners = [1, 2].

```

---

## 💻 Implementation (python3)

```py
SELECT 
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM 
    DailySales
GROUP BY 
    date_id, 
    make_name;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks us to aggregate sales data by two dimensions: `date_id` and `make_name`. For each unique combination of these two attributes, we need to count how many distinct `lead_id` values and distinct `partner_id` values exist.

In SQL, this maps directly to:
1. `GROUP BY date_id, make_name` to define the granularity of the aggregation.
2. `COUNT(DISTINCT lead_id)` and `COUNT(DISTINCT partner_id)` to count unique entities within each partition, ignoring duplicate values.

### Step-by-Step Approach
1. **Grouping Dimensions**: Group the records by `date_id` and `make_name`.
2. **Aggregation**: Apply `COUNT(DISTINCT ...)` on `lead_id` and alias the column as `unique_leads`. Apply `COUNT(DISTINCT ...)` on `partner_id` and alias the column as `unique_partners`.
3. **Output**: Return the grouped columns along with their respective distinct counts.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log N)$ or $\mathcal{O}(N)$ depending on whether MySQL uses sorting (filesort) or hash-based aggregation (available in MySQL 8.0+ for certain queries). Here, $N$ is the number of rows in the `DailySales` table.
- **Space Complexity**: $\mathcal{O}(U)$ auxiliary space, where $U$ is the number of unique `(date_id, make_name)` pairs, to maintain the aggregation hash table/temporary tables in memory.

### Common Pitfalls / Mistakes Candidates Make
1. **Using `COUNT(*)` or `COUNT(lead_id)` instead of `COUNT(DISTINCT lead_id)`**: The prompt explicitly highlights finding the number of *distinct* leads and partners. Standard `COUNT(col)` includes duplicates.
2. **Incorrect Column Aliases**: Failing to name the output columns exactly as requested (`unique_leads`, `unique_partners`).
3. **Incomplete `GROUP BY` Clause**: Grouping by only `date_id` or `make_name` instead of the composite key `(date_id, make_name)`.

### Real Interview Follow-Up Questions & Scale

#### 1. How would you optimize this query for a multi-billion row table?
- **Composite Indexing**: Create a covering composite index on `(date_id, make_name, lead_id, partner_id)`. With an index starting with `(date_id, make_name)`, the database engine can perform loose or tight index scans to compute the grouping without scanning the full table or creating on-disk temporary tables.
- **Partitioning**: Partition the table by range on `date_id` (e.g., monthly or yearly partitions). Queries filtering or grouping by date can leverage partition pruning.

#### 2. What if multiple `COUNT(DISTINCT ...)` operations cause performance degradation at scale?
- In MySQL, executing multiple `COUNT(DISTINCT)` expressions in the same query often prevents loose index scan optimizations and forces the engine to materialize temporary tables to deduplicate both dimensions.
- **Workaround (Pre-aggregation / Materialized Views)**: At massive scale (e.g., in a data warehouse like Snowflake or BigQuery), distinct counts are pre-aggregated incrementally into intermediate daily tables or computed using approximate algorithms like **HyperLogLog (HLL)** if a small error tolerance (~1-2%) is acceptable.
