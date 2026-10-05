# 2373. Largest Local Values in a Matrix

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/largest-local-values-in-a-matrix/](https://leetcode.com/problems/largest-local-values-in-a-matrix/)  
**Topics:** Array, Matrix

---

## 📝 Problem Statement

You are given an `n x n` integer matrix `grid`.

Generate an integer matrix `maxLocal` of size `(n - 2) x (n - 2)` such that:

	- `maxLocal[i][j]` is equal to the **largest** value of the `3 x 3` matrix in `grid` centered around row `i + 1` and column `j + 1`.

In other words, we want to find the largest value in every contiguous `3 x 3` matrix in `grid`.

Return *the generated matrix*.

 
Example 1:

```

**Input:** grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
**Output:** [[9,9],[8,6]]
**Explanation:** The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
```

Example 2:

```

**Input:** grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
**Output:** [[2,2,2],[2,2,2],[2,2,2]]
**Explanation:** Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.

```

 
**Constraints:**

	- `n == grid.length == grid[i].length`

	- `3

---

## 💻 Implementation (python3)

```py
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        # Result matrix dimensions are (n - 2) x (n - 2)
        max_local = [[0] * (n - 2) for _ in range(n - 2)]
        
        # Iterate over all possible top-left corners of 3x3 submatrices
        for i in range(n - 2):
            for j in range(n - 2):
                # Find maximum value in the 3x3 window:
                # rows: i to i + 2, cols: j to j + 2
                max_val = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if grid[r][c] > max_val:
                            max_val = grid[r][c]
                max_local[i][j] = max_val
                
        return max_local
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to compute a 2D max-pooling operation with a kernel size of $3 \times 3$ and stride of $1$, which is a standard operation in Convolutional Neural Networks (CNNs).

Given an $n \times n$ grid, each valid center $(i + 1, j + 1)$ corresponds to a $3 \times 3$ subgrid whose rows span from $i$ to $i + 2$ and columns span from $j$ to $j + 2$. Since $i$ ranges from $0$ to $n - 3$ and $j$ ranges from $0$ to $n - 3$, the output matrix will naturally have dimensions $(n - 2) \times (n - 2)$.

Because the window size is fixed at $3 \times 3$, each cell in the result matrix requires inspecting exactly $9$ elements. With $n \le 100$, an explicit scan of all $9$ elements for each of the $(n - 2)^2$ cells results in at most $9 \times 98 \times 98 \approx 8.6 \times 10^4$ operations, which executes in a few milliseconds.

---

### Step-by-Step Approach

1. **Initialize Output Matrix**: Allocate an $(n - 2) \times (n - 2)$ matrix initialized with zeros.
2. **Iterate Subgrids**:
   - Loop `i` from $0$ to $n - 3$.
   - Loop `j` from $0$ to $n - 3$.
3. **Find Maximum**:
   - For each pair $(i, j)$, scan all elements $(r, c)$ where $r \in [i, i+2]$ and $c \in [j, j+2]$.
   - Track the maximum value encountered.
4. **Store and Return**: Assign the computed maximum to `maxLocal[i][j]`. After traversing all windows, return `maxLocal`.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(n^2)$
  There are $(n - 2)^2$ positions. For each position, we inspect exactly $3 \times 3 = 9$ cells. Hence, total operations are $9(n - 2)^2 = \mathcal{O}(n^2)$, which is asymptotically optimal because every element in the output matrix must be written.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (or $\mathcal{O}(n^2)$ including the output matrix). No additional dynamic data structures are used.

---

### Common Pitfalls / Mistakes

1. **Off-by-One in Boundaries**: Iterating up to $n$ instead of $n - 2$ leads to `IndexError` when looking at $i + 2$ or $j + 2$.
2. **Center vs. Top-Left Indexing**: The problem defines the cell as centered at $(i + 1, j + 1)$. Candidates sometimes confuse the coordinates and add offsets inconsistently. Defining the window directly from $(i, j)$ to $(i + 2, j + 2)$ avoids coordinate confusion.
3. **Overengineering**: Trying to implement a 2D monotonic queue or segment tree for a fixed $3 \times 3$ kernel adds unnecessary code complexity and memory overhead, increasing the risk of bugs during an interview.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the window size is $k \times k$ instead of $3 \times 3$, where $k$ can be large (up to $n$)?
- **Answer**: 
  - If we brute-force, it takes $\mathcal{O}(n^2 \cdot k^2)$ time.
  - We can optimize to $\mathcal{O}(n^2)$ using a **1D Monotonic Deque** (Sliding Window Maximum) in two passes (separable filter):
    1. For each row, compute sliding window maximum of length $k$ across columns. This produces an $n \times (n - k + 1)$ intermediate matrix in $\mathcal{O}(n^2)$ time.
    2. For each column of the intermediate matrix, compute sliding window maximum of length $k$ across rows. This produces the final $(n - k + 1) \times (n - k + 1)$ matrix in $\mathcal{O}(n^2)$ time.

#### 2. What if the input matrix is streaming row-by-row?
- **Answer**: 
  - We only need to buffer the last $3$ rows in memory at any given time.
  - Once row $r$ arrives, we drop row $r - 3$, and immediately emit the maximums for row $r - 2$.
  - Space complexity drops from storing the whole grid $\mathcal{O}(n^2)$ to $\mathcal{O}(n)$.

#### 3. How would you parallelize this computation for a massive image (e.g., $10000 \times 10000$)?
- **Answer**:
  - Max-pooling is an **embarrassingly parallel** stencil operation.
  - We can partition the grid into horizontal or 2D tiles across multiple threads or GPU threads. Each worker computes its assigned subgrid.
  - Border sharing (a halo/ghost zone of 1 cell width) is required if processing across distributed nodes.
