# 1572. Matrix Diagonal Sum

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/matrix-diagonal-sum/](https://leetcode.com/problems/matrix-diagonal-sum/)  
**Topics:** Array, Matrix

---

## 📝 Problem Statement

Given a square matrix `mat`, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 
Example 1:

```

**Input:** mat = [[**1**,2,**3**],
              [4,**5**,6],
              [**7**,8,**9**]]
**Output:** 25
**Explanation: **Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

```

Example 2:

```

**Input:** mat = [[**1**,1,1,**1**],
              [1,**1**,**1**,1],
              [1,**1**,**1**,1],
              [**1**,1,1,**1**]]
**Output:** 8

```

Example 3:

```

**Input:** mat = [[**5**]]
**Output:** 5

```

 
**Constraints:**

	- `n == mat.length == mat[i].length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total_sum = 0
        
        for i in range(n):
            # Add element from the primary diagonal
            total_sum += mat[i][i]
            
            # Add element from the secondary diagonal only if it's not the intersection
            secondary_col = n - 1 - i
            if i != secondary_col:
                total_sum += mat[i][secondary_col]
                
        return total_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A square matrix of dimension $n \times n$ has two main diagonals:
1. **Primary Diagonal**: Extends from the top-left to the bottom-right. Elements are indexed as `mat[i][i]` for $0 \le i < n$.
2. **Secondary Diagonal**: Extends from the top-right to the bottom-left. Elements are indexed as `mat[i][n - 1 - i]` for $0 \le i < n$.

The key observation is that when $n$ is odd, the primary and secondary diagonals intersect at the exact center element, located at `mat[n // 2][n // 2]`. The problem statement requires that overlapping elements be counted only once.

Rather than iterating over all $n^2$ elements in the matrix, we can traverse row-by-row in a single loop from $0$ to $n - 1$:
- Add `mat[i][i]`.
- Check if the secondary diagonal coordinate `(i, n - 1 - i)` is distinct from `(i, i)`. If it is distinct (i.e., `i != n - 1 - i`), add `mat[i][n - 1 - i]`.

### Step-by-Step Approach

1. Determine the size of the square matrix $n = \text{len}(mat)$.
2. Initialize an accumulator variable `total_sum = 0`.
3. Loop $i$ from $0$ to $n - 1$:
   - Add `mat[i][i]` to `total_sum`.
   - If $i \neq n - 1 - i$, add `mat[i][n - 1 - i]` to `total_sum`.
4. Return `total_sum`.

*Alternative clean approach:* Add both diagonals completely and subtract the center element `mat[n // 2][n // 2]` if $n \% 2 \neq 0$. Both approaches are $O(n)$ time and $O(1)$ space.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the number of rows (or columns) in the matrix. We iterate through the matrix exactly once with a single loop of size $n$, accessing at most two elements per row. This is optimal since any algorithm must inspect at least the diagonal elements.
- **Space Complexity:** $O(1)$ auxiliary space. Only a few integer variables are used.

### Common Pitfalls / Mistakes Candidates Make

1. **$O(n^2)$ Traversal**: Iterating over every cell `mat[i][j]` using nested loops and checking `if i == j or i + j == n - 1`. While correct, this does $n^2$ operations instead of $n$. In an interview, failing to optimize from $O(n^2)$ to $O(n)$ for a simple traversal stands out negatively.
2. **Double Counting the Center**: Simply summing `mat[i][i] + mat[i][n - 1 - i]` without accounting for odd $n$ causes the center element to be counted twice.
3. **Integer Overflow**: In languages with fixed-width integers like C++ or Java, if matrix elements can be very large (e.g., $10^9$) or matrix dimensions are huge, the sum can exceed $2^{31}-1$. In Python, integers have arbitrary precision, but it is always good practice to mention this to the interviewer.

### Real Interview Follow-Up Questions & Answers

#### 1. What if the matrix is too large to fit in memory (e.g., stored on disk in row-major order)?
**Answer:** Because we only need `mat[i][i]` and `mat[i][n - 1 - i]` for each row $i$, we can stream the file row-by-row. We only need to hold one row in memory at any given time (requiring $O(n)$ memory instead of $O(n^2)$). If seeking is supported on disk, we can use direct byte offsets to seek and read only the two target elements per row, requiring $O(1)$ memory and minimal I/O.

#### 2. How would you parallelize this computation across multiple threads/cores?
**Answer:** The summation of elements across rows is an associative and commutative operation (a reduction). We can divide the rows $[0, n-1]$ into $k$ disjoint chunks and assign each chunk to a worker thread. Each thread computes its local sum, and a final reduction step sums the results. This achieves near-linear speedup with zero lock contention.

#### 3. What if the input matrix is sparse (represented as a Coordinate list / CSR format)?
**Answer:** 
- In a coordinate list (COO) format `(row, col, value)`, we can filter for entries where `row == col` or `row + col == n - 1`.
- In a Compressed Sparse Row (CSR) format, for each row $i$, we perform a binary search or hash lookup within that row's column index array to find columns $i$ and $n - 1 - i$. If non-zero values are scarce, this can be significantly faster than iterating through dense zero values.
