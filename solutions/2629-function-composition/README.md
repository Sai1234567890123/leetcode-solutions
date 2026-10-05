# 2629. Function Composition

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/function-composition/](https://leetcode.com/problems/function-composition/)  
**Topics:** 

---

## 📝 Problem Statement

Given an array of functions `[f1, f2, f3, ..., fn]`, return a new function `fn` that is the **function composition** of the array of functions.

The **function composition** of `[f(x), g(x), h(x)]` is `fn(x) = f(g(h(x)))`.

The **function composition** of an empty list of functions is the **identity function** `f(x) = x`.

You may assume each function in the array accepts one integer as input and returns one integer as output.

 
Example 1:

```

**Input:** functions = [x => x + 1, x => x * x, x => 2 * x], x = 4
**Output:** 65
**Explanation:**
Evaluating from right to left ...
Starting with x = 4.
2 * (4) = 8
(8) * (8) = 64
(64) + 1 = 65

```

Example 2:

```

**Input:** functions = [x => 10 * x, x => 10 * x, x => 10 * x], x = 1
**Output:** 1000
**Explanation:**
Evaluating from right to left ...
10 * (1) = 10
10 * (10) = 100
10 * (100) = 1000

```

Example 3:

```

**Input:** functions = [], x = 42
**Output:** 42
**Explanation:**
The composition of zero functions is the identity function
```

 
**Constraints:**

	- `-1000 `

	- `0 `

	- all functions accept and return a single integer

---

## 💻 Implementation (python3)

```js
/**
 * Composes an array of functions from right to left.
 *
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        // Iterate from right to left to evaluate functions in composition order:
        // fn(x) = f1(f2(...fn(x)))
        let result = x;
        for (let i = functions.length - 1; i >= 0; i--) {
            result = functions[i](result);
        }
        return result;
    };
};
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

Function composition in mathematics is defined as $(f \circ g)(x) = f(g(x))$. For a list of functions $[f_1, f_2, \dots, f_n]$, the composed function applied to an input $x$ is:
$$f_1(f_2(\dots f_n(x) \dots))$$

This means evaluation happens **strictly from right to left**:
1. Apply the last function $f_n$ to the input $x$.
2. Feed its result into the second to last function $f_{n-1}$.
3. Repeat this process until $f_1$ produces the final output.
4. If the array is empty, we return the input $x$ unchanged (the identity function).

While JavaScript provides `Array.prototype.reduceRight`, an imperative backwards `for` loop is typically preferred in performance-critical code because it avoids the overhead of allocating and executing an extra callback function for every element in the array.

### Step-by-Step Approach

1. Return a closure that accepts the starting argument `x`.
2. Initialize an accumulator variable `result = x`.
3. Loop backwards from index `functions.length - 1` down to `0`.
4. Update `result` at each step by invoking the current function with `result`: `result = functions[i](result)`.
5. Return the final `result`. If `functions` is empty, the loop will not execute, and the initial value `x` is immediately returned.

### Complexity Analysis

- **Time Complexity:** 
  - **Setup (`compose`):** $\mathcal{O}(1)$ — simply returns a closure.
  - **Execution (`fn(x)`):** $\mathcal{O}(n)$, where $n$ is the number of functions in the `functions` array, assuming each function runs in $\mathcal{O}(1)$ time.
- **Space Complexity:** 
  - **Auxiliary Space:** $\mathcal{O}(1)$ — only a single primitive variable (`result`) is maintained during execution.
  - **Closure Memory:** $\mathcal{O}(1)$ additional memory (only holding a reference to the existing `functions` array).

---

### Common Pitfalls & Mistakes Candidates Make

1. **Left-to-Right Evaluation:**
   - A classic mistake is iterating from index `0` to `n - 1` (equivalent to `Array.prototype.reduce`), which evaluates the pipeline as $f_n(\dots f_1(x))$, known as `pipe`, rather than standard mathematical composition `compose`.
2. **Mutating the Input Array:**
   - Using `functions.reverse().reduce(...)` mutates the input array in place, which causes unexpected side-effects if the original array is reused elsewhere.
3. **Handling the Empty Array:**
   - Forgetting that an empty list must return an identity function ($f(x) = x$).
4. **Recursion Overflows:**
   - Using recursion instead of an iterative loop can lead to `Maximum call stack size exceeded` errors if $n$ is large.

---

### Real Interview Follow-Up Questions & How to Answer

#### 1. What if the functions are asynchronous (return Promises)?
**Answer:** We can create `composeAsync` using `async/await` in the loop:
```javascript
const composeAsync = (functions) => async (x) => {
    let result = x;
    for (let i = functions.length - 1; i >= 0; i--) {
        result = await functions[i](result);
    }
    return result;
};
```
Alternatively, using `reduceRight`:
```javascript
const composeAsync = (functions) => (x) => 
    functions.reduceRight(async (accPromise, fn) => fn(await accPromise), Promise.resolve(x));
```

#### 2. What if the rightmost function accepts multiple arguments?
**Answer:** The first function called (the rightmost one) can take multiple arguments, whereas all subsequent functions can only take the single return value of the previous function. We can use rest parameters:
```javascript
const compose = (functions) => {
    if (functions.length === 0) return (x) => x;
    return (...args) => {
        const lastFn = functions[functions.length - 1];
        let result = lastFn(...args);
        for (let i = functions.length - 2; i >= 0; i--) {
            result = functions[i](result);
        }
        return result;
    };
};
```

#### 3. How would you memoize or cache the composed function?
**Answer:** If all functions are pure, we can wrap the returned function in a memoization utility using a `Map` (or a LRU cache) keyed on the input argument to avoid redundant computation.
