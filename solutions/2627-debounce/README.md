# 2627. Debounce

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/debounce/](https://leetcode.com/problems/debounce/)  
**Topics:** 

---

## 📝 Problem Statement

Given a function `fn` and a time in milliseconds `t`, return a **debounced** version of that function.

A **debounced** function is a function whose execution is delayed by `t` milliseconds and whose execution is cancelled if it is called again within that window of time. The debounced function should also receive the passed parameters.

For example, let's say `t = 50ms`, and the function was called at `30ms`, `60ms`, and `100ms`.

The first 2 function calls would be cancelled, and the 3rd function call would be executed at `150ms`.

If instead `t = 35ms`, The 1st call would be cancelled, the 2nd would be executed at `95ms`, and the 3rd would be executed at `135ms`.

The above diagram shows how debounce will transform events. Each rectangle represents 100ms and the debounce time is 400ms. Each color represents a different set of inputs.

Please solve it without using lodash's `_.debounce()` function.

 
Example 1:

```

**Input:** 
t = 50
calls = [
  {"t": 50, inputs: [1]},
  {"t": 75, inputs: [2]}
]
**Output:** [{"t": 125, inputs: [2]}]
**Explanation:**
let start = Date.now();
function log(...inputs) { 
  console.log([Date.now() - start, inputs ])
}
const dlog = debounce(log, 50);
setTimeout(() => dlog(1), 50);
setTimeout(() => dlog(2), 75);

The 1st call is cancelled by the 2nd call because the 2nd call occurred before 100ms
The 2nd call is delayed by 50ms and executed at 125ms. The inputs were (2).

```

Example 2:

```

**Input:** 
t = 20
calls = [
  {"t": 50, inputs: [1]},
  {"t": 100, inputs: [2]}
]
**Output:** [{"t": 70, inputs: [1]}, {"t": 120, inputs: [2]}]
**Explanation:**
The 1st call is delayed until 70ms. The inputs were (1).
The 2nd call is delayed until 120ms. The inputs were (2).

```

Example 3:

```

**Input:** 
t = 150
calls = [
  {"t": 50, inputs: [1, 2]},
  {"t": 300, inputs: [3, 4]},
  {"t": 300, inputs: [5, 6]}
]
**Output:** [{"t": 200, inputs: [1,2]}, {"t": 450, inputs: [5, 6]}]
**Explanation:**
The 1st call is delayed by 150ms and ran at 200ms. The inputs were (1, 2).
The 2nd call is cancelled by the 3rd call
The 3rd call is delayed by 150ms and ran at 450ms. The inputs were (5, 6).

```

 
**Constraints:**

	- `0

---

## 💻 Implementation (python3)

```js
/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    // timerId will store the ID returned by setTimeout.
    // It needs to be declared outside the returned function to persist across calls
    // and be accessible for clearTimeout due to closure.
    let timerId;

    // Return the debounced function. This is the function that users will call.
    return function(...args) {
        // Capture the 'this' context of the current call.
        // This ensures that when 'fn' is eventually executed, it has the correct 'this' binding.
        const context = this;

        // Clear any existing timer.
        // If the debounced function is called again before 't' milliseconds have passed,
        // the previously scheduled execution of 'fn' is cancelled.
        clearTimeout(timerId);

        // Schedule a new execution of 'fn' after 't' milliseconds.
        // The 'fn' will be called with the captured 'this' context and arguments.
        timerId = setTimeout(() => {
            // Use apply to pass the captured 'this' context and arguments array to 'fn'.
            fn.apply(context, args);
        }, t);
    };
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The core idea behind a `debounce` function is to delay the execution of a function until a certain amount of time (`t`) has passed without it being called again. If the function is called multiple times within this `t` millisecond window, only the *last* call should trigger the actual execution of the original function `fn`. All previous calls within that window are effectively cancelled.

To achieve this, we need a mechanism to:
1.  **Schedule execution:** When the debounced function is called, we want to schedule `fn` to run after `t` milliseconds. JavaScript's `setTimeout` is perfect for this.
2.  **Cancel previous execution:** If the debounced function is called again *before* the scheduled `fn` has run, we must cancel the pending execution and schedule a *new* one based on the latest call. JavaScript's `clearTimeout` allows us to cancel a `setTimeout` using its returned ID.
3.  **Maintain state:** The `timerId` (returned by `setTimeout`) needs to be accessible across multiple calls to the debounced function so that `clearTimeout` can reference the correct pending timer. This implies using a closure.
4.  **Pass arguments and context:** The original function `fn` should receive the arguments passed to the debounced function, and its `this` context should be preserved.

## Step-by-Step Approach

1.  **Define the `debounce` factory function:** It takes `fn` (the function to debounce) and `t` (the delay in milliseconds) as arguments.
    ```javascript
    var debounce = function(fn, t) { ... };
    ```
2.  **Declare `timerId` in the outer scope:** Inside `debounce` but outside the returned function, declare a variable `timerId`. This variable will hold the ID returned by `setTimeout` and will be part of the closure, allowing it to persist and be updated across multiple calls to the debounced function. Initialize it to `null` or `undefined`.
    ```javascript
    let timerId;
    ```
3.  **Return an inner function:** This inner function is the actual debounced function that will be called by the user. It needs to accept arbitrary arguments (`...args`).
    ```javascript
    return function(...args) { ... };
    ```
4.  **Capture `this` context:** Inside the returned function, capture the `this` context of the current call. This is important if `fn` relies on `this`.
    ```javascript
    const context = this;
    ```
5.  **Clear any existing timer:** Before scheduling a new execution, call `clearTimeout(timerId)`. If `timerId` holds a valid ID of a pending `setTimeout`, that pending execution will be cancelled. If `timerId` is `null` or refers to an already completed timer, `clearTimeout` does nothing, which is fine.
    ```javascript
    clearTimeout(timerId);
    ```
6.  **Schedule a new `setTimeout`:** Set a new timer using `setTimeout`. The callback for this timer will execute `fn`.
    ```javascript
    timerId = setTimeout(() => {
        // ... execute fn ...
    }, t);
    ```
7.  **Execute `fn` with correct context and arguments:** Inside the `setTimeout` callback, call `fn` using `apply` (or `call`) to ensure it receives the correct `this` context and arguments.
    ```javascript
    fn.apply(context, args);
    ```

This sequence ensures that every time the debounced function is called, any previous pending execution is cancelled, and a new one is scheduled. Only if `t` milliseconds pass without another call will the `fn` finally execute.

## Complexity Analysis

*   **Time Complexity:** O(1) for each call to the debounced function.
    *   Each call involves a `clearTimeout` operation and a `setTimeout` operation. Both of these are typically constant time operations in JavaScript runtime environments. The actual execution of `fn` happens asynchronously and is not part of the synchronous complexity of calling the debounced function itself.
*   **Space Complexity:** O(1) for each debounced function instance.
    *   The `debounce` function creates a closure that stores a single `timerId` variable. This variable holds a primitive value (the timer ID). Regardless of the number of times the debounced function is called or the size of `fn`'s arguments, the additional memory used by the `debounce` wrapper remains constant.

## Common Pitfalls / Mistakes

1.  **Forgetting `clearTimeout`:** The most common mistake. Without `clearTimeout(timerId)`, every call to the debounced function would schedule a new execution of `fn`, leading to `fn` being called multiple times, which defeats the purpose of debouncing.
2.  **Incorrect `timerId` scope:** Declaring `timerId` inside the returned function (e.g., `return function(...args) { let timerId; ... }`) would mean each call creates its own `timerId`. `clearTimeout` would then only cancel the timer set by the *current* call, not previous ones, again breaking the debounce logic. `timerId` *must* be in the closure scope of the returned function.
3.  **Not preserving `this` context:** If `fn` relies on `this` (e.g., `this.value`), simply calling `setTimeout(() => fn(args), t)` would cause `fn` to be called with `this` bound to the global object (or `undefined` in strict mode), leading to incorrect behavior. Using `fn.apply(context, args)` correctly preserves the `this` context from the call to the debounced function.
4.  **Incorrect argument passing:** Forgetting to pass `...args` from the debounced function to `fn` (or passing them incorrectly) would result in `fn` not receiving the expected inputs.

## Real Interview Follow-Up Questions

1.  **What if `fn` needs to return a value?**
    *   **Answer:** A standard `debounce` implementation, as shown, returns `undefined` immediately when the debounced function is called. This is because the actual execution of `fn` is asynchronous and delayed. If `fn`'s return value is critical, a simple `debounce` might not be the right pattern. Alternative approaches could involve:
        *   **Promises:** The debounced function could return a Promise that resolves with `fn`'s result when it finally executes. However, this adds complexity, especially with cancellation.
        *   **Callbacks:** `fn` could be designed to accept a callback function that receives its result.
        *   **Event Emitters:** `fn` could emit an event with its result.
    *   For most UI-related debounce use cases (e.g., search input, window resize), the return value of the debounced function itself is not typically consumed by the caller.

2.  **How would you implement `debounce` with an `immediate` option (leading edge)?**
    *   **Answer:** A "leading edge" debounce executes `fn` immediately on the *first* call within a `t`-millisecond window. Subsequent calls within that window are ignored. After `t` milliseconds pass without any calls, the next call will again trigger immediate execution.
    *   **Implementation Idea:**
        ```javascript
        var debounce = function(fn, t, immediate = false) {
            let timerId;
            let lastArgs;
            let lastContext;

            return function(...args) {
                lastArgs = args; // Store latest args
                lastContext = this; // Store latest context

                const callNow = immediate && !timerId; // If immediate and no timer is active

                clearTimeout(timerId); // Always clear previous timer

                timerId = setTimeout(() => {
                    timerId = null; // Reset timerId after 't' ms to allow next call to be immediate (if immediate=true)
                    if (!immediate) { // If not immediate, execute on trailing edge
                        fn.apply(lastContext, lastArgs);
                    }
                }, t);

                if (callNow) { // If immediate, execute now
                    fn.apply(lastContext, lastArgs);
                }
            };
        };
        ```
    *   This version requires more state (`lastArgs`, `lastContext`) and careful logic to determine when to call `fn` immediately versus on the trailing edge.

3.  **What's the difference between `debounce` and `throttle`?**
    *   **Answer:**
        *   **Debounce:** Delays function execution until a certain period of inactivity has passed. It's like saying, "Don't do anything until the user *stops* doing X for `t` milliseconds." Useful for search input (search only after typing stops), window resize (recalculate layout only after resizing stops).
        *   **Throttle:** Limits the rate at which a function can be called. It's like saying, "Do X at most once every `t` milliseconds." Useful for scroll events (update UI periodically while scrolling), mouse move (track position periodically).
    *   **Analogy:** Imagine a rapidly closing elevator door.
        *   **Debounce:** If someone presses the "door close" button, the door waits `t` seconds. If someone presses it again within `t` seconds, the timer resets. The door only closes after `t` seconds of *no button presses*.
        *   **Throttle:** If someone presses the "door close" button, the door closes. For the next `t` seconds, any button presses are ignored. After `t` seconds, if the button is pressed again, the door closes again.

4.  **How would you handle multiple debounced functions if they all share the same `timerId` variable?**
    *   **Answer:** This is not an issue with the provided implementation. Each time the `debounce` *factory function* is called, it creates a *new closure* with its own independent `timerId` variable.
    *   For example:
        ```javascript
        const debouncedLog1 = debounce(console.log, 100);
        const debouncedLog2 = debounce(alert, 200);
        ```
        `debouncedLog1` and `debouncedLog2` will each have their own `timerId` in their respective closures, so they will not interfere with each other.

5.  **Are there any performance concerns if `t` is very large (e.g., 10 seconds) and the debounced function is called very frequently?**
    *   **Answer:** The `debounce` wrapper itself is very efficient (O(1) per call). The primary concern isn't the performance of `debounce` but rather the user experience. If `t` is very large and the user frequently interacts (e.g., types in a search box every few milliseconds), the actual `fn` might never execute, as the timer keeps getting reset. This could lead to a frustrating user experience where their action never seems to complete. From a system resource perspective, `setTimeout` and `clearTimeout` are lightweight operations, so even frequent calls for a large `t` are generally not a significant performance bottleneck for the browser/Node.js event loop, unless the number of *distinct* active timers becomes excessively high (which is not the case here, as we only have one `timerId` per debounced function instance).
