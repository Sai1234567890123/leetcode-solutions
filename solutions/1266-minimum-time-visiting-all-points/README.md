# 1266. Minimum Time Visiting All Points

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/minimum-time-visiting-all-points/](https://leetcode.com/problems/minimum-time-visiting-all-points/)  
**Topics:** Array, Math, Geometry

---

## 📝 Problem Statement

On a 2D plane, there are `n` points with integer coordinates `points[i] = [xi, yi]`. Return *the **minimum time** in seconds to visit all the points in the order given by *`points`.

You can move according to these rules:

	In `1` second, you can either:

	
		- move vertically by one unit,

		- move horizontally by one unit, or

		- move diagonally `sqrt(2)` units (in other words, move one unit vertically then one unit horizontally in `1` second).

	
	
	- You have to visit the points in the same order as they appear in the array.

	- You are allowed to pass through points that appear later in the order, but these do not count as visits.

 
Example 1:

```

**Input:** points = [[1,1],[3,4],[-1,0]]
**Output:** 7
**Explanation: **One optimal path is **[1,1]** -> [2,2] -> [3,3] -> **[3,4] **-> [2,3] -> [1,2] -> [0,1] -> **[-1,0]**   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
```

Example 2:

```

**Input:** points = [[3,2],[-2,2]]
**Output:** 5

```

 
**Constraints:**

	- `points.length == n`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total_time = 0
        
        # Traverse through each consecutive pair of points
        for i in range(len(points) - 1):
            dx = abs(points[i + 1][0] - points[i][0])
            dy = abs(points[i + 1][1] - points[i][1])
            
            # The minimum steps between two points allowing diagonal moves is
            # max(dx, dy) (Chebyshev distance / L_infinity norm).
            # Moving diagonally covers 1 horizontal and 1 vertical unit simultaneously in 1 second.
            total_time += max(dx, dy)
            
        return total_time
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the minimum time to travel between a series of 2D points in sequential order. 

In one second, we can move:
1. Horizontally: $(\pm 1, 0)$
2. Vertically: $(0, \pm 1)$
3. Diagonally: $(\pm 1, \pm 1)$

To travel from $(x_1, y_1)$ to $(x_2, y_2)$, let $\Delta x = |x_1 - x_2|$ and $\Delta y = |y_1 - y_2|$. 
Since diagonal movements allow us to reduce both the horizontal and vertical distances simultaneously by $1$ unit per second, we should move diagonally as much as possible—specifically for $\min(\Delta x, \Delta y)$ seconds. 

After doing that, one of the coordinates will match the target, and we are left with $|\Delta x - \Delta y|$ units along the remaining axis, which must be traversed horizontally or vertically (1 unit per second).

Thus, the total time required between two points is:
$$\min(\Delta x, \Delta y) + |\Delta x - \Delta y| = \max(\Delta x, \Delta y)$$

This metric is mathematically known as the **Chebyshev distance** (or $L_\infty$ distance). Because we must visit points in the exact order given, the total minimum time is simply the sum of Chebyshev distances between each consecutive pair of points.

---

### Step-by-Step Approach

1. Initialize `total_time = 0`.
2. Iterate through the array from index `0` to `len(points) - 2`.
3. For each pair of consecutive points $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$:
   - Calculate $\Delta x = |x_{i+1} - x_i|$.
   - Calculate $\Delta y = |y_{i+1} - y_i|$.
   - Add $\max(\Delta x, \Delta y)$ to `total_time`.
4. Return `total_time`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the number of points. We iterate through the list of points once and perform constant-time $\mathcal{O}(1)$ arithmetic operations for each pair.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. Only a few primitive scalar variables (`total_time`, `dx`, `dy`) are maintained.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Simulating Step-by-Step:** Attempting to simulate the movement unit-by-unit using loops or BFS. Given coordinate ranges up to $1000$ (and potentially larger in generalized settings), simulation is inefficient and overcomplicates the logic.
2. **Confusing Distance Metrics:** Using Manhattan distance ($|x_1 - x_2| + |y_1 - y_2|$) or Euclidean distance ($\sqrt{\Delta x^2 + \Delta y^2}$) instead of Chebyshev distance.
3. **Off-by-One in Iteration:** Looping up to `len(points)` instead of `len(points) - 1`, leading to `IndexOutOfBoundsException`.
4. **Order of Points:** Trying to reorder the points to find an optimal traveling salesman tour. The problem explicitly states that points must be visited *in the order given*.

---

### Real Interview Follow-Up Questions

#### 1. What if the points are arriving in a continuous data stream?
- **Answer:** We only need the coordinates of the *previous* point to compute the incremental time for the incoming point. We can maintain a single state variable `prev_point` and `total_time`. Each new point updates `total_time += max(abs(curr.x - prev.x), abs(curr.y - prev.y))` and replaces `prev_point = curr`, achieving $\mathcal{O}(1)$ processing time and $\mathcal{O}(1)$ memory per stream event.

#### 2. What if diagonal moves cost more time than horizontal/vertical moves (e.g., diagonal takes $c$ seconds where $c > 1$)?
- **Answer:** 
  - If $c \ge 2$, diagonal moves are never optimal. The distance is the Manhattan distance: $\Delta x + \Delta y$.
  - If $1 < c < 2$, diagonal moves are still cheaper than two straight moves. We take $\min(\Delta x, \Delta y)$ diagonal steps (costing $c \times \min(\Delta x, \Delta y)$) plus $|\Delta x - \Delta y|$ straight steps (costing $1 \times |\Delta x - \Delta y|$).
  - Formula: $c \cdot \min(\Delta x, \Delta y) + |\Delta x - \Delta y|$.

#### 3. What if the points do NOT have to be visited in the order given (Traveling Salesperson Problem variant)?
- **Answer:** If any visitation order is allowed, this transforms into the metric Traveling Salesperson Problem (TSP) with Chebyshev metric, which is NP-hard. For small $n \le 20$, it can be solved in $\mathcal{O}(n^2 2^n)$ time using Held-Karp dynamic programming with bitmasking. For larger $n$, approximation algorithms (such as Christofides' algorithm providing a $1.5$-approximation) or metaheuristics (2-opt, simulated annealing) would be needed.
