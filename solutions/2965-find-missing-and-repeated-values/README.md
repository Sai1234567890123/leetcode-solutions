# 2965. Find Missing and Repeated Values

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-missing-and-repeated-values/](https://leetcode.com/problems/find-missing-and-repeated-values/)  
**Topics:** Array, Hash Table, Math, Matrix

---

## 📝 Problem Statement

You are given a **0-indexed** 2D integer matrix `grid` of size `n * n` with values in the range `[1, n2]`. Each integer appears **exactly once** except `a` which appears **twice** and `b` which is **missing**. The task is to find the repeating and missing numbers `a` and `b`.

Return *a **0-indexed **integer array *`ans`* of size *`2`* where *`ans[0]`* equals to *`a`* and *`ans[1]`* equals to *`b`*.*

 
Example 1:

```

**Input:** grid = [[1,3],[2,2]]
**Output:** [2,4]
**Explanation:** Number 2 is repeated and number 4 is missing so the answer is [2,4].

```

Example 2:

```

**Input:** grid = [[9,1,7],[8,9,2],[3,4,6]]
**Output:** [9,5]
**Explanation:** Number 9 is repeated and number 5 is missing so the answer is [9,5].

```

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        """
        Finds the repeating number 'a' and missing number 'b' from an n x n grid.
        Uses the mathematical sum and sum of squares approach to achieve O(1) auxiliary space.
        """
        n = len(grid)
        total_elements = n * n

        # Expected sum and sum of squares for 1 to total_elements (N)
        expected_sum = total_elements * (total_elements + 1) // 2
        expected_sum_sq = total_elements * (total_elements + 1) * (2 * total_elements + 1) // 6

        actual_sum = 0
        actual_sum_sq = 0

        for row in grid:
            for val in row:
                actual_sum += val
                actual_sum_sq += val * val

        # diff1 = a - b
        diff1 = actual_sum - expected_sum
        # diff2 = a^2 - b^2 = (a - b) * (a + b)
        diff2 = actual_sum_sq - expected_sum_sq

        # sum_ab = a + b = diff2 / diff1
        sum_ab = diff2 // diff1

        # Solving the linear system:
        # a = ((a - b) + (a + b)) / 2
        # b = ((a + b) - (a - b)) / 2
        repeated = (diff1 + sum_ab) // 2
        missing = (sum_ab - diff1) // 2

        return [repeated, missing]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem presents an $n \times n$ matrix containing integers from $1$ to $n^2$ where one integer $a$ appears twice (repeated) and another integer $b$ is omitted (missing). 

While an auxiliary frequency array or hash set can solve this in $O(n^2)$ time and $O(n^2)$ space, we can do strictly better on space complexity:
1. **Direct Mathematical Derivation ($O(1)$ auxiliary space)**:
   Let $N = n^2$.
   - The expected sum of the first $N$ natural numbers is $S = \frac{N(N + 1)}{2}$.
   - The expected sum of squares of the first $N$ natural numbers is $P = \frac{N(N + 1)(2N + 1)}{6}$.
   - Let the actual sum of elements in the grid be $A = \sum x$, and the sum of squares be $A_2 = \sum x^2$.

   From these:
   $$A - S = a - b$$
   $$A_2 - P = a^2 - b^2 = (a - b)(a + b)$$

   Dividing the second equation by the first:
   $$a + b = \frac{A_2 - P}{A - S}$$

   Now, we have a system of two simple linear equations:
   1. $a - b = \Delta_1$
   2. $a + b = \Delta_2 / \Delta_1$

   Adding the two yields $2a$, from which we solve for $a$. Subtracting gives $2b$, from which we solve for $b$.

### Step-by-Step Approach

1. Compute $N = n^2$.
2. Compute the theoretical sum `expected_sum` $= N(N + 1) / 2$ and sum of squares `expected_sum_sq` $= N(N + 1)(2N + 1) / 6$.
3. Iterate through each cell in `grid` to accumulate `actual_sum` and `actual_sum_sq`.
4. Calculate $\Delta_1 = A - S$ and $\Delta_2 = A_2 - P$.
5. Compute $(a + b) = \Delta_2 // \Delta_1$.
6. Calculate $a = (\Delta_1 + (a + b)) // 2$ and $b = ((a + b) - \Delta_1) // 2$.
7. Return `[a, b]`.

### Complexity Analysis

- **Time Complexity**: $O(n^2)$
  We iterate through the entire $n \times n$ grid exactly once to accumulate the sum and sum of squares. Computing the final formulas is $O(1)$.
- **Space Complexity**: $O(1)$ auxiliary space
  We only use a few scalar variables (`actual_sum`, `actual_sum_sq`, `expected_sum`, etc.) without allocating any extra data structures or modifying the input array.

### Common Pitfalls / Mistakes Candidates Make

1. **Integer Overflow (in statically typed languages like C++/Java)**:
   For $n = 50$, $N = 2500$. The sum of squares is approximately $\frac{2500^3}{3} \approx 5.2 \times 10^9$, which exceeds the standard 32-bit signed integer maximum ($2^{31} - 1 \approx 2.14 \times 10^9$). In Python, integers have arbitrary precision, but in C++/Java, `long long` / `long` must be used to avoid overflow.
2. **Order of Results**:
   The problem specifies returning `[repeated, missing]` (i.e., `[a, b]`). A common bug is returning `[missing, repeated]` due to misreading the prompt.
3. **Division by Zero**:
   Since $a \neq b$, $a - b \neq 0$, so $\Delta_1$ is guaranteed to be non-zero.

### Real Interview Follow-Up Questions & Answers

- **Q1: What if integer overflow is a strict concern and large integer types are unavailable?**
  - **Answer**: We can use the **XOR Bit Manipulation** technique:
    1. XOR all numbers in the grid with all numbers from $1$ to $N$. The result is $X = a \oplus b$.
    2. Find the lowest set bit in $X$: `diff_bit = X & (-X)`.
    3. Partition both the grid elements and the numbers from $1$ to $N$ into two groups based on whether this bit is set.
    4. XORing within each group yields $a$ and $b$ individually.
    5. A final quick pass over the grid determines which of the two values is $a$ (appears twice) and which is $b$.
    - *Complexity*: $O(n^2)$ time, $O(1)$ space, zero overflow risk.

- **Q2: What if the grid is massive and streamed across multiple machines (MapReduce / Distributed Setting)?**
  - **Answer**: The mathematical approach is inherently associative and commutative. Each worker can compute partial `count`, `sum`, and `sum_sq` for their assigned slice of data. A reducer simply adds up these scalar metrics, calculates the theoretical values based on $N$, and solves the system of equations. This requires minimal network transfer: $O(1)$ data per worker.

- **Q3: What if the grid contains multiple missing and multiple repeating values?**
  - **Answer**: The sum/square approach can be generalized using higher-order power sums (Newton's identities) for small fixed $k$, but quickly becomes numerically unstable. If modifying the input is allowed, we can use **in-place cyclic sort / index-as-hash** (negating values at `grid[val - 1]`) in $O(n^2)$ time and $O(1)$ space. If read-only, a frequency array or bitmap ($O(N)$ space) is the standard industry approach.
