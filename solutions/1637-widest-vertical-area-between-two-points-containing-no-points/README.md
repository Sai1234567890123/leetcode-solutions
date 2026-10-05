# 1637. Widest Vertical Area Between Two Points Containing No Points

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/)  
**Topics:** Array, Sorting

---

## 📝 Problem Statement

Given `n` `points` on a 2D plane where `points[i] = [xi, yi]`, Return* the **widest vertical area** between two points such that no points are inside the area.*

A **vertical area** is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The **widest vertical area** is the one with the maximum width.

Note that points **on the edge** of a vertical area **are not** considered included in the area.

 
Example 1:
​
```

**Input:** points = [[8,7],[9,9],[7,4],[9,7]]
**Output:** 1
**Explanation:** Both the red and the blue area are optimal.

```

Example 2:

```

**Input:** points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
**Output:** 3

```

 
**Constraints:**

	- `n == points.length`

	- `2 5`

	- `points[i].length == 2`

	- `0 i, yi 9`

---

## 💻 Implementation (python3)

```py
class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        # Extract and sort only the x-coordinates, since the y-coordinates
        # have no bearing on the vertical area's width (infinite height).
        x_coords = sorted(p[0] for p in points)
        
        # Find the maximum gap between any two adjacent x-coordinates.
        max_width = 0
        for i in range(1, len(x_coords)):
            gap = x_coords[i] - x_coords[i - 1]
            if gap > max_width:
                max_width = gap
                
        return max_width
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the widest vertical strip of the 2D plane extending infinitely in the $y$-direction that contains no points strictly inside it. 

Key Observations:
1. **$y$-coordinates are irrelevant:** A vertical area extends from $-\infty$ to $+\infty$ along the $y$-axis. The vertical boundaries are lines of the form $x = a$ and $x = b$. The $y$-coordinates of points have zero impact on the horizontal width between these vertical lines.
2. **Consecutive $x$-coordinates:** Any point with an $x$-coordinate between $a$ and $b$ (i.e., $a < x < b$) would violate the condition that no points are inside the area. Therefore, the boundary lines $x = a$ and $x = b$ must be formed by **consecutively adjacent** distinct $x$-coordinates when sorted.
3. **Reduction to Maximum Gap:** The problem reduces to extracting all $x$-coordinates, sorting them, and finding the maximum difference between two adjacent values in the sorted order.

### Step-by-Step Approach

1. Extract the $x$-coordinate from each pair $[x_i, y_i]$.
2. Sort the extracted $x$-coordinates in ascending order.
3. Iterate through the sorted $x$-coordinates, tracking the maximum difference `x_coords[i] - x_coords[i - 1]`.
4. Return the maximum difference found.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n \log n)$, where $n$ is the number of points. Extracting the $x$-coordinates takes $\mathcal{O}(n)$, and sorting them takes $\mathcal{O}(n \log n)$ using Timsort. The linear scan takes $\mathcal{O}(n)$.
- **Space Complexity:** $\mathcal{O}(n)$ to store the extracted list of $x$-coordinates. (Alternatively, sorting `points` in-place by the first coordinate requires $\mathcal{O}(\log n)$ auxiliary space for Timsort's recursion stack).

---

### Common Pitfalls / Mistakes Candidates Make

1. **Overcomplicating with 2D Data Structures:** Candidates often attempt to use 2D spatial data structures (like KD-Trees, QuadTrees, or sweep-line algorithms with interval trees) because the input is presented as 2D coordinates.
2. **Ignoring Duplicate $x$-Coordinates:** Multiple points can share the exact same $x$-coordinate. The difference between identical adjacent $x$-coordinates is $0$, which naturally does not affect the maximum gap, but candidates sometimes add unnecessary deduplication logic or handle it incorrectly.
3. **Misinterpreting Boundary Conditions:** The problem states points *on the edge* are not inside the area. If they were considered inside, empty widths would be restricted differently.

---

### Real Interview Follow-Up Questions

#### 1. Can we solve this in $\mathcal{O}(n)$ time?
**Answer:** Yes, this is identical to LeetCode 164 (*Maximum Gap*). By applying the **Pigeonhole Principle** and **Bucket Sort**:
- Find $min(x)$ and $max(x)$.
- Create $n - 1$ buckets of uniform width $w = \max(1, \lfloor(max - min) / (n - 1)\rfloor)$.
- Each bucket only needs to store its minimum and maximum elements.
- The maximum gap cannot occur within the same bucket (since bucket width is less than the average gap), so it must be the difference between the minimum of a non-empty bucket and the maximum of the previous non-empty bucket.
- This achieves $\mathcal{O}(n)$ time and $\mathcal{O}(n)$ space.

#### 2. What if the dataset is too massive to fit into RAM (External Memory / Big Data)?
**Answer:**
- If $n \gg 10^9$, we cannot sort in memory.
- We can use **External Merge Sort** or distributed computing (e.g., Apache Spark/MapReduce). 
- In MapReduce: Partition points by ranges of $x$-coordinates into sorted partitions, sort each partition locally, and compare boundary elements between adjacent partitions.

#### 3. How would you handle a real-time stream of points?
**Answer:**
- If points arrive dynamically and we need to query the maximum vertical area at any time:
  - Maintain a **Balanced Binary Search Tree** (or Skip List) containing the sorted distinct $x$-coordinates.
  - Maintain a **Max-Heap** (or multiset/treap) of the adjacent differences (`gaps`).
  - Upon inserting a new $x$: find its predecessor $x_{prev}$ and successor $x_{next}$ in $\mathcal{O}(\log n)$. Remove the old gap $(x_{next} - x_{prev})$ and insert $(x - x_{prev})$ and $(x_{next} - x)$.
  - Time per insertion: $\mathcal{O}(\log n)$; Query time: $\mathcal{O}(1)$.
