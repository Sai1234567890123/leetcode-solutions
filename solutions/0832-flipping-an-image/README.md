# 0832. Flipping an Image

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/flipping-an-image/](https://leetcode.com/problems/flipping-an-image/)  
**Topics:** Array, Two Pointers, Bit Manipulation, Matrix, Simulation

---

## 📝 Problem Statement

Given an `n x n` binary matrix `image`, flip the image **horizontally**, then invert it, and return *the resulting image*.

To flip an image horizontally means that each row of the image is reversed.

	- For example, flipping `[1,1,0]` horizontally results in `[0,1,1]`.

To invert an image means that each `0` is replaced by `1`, and each `1` is replaced by `0`.

	- For example, inverting `[0,1,1]` results in `[1,0,0]`.

 
Example 1:

```

**Input:** image = [[1,1,0],[1,0,1],[0,0,0]]
**Output:** [[1,0,0],[0,1,0],[1,1,1]]
**Explanation:** First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

```

Example 2:

```

**Input:** image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
**Output:** [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
**Explanation:** First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

```

 
**Constraints:**

	- `n == image.length`

	- `n == image[i].length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """
        Flips the binary matrix horizontally and inverts it in-place.
        """
        n = len(image)
        mid = (n + 1) // 2
        
        for row in image:
            for j in range(mid):
                k = n - 1 - j
                # Key insight:
                # If row[j] == row[k], flipping swaps identical values,
                # then inverting flips both values (0 -> 1 or 1 -> 0).
                # If row[j] != row[k], flipping swaps 0 and 1 to 1 and 0,
                # and inverting swaps them back to 0 and 1, leaving them unchanged!
                if row[j] == row[k]:
                    row[j] = row[k] = row[j] ^ 1
                    
        return image
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A naive approach would be to first reverse each row and then iterate through the matrix to invert every bit ($0 \to 1, 1 \to 0$). That requires two distinct passes or creating a new matrix via list comprehensions like `[[1 - x for x in reversed(row)] for row in image]`.

However, we can do this **in-place in a single pass** by analyzing what happens to a symmetric pair of elements at indices `j` and `k = n - 1 - j`:
1. **Case 1: `row[j] == row[k]`**
   - Flipping horizontally swaps two equal values (e.g., `(1, 1) -> (1, 1)` or `(0, 0) -> (0, 0)`).
   - Inverting flips both values (e.g., `(1, 1) -> (0, 0)` or `(0, 0) -> (1, 1)`).
   - Thus, both elements simply invert: `row[j] = row[k] = row[j] ^ 1`.
   - When `j == k` (the center element in an odd-length row), this rule naturally applies and correctly inverts the center element.
2. **Case 2: `row[j] != row[k]`**
   - One element is `0` and the other is `1` (e.g., `(1, 0)`).
   - Flipping swaps them to `(0, 1)`.
   - Inverting then transforms `(0, 1)` back to `(1, 0)`.
   - Notice that the elements **remain identical to their initial values**! We do not need to do any operation at all.

---

### Step-by-Step Approach

1. Determine the length `n` of the matrix.
2. For each row in `image`, iterate pointer `j` from `0` to `(n + 1) // 2` (up to and including the middle element).
3. Let `k = n - 1 - j` be the symmetric counter-part index.
4. If `row[j] == row[k]`, invert both using bitwise XOR: `row[j] = row[k] = row[j] ^ 1`.
5. Return the modified `image` matrix.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n^2)$
  There are $n$ rows, and for each row, we examine $\lceil n / 2 \rceil$ pairs. Total operations are $n \times \lceil n / 2 \rceil \approx \frac{n^2}{2}$, which is strictly optimal since every element must be processed or inspected at least once.
- **Space Complexity:** $\mathcal{O}(1)$ Auxiliary Space
  The transformation is executed completely in-place without allocating auxiliary matrices or additional lists.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Double-Inverting the Middle Element:**
   When doing `row[j] ^= 1` and `row[k] ^= 1`, if $j == k$, applying XOR twice cancels out the inversion (`x ^ 1 ^ 1 == x`). Assigning `row[j] = row[k] = row[j] ^ 1` safely handles this case.
2. **Unnecessary Memory Allocation:**
   Many candidates construct an entirely new 2D list. While acceptable for easy problems, demonstrating an in-place $\mathcal{O}(1)$ auxiliary space approach shows strong mastery of memory efficiency.
3. **Off-by-One on Center Column:**
   Using `range(n // 2)` instead of `range((n + 1) // 2)` misses the middle element when $n$ is odd.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if modifying the input in-place is not allowed?
**Answer:** We can use Python's list comprehension to generate the result concisely:
```python
return [[x ^ 1 for x in reversed(row)] for row in image]
```
This is $\mathcal{O}(n^2)$ time and $\mathcal{O}(n^2)$ space for the new matrix.

#### 2. How would you optimize this if each row is represented as a 64-bit integer (bitboard/bitmask) instead of an array of integers?
**Answer:**
If rows are represented as integers (bit vectors of length $n$):
- Reversing the bits can be done in $\mathcal{O}(\log n)$ bitwise operations using parallel bit-reversal masks (or hardware instructions like `rbit` on ARM).
- Inverting is simply a bitwise NOT masked to $n$ bits: `(~reversed_row) & ((1 << n) - 1)`.
- This reduces the row transformation from $\mathcal{O}(n)$ steps to $\mathcal{O}(1)$ machine word operations.

#### 3. How would you handle an extremely large image that doesn't fit into memory (e.g., $100,000 \times 100,000$ stored on disk)?
**Answer:**
Since each row can be transformed independently:
- Stream each row from disk sequentially or in chunks.
- Process the row in memory (in-place) and stream the transformed row directly to the output file or network sink.
- This allows processing with $\mathcal{O}(n)$ memory buffer regardless of the total number of rows.
