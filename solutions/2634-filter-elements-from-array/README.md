# 2634. Filter Elements from Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/filter-elements-from-array/](https://leetcode.com/problems/filter-elements-from-array/)  
**Topics:** 

---

## 📝 Problem Statement

Given an integer array `arr` and a filtering function `fn`, return a filtered array `filteredArr`.

The `fn` function takes one or two arguments:

	- `arr[i]` - number from the `arr`

	- `i` - index of `arr[i]`

`filteredArr` should only contain the elements from the `arr` for which the expression `fn(arr[i], i)` evaluates to a **truthy** value. A **truthy** value is a value where `Boolean(value)` returns `true`.

Please solve it without the built-in `Array.filter` method.

 
Example 1:

```

**Input:** arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }
**Output:** [20,30]
**Explanation:**
const newArray = filter(arr, fn); // [20, 30]
The function filters out values that are not greater than 10
```

Example 2:

```

**Input:** arr = [1,2,3], fn = function firstIndex(n, i) { return i === 0; }
**Output:** [1]
**Explanation:**
fn can also accept the index of each element
In this case, the function removes elements not at index 0

```

Example 3:

```

**Input:** arr = [-2,-1,0,1,2], fn = function plusOne(n) { return n + 1 }
**Output:** [-2,0,1,2]
**Explanation:**
Falsey values such as 0 should be filtered out

```

 
**Constraints:**

	- `0 9 9`

---

## 💻 Implementation (python3)

```js
/**
 * Custom implementation of Array.prototype.filter.
 * 
 * @param {number[]} arr - The input array of numbers.
 * @param {Function} fn - The filtering callback function taking (element, index).
 * @return {number[]} - Array containing only elements where fn returned a truthy value.
 */
var filter = function(arr, fn) {
    const filteredArr = [];
    
    // Iterate through the array maintaining the original index
    for (let i = 0; i < arr.length; i++) {
        // Truthy check: In JavaScript, `if (condition)` implicitly evaluates Boolean(condition)
        if (fn(arr[i], i)) {
            filteredArr.push(arr[i]);
        }
    }
    
    return filteredArr;
};
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The objective is to implement the core functionality of JavaScript's native `Array.prototype.filter` method from scratch without utilizing the built-in function.

Key observations:
1. **Preserving Order & Indices**: We need to examine each element in sequence from left to right, tracking both the current element `arr[i]` and its index `i`.
2. **Truthy Evaluation**: The filtering function `fn` returns a value that might not strictly be a boolean (e.g., `fn(n)` might return a number like `1` or `0`, a string, or an object). In JavaScript, the `if (...)` statement inherently checks for truthiness using abstract boolean conversion rules (equivalent to `Boolean(fn(arr[i], i)) === true`).
3. **Memory Allocation**: We collect qualifying elements into a new array.

### Step-by-Step Approach

1. Initialize an empty array `filteredArr`.
2. Loop through the input array `arr` using a standard `for` loop from index `0` up to `arr.length - 1`.
3. In each iteration, invoke `fn(arr[i], i)`.
4. If the returned value is truthy, append `arr[i]` to `filteredArr`.
5. Return `filteredArr`.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$, where $N$ is the number of elements in `arr`. Assuming `fn` runs in $\mathcal{O}(1)$ time, we iterate through the array once and perform an $\mathcal{O}(1)$ amortized append operation for qualifying elements.
- **Space Complexity**: $\mathcal{O}(N)$ in the worst case (when all elements satisfy the predicate) to store the result array. The auxiliary space used (excluding the returned array) is $\mathcal{O}(1)$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Strict Equality Check on Booleans**:
   ```javascript
   // WRONG
   if (fn(arr[i], i) === true)
   ```
   If `fn` returns a truthy value like a non-zero number (e.g., `fn(n) = n + 1` returning `2`), `2 === true` evaluates to `false`. Always rely on implicit truthiness `if (fn(arr[i], i))` or `if (Boolean(fn(arr[i], i)))`.

2. **Incorrect Argument Order**:
   Passing `fn(i, arr[i])` instead of `fn(arr[i], i)`. JavaScript convention for array higher-order methods is always `(element, index, array)`.

3. **Using Built-ins**:
   Accidentally using `arr.filter(...)` or `arr.reduce(...)` when the prompt explicitly forbids using the built-in filter functionality.

---

### Real Interview Follow-Up Questions

#### 1. In-place Filtering (Memory Constraints: $\mathcal{O}(1)$ Auxiliary Space)
**Question:** What if memory is extremely constrained and you are required to modify the original array in-place without allocating an extra array?
**Answer:** We can use the two-pointer technique (similar to LeetCode #26 / #27):
```javascript
var filterInPlace = function(arr, fn) {
    let writeIndex = 0;
    for (let readIndex = 0; readIndex < arr.length; readIndex++) {
        if (fn(arr[readIndex], readIndex)) {
            arr[writeIndex] = arr[readIndex];
            writeIndex++;
        }
    }
    arr.length = writeIndex; // Truncate the array
    return arr;
};
```
*Time Complexity:* $\mathcal{O}(N)$, *Auxiliary Space Complexity:* $\mathcal{O}(1)$.

#### 2. Handling Sparse Arrays
**Question:** How does native `Array.prototype.filter` handle sparse arrays (e.g., `[1, , 3]`), and does our implementation behave the same?
**Answer:** Native `Array.prototype.filter` skips empty slots (holes) and does not invoke the callback on them. In our current implementation, `arr[i]` will be `undefined`, and `fn` will still be invoked. To mimic native behavior:
```javascript
if (i in arr && fn(arr[i], i)) {
    filteredArr.push(arr[i]);
}
```

#### 3. Handling Infinite / Streaming Data
**Question:** How would you adapt this for asynchronous or continuous streaming data (e.g., RxJS observables or async generators)?
**Answer:** We can implement an async generator function that yields items as they pass the predicate:
```javascript
async function* filterAsyncStream(stream, asyncFn) {
    let index = 0;
    for await (const item of stream) {
        if (await asyncFn(item, index++)) {
            yield item;
        }
    }
}
```
