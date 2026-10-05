# 2553. Separate the Digits in an Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/separate-the-digits-in-an-array/](https://leetcode.com/problems/separate-the-digits-in-an-array/)  
**Topics:** Array, Simulation

---

## 📝 Problem Statement

Given an array of positive integers `nums`, return *an array *`answer`* that consists of the digits of each integer in *`nums`* after separating them in **the same order** they appear in *`nums`.

To separate the digits of an integer is to get all the digits it has in the same order.

	- For example, for the integer `10921`, the separation of its digits is `[1,0,9,2,1]`.

 
Example 1:

```

**Input:** nums = [13,25,83,77]
**Output:** [1,3,2,5,8,3,7,7]
**Explanation:** 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.

```

Example 2:

```

**Input:** nums = [7,1,3,9]
**Output:** [7,1,3,9]
**Explanation:** The separation of each integer in nums is itself.
answer = [7,1,3,9].

```

 
**Constraints:**

	- `1 5`

---

## 💻 Implementation (python3)

```py
class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        """
        Separates the digits of each integer in nums and returns them
        in the exact order of their appearance.
        """
        # List comprehension leveraging fast C-level string iteration in Python
        return [int(char) for num in nums for char in str(num)]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires extracting all individual digits from a list of integers while preserving their relative order—both across numbers and within each individual number.

There are two primary ways to approach this:
1. **String Conversion (Idiomatic Python):** Convert each integer to its string representation and iterate through each character, converting it back to an integer. In CPython, string conversion and iteration are implemented in optimized C, making this both concise and extremely performant.
2. **Mathematical Extraction (Arithmetic Approach):** Use modulo (`num % 10`) and division (`num // 10`) to extract digits from least significant to most significant, then reverse them. While this avoids string allocation, it adds code overhead and typically runs slower in interpreted Python.

The string comprehension approach is optimal in Python for readability, memory efficiency, and speed.

---

### Step-by-Step Approach

1. Iterate over each integer `num` in `nums`.
2. Convert `num` to a string: `str(num)`.
3. Iterate over each character `char` in the string representation.
4. Convert `char` back to an integer `int(char)`.
5. Collect these digits in order in the resulting list.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot D)$, where $N$ is the number of integers in `nums` and $D$ is the maximum number of digits in an integer. Given $nums[i] \le 10^5$, $D \le 6$, making $D$ effectively a constant. Thus, the time complexity is strictly linear: $\mathcal{O}(N)$.
- **Space Complexity:** $\mathcal{O}(N \cdot D)$ to store the output array. If we do not count the output array (as it is required by the problem statement), the auxiliary space is $\mathcal{O}(D) = \mathcal{O}(1)$ for intermediate string representations.

---

### Common Pitfalls / Mistakes

1. **Reversed Digits with Arithmetic:** Extracting digits via `num % 10` retrieves them from right to left (least significant to most significant). Candidates often forget to reverse the extracted digits before appending them to the main result.
2. **Handling Zero:** Although the problem specifies positive integers ($nums[i] \ge 1$), if $0$ were possible, a standard `while num > 0:` loop would fail to capture the digit `0`.
3. **Inefficient List Concatenation:** Using `result = result + [...]` inside a loop leads to $\mathcal{O}(K^2)$ quadratic time due to creating new lists repeatedly, rather than using `result.extend(...)` or list comprehensions.

---

### Real Interview Follow-Up Questions

#### 1. What if you are forbidden from converting integers to strings?
**Answer:** We can extract digits arithmetically. We either:
- Push digits extracted via `% 10` to a temporary stack/list and pop/reverse them:
  ```python
  ans = []
  for num in nums:
      digits = []
      while num > 0:
          digits.append(num % 10)
          num //= 10
      ans.extend(reversed(digits))
  return ans
  ```
- Or find the highest power of 10 less than or equal to `num` and extract digits from left to right directly.

#### 2. How would you handle a streaming input where memory is severely constrained?
**Answer:** Instead of collecting all digits into a list in memory, yield them one by one using a generator:
```python
def separate_digits_stream(nums_stream):
    for num in nums_stream:
        for char in str(num):
            yield int(char)
```
This reduces auxiliary memory to $\mathcal{O}(1)$ regardless of stream length.

#### 3. What if integers can be negative?
**Answer:** Digits of a number are unsigned. If the input allows negative numbers (e.g., `-13`), clarify whether the negative sign should be ignored or represented. Typically, we take `abs(num)` before digit extraction.
