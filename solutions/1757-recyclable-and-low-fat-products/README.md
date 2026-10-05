# 1757. Recyclable and Low Fat Products

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/recyclable-and-low-fat-products/](https://leetcode.com/problems/recyclable-and-low-fat-products/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Products`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
```

 

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in **any order**.

The result format is in the following example.

 
Example 1:

```

**Input:** 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
**Output:** 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
**Explanation:** Only products 1 and 3 are both low fat and recyclable.

```

---

## 💻 Implementation (python3)

```py
SELECT product_id
FROM Products
WHERE low_fats = 'Y' 
  AND recyclable = 'Y';
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem requires filtering a database table (`Products`) to find records satisfying two distinct boolean conditions simultaneously:
1. `low_fats` must be equal to `'Y'`.
2. `recyclable` must be equal to `'Y'`.

Since the output only asks for the `product_id` and the order does not matter, a single `SELECT` projection paired with a conjunctive `WHERE` clause (`AND`) delivers the direct and optimal result.

### Step-by-Step Approach
1. **Projection**: Specify `product_id` in the `SELECT` clause as required by the expected schema output.
2. **Source**: Read from table `Products`.
3. **Filtering**: Use the `WHERE` clause combining both constraints with the `AND` operator: `low_fats = 'Y' AND recyclable = 'Y'`.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$, where $N$ is the total number of rows in the `Products` table. In the absence of an index, the query engine performs a full table scan. With a composite index on `(low_fats, recyclable, product_id)`, this can be reduced to $\mathcal{O}(K)$ where $K$ is the number of matching rows (index-only scan).
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space beyond the memory needed to stream the result set to the client.

---

### Common Pitfalls / Mistakes Candidates Make
1. **Using `OR` instead of `AND`**: The problem specifies products that are *both* low fat and recyclable.
2. **Handling `ENUM` as boolean/integers**: While MySQL internally stores `ENUM` values as integers, writing `low_fats = 1` or `low_fats IS TRUE` can lead to subtle bugs or prevent index utilization. Always query against the literal enum string value (`'Y'`).
3. **Overcomplicating with subqueries / `INTERSECT`**: Attempting to query low-fat products and intersect with recyclable products introduces unnecessary overhead.

---

### Real Interview Follow-Up Questions

#### 1. How would you optimize this query if the `Products` table has hundreds of millions of rows?
- **Answer**: Create a composite index on `(low_fats, recyclable, product_id)` or `(recyclable, low_fats, product_id)`.
  - Because `product_id` is the primary key (or included in the index), this acts as a **covering index** (index-only scan). The database engine can satisfy the query entirely from the B+ Tree without reading the underlying row data pages (eliminating random I/O).

#### 2. What if the distribution of 'Y' and 'N' is heavily skewed?
- **Answer**: If 99% of products are `low_fats = 'Y'` and `recyclable = 'Y'`, an index scan might actually be slower than a sequential table scan due to random lookups (if not using a covering index). In systems like PostgreSQL, a **partial index** (`CREATE INDEX ... WHERE low_fats = 'Y' AND recyclable = 'Y'`) would be ideal. In MySQL 8.0+, we can use a functional index or simply rely on the query optimizer's cost model (engine checks statistics via histogram/analyze table).

#### 3. How does MySQL physically store `ENUM` types?
- **Answer**: MySQL stores `ENUM` values internally as 1- or 2-byte integers mapped to the declared string literals (up to 255 distinct elements use 1 byte; up to 65,535 use 2 bytes). Sorting/indexing is based on their internal index order unless explicit string casting is applied.
