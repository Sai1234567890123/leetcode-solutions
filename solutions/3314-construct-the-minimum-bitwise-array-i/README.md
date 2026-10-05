# 3314. Construct the Minimum Bitwise Array I

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/)  
**Topics:** Array, Bit Manipulation

---

## 📝 Problem Statement

You are given an array `nums` consisting of `n` prime integers.

You need to construct an array `ans` of length `n`, such that, for each index `i`, the bitwise `OR` of `ans[i]` and `ans[i] + 1` is equal to `nums[i]`, i.e. `ans[i] OR (ans[i] + 1) == nums[i]`.

Additionally, you must **minimize** each value of `ans[i]` in the resulting array.

If it is *not possible* to find such a value for `ans[i]` that satisfies the **condition**, then set `ans[i] = -1`.

 
Example 1:

**Input:** nums = [2,3,5,7]

**Output:** [-1,1,4,3]

**Explanation:**

	- For `i = 0`, as there is no value for `ans[0]` that satisfies `ans[0] OR (ans[0] + 1) = 2`, so `ans[0] = -1`.

	- For `i = 1`, the smallest `ans[1]` that satisfies `ans[1] OR (ans[1] + 1) = 3` is `1`, because `1 OR (1 + 1) = 3`.

	- For `i = 2`, the smallest `ans[2]` that satisfies `ans[2] OR (ans[2] + 1) = 5` is `4`, because `4 OR (4 + 1) = 5`.

	- For `i = 3`, the smallest `ans[3]` that satisfies `ans[3] OR (ans[3] + 1) = 7` is `3`, because `3 OR (3 + 1) = 7`.

Example 2:

**Input:** nums = [11,13,31]

**Output:** [9,12,15]

**Explanation:**

	- For `i = 0`, the smallest `ans[0]` that satisfies `ans[0] OR (ans[0] + 1) = 11` is `9`, because `9 OR (9 + 1) = 11`.

	- For `i = 1`, the smallest `ans[1]` that satisfies `ans[1] OR (ans[1] + 1) = 13` is `12`, because `12 OR (12 + 1) = 13`.

	- For `i = 2`, the smallest `ans[2]` that satisfies `ans[2] OR (ans[2] + 1) = 31` is `15`, because `15 OR (15 + 1) = 31`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            if x == 2:
                # 2 is the only even prime. For any integer k, k OR (k + 1) is always odd.
                ans.append(-1)
            else:
                # Find the lowest unset bit of x: (x + 1) & -(x + 1) gives 2^k,
                # where bits 0 to k - 1 of x are all 1s.
                # To minimize the answer, we flip the most significant bit among these
                # trailing ones, which is bit (k - 1) (i.e. value 2^(k - 1)).
                lowest_unset_bit = (x + 1) & -(x + 1)
                ans.append(x - (lowest_unset_bit >> 1))
        return ans
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

For any integer $y$, the operation $y + 1$ flips the lowest unset bit (the least significant `0`-bit) to `1` and resets all lower bits (which were previously `1`) to `0`.
When we compute $y \text{ OR } (y + 1)$:
- The bits above the lowest unset bit of $y$ remain identical.
- The lowest unset bit of $y$ becomes `1` in $(y + 1)$, so it becomes `1` in the OR result.
- The bits below the lowest unset bit are `1` in $y$, so they also remain `1` in the OR result.

Thus, $y \text{ OR } (y + 1)$ has the exact effect of turning the **least significant `0`-bit** of $y$ into a `1`.

Consequently:
1. $y \text{ OR } (y + 1)$ is **always odd**, because the least significant bit (bit 0) is guaranteed to be `1`. Since `2` is an even prime, no integer $y$ can satisfy $y \text{ OR } (y + 1) = 2$. Hence, for `nums[i] = 2`, the answer is always `-1`.
2. For any odd prime $x$, $x$ has a block of $k \ge 1$ trailing `1`s at bits $0, 1, \dots, k-1$, with bit $k$ being `0`.
   To obtain $x = y \text{ OR } (y + 1)$, $y$ must be formed by changing one of the bits that is `1` in $x$ back to `0`, such that this bit becomes the *lowest* unset bit of $y$.
   - Any bit chosen must have all bits to its right set to `1` in $y$ (and therefore in $x$).
   - This means the bit we choose to set to `0` must be within the contiguous block of trailing `1`s of $x$ (i.e., at some position $p \in [0, k-1]$).
   - To **minimize** $y$, we want to subtract the largest possible power of two, which corresponds to choosing the highest possible position: $p = k - 1$.

Therefore, the optimal $y$ is:
$$y = x - 2^{k-1}$$

### Step-by-Step Approach

1. Iterate through each element $x$ in `nums`.
2. If $x == 2$, append `-1`.
3. Otherwise:
   - Identify the position of the lowest unset bit of $x$, which is equal to `(x + 1) & -(x + 1)`. Let this value be $2^k$.
   - The highest trailing set bit is $2^{k-1} = 2^k \gg 1$.
   - Subtract this value from $x$ and append $x - 2^{k-1}$ to `ans`.
4. Return `ans`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `nums`. For each element, finding the lowest unset bit and computing the result takes $\mathcal{O}(1)$ bitwise operations.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding the output array $\mathcal{O}(n)$).

### Common Pitfalls / Mistakes Candidates Make

1. **Brute Force Linear Search:** Trying all values from $0$ to $x$ for each query. While $nums[i]$ is small in Part I, this will TLE in Part II where $nums[i] \le 10^9$.
2. **Missing the Even Prime Case ($2$):** Forgetting that $2$ is prime, but cannot be represented as $y \text{ OR } (y + 1)$ because $y \text{ OR } (y + 1)$ is always odd.
3. **Flipping the Lowest Bit Instead of the Highest Trailing Bit:** Flipping bit $0$ gives $x - 1$, which is valid but not minimal (e.g., for $x = 7$ (`111`), $x - 1 = 6$ gives $6 \text{ OR } 7 = 7$, but $x - 4 = 3$ gives $3 \text{ OR } 4 = 7$, and $3 < 6$).

### Real Interview Follow-Ups & Answers

- **Follow-Up 1: What if $nums[i]$ is up to $10^9$ (Construct the Minimum Bitwise Array II)?**
  - *Answer:* The bitwise formula `x - (((x + 1) & -(x + 1)) >> 1)` works directly in $\mathcal{O}(1)$ time per element, effortlessly scaling to 32-bit and 64-bit integers with zero performance degradation.

- **Follow-Up 2: How would you process a continuous stream of numbers?**
  - *Answer:* Because each query is independent and computed in $\mathcal{O}(1)$ time and $\mathcal{O}(1)$ space, the function can be implemented as an iterator/generator (`yield`) or mapped over a streaming consumer without buffering elements in memory.

- **Follow-Up 3: Can this be parallelized / vectorized for extremely large inputs (e.g., SIMD / GPU)?**
  - *Answer:* Yes, bitwise arithmetic (`+`, `&`, `-`, `>>`) is embarrassingly parallel. In C++/CUDA, SIMD vector intrinsics (like AVX-512) or GPU compute kernels can process billions of integers per second.
