# 2125. Number of Laser Beams in a Bank

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/number-of-laser-beams-in-a-bank/](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)  
**Topics:** Array, Math, String, Matrix

---

## 📝 Problem Statement

Anti-theft security devices are activated inside a bank. You are given a **0-indexed** binary string array `bank` representing the floor plan of the bank, which is an `m x n` 2D matrix. `bank[i]` represents the `ith` row, consisting of `'0'`s and `'1'`s. `'0'` means the cell is empty, while`'1'` means the cell has a security device.

There is **one** laser beam between any **two** security devices **if both** conditions are met:

	- The two devices are located on two **different rows**: `r1` and `r2`, where `r1 2`.

	- For **each** row `i` where `r1 2`, there are **no security devices** in the `ith` row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return *the total number of laser beams in the bank*.

 
Example 1:

```

**Input:** bank = ["011001","000000","010100","001000"]
**Output:** 8
**Explanation:** Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.

```

Example 2:

```

**Input:** bank = ["000","111","000"]
**Output:** 0
**Explanation:** There does not exist two devices located on two different rows.

```

 
**Constraints:**

	- `m == bank.length`

	- `n == bank[i].length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        total_beams = 0
        prev_row_count = 0

        for row in bank:
            # Count the number of security devices ('1') in the current row
            curr_row_count = row.count('1')

            # If there are no devices in this row, beams pass through uninterrupted
            if curr_row_count == 0:
                continue

            # Every device in the previous valid row connects to every device in this row
            total_beams += prev_row_count * curr_row_count
            
            # Update the previous valid row device count
            prev_row_count = curr_row_count

        return total_beams
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to find the total number of laser beams between security devices (`'1'`) on different rows. A laser beam connects two devices if and only if there are no intermediate rows between them that also contain security devices.

Key observations:
1. **Empty Rows Don't Block or Emit Beams:** Any row with zero devices (`'1'`s) has no effect on beam formation. Lasers simply pass through them. We can safely skip these rows.
2. **Multiplication Principle:** If row $A$ has $c_A > 0$ devices and the next non-empty row $B$ has $c_B > 0$ devices, every device in row $A$ will form a beam with every device in row $B$. Therefore, the total number of beams between these two rows is $c_A \times c_B$.
3. **Chaining Rows:** Once row $B$ is processed, it blocks any beams from row $A$ to rows below $B$. Thus, row $B$ becomes the new "previous" row for subsequent rows.

This allows us to solve the problem in a single pass while tracking only the device count of the most recent non-empty row (`prev_row_count`).

---

### Step-by-Step Approach

1. Initialize `total_beams = 0` and `prev_row_count = 0`.
2. Iterate through each row in `bank`:
   - Count the number of `'1'`s in the current row (`curr_row_count`).
   - If `curr_row_count == 0`, continue to the next row (no devices to emit or block beams).
   - If `curr_row_count > 0`:
     - Add `prev_row_count * curr_row_count` to `total_beams`.
     - Update `prev_row_count = curr_row_count`.
3. Return `total_beams`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \times n)$, where $m$ is the number of rows and $n$ is the length of each row (`bank[0].length`). We iterate through each string of length $n$ once to count `'1'`s.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. We only use two integer variables (`total_beams` and `prev_row_count`) without allocating any intermediate arrays or extra data structures.

---

### Common Pitfalls / Mistakes

1. **Storing All Counts in a List:** While an $\mathcal{O}(m)$ list storing non-zero counts still passes, it incurs unnecessary memory allocation. Doing it online in $\mathcal{O}(1)$ space is the expected standard for senior/principal level interviews.
2. **Pairwise Row Comparison ($\mathcal{O}(m^2)$):** Checking every pair of rows $(i, j)$ and verifying that all rows between them are empty leads to an inefficient $\mathcal{O}(m^2 \cdot n)$ solution.
3. **Edge Cases:**
   - Only 1 row in total (`m == 1`): Loop runs once, `prev_row_count` starts at 0, returns 0 correctly.
   - All rows have zero devices: `curr_row_count` is always 0, returns 0 correctly.
   - Only one row has devices: Product is never formed with a valid `prev_row_count`, returns 0 correctly.

---

### Real Interview Follow-Up Questions

#### 1. What if the input is a continuous data stream where rows are received one by one?
**Answer:** The current solution naturally operates as a streaming algorithm. We do not need random access to rows. As each row arrives over a stream or network socket, we compute its count, update `total_beams`, update `prev_row_count`, and discard the row string immediately. Memory usage remains $\mathcal{O}(1)$ regardless of stream length.

#### 2. What if $n$ (row length) is extremely large (e.g., $n = 10^9$) and rows are given as sparse intervals or indices of devices?
**Answer:** Instead of a string representation, each row would be represented as a list of column indices `List[int]` or by its length and a count. Since we only need the count of devices per row, we can just take `len(row_devices)` in $\mathcal{O}(1)$ time per row. Time complexity drops from $\mathcal{O}(m \times n)$ to $\mathcal{O}(m + k)$ where $k$ is the total number of devices.

#### 3. How would you parallelize this for massive datasets (e.g., MapReduce / Spark)?
**Answer:** 
- **Map phase:** Each worker receives a chunk of rows and filters out rows with zero devices, outputting `(row_index, count)`.
- **Reduce phase:** Sort/order the non-zero counts by `row_index` and perform a parallel prefix or straightforward linear scan across the reduced non-zero counts to accumulate adjacent products.
