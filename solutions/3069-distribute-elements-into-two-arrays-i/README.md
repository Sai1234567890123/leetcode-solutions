# 3069. Distribute Elements Into Two Arrays I

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/distribute-elements-into-two-arrays-i/](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/)  
**Topics:** Array, Two Pointers, Simulation

---

## 📝 Problem Statement

You are given a **1-indexed** array of **distinct** integers `nums` of length `n`.

You need to distribute all the elements of `nums` between two arrays `arr1` and `arr2` using `n` operations. In the first operation, append `nums[1]` to `arr1`. In the second operation, append `nums[2]` to `arr2`. Afterwards, in the `ith` operation:

	- If the last element of `arr1` is** greater** than the last element of `arr2`, append `nums[i]` to `arr1`. Otherwise, append `nums[i]` to `arr2`.

The array `result` is formed by concatenating the arrays `arr1` and `arr2`. Concatenating two arrays appends the second to the end of the first; for example, concatenating `[1,2,3]` with `[4,5,6]` gives `[1,2,3,4,5,6]`.

Return *the array* `result`.

 
Example 1:

```

**Input:** nums = [2,1,3]
**Output:** [2,3,1]
**Explanation:** After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3rd operation, as the last element of arr1 is greater than the last element of arr2 (2 > 1), append nums[3] to arr1.
After 3 operations, arr1 = [2,3] and arr2 = [1].
Hence, the array result formed by concatenation is [2,3,1].

```

Example 2:

```

**Input:** nums = [5,4,3,8]
**Output:** [5,3,4,8]
**Explanation:** After the first 2 operations, arr1 = [5] and arr2 = [4].
In the 3rd operation, as the last element of arr1 is greater than the last element of arr2 (5 > 4), append nums[3] to arr1, hence arr1 becomes [5,3].
In the 4th operation, as the last element of arr2 is greater than the last element of arr1 (4 > 3), append nums[4] to arr2, hence arr2 becomes [4,8].
After 4 operations, arr1 = [5,3] and arr2 = [4,8].
Hence, the array result formed by concatenation is [5,3,4,8].

```

 
**Constraints:**

	- `3

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        """
        Distributes elements of nums into two arrays arr1 and arr2 based on
        the comparison between their last elements, and returns arr1 + arr2.
        """
        # Step 1: Initialize arr1 and arr2 with the first two elements.
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        # Step 2: Iterate through the remaining elements and distribute accordingly.
        for num in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
                
        # Step 3: Concatenate and return the combined list.
        return arr1 + arr2
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem presents a direct deterministic simulation:
1. Initialize two lists, `arr1` and `arr2`, with the first two elements (`nums[0]` into `arr1`, `nums[1]` into `arr2`).
2. For each subsequent element `nums[i]` (from index 2 onwards), inspect the last element of `arr1` (i.e., `arr1[-1]`) and the last element of `arr2` (i.e., `arr2[-1]`).
3. Append `nums[i]` to `arr1` if `arr1[-1] > arr2[-1]`; otherwise, append it to `arr2`.
4. Finally, return the concatenated result `arr1 + arr2`.

Since accessing the last element and appending to a dynamic array in Python takes $O(1)$ amortized time, a direct iterative approach achieves optimal linear time.

---

### Step-by-Step Approach

1. **Initialization**:
   - `arr1 = [nums[0]]`
   - `arr2 = [nums[1]]`
2. **Simulation Loop**:
   - Loop through `num` in `nums[2:]`.
   - Compare `arr1[-1]` and `arr2[-1]`.
   - If `arr1[-1] > arr2[-1]`, execute `arr1.append(num)`.
   - Otherwise, execute `arr2.append(num)`.
3. **Combination**:
   - Concatenate `arr1` and `arr2` using list addition (`+`) or `arr1.extend(arr2)` and return.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(n)$
  - Slicing `nums[2:]` and iterating takes $\mathcal{O}(n)$ time.
  - In each iteration, indexing the last element (`arr1[-1]`, `arr2[-1]`) and appending takes $\mathcal{O}(1)$ amortized time.
  - Final concatenation takes $\mathcal{O}(n)$ time.
  - Overall time complexity is strictly $\mathcal{O}(n)$.

- **Space Complexity**: $\mathcal{O}(n)$
  - `arr1` and `arr2` store a total of $n$ elements combined, which is required to return the output.
  - Beyond the output storage, auxiliary space is $\mathcal{O}(1)$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **1-based vs 0-based indexing confusion**: The problem description references 1-based indexing (`nums[1]`, `nums[2]`), but in Python arrays are 0-indexed (`nums[0]`, `nums[1]`). Off-by-one errors are common if candidates blindly copy problem indices.
2. **Re-evaluating full arrays instead of top elements**: Accompanying problem "Distribute Elements Into Two Arrays II" (LeetCode 3072) asks to compare counts of strictly greater elements (which requires Fenwick Trees or Segment Trees). Candidates sometimes overcomplicate this variation (Part I) which only requires checking the *last* element.

---

### Real Interview Follow-Up Questions

#### 1. What if the input is streaming (infinite data stream) and cannot fit in memory?
- **Answer**: If we are required to yield the elements in order of `arr1` followed by `arr2`, we cannot emit the elements of `arr2` until the stream terminates because `arr1` must come first. If memory is constrained, we would write `arr2` elements to external storage (e.g., disk or disk-backed buffer) while outputting `arr1` elements immediately, or buffer both to separate disk segments and merge them at the end.

#### 2. Can we do this in-place with $\mathcal{O}(1)$ auxiliary space?
- **Answer**: In-place rearrangement is possible but non-trivial because it is equivalent to a stable partitioning based on a dynamic condition. However, because each decision depends only on the previous decision's outcome, we can simulate the decisions and then use in-place cyclic shifts or block swaps to move all `arr2` elements to the back of `nums`, achieving $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ auxiliary space.

#### 3. What if the condition is based on the count of elements greater than `nums[i]` in `arr1` vs `arr2` (LeetCode 3072)?
- **Answer**: That requires maintaining order statistics dynamically. We would use coordinate compression along with two Binary Indexed Trees (Fenwick Trees) or Order Statistic Trees (such as `SortedList` in Python) to query the number of elements strictly greater than `nums[i]` in $\mathcal{O}(\log n)$ time per element, leading to an overall $\mathcal{O}(n \log n)$ solution.
