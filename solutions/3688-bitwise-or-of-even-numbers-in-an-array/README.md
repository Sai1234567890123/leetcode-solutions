# 3688. Bitwise OR of Even Numbers in an Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/](https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/)  
**Topics:** Array, Bit Manipulation, Simulation

---

## 📝 Problem Statement

You are given an integer array `nums`.

Return the bitwise **OR** of all **even** numbers in the array.

If there are no even numbers in `nums`, return 0.

 
Example 1:

**Input:** nums = [1,2,3,4,5,6]

**Output:** 6

**Explanation:**

The even numbers are 2, 4, and 6. Their bitwise OR equals 6.

Example 2:

**Input:** nums = [7,9,11]

**Output:** 0

**Explanation:**

There are no even numbers, so the result is 0.

Example 3:

**Input:** nums = [1,8,16]

**Output:** 24

**Explanation:**

The even numbers are 8 and 16. Their bitwise OR equals 24.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        
        for num in nums:
            # Check if the number is even using bitwise AND with 1
            if (num & 1) == 0:
                result |= num
                
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the bitwise OR of all even numbers in a given list of integers `nums`. If there are no even numbers, we need to return `0`.

Key observations:
1. **Even Number Check**: A number $x$ is even if and only if its least significant bit (LSB) is $0$. We can test this in $O(1)$ using the condition `(x & 1) == 0` or standard modulo arithmetic `x % 2 == 0`.
2. **Identity Element for Bitwise OR**: The identity element of the bitwise OR operation is $0$ ($x \mid 0 = x$). Thus, initializing our accumulator variable to `0` satisfies two things naturally:
   - It doesn't alter the bitwise OR when elements are combined.
   - If no even numbers are present in `nums`, the accumulator remains `0`, perfectly matching the fallback requirement.

### Step-by-Step Approach

1. Initialize `result = 0`.
2. Iterate through each integer `num` in the array `nums`:
   - If `(num & 1) == 0`, perform bitwise OR: `result |= num`.
3. Return `result`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of elements in `nums`. We traverse the array once, performing constant time bitwise operations for each element.
- **Space Complexity:** $\mathcal{O}(1)$. Only a single integer variable `result` is maintained in memory.

### Common Pitfalls / Mistakes Candidates Make

1. **Operator Precedence in Python**: In Python, bitwise AND (`&`) has lower precedence than equality (`==`). Writing `num & 1 == 0` evaluates as `num & (1 == 0)`, which yields `num & False` -> `0`. Always use parentheses: `(num & 1) == 0`.
2. **Handling Empty or Odd-Only Lists**: Using `functools.reduce` without specifying an `initial` value will raise a `TypeError` on an empty sequence or require an explicit check for when no even numbers are found. Initializing with `0` cleanly avoids this.
3. **Negative Numbers**: While typical LeetCode bit manipulation problems use non-negative numbers, if negative numbers are possible, Python handles arbitrary-precision integers (two's complement abstraction), but `num % 2 == 0` or `(num & 1) == 0` remains correct for negative even numbers as well.

### Real Interview Follow-Up Questions & Answers

#### 1. How would you handle a streaming data input (infinite stream of integers)?
**Answer:** The bitwise OR operation is associative, commutative, and idempotent ($x \mid x = x$). Because of these properties, we do not need to store the stream. We simply maintain a running state `current_or = 0` and update it as each element arrives: `if (x & 1) == 0: current_or |= x`. Queries for the current bitwise OR can be served in $\mathcal{O}(1)$ time with $\mathcal{O}(1)$ auxiliary space.

#### 2. What if the array is massive and distributed across multiple machines (MapReduce / Spark)?
**Answer:** Because bitwise OR is associative and commutative, this is an embarrassingly parallel problem:
- **Map phase:** Each worker independently computes the bitwise OR of all even numbers in its assigned partition.
- **Reduce phase:** The master node aggregates the partial bitwise OR results from each partition using a single reduction tree.

#### 3. Can we optimize further using SIMD / Vectorization?
**Answer:** Yes. On modern CPUs, AVX2 or AVX-512 instructions can load vectors of 32-bit or 64-bit integers, mask out odd values using vector bitwise operations, and perform vector OR reductions across 256/512-bit registers, achieving a high throughput multi-fold speedup over scalar loops.
