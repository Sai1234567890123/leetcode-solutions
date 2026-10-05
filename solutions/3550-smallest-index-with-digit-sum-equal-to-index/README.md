# 3550. Smallest Index With Digit Sum Equal to Index

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/)  
**Topics:** Array, Math

---

## 📝 Problem Statement

You are given an integer array `nums`.

Return the **smallest** index `i` such that the sum of the digits of `nums[i]` is equal to `i`.

If no such index exists, return `-1`.

 
Example 1:

**Input:** nums = [1,3,2]

**Output:** 2

**Explanation:**

	- For `nums[2] = 2`, the sum of digits is 2, which is equal to index `i = 2`. Thus, the output is 2.

Example 2:

**Input:** nums = [1,10,11]

**Output:** 1

**Explanation:**

	- For `nums[1] = 10`, the sum of digits is `1 + 0 = 1`, which is equal to index `i = 1`.

	- For `nums[2] = 11`, the sum of digits is `1 + 1 = 2`, which is equal to index `i = 2`.

	- Since index 1 is the smallest, the output is 1.

Example 3:

**Input:** nums = [1,2,3]

**Output:** -1

**Explanation:**

	- Since no index satisfies the condition, the output is -1.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        """
        Finds the smallest index i such that the sum of the digits of nums[i] is equal to i.
        """
        for i, val in enumerate(nums):
            # Compute sum of digits mathematically to avoid string conversion overhead
            digit_sum = 0
            temp = val
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            # Since we iterate from 0 upwards, the first match is guaranteed to be the smallest
            if digit_sum == i:
                return i
                
        return -1
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the **smallest** index `i` where the sum of the digits of `nums[i]` equals `i`. 

Because we need the *smallest* index, we can linearly scan the array from index `0` to `n - 1`. The very first index `i` that satisfies the condition `sum_of_digits(nums[i]) == i` is guaranteed to be the minimal such index, allowing us to return early. If the loop completes without finding any such index, we return `-1`.

To compute the sum of digits of each number:
- We can extract digits using modulo `10` and integer division `// 10`. This is more efficient and memory-friendly than converting numbers to strings (`str(x)`), as it avoids heap allocation.

### Step-by-Step Approach

1. Iterate through `nums` using `enumerate(nums)` to get both the index `i` and value `val`.
2. For each number, compute the sum of its decimal digits:
   - Repeatedly take `temp % 10` and add it to an accumulator `digit_sum`.
   - Update `temp //= 10` until `temp` becomes `0`.
3. Check if `digit_sum == i`:
   - If true, return `i` immediately.
4. If the loop finishes without finding any matching index, return `-1`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n \cdot \log_{10}(M))$, where $n$ is the length of `nums` and $M$ is the maximum value in `nums`.
  - For standard 32-bit or 64-bit integers, the number of digits $\log_{10}(M) \le 19$, which is a small constant (at most $\approx 10$ operations for 32-bit integers).
  - Therefore, the time complexity is essentially linear: $\mathcal{O}(n)$.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space since we only use a few integer variables (`digit_sum`, `temp`, `i`, `val`) without allocating additional memory.

### Common Pitfalls / Mistakes Candidates Make

1. **String Conversion Overhead:** Using `sum(map(int, str(val)))` creates new string objects and lists on every iteration. While acceptable in casual Python scripts, in performance-critical code or competitive programming, arithmetic extraction is faster and avoids garbage collection pressure.
2. **Not Returning Early:** Finding all valid indices and then taking `min()` wastes time when the answer could be at index `0` or `1`. Returning on the first match is optimal.
3. **Handling `0`:** If `nums[i] == 0`, the while loop `temp > 0` doesn't execute and `digit_sum` remains `0`. If `i == 0` and `nums[0] == 0`, `digit_sum == i` holds (`0 == 0`), which correctly matches.

### Real Interview Follow-Up Questions

#### 1. What if the array is massive and streamed (e.g., millions of elements, potentially infinite stream)?
- **Answer:** We can process the elements on-the-fly with an index counter without storing the stream in memory. Furthermore, an interesting theoretical upper bound exists: the maximum possible digit sum for a standard integer (e.g., $M \le 10^9$) is $9 \times 9 = 81$ (for $999,999,999$). If index $i > \text{max\_possible\_digit\_sum}$, it is mathematically impossible for `digit_sum(nums[i]) == i`. Thus, we can terminate early after $i$ exceeds the maximum possible digit sum of the input type (e.g., stop checking after $i > 81$ if numbers are $\le 10^9$).

#### 2. What if $nums$ elements are represented as very large numbers (e.g., strings of up to $10^5$ digits)?
- **Answer:** If numbers are given as strings, direct digit summation takes $\mathcal{O}(L)$ time where $L$ is the string length. We would iterate over character bytes (`ord(c) - ord('0')`) and compare against $i$. Note that $i$ can still fit in a standard integer.

#### 3. How to optimize this using multi-threading/concurrency?
- **Answer:** Since we need the *smallest* index, we can divide the array into chunks (e.g., chunk 0: `[0, 1000)`, chunk 1: `[1000, 2000)`). We process chunks or use an atomic variable to track the minimum matching index found so far. If a thread finds a match at index $k$, any threads processing indices $\ge k$ can be cancelled immediately.
