# 2695. Array Wrapper

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/array-wrapper/](https://leetcode.com/problems/array-wrapper/)  
**Topics:** 

---

## 📝 Problem Statement

Create a class `ArrayWrapper` that accepts an array of integers in its constructor. This class should have two features:

	- When two instances of this class are added together with the `+` operator, the resulting value is the sum of all the elements in both arrays.

	- When the `String()` function is called on the instance, it will return a comma separated string surrounded by brackets. For example, `[1,2,3]`.

 
Example 1:

```

**Input:** nums = [[1,2],[3,4]], operation = "Add"
**Output:** 10
**Explanation:**
const obj1 = new ArrayWrapper([1,2]);
const obj2 = new ArrayWrapper([3,4]);
obj1 + obj2; // 10

```

Example 2:

```

**Input:** nums = [[23,98,42,70]], operation = "String"
**Output:** "[23,98,42,70]"
**Explanation:**
const obj = new ArrayWrapper([23,98,42,70]);
String(obj); // "[23,98,42,70]"

```

Example 3:

```

**Input:** nums = [[],[]], operation = "Add"
**Output:** 0
**Explanation:**
const obj1 = new ArrayWrapper([]);
const obj2 = new ArrayWrapper([]);
obj1 + obj2; // 0

```

 
**Constraints:**

	- `0

---

## 💻 Implementation (python3)

```js
/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
    // Precompute the sum to make valueOf() an O(1) operation
    this.sum = nums.reduce((acc, curr) => acc + curr, 0);
};

/**
 * Invoked during numeric coercion or default primitive conversion (e.g. `obj1 + obj2`).
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.sum;
};

/**
 * Invoked during string coercion (e.g. `String(obj)`).
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return `[${this.nums.join(',')}]`;
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

JavaScript uses type coercion when operators like `+` or built-in functions like `String()` are applied to objects. 

1. **Addition (`+` operator)**:
   - When using the binary `+` operator on two objects, JavaScript attempts to convert each object to a primitive value.
   - It checks `[Symbol.toPrimitive]('default')`. If not defined, it checks `valueOf()`, and if `valueOf()` returns a primitive, it uses that primitive.
   - By implementing `valueOf()` to return the sum of all elements in the array, evaluating `obj1 + obj2` will resolve to `obj1.valueOf() + obj2.valueOf()`, producing the sum of all elements across both instances.
   - We can precompute the sum in the constructor so that every addition operation runs in $O(1)$ time.

2. **String Conversion (`String()` function)**:
   - When an object is converted to a string using `String(obj)`, JavaScript invokes `[Symbol.toPrimitive]('string')`, and if not present, falls back to `toString()`.
   - By implementing `toString()` to join elements with commas and wrap them in square brackets (or via `JSON.stringify(this.nums)`), we produce the exact required representation `"[x,y,z]"`.

---

### Step-by-Step Approach

1. **Constructor (`ArrayWrapper`)**:
   - Store the input array reference as `this.nums`.
   - Calculate and cache the sum of all elements using `Array.prototype.reduce()`.

2. **`valueOf()`**:
   - Return the precomputed sum `this.sum`.

3. **`toString()`**:
   - Format and return `[${this.nums.join(',')}]`. Note that for empty arrays, `[].join(',')` yields `""`, so the template literal results in `"[]"`, which matches the expected output.

---

### Complexity Analysis

- **Time Complexity**:
  - **Constructor**: $\mathcal{O}(N)$, where $N$ is the number of elements in `nums`, due to the single pass of `reduce()` to compute the sum.
  - **`valueOf()`**: $\mathcal{O}(1)$ since the sum is cached upon creation.
  - **`toString()`**: $\mathcal{O}(N)$ because joining $N$ numbers into a string takes linear time in the total number of characters and elements.
  
- **Space Complexity**:
  - $\mathcal{O}(1)$ auxiliary space (ignoring the storage of the original array reference and the returned string).

---

### Common Pitfalls / Mistakes

1. **Overwriting Object Prototype Methods vs. Custom Methods**:
   - Some candidates attempt to write a custom `.add()` method instead of recognizing that JavaScript looks for `valueOf` or `Symbol.toPrimitive` when handling the `+` operator.

2. **Order of Coercion**:
   - If `valueOf()` returns an object instead of a primitive, JavaScript falls back to `toString()`. Returning a primitive number directly from `valueOf()` ensures proper numeric addition.

3. **Empty Arrays**:
   - For an empty array `[]`, `reduce` must be provided an initial value (`0`), otherwise calling `[].reduce(...)` without an initial value throws a `TypeError: Reduce of empty array with no initial value`.

---

### Real Interview Follow-Up Questions

#### 1. What if the array can be mutated after instantiation (e.g., `push`, `pop`)?
- **Answer**: Precomputing the sum in the constructor would lead to stale data. Either:
  1. Calculate the sum on-the-fly inside `valueOf()` in $\mathcal{O}(N)$ time.
  2. Encapsulate mutation methods (e.g., `addNumber(n)`) on `ArrayWrapper` to update `this.sum` dynamically in $\mathcal{O}(1)$ time.
  3. Wrap `nums` using a `Proxy` that intercepts array index mutations and methods like `push`/`pop` to adjust the running total.

#### 2. How can we handle modern ES6+ coercion protocols?
- **Answer**: Implement `[Symbol.toPrimitive](hint)`:
  ```javascript
  ArrayWrapper.prototype[Symbol.toPrimitive] = function(hint) {
      if (hint === 'string') {
          return this.toString();
      }
      return this.valueOf(); // 'number' and 'default'
  };
  ```
  `Symbol.toPrimitive` takes precedence over `valueOf` and `toString`.

#### 3. What if the array contains large numbers exceeding `Number.MAX_SAFE_INTEGER`?
- **Answer**: Standard 64-bit IEEE 754 floats will lose precision past $2^{53} - 1$. We should check constraints and optionally use `BigInt` if operations involve arbitrarily large integers.
