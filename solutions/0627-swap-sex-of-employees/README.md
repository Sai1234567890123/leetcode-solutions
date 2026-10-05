# 0627. Swap Sex of Employees

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/swap-sex-of-employees/](https://leetcode.com/problems/swap-sex-of-employees/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Salary`

```

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
id is the primary key (column with unique values) for this table.
The sex column is ENUM (category) value of type ('m', 'f').
The table contains information about an employee.

```

 

Write a solution to swap all `'f'` and `'m'` values (i.e., change all `'f'` values to `'m'` and vice versa) with a **single update statement** and no intermediate temporary tables.

Note that you must write a single update statement, **do not** write any select statement for this problem.

The result format is in the following example.

 
Example 1:

```

**Input:** 
Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+
**Output:** 
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
+----+------+-----+--------+
**Explanation:** 
(1, A) and (3, C) were changed from 'm' to 'f'.
(2, B) and (4, D) were changed from 'f' to 'm'.

```

---

## 💻 Implementation (python3)

```py
UPDATE Salary
SET 
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The objective is to toggle the value of `sex` between `'m'` and `'f'` in-place using a single `UPDATE` statement without creating temporary tables or using intermediate `SELECT` queries.

Because an `UPDATE` statement applies the expression row-by-row concurrently at the logical level:
1. If the current row's value is `'m'`, we change it to `'f'`.
2. Otherwise, if it is `'f'`, we change it to `'m'`.

In SQL, conditional column assignment in an `UPDATE` statement can be cleanly performed using either a `CASE` expression or the MySQL `IF()` function. A standard `CASE` expression is preferred as it is ANSI SQL compliant and portable across database management systems (PostgreSQL, Oracle, SQL Server, etc.).

### Step-by-Step Approach

1. **Target Table**: Specify the `Salary` table in the `UPDATE` clause.
2. **Conditional Assignment**: Use `SET sex = CASE sex WHEN 'm' THEN 'f' ELSE 'm' END;`.
   - Alternative MySQL-specific form: `SET sex = IF(sex = 'm', 'f', 'm');`.
3. **Execution**: No `WHERE` clause is needed because every row in the table needs its `sex` toggled.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the number of rows in the `Salary` table. Each row is read and updated in a single pass.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space. The update is performed in-place without generating temporary tables or intermediate buffers.

### Common Pitfalls / Mistakes

1. **Sequential Updates**: Trying to run two separate updates:
   ```sql
   -- INCORRECT:
   UPDATE Salary SET sex = 'f' WHERE sex = 'm';
   UPDATE Salary SET sex = 'm' WHERE sex = 'f'; -- This now sets ALL rows to 'm'!
   ```
2. **Using a `SELECT` statement**: The problem explicitly requires a single `UPDATE` query without subqueries or temporary tables.
3. **Handling `NULL` values**: If `sex` could be `NULL`, `ELSE 'm'` would convert `NULL` to `'m'`. While the problem specifies `sex` is an ENUM with values `('m', 'f')`, in production systems with nullable columns, explicit branching should be used:
   ```sql
   CASE 
       WHEN sex = 'm' THEN 'f'
       WHEN sex = 'f' THEN 'm'
       ELSE sex 
   END
   ```

### Real Interview Follow-Up Questions

#### 1. What happens if this table has 500 million rows? How do you run this update in production?
- **Problem**: Running a single, full-table `UPDATE` locks the table/rows (depending on storage engine and isolation level), causes massive transaction log (undo/redo log) growth, and can cause replication lag in read replicas.
- **Solution**: Chunk the updates in batches by the primary key (`id`) using indexed pagination:
  ```sql
  -- Pseudocode for chunking batch:
  UPDATE Salary 
  SET sex = IF(sex = 'm', 'f', 'm')
  WHERE id BETWEEN ? AND ?;
  ```
  Sleep briefly between iterations to allow replica catch-up and prevent lock contention.

#### 2. How does MySQL handle replication for this statement?
- **Row-Based Replication (RBR)**: MySQL writes the before-and-after image of each modified row into the binary log. For large tables, this generates massive binary log volume.
- **Statement-Based Replication (SBR)**: MySQL logs the SQL statement itself, which is deterministic in this case, but can cause replication lag on replicas while the single long-running query executes.

#### 3. Can we solve this using bitwise XOR or ASCII arithmetic?
- Yes, using ASCII arithmetic:
  - ASCII of `'m'` is 109, ASCII of `'f'` is 102.
  - Notice that $109 + 102 = 211$.
  - Therefore: `CHAR(211 - ASCII(sex))` flips `'m'` to `'f'` and `'f'` to `'m'`.
  - Or using XOR: `'m' ^ 'f' ^ sex`.
  While clever in competitive programming, these arithmetic tricks bypass column type checks/constraints and are strongly discouraged in production due to poor readability and optimization penalties.
