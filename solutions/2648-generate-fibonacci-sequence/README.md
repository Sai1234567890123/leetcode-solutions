# 2648. Generate Fibonacci Sequence

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/generate-fibonacci-sequence/](https://leetcode.com/problems/generate-fibonacci-sequence/)  
**Topics:** 

---

## 📝 Problem Statement

Write a generator function that returns a generator object which yields the **fibonacci sequence**.

The **fibonacci sequence** is defined by the relation `Xn = Xn-1 + Xn-2`.

The first few numbers of the series are `0, 1, 1, 2, 3, 5, 8, 13`.

 
Example 1:

```

**Input:** callCount = 5
**Output:** [0,1,1,2,3]
**Explanation:**
const gen = fibGenerator();
gen.next().value; // 0
gen.next().value; // 1
gen.next().value; // 1
gen.next().value; // 2
gen.next().value; // 3

```

Example 2:

```

**Input:** callCount = 0
**Output:** []
**Explanation:** gen.next() is never called so nothing is outputted

```

 
**Constraints:**

	- `0

---

## 💻 Implementation (python3)

```js
/**
 * Generates the Fibonacci sequence infinitely using a generator function.
 * 
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let current = 0;
    let next = 1;

    while (true) {
        // Yield the current Fibonacci number
        yield current;
        // Update values for the next iteration using destructuring assignment
        [current, next] = [next, current + next];
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The Fibonacci sequence is defined by the recurrence relation:
$$F_0 = 0$$
$$F_1 = 1$$
$$F_n = F_{n-1} + F_{n-2} \quad \text{for } n \ge 2$$

Since the requirement is to create a generator that produces elements on demand, we can maintain the state across generator pauses (`yield`). We only need two state variables at any point: the `current` number to yield and the `next` number in the sequence. 

By executing an infinite loop (`while (true)`), each call to `gen.next()` will resume execution right after the previous `yield`, update the state, and yield the next Fibonacci number before pausing again.

### Step-by-Step Approach

1. Initialize `current = 0` and `next = 1`.
2. Enter an infinite loop (`while (true)`).
3. `yield current` to output the current value and suspend execution.
4. When resumed, update `current` and `next`:
   - New `current` becomes old `next`.
   - New `next` becomes old `current + next`.
   - In modern JavaScript (ES6+), destructuring assignment `[current, next] = [next, current + next]` performs this swap cleanly without an explicit temporary variable.

### Complexity Analysis

- **Time Complexity:**
  - Initialization: $O(1)$ to create the generator object.
  - Per call to `gen.next()`: $O(1)$ arithmetic addition and variable assignment.
  - For $n$ calls: $O(n)$ total time.
- **Space Complexity:**
  - $O(1)$ auxiliary space. The generator maintains only two numeric variables (`current` and `next`) in its execution context stack frame.

### Common Pitfalls / Mistakes Candidates Make

1. **Premature Array Precomputation:** Generating an array of $N$ elements upfront instead of computing lazily. The generator interface implies an infinite or streaming sequence where values are evaluated on demand.
2. **Missing `0` as the first element:** Some definitions of Fibonacci start at $1, 1, 2, \dots$ instead of $0, 1, 1, \dots$. Always check the problem specification.
3. **Improper variable swapping:** Writing `current = next; next = current + next;` without a temporary variable or destructuring results in `next = 2 * next`, corrupting the sequence.
4. **Integer Overflow in JavaScript:** In standard JavaScript, numbers are double-precision floats (IEEE 754). Integers exceeding `Number.MAX_SAFE_INTEGER` ($2^{53} - 1 \approx 9 \times 10^{15}$, roughly $F_{78}$) lose precision unless `BigInt` is used.

### Real Interview Follow-Up Questions & Answers

#### 1. What happens if the generator is called more than 78 times?
*Answer:* In JavaScript, numbers larger than `Number.MAX_SAFE_INTEGER` ($2^{53} - 1$) lose precision. For an arbitrary-precision generator, we should use `BigInt`:
```javascript
var fibGeneratorBigInt = function*() {
    let current = 0n;
    let next = 1n;
    while (true) {
        yield current;
        [current, next] = [next, current + next];
    }
};
```

#### 2. How would you find the $N$-th Fibonacci number directly in $O(\log N)$ time instead of iterating with a generator?
*Answer:* We can use **Matrix Exponentiation** or **Fast Doubling**:
$$\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n$$
By computing the $n$-th power of the matrix using binary exponentiation, we achieve $O(\log n)$ arithmetic operations.

#### 3. How would you consume this generator safely without causing an infinite loop?
*Answer:* Since the generator is infinite, iterating with `for...of` without a termination check will hang the thread. You should either:
- Use a counter with `gen.next()` inside a standard loop.
- Implement a helper like `take(generator, count)` or use iterator helpers (such as `Iterator.prototype.take` in ECMAScript proposals).
