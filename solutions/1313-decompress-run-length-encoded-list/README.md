# 1313. Decompress Run-Length Encoded List

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/decompress-run-length-encoded-list/](https://leetcode.com/problems/decompress-run-length-encoded-list/)  
**Topics:** Array

---

## 📝 Problem Statement

We are given a list `nums` of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements `[freq, val] = [nums[2*i], nums[2*i+1]]` (with `i >= 0`).  For each such pair, there are `freq` elements with value `val` concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

 
Example 1:

```

**Input:** nums = [1,2,3,4]
**Output:** [2,4,4,4]
**Explanation:** The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

```

Example 2:

```

**Input:** nums = [1,1,2,3]
**Output:** [1,3,3]

```

 
**Constraints:**

	- `2 1 `

---

## 💻 Implementation (python3)

```py
class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        decompressed: list[int] = []
        
        # Iterate through nums in pairs: (freq, val) at indices (i, i + 1)
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            # [val] * freq creates the repeated sequence in C-speed,
            # and extend appends the elements in-place to avoid reallocating intermediate lists.
            decompressed.extend([val] * freq)
            
        return decompressed
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem provides a 1D array compressed using Run-Length Encoding (RLE). Every even index `2 * i` represents the frequency (`freq`), and the subsequent odd index `2 * i + 1` represents the value (`val`). 

The objective is to reconstruct the original list by expanding each `(freq, val)` pair into `freq` instances of `val` and concatenating them in order.

In Python, the most performant and idiomatic way to expand and concatenate is using `list.extend([val] * freq)`. Python's `[val] * freq` allocates a list of size `freq` with pointers pointing to the single integer object `val` in $O(\text{freq})$ time via fast C-level memory initialization, and `list.extend` handles amortized dynamic resizing efficiently.

### Step-by-Step Approach
1. Initialize an empty list `decompressed`.
2. Loop through `nums` with a step size of 2 (i.e., `range(0, len(nums), 2)`).
3. At index `i`, extract `freq = nums[i]` and `val = nums[i + 1]`.
4. Append `freq` copies of `val` to `decompressed` using `decompressed.extend([val] * freq)`.
5. Return `decompressed`.

### Complexity Analysis
- **Time Complexity:** $O(N + M)$, where $N$ is the length of `nums` and $M = \sum \text{nums}[2i]$ is the total number of elements in the decompressed list. We touch each element in `nums` once ($O(N)$) and write $M$ elements to the output array ($O(M)$). Since $M \ge N/2$, this is asymptotically $O(M)$.
- **Space Complexity:** $O(1)$ auxiliary space (excluding the memory required to store the returned output list of size $M$).

### Common Pitfalls / Mistakes Candidates Make
1. **Inefficient Concatenation:** Using `result = result + [val] * freq` inside the loop. This creates a brand-new list on every iteration, leading to an accidental $O(M^2)$ time complexity due to repeated copying. Always use `extend()` or `+=` which mutates in-place.
2. **Off-by-one / Index Errors:** Forgetting that `range` step is 2, or indexing out of bounds when accessing `i + 1`. The problem constraint guarantees `len(nums)` is even, but defensive bounds checking is good practice in production code.

### Real Interview Follow-Up Questions

#### 1. What if the decompressed list is extremely large (e.g., gigabytes/terabytes) and cannot fit in memory?
*Answer:* Return a generator / iterator instead of an instantiated list. 
```python
def decompress_stream(nums: list[int]):
    for i in range(0, len(nums), 2):
        freq, val = nums[i], nums[i + 1]
        for _ in range(freq):
            yield val
```
This reduces the auxiliary memory footprint to $O(1)$.

#### 2. How would you handle random access (e.g., finding the element at index `k` in the decompressed list) without decompressing?
*Answer:* Compute the prefix sums of the frequencies:
- The compressed array defines intervals of indices.
- A prefix sum array of frequencies `P` where `P[i] = P[i-1] + freq_i` allows us to use **Binary Search** (`bisect_right`) to find which bucket index `k` falls into in $O(\log(N/2))$ time and $O(1)$ additional decompression space.

#### 3. How would you parallelize the decompression across multiple CPU cores?
*Answer:* 
1. Calculate the prefix sum of frequencies to determine the exact destination index slice `[start_idx, end_idx)` in a pre-allocated shared-memory array for each `(freq, val)` block.
2. Distribute chunks of pairs to worker threads/processes.
3. Each worker writes directly into its assigned slice without needing locks or synchronization.
