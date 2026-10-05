# 1389. Create Target Array in the Given Order

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/create-target-array-in-the-given-order/](https://leetcode.com/problems/create-target-array-in-the-given-order/)  
**Topics:** Array, Simulation

---

## 📝 Problem Statement

Given two arrays of integers `nums` and `index`. Your task is to create *target* array under the following rules:

	- Initially *target* array is empty.

	- From left to right read nums[i] and index[i], insert at index `index[i]` the value `nums[i]` in *target* array.

	- Repeat the previous step until there are no elements to read in `nums` and `index.`

Return the *target* array.

It is guaranteed that the insertion operations will be valid.

 
Example 1:

```

**Input:** nums = [0,1,2,3,4], index = [0,1,2,2,1]
**Output:** [0,4,1,3,2]
**Explanation:**
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

```

Example 2:

```

**Input:** nums = [1,2,3,4,0], index = [0,1,2,3,0]
**Output:** [0,1,2,3,4]
**Explanation:**
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

```

Example 3:

```

**Input:** nums = [1], index = [0]
**Output:** [1]

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        """
        Creates the target array by inserting each element from `nums`
        at the specified index in `index`.
        """
        target = []
        
        # Iterate through pairs of (val, idx) and insert sequentially
        for val, idx in zip(nums, index):
            target.insert(idx, val)
            
        return target
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem directly specifies a simulation process:
1. Start with an empty list `target`.
2. For each element `nums[i]` and corresponding position `index[i]`, insert `nums[i]` at `target[index[i]]`.
3. Elements at or to the right of `index[i]` are shifted one position to the right.

Given the constraint $1 \le N \le 100$, Python's built-in dynamic array (list) `insert(index, value)` operation takes $O(k)$ time where $k$ is the number of elements shifted. Over $N$ insertions, this results in an $O(N^2)$ runtime and $O(1)$ auxiliary space (excluding the output array), which executes in a few microseconds.

---

### Step-by-Step Approach

1. Initialize an empty list `target = []`.
2. Pair each element of `nums` with `index` using `zip(nums, index)`.
3. For each pair `(val, idx)`, invoke `target.insert(idx, val)`.
4. Return `target`.

---

### Complexity Analysis

- **Time Complexity:** $O(N^2)$
  - There are $N$ insertion steps.
  - At step $i$, inserting into a list of size $i$ takes $O(i)$ time in the worst case (e.g., prepending at index 0).
  - Total operations: $\sum_{i=0}^{N-1} O(i) = O\left(\frac{N(N-1)}{2}\right) = O(N^2)$.
- **Space Complexity:** $O(1)$ auxiliary space ($O(N)$ space for the returned output array).

---

### Common Pitfalls / Mistakes

1. **Confusing Replacement with Insertion:** Attempting to pre-allocate an array of size $N$ and assigning `target[index[i]] = nums[i]`. This overwrites elements rather than shifting them.
2. **Handling Index Out of Range:** The problem guarantees `0 <= index[i] <= i`. If this guarantee were not present, boundary validation would be required.

---

### Real Interview Follow-Up Questions & Scalability

#### 1. What if $N = 10^5$? How can we optimize this beyond $O(N^2)$?
At $N = 10^5$, an $O(N^2)$ algorithm would perform $10^{10}$ operations and Time Out (TLE).
We can solve this in **$O(N \log N)$ time** by processing the insertions in **reverse order** using a **Binary Indexed Tree (Fenwick Tree)** or **Segment Tree**:
- **Backward Insight:** The last inserted element will never be shifted; its final position in the target array is strictly its given index. The second-to-last element will be placed at its specified index among the *remaining unfilled positions*.
- **Mechanism:**
  1. Initialize a Fenwick Tree where all $N$ positions are marked as available (value = 1).
  2. Iterate $i$ from $N - 1$ down to $0$:
     - We need to find the `(index[i] + 1)`-th empty slot.
     - Using binary lifting on the Fenwick Tree, we can find this position in $O(\log N)$ time.
     - Place `nums[i]` at this slot in the output array and update the Fenwick Tree (mark slot as 0).
- Total Time: $O(N \log N)$, Space: $O(N)$.

#### 2. How to handle concurrent insertions in a distributed environment?
If multiple workers are generating `(value, index)` events:
- A shared balanced binary search tree (like a Treap or Order Statistic Tree) with fine-grained locking or lock-free skip lists can allow concurrent positional inserts.
- Alternatively, assign monotonic sequence IDs via an append-only log (e.g., Apache Kafka) to preserve deterministic ordering before constructing the target.
