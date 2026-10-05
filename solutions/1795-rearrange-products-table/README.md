# 1795. Rearrange Products Table

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/rearrange-products-table/](https://leetcode.com/problems/rearrange-products-table/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Products`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.

```

 

Write a solution to rearrange the `Products` table so that each row has `(product_id, store, price)`. If a product is not available in a store, do **not** include a row with that `product_id` and `store` combination in the result table.

Return the result table in **any order**.

The result format is in the following example.

 
Example 1:

```

**Input:** 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
**Output:** 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
**Explanation:** 
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.

```

---

## 💻 Implementation (python3)

```py
SELECT 
    product_id, 
    'store1' AS store, 
    store1 AS price 
FROM 
    Products 
WHERE 
    store1 IS NOT NULL

UNION ALL

SELECT 
    product_id, 
    'store2' AS store, 
    store2 AS price 
FROM 
    Products 
WHERE 
    store2 IS NOT NULL

UNION ALL

SELECT 
    product_id, 
    'store3' AS store, 
    store3 AS price 
FROM 
    Products 
WHERE 
    store3 IS NOT NULL;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires transforming data from a "wide" format (columns representing attributes/entities) to a "long" or "narrow" format (rows representing key-value pairs). This operation is classically known as **unpivoting**.

In databases like SQL Server or Oracle, there is an explicit `UNPIVOT` operator. However, in MySQL, the standard, most readable, and highly performant approach is to use `UNION ALL` across multiple `SELECT` queries—one for each column that needs to be converted into a row.

Each individual query:
1. Selects `product_id`.
2. Hardcodes the literal store name (`'store1'`, `'store2'`, `'store3'`) as `store`.
3. Selects the respective column value as `price`.
4. Filters out unavailable prices with `WHERE <store_col> IS NOT NULL`.

Using `UNION ALL` instead of `UNION` is crucial here because `UNION ALL` does not incur the performance penalty of a duplicate-elimination sort/hash step. Since each branch queries a distinct store name, rows across the three branches are inherently unique.

---

### Step-by-Step Approach

1. **First Branch (`store1`)**:
   - Extract `product_id`, constant string `'store1'` as `store`, and `store1` as `price`.
   - Filter rows where `store1 IS NOT NULL`.
2. **Combine via `UNION ALL`**:
   - Preserves all rows without sorting or deduplication overhead.
3. **Repeat for `store2` and `store3`**:
   - Apply the exact same projection and null filtering for `store2` and `store3`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of rows in the `Products` table. Each branch performs a linear scan over the table (or index scan if applicable), scanning the table 3 times. $3 \times \mathcal{O}(N) = \mathcal{O}(N)$.
- **Space Complexity:** $\mathcal{O}(N)$ auxiliary memory to store and stream the result set of up to $3N$ rows.

---

### Common Pitfalls / Mistakes

1. **Using `UNION` instead of `UNION ALL`:**
   - Using `UNION` forces the database engine to perform an unnecessary sort or hash table operation to deduplicate rows across queries. This degrades performance from linear time to $\mathcal{O}(N \log N)$ or introduces significant memory overhead.
2. **Forgetting `IS NOT NULL`:**
   - If missing, rows with `NULL` prices will appear in the result set, violating the requirement: *"If a product is not available in a store, do not include a row"*.
3. **Using `!= NULL` instead of `IS NOT NULL`:**
   - In SQL, comparing any value to `NULL` using equality operators (`=` or `!=`) evaluates to `UNKNOWN` (falsy in `WHERE` clauses). Always use `IS NOT NULL`.

---

### Real Interview Follow-Up Questions

#### 1. What if there are 100+ stores instead of just 3? How would you design this?
- **Answer:** Hardcoding 100 `UNION ALL` statements becomes unmaintainable and results in 100 table scans.
  - **Dynamic SQL:** Construct the `UNION ALL` query dynamically via a stored procedure or application layer.
  - **Schema Redesign:** The root issue is a violation of First Normal Form (1NF). The table should ideally be modeled normalized from the start: `ProductPrices(product_id, store_id, price)` with a composite primary key `(product_id, store_id)`.
  - **Cross Join / Lateral Unpivot:** In MySQL 8.0.19+, we can join with a derived table of store names and unpivot in a single table scan using a `CROSS JOIN` with `CASE` expressions or `JSON_TABLE`.

#### 2. How can we perform this in a single scan of the `Products` table without multiple `UNION ALL` passes?
- **Answer:** We can cross join `Products` with a small virtual table containing 3 rows:
  ```sql
  SELECT 
      p.product_id,
      s.store,
      CASE s.store
          WHEN 'store1' THEN p.store1
          WHEN 'store2' THEN p.store2
          WHEN 'store3' THEN p.store3
      END AS price
  FROM Products p
  CROSS JOIN (
      SELECT 'store1' AS store 
      UNION ALL SELECT 'store2' 
      UNION ALL SELECT 'store3'
  ) s
  WHERE 
      CASE s.store
          WHEN 'store1' THEN p.store1
          WHEN 'store2' THEN p.store2
          WHEN 'store3' THEN p.store3
      END IS NOT NULL;
  ```
  This guarantees a single scan of the large `Products` table.
