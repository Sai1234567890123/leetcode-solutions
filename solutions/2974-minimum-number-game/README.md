# 2974. Minimum Number Game

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/minimum-number-game/](https://leetcode.com/problems/minimum-number-game/)  
**Topics:** Array, Sorting, Heap (Priority Queue), Simulation

---

## 📝 Problem Statement

You are given a **0-indexed** integer array `nums` of **even** length and there is also an empty array `arr`. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

	- Every round, first Alice will remove the **minimum** element from `nums`, and then Bob does the same.

	- Now, first Bob will append the removed element in the array `arr`, and then Alice does the same.

	- The game continues until `nums` becomes empty.

Return *the resulting array *`arr`.

 
Example 1:

```

**Input:** nums = [5,4,2,3]
**Output:** [3,2,5,4]
**Explanation:** In round one, first Alice removes 2 and then Bob removes 3. Then in arr firstly Bob appends 3 and then Alice appends 2. So arr = [3,2].
At the begining of round two, nums = [5,4]. Now, first Alice removes 4 and then Bob removes 5. Then both append in arr which becomes [3,2,5,4].

```

Example 2:

```

**Input:** nums = [2,5]
**Output:** [5,2]
**Explanation:** In round one, first Alice removes 2 and then Bob removes 5. Then in arr firstly Bob appends and then Alice appends. So arr = [5,2].

```

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        # Sort the array in non-decreasing order.
        # This allows us to access the smallest elements sequentially.
        nums.sort()
        
        # In each round, Alice picks nums[i] and Bob picks nums[i + 1].
        # Bob appends first, followed by Alice, effectively swapping their positions.
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            
        return nums
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The rules of the game dictate:
1. Alice removes the absolute minimum element from `nums`.
2. Bob removes the next smallest element from `nums`.
3. Bob places his element into `arr` first.
4. Alice places her element into `arr` second.

If the entire array `nums` is sorted in ascending order:
- The first pair of minimum elements will be `nums[0]` (Alice's pick) and `nums[1]` (Bob's pick).
- Bob appends first, then Alice, so the output starts with `[nums[1], nums[0]]`.
- The second pair will be `nums[2]` and `nums[3]`, appended as `[nums[3], nums[2]]`.

This pattern generalizes to every adjacent pair: for every index `i = 0, 2, 4, ...`, we swap `nums[i]` and `nums[i + 1]`.

### Step-by-Step Approach

1. Sort `nums` in ascending order in place using Python's built-in Timsort (`nums.sort()`).
2. Iterate through the array with a step of 2 (`for i in range(0, len(nums), 2)`).
3. Swap elements at index `i` and `i + 1`.
4. Return the modified `nums` array.

### Complexity Analysis

- **Time Complexity:** 
  - Sorting takes $\mathcal{O}(n \log n)$ where $n$ is the length of `nums`.
  - The subsequent pairwise swap loop runs in $\mathcal{O}(n)$ time.
  - Overall Time Complexity: $\mathcal{O}(n \log n)$.
  *(Note: Because $nums[i] \le 100$, Counting Sort could achieve $\mathcal{O}(n + K)$ time where $K = 100$, but comparison sort is standard, clean, and optimal for arbitrary ranges).*

- **Space Complexity:** 
  - $\mathcal{O}(1)$ auxiliary space if modifying in-place, or $\mathcal{O}(n)$ space allocated internally by Timsort for slicing/merging operations.

### Common Pitfalls / Mistakes Candidates Make

1. **Simulating using min-heaps / repeated `min()` lookups:**
   - Repeatedly calling `min()` and `nums.remove()` results in an inefficient $\mathcal{O}(n^2)$ time complexity.
   - Using a min-heap is $\mathcal{O}(n \log n)$ but introduces unnecessary overhead and $\mathcal{O}(n)$ auxiliary space compared to a simple in-place sort and swap.
2. **Off-by-one errors in stepping:**
   - Using `range(0, len(nums) - 1)` without a step of `2`, or missing the last pair.
3. **Mutability concerns:**
   - Always clarify with the interviewer whether modifying the input array in-place is permitted.

### Real Interview Follow-Up Questions & Answers

#### 1. What if $nums[i]$ is strictly bounded (e.g., $nums[i] \le 100$)?
*Answer:* We can use **Counting Sort** / Bucket Sort. We count the frequencies of all numbers in an array of size 101, then reconstruct the sorted pairs on the fly, reducing time complexity to $\mathcal{O}(n + K)$ where $K = \max(nums)$.

#### 2. What if $nums$ is an unbounded incoming stream of even total length?
*Answer:* If the stream needs to process rounds dynamically without waiting for all elements, it's fundamentally not possible because Alice and Bob need the global minimums at each step. However, if the stream arrives in batches of known size, we could use a min-heap or external merge sort depending on memory limits.

#### 3. How would you solve this if in-place mutation of the input is strictly forbidden?
*Answer:* Instead of swapping in-place, construct a new array using list comprehension:
```python
arr = []
nums_sorted = sorted(nums)
for i in range(0, len(nums_sorted), 2):
    arr.extend([nums_sorted[i + 1], nums_sorted[i]])
return arr
```
This guarantees immutability of the original argument while preserving $\mathcal{O}(n \log n)$ time.
