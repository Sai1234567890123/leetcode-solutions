# 1393. Capital Gain/Loss

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/capital-gainloss/](https://leetcode.com/problems/capital-gainloss/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Stocks`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| stock_name    | varchar |
| operation     | enum    |
| operation_day | int     |
| price         | int     |
+---------------+---------+
(stock_name, operation_day) is the primary key (combination of columns with unique values) for this table.
The operation column is an ENUM (category) of type ('Sell', 'Buy')
Each row of this table indicates that the stock which has stock_name had an operation on the day operation_day with the price.
It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day. It is also guaranteed that each 'Buy' operation for a stock has a corresponding 'Sell' operation in an upcoming day.

```

 

Write a solution to report the **Capital gain/loss** for each stock.

The **Capital gain/loss** of a stock is the total gain or loss after buying and selling the stock one or many times.

Return the result table in **any order**.

The result format is in the following example.

 
Example 1:

```

**Input:** 
Stocks table:
+---------------+-----------+---------------+--------+
| stock_name    | operation | operation_day | price  |
+---------------+-----------+---------------+--------+
| Leetcode      | Buy       | 1             | 1000   |
| Corona Masks  | Buy       | 2             | 10     |
| Leetcode      | Sell      | 5             | 9000   |
| Handbags      | Buy       | 17            | 30000  |
| Corona Masks  | Sell      | 3             | 1010   |
| Corona Masks  | Buy       | 4             | 1000   |
| Corona Masks  | Sell      | 5             | 500    |
| Corona Masks  | Buy       | 6             | 1000   |
| Handbags      | Sell      | 29            | 7000   |
| Corona Masks  | Sell      | 10            | 10000  |
+---------------+-----------+---------------+--------+
**Output:** 
+---------------+-------------------+
| stock_name    | capital_gain_loss |
+---------------+-------------------+
| Corona Masks  | 9500              |
| Leetcode      | 8000              |
| Handbags      | -23000            |
+---------------+-------------------+
**Explanation:** 
Leetcode stock was bought at day 1 for 1000$ and was sold at day 5 for 9000$. Capital gain = 9000 - 1000 = 8000$.
Handbags stock was bought at day 17 for 30000$ and was sold at day 29 for 7000$. Capital loss = 7000 - 30000 = -23000$.
Corona Masks stock was bought at day 1 for 10$ and was sold at day 3 for 1010$. It was bought again at day 4 for 1000$ and was sold at day 5 for 500$. At last, it was bought at day 6 for 1000$ and was sold at day 10 for 10000$. Capital gain/loss is the sum of capital gains/losses for each ('Buy' --> 'Sell') operation = (1010 - 10) + (500 - 1000) + (10000 - 1000) = 1000 - 500 + 9000 = 9500$.

```

---

## 💻 Implementation (python3)

```py
# Write your MySQL query statement below
SELECT 
    stock_name,
    SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
FROM 
    Stocks
GROUP BY 
    stock_name;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the net capital gain or loss for each stock. A transaction consists of buying a stock at a certain price and subsequently selling it at another price.
The gain or loss for a single pair of buy/sell operations is:
$$\text{Gain/Loss} = \text{Sell Price} - \text{Buy Price}$$

The problem statement guarantees that:
1. Every `Buy` operation has a corresponding `Sell` operation later.
2. Every `Sell` operation has a corresponding `Buy` operation earlier.

By the associative and commutative properties of addition:
$$\sum (\text{Sell Price} - \text{Buy Price}) = \sum \text{Sell Price} - \sum \text{Buy Price}$$

Thus, we do not need to explicitly pair up each buy with its corresponding sell. Instead, we can treat each `Buy` operation as a negative cash flow (`-price`) and each `Sell` operation as a positive cash flow (`+price`). Summing these cash flows grouped by `stock_name` gives the total capital gain or loss directly.

### Step-by-Step Approach

1. **Group by Stock**: Group the records by `stock_name` using `GROUP BY stock_name`.
2. **Conditional Aggregation**: Use a `CASE` expression (or `IF` function) inside `SUM()`:
   - If `operation = 'Sell'`, the contribution is `+price`.
   - If `operation = 'Buy'`, the contribution is `-price`.
3. **Alias the Result**: Rename the aggregated result to `capital_gain_loss`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of rows in the `Stocks` table. We perform a single pass over the table to aggregate the values per `stock_name`. If an index exists on `(stock_name)`, aggregation is optimized using hash aggregation or index streaming.
- **Space Complexity:** $\mathcal{O}(U)$, where $U$ is the number of unique `stock_name` values. The query engine uses memory proportional to the number of distinct groups to maintain intermediate aggregation state.

### Common Pitfalls / Mistakes

1. **Overcomplicating with Self-Joins / Window Functions**: Candidates often try to pair each buy with its specific sell using `ROW_NUMBER()` or self-joins. While logically valid, this is $\mathcal{O}(N \log N)$ or $\mathcal{O}(N^2)$ in query plan complexity, requires much more memory, and is prone to errors.
2. **Handling Unmatched Trades**: Notice the problem guarantee: every buy has a matching sell. If this guarantee were removed (e.g., unrealized holdings), you would need to filter out open positions or use FIFO matching via window functions.
3. **Data Type Overflow**: In real-world enterprise databases with high volumes, summing large prices can overflow 32-bit integers. Using `BIGINT` or `DECIMAL` is recommended in production.

### Real Interview Follow-Up Questions

#### 1. What if not all buys are sold yet (unrealized gains/losses), and trades must be matched using FIFO (First-In, First-Out)?
*Answer:* If stocks are sold partially and FIFO is required:
- We cannot simply do global sums. We would need to compute running cumulative sums of quantity bought and quantity sold using window functions (`SUM(quantity) OVER (PARTITION BY stock_name ORDER BY operation_day)`).
- We can determine overlaps between buy and sell tranches using window functions or recursive CTEs to calculate realized gains on closed positions and mark-to-market on open positions.

#### 2. How would this query scale on a table with 1 billion rows?
*Answer:*
- **Partitioning / Indexing**: Partition the table by range on `operation_day` (or hash on `stock_name`). A composite index on `(stock_name, operation, price)` allows an index-only scan (covering index), avoiding hitting the primary table storage.
- **Incremental Pre-aggregation**: In high-throughput transactional systems, maintain a materialized view or aggregate table that updates `capital_gain_loss` incrementally upon each transaction rather than recalculating from raw event logs.

#### 3. How to handle concurrent writes / late-arriving records?
*Answer:*
- For financial ledger systems, append-only event sourcing is standard (which matches this schema).
- To prevent phantom reads and ensure consistency when calculating balances across distributed nodes, queries run under Snapshot Isolation (MVCC) or use idempotent streaming consumer pipelines (e.g., Kafka + Apache Flink) that emit changelog streams to an OLAP store (like ClickHouse or StarRocks).
