# 2621. Sleep

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/sleep/](https://leetcode.com/problems/sleep/)  
**Topics:** 

---

## 📝 Problem Statement

Given a positive integer `millis`, write an asynchronous function that sleeps for `millis` milliseconds. It can resolve any value.

**Note** that *minor* deviation from `millis` in the actual sleep duration is acceptable.

 
Example 1:

```

**Input:** millis = 100
**Output:** 100
**Explanation:** It should return a promise that resolves after 100ms.
let t = Date.now();
sleep(100).then(() => {
  console.log(Date.now() - t); // 100
});

```

Example 2:

```

**Input:** millis = 200
**Output:** 200
**Explanation:** It should return a promise that resolves after 200ms.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```js
/**
 * Asynchronously pauses execution for the specified duration.
 *
 * @param {number} millis - The number of milliseconds to sleep.
 * @return {Promise<void>} A promise that resolves after millis milliseconds.
 */
async function sleep(millis) {
    // Return a Promise that resolves when setTimeout completes after `millis` ms.
    return new Promise(resolve => setTimeout(resolve, millis));
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

JavaScript's runtime model is single-threaded and event-loop driven. Unlike synchronous languages (e.g., C/C++ `sleep()` or Python `time.sleep()`), blocking the thread synchronously in JavaScript (such as using a busy-wait loop `while (Date.now() - start < millis)`) freezes the entire call stack, halting UI rendering and incoming event handling.

To non-blockingly pause asynchronous execution, we wrap the native timer API `setTimeout` in a JavaScript `Promise`. The caller can then `await` this Promise or attach a `.then()` handler, allowing the JavaScript engine to schedule other tasks while waiting for the timer event to enter the Macrotask Queue.

### Step-by-Step Approach

1. Instantiate and return a `new Promise((resolve) => ...)`.
2. Inside the Promise executor function, register a callback with `setTimeout`.
3. Pass `resolve` as the callback to `setTimeout`, along with `millis` as the delay.
4. When `millis` milliseconds elapse (subject to event loop timer granularity), the event loop picks up the timer callback from the macrotask queue, calls `resolve()`, and transitions the Promise to the `fulfilled` state.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ computational time. The setup time of the timer and the execution of the callback are instantaneous ($\mathcal{O}(1)$ CPU work). The wall-clock delay is $\mathcal{O}(millis)$, but this does not block the thread.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. A single Promise object and a single timer entry are registered in the runtime's timer heap / table.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Busy-Wait Loop (`while (Date.now() - start < millis)`):**
   - *Mistake:* Attempting to block execution synchronously.
   - *Why it's bad:* Completely starves the Event Loop, freezes browser UI tabs, and consumes 100% of a CPU core.

2. **Unnecessary `await` Inside the Function:**
   ```javascript
   async function sleep(millis) {
       await new Promise(res => setTimeout(res, millis));
   }
   ```
   - While syntactically valid and passing tests, returning the promise directly (`return new Promise(...)`) avoids the unnecessary overhead of creating an extra microtask resolution tick.

3. **Passing Invocation Instead of Reference to `setTimeout`:**
   - Writing `setTimeout(resolve(), millis)` instead of `setTimeout(resolve, millis)`. Calling `resolve()` immediately resolves the promise on the exact same tick without sleeping.

---

### Real Interview Follow-Up Questions & How to Answer

#### 1. What if the caller needs to cancel the sleep early (cancellation support)?
- **Answer:** Use the standard `AbortSignal` pattern from the Web API / Node.js.
  ```javascript
  function cancellableSleep(millis, signal) {
      return new Promise((resolve, reject) => {
          if (signal?.aborted) {
              return reject(new DOMException("Aborted", "AbortError"));
          }
          const timer = setTimeout(resolve, millis);
          signal?.addEventListener('abort', () => {
              clearTimeout(timer);
              reject(new DOMException("Aborted", "AbortError"));
          }, { once: true });
      });
  }
  ```

#### 2. Why might `sleep(100)` take longer than 100ms in practice?
- **Answer:** 
  - **Event Loop Starvation:** `setTimeout` specifies a *minimum* delay, not an exact execution time. If long-running synchronous code or microtasks are on the stack, the timer callback must wait until the call stack is clear.
  - **Timer Clamping:** Browsers clamp nested `setTimeout` calls to a minimum of 4ms (HTML spec). In background/inactive tabs, timers may be throttled to 1000ms to preserve battery and CPU.

#### 3. How would you handle a delay larger than `2^31 - 1` milliseconds (~24.8 days)?
- **Answer:** `setTimeout` stores delays as a 32-bit signed integer. Values greater than `2147483647` cause integer overflow, leading to an immediate trigger (`0ms`). To handle arbitrary long durations, implement a recursive/looping sleep that waits in chunks of `2147483647` ms until the total duration is exhausted.
