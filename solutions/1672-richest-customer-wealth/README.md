# 1672. Richest Customer Wealth

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/richest-customer-wealth/](https://leetcode.com/problems/richest-customer-wealth/)  
**Topics:** Array, Matrix

---

## 📝 Problem Statement

You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the `i​​​​​​​​​​​th​​​​` customer has in the `j​​​​​​​​​​​th`​​​​ bank. Return* the **wealth** that the richest customer has.*

A customer's **wealth** is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum **wealth**.

 
Example 1:

```

**Input:** accounts = [[1,2,3],[3,2,1]]
**Output:** 6
**Explanation****:**
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

```

Example 2:

```

**Input:** accounts = [[1,5],[7,3],[3,5]]
**Output:** 10
**Explanation**: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
```

Example 3:

```

**Input:** accounts = [[2,8,7],[7,1,3],[1,9,5]]
**Output:** 17

```

 
**Constraints:**

	- `m == accounts.length`

	- `n == accounts[i].length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        """
        Calculates the maximum wealth among all customers.
        Each row represents a customer's accounts across different banks.
        """
        # Use a generator expression inside max() to maintain O(1) auxiliary space
        return max(sum(customer_accounts) for customer_accounts in accounts)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks for the maximum wealth of any single customer. A customer's wealth is the sum of their balances across all banks (represented by a row in the 2D grid). 

To find the maximum wealth:
1. Iterate through each row in the 2D matrix `accounts`.
2. Compute the sum of the values in each row (representing that customer's total wealth).
3. Track and return the maximum sum encountered.

### Step-by-Step Approach
1. Iterate over each row `customer_accounts` in `accounts`.
2. Compute `sum(customer_accounts)`.
3. Feed this into the built-in `max()` function using a generator expression. A generator expression avoids allocating a separate list in memory to store the sums, evaluating each row on-the-fly.

### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(m \times n)$, where $m$ is the number of customers (rows) and $n$ is the number of bank accounts per customer (columns). Every cell in the grid must be visited exactly once to calculate the sum.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The generator computes the sum for one customer at a time and tracks the running maximum without allocating additional data structures.

### Common Pitfalls / Mistakes
- **Creating intermediate lists:** Writing `max([sum(c) for c in accounts])` allocates an unnecessary $\mathcal{O}(m)$ list in memory. Using a generator `(sum(c) for c in accounts)` is the idiomatic, memory-optimal Python pattern.
- **Integer Overflow (Language-dependent):** In languages like C++ or Java, summing numbers could theoretically overflow standard 32-bit signed integers if bank values were up to $2 \times 10^9$. Given the constraints ($m, n \le 50$, $accounts[i][j] \le 100$), standard integers and Python's arbitrary-precision integers easily avoid overflow. Always check constraints in an interview.

### Real Interview Follow-Up Questions & Answers

#### 1. What if the matrix is stored on disk because it's too large to fit in memory? (Streaming Data / Scale)
- **Answer:** Stream the data row-by-row (or line-by-line from a distributed file system like HDFS / GCS / S3). For each line/row, parse the numbers, compute the sum, update a global running `max_wealth`, and discard the row data immediately. This keeps memory usage strictly at $\mathcal{O}(n)$ (or $\mathcal{O}(1)$ if streaming token-by-token).

#### 2. What if $m$ and $n$ are massive (e.g., millions of customers, thousands of banks)? (Concurrency / Parallelism)
- **Answer:** This problem is embarrassingly parallel. We can use MapReduce / Spark or a multi-threaded/multi-process worker pool:
  - **Map phase:** Partition the customer rows among worker nodes/threads. Each worker computes `sum(row)` for its assigned rows and finds its local maximum.
  - **Reduce phase:** Aggregate the local maximums from all workers to determine the global maximum.

#### 3. How would you handle negative balances (e.g., customer debts / loans)?
- **Answer:** The logic remains identical. The only change needed is initializing the maximum tracker to $-\infty$ (`float('-inf')` in Python or `Integer.MIN_VALUE` in Java) instead of `0`, ensuring that if all customers have net-negative wealth, the least negative wealth is accurately returned.
