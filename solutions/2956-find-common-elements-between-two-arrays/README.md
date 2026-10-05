# 2956. Find Common Elements Between Two Arrays

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-common-elements-between-two-arrays/](https://leetcode.com/problems/find-common-elements-between-two-arrays/)  
**Topics:** Array, Hash Table

---

## 📝 Problem Statement

You are given two integer arrays `nums1` and `nums2` of sizes `n` and `m`, respectively. Calculate the following values:

	- `answer1` : the number of indices `i` such that `nums1[i]` exists in `nums2`.

	- `answer2` : the number of indices `i` such that `nums2[i]` exists in `nums1`.

Return `[answer1,answer2]`.

 
Example 1:

**Input:** nums1 = [2,3,2], nums2 = [1,2]

**Output:** [2,1]

**Explanation:**

Example 2:

**Input:** nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]

**Output:** [3,4]

**Explanation:**

The elements at indices 1, 2, and 3 in `nums1` exist in `nums2` as well. So `answer1` is 3.

The elements at indices 0, 1, 3, and 4 in `nums2` exist in `nums1`. So `answer2` is 4.

Example 3:

**Input:** nums1 = [3,4,2,3], nums2 = [1,5]

**Output:** [0,0]

**Explanation:**

No numbers are common between `nums1` and `nums2`, so answer is [0,0].

 
**Constraints:**

	- `n == nums1.length`

	- `m == nums2.length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Convert arrays to hash sets for O(1) average-time membership lookups
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Count elements in nums1 that appear in nums2
        count1 = sum(1 for x in nums1 if x in set2)
        
        # Count elements in nums2 that appear in nums1
        count2 = sum(1 for x in nums2 if x in set1)
        
        return [count1, count2]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for two counts:
1. The number of occurrences in `nums1` of elements that exist anywhere in `nums2`.
2. The number of occurrences in `nums2` of elements that exist anywhere in `nums1`.

A naive brute-force approach would check each element of `nums1` against all elements of `nums2` (and vice-versa), taking $O(n \times m)$ time. 

To optimize this, we can precompute the unique elements of both arrays into hash sets:
- Membership checks in a hash set take $O(1)$ average time.
- By converting `nums2` to a hash set `set2`, we can scan `nums1` and count how many elements exist in `set2` in $O(n)$ time.
- Similarly, by converting `nums1` to a hash set `set1`, we can scan `nums2` and count how many elements exist in `set1` in $O(m)$ time.

### Step-by-Step Approach

1. Create a set `set1 = set(nums1)` and a set `set2 = set(nums2)`.
2. Initialize `count1 = sum(1 for x in nums1 if x in set2)`.
3. Initialize `count2 = sum(1 for x in nums2 if x in set1)`.
4. Return `[count1, count2]`.

### Complexity Analysis

- **Time Complexity:** $O(n + m)$, where $n$ is the length of `nums1` and $m$ is the length of `nums2`.
  - Creating `set1` takes $O(n)$ time.
  - Creating `set2` takes $O(m)$ time.
  - Iterating through `nums1` and querying `set2` takes $O(n)$ time.
  - Iterating through `nums2` and querying `set1` takes $O(m)$ time.
  - Overall time complexity is linear: $O(n + m)$.

- **Space Complexity:** $O(n + m)$ (or bounded by the value universe $O(U)$ where $U \le 100$).
  - `set1` stores at most $n$ elements.
  - `set2` stores at most $m$ elements.
  - Total auxiliary space is $O(n + m)$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Misinterpreting Unique vs. Non-Unique Counts:**
   - Some candidates mistakenly count the size of the set intersection (`len(set1 & set2)`), which ignores duplicate elements in the original arrays. The problem asks for the number of *indices* in each array, so duplicate elements that exist in the other array must each be counted.
2. **$O(n \times m)$ Brute-force:**
   - Writing `sum(1 for x in nums1 if x in nums2)` directly without converting `nums2` to a `set`. In Python, checking membership in a list takes $O(m)$ time per query, making the overall time $O(n \times m)$.

---

### Real Interview Follow-Up Questions & Solutions

#### 1. What if memory is extremely constrained (e.g., embedded systems) or space complexity must be $O(1)$ auxiliary space?
- **Answer:** If we can modify the input arrays, we can sort both arrays in-place ($O(n \log n + m \log m)$ time and $O(1)$ space using Heapsort). Then, for each element in `nums1`, we can use binary search on `nums2` to check for existence in $O(\log m)$ time, leading to $O(1)$ auxiliary space.
- Alternatively, given the problem's constraint that numbers are small integers ($1 \le nums[i] \le 100$), we can use a fixed-size 128-bit integer as a bitmask (or a fixed-size boolean array of length 101) to achieve $O(1)$ auxiliary memory and $O(n + m)$ time.

#### 2. What if one array is massive (e.g., stored across a distributed file system like BigQuery/HDFS) and the other fits in memory?
- **Answer:** We load the smaller array into memory, deduplicate it into a hash set (or a Bloom Filter if memory is tight and small false positive rates are acceptable), and stream the large dataset, incrementing the counter whenever a record exists in the hash set.
