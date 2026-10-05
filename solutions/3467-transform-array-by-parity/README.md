# 3467. Transform Array by Parity

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/transform-array-by-parity/](https://leetcode.com/problems/transform-array-by-parity/)  
**Topics:** Array, Sorting, Counting

---

## 📝 Problem Statement

You are given an integer array `nums`. Transform `nums` by performing the following operations in the **exact** order specified:

	- Replace each even number with 0.

	- Replace each odd numbers with 1.

	- Sort the modified array in **non-decreasing** order.

Return the resulting array after performing these operations.

 
Example 1:

**Input:** nums = [4,3,2,1]

**Output:** [0,0,1,1]

**Explanation:**

	- Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, `nums = [0, 1, 0, 1]`.

	- After sorting `nums` in non-descending order, `nums = [0, 0, 1, 1]`.

Example 2:

**Input:** nums = [1,5,1,4,2]

**Output:** [0,0,1,1,1]

**Explanation:**

	- Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, `nums = [1, 1, 1, 0, 0]`.

	- After sorting `nums` in non-descending order, `nums = [0, 0, 1, 1, 1]`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        # Count the number of even integers in the input array.
        # Since even numbers map to 0 and odd numbers map to 1,
        # sorting them simply places all 0s before all 1s.
        even_count = sum(1 for x in nums if x % 2 == 0)
        odd_count = len(nums) - even_count
        
        # Construct and return the result: all zeros followed by all ones.
        return [0] * even_count + [1] * odd_count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem specifies three operations:
1. Replace each even number with `0`.
2. Replace each odd number with `1`.
3. Sort the array in non-decreasing order.

A naive approach would literally map each element `x -> x % 2` and then call a generic sort algorithm like Timsort ($O(n \log n)$).

However, an optimal interview response immediately identifies that:
- Every even number becomes `0`.
- Every odd number becomes `1`.
- Sorting an array containing exclusively `0`s and `1`s simply groups all `0`s first, followed by all `1`s.

Therefore, this problem reduces to counting the frequency of even numbers (which become `0`) and odd numbers (which become `1`), and constructing an array with `even_count` zeros followed by `odd_count` ones. This is essentially the Dutch National Flag / Counting Sort technique, reducing the time complexity from $O(n \log n)$ to $O(n)$.

---

### Step-by-Step Approach

1. Iterate through `nums` once and count the number of even numbers (`x % 2 == 0`).
2. The number of odd numbers is simply `len(nums) - even_count`.
3. Construct the resulting array consisting of `even_count` copies of `0` followed by `odd_count` copies of `1`.

---

### Complexity Analysis

- **Time Complexity:** $O(n)$ where $n$ is the length of `nums`. We perform a single linear scan to count the parity of the elements and another linear pass to allocate/fill the output array. This beats the $O(n \log n)$ sorting approach.
- **Space Complexity:** $O(1)$ auxiliary space (excluding the output array of size $n$). If required to be strictly in-place, we could overwrite `nums` directly using two pointers or slice assignment without extra memory.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Using a general $O(n \log n)$ sort:** Calling `.sort()` on the binary-valued array works, but in an interview setting, failing to recognize that sorting a two-value array can be done in $O(n)$ time shows a lack of optimization intuition.
2. **Handling negative numbers in other languages:** While Python's modulo operator `%` always returns a result with the same sign as the divisor (e.g., `-3 % 2 == 1`), in languages like C++ or Java, `-3 % 2 == -1`. Checking `x % 2 == 0` or using bitwise `(x & 1) == 0` is universally safe across all languages.

---

### Real Interview Follow-Up Questions

#### 1. What if we must perform the operation completely in-place with $O(1)$ extra space?
**Answer:** Use the two-pointer partitioning technique (similar to Lomuto or Hoare partitioning in QuickSort):
- Maintain a pointer `left = 0`.
- Iterate through `nums` with pointer `right`. Whenever `nums[right] % 2 == 0`, swap `nums[left]` and `nums[right]`, then increment `left`.
- Finally, fill indices `0` through `left - 1` with `0`, and indices `left` through `n - 1` with `1`.

#### 2. What if the input arrives as an infinite stream?
**Answer:** Maintain a running count of even and odd numbers received so far. If at any moment a snapshot of the sorted transformed array is requested, output `0` streamed `even_count` times followed by `1` streamed `odd_count` times without needing to store the original numbers.

#### 3. What if we had 3 or $K$ categories instead of 2 (e.g., modulo 3)?
**Answer:** 
- For 3 categories (0, 1, 2), this is the classic **Dutch National Flag problem** (LeetCode 75: Sort Colors), solvable in a single pass in-place using 3 pointers.
- For $K$ categories, standard **Counting Sort** can be applied in $O(n + K)$ time and $O(K)$ space.
