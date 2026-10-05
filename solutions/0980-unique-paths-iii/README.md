# 0980. Unique Paths III

**Difficulty:** Hard  
**LeetCode Link:** [https://leetcode.com/problems/unique-paths-iii/](https://leetcode.com/problems/unique-paths-iii/)  
**Topics:** Array, Backtracking, Bit Manipulation, Matrix, Hamiltonian Path

---

## 📝 Problem Statement

You are given an `m x n` integer array `grid` where `grid[i][j]` could be:

	- `1` representing the starting square. There is exactly one starting square.

	- `2` representing the ending square. There is exactly one ending square.

	- `0` representing empty squares we can walk over.

	- `-1` representing obstacles that we cannot walk over.

Return *the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once*.

 
Example 1:

```

**Input:** grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
**Output:** 2
**Explanation:** We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

```

Example 2:

```

**Input:** grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
**Output:** 4
**Explanation:** We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

```

Example 3:

```

**Input:** grid = [[0,1],[2,0]]
**Output:** 0
**Explanation:** There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

```

 
**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        start_r, start_c = 0, 0
        # Count total non-obstacle squares that must be visited.
        # Include start (1) and empty squares (0).
        empty_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    empty_count += 1
                elif grid[r][c] == 0:
                    empty_count += 1

        total_paths = 0

        def backtrack(r: int, c: int, remaining: int) -> None:
            nonlocal total_paths
            
            # Base case: Reached the ending square
            if grid[r][c] == 2:
                # Valid path only if all empty squares and start square have been visited
                if remaining == 0:
                    total_paths += 1
                return

            # Mark current square as visited by temporarily setting it to an obstacle
            temp = grid[r][c]
            grid[r][c] = -1

            # Explore all 4 orthogonal directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    backtrack(nr, nc, remaining - 1)

            # Backtrack / unmark the current square
            grid[r][c] = temp

        # Start backtracking from the starting cell.
        # remaining represents non-obstacle squares (excluding end cell '2') left to step off from.
        backtrack(start_r, start_c, empty_count)
        return total_paths
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the number of paths from square `1` to square `2` that visit every non-obstacle square exactly once. This is the **Hamiltonian Path Problem** on a grid graph. Hamiltonian path is NP-hard in general, but the constraints here specify $m \times n \le 20$. 

Given $m \times n \le 20$:
1. A straightforward **Depth-First Search (DFS) with backtracking** is well within the execution time limits.
2. In each step, we can move in 4 directions, but each visited square becomes an obstacle for future moves along the current path.
3. Because the path cannot intersect itself and dead-ends are pruned immediately, the effective branching factor is significantly less than 4 (typically between 1.5 and 2.5).
4. In-place modification of `grid` avoids allocating extra memory for a `visited` set or 2D boolean array, optimizing both cache locality and memory overhead.

### Step-by-Step Approach

1. **Pre-computation**:
   - Scan the grid to locate the start cell (`1`) and count the number of cells that must be traversed (start cell `1` + all empty cells `0`).
2. **Backtracking DFS**:
   - Function signature: `backtrack(r, c, remaining)`.
   - **Base condition**: If `grid[r][c] == 2`, check if `remaining == 0`. If so, all non-obstacle cells have been visited; increment the path count. Return regardless.
   - **State modification**: Temporarily mark `grid[r][c] = -1` (visited).
   - **Recursive exploration**: For each orthogonal neighbor `(nr, nc)` that is within bounds and not an obstacle (`grid[nr][nc] != -1`), recursively call `backtrack(nr, nc, remaining - 1)`.
   - **Backtrack**: Restore `grid[r][c]` to its original value so other paths can use it.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(3^k)$ or $\mathcal{O}(4 \cdot 3^{k-1})$ in the worst-case, where $k$ is the number of empty squares ($k \le 20$). In practice, the search tree is drastically smaller due to boundary walls, self-avoiding path constraints, and obstacles. The search terminates in tens of milliseconds for $m \times n \le 20$.
- **Space Complexity**: $\mathcal{O}(k)$ auxiliary stack space for the recursion depth, where $k \le 20$. Modifying the input grid in-place gives $\mathcal{O}(1)$ additional heap space.

---

### Common Pitfalls / Mistakes

1. **Forgetting to count the starting square**: The starting square `1` is part of the path, so it must be counted when tracking the required number of steps to reach `2`.
2. **Checking the destination too late or too early**:
   - If you check whether `grid[r][c] == 2` after decrementing or inside the neighbor loop incorrectly, you might count paths that hit `2` prematurely before visiting all other cells.
   - Marking `2` as visited without verifying whether all cells were covered can introduce bugs if not handled cleanly at the base case.
3. **Not backtracking in-place mutations**: Forgetting to restore `grid[r][c]` to its original value after the recursive calls leads to incomplete path exploration.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if $m \times n$ is up to $30$ or $36$? How do you optimize?
- **Bitmask Dynamic Programming / Memoization**: If $m \times n \le 25$, we can represent visited states as an integer bitmask: `dp(r, c, mask)`.
- **Connectivity / Reachability Pruning**: Before continuing DFS, perform a quick BFS/DFS or disjoint-set check. If any remaining unvisited cells are disconnected from each other or from the target cell `2`, the current branch cannot form a valid Hamiltonian path and can be pruned immediately.
- **Dead-end Detection (Degree Check)**: Any unvisited cell (other than the destination `2`) must have at least 2 available unvisited neighbors (entry and exit). If any unvisited cell has degree $< 2$, or the destination has degree $< 1$, we can prune immediately.

#### 2. How would you solve this if $m \times n$ was larger (e.g., $10 \times 10$) using distributed computing / parallelization?
- Use parallel backtracking: Generate the search tree up to depth $D$ (e.g., $D = 8$) sequentially to create independent path prefixes.
- Dispatch each prefix as an independent job to worker nodes/threads via a work-stealing queue or distributed task runner (e.g., Ray, Celery).
- Workers sum their local path counts and return the reduction result to the coordinator.
