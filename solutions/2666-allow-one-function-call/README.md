# 2666. Allow One Function Call

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/allow-one-function-call/](https://leetcode.com/problems/allow-one-function-call/)  
**Topics:** 

---

## 📝 Problem Statement

Given a function `fn`, return a new function that is identical to the original function except that it ensures `fn` is called at most once.

	- The first time the returned function is called, it should return the same result as `fn`.

	- Every subsequent time it is called, it should return `undefined`.

 
Example 1:

```

**Input:** fn = (a,b,c) => (a + b + c), calls = [[1,2,3],[2,3,6]]
**Output:** [{"calls":1,"value":6}]
**Explanation:**
const onceFn = once(fn);
onceFn(1, 2, 3); // 6
onceFn(2, 3, 6); // undefined, fn was not called

```

Example 2:

```

**Input:** fn = (a,b,c) => (a * b * c), calls = [[5,7,4],[2,3,6],[4,6,8]]
**Output:** [{"calls":1,"value":140}]
**Explanation:**
const onceFn = once(fn);
onceFn(5, 7, 4); // 140
onceFn(2, 3, 6); // undefined, fn was not called
onceFn(4, 6, 8); // undefined, fn was not called

```

 
**Constraints:**

	- `calls` is a valid JSON array

	- `1

---

## 💻 Implementation (python3)

```js
/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let hasBeenCalled = false;

    return function(...args) {
        if (!hasBeenCalled) {
            hasBeenCalled = true;
            // Use apply to preserve the execution context (`this`)
            return fn.apply(this, args);
        }
        return undefined;
    };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

This is a classic implementation of the **Once Decorator** pattern, commonly seen in utility libraries like Lodash (`_.once`). 

In JavaScript, functions are first-class citizens. When a function returns another function, the inner function maintains access to the outer function's scope even after the outer function has finished executing. This mechanism is called a **closure**.

To ensure `fn` is called at most once:
1. We maintain state across invocations using a boolean flag (`hasBeenCalled`) stored in the closure.
2. On the first call, we flip the flag to `true`, call the underlying function with the provided arguments, and return its value.
3. On every subsequent call, we immediately return `undefined` without executing `fn`.

### Step-by-Step Approach

1. Define a state variable `hasBeenCalled = false` in the outer function's scope.
2. Return a new wrapper function accepting rest parameters `(...args)`.
3. Check `if (!hasBeenCalled)`:
   - Mark `hasBeenCalled = true`.
   - Call `fn.apply(this, args)` (or `Reflect.apply(fn, this, args)`). Preserving `this` is crucial for JavaScript production code in case `fn` relies on object method context.
4. If `hasBeenCalled` is already `true`, return `undefined`.

### Complexity Analysis

- **Time Complexity:** 
  - **Wrapper overhead:** $\mathcal{O}(1)$ time per call.
  - **First call:** $\mathcal{O}(T)$, where $T$ is the execution time of `fn(...args)`.
  - **Subsequent calls:** $\mathcal{O}(1)$, as the function immediately returns `undefined` without executing `fn`.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The closure holds a single boolean reference (`hasBeenCalled`), which takes constant memory.

### Common Pitfalls / Mistakes Candidates Make

1. **Context Loss (`this` binding):**
   Simply writing `fn(...args)` ignores the `this` context. If the wrapped function is invoked as an object method (e.g., `obj.onceMethod()`), `fn` will lose reference to `obj` unless called via `fn.apply(this, args)`.
2. **Checking the Cached Value Instead of a Flag:**
   Some candidates try to check `if (result !== undefined)` instead of a dedicated boolean flag. If the original function legitimately returns `undefined`, the function would incorrectly execute again on subsequent calls.
3. **Memory Leaks with Stored Arguments/Results:**
   If asked to cache the result (like standard memoization or `lodash.once`), candidates often keep references to large objects in memory indefinitely. Cleaning up unneeded references or understanding when garbage collection occurs is a key senior-level distinction.

### Real Interview Follow-Up Questions

#### 1. What if the requirement was to return the *cached result* of the first call instead of `undefined`?
*Answer:* Maintain a `result` variable in closure scope.
```javascript
var once = function(fn) {
    let hasBeenCalled = false;
    let result;
    return function(...args) {
        if (!hasBeenCalled) {
            hasBeenCalled = true;
            result = fn.apply(this, args);
        }
        return result;
    };
};
```

#### 2. What happens if `fn` throws an error on the first call?
*Answer:* In our implementation, if `fn` throws an error, `hasBeenCalled` is already set to `true`, meaning future calls will return `undefined` instead of re-trying. Depending on product requirements:
- If failures should retry: set `hasBeenCalled = true` only *after* `fn` succeeds, or wrap in `try...catch`.
- If failures should permanently fail or re-throw: capture the thrown exception and re-throw it on subsequent calls.

#### 3. How does this behave in multithreaded environments (e.g., Node.js Worker Threads, Java, Go)?
*Answer:* JavaScript in the main browser/Node thread runs on a single-threaded event loop, so there are no race conditions between checking `hasBeenCalled` and mutating it. However, in multithreaded environments, a race condition exists (Check-Then-Act). You would need synchronization primitives like a mutex, atomic compare-and-swap (CAS), or language constructs like `sync.Once` in Go or Double-Checked Locking with `volatile` in Java.
