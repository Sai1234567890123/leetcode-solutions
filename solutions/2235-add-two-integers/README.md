# 2235. Add Two Integers

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/add-two-integers/](https://leetcode.com/problems/add-two-integers/)  
**Topics:** Math

---

## 📝 Problem Statement

Given two integers `num1` and `num2`, return *the **sum** of the two integers*.
 
Example 1:

```

**Input:** num1 = 12, num2 = 5
**Output:** 17
**Explanation:** num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

```

Example 2:

```

**Input:** num1 = -10, num2 = 4
**Output:** -6
**Explanation:** num1 + num2 = -6, so -6 is returned.

```

 
**Constraints:**

	- `-100

---

## 💻 Implementation (python3)

```py
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        """
        Calculates the sum of two integers.
        
        :param num1: First integer operand
        :param num2: Second integer operand
        :return: Sum of num1 and num2
        """
        return num1 + num2
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks for the arithmetic sum of two integers, `num1` and `num2`. Under the given constraints ($-100 \le num1, num2 \le 100$), Python handles arbitrary-precision integers natively, so there is no risk of integer overflow. The standard addition operator `+` directly computes the result in constant time.

### Step-by-Step Approach
1. Take inputs `num1` and `num2`.
2. Apply the addition operator `+` to compute `num1 + num2`.
3. Return the evaluated result.

### Complexity Analysis
- **Time Complexity:** $O(1)$. Addition of fixed-size integers is performed in a single processor instruction cycle.
- **Space Complexity:** $O(1)$. No auxiliary memory or data structures are allocated.

### Common Pitfalls / Mistakes
1. **Overthinking the Problem:** Attempting complex bitwise manipulation (like full-adder logic using XOR and AND) unless explicitly asked not to use the `+` operator (e.g., LeetCode 371: *Sum of Two Integers*).
2. **Integer Overflow Assumptions:** In statically-typed languages like C++ or Java, adding two large 32-bit signed integers could trigger arithmetic overflow. Even though constraints here are small ($-100$ to $100$), in a real interview, always clarify the numerical bounds and discuss how overflow should be handled.

### Real Interview Follow-Up Questions & How to Answer Them

#### 1. What if you are forbidden from using the `+` or `-` operators?
*Answer:* We can implement bitwise addition using a half-adder / full-adder logic:
- The sum without carry is computed using XOR: `a ^ b`.
- The carry is computed using AND followed by a left shift: `(a & b) << 1`.
- We repeat this process iteratively or recursively until the carry is 0. In Python, because integers have arbitrary precision, a mask (e.g., `0xFFFFFFFF` for 32-bit integers) is required to handle negative numbers properly.

```python
def getSum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    while b & mask:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a & mask if b > 0 else a
```

#### 2. How would you handle inputs that exceed standard integer ranges (e.g., numbers with millions of digits)?
*Answer:* In Python, integers have arbitrary precision by default. In languages with fixed-width integers (e.g., C++, Java), we would represent the numbers as strings or arrays of digits/words and implement digit-by-digit addition (similar to LeetCode 415: *Add Strings* or BigInteger implementations) with an explicit `carry` variable.

#### 3. What if the input arrives as a streaming data pipeline?
*Answer:* If we are continuously receiving a stream of numbers and need a running sum, we can maintain an accumulator state protected by appropriate concurrency primitives (e.g., `threading.Lock` or atomic operations like `AtomicLong` in Java) if accessed across multiple worker threads.
