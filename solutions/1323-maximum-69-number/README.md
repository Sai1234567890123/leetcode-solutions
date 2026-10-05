# 1323. Maximum 69 Number

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/maximum-69-number/](https://leetcode.com/problems/maximum-69-number/)  
**Topics:** Math, Greedy

---

## 📝 Problem Statement

You are given a positive integer `num` consisting only of digits `6` and `9`.

Return *the maximum number you can get by changing **at most** one digit (*`6`* becomes *`9`*, and *`9`* becomes *`6`*)*.

 
Example 1:

```

**Input:** num = 9669
**Output:** 9969
**Explanation:** 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

```

Example 2:

```

**Input:** num = 9996
**Output:** 9999
**Explanation:** Changing the last digit 6 to 9 results in the maximum number.

```

Example 3:

```

**Input:** num = 9999
**Output:** 9999
**Explanation:** It is better not to apply any change.

```

 
**Constraints:**

	- `1 4`

	- `num` consists of only `6` and `9` digits.

---

## 💻 Implementation (python3)

```py
class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        position = 0
        leftmost_six_pos = -1

        # Traverse digits from right to left (least significant to most significant)
        while temp > 0:
            digit = temp % 10
            if digit == 6:
                # Update the position of the 6 found; since we move right-to-left,
                # the last 6 we encounter will be the most significant (leftmost).
                leftmost_six_pos = position
            temp //= 10
            position += 1

        # If a '6' was found, changing it to '9' adds 3 * (10 ** position)
        if leftmost_six_pos != -1:
            return num + 3 * (10 ** leftmost_six_pos)
        
        return num
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The goal is to maximize the integer by flipping at most one digit: either a `6` to `9`, or a `9` to `6`.

1. **Direction of Flip**: 
   - Flipping `9` to `6` decreases the value, which never helps us maximize the number.
   - Flipping `6` to `9` increases the value by $3 \times 10^k$, where $k$ is the 0-indexed position of the digit from the right (power of 10).
2. **Greedy Choice**:
   - The value added by changing a digit is strictly proportional to its place value ($10^k$). A change at a higher place value always contributes more than any change at lower place values ($3 \times 10^k > \sum_{i=0}^{k-1} 3 \times 10^i$).
   - Therefore, to maximize the result, we must flip the **leftmost (most significant) `6`** to a `9`. If there are no `6`s, the number is already maximized.

While converting the number to a string and replacing the first `'6'` is an intuitive one-liner (`int(str(num).replace('6', '9', 1))`), solving it purely mathematically avoids string allocations, operating in true $O(1)$ auxiliary space.

---

### Step-by-Step Approach

1. Initialize `temp = num`, `position = 0`, and `leftmost_six_pos = -1`.
2. Extract digits from right to left using modulo `10` and integer division `// 10`:
   - If the current digit is `6`, record `leftmost_six_pos = position`. Because we iterate from least significant to most significant digit, subsequent `6`s will overwrite this variable, naturally ending up with the index of the leftmost `6`.
   - Increment `position` by 1.
3. If `leftmost_six_pos != -1`, we add $3 \times 10^{\text{leftmost\_six\_pos}}$ to `num`.
4. Return `num`.

---

### Complexity Analysis

- **Time Complexity:** $O(\log_{10}(\text{num}))$. The number of iterations equals the number of digits in `num`. Since $\text{num} \le 10^4$, there are at most 4-5 iterations, which runs in $O(1)$ bounded time.
- **Space Complexity:** $O(1)$ auxiliary space. We only use a few integer variables for arithmetic and tracking indices; no strings or auxiliary arrays are allocated.

---

### Common Pitfalls / Mistakes

1. **Greedily Flipping the Wrong Digit**: Flipping the first `6` encountered when traversing right-to-left (least significant) instead of left-to-right (most significant).
2. **Flipping '9' to '6'**: Missing the condition that we want to *maximize*, which means we should never turn a `9` into a `6`.
3. **Overwriting All Occurrences**: Using `str.replace('6', '9')` without specifying `count=1`, resulting in all `6`s being flipped instead of at most one.
4. **Unnecessary String Allocations**: Relying solely on `str()` conversions when an interviewer asks for a memory-efficient or in-place numeric manipulation.

---

### Real Interview Follow-Up Questions

#### 1. What if the number is provided as a stream of digits from left to right?
- **Answer:** We read digits one by one. The very first `6` we see should be printed/emitted as `9`. All subsequent digits remain unchanged. This enables an online, single-pass $O(1)$ memory streaming solution.

#### 2. What if we are allowed to change up to $k$ digits?
- **Answer:** We use the same greedy strategy generalized: change the first $k$ occurrences of `6` from left to right into `9`s. If there are fewer than $k$ occurrences of `6`, convert all of them to `9`s.

#### 3. What if the number contains digits other than 6 and 9 (e.g., standard digits 0-9)?
- **Answer:** To maximize, we still want to make the most significant digit as large as possible (ideally `9`). Scan from left to right to find the first digit $d < 9$, and replace it with `9`.
