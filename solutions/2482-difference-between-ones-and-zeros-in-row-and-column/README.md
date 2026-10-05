# 2482. Difference Between Ones and Zeros in Row and Column

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/)  
**Topics:** Array, Matrix, Simulation

---

## 📝 Problem Statement

You are given a **0-indexed** `m x n` binary matrix `grid`.

A **0-indexed** `m x n` difference matrix `diff` is created with the following procedure:

	- Let the number of ones in the `ith` row be `onesRowi`.

	- Let the number of ones in the `jth` column be `onesColj`.

	- Let the number of zeros in the `ith` row be `zerosRowi`.

	- Let the number of zeros in the `jth` column be `zerosColj`.

	- `diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj`

Return *the difference matrix *`diff`.

 
Example 1:

```

**Input:** grid = [[0,1,1],[1,0,1],[0,0,1]]
**Output:** [[0,0,4],[0,0,4],[-2,-2,2]]
**Explanation:**
- diff[0][0] = `onesRow0 + onesCol0 - zerosRow0 - zerosCol0` = 2 + 1 - 1 - 2 = 0 
- diff[0][1] = `onesRow0 + onesCol1 - zerosRow0 - zerosCol1` = 2 + 1 - 1 - 2 = 0 
- diff[0][2] = `onesRow0 + onesCol2 - zerosRow0 - zerosCol2` = 2 + 3 - 1 - 0 = 4 
- diff[1][0] = `onesRow1 + onesCol0 - zerosRow1 - zerosCol0` = 2 + 1 - 1 - 2 = 0 
- diff[1][1] = `onesRow1 + onesCol1 - zerosRow1 - zerosCol1` = 2 + 1 - 1 - 2 = 0 
- diff[1][2] = `onesRow1 + onesCol2 - zerosRow1 - zerosCol2` = 2 + 3 - 1 - 0 = 4 
- diff[2][0] = `onesRow2 + onesCol0 - zerosRow2 - zerosCol0` = 1 + 1 - 2 - 2 = -2
- diff[2][1] = `onesRow2 + onesCol1 - zerosRow2 - zerosCol1` = 1 + 1 - 2 - 2 = -2
- diff[2][2] = `onesRow2 + onesCol2 - zerosRow2 - zerosCol2` = 1 + 3 - 2 - 0 = 2

```

Example 2:

```

**Input:** grid = [[1,1,1],[1,1,1]]
**Output:** [[5,5,5],[5,5,5]]
**Explanation:**
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5

```

 
**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 5`

	- `1 5`

	- `grid[i][j]` is either `0` or `1`.

---

## 💻 Implementation (python3)

```py
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        
        # Precompute the count of 1s in each row and each column
        ones_row = [sum(row) for row in grid]
        ones_col = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        # Mathematical simplification:
        # zeros_row[i] = n - ones_row[i]
        # zeros_col[j] = m - ones_col[j]
        # diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]
        #            = ones_row[i] + ones_col[j] - (n - ones_row[i]) - (m - ones_col[j])
        #            = 2 * ones_row[i] + 2 * ones_col[j] - (m + n)
        total_dim = m + n
        
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            row_term = 2 * ones_row[i] - total_dim
            for j in range(n):
                diff[i][j] = row_term + 2 * ones_col[j]
                
        return diff
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A naive approach would recalculate the count of ones and zeros for the row and column of every single cell `(i, j)`. For an $m \times n$ matrix, computing these counts for each cell takes $O(m + n)$ time, resulting in an overall time complexity of $O(m \cdot n \cdot (m + n))$, which would lead to a Time Limit Exceeded (TLE) error for larger dimensions.

Instead, we can observe two critical properties:
1. **Redundant Computations:** The number of ones in row $i$ (`onesRow[i]`) and column $j$ (`onesCol[j]`) are invariant regardless of the specific cell in row $i$ or column $j$. We can precompute these counts once in $O(m \times n)$ time.
2. **Algebraic Simplification:**
   In a binary grid of dimensions $m \times n$:
   $$\text{zerosRow}_i = n - \text{onesRow}_i$$
   $$\text{zerosCol}_j = m - \text{onesCol}_j$$
   
   Substituting these into the given formula:
   $$\begin{aligned}
   \text{diff}[i][j] &= \text{onesRow}_i + \text{onesCol}_j - \text{zerosRow}_i - \text{zerosCol}_j \\
   &= \text{onesRow}_i + \text{onesCol}_j - (n - \text{onesRow}_i) - (m - \text{onesCol}_j) \\
   &= 2 \cdot \text{onesRow}_i + 2 \cdot \text{onesCol}_j - (m + n)
   \end{aligned}$$

