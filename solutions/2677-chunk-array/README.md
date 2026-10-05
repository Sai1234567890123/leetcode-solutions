# 2677. Chunk Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/chunk-array/](https://leetcode.com/problems/chunk-array/)  
**Topics:** 

---

## 📝 Problem Statement

Given an array `arr` and a chunk size `size`, return a **chunked** array.

A **chunked** array contains the original elements in `arr`, but consists of subarrays each of length `size`. The length of the last subarray may be less than `size` if `arr.length` is not evenly divisible by `size`.

Please solve it without using lodash's `_.chunk` function.

 
Example 1:

```

**Input:** arr = [1,2,3,4,5], size = 1
**Output:** [[1],[2],[3],[4],[5]]
**Explanation:** The arr has been split into subarrays each with 1 element.

```

Example 2:

```

**Input:** arr = [1,9,6,3,2], size = 3
**Output:** [[1,9,6],[3,2]]
**Explanation:** The arr has been split into subarrays with 3 elements. However, only two elements are left for the 2nd subarray.

```

Example 3:

```

**Input:** arr = [8,5,3,2,6], size = 6
**Output:** [[8,5,3,2,6]]
**Explanation:** Size is greater than arr.length thus all elements are in the first subarray.

```

Example 4:

```

**Input:** arr = [], size = 1
**Output:** []
**Explanation:** There are no elements to be chunked so an empty array is returned.
```

 
**Constraints:**

	- `arr` is a string representing the array.

	- `2 5`

	- `1

---

## 💻 Implementation (python3)

```js
/**
 * Chunks an array into subarrays of specified size.
 * 
 * @param {Array} arr - The array to process.
 * @param {number} size - The length of each chunk.
 * @return {Array} - The array of chunks.
 */
var chunk = function(arr, size) {
    const chunked = [];
    
    // Step through the array in strides of `size`
    for (let i = 0; i < arr.length; i += size) {
        // Array.prototype.slice handles out-of-bound indices gracefully
        // by slicing up to arr.length without throwing an error
        chunked.push(arr.slice(i, i + size));
    }
    
    return chunked;
};
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The objective is to partition an array `arr` into smaller arrays, each having a maximum length of `size`. If the number of remaining elements is less than `size`, the final chunk should just contain whatever elements are left.

In JavaScript, `Array.prototype.slice(start, end)` is an ideal built-in method for this operation:
- It returns a shallow copy of a portion of an array from index `start` up to (but not including) `end`.
- Crucially, if `end` exceeds `arr.length`, `slice` naturally extracts only up to the end of the array without throwing an index out-of-bounds error.

By advancing our loop index `i` by `size` on each iteration, we can extract contiguous blocks of length `size` in $O(N)$ total operations.

---

### Step-by-Step Approach

1. Initialize an empty result array `chunked`.
2. Loop through `arr` starting at index `i = 0`, incrementing `i` by `size` on each step (`i += size`).
3. For each iteration, slice the subarray from `i` to `i + size` and push it into `chunked`.
4. Return `chunked`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of elements in `arr`.
  - The loop runs $\lceil N / \text{size} \rceil$ times.
  - In each iteration, `arr.slice(i, i + size)` copies up to `size` elements.
  - In total, every element is visited and copied exactly once: $\sum \text{chunk size} = N$.

- **Space Complexity:** $\mathcal{O}(N)$ (or $\mathcal{O}(1)$ auxiliary space excluding the returned output).
  - The output array holds all $N$ original elements partitioned across subarrays.
  - No additional non-trivial memory is allocated during execution.

---

### Common Pitfalls / Mistakes

1. **Off-by-One & Bounds Checking:** Candidates often write manual inner loops to build chunks and forget to break when the index reaches `arr.length`, or incorrectly handle when `arr.length % size !== 0`.
2. **Mutating the Input:** Using `arr.splice(0, size)` inside a `while (arr.length)` loop is a destructive approach that takes $\mathcal{O}(N^2)$ time because `splice` shifts elements on each removal.
3. **Invalid `size` Handling:** In production code, passing `size <= 0` can lead to an infinite loop if `i` doesn't advance. While constraints here guarantee valid `size`, in an interview, clarifying or adding `if (size <= 0) return [];` is good practice.

---

### Real Interview Follow-Up Questions

#### 1. What if the input array is extremely large and does not fit into memory (Streaming / Generator approach)?
**Answer:** We can write a generator function (`function*`) to yield chunks lazily. This allows processing one chunk at a time with $\mathcal{O}(\text{size})$ auxiliary memory rather than loading all chunks into memory at once:
```javascript
function* chunkGenerator(iterable, size) {
    let chunk = [];
    for (const item of iterable) {
        chunk.push(item);
        if (chunk.length === size) {
            yield chunk;
            chunk = [];
        }
    }
    if (chunk.length > 0) {
        yield chunk;
    }
}
```

#### 2. How do shallow copies affect nested objects inside `arr`?
**Answer:** `Array.prototype.slice` creates a shallow copy. If `arr` contains objects, modifying an object inside a chunk modifies the object in the original `arr`. If complete isolation is required, a deep copy (e.g., using `structuredClone`) must be performed, which incurs extra CPU and memory overhead.

#### 3. How would you handle this in a distributed or multi-threaded context (e.g., batch processing jobs)?
**Answer:** The chunking logic can be distributed by determining chunk boundaries mathematically using indices: Chunk $k$ starts at index $k \times \text{size}$ and ends at $\min((k + 1) \times \text{size}, N)$. Workers can directly read their assigned byte/index ranges without needing a centralized chunk coordinator.
