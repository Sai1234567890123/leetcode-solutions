# 2724. Sort By

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/sort-by/](https://leetcode.com/problems/sort-by/)  
**Topics:** 

---

## 📝 Problem Statement

Given an array `arr` and a function `fn`, return a sorted array `sortedArr`. You can assume `fn` only returns numbers and those numbers determine the sort order of `sortedArr`. `sortedArr` must be sorted in **ascending order** by `fn` output.

You may assume that `fn` will never duplicate numbers for a given array.

 
Example 1:

```

**Input:** arr = [5, 4, 1, 2, 3], fn = (x) => x
**Output:** [1, 2, 3, 4, 5]
**Explanation:** fn simply returns the number passed to it so the array is sorted in ascending order.

```

Example 2:

```

**Input:** arr = [{"x": 1}, {"x": 0}, {"x": -1}], fn = (d) => d.x
**Output:** [{"x": -1}, {"x": 0}, {"x": 1}]
**Explanation:** fn returns the value for the "x" key. So the array is sorted based on that value.

```

Example 3:

```

**Input:** arr = [[3, 4], [5, 2], [10, 1]], fn = (x) => x[1]
**Output:** [[10, 1], [5, 2], [3, 4]]
**Explanation:** arr is sorted in ascending order by number at index=1. 

```

 
**Constraints:**

	- `arr` is a valid JSON array

	- `fn` is a function that returns a number

	- `1 5`

---

## 💻 Implementation (python3)

```js
/**
 * Sorts an array in ascending order based on the output of a mapping function.
 *
 * @param {Array} arr - The array of items to sort.
 * @param {Function} fn - Function that returns a numeric key for each item.
 * @return {Array} - The sorted array.
 */
var sortBy = function(arr, fn) {
    // Array.prototype.sort takes a comparator function (a, b).
    // Comparing fn(a) - fn(b) sorts elements in ascending order of their fn values.
    // If fn(a) < fn(b), result is negative -> 'a' comes before 'b'.
    // If fn(a) > fn(b), result is positive -> 'b' comes before 'a'.
    return arr.sort((a, b) => fn(a) - fn(b));
};
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires ordering the elements of an array `arr` based on the numerical value returned by a provided transformation function `fn(x)`. 

In JavaScript, `Array.prototype.sort()` takes an optional comparator function `compareFn(a, b)`. If provided:
- A negative return value indicates that `a` should come before `b`.
- A positive return value indicates that `b` should come before `a`.
- Zero indicates that the elements are equal in priority.

Since `fn` is guaranteed to return numbers and we need ascending order, the comparator simply evaluates:
$$\text{comparator}(a, b) = fn(a) - fn(b)$$

### Step-by-Step Approach

1. Call `arr.sort()` directly on the input array.
2. Provide an arrow comparator `(a, b) => fn(a) - fn(b)`.
3. Return the mutated and sorted array reference.

*Note on Precomputation (Schwartzian Transform / Decorate-Sort-Undecorate):*
In standard interview settings, if `fn` is computationally heavy (e.g., $O(K)$ or network/disk I/O), computing `fn` inside the comparator would call `fn` $O(N \log N)$ times. In such cases, it is optimal to precompute the keys:
```javascript
return arr
    .map(item => ({ item, key: fn(item) }))
    .sort((a, b) => a.key - b.key)
    .map(({ item }) => item);
```
However, under standard LeetCode constraints where `fn` is an $O(1)$ accessor or mathematical calculation, `arr.sort((a, b) => fn(a) - fn(b))` minimizes memory allocations and avoids $O(N)$ object creation overhead.

### Complexity Analysis

- **Time Complexity:** $O(N \log N)$ on average and worst-case, where $N$ is the length of `arr`. Modern JavaScript engines (such as V8 in Node.js and Chrome) use Timsort, which guarantees $O(N \log N)$ comparisons.
- **Space Complexity:** $O(\log N)$ or $O(1)$ auxiliary space depending on the engine's Timsort implementation stack frames. The sort is performed in-place.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Default Lexicographical Sort:**
   Calling `arr.sort()` without a comparator converts elements to strings. For example, `[10, 2].sort()` results in `[10, 2]` because `"10"` comes before `"2"` alphabetically. Always pass an explicit numerical comparator.
   
2. **Integer Overflow in Other Languages:**
   While JavaScript numbers are double-precision IEEE 754 floats (safe up to `Number.MAX_SAFE_INTEGER`), using subtraction `a - b` in languages like Java, C++, or C# can cause 32-bit integer overflow. In those languages, explicit comparisons or `Long.compare()` should be used.

3. **Impure / Non-deterministic `fn`:**
   Assuming `fn` could return `NaN` or non-numeric types would break Timsort invariants and cause non-deterministic ordering or sorting bugs.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if `fn` is computationally expensive?
**Answer:** Use the Schwartzian Transform (Decorate-Sort-Undecorate). Precompute `fn(x)` exactly once for each of the $N$ elements into an array of tuples or objects `[fn(x), x]`, sort the wrapper objects (which only performs $O(1)$ number comparisons), and then extract the original elements. This reduces calls to `fn` from $O(N \log N)$ down to $O(N)$ at the cost of $O(N)$ auxiliary space.

#### 2. What if the input array does not fit into memory (External Sorting)?
**Answer:** We cannot use `Array.prototype.sort`. We divide the dataset into manageable chunks that fit into RAM, sort each chunk using standard sorting, and write them back to disk as temporary files. Then, perform a multi-way merge (using a Min-Heap / Priority Queue) across all sorted runs to stream the output.

#### 3. How does stability matter here?
**Answer:** A sort is stable if it preserves the relative order of elements with equal keys. ECMAScript 2019 (ES10) strictly mandates that `Array.prototype.sort` must be stable. If two elements produce the same `fn` value, their initial relative order in `arr` will be preserved.
