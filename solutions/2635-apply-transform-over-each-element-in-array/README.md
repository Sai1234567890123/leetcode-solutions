# 2635. Apply Transform Over Each Element in Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/apply-transform-over-each-element-in-array/](https://leetcode.com/problems/apply-transform-over-each-element-in-array/)  
**Topics:** 

---

## 📝 Problem Statement

Given an integer array `arr` and a mapping function `fn`, return a new array with a transformation applied to each element.

The returned array should be created such that `returnedArray[i] = fn(arr[i], i)`.

Please solve it without the built-in `Array.map` method.

 
Example 1:

```

**Input:** arr = [1,2,3], fn = function plusone(n) { return n + 1; }
**Output:** [2,3,4]
**Explanation:**
const newArray = map(arr, plusone); // [2,3,4]
The function increases each value in the array by one. 

```

Example 2:

```

**Input:** arr = [1,2,3], fn = function plusI(n, i) { return n + i; }
**Output:** [1,3,5]
**Explanation:** The function increases each value by the index it resides in.

```

Example 3:

```

**Input:** arr = [10,20,30], fn = function constant() { return 42; }
**Output:** [42,42,42]
**Explanation:** The function always returns 42.

```

 
**Constraints:**

	- `0 -109 9`

	- `fn` returns an integer.

---

## 💻 Implementation (python3)

```js
/**
 * Applies a transformation function over each element in an array.
 * 
 * @param {number[]} arr - The input array of integers.
 * @param {Function} fn - The mapping function taking (element, index) and returning a transformed value.
 * @return {number[]} - The newly constructed transformed array.
 */
var map = function(arr, fn) {
    const len = arr.length;
    // Pre-allocate the exact length to prevent dynamic array resizing in V8.
    const result = new Array(len);
    
    for (let i = 0; i < len; i++) {
        // Apply mapping function with current element and current index
        result[i] = fn(arr[i], i);
    }
    
    return result;
};
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to replicate the core behavior of `Array.prototype.map` without using the built-in method. 

1. **Pre-allocation Optimization:** Rather than pushing elements into an empty array (`[]`) and triggering memory reallocations as the underlying array buffer grows, we can instantiate an array of known fixed size `new Array(arr.length)`.
2. **Deterministic Iteration:** A standard indexed `for` loop ensures $O(1)$ constant time step iteration and maintains exact reference to both the element `arr[i]` and the index `i`.
3. **Pure Function Semantics:** The problem specifies returning a *new* array, preserving immutability of the input array `arr`.

### Step-by-Step Approach

1. Cache `arr.length` in a local variable `len`.
2. Instantiate `result = new Array(len)`.
3. Iterate index `i` from `0` to `len - 1`:
   - Compute `result[i] = fn(arr[i], i)`.
4. Return `result`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `arr`. We visit each index exactly once, and each invocation of `fn` executes in $\mathcal{O}(1)$ assuming `fn` does constant-time work.
- **Space Complexity:** $\mathcal{O}(n)$ auxiliary space to allocate and return the transformed array of length $n$. No additional memory is used.

### Common Pitfalls / Mistakes Candidates Make

1. **Ignoring the second argument:** Candidates often write `fn(arr[i])` instead of `fn(arr[i], i)`. The problem specification explicitly states `returnedArray[i] = fn(arr[i], i)`.
2. **Mutating the original array:** Modifying `arr` in-place when the problem expects a new array violates function purity and leads to side-effects.
3. **Using built-in methods:** Falling back to `arr.map`, `arr.forEach`, or `arr.reduce` may violate the constraint ("Please solve it without the built-in Array.map method" and interviewers extending this to avoid built-in iterators entirely to test fundamentals).
4. **Sparse arrays / `for...in` trap:** Using `for...in` instead of an indexed loop will traverse stringified keys, include prototype properties if not guarded, and can lead to incorrect order or performance penalties.

### Real Interview Follow-Up Questions

#### 1. What if memory constraints are extremely tight and the input array is massive?
*Answer:* If immutability is not strictly required and we are allowed to mutate the input, we can perform the transformation **in-place**:
```javascript
for (let i = 0; i < arr.length; i++) {
    arr[i] = fn(arr[i], i);
}
return arr;
```
This reduces auxiliary space to $\mathcal{O}(1)$.

#### 2. How would you handle an infinite or streaming data source (e.g., generator / Node.js streams)?
*Answer:* Rather than collecting all elements in memory, convert the mapper into a generator function:
```javascript
function* mapStream(iterable, fn) {
    let index = 0;
    for (const item of iterable) {
        yield fn(item, index++);
    }
}
```
This enables lazy evaluation, processing one item at a time with $\mathcal{O}(1)$ space.

#### 3. What if `fn` is asynchronous (`fn` returns a Promise)?
*Answer:* 
- If concurrency is allowed:
  ```javascript
  const asyncMap = async (arr, fn) => Promise.all(arr.map((item, i) => fn(item, i)));
  ```
- If order and concurrency limits (e.g., max 5 concurrent requests) are required to prevent resource exhaustion, use a worker pool pattern or libraries like `p-limit`.
