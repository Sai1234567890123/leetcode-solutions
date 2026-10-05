# 2725. Interval Cancellation

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/interval-cancellation/](https://leetcode.com/problems/interval-cancellation/)  
**Topics:** 

---

## 📝 Problem Statement

Given a function `fn`, an array of arguments `args`, and an interval time `t`, return a cancel function `cancelFn`.

After a delay of `cancelTimeMs`, the returned cancel function `cancelFn` will be invoked.

```

setTimeout(cancelFn, cancelTimeMs)

```

The function `fn` should be called with `args` immediately and then called again every `t` milliseconds until `cancelFn` is called at `cancelTimeMs` ms.

 
Example 1:

```

**Input:** fn = (x) => x * 2, args = [4], t = 35
**Output:** 
[
   {"time": 0, "returned": 8},
   {"time": 35, "returned": 8},
   {"time": 70, "returned": 8},
   {"time": 105, "returned": 8},
   {"time": 140, "returned": 8},
   {"time": 175, "returned": 8}
]
**Explanation:** 
const cancelTimeMs = 190;
const cancelFn = cancellable((x) => x * 2, [4], 35);
setTimeout(cancelFn, cancelTimeMs);

Every 35ms, fn(4) is called. Until t=190ms, then it is cancelled.
1st fn call is at 0ms. fn(4) returns 8.
2nd fn call is at 35ms. fn(4) returns 8.
3rd fn call is at 70ms. fn(4) returns 8.
4th fn call is at 105ms. fn(4) returns 8.
5th fn call is at 140ms. fn(4) returns 8.
6th fn call is at 175ms. fn(4) returns 8.
Cancelled at 190ms

```

Example 2:

```

**Input:** fn = (x1, x2) => (x1 * x2), args = [2, 5], t = 30
**Output:** 
[
   {"time": 0, "returned": 10},
   {"time": 30, "returned": 10},
   {"time": 60, "returned": 10},
   {"time": 90, "returned": 10},
   {"time": 120, "returned": 10},
   {"time": 150, "returned": 10}
]
**Explanation:** 
const cancelTimeMs = 165; 
const cancelFn = cancellable((x1, x2) => (x1 * x2), [2, 5], 30) 
setTimeout(cancelFn, cancelTimeMs)

Every 30ms, fn(2, 5) is called. Until t=165ms, then it is cancelled.
1st fn call is at 0ms 
2nd fn call is at 30ms 
3rd fn call is at 60ms 
4th fn call is at 90ms 
5th fn call is at 120ms 
6th fn call is at 150ms
Cancelled at 165ms

```

Example 3:

```

**Input:** fn = (x1, x2, x3) => (x1 + x2 + x3), args = [5, 1, 3], t = 50
**Output:** 
[
   {"time": 0, "returned": 9},
   {"time": 50, "returned": 9},
   {"time": 100, "returned": 9},
   {"time": 150, "returned": 9}
]
**Explanation:** 
const cancelTimeMs = 180;
const cancelFn = cancellable((x1, x2, x3) => (x1 + x2 + x3), [5, 1, 3], 50)
setTimeout(cancelFn, cancelTimeMs)

Every 50ms, fn(5, 1, 3) is called. Until t=180ms, then it is cancelled. 
1st fn call is at 0ms
2nd fn call is at 50ms
3rd fn call is at 100ms
4th fn call is at 150ms
Cancelled at 180ms

```

 
**Constraints:**

	- `fn` is a function

	- `args` is a valid JSON array

	- `1 30 `

	- `10 cancelTimeMs `

---

## 💻 Implementation (python3)

```js
/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Invoke the function immediately with provided arguments at t = 0ms
    fn(...args);

    // Schedule subsequent invocations every t milliseconds
    const timerId = setInterval(() => {
        fn(...args);
    }, t);

    // Return the cancellation function to clear the scheduled interval
    return function cancelFn() {
        clearInterval(timerId);
    };
};
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires executing a function `fn` immediately at time $0$, followed by repetitive invocations every $t$ milliseconds. Crucially, we must return a cancellation function that halts all subsequent scheduled executions when called.

In JavaScript's asynchronous concurrency model (the Event Loop):
1. **Immediate Execution**: Calling `fn(...args)` synchronously at the start of `cancellable` guarantees execution at $t = 0$.
2. **Periodic Execution**: `setInterval(callback, t)` schedules recurring calls on the host environment's timer queue.
3. **Cancellation via Closure**: `setInterval` returns an identifier (`timerId`). By creating a closure, the returned `cancelFn` retains access to `timerId` and calls `clearInterval(timerId)` to tear down the timer.

---

### Step-by-Step Approach

1. **Immediate Call**: Call `fn(...args)` directly so the first invocation happens without any delay.
2. **Set Interval**: Store the timer reference returned by `setInterval(() => fn(...args), t)`.
3. **Return Canceler**: Return an anonymous function (or arrow function) that invokes `clearInterval(timerId)`.

---

### Complexity Analysis

- **Time Complexity:** 
  - **Setup (`cancellable`)**: $O(1)$ (plus the execution time of the initial `fn(...args)` call).
  - **Interval Execution**: $O(1)$ overhead per tick (plus the execution time of `fn(...args)`).
  - **Cancellation (`cancelFn`)**: $O(1)$ to invoke `clearInterval`.
- **Space Complexity:** $O(1)$ auxiliary space. The closure retains references to `timerId` and `args`, using a constant amount of memory.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Forgetting the Immediate Call**: Standard `setInterval` only executes after the first interval of $t$ ms has elapsed. Forgetting to invoke `fn(...args)` synchronously at $t = 0$ will cause the initial output at $0$ ms to be missed.
2. **Timer Drift with `setInterval`**: In real-world JavaScript runtimes, `setInterval` callbacks can drift or stack if `fn` is a heavy synchronous task or an asynchronous operation that takes longer than $t$ to complete.
3. **Argument Forwarding**: Passing `args` directly as a single array argument instead of spreading them (`fn(...args)` or `fn.apply(null, args)`).

---

### Real Interview Follow-Up Questions

#### 1. What if `fn` is an asynchronous function (`async/await`) and its execution time exceeds $t$?
*Interview Answer:* If `fn` returns a Promise and takes longer than $t$ ms, `setInterval` will still trigger every $t$ ms, leading to overlapping executions and potential race conditions. To ensure sequential, non-overlapping executions, use a recursive `setTimeout` pattern:
```javascript
let timerId = null;
let isCancelled = false;

const run = async () => {
    if (isCancelled) return;
    await fn(...args);
    if (!isCancelled) {
        timerId = setTimeout(run, t);
    }
};

run();
return () => {
    isCancelled = true;
    clearTimeout(timerId);
};
```

#### 2. How does JavaScript handle timer throttling in background tabs?
*Interview Answer:* Browsers throttle background tabs to run timers at most once per second ($1000$ ms) or longer to conserve CPU and battery. If sub-second precision is required in a web application even when tabbed out, offload the timing logic to a **Web Worker**, which runs in a separate thread and is not subject to DOM tab throttling.

#### 3. How would you support passing an `AbortSignal` instead of returning a custom cancel function?
*Interview Answer:* Modern web APIs (like `fetch` and Event Listeners) use the standard `AbortController` / `AbortSignal` pattern. We can accept an `AbortSignal`:
```javascript
function cancellableWithSignal(fn, args, t, signal) {
    if (signal?.aborted) return;
    fn(...args);
    const timerId = setInterval(() => fn(...args), t);
    signal?.addEventListener('abort', () => clearInterval(timerId), { once: true });
}
```
