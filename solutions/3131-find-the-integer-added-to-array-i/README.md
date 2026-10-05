# 3131. Find the Integer Added to Array I

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-the-integer-added-to-array-i/](https://leetcode.com/problems/find-the-integer-added-to-array-i/)  
**Topics:** Array

---

## 📝 Problem Statement

You are given two arrays of equal length, `nums1` and `nums2`.

Each element in `nums1` has been increased (or decreased in the case of negative) by an integer, represented by the variable `x`.

As a result, `nums1` becomes **equal** to `nums2`. Two arrays are considered **equal** when they contain the same integers with the same frequencies.

Return the integer `x`.

 
Example 1:

**Input:** nums1 = [2,6,4], nums2 = [9,7,5]

**Output:** 3

**Explanation:**

The integer added to each element of `nums1` is 3.

Example 2:

**Input:** nums1 = [10], nums2 = [5]

**Output:** -5

**Explanation:**

The integer added to each element of `nums1` is -5.

Example 3:

**Input:** nums1 = [1,1,1,1], nums2 = [1,1,1,1]

**Output:** 0

**Explanation:**

The integer added to each element of `nums1` is 0.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Finds the integer x added to every element of nums1 to make it equal to nums2.
        
        Since every element in nums1 is shifted by the exact same value x, 
        the minimum element in nums1 must map to the minimum element in nums2.
        Therefore, x = min(nums2) - min(nums1).
        """
        return min(nums2) - min(nums1)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem states that after adding an unknown integer $x$ to every element of `nums1`, the frequency of every element in `nums1` matches `nums2`. In other words, `nums2` is a permutation of `nums1` where every value has been translated by $x$.

Because the relative order of elements is preserved under a uniform shift:
1. The smallest element in `nums1` must become the smallest element in `nums2`.
2. The largest element in `nums1` must become the largest element in `nums2`.
3. The sum of `nums2` equals the sum of `nums1` plus $n \times x$.

The most direct and overflow-safe relationship is tracking the minimums:
$$\min(\text{nums2}) = \min(\text{nums1}) + x \implies x = \min(\text{nums2}) - \min(\text{nums1})$$

### Step-by-Step Approach

1. Compute the minimum value of `nums1`.
2. Compute the minimum value of `nums2`.
3. Return the difference: $\min(\text{nums2}) - \min(\text{nums1})$.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the length of `nums1` (and `nums2`). Finding the minimum of both arrays requires a single linear scan over each array.
- **Space Complexity:** $O(1)$ auxiliary space, as only a constant number of variables are used.

### Common Pitfalls / Mistakes Candidates Make

1. **Sorting the Arrays ($O(n \log n)$):**
   A common knee-jerk reaction is to sort both `nums1` and `nums2` and compute `nums2[0] - nums1[0]`. While correct, sorting takes $O(n \log n)$ time, which is suboptimal compared to the linear scan $O(n)$.
2. **Using Sums in Languages with Fixed-Width Integers:**
   Using $x = \frac{\sum \text{nums2} - \sum \text{nums1}}{n}$ is theoretically $O(n)$, but summing large arrays in languages like C++ or Java can lead to integer overflow if 32-bit integers are used. Comparing extremums ($\min$ or $\max$) completely bypasses overflow concerns.

### Real Interview Follow-Up Questions

#### 1. What if the problem did not guarantee that a valid $x$ exists?
*Answer:* After calculating candidate $x = \min(\text{nums2}) - \min(\text{nums1})$, we would need to verify the condition. We could sort both arrays in $O(n \log n)$ and check if $\text{nums2}[i] - \text{nums1}[i] == x$ for all $i$, or use a hash map / frequency counter to verify that the multiset of $(\text{nums1}[i] + x)$ equals $\text{nums2}$ in $O(n)$ time and $O(n)$ space.

#### 2. What if data is arriving as an unbounded stream?
*Answer:* We can maintain running minimums of both streams using two scalar variables:
```python
min1 = min(min1, new_val_1)
min2 = min(min2, new_val_2)
```
At any point, the shift candidate remains $x = \min_2 - \min_1$, requiring $O(1)$ memory per update.

#### 3. How would you parallelize this for massive datasets (e.g., billions of elements distributed across a cluster)?
*Answer:* Finding the minimum is an associative and commutative reduction operation. In MapReduce / Spark:
- **Map phase:** Compute local minimums for each partition.
- **Reduce phase:** Aggregate partition minimums to find global $\min(\text{nums1})$ and $\min(\text{nums2})$.
- Finally, compute the difference on the driver node.
