# 2637. Promise Time Limit

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/promise-time-limit/](https://leetcode.com/problems/promise-time-limit/)  
**Topics:** 

---

## 📝 Problem Statement

Given an asynchronous function `fn` and a time `t` in milliseconds, return a new **time limited** version of the input function. `fn` takes arguments provided to the **time limited **function.

The **time limited** function should follow these rules:

	- If the `fn` completes within the time limit of `t` milliseconds, the **time limited** function should resolve with the result.

	- If the execution of the `fn` exceeds the time limit, the **time limited** function should reject with the string `"Time Limit Exceeded"`.

 
Example 1:

```

**Input:** 
fn = async (n) => { 
  await new Promise(res => setTimeout(res, 100)); 
  return n * n; 
}
inputs = [5]
t = 50
**Output:** {"rejected":"Time Limit Exceeded","time":50}
**Explanation:**
const limited = timeLimit(fn, t)
const start = performance.now()
let result;
try {
   const res = await limited(...inputs)
   result = {"resolved": res, "time": Math.floor(performance.now() - start)};
} catch (err) {
   result = {"rejected": err, "time": Math.floor(performance.now() - start)};
}
console.log(result) // Output

The provided function is set to resolve after 100ms. However, the time limit is set to 50ms. It rejects at t=50ms because the time limit was reached.

```

Example 2:

```

**Input:** 
fn = async (n) => { 
  await new Promise(res => setTimeout(res, 100)); 
  return n * n; 
}
inputs = [5]
t = 150
**Output:** {"resolved":25,"time":100}
**Explanation:**
The function resolved 5 * 5 = 25 at t=100ms. The time limit is never reached.

```

Example 3:

```

**Input:** 
fn = async (a, b) => { 
  await new Promise(res => setTimeout(res, 120)); 
  return a + b; 
}
inputs = [5,10]
t = 150
**Output:** {"resolved":15,"time":120}
**Explanation:**
​​​​The function resolved 5 + 10 = 15 at t=120ms. The time limit is never reached.

```

Example 4:

```

**Input:** 
fn = async () => { 
  throw "Error";
}
inputs = []
t = 1000
**Output:** {"rejected":"Error","time":0}
**Explanation:**
The function immediately throws an error.
```

 
**Constraints:**

	- `0

---

## 💻 Implementation (python3)

```js
/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        let timerId;
        
        // Create a promise that rejects after `t` milliseconds
        const timeoutPromise = new Promise((_, reject) => {
            timerId = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);
        });

        try {
            // Race the original async function against the timeout promise
            return await Promise.race([fn(...args), timeoutPromise]);
        } finally {
            // Clean up the timer to prevent memory leaks and pending operations
            clearTimeout(timerId);
        }
    };
};
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The objective is to enforce an upper bound of `t` milliseconds on the execution of an asynchronous function `fn`. 

In JavaScript, managing concurrent asynchronous operations where only the first completion matters is the exact use-case for `Promise.race`. We can race two promises against each other:
1. The execution of `fn(...args)`.
2. A synthetic promise that rejects with `"Time Limit Exceeded"` after a `setTimeout` of `t` milliseconds.

Whichever promise settles first (resolves or rejects) determines the outcome of the wrapped function call.

A critical production-grade consideration often overlooked in simple competitive programming solutions is **timer cleanup**. If `fn` completes well before `t` milliseconds, the scheduled `setTimeout` callback remains in the Node.js/browser event loop timer queue until `t` elapses. By wrapping the race in a `try...finally` block and executing `clearTimeout(timerId)`, we ensure no dangling timers cause memory leaks or delay Node.js event-loop exits.

---

### Step-by-Step Approach

1. Return an `async` function accepting any number of arguments using the rest parameter `...args`.
2. Instantiate a `timeoutPromise` that registers a `setTimeout` scheduled for `t` milliseconds, rejecting with `"Time Limit Exceeded"`.
3. Save the returned `timerId` from `setTimeout`.
4. Use `await Promise.race([fn(...args), timeoutPromise])` to resolve or reject based on the fastest promise.
5. In the `finally` block, execute `clearTimeout(timerId)` to immediately remove the timeout handler from the event loop regardless of whether `fn` succeeded, failed, or timed out.

---

### Complexity Analysis

- **Time Complexity:** 
  - If `fn` settles in time $T_{fn} \le t$, time complexity is dominated by $O(T_{fn})$.
  - If $T_{fn} > t$, the promise rejects after exactly $O(t)$ milliseconds.
  - Overall time complexity: $O(\min(T_{fn}, t))$.

- **Space Complexity:** 
  - $O(1)$ auxiliary space overhead. We create two lightweight promise objects and a single timer reference per invocation.

---

### Common Pitfalls / Mistakes

1. **Forgetting `clearTimeout`:**
   - Omitting `clearTimeout` leaves active timers in the event loop. In long-running backend services (e.g., Node.js servers), this leads to memory leaks and uncollected closures.
2. **Not Handling Synchronous Errors:**
   - If `fn` is a synchronous function or throws before returning a promise, `fn(...args)` can throw an unhandled exception before `Promise.race` can handle it. When `fn` is marked `async` (per the problem description), it always returns a promise, but using `Promise.resolve(fn(...args))` can be an extra defensive measure.
3. **Promise State Mutability Misconception:**
   - Assuming that cancelling/rejecting a wrapper promise automatically aborts `fn`. JavaScript Promises are non-cancellable by default. Even after `Promise.race` rejects, `fn` continues executing in the background unless paired with an `AbortController`.

---

### Real Interview Follow-Up Questions & Answers

#### 1. "How would you actually abort the running operation inside `fn` instead of just ignoring its result?"
**Answer:**
JavaScript promises cannot be cancelled externally once initiated. To truly cancel the underlying task (e.g., an HTTP fetch or I/O operation), we pass an `AbortSignal`:
```javascript
const controller = new AbortController();
const timerId = setTimeout(() => controller.abort(), t);
// fn must accept { signal: controller.signal } and listen to abort events.
```
In modern fetch APIs, `fetch(url, { signal: controller.signal })` will actively terminate the underlying TCP/socket connection, saving bandwidth and server load.

#### 2. "What happens if `t = 0`?"
**Answer:**
If `t = 0`, `setTimeout` schedules the rejection on the macrotask queue (with a minimum browser clamp of typically 1-4ms depending on nesting level). If `fn(...args)` resolves synchronously or in the microtask queue, `fn` will win. If `fn` awaits any macrotask, the timeout will win. To guarantee immediate timeout at `t = 0`, an explicit check `if (t <= 0) return Promise.reject("Time Limit Exceeded")` can be placed at the start of the function.

#### 3. "How would you handle rate limiting or concurrency control with timeouts across thousands of concurrent calls?"
**Answer:**
Running thousands of concurrent timeouts can saturate the timer heap in the V8 engine. Instead of a naive wrapper, we would use an execution queue (e.g., a Semaphore or Leaky Bucket/Token Bucket rate limiter) with a bounded worker pool. The timeout wrapper is applied only when the task actually begins execution, not while it is waiting in the queue.