This eliminates the need to track zero counts entirely and reduces each entry's calculation to a constant-time $O(1)$ arithmetic operation.

---

### Step-by-Step Approach

1. **Precompute Row Sums:** Calculate `ones_row[i]` for each row $i \in [0, m-1]$. In Python, this is simply `sum(grid[i])`.
2. **Precompute Column Sums:** Calculate `ones_col[j]` for each column $j \in [0, n-1]$ by summing elements along column $j$.
3. **Construct the Result Matrix:** 
   - Initialize a matrix `diff` of size $m \times n$.
   - Precompute `row_term = 2 * ones_row[i] - (m + n)` for the outer loop to minimize repeated calculations in the inner loop.
   - Set `diff[i][j] = row_term + 2 * ones_col[j]`.
4. Return `diff`.

---

### Complexity Analysis

- **Time Complexity:** $O(m \times n)$
  - Computing `ones_row` takes $O(m \times n)$ time.
  - Computing `ones_col` takes $O(m \times n)$ time.
  - Filling the $m \times n$ result matrix takes $O(m \times n)$ time.
  - Overall Time Complexity: $\mathcal{O}(m \times n)$, which is asymptotically optimal because every element must be visited and produced.

- **Space Complexity:** $O(m + n)$ auxiliary space
  - `ones_row` requires $O(m)$ auxiliary space.
  - `ones_col` requires $O(n)$ auxiliary space.
  - The output matrix `diff` takes $O(m \times n)$ space, but standard interview conventions treat the return value as separate from auxiliary algorithmic memory.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Brute Force Counting:** Scanning the row and column inside the nested loops ($O(m \cdot n \cdot (m + n))$), demonstrating a lack of efficiency awareness.
2. **Maintaining Redundant Arrays:** Allocating separate arrays for `zeros_row` and `zeros_col`. While $O(m + n)$ is preserved, failing to algebraically simplify the formula misses an opportunity to show clean mathematical problem-solving.
3. **Cache-Unfriendly Iteration:** In languages like C++ or Java, traversing the matrix column-by-column rather than row-by-row during column precomputation can degrade CPU cache performance. In Python, list comprehensions should be structured efficiently.

---

### Real Interview Follow-Up Questions

#### 1. Can we solve this in $O(1)$ auxiliary space?
**Answer:** 
Yes, if modifying the input `grid` in-place is allowed. We can store the row sums and column sums directly in the first row and column or use bit manipulation/encoding if values fit within standard integer limits. However, since the result matrix `diff` contains negative numbers and numbers larger than 1, we cannot do a pure in-place overwrite cell-by-cell without either a temporary buffer or an encoding scheme (e.g., bitwise shifting if entries fit in a 32-bit integer). In Python/standard interview settings, modifying the input signature from `list[list[int]]` containing 0/1 to arbitrary integers is acceptable if explicitly agreed upon with the interviewer.

#### 2. What if the matrix is too large to fit in memory (External Memory / Distributed Systems)?
**Answer:**
If the matrix is partitioned across multiple machines (e.g., MapReduce/Spark):
- **Mapper Phase 1:** Emit key-value pairs for row sums `(row_id, val)` and column sums `(col_id, val)`.
- **Reducer Phase 1:** Aggregate to obtain global `ones_row` and `ones_col`. Since $m + n \ll m \times n$, these two vectors easily fit into memory (e.g., a few megabytes even for $m, n = 1,000,000$).
- **Mapper Phase 2 / Broadcast:** Broadcast `ones_row` and `ones_col` to all worker nodes. Each worker streaming a chunk/block of `grid` can locally output the corresponding chunk of `diff` in a single pass without cross-node shuffle.
