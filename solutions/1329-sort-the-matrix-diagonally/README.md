# 1329. Sort the Matrix Diagonally

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/sort-the-matrix-diagonally/](https://leetcode.com/problems/sort-the-matrix-diagonally/)  
**Topics:** Array, Sorting, Matrix

---

## 📝 Problem Statement

A **matrix diagonal** is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the **matrix diagonal** starting from `mat[2][0]`, where `mat` is a `6 x 3` matrix, includes cells `mat[2][0]`, `mat[3][1]`, and `mat[4][2]`.

Given an `m x n` matrix `mat` of integers, sort each **matrix diagonal** in ascending order and return *the resulting matrix*.

 
Example 1:

```

**Input:** mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
**Output:** [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

```

Example 2:

```

**Input:** mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
**Output:** [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

```

 
**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        def sort_diagonal(start_r: int, start_c: int) -> None:
            """Collects, sorts, and writes back values along a diagonal."""
            # Collect elements along the diagonal
            vals = []
            r, c = start_r, start_c
            while r < m and c < n:
                vals.append(mat[r][c])
                r += 1
                c += 1

            # Sort the collected values
            vals.sort()

            # Write sorted elements back along the diagonal
            r, c = start_r, start_c
            for val in vals:
                mat[r][c] = val
                r += 1
                c += 1

        # Process diagonals starting along the first column (r, 0)
        for r in range(m):
            sort_diagonal(r, 0)

        # Process diagonals starting along the first row (0, c), skipping (0, 0) as it was covered
        for c in range(1, n):
            sort_diagonal(0, c)

        return mat
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A diagonal traversing from top-left to bottom-right is uniquely identified by the mathematical invariant $r - c$ (row index minus column index). Alternatively, every such diagonal begins at a unique cell located either:
1. Along the leftmost column: $(r, 0)$ for $r \in [0, m-1]$
2. Along the topmost row: $(0, c)$ for $c \in [1, n-1]$

Rather than hashing all elements into a hash table mapping $(r - c) \to \text{list}$, which consumes $O(m \times n)$ auxiliary space to store all matrix elements simultaneously, we can process each diagonal **one at a time**:
1. Traverse down the diagonal to collect its elements.
2. Sort the extracted array in-place.
3. Write the sorted values back along the exact same diagonal path.

This reduces the extra auxiliary space to just $O(\min(m, n))$, representing the maximum length of any single diagonal.

---

### Step-by-Step Approach

1. Define a helper function `sort_diagonal(start_r, start_c)`:
   - Walk from `(start_r, start_c)` in steps of `(+1, +1)` until boundary limits $m$ or $n$ are reached, recording values into an array `vals`.
   - Sort `vals` in ascending order.
   - Walk the same coordinates again, overwriting `mat[r][c]` with the sorted values from `vals`.
2. Iterate through all valid starting coordinates:
   - First column: `(r, 0)` for $r \in [0, m-1]$.
   - First row: `(0, c)` for $c \in [1, n-1]$.
3. Return the modified `mat`.

---

### Complexity Analysis

- **Time Complexity:** 
  - There are $m + n - 1$ diagonals.
  - Let $L_i$ denote the length of diagonal $i$. Notice that $\sum L_i = m \times n$, and each $L_i \le \min(m, n)$.
  - Sorting diagonal $i$ takes $O(L_i \log L_i) \le O(L_i \log(\min(m, n)))$.
  - Total time complexity:
    $$\sum O(L_i \log L_i) \le O\left(\sum L_i \cdot \log(\min(m, n))\right) = O(m \cdot n \log(\min(m, n)))$$
  - Given $m, n \le 100$, $\min(m, n) \le 100$, this executes in a few milliseconds.
  
- **Space Complexity:** 
  - **$O(\min(m, n))$** auxiliary space. At any point, we only allocate a buffer of length at most $\min(m, n)$ for the diagonal currently being processed.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Global Hash Map Memory Overhead:** Grouping all matrix cells into a dictionary `defaultdict(list)` indexed by `r - c`. While $O(m \cdot n)$ space is acceptable, it allocates full copies of the matrix and misses the chance to demonstrate optimal memory management.
2. **Double-Processing the Origin:** Including $(0, 0)$ when iterating both row starts and column starts. While idempotent, it performs duplicate work.
3. **Off-by-One / Directional Inversions:** Confusing anti-diagonals (where $r + c = \text{const}$) with main diagonals (where $r - c = \text{const}$ or moving $(+1, +1)$).

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if $1 \le mat[i][j] \le K$ where $K$ is small (e.g., $K = 100$ as in this problem)?
- **Answer:** We can replace comparison-based sorting with **Counting Sort**.
- For a diagonal of length $L$, counting sort takes $O(L + K)$ time and $O(K)$ space.
- Total time becomes $O(m \cdot n + (m + n) \cdot K)$. If $K \ll \min(m, n)$, this achieves strictly linear $O(m \cdot n)$ runtime.

#### 2. How to handle a massive matrix stored on disk (Out-of-Core / Does not fit in memory)?
- **Answer:**
  - Notice that each diagonal is completely independent of every other diagonal.
  - A diagonal can be processed as an independent streaming sequence. 
  - If row-major storage causes cache thrashing during diagonal traversals, we can chunk the matrix into sub-blocks (tiles) or sort diagonals in parallel using an external sorting framework (e.g., map-reduce where mapper outputs `(r - c, value)` pairs partitioned by diagonal ID, and reducers sort each diagonal independently).

#### 3. How would you parallelize this algorithm across multiple CPU cores?
- **Answer:**
  - Because no two diagonals share any cells, there are **zero race conditions** between sorting different diagonals.
  - We can divide the $m + n - 1$ diagonal starting points across a thread pool / multiprocessing worker pool without needing synchronization locks.
