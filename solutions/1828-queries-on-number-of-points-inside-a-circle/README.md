# 1828. Queries on Number of Points Inside a Circle

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/](https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/)  
**Topics:** Array, Math, Geometry

---

## 📝 Problem Statement

You are given an array `points` where `points[i] = [xi, yi]` is the coordinates of the `ith` point on a 2D plane. Multiple points can have the **same** coordinates.

You are also given an array `queries` where `queries[j] = [xj, yj, rj]` describes a circle centered at `(xj, yj)` with a radius of `rj`.

For each query `queries[j]`, compute the number of points **inside** the `jth` circle. Points **on the border** of the circle are considered **inside**.

Return *an array *`answer`*, where *`answer[j]`* is the answer to the *`jth`* query*.

 
Example 1:

```

**Input:** points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
**Output:** [3,2,2]
**Explanation: **The points and circles are shown above.
queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.

```

Example 2:

```

**Input:** points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
**Output:** [2,3,2,4]
**Explanation: **The points and circles are shown above.
queries[0] is green, queries[1] is red, queries[2] is blue, and queries[3] is purple.

```

 
**Constraints:**

	- `1 ​​​​​​i, y​​​​​​i j, yj j 

 
**Follow up:** Could you find the answer for each query in better complexity than `O(n)`?

---

## 💻 Implementation (python3)

```py
from bisect import bisect_left, bisect_right

class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        # Sort points by their x-coordinates to allow pruning queries via binary search
        points.sort(key=lambda p: p[0])
        x_coords = [p[0] for p in points]
        
        ans = []
        for cx, cy, r in queries:
            r_squared = r * r
            
            # Points inside the circle must satisfy: cx - r <= px <= cx + r
            left_idx = bisect_left(x_coords, cx - r)
            right_idx = bisect_right(x_coords, cx + r)
            
            count = 0
            for i in range(left_idx, right_idx):
                px, py = points[i]
                dx = px - cx
                dy = py - cy
                # Euclidean distance squared comparison to avoid floating-point errors
                if dx * dx + dy * dy <= r_squared:
                    count += 1
            
            ans.append(count)
            
        return ans
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A point $(p_x, p_y)$ lies inside or on the boundary of a circle centered at $(c_x, c_y)$ with radius $r$ if and only if the Euclidean distance between them is at most $r$:
$$\sqrt{(p_x - c_x)^2 + (p_y - c_y)^2} \le r \iff (p_x - c_x)^2 + (p_y - c_y)^2 \le r^2$$

Working with squared distances avoids computing square roots, which prevents floating-point precision issues and significantly speeds up runtime.

#### Optimizing beyond naive $O(N \cdot Q)$
A naive check evaluates every point for every query ($O(N \cdot Q)$). To address the follow-up ("better complexity than $O(N)$ per query"):
1. **1D Coordinate Pruning (Binary Search)**:
   Any point inside the circle must lie within the bounding box of the circle, specifically $c_x - r \le p_x \le c_x + r$.
   By sorting `points` by their $x$-coordinates once in $O(N \log N)$, we can use binary search (`bisect_left` and `bisect_right`) to isolate only the points within the horizontal span $[c_x - r, c_x + r]$. For uniform point distributions, this reduces the candidate pool substantially.

### Step-by-Step Approach

1. **Sort Points**: Sort `points` in ascending order of $x$-coordinate and extract an array `x_coords` for fast binary searches.
2. **Process Each Query**:
   - For a query $(c_x, c_y, r)$, determine the range $[c_x - r, c_x + r]$.
   - Use `bisect_left` to find the first point with $p_x \ge c_x - r$.
   - Use `bisect_right` to find the upper bound where $p_x \le c_x + r$.
3. **Filter Candidates**:
   - Loop only over the slice of points between `left_idx` and `right_idx`.
   - Increment the counter if $(p_x - c_x)^2 + (p_y - c_y)^2 \le r^2$.
4. **Return Results**: Collect and return counts for each query.

### Complexity Analysis

- **Time Complexity**:
  - **Sorting**: $O(N \log N)$ where $N$ is the number of points.
  - **Per Query**:
    - Binary search takes $O(\log N)$.
    - Candidate iteration: In the worst case (all points have the same $x$-coordinate or fall in the range), $O(N)$. On average for uniformly distributed points over a 2D region, only a fraction of points proportional to $\frac{2r}{\text{range}_x}$ are checked.
    - Thus, total query time is $O(Q \log N + Q \cdot K_{\text{avg}})$, which is significantly faster than $O(N \cdot Q)$ in practice.
- **Space Complexity**:
  - $O(N)$ auxiliary space for sorting and storing the separated `x_coords` array (in addition to $O(Q)$ for the output list).

### Common Pitfalls / Mistakes Candidates Make

1. **Using Floating-Point `sqrt`**:
   Using `math.sqrt(dx*dx + dy*dy) <= r` can introduce floating-point inaccuracies on border cases and is computationally slower than integer multiplication `dx*dx + dy*dy <= r*r`.
2. **Strict Inequality (`<`) instead of Non-Strict (`<=`)**:
   Points on the boundary are considered *inside* the circle. Using `<` fails on boundary points.
3. **Missed Follow-up on Spatial Indexing**:
   Many candidates only write the $O(N \cdot Q)$ loop without mentioning spatial pruning or data structures like k-d Trees / QuadTrees.

### Real Interview Follow-Up Questions & Answers

#### 1. How would you achieve true sub-linear time ($O(\sqrt{N} + K)$ or $O(\log N + K)$) per query?
- **Answer**: We can construct a **2D k-d Tree** or a **QuadTree**.
  - A k-d tree recursively splits points along alternating $x$ and $y$ axes.
  - When querying a circle, we check if the bounding box of a k-d tree node intersects the circle. If it does not, we prune the entire subtree. If the bounding box is fully contained inside the circle, we can immediately add the subtree size without inspecting individual points.
  - This achieves an average query time of $O(\sqrt{N} + K)$, where $K$ is the number of reported points.

#### 2. What if $N$ and $Q$ are massive (e.g., $10^7$ points and queries) and coordinates are geographically bounded?
- **Answer**: Use **Spatial Hashing / Geohashing / Grid Indexing (e.g., Uber's H3 or Google's S2)**:
  - Divide the 2D plane into a uniform grid with cell size proportional to average circle radii.
  - Hash points into their corresponding grid cells.
  - For each query, determine all grid cells that overlap with the bounding box of the circle and only inspect points in those cells.

#### 3. How would you handle a streaming scenario where points are inserted/deleted continuously while queries are being made concurrently?
- **Answer**:
  - Use a concurrent spatial index such as an **R-Tree** or **Dynamic QuadTree** protected by fine-grained read-write locks (`RWLock`) or lock-free data structures.
  - Reads (queries) acquire shared read locks on tree branches/nodes, allowing concurrent querying without blocking other queries.
  - Writes (point insertions/removals) acquire exclusive write locks localized to the affected bounding boxes or leaf nodes.
