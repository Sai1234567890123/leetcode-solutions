# 2520. Count the Digits That Divide a Number

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-the-digits-that-divide-a-number/](https://leetcode.com/problems/count-the-digits-that-divide-a-number/)  
**Topics:** Math

---

## 📝 Problem Statement

Given an integer `num`, return *the number of digits in `num` that divide *`num`.

An integer `val` divides `nums` if `nums % val == 0`.

 
**Example 1:**

```

**Input:** num = 7
**Output:** 1
**Explanation:** 7 divides itself, hence the answer is 1.

```

**Example 2:**

```

**Input:** num = 121
**Output:** 2
**Explanation:** 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

```

**Example 3:**

```

**Input:** num = 1248
**Output:** 4
**Explanation:** 1248 is divisible by all of its digits, hence the answer is 4.

```

 
**Constraints:**

	- `1 9`

	- `num` does not contain `0` as one of its digits.

---

## 💻 Implementation (python3)

```py
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        
        # Extract each digit mathematically to avoid string conversion overhead
        while temp > 0:
            digit = temp % 10
            if num % digit == 0:
                count += 1
            temp //= 10
            
        return count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem requires checking whether each constituent digit of a given integer `num` is a divisor of `num`. Since the constraints guarantee that `num` does not contain the digit `0`, we do not need to worry about division-by-zero errors.

We have two primary ways to access the digits:
1. **String Conversion (`str(num)`):** Simple and readable, but allocates additional memory on the heap.
2. **Mathematical Digit Extraction (`num % 10` and `num //= 10`):** Operates strictly in $O(1)$ auxiliary space and avoids object allocation, making it the preferred approach in production code and systems-level programming.

### Step-by-Step Approach
1. Maintain a copy of `num` called `temp` and initialize a counter `count = 0`.
2. While `temp > 0`:
   - Extract the least significant digit using `digit = temp % 10`.
   - Check if `num % digit == 0`. If true, increment `count`.
   - Remove the least significant digit using integer division: `temp //= 10`.
3. Return `count`.

### Complexity Analysis
- **Time Complexity:** $O(\log_{10}(\text{num}))$ or $O(D)$, where $D$ is the number of digits in `num`. Given $\text{num} \le 10^9$, $D \le 10$. The loop executes at most 10 times, making it effectively $O(1)$ constant time.
- **Space Complexity:** $O(1)$ auxiliary space, as only a few primitive integer variables (`count`, `temp`, `digit`) are used.

### Common Pitfalls / Mistakes Candidates Make
1. **Division by Zero:** Candidates often forget that a digit could be `0` in general problems. Even though the constraints here guarantee no `0` digits, in a real interview, explicitly calling out the zero-division check (`digit != 0`) shows defensive programming skills.
2. **Mutating the Original Value:** Mutating `num` directly while extracting digits will break the divisibility check `num % digit == 0`. Always use a temporary copy or extract digits without modifying the reference value needed for modulus.

### Real Interview Follow-Up Questions
1. **What if `num` contains zeros?**
   - *Answer:* Add a guard condition `if digit != 0 and num % digit == 0`.
2. **What if `num` can be negative?**
   - *Answer:* Work with the absolute value `abs(num)` for digit extraction and divisibility testing.
3. **What if `num` is represented as an arbitrarily large number / stream of digits?**
   - *Answer:* If `num` has millions of digits (e.g., streaming or big integer), checking `num % digit == 0` can be done using the division rules for single digits (1 to 9):
     - Digits like 1, 2, 5 only depend on the last digit.
     - Digits like 3 and 9 depend on the sum of digits modulo 3 or 9.
     - Digits like 4 and 8 depend on the last 2 or 3 digits.
     - Digits 6 depends on divisibility by 2 and 3.
     - Digit 7 can be tracked via standard streaming modulo: `remainder = (remainder * 10 + digit) % 7`.
     This avoids storing or processing the massive number all at once.
