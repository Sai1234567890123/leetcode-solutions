# 1587. Bank Account Summary II

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/bank-account-summary-ii/](https://leetcode.com/problems/bank-account-summary-ii/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Users`

```

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| account      | int     |
| name         | varchar |
+--------------+---------+
account is the primary key (column with unique values) for this table.
Each row of this table contains the account number of each user in the bank.
There will be no two users having the same name in the table.

```

 

Table: `Transactions`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trans_id      | int     |
| account       | int     |
| amount        | int     |
| transacted_on | date    |
+---------------+---------+
trans_id is the primary key (column with unique values) for this table.
Each row of this table contains all changes made to all accounts.
amount is positive if the user received money and negative if they transferred money.
All accounts start with a balance of 0.

```

 

Write a solution to report the name and balance of users with a balance higher than `10000`. The balance of an account is equal to the sum of the amounts of all transactions involving that account.

Return the result table in **any order**.

The result format is in the following example.

 
Example 1:

```

**Input:** 
Users table:
+------------+--------------+
| account    | name         |
+------------+--------------+
| 900001     | Alice        |
| 900002     | Bob          |
| 900003     | Charlie      |
+------------+--------------+
Transactions table:
+------------+------------+------------+---------------+
| trans_id   | account    | amount     | transacted_on |
+------------+------------+------------+---------------+
| 1          | 900001     | 7000       |  2020-08-01   |
| 2          | 900001     | 7000       |  2020-09-01   |
| 3          | 900001     | -3000      |  2020-09-02   |
| 4          | 900002     | 1000       |  2020-09-12   |
| 5          | 900003     | 6000       |  2020-08-07   |
| 6          | 900003     | 6000       |  2020-09-07   |
| 7          | 900003     | -4000      |  2020-09-11   |
+------------+------------+------------+---------------+
**Output:** 
+------------+------------+
| name       | balance    |
+------------+------------+
| Alice      | 11000      |
+------------+------------+
**Explanation:** 
Alice's balance is (7000 + 7000 - 3000) = 11000.
Bob's balance is 1000.
Charlie's balance is (6000 + 6000 - 4000) = 8000.

```

---

## 💻 Implementation (python3)

```py
SELECT 
    u.name,
    SUM(t.amount) AS balance
FROM Users u
INNER JOIN Transactions t 
    ON u.account = t.account
GROUP BY 
    u.account, 
    u.name
HAVING 
    balance > 10000;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The objective is to compute the cumulative transaction balance for each account and return the `name` and `balance` for users whose balance exceeds `10,000`.

1. **Relation between Tables**: `Users` stores user identities and account numbers, while `Transactions` records individual monetary flows (`amount`). They link via `account`.
2. **Filtering Pre vs. Post Aggregation**: Since balance is defined as `SUM(amount)`, users with no transactions have a starting balance of 0, which is `<= 10000`. Thus, an `INNER JOIN` is appropriate (users with 0 transactions are naturally excluded).
3. **Aggregation**: We group by `u.account` (the unique identifier) and include `u.name` in the `GROUP BY` clause to satisfy SQL standard compliance (`ONLY_FULL_GROUP_BY`).
4. **Condition on Aggregate**: To filter aggregated values, SQL requires a `HAVING` clause rather than a `WHERE` clause. MySQL permits referencing the column alias `balance` directly in the `HAVING` clause.

### Step-by-Step Approach
1. Perform an `INNER JOIN` between `Users` and `Transactions` on `u.account = t.account`.
2. Apply `GROUP BY u.account, u.name` to isolate each user's financial ledger.
3. Compute `SUM(t.amount) AS balance` for each account.
4. Filter using `HAVING balance > 10000` to select only accounts strictly greater than the threshold.

### Complexity Analysis
- **Time Complexity**: 
  - Without indexes: $\mathcal{O}(M + N \log N)$ or $\mathcal{O}(M \log M)$ where $M$ is the number of rows in `Transactions` and $N$ is the number of rows in `Users`, due to scanning and hash/sort grouping.
  - With an index on `Transactions(account, amount)` and `Users(account)`: The engine can stream-aggregate transactions in $\mathcal{O}(M)$ time and fetch names in $\mathcal{O}(K)$ where $K$ is the number of qualifying accounts.
- **Space Complexity**: $\mathcal{O}(U)$ auxiliary space where $U$ is the number of unique accounts processed in the hash aggregate table / temporary sorting buffer.

### Common Pitfalls / Mistakes Candidates Make
1. **Using `WHERE` instead of `HAVING`**: Attempting `WHERE SUM(t.amount) > 10000` will fail with an invalid use of group function error because `WHERE` filters rows *before* grouping occurs.
2. **`LEFT JOIN` overhead**: Using `LEFT JOIN` is not incorrect logically, but unnecessary since accounts without transactions have balance = 0, which never satisfies `> 10000`. `INNER JOIN` allows the optimizer more join order freedom.
3. **Grouping by `name` only**: Two users could theoretically share a name in other variations of this problem (even though the problem states names are unique here). Best practice is always to group by the primary key `u.account` (or `u.account, u.name`) to prevent accidental merges.
4. **ANSI SQL Compliance**: Omitting `u.name` from `GROUP BY` will trigger `ONLY_FULL_GROUP_BY` syntax errors in strict SQL modes unless functional dependency is recognized by the DBMS.

### Real Interview Follow-Up Questions

#### 1. Scale: "What if `Transactions` has 10 billion rows and `Users` has 50 million rows?"
- **Answer**: 
  - Performing a join before aggregation would explode intermediate memory. Instead, aggregate `Transactions` first:
    ```sql
    SELECT u.name, t.balance
    FROM (
        SELECT account, SUM(amount) AS balance
        FROM Transactions
        GROUP BY account
        HAVING SUM(amount) > 10000
    ) t
    JOIN Users u ON t.account = u.account;
    ```
  - Create a composite covering index: `Transactions(account, amount)`. This allows index-only scans (no table heap lookups).
  - At massive scale, maintain an aggregated table or materialized view for current balances updated asynchronously or via event-driven stream processing (e.g., Apache Flink/Kafka).

#### 2. Concurrency: "How would you handle continuous high-throughput incoming transactions?"
- **Answer**: 
  - Querying aggregate sums over raw transaction ledgers on write-heavy tables creates lock contention and slow reads.
  - In practice, we maintain a `current_balance` column directly on the `Accounts` / `Users` table updated within a transactional boundary (or write-ahead ledger with snapshot balances), making balance checks an indexed range query: `SELECT name, balance FROM Users WHERE balance > 10000;`.
