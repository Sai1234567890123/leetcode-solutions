# 3446. Sort Matrix by Diagonals

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/sort-matrix-by-diagonals/](https://leetcode.com/problems/sort-matrix-by-diagonals/)  
**Topics:** Array, Sorting, Matrix

---

## 📝 Problem Statement

You are given an `n x n` square matrix of integers `grid`. Return the matrix such that:

	- The diagonals in the **bottom-left triangle** (including the middle diagonal) are sorted in **non-increasing order**.

	- The diagonals in the **top-right triangle** are sorted in **non-decreasing order**.

 
Example 1:

**Input:** grid = [[1,7,3],[9,8,2],[4,5,6]]

**Output:** [[8,2,3],[9,6,7],[4,5,1]]

**Explanation:**

The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

	- `[1, 8, 6]` becomes `[8, 6, 1]`.

	- `[9, 5]` and `[4]` remain unchanged.

The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

	- `[7, 2]` becomes `[2, 7]`.

	- `[3]` remains unchanged.

Example 2:

**Input:** grid = [[0,1],[1,2]]

**Output:** [[2,1],[1,0]]

**Explanation:**

The diagonals with a black arrow must be non-increasing, so `[0, 2]` is changed to `[2, 0]`. The other diagonals are already in the correct order.

Example 3:

**Input:** grid = [[1]]

**Output:** [[1]]

**Explanation:**

Diagonals with exactly one element are already in order, so no changes are needed.

 
**Constraints:**

	- `grid.length == grid[i].length == n`

	- `1 5 5`

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        # 1. Process diagonals in the bottom-left triangle (including main diagonal)
        # These diagonals start at grid[r][0] for r in range(n) and satisfy row - col >= 0.
        # They must be sorted in non-increasing (descending) order.
        for r in range(n):
            diag = []
            length = n - r
            for k in range(length):
                diag.append(grid[r + k][k])
            
            # Sort non-increasing
            diag.sort(reverse=True)
            
            # Write back
            for k in range(length):
                grid[r + k][k] = diag[k]

        # 2. Process diagonals in the top-right triangle
        # These diagonals start at grid[0][c] for c in range(1, n) and satisfy row - col < 0.
        # They must be sorted in non-decreasing (ascending) order.
        for c in range(1, n):
            diag = []
            length = n - c
            for k in range(length):
                diag.append(grid[k][c + k])
            
            # Sort non-decreasing
            diag.sort()
            
            # Write back
            for k in range(length):
                grid[k][c + k] = diag[k]

        return grid
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A diagonal traversing from top-left to bottom-right is uniquely characterized by the difference between its row and column indices: `r - c`.
- When `r - c >= 0`, the diagonal belongs to the **bottom-left triangle** (including the primary diagonal where `r - c == 0`).
  - These diagonals start along the first column: at `(r, 0)` for `r` from `0` to `n - 1`.
  - The problem specifies these should be sorted in **non-increasing** (descending) order.
- When `r - c < 0`, the diagonal belongs to the **top-right triangle**.
  - These diagonals start along the first row: at `(0, c)` for `c` from `1` to `n - 1`.
  - The problem specifies these should be sorted in **non-decreasing** (ascending) order.

Instead of grouping elements using a hash map which incurs extra hashing overhead, we can directly iterate over the starting point of each diagonal, extract the diagonal values into a small list, sort them according to the diagonal's condition, and write the sorted values back in place.

---

### Step-by-Step Approach

1. **Identify Matrix Dimension**: Let `n = len(grid)`.
2. **Handle Bottom-Left Diagonals (including main diagonal)**:
   - Loop `r` from `0` to `n - 1`.
   - The diagonal length starting at `(r, 0)` is `n - r`.
   - Collect elements `grid[r + k][k]` for `k` from `0` to `n - r - 1`.
   - Sort the extracted list in non-increasing order (`reverse=True`).
   - Write the values back into `grid[r + k][k]`.
3. **Handle Top-Right Diagonals**:
   - Loop `c` from `1` to `n - 1`.
   - The diagonal length starting at `(0, c)` is `n - c`.
   - Collect elements `grid[k][c + k]` for `k` from `0` to `n - c - 1`.
   - Sort the extracted list in non-decreasing order (`reverse=False`).
   - Write the values back into `grid[k][c + k]`.
4. **Return Matrix**: Return the modified `grid`.

---

### Complexity Analysis

- **Time Complexity**: 
  - There are $2n - 1$ diagonals.
  - The lengths of the diagonals are $n, n-1, n-2, \dots, 1$ in both directions.
  - Sorting a diagonal of length $L$ takes $O(L \log L)$ time.
  - Total time across all diagonals is $\sum_{L=1}^{n} O(L \log L) = O(n^2 \log n)$. Since $n^2$ is the total number of cells in the grid, this is optimal for comparison-based sorting.
- **Space Complexity**:
  - **Auxiliary Space**: $O(n)$ to store the elements of the longest diagonal (the main diagonal has length $n$) during sorting.
  - **In-place**: The grid is modified in place, so no secondary full matrix is allocated.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Confusing Diagonal Direction**: Mistaking top-left to bottom-right diagonals (`r - c = const`) with anti-diagonals (`r + c = const`).
2. **Main Diagonal Misclassification**: Forgetting whether the main diagonal (`r == c`) belongs to the bottom-left or top-right group. The problem clearly designates the middle diagonal as belonging to the bottom-left triangle.
3. **Ascending vs. Descending Order**: Swapping which triangle receives non-increasing vs. non-decreasing sort order.
4. **Off-by-one Errors on Bounds**: Forgetting that top-right diagonals start at `c = 1` rather than `c = 0` (which would re-process the main diagonal in ascending order, violating the specification).

---

### Real Interview Follow-Up Questions

#### 1. What if the matrix is stored on disk and does not fit into RAM?
- **Answer**: Diagonals access elements with a stride of `n + 1` elements in row-major layout, which causes cache misses if done naively. If the matrix is on disk, reading diagonals one by one would cause significant random I/O.
- Instead, read the matrix in chunks/blocks (row-by-row or tile-by-tile), assign elements to diagonal buffers (or external sort runs for each diagonal), sort each diagonal individually in memory (since diagonal length $n \le \text{RAM}$ even if $n^2 > \text{RAM}$), and stream the sorted values back into the respective row chunks.

#### 2. Can we achieve $O(n^2)$ time if elements are bounded integers?
- **Answer**: Yes. If elements are within a bounded integer range (e.g., $0 \le grid[i][j] \le U$), we can use Counting Sort or Radix Sort for each diagonal. This reduces the diagonal sorting time from $O(L \log L)$ to $O(L + U)$, achieving an overall time complexity of $O(n^2 + n \cdot U)$.

#### 3. How would you parallelize this operation across multiple threads or GPU?
- **Answer**: Each diagonal is completely independent of all other diagonals. We can distribute the $2n - 1$ diagonal sorting tasks across a thread pool with zero synchronization or locking needed between threads.
