# 2626. Array Reduce Transformation

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/array-reduce-transformation/](https://leetcode.com/problems/array-reduce-transformation/)  
**Topics:** 

---

## 📝 Problem Statement

Given an integer array `nums`, a reducer function `fn`, and an initial value `init`, return the final result obtained by executing the `fn` function on each element of the array, sequentially, passing in the return value from the calculation on the preceding element.

This result is achieved through the following operations: `val = fn(init, nums[0]), val = fn(val, nums[1]), val = fn(val, nums[2]), ...` until every element in the array has been processed. The ultimate value of `val` is then returned.

If the length of the array is 0, the function should return `init`.

Please solve it without using the built-in `Array.reduce` method.

 
Example 1:

```

**Input:** 
nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr; }
init = 0
**Output:** 10
**Explanation:**
initially, the value is init=0.
(0) + nums[0] = 1
(1) + nums[1] = 3
(3) + nums[2] = 6
(6) + nums[3] = 10
The final answer is 10.

```

Example 2:

```

**Input:** 
nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr * curr; }
init = 100
**Output:** 130
**Explanation:**
initially, the value is init=100.
(100) + nums[0] * nums[0] = 101
(101) + nums[1] * nums[1] = 105
(105) + nums[2] * nums[2] = 114
(114) + nums[3] * nums[3] = 130
The final answer is 130.

```

Example 3:

```

**Input:** 
nums = []
fn = function sum(accum, curr) { return 0; }
init = 25
**Output:** 25
**Explanation:** For empty arrays, the answer is always init.

```

 
**Constraints:**

	- `0

---

## 💻 Implementation (python3)

```js
/**
 * Executes a reducer function sequentially on each element of an array,
 * passing the accumulated result to the next iteration.
 *
 * @param {number[]} nums - Array of integers to reduce.
 * @param {Function} fn - Reducer callback: fn(accumulator, currentValue).
 * @param {number} init - Initial value for the accumulator.
 * @return {number} - Final accumulated result.
 */
var reduce = function(nums, fn, init) {
    let accumulator = init;

    // Use a classic indexed for-loop for maximum performance in V8
    for (let i = 0; i < nums.length; i++) {
        accumulator = fn(accumulator, nums[i]);
    }

    return accumulator;
};
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The goal is to implement a fold/reduce operation from functional programming principles from scratch without relying on `Array.prototype.reduce`.

A reduction sequentially collapses a collection of values into a single summary value by maintaining an ongoing state (often called an accumulator). 
1. We start with the base state `init`.
2. For each element in the input list, we update the accumulator state using the user-provided binary function: `accumulator = fn(accumulator, currentElement)`.
3. If the input array is empty, the loop body does not execute, gracefully returning `init` without requiring special-case branching.

### Step-by-Step Approach

1. Initialize `accumulator = init`.
2. Iterate through the array `nums` from index `0` to `nums.length - 1`. A traditional indexed `for` loop is preferred in performance-critical JavaScript engines (like V8) because it avoids iterator protocol overhead (`for...of`) and method call overhead (`forEach`).
3. In each iteration, reassign `accumulator` to the return value of `fn(accumulator, nums[i])`.
4. Return `accumulator`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is `nums.length`. We make exactly $N$ invocations of the callback function `fn`. Assuming each execution of `fn` runs in $\mathcal{O}(1)$ time, total execution is strictly linear.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The calculation maintains only a single scalar variable for the accumulator and an index counter, allocating no additional memory.

### Common Pitfalls / Mistakes Candidates Make

1. **Mutating Inputs:** Directly mutating `nums` (e.g., using `nums.shift()` in a `while` loop) leads to an accidental $\mathcal{O}(N^2)$ runtime due to element shifting and violates functional purity.
2. **Missing Empty Array Edge Case:** Forgetting that when `nums.length === 0`, the function should immediately return `init` without calling `fn`.
3. **Using Built-in Methods:** Interviewers explicitly test foundational knowledge; using `Array.prototype.reduce` or wrapping `reduceRight` fails problem constraints.
4. **Passing Incorrect Callback Arguments:** In standard JavaScript, `Array.prototype.reduce` passes `(accumulator, currentValue, currentIndex, array)`. While the problem specification only expects `fn(accumulator, nums[i])`, candidates should be aware of the standard signature when asked.

### Real Interview Follow-Up Questions & Answers

#### 1. What if `init` is optional (mirroring standard `Array.prototype.reduce`)?
**Answer:** If `init` is not provided and the array is empty, JavaScript throws a `TypeError: Reduce of empty array with no initial value`. If elements exist, the accumulator is initialized to `nums[0]`, and iteration starts at index `1`.

#### 2. How would you handle an asynchronous reducer function (`async fn`)?
**Answer:** If `fn` returns a Promise, we must await the resolution before proceeding to the next element:
```javascript
async function asyncReduce(nums, asyncFn, init) {
    let accumulator = init;
    for (let i = 0; i < nums.length; i++) {
        accumulator = await asyncFn(accumulator, nums[i]);
    }
    return accumulator;
}
```

#### 3. How would you handle a continuous data stream where array size is unbounded or unknown?
**Answer:** Use an async generator / `for await...of` loop or an event-driven subscriber (like RxJS / Node.js Streams / Web Streams API). Each chunk or data event updates the internal state without holding previous items in memory, maintaining $\mathcal{O}(1)$ space.

#### 4. Can this operation be parallelized across multiple cores/threads (MapReduce)?
**Answer:** Only if the operation performed by `fn` is **associative** (i.e., `(a + b) + c === a + (b + c)`). If associative, we can split `nums` into chunks, reduce each chunk independently across worker threads, and combine the chunk results (tree reduction). Non-associative operations (e.g., subtraction, non-commutative matrix transformations) must be strictly processed sequentially.
