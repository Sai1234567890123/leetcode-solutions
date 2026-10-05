# 1342. Number of Steps to Reduce a Number to Zero

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)  
**Topics:** Math, Bit Manipulation

---

## 📝 Problem Statement

Given an integer `num`, return *the number of steps to reduce it to zero*.

In one step, if the current number is even, you have to divide it by `2`, otherwise, you have to subtract `1` from it.

 
Example 1:

```

**Input:** num = 14
**Output:** 6
**Explanation:** 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

```

Example 2:

```

**Input:** num = 8
**Output:** 4
**Explanation:** 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.

```

Example 3:

```

**Input:** num = 123
**Output:** 12

```

 
**Constraints:**

	- `0 6`

---

## 💻 Implementation (python3)

```py
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        
        # In binary representation:
        # - Subtracting 1 flips a set bit (1 -> 0).
        # - Dividing by 2 right-shifts the bits by 1.
        #
        # Each set bit ('1') requires:
        #   1 step to subtract (except the most significant bit) + 1 step to shift right.
        # Each unset bit ('0') requires:
        #   1 step to shift right.
        #
        # Total steps = (total bits - 1) + (count of set bits)
        # where (total bits - 1) is the number of right shifts,
        # and (count of set bits) is the number of subtractions.
        return (num.bit_length() - 1) + num.bit_count()
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The operations allowed on `num` correspond directly to binary operations:
1. **Subtract 1 if odd**: An odd number in binary ends with `1`. Subtracting 1 changes the least significant bit (LSB) from `1` to `0`.
2. **Divide by 2 if even**: An even number in binary ends with `0`. Dividing by 2 right-shifts the binary representation by 1 bit (`num >>= 1`).

To reduce `num` to `0`:
- Every bit up to the most significant bit (MSB) must be shifted out. Shifting all bits right until 0 is reached requires `num.bit_length() - 1` divisions.
- Every set bit (`1`) must be flipped to `0` via subtraction before it can be shifted out. This requires `num.bit_count()` subtractions (one for each set bit, including the MSB which becomes 0 at the very last step).

Hence, for any `num > 0`:
$$\text{Total Steps} = (\text{bit\_length} - 1) + \text{bit\_count}$$

For `num = 0`, 0 steps are required.

---

### Step-by-Step Approach

1. **Handle Base Case**: If `num == 0`, immediately return `0`.
2. **Use Built-in Bit Manipulation**:
   - `num.bit_length()` returns the number of bits necessary to represent `num` in binary (excluding the sign and leading zeros).
   - `num.bit_count()` returns the number of set bits (population count / popcount).
3. **Compute and Return**: Calculate `(num.bit_length() - 1) + num.bit_count()`.

*(Alternative Simulation Approach)*:
A while loop `while num > 0:` with `num = num - 1 if num & 1 else num >> 1` also achieves $O(\log \text{num})$ time, but the bit-math approach runs directly in $O(1)$ CPU cycles utilizing hardware instructions (`POPCNT` and `CLZ`/`BSR`).

---

### Complexity Analysis

- **Time Complexity:** $O(1)$ under standard fixed-size integer models (or $O(\log(\text{num}))$ bit-level complexity). Both `bit_length()` and `bit_count()` compile down to CPU intrinsics (`LZCNT`/`POPCNT`), executing in a few clock cycles.
- **Space Complexity:** $O(1)$. No auxiliary memory or data structures are allocated.

---

### Common Pitfalls / Mistakes

1. **Forgetting the Zero Edge Case:** If `num = 0`, `num.bit_length()` is `0`, leading to `(0 - 1) + 0 = -1` without an explicit guard check.
2. **Double Counting the MSB Shift:** When the MSB is reduced from `1` to `0`, the number becomes `0` and terminates. Candidates simulating division might perform an extra shift after reducing to zero if loop conditions are misconfigured.
3. **Using Division `/` instead of Integer Division `//` or Bit Shifts `>>`:** Float precision can break down for large numbers, and integer bit shifts (`>> 1`) are both faster and idiomatically correct.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if `num` is provided as an arbitrarily large string of binary digits (e.g., $10^6$ bits)?
**Answer:** The logic still holds! Rather than parsing it to an integer (which takes $O(N^2)$ or $O(N \log^2 N)$ time for string-to-int conversion), we can iterate over the binary string once in $O(N)$ time:
- Count total characters $L$ (ignoring leading zeros).
- Count the number of `'1'`s.
- Result is $(L - 1) + \text{count}('1')$.

#### 2. How would you handle a streaming input of operations or numbers?
**Answer:** If bits arrive via a stream (e.g., from LSB to MSB or MSB to LSB), maintain two running counters: total bits received and total set bits. Once the stream ends, apply the same formula in $O(1)$ post-processing.

#### 3. What if negative numbers are allowed?
**Answer:** The problem statement must define what "reducing to zero" means for negatives. If the same rules apply:
- An odd negative (e.g., `-3`) minus 1 becomes `-4` (moving further from zero).
- In such a framework, negative numbers might enter infinite loops unless rules are modified (e.g., add 1 if odd, or operate on absolute values). Always clarify constraints with the interviewer.
