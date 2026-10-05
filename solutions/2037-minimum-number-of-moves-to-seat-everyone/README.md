# 2037. Minimum Number of Moves to Seat Everyone

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/)  
**Topics:** Array, Greedy, Sorting, Counting Sort

---

## 📝 Problem Statement

There are `n` **availabe **seats and `n` students **standing** in a room. You are given an array `seats` of length `n`, where `seats[i]` is the position of the `ith` seat. You are also given the array `students` of length `n`, where `students[j]` is the position of the `jth` student.

You may perform the following move any number of times:

	- Increase or decrease the position of the `ith` student by `1` (i.e., moving the `ith` student from position `x` to `x + 1` or `x - 1`)

Return *the **minimum number of moves** required to move each student to a seat** such that no two students are in the same seat.*

Note that there may be **multiple** seats or students in the **same **position at the beginning.

 
Example 1:

```

**Input:** seats = [3,1,5], students = [2,7,4]
**Output:** 4
**Explanation:** The students are moved as follows:
- The first student is moved from position 2 to position 1 using 1 move.
- The second student is moved from position 7 to position 5 using 2 moves.
- The third student is moved from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.

```

Example 2:

```

**Input:** seats = [4,1,5,9], students = [1,3,2,6]
**Output:** 7
**Explanation:** The students are moved as follows:
- The first student is not moved.
- The second student is moved from position 3 to position 4 using 1 move.
- The third student is moved from position 2 to position 5 using 3 moves.
- The fourth student is moved from position 6 to position 9 using 3 moves.
In total, 0 + 1 + 3 + 3 = 7 moves were used.

```

Example 3:

```

**Input:** seats = [2,2,6,6], students = [1,3,2,6]
**Output:** 4
**Explanation:** Note that there are two seats at position 2 and two seats at position 6.
The students are moved as follows:
- The first student is moved from position 1 to position 2 using 1 move.
- The second student is moved from position 3 to position 6 using 3 moves.
- The third student is not moved.
- The fourth student is not moved.
In total, 1 + 3 + 0 + 0 = 4 moves were used.

```

 
**Constraints:**

	- `n == seats.length == students.length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        """
        Calculates the minimum moves required to seat all students.
        
        Using the greedy property (Monge property / 1D optimal transport):
        Matching the i-th smallest student position with the i-th smallest seat position
        guarantees the minimum total displacement without crossings.
        """
        # Sort both lists in non-decreasing order
        seats.sort()
        students.sort()
        
        # Sum the absolute differences between matched pairs
        return sum(abs(seat - student) for seat, student in zip(seats, students))
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for an optimal matching between $n$ students and $n$ seats along a 1-dimensional line to minimize the total Manhattan distance (sum of absolute differences).

Consider two students at positions $A$ and $B$ (with $A \le B$) and two seats at positions $X$ and $Y$ (with $X \le Y$).
There are two possible assignments:
1. Student $A \to X$ and Student $B \to Y$, costing $|A - X| + |B - Y|$.
2. Student $A \to Y$ and Student $B \to X$, costing $|A - Y| + |B - X|$.

By the triangle inequality and properties of 1D metric spaces (also known as the Monge property or 1D optimal transport), the "non-crossing" matching always yields a cost less than or equal to the "crossing" matching:
$$|A - X| + |B - Y| \le |A - Y| + |B - X|$$

Extending this pairwise property to $n$ elements, we can guarantee that matching the $i$-th smallest student position with the $i$-th smallest seat position is strictly optimal.

---

### Step-by-Step Approach

1. **Sort Both Arrays**: Sort `seats` and `students` in ascending order.
2. **Pairwise Accumulation**: Iterate through indices $0$ to $n-1$, compute the absolute difference $|seats[i] - students[i]|$, and accumulate these differences.
3. **Return Total**: The accumulated sum is the global minimum number of moves.

---

### Complexity Analysis

- **Time Complexity**: 
  - Standard comparison sorting takes $\mathcal{O}(n \log n)$, where $n$ is the number of seats/students.
  - The linear scan with `zip` takes $\mathcal{O}(n)$.
  - **Total Time Complexity**: $\mathcal{O}(n \log n)$.
  
- **Space Complexity**:
  - Python's Timsort uses $\mathcal{O}(n)$ auxiliary space in the worst case (or $\mathcal{O}(1)$ additional space if sorting in-place in languages like C++ with `std::sort`).
  - **Total Space Complexity**: $\mathcal{O}(1)$ auxiliary space beyond the sorting buffer.

---

### Alternative $\mathcal{O}(n + M)$ Approach (Counting / Net Flow)

Since the values in the problem constraints satisfy $1 \le seats[i], students[i] \le 100$, we can also solve this in linear time $\mathcal{O}(n + M)$ where $M = \max(seats, students)$:
1. Maintain a frequency difference array `diff` of size $M + 1$, where we increment for each student and decrement for each seat at position $x$.
2. Compute prefix sums across positions. The prefix sum at position $x$ represents the net number of students that must traverse the segment between $x$ and $x + 1$.
3. Total moves is simply $\sum_{x=1}^{M} |\text{prefix\_sum}[x]|$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Using 2D Dynamic Programming / Bipartite Matching**: Candidates sometimes overcomplicate this into the Hungarian algorithm ($\mathcal{O}(n^3)$) or DP ($\mathcal{O}(n^2)$), missing the greedy non-crossing property.
2. **Greedy Nearest Matching (Local Greedy)**: Iterating through students one-by-one and greedily assigning the closest available seat fails. For example, if seats are at $[1, 10]$ and students are at $[2, 3]$, greedily matching student $2$ to seat $1$ leaves student $3$ to walk to $10$ (total: $|2-1| + |3-10| = 8$). However, student $2 \to 1$ and student $3 \to 10$ is 8, but if seats were $[2, 10]$ and students were $[1, 3]$, a greedy pick of $3 \to 2$ leaves $1 \to 10$ (cost $1+9=10$), whereas $1 \to 2$ and $3 \to 10$ has cost $1+7=8$. Local greedy without global sorting leads to sub-optimal decisions.

---

### Real Interview Follow-Up Questions

#### 1. What if $n$ is very large (e.g., $n = 10^7$) and the range of positions is small ($M \le 100$)?
* **Answer**: Use the **Counting / Net Flow** approach mentioned above. Count frequencies of students and seats in $\mathcal{O}(n)$, then compute cumulative flow across the $M$ positions in $\mathcal{O}(M)$ time and $\mathcal{O}(M)$ auxiliary space. Total time becomes $\mathcal{O}(n + M)$ instead of $\mathcal{O}(n \log n)$.

#### 2. What if students and seats arrive as continuous, unbounded data streams?
* **Answer**:
  - If we need the real-time cost after each insertion, we can maintain two balanced Binary Search Trees (or order-statistic trees / Fenwick trees over compressed coordinates) to maintain rank order and efficiently query the matching cost.
  - If seats are fixed and students arrive dynamically online, this becomes the **Online Bipartite Matching on a Metric Space** problem, where competitive analysis algorithms (like Work Function Algorithm or Greedy with random perturbations) apply.

#### 3. What if moving left costs $C_{left}$ and moving right costs $C_{right}$?
* **Answer**: The non-crossing property still holds because the asymmetric cost function $c(x, y) = C_{right}(y - x)$ for $y \ge x$ and $C_{left}(x - y)$ for $x > y$ remains convex and Monge. Sorting both arrays and pairing matching indices remains optimal.
