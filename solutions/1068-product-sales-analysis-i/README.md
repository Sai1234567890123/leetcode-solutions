# 1068. Product Sales Analysis I

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/product-sales-analysis-i/](https://leetcode.com/problems/product-sales-analysis-i/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Sales`

```

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to `Product` table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.

```

 

Table: `Product`

```

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.

```

 

Write a solution to report the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table.

Return the resulting table in **any order**.

The result format is in the following example.

 
Example 1:

```

**Input:** 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
**Output:** 
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
**Explanation:** 
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.

```

---

## 💻 Implementation (python3)

```py
SELECT 
    p.product_name,
    s.year,
    s.price
FROM 
    Sales s
INNER JOIN 
    Product p ON s.product_id = p.product_id;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The objective is to retrieve the product name, year of sale, and unit price for every recorded sale in the `Sales` table.

1. **Identify Source Tables**:
   - `year` and `price` reside in the `Sales` table.
   - `product_name` resides in the `Product` table.
2. **Determine Join Condition**:
   - The two tables are related via `product_id`.
   - The problem statement specifies that `product_id` in `Sales` is a foreign key referencing the `Product` table. This guarantees referential integrity, meaning every `product_id` in `Sales` maps directly to a valid entry in `Product`.
   - An `INNER JOIN` (or simply `JOIN`) on `s.product_id = p.product_id` is the most optimal and straightforward way to match each sale with its corresponding product name without introducing unnecessary overhead.

### Step-by-Step Approach

1. **Select Columns**: Specify `p.product_name`, `s.year`, and `s.price` as requested by the output schema.
2. **From Clause**: Start with the `Sales` table aliased as `s`.
3. **Join Clause**: `INNER JOIN` the `Product` table aliased as `p` on `s.product_id = p.product_id`.
4. **Ordering**: The prompt states the result can be returned in any order, so no `ORDER BY` clause is required, saving sort overhead.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$, where $N$ is the number of rows in the `Sales` table.
  - Since `product_id` is the primary key of the `Product` table, the MySQL query optimizer can perform an index lookup (clustered index/B-tree) on `Product` for each record in `Sales`, leading to $\mathcal{O}(1)$ lookup time per row in `Sales`.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding the space needed to store/return the output result set), as the join can be evaluated as a streaming nested-loop join without intermediate temporary tables.

---

### Common Pitfalls / Mistakes

1. **Using `LEFT JOIN` without necessity**: While `LEFT JOIN` works here, candidates often default to it without understanding that `product_id` is a strictly defined foreign key. `INNER JOIN` conveys intent better and allows the query planner greater flexibility in join ordering if needed.
2. **Ambiguous Column References**: Forgetting to qualify column names with table aliases (e.g., using `product_id` without `s.` or `p.`) when columns share the same name across joined tables.
3. **Unnecessary `GROUP BY` or `DISTINCT`**: Adding `DISTINCT` or `GROUP BY` when not needed degrades performance by causing MySQL to create temporary tables and sort data.

---

### Real Interview Follow-Up Questions

#### 1. What if `Sales` contains billions of rows and the query is slow?
- **Answer**:
  - Ensure there is an index on `Sales(product_id)`. Without it, MySQL would scan `Sales` and do lookups on `Product`. If the planner decides to scan `Product` instead (e.g., if filtering by specific products), an index on `Sales(product_id)` enables index nested-loop join.
  - If partitioning `Sales` by `year`, query execution can take advantage of partition pruning if a year filter is introduced.
  - Consider denormalization: If `product_name` rarely changes, storing it directly in the `Sales` / transactional fact table eliminates the join altogether in high-throughput analytical OLAP systems (e.g., ClickHouse, Snowflake, BigQuery).

#### 2. What if referential integrity is broken (e.g., distributed databases without FK constraints)?
- **Answer**:
  - In microservices or eventual-consistency architectures, a sale might be written before the product metadata is replicated. In that case, an `INNER JOIN` would drop those sales rows.
  - To preserve all sales records regardless of metadata availability, switch to a `LEFT JOIN` and handle `NULL` product names using `COALESCE(p.product_name, 'Unknown')`.

#### 3. How would you handle SCD (Slowly Changing Dimensions) if a product's name changes over time?
- **Answer**:
  - Under SCD Type 2, the `Product` table would have `start_date` and `end_date` (or `effective_year`).
  - The join condition would be updated to:
    ```sql
    ON s.product_id = p.product_id 
   AND s.year BETWEEN p.start_year AND p.end_year
    ```
