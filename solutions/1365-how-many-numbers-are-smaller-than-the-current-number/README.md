# 1365. How Many Numbers Are Smaller Than the Current Number

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)  
**Topics:** Array, Hash Table, Sorting, Counting Sort

---

## 📝 Problem Statement

Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` **and** `nums[j] 

Return the answer in an array.

 
Example 1:

```

**Input:** nums = [8,1,2,2,3]
**Output:** [4,0,1,1,3]
**Explanation:** 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

```

Example 2:

```

**Input:** nums = [6,5,4,8]
**Output:** [2,1,0,3]

```

Example 3:

```

**Input:** nums = [7,7,7,7]
**Output:** [0,0,0,0]

```

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # Given constraint: 0 <= nums[i] <= 100
        # We can use a frequency array and prefix sums for O(N + K) optimal time.
        MAX_VAL = 100
        freq = [0] * (MAX_VAL + 1)
        
        # Step 1: Count frequency of each number
        for num in nums:
            freq[num] += 1
            
        # Step 2: Compute running count of strictly smaller numbers
        # smaller_count[i] will store the number of elements strictly less than i
        smaller_count = [0] * (MAX_VAL + 1)
        running_sum = 0
        for i in range(MAX_VAL + 1):
            smaller_count[i] = running_sum
            running_sum += freq[i]
            
        # Step 3: Map each number in the original list to its smaller count
        return [smaller_count[num] for num in nums]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A brute-force approach compares every pair $(i, j)$, leading to an $O(N^2)$ runtime. 
Another standard approach is sorting the array: if we sort a copy of `nums`, the first index where a number appears corresponds directly to how many numbers are smaller than it. Storing this mapping in a hash table yields an $O(N \log N)$ runtime.

However, the constraints explicitly state that $0 \le nums[i] \le 100$. This bounded range allows for a **Counting Sort / Prefix Sum** technique:
1. Count the occurrences of each distinct value in $O(N)$ time.
2. Build a prefix sum array where each index $v$ records the total count of numbers strictly less than $v$ in $O(K)$ time (where $K = 101$).
3. For each element in the original list, look up its count in $O(1)$ time.

This improves both time and auxiliary space to optimal bounds.

---

### Step-by-Step Approach

1. **Frequency Array Initialization**: Create an array `freq` of size 101 initialized to zeros.
2. **Frequency Count**: Iterate through `nums` and increment `freq[num]`.
3. **Prefix Sum (Accumulation)**:
   - Maintain a `running_sum` representing the count of all elements strictly smaller than the current index $i$.
   - For each $i \in [0, 100]$, set `smaller_count[i] = running_sum`, then add `freq[i]` to `running_sum`.
4. **Result Construction**: Use a list comprehension to map each element `num` in `nums` to `smaller_count[num]`.

---

### Complexity Analysis

- **Time Complexity**: $O(N + K)$, where $N$ is the number of elements in `nums` and $K = 101$ is the range of values $[0, 100]$. Since $K$ is a constant, this runs in strictly linear $O(N)$ time.
- **Space Complexity**: $O(K)$ auxiliary space for the frequency and prefix arrays. Since $K = 101$ is fixed, auxiliary space is $O(1)$ (excluding the returned result array which takes $O(N)$ space).

---

### Common Pitfalls / Mistakes Candidates Make

1. **Defaulting to $O(N^2)$**: Overlooking the constraints and writing nested loops.
2. **Ignoring the Duplicate Count**: When sorting the array, candidates often mistakenly use `nums.index(x)` inside a loop (which degrades to $O(N^2)$) or forget that duplicates share the exact same count of strictly smaller numbers (e.g., using current index instead of first occurrence index).
3. **Missing the Value Range**: Overlooking the bounded constraint $nums[i] \le 100$ and implementing an $O(N \log N)$ sorting solution instead of the linear $O(N)$ counting sort.

---

### Real Interview Follow-Up Questions

#### 1. What if the range of numbers is very large (e.g., $-10^9 \le nums[i] \le 10^9$)?
- **Answer**: The counting sort approach is no longer feasible due to memory limitations.
  - **Sorting + Hash Map ($O(N \log N)$ time, $O(N)$ space)**:
    Sort a copy of `nums`. Iterate through the sorted array and store `num -> index` in a hash map only for the first occurrence of `num`. Then, build the answer array using the map.
  - **Coordinate Compression**: Map the unique sorted values to ranks $[0, U-1]$ and proceed accordingly.

#### 2. What if data is arriving as a stream, and we need the count of smaller numbers dynamically?
- **Answer**:
  - If dynamic counts must be reported relative to the elements seen *so far* (e.g., LeetCode 315: Count of Smaller Numbers After Self):
    - Use a **Fenwick Tree (Binary Indexed Tree)** or **Segment Tree** over coordinates.
    - Alternatively, maintain a **Self-Balancing Binary Search Tree** (like an AVL tree or Treap) augmented with subtree sizes. Insertion and rank queries will take $O(\log N)$ time per element.
