# 0885. Spiral Matrix III

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/spiral-matrix-iii/](https://leetcode.com/problems/spiral-matrix-iii/)  
**Topics:** Array, Matrix, Simulation

---

## 📝 Problem Statement

You start at the cell `(rStart, cStart)` of an `rows x cols` grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all `rows * cols` spaces of the grid.

Return *an array of coordinates representing the positions of the grid in the order you visited them*.

 
Example 1:

```

**Input:** rows = 1, cols = 4, rStart = 0, cStart = 0
**Output:** [[0,0],[0,1],[0,2],[0,3]]

```

Example 2:

```

**Input:** rows = 5, cols = 6, rStart = 1, cStart = 4
**Output:** [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        total_cells = rows * cols
        result = [[rStart, cStart]]
        
        # Directions ordered: East, South, West, North (clockwise)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # Start facing East
        step_length = 1  # Number of steps to take in the current direction
        
        r, c = rStart, cStart
        
        while len(result) < total_cells:
            # The spiral pattern increases step length after every two turns:
            # 1 East, 1 South, 2 West, 2 North, 3 East, 3 South, etc.
            for _ in range(2):
                dr, dc = directions[d]
                for _ in range(step_length):
                    r += dr
                    c += dc
                    # Only collect coordinates that are within the grid bounds
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        if len(result) == total_cells:
                            return result
                
                # Turn 90 degrees clockwise
                d = (d + 1) % 4
            
            # Increase length for the next pair of directions
            step_length += 1
            
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires us to simulate a clockwise spiral walk beginning at `(rStart, cStart)` and moving initially East.
Observing the sequence of step counts for each direction:
- East: 1 step
- South: 1 step
- West: 2 steps
- North: 2 steps
- East: 3 steps
- South: 3 steps
- West: 4 steps
- North: 4 steps
...

Notice the rule:
1. The direction cycle is always: **East $\to$ South $\to$ West $\to$ North** (indices 0, 1, 2, 3).
2. The number of steps taken increases by 1 after every two direction changes (e.g., East & South take 1 step, West & North take 2 steps, and so on).
3. Even if we step outside the grid, we must continue tracking the walker's coordinates, but we only record the coordinate into our result list if $0 \le r < \text{rows}$ and $0 \le c < \text{cols}$.
4. The process terminates immediately once we have collected all $\text{rows} \times \text{cols}$ cells.

### Step-by-Step Approach

1. Initialize `result` with the starting position `[rStart, cStart]`.
2. Maintain `(r, c)` for current position, `d = 0` for current direction, and `step_length = 1`.
3. Loop until `len(result) == rows * cols`:
   - Run a loop 2 times (once for horizontal, once for vertical):
     - Take `step_length` individual steps in `directions[d]`.
     - After each single step, check if the cell is within valid bounds. If yes, append to `result` and exit early if all cells are visited.
     - Advance direction: `d = (d + 1) % 4`.
   - Increment `step_length += 1`.
4. Return `result`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\max(\text{rows}, \text{cols})^2)$.
  The spiral expands outward until it encloses the entire grid. In the worst case, the starting position is in one corner (e.g., bottom-right) and needs to reach the opposite corner. The maximum radius of the spiral will be at most $2 \times \max(\text{rows}, \text{cols})$. The area covered by the spiral is $\mathcal{O}((\max(\text{rows}, \text{cols}))^2)$. Since $\text{rows}, \text{cols} \le 100$, the maximum number of steps is at most $\approx (200)^2 = 40,000$ operations, which executes in a few milliseconds.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding the output array of size $\mathcal{O}(\text{rows} \times \text{cols})$).

### Common Pitfalls / Mistakes

1. **Incorrect Step Length Sequence:** Forgetting that step sizes repeat twice before incrementing (`1, 1, 2, 2, 3, 3, ...`).
2. **Bounds Checking Order:** Checking bounds before incrementing position instead of after, or skipping the simulation of positions outside the grid. Coordinates outside the grid *must* still be simulated step-by-step (or mathematically calculated) because they determine where the path re-enters the valid matrix.
3. **Missing Early Exit:** Not terminating immediately when all cells have been collected, potentially adding duplicate or extra steps unnecessarily.

### Real Interview Follow-Up Questions

#### 1. What if `rows` and `cols` are up to $10^9$, but we only want to find the $k$-th visited cell?
**Answer:** We cannot simulate step-by-step. Instead, we can skip full segments algebraically.
Each segment is a straight line of length $L$ moving in direction $\vec{d}$. We can use geometry / segment-rectangle intersection to find the number of grid points intersected in $\mathcal{O}(1)$ time per segment. We can then advance segment by segment (or binary search the spiral layer) in $\mathcal{O}(\text{layers})$ or $\mathcal{O}(1)$ without visiting every cell.

#### 2. Can we optimize the simulation so that it jumps over segments that are entirely out of bounds?
**Answer:** Yes. We can compute the bounding box of the grid. If a segment from $(r_1, c_1)$ to $(r_2, c_2)$ is strictly above, below, left, or right of the grid bounds $[0, \text{rows}-1] \times [0, \text{cols}-1]$, no cells from that segment will be added. We can simply update $(r, c)$ to the end of the segment directly without looping through each step. If it intersects the grid, we only iterate through the intersection interval $[ \max(\dots), \min(\dots) ]$.
