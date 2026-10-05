# 2715. Timeout Cancellation

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/timeout-cancellation/](https://leetcode.com/problems/timeout-cancellation/)  
**Topics:** 

---

## 📝 Problem Statement

Given a function `fn`, an array of arguments `args`, and a timeout `t` in milliseconds, return a cancel function `cancelFn`.

After a delay of `cancelTimeMs`, the returned cancel function `cancelFn` will be invoked.

```

setTimeout(cancelFn, cancelTimeMs)

```

Initially, the execution of the function `fn` should be delayed by `t` milliseconds.

If, before the delay of `t` milliseconds, the function `cancelFn` is invoked, it should cancel the delayed execution of `fn`. Otherwise, if `cancelFn` is not invoked within the specified delay `t`, `fn` should be executed with the provided `args` as arguments.

 
Example 1:

```

**Input:** fn = (x) => x * 5, args = [2], t = 20
**Output:** [{"time": 20, "returned": 10}]
**Explanation:** 
const cancelTimeMs = 50;
const cancelFn = cancellable((x) => x * 5, [2], 20);
setTimeout(cancelFn, cancelTimeMs);

The cancellation was scheduled to occur after a delay of cancelTimeMs (50ms), which happened after the execution of fn(2) at 20ms.

```

Example 2:

```

**Input:** fn = (x) => x**2, args = [2], t = 100
**Output:** []
**Explanation:** 
const cancelTimeMs = 50;
const cancelFn = cancellable((x) => x**2, [2], 100);
setTimeout(cancelFn, cancelTimeMs);

The cancellation was scheduled to occur after a delay of cancelTimeMs (50ms), which happened before the execution of fn(2) at 100ms, resulting in fn(2) never being called.

```

Example 3:

```

**Input:** fn = (x1, x2) => x1 * x2, args = [2,4], t = 30
**Output:** [{"time": 30, "returned": 8}]
Explanation: 
const cancelTimeMs = 100;
const cancelFn = cancellable((x1, x2) => x1 * x2, [2,4], 30);
setTimeout(cancelFn, cancelTimeMs);

The cancellation was scheduled to occur after a delay of cancelTimeMs (100ms), which happened after the execution of fn(2,4) at 30ms.

```

 
**Constraints:**

	- `fn` is a function

	- `args` is a valid JSON array

	- `1 20 `

	- `10 `

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
    // Schedule fn to be executed after `t` milliseconds with the given args
    const timerId = setTimeout(() => {
        fn(...args);
    }, t);

    // Return a cancellation function that clears the scheduled timeout
    return function cancelFn() {
        clearTimeout(timerId);
    };
};
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to defer the execution of a function `fn` by `t` milliseconds while providing a mechanism to abort this execution before it occurs.

In JavaScript's concurrency and asynchronous model (the Event Loop), scheduling delayed tasks is natively handled by the Web API / Node.js global method `setTimeout`. `setTimeout` returns an identifier (`timerId`) representing the scheduled task in the host environment's timer table. To prevent the callback from executing, the environment provides `clearTimeout(timerId)`.

By leveraging a closure, the returned cancellation function captures the `timerId` and clears the timer when invoked.

### Step-by-Step Approach

1. Call `setTimeout` with a callback that invokes `fn(...args)` (using the spread operator to unpack the argument array) and delay `t`.
2. Store the returned identifier in a constant `timerId`.
3. Return a closure (`cancelFn`) that executes `clearTimeout(timerId)`.
4. If `cancelFn` is called prior to `t` milliseconds elapsed, the timer is cleared from the event queue and `fn` is never executed. If `t` milliseconds elapse before `cancelFn` is called, `fn` executes as scheduled, and any subsequent call to `clearTimeout` is safely a no-op.

### Complexity Analysis

- **Time Complexity:**
  - `cancellable(...)`: $\mathcal{O}(1)$ to set the timer and return the cancellation closure.
  - `fn(...args)` execution: $\mathcal{O}(K)$ where $K$ is the number of arguments (due to spreading), plus the time complexity of `fn` itself.
  - `cancelFn()`: $\mathcal{O}(1)$ as `clearTimeout` is an $\mathcal{O}(1)$ lookup/deregistration operation.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The closure retains references to `timerId`, `fn`, and `args`, consuming constant additional heap memory.

### Common Pitfalls / Mistakes

1. **Forgetting to Spread Arguments:** Writing `fn(args)` instead of `fn(...args)` passes the array as a single parameter rather than spreading individual arguments into `fn`.
2. **Context Binding (`this`):** If `fn` relies on a specific execution context (`this`), calling `fn(...args)` might lose the context. While not strictly tested in this specific LeetCode problem, in production utilities it is safer to use `fn.apply(this, args)`.
3. **Memory Leaks in Long-Lived Applications:** Leaving references inside closures indefinitely if timers are long-lived and never cleared.

### Real Interview Follow-Up Questions

1. **How would you implement this using modern Web APIs like `AbortController`?**
   * *Answer:* An `AbortController` standardizes cancellation in modern JavaScript (used extensively in `fetch`). We can accept an `AbortSignal` or create an internal controller:
     ```javascript
     const controller = new AbortController();
     const { signal } = controller;
     const timer = setTimeout(() => fn(...args), t);
     signal.addEventListener('abort', () => clearTimeout(timer), { once: true });
     return () => controller.abort();
     ```

2. **What happens if `cancelFn` is called multiple times?**
   * *Answer:* `clearTimeout` handles redundant calls gracefully (it silently does nothing if the timer has already been cleared or has already fired). The operation is idempotent.

3. **How does JavaScript handle timer drift and concurrency under heavy CPU load?**
   * *Answer:* JavaScript is single-threaded. `setTimeout` does not guarantee execution *at* exactly `t` milliseconds; it guarantees execution *no earlier than* `t` milliseconds. If the call stack / microtask queue is saturated with synchronous or Promise-based work, the callback will be queued until the event loop turns, causing timer drift. For high-precision requirements, compensation techniques (e.g., measuring `performance.now()` delta or Web Workers) must be employed.
