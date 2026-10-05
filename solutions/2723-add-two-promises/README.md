# 2723. Add Two Promises

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/add-two-promises/](https://leetcode.com/problems/add-two-promises/)  
**Topics:** 

---

## 📝 Problem Statement

Given two promises `promise1` and `promise2`, return a new promise. `promise1` and `promise2` will both resolve with a number. The returned promise should resolve with the sum of the two numbers.
 
Example 1:

```

**Input:** 
promise1 = new Promise(resolve => setTimeout(() => resolve(2), 20)), 
promise2 = new Promise(resolve => setTimeout(() => resolve(5), 60))
**Output:** 7
**Explanation:** The two input promises resolve with the values of 2 and 5 respectively. The returned promise should resolve with a value of 2 + 5 = 7. The time the returned promise resolves is not judged for this problem.

```

Example 2:

```

**Input:** 
promise1 = new Promise(resolve => setTimeout(() => resolve(10), 50)), 
promise2 = new Promise(resolve => setTimeout(() => resolve(-12), 30))
**Output:** -2
**Explanation:** The two input promises resolve with the values of 10 and -12 respectively. The returned promise should resolve with a value of 10 + -12 = -2.

```

 
**Constraints:**

	- `promise1` and `promise2` are promises that resolve with a number

---

## 💻 Implementation (python3)

```js
/**
 * @param {Promise<number>} promise1
 * @param {Promise<number>} promise2
 * @return {Promise<number>}
 */
var addTwoPromises = async function(promise1, promise2) {
    // Use 'await' to pause the execution of this async function until promise1 resolves.
    // The resolved value of promise1 (a number) will be assigned to num1.
    // Note: promise1 and promise2 start executing concurrently as soon as they are created/passed.
    // 'await' merely waits for their results without blocking other asynchronous operations.
    const num1 = await promise1;

    // Similarly, await the resolution of promise2.
    // The resolved value of promise2 (a number) will be assigned to num2.
    const num2 = await promise2;

    // Once both numbers are available, calculate their sum.
    // An async function implicitly returns a Promise that resolves with the value returned by the function.
    // So, this function will return a Promise that resolves with num1 + num2.
    return num1 + num2;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to take two promises, `promise1` and `promise2`, both of which resolve with a number, and return a new promise that resolves with the sum of those two numbers.

The core challenge here is to *wait* for both promises to complete their asynchronous operations and yield their respective numbers before we can perform the addition. JavaScript provides several ways to handle asynchronous operations and wait for promises:

1.  **`Promise.all()`**: This method takes an array of promises and returns a single promise. This returned promise resolves when all of the input promises have resolved, with an array of their resolved values. If any of the input promises reject, `Promise.all()` immediately rejects with the reason of the first promise that rejected.
2.  **`async/await` syntax**: This modern JavaScript syntax allows us to write asynchronous code that looks and behaves more like synchronous code. An `async` function always returns a promise. Inside an `async` function, the `await` keyword can be used before a promise to pause the execution of the `async` function until that promise settles (resolves or rejects).

Given the starter code snippet `var addTwoPromises = async function(promise1, promise2) { ... };`, the `async/await` approach is the most natural and idiomatic choice.

Our intuition is to:
1.  Declare the function as `async` to enable the use of `await`.
2.  Use `await promise1` to get the first number. This will pause the `async` function's execution until `promise1` resolves.
3.  Use `await promise2` to get the second number. This will pause the `async` function's execution until `promise2` resolves.
4.  Once both numbers are obtained, simply add them together.
5.  The `async` function will automatically wrap the returned sum in a new promise that resolves with that sum.

It's important to understand that `await promise1; await promise2;` does not mean `promise2` waits for `promise1` to *start* resolving. Both `promise1` and `promise2` begin their asynchronous tasks concurrently as soon as they are created or passed into the function. The `await` keyword merely ensures that the *current `async` function's execution* pauses until the respective promise has *finished* resolving and its value is available. This ensures optimal performance by not unnecessarily sequentializing independent asynchronous operations.

## Step-by-Step Approach

1.  **Define an `async` function**: The problem provides the starter signature `var addTwoPromises = async function(promise1, promise2) { ... };`. This is crucial as it allows us to use `await`.
2.  **Await `promise1`**: Inside the `async` function, use `const num1 = await promise1;`. This line will wait for `promise1` to resolve. Once it resolves, its numerical value will be stored in the `num1` variable.
3.  **Await `promise2`**: Similarly, use `const num2 = await promise2;`. This line will wait for `promise2` to resolve. Its numerical value will be stored in the `num2` variable.
4.  **Calculate and return the sum**: After both `num1` and `num2` have been successfully retrieved, calculate their sum: `num1 + num2`.
5.  **Implicit Promise Return**: Since `addTwoPromises` is an `async` function, whatever value it returns (in this case, `num1 + num2`) will automatically be wrapped in a new promise that resolves with that value. This new promise is the one returned by `addTwoPromises`.

## Complexity Analysis

*   **Time Complexity**: `O(max(t1, t2))`
    *   `t1` is the time it takes for `promise1` to resolve.
    *   `t2` is the time it takes for `promise2` to resolve.
    *   Since `promise1` and `promise2` execute concurrently (in parallel), the total time taken for `addTwoPromises` to resolve will be determined by the promise that takes longer to complete. We must wait for both to finish before we can sum their values. This is the most optimal time complexity achievable for this problem.

*   **Space Complexity**: `O(1)`
    *   We are only storing a few variables (`num1`, `num2`, and their sum) in memory, regardless of the values resolved by the promises. This constitutes constant extra space.

## Common Pitfalls / Mistakes

1.  **Not using `await` or `Promise.all()`**: A common beginner mistake is to try to add the promises directly, e.g., `return promise1 + promise2;`. This would result in string concatenation like `"[object Promise][object Promise]"` or `NaN` if JavaScript tries to coerce them to numbers, which is not the desired behavior. Promises are objects, not their resolved values.
2.  **Misunderstanding `async/await` concurrency**: Some might incorrectly assume that `const num1 = await promise1; const num2 = await promise2;` executes `promise2` *after* `promise1` has fully resolved. While the `await` statements pause the *function's execution* sequentially, the underlying promises themselves (`promise1` and `promise2`) are typically initiated and run in parallel. The `await` simply ensures we have the result before proceeding. For this problem, this behavior is correct and optimal.
3.  **Error Handling (not applicable here, but good to know)**: The problem statement guarantees that promises will resolve with a number. In a real-world scenario, if promises could reject, one would need to wrap the `await` calls in a `try...catch` block or use `.catch()` with `Promise.all()` to handle potential errors gracefully.

## Real Interview Follow-Up Questions and Answers

### 1. What if there were `N` promises instead of 2? How would you adapt your solution?

**Answer:**
If there were `N` promises, `Promise.all()` would be the most elegant and efficient solution.

```javascript
async function addNPromises(promises) {
    // Promise.all takes an array of promises and returns a single promise
    // that resolves with an array of their resolved values.
    const values = await Promise.all(promises);
    // Sum all the resolved values.
    return values.reduce((sum, current) => sum + current, 0);
}
```

**Explanation:**
`Promise.all(promises)` would wait for all `N` promises to resolve concurrently. Once they all resolve, it returns an array of their values. We can then use `reduce` to sum these values. The time complexity would be `O(max(t_i))` where `t_i` is the resolution time of the i-th promise, and space complexity would be `O(N)` to store the resolved values in the `values` array.

### 2. What if one of the promises rejects? How would your current solution behave, and how would you handle it if you needed to return a default value or re-throw a specific error?

**Answer:**
My current `async/await` solution would cause the `addTwoPromises` function (which implicitly returns a promise) to *reject* with the same reason as the first promise that rejects.

To handle rejections:

**Option A: Catch and return a default value:**

```javascript
async function addTwoPromisesWithDefault(promise1, promise2) {
    let num1, num2;
    try {
        num1 = await promise1;
    } catch (error) {
        console.error("Promise 1 rejected:", error);
        num1 = 0; // Default value if promise1 rejects
    }
    try {
        num2 = await promise2;
    } catch (error) {
        console.error("Promise 2 rejected:", error);
        num2 = 0; // Default value if promise2 rejects
    }
    return num1 + num2;
}
```
**Explanation:** This approach uses separate `try...catch` blocks for each `await`. If a promise rejects, we log the error and assign a default value (e.g., 0) to its corresponding number, allowing the sum to proceed.

**Option B: Catch and re-throw a custom error:**

```javascript
async function addTwoPromisesWithCustomError(promise1, promise2) {
    try {
        const num1 = await promise1;
        const num2 = await promise2;
        return num1 + num2;
    } catch (error) {
        console.error("One of the promises rejected:", error);
        // Re-throw a custom error or the original error
        throw new Error("Failed to add promises: " + error.message);
    }
}
```
**Explanation:** This approach uses a single `try...catch` block around both `await` calls. If *any* promise rejects, the `catch` block is executed. We can then log the error and re-throw a more specific or custom error, allowing the caller to handle the rejection.

If using `Promise.all()`:

```javascript
async function addTwoPromisesWithPromiseAllAndCatch(promise1, promise2) {
    try {
        const values = await Promise.all([promise1, promise2]);
        return values[0] + values[1];
    } catch (error) {
        console.error("One of the promises rejected:", error);
        throw new Error("Failed to sum promises: " + error.message);
    }
}
```
**Explanation:** `Promise.all()` itself will reject if any of its input promises reject. A single `try...catch` around `await Promise.all(...)` is sufficient to catch any rejection from the input promises.

### 3. What if the problem required you to return the sum *as soon as possible*, even if one promise takes significantly longer than the other, and you only needed the result from the *first* promise to resolve? (This is a trick question to test understanding of `Promise.race` vs `Promise.all`).

**Answer:**
This scenario would not be about summing two numbers, as summing requires both values. However, if the requirement was to get *any* value from the *first* promise that resolves (e.g., if we had multiple sources for a number and just needed the quickest one), we would use `Promise.race()`.

```javascript
async function getFirstResolvedValue(promise1, promise2) {
    // Promise.race returns a promise that resolves or rejects
    // as soon as one of the input promises resolves or rejects.
    return await Promise.race([promise1, promise2]);
}
```
**Explanation:** `Promise.race()` is designed for scenarios where you only care about the outcome of the first promise to settle. It's not suitable for summing two values, as it would only give you one of them. This question highlights the distinction between `Promise.all()` (wait for all) and `Promise.race()` (wait for any).

### 4. How would you handle a scenario where you need to add two promises, but one of them might resolve with a non-numeric value?

**Answer:**
The problem statement explicitly says "promise1 and promise2 will both resolve with a number." If this constraint were relaxed, we would need to add validation.

```javascript
async function addTwoPromisesWithValidation(promise1, promise2) {
    const num1 = await promise1;
    const num2 = await promise2;

    if (typeof num1 !== 'number' || isNaN(num1)) {
        throw new TypeError(`Promise 1 resolved with a non-numeric value: ${num1}`);
    }
    if (typeof num2 !== 'number' || isNaN(num2)) {
        throw new TypeError(`Promise 2 resolved with a non-numeric value: ${num2}`);
    }

    return num1 + num2;
}
```
**Explanation:** After `await`ing both promises, we would perform type checking using `typeof` and `isNaN` to ensure the resolved values are indeed valid numbers. If not, we would throw a `TypeError` to indicate the invalid input, preventing incorrect arithmetic operations. This ensures robustness in less constrained environments.
