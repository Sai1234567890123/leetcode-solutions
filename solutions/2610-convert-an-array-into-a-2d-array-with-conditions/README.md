# 2610. Convert an Array Into a 2D Array With Conditions

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/)  
**Topics:** Array, Hash Table

---

## 📝 Problem Statement

You are given an integer array `nums`. You need to create a 2D array from `nums` satisfying the following conditions:

	- The 2D array should contain **only** the elements of the array `nums`.

	- Each row in the 2D array contains **distinct** integers.

	- The number of rows in the 2D array should be **minimal**.

Return *the resulting array*. If there are multiple answers, return any of them.

**Note** that the 2D array can have a different number of elements on each row.

 
Example 1:

```

**Input:** nums = [1,3,4,1,2,3,1]
**Output:** [[1,3,4,2],[1,3],[1]]
**Explanation:** We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
```

Example 2:

```

**Input:** nums = [1,2,3,4]
**Output:** [[4,3,2,1]]
**Explanation:** All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        """
        Creates a 2D array from nums with minimal rows such that each row contains distinct integers.
        """
        # Frequency map or array to track how many times each number has appeared.
        # Since nums[i] <= len(nums), a fixed-size array or hash map can be used.
        freq: dict[int, int] = {}
        res: list[list[int]] = []

        for num in nums:
            # The current count indicates the 0-indexed row where this instance belongs.
            count = freq.get(num, 0)
            
            # If the row doesn't exist yet, create a new row.
            if count == len(res):
                res.append([])
            
            # Place the number into its assigned row and increment frequency.
            res[count].append(num)
            freq[num] = count + 1

        return res
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

1. **Condition for Minimality**:
   By the Pigeonhole Principle, if an integer appears $k$ times in `nums`, we must distribute its $k$ occurrences across at least $k$ distinct rows, because no row can contain duplicate values.
   Therefore, the minimal number of rows required is strictly equal to the maximum frequency of any element:
   $$\text{Number of rows} = \max_{x \in \text{nums}} (\text{count}(x))$$

2. **Placement Strategy**:
   Instead of precomputing frequencies and then building the rows, we can build the 2D array dynamically in a single pass:
   - Maintain the count of occurrences seen so far for each number.
   - For a number `num`, if it has already appeared $k$ times (0-indexed: $0, 1, \dots, k-1$), its current instance must go to row index $k$.
   - If row $k$ does not exist yet, we append a new empty row to our result.
   - Append `num` to row $k$, and increment the count for `num`.

This guarantees that each row contains strictly unique elements and the number of rows is exactly the maximum frequency seen.

---

### Step-by-Step Approach

1. Initialize `freq` as an empty hash map (or array) and `res` as an empty list of lists.
2. Iterate through each element `num` in `nums`:
   - Retrieve its current frequency `count = freq.get(num, 0)`.
   - If `count == len(res)`, this is the first element that requires row index `count`. Append `[]` to `res`.
   - Append `num` to `res[count]`.
   - Update `freq[num] = count + 1`.
3. Return `res`.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$
  We iterate through the input list of length $N$ exactly once. Hash map lookups and row appends take $\mathcal{O}(1)$ amortized time. Total time is $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$
  - Auxiliary Space: $\mathcal{O}(U)$ where $U$ is the number of unique elements ($U \le N$) for the frequency map.
  - Output Space: $\mathcal{O}(N)$ to store the resulting 2D array.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Sorting First**: Candidates often sort the array ($\mathcal{O}(N \log N)$), which is unnecessary and less optimal.
2. **Two-Pass Inefficiencies**: Computing frequencies first, finding the maximum frequency, preallocating rows, and filling them. While $\mathcal{O}(N)$, a single-pass greedy row-assignment is cleaner and handles streaming inputs naturally.
3. **Repeated Scans / Set Lookups**: Repeatedly trying to find an existing row where `num` does not exist using row-wise `in` lookups leads to $\mathcal{O}(N^2)$ time. Tracking row assignment by frequency avoids this entirely.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if `nums` is a continuous data stream?
- **Answer**: The one-pass approach presented above directly supports streaming. When a new integer arrives, look up its current count in the frequency table, expand the result matrix if needed, append the integer to `res[count]`, and increment the count. All operations per streaming item take $\mathcal{O}(1)$ amortized time.

#### 2. What if memory is severely constrained and modifying the input array is allowed?
- **Answer**: If `nums[i] <= len(nums)` (as per the problem constraints), we can encode counts in-place using index-based manipulation (e.g., adding $M = N + 1$ or bit manipulation) to store frequencies in $\mathcal{O}(1)$ auxiliary space before constructing the result rows.

#### 3. How to balance row lengths (make row sizes as uniform as possible)?
- **Answer**: If the problem asks for minimal rows *and* approximately equal-length rows:
  - First compute total rows $R = \max(\text{count})$.
  - For elements with count $< R$, we can distribute them across rows using a round-robin pointer or a min-heap tracking the shortest row currently not containing that element.
