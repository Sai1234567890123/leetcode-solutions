# 0807. Max Increase to Keep City Skyline

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/max-increase-to-keep-city-skyline/](https://leetcode.com/problems/max-increase-to-keep-city-skyline/)  
**Topics:** Array, Greedy, Matrix

---

## 📝 Problem Statement

There is a city composed of `n x n` blocks, where each block contains a single building shaped like a vertical square prism. You are given a **0-indexed** `n x n` integer matrix `grid` where `grid[r][c]` represents the **height** of the building located in the block at row `r` and column `c`.

A city's **skyline** is the outer contour formed by all the building when viewing the side of the city from a distance. The **skyline** from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of **any number of buildings by any amount** (the amount can be different per building). The height of a `0`-height building can also be increased. However, increasing the height of a building should **not** affect the city's **skyline** from any cardinal direction.

Return *the **maximum total sum** that the height of the buildings can be increased by **without** changing the city's **skyline** from any cardinal direction*.

 
Example 1:

```

**Input:** grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
**Output:** 35
**Explanation:** The building heights are shown in the center of the above image.
The skylines when viewed from each cardinal direction are drawn in red.
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

```

Example 2:

```

**Input:** grid = [[0,0,0],[0,0,0],[0,0,0]]
**Output:** 0
**Explanation:** Increasing the height of any building will result in the skyline changing.

```

 
**Constraints:**

	- `n == grid.length`

	- `n == grid[r].length`

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Precompute the maximum height in each row and each column.
        # The skyline from East/West is determined by row maximums.
        # The skyline from North/South is determined by column maximums.
        row_max = [max(row) for row in grid]
        col_max = [max(grid[r][c] for r in range(n)) for c in range(n)]
        
        total_increase = 0
        
        # For each building, the maximum allowed height without altering
        # the skyline is min(row_max[r], col_max[c]).
        for r in range(n):
            r_max = row_max[r]
            for c in range(n):
                total_increase += min(r_max, col_max[c]) - grid[r][c]
                
        return total_increase
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The skyline of the city from any cardinal direction is determined by the maximum heights:
- **East and West views**: Looking along any row $r$, the maximum height visible is $\max(\text{row } r)$.
- **North and South views**: Looking along any column $c$, the maximum height visible is $\max(\text{column } c)$.

For any specific building located at $(r, c)$:
1. Its height cannot exceed the maximum building height in row $r$ (otherwise, the East/West skyline would increase).
2. Its height cannot exceed the maximum building height in column $c$ (otherwise, the North/South skyline would increase).

Therefore, the maximum height this building can be increased to is:
$$\text{new\_height}(r, c) = \min(\text{row\_max}[r], \text{col\_max}[c])$$

Since the operations on each building are mutually independent (raising a building to at most its row and column maximum will never exceed the existing maximums), we can greedily maximize every building independently. The increase for each cell is $\text{new\_height}(r, c) - \text{grid}[r][c]$.

---

### Step-by-Step Approach

1. **Precompute Row Maximums**: Compute an array `row_max` where `row_max[r]` is the maximum element in row $r$.
2. **Precompute Column Maximums**: Compute an array `col_max` where `col_max[c]` is the maximum element in column $c$.
3. **Aggregate Total Increase**: Iterate through each cell $(r, c)$ in the grid, add $\min(\text{row\_max}[r], \text{col\_max}[c]) - \text{grid}[r][c]$ to the running sum, and return the total.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(n^2)$
  - Computing all row maximums takes $\mathcal{O}(n^2)$ time.
  - Computing all column maximums takes $\mathcal{O}(n^2)$ time.
  - Iterating over all $n \times n$ cells to compute the total delta takes $\mathcal{O}(n^2)$ time.
  - Overall time is $\mathcal{O}(n^2)$, which is optimal since we must read all elements in the input.

- **Space Complexity**: $\mathcal{O}(n)$
  - We store `row_max` of size $n$ and `col_max` of size $n$.
  - This requires $\mathcal{O}(n)$ auxiliary space.

---

### Common Pitfalls / Mistakes

1. **Recomputing Maxima on the Fly**: Calling `max(grid[r])` or scanning column $c$ inside the nested loop would lead to an $\mathcal{O}(n^3)$ solution, which is inefficient.
2. **Assuming Rectangular vs. Square Grid**: While the problem states the grid is $n \times n$, assuming rows and columns have identical indices or iterating incorrectly can cause `IndexError` if adapted to an $m \times n$ matrix. Writing robust code by indexing properly is best practice.
3. **Negative Increases**: Overthinking that increasing a building might decrease the skyline or require an adjustment that lowers a building. The problem only permits *increasing* heights, and $\min(\text{row\_max}[r], \text{col\_max}[c]) \ge \text{grid}[r][c]$ is mathematically guaranteed to be $\ge 0$.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the grid is massive and stored across distributed storage (e.g., MapReduce / Spark)?
**Answer**:
- **Phase 1 (Row & Column Max)**: In one pass, compute the maximum of each row and column. In MapReduce, map each cell `(r, c, val)` to `(row_r, val)` and `(col_c, val)` to compute `row_max` and `col_max` via standard reducer operations.
- **Phase 2 (Join & Delta Computation)**: Broadcast `row_max` and `col_max` (which are small, $\mathcal{O}(n)$, compared to the $\mathcal{O}(n^2)$ data) to all worker nodes. Each worker can then stream through its partition of the matrix and compute $\sum (\min(\text{row\_max}[r], \text{col\_max}[c]) - \text{grid}[r][c])$ locally, followed by a global reduction sum.

#### 2. What if $n$ is very large (e.g., $10^5 \times 10^5$), but the grid is sparse (most buildings have height 0)?
**Answer**:
- Represent the matrix in Coordinate List (COO) or Compressed Sparse Row (CSR) format: only store non-zero entries $(r, c, h)$.
- If most cells are $0$, note that non-empty cells still dictate `row_max` and `col_max`.
- Empty cells contribute $\min(\text{row\_max}[r], \text{col\_max}[c])$. Summing over all $n^2$ pairs would be $\mathcal{O}(n^2)$.
- To optimize: sum $\min(\text{row\_max}[r], \text{col\_max}[c])$ across all $(r, c)$ in $\mathcal{O}(n \log n)$ using sorting and prefix sums (similar to the standard trick: sort `col_max`, and for each `row_max[r]`, binary search to split where $\text{col\_max} < \text{row\_max}$ and where $\text{row\_max} \le \text{col\_max}$). Then subtract the sum of original non-zero entries.

#### 3. What if we can only increase at most $K$ buildings total, or have a total budget $B$ on height increase, to maximize some score?
**Answer**:
- Compute the potential gain $g_{r,c} = \min(\text{row\_max}[r], \text{col\_max}[c]) - \text{grid}[r][c]$ for every building.
- If we can select at most $K$ buildings to increase to their maximum: this reduces to picking the top-$K$ largest values of $g_{r, c}$, solvable in $\mathcal{O}(n^2)$ using Quickselect / `heapq.nlargest`.
- If buildings can be partially increased up to budget $B$: we can greedily allocate budget to any building with $g_{r, c} > 0$ until $B$ is exhausted.
