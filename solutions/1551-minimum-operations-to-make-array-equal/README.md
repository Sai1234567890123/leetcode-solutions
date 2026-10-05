# 1551. Minimum Operations to Make Array Equal

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/minimum-operations-to-make-array-equal/](https://leetcode.com/problems/minimum-operations-to-make-array-equal/)  
**Topics:** Math

---

## 📝 Problem Statement

You have an array `arr` of length `n` where `arr[i] = (2 * i) + 1` for all valid values of `i` (i.e., `0 

In one operation, you can select two indices `x` and `y` where `0 

Given an integer `n`, the length of the array, return *the minimum number of operations* needed to make all the elements of arr equal.

 
Example 1:

```

**Input:** n = 3
**Output:** 2
**Explanation:** arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

```

Example 2:

```

**Input:** n = 6
**Output:** 9

```

 
**Constraints:**

	- `1 4`

---

## 💻 Implementation (python3)

```py
class Solution:
    def minOperations(self, n: int) -> int:
        """
        Calculates the minimum number of operations to make all elements equal.
        Each operation shifts 1 from an element > target to an element < target.
        The target element must be the mean of the array, which is n.
        Total operations required simplifies mathematically to n^2 // 4.
        """
        # Alternatively written as (n // 2) * ((n + 1) // 2)
        return (n * n) // 4
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The array is defined as `arr[i] = 2 * i + 1` for $0 \le i < n$.
The sum of the first $n$ odd numbers is a well-known identity:
$$\sum_{i=0}^{n-1} (2i + 1) = n^2$$

Since each operation consists of incrementing one element by 1 and decrementing another by 1, the total sum of the array is an invariant (it never changes). Therefore, if all $n$ elements are to be made equal, each element must end up equal to the average of the array:
$$\text{Target} = \frac{n^2}{n} = n$$

Each valid operation takes 1 from an element strictly greater than $n$ and gives it to an element strictly smaller than $n$. The minimum number of operations is simply the total deficit of all elements smaller than $n$:
$$\text{Operations} = \sum_{arr[i] < n} (n - arr[i])$$

Elements smaller than $n$ occur when $2i + 1 < n$, which gives $i < \frac{n - 1}{2}$. There are $k = \lfloor \frac{n}{2} \rfloor$ such elements.

- **Case 1: $n$ is even ($n = 2m$)**
  The elements smaller than $n$ have differences from $n$ equal to:
  $$(n - arr[m - 1]), \dots, (n - arr[0]) = 1, 3, 5, \dots, (2m - 1)$$
  The sum of the first $m$ odd numbers is $m^2 = (n / 2)^2 = \frac{n^2}{4}$.

- **Case 2: $n$ is odd ($n = 2m + 1$)**
  The elements smaller than $n$ have differences from $n$ equal to:
  $$(n - arr[m - 1]), \dots, (n - arr[0]) = 2, 4, 6, \dots, 2m$$
  The sum of the first $m$ even numbers is $2 \times \frac{m(m + 1)}{2} = m(m + 1) = \frac{n - 1}{2} \times \frac{n + 1}{2} = \frac{n^2 - 1}{4} = \lfloor \frac{n^2}{4} \rfloor$.

In both cases, using integer division, the answer is universally $\lfloor \frac{n^2}{4} \rfloor$ or `(n * n) // 4`.

---

### Step-by-Step Approach

1. Recognize that the operation preserves the array's sum.
2. Determine that the target value for every element must be $n$.
3. Compute the sum of deviations for all elements smaller than $n$.
4. Use the derived closed-form formula `(n * n) // 4` to return the result in $O(1)$ time without simulating or allocating any array.

---

### Complexity Analysis

- **Time Complexity:** $O(1)$. A single multiplication and integer division are computed in constant time.
- **Space Complexity:** $O(1)$. No additional memory or array allocation is used.

---

### Common Pitfalls / Mistakes

1. **Simulating the Operations:** Attempting to actually generate the array `[1, 3, 5, ...]` and simulate the two-pointer increments/decrements. This leads to $O(n)$ time and $O(n)$ space, which is unnecessary and inefficient.
2. **Looping to Sum Differences:** Computing the sum via a loop $O(n)$ instead of finding the closed-form arithmetic progression formula $O(1)$.
3. **Integer Overflow in Other Languages:** In languages like C++ or Java, when $n \le 10^4$, $n^2 \le 10^8$, which fits within a standard 32-bit signed integer. However, if $n \le 10^9$, computing `n * n` would overflow a 32-bit integer, necessitating a 64-bit integer (`long long`).

---

### Real Interview Follow-Up Questions

#### 1. What if $n$ is up to $10^{18}$?
- In Python, integers have arbitrary precision, so `(n * n) // 4` works out of the box.
- In languages like C++/Java/Go, `n * n` would exceed 64-bit unsigned integers (`uint64_t` max is $\approx 1.8 \times 10^{19}$, whereas $(10^{18})^2 = 10^{36}$). We can write it as `(n / 2) * ((n + 1) / 2)` using `__int128` or a BigInteger library to prevent intermediate overflow.

#### 2. What if operations had costs, e.g., moving between index $x$ and index $y$ costs $|x - y|$?
- This transforms into an optimal transport / Earth Mover's Distance problem.
- Symmetrical pairing $(i, n - 1 - i)$ is still optimal because crossing paths would strictly increase the transportation distance (by the triangle inequality).

#### 3. What if the array was not predefined as $arr[i] = 2i + 1$, but an arbitrary array where you can add 1 to one element and subtract 1 from another?
- If the sum is not divisible by $n$, all elements cannot be made equal.
- If it is divisible, target = $\text{sum} / n$. The minimum operations would be $\frac{1}{2} \sum_{i=0}^{n-1} |arr[i] - \text{target}|$.
