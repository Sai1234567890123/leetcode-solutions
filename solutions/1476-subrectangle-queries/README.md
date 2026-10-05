# 1476. Subrectangle Queries

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/subrectangle-queries/](https://leetcode.com/problems/subrectangle-queries/)  
**Topics:** Array, Design, Matrix

---

## 📝 Problem Statement

Implement the class `SubrectangleQueries` which receives a `rows x cols` rectangle as a matrix of integers in the constructor and supports two methods:

1.` updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)`

	- Updates all values with `newValue` in the subrectangle whose upper left coordinate is `(row1,col1)` and bottom right coordinate is `(row2,col2)`.

2.` getValue(int row, int col)`

	- Returns the current value of the coordinate `(row,col)` from the rectangle.

 
Example 1:

```

**Input**
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
**Output**
[null,1,null,5,5,null,10,5]
**Explanation**
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);  
// The initial rectangle (4x3) looks like:
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
// After this update the rectangle looks like:
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5 
subrectangleQueries.getValue(0, 2); // return 5
subrectangleQueries.getValue(3, 1); // return 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// After this update the rectangle looks like:
// 5   5   5
// 5   5   5
// 5   5   5
// 10  10  10 
subrectangleQueries.getValue(3, 1); // return 10
subrectangleQueries.getValue(0, 2); // return 5

```

Example 2:

```

**Input**
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
**Output**
[null,1,null,100,100,null,20]
**Explanation**
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
subrectangleQueries.getValue(0, 0); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
subrectangleQueries.getValue(0, 0); // return 100
subrectangleQueries.getValue(2, 2); // return 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
subrectangleQueries.getValue(2, 2); // return 20

```

 
**Constraints:**

	- There will be at most `500` operations considering both methods: `updateSubrectangle` and `getValue`.

	- `1

---

## 💻 Implementation (python3)

```py
class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        """
        Initialize the object with the given matrix and an empty list of updates.
        """
        self.rect = rectangle
        # Stores history of updates as tuples: (row1, col1, row2, col2, newValue)
        self.updates: list[tuple[int, int, int, int, int]] = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        """
        Records the update operation in O(1) time without modifying the underlying grid.
        """
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        """
        Retrieves the value at (row, col) by checking updates in reverse chronological order.
        If no update covers the cell, returns the original matrix value.
        """
        # Iterate backwards from most recent update to oldest
        for r1, c1, r2, c2, val in reversed(self.updates):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        
        # Fall back to initial value if never overwritten
        return self.rect[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires supporting two operations on a 2D grid:
1. Update a subrectangle `(row1, col1)` to `(row2, col2)` with `newValue`.
2. Retrieve the value at coordinate `(row, col)`.

There are two primary paradigms to approach this problem:

1. **Eager Update (Brute-Force In-Place)**:
   - Directly modify every cell within `[row1..row2] x [col1..col2]`.
   - Update takes $O((row2 - row1 + 1) \times (col2 - col1 + 1)) \approx O(R \times C)$.
   - Query takes $O(1)$.
   
2. **Lazy History Tracking (Optimal for frequent updates & limited operation count)**:
   - Instead of immediately rewriting cells in the grid, record each update as a bounding box `(row1, col1, row2, col2, newValue)` in an operations log.
   - `updateSubrectangle` runs in $O(1)$ time by simply appending the update to the list.
   - `getValue(row, col)` inspects the log in **reverse chronological order**. The most recent update containing `(row, col)` gives the correct value. If no update covers `(row, col)`, fall back to the initial grid value.

Given the constraint of at most $500$ operations total, the lazy approach guarantees $O(1)$ updates and at most $500$ checks per query (running in sub-millisecond time), completely avoiding the costly cell-by-cell write overhead of up to $10,000$ operations per update.

---

### Step-by-Step Approach

1. **Initialization (`__init__`)**:
   - Retain a reference to the initial `rectangle`.
   - Initialize an empty list `self.updates` to store the history of update calls.

2. **Update (`updateSubrectangle`)**:
   - Append `(row1, col1, row2, col2, newValue)` to `self.updates`. Time complexity is $O(1)$.

3. **Query (`getValue`)**:
   - Traverse `self.updates` from end to beginning (`reversed(self.updates)`).
   - Check if `row1 <= row <= row2` and `col1 <= col <= col2`.
   - If a match is found, immediately return `newValue` because this is the latest modification applied to this cell.
   - If no update contains the coordinate, return `self.rect[row][col]`.

---

### Complexity Analysis

- **Time Complexity**:
  - `__init__`: $O(1)$ auxiliary time (holds reference to input matrix).
  - `updateSubrectangle`: $O(1)$ per operation.
  - `getValue`: $O(U)$ per operation, where $U$ is the number of updates made so far ($U \le 500$). At worst, $500$ simple range checks are performed.
  
- **Space Complexity**:
  - $O(U)$ auxiliary space to store the update operations, where $U \le 500$.
  - Space occupied by the initial grid is $O(R \times C)$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Over-engineering with 2D Segment Trees**:
   - Candidates often jump straight into 2D Segment Trees or 2D Fenwick Trees with lazy propagation. While theoretically interesting, a 2D Range Update Point Query Segment Tree requires complex dynamic node allocation and has huge constant factors, which is entirely overkill for $500$ operations.

2. **Ignoring the Read/Write Trade-off**:
   - In interviews, failing to ask about the ratio of `update` calls vs. `getValue` calls. If queries vastly outnumber updates, the eager in-place method ($O(R \times C)$ update, $O(1)$ query) might be favored. When updates are frequent or bounds are small, the lazy history method is strictly superior.

3. **Forward Iteration Instead of Backward**:
   - Checking updates from oldest to newest requires scanning all updates without early-stopping. Checking in reverse chronological order allows terminating immediately upon the first enclosing rectangle.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if `getValue` calls are called millions of times and updates are rare?
**Answer**: 
If the workload is heavily read-heavy, switch to the eager approach:
- Perform in-place updates directly on the matrix in $O(R \times C)$.
- `getValue` performs a direct array index access in $O(1)$ time.

#### 2. What if both the grid size ($10^5 \times 10^5$) and the number of operations ($10^5$) are very large?
**Answer**:
- If coordinates are large and queries/updates are both frequent, we can use a **2D Segment Tree with Lazy Propagation** or a **QuadTree**.
- Alternatively, if queries are offline, we can use a 2D sweep-line algorithm with a 1D segment tree over the active intervals.

#### 3. How would you handle concurrency / multi-threaded access?
**Answer**:
- **Read-Write Lock (e.g., `threading.RWMutex`)**: Allow multiple concurrent `getValue` calls simultaneously (shared read lock). Require an exclusive write lock for `updateSubrectangle`.
- **Copy-On-Write / Persistent Data Structures**: Maintain an immutable version history (append-only list with snapshot pointers). Readers read the latest snapshot lock-free using atomic pointer swaps.
