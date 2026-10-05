# 1863. Sum of All Subset XOR Totals

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/sum-of-all-subset-xor-totals/](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)  
**Topics:** Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration

---

## 📝 Problem Statement

The **XOR total** of an array is defined as the bitwise `XOR` of** all its elements**, or `0` if the array is** empty**.

	- For example, the **XOR total** of the array `[2,5,6]` is `2 XOR 5 XOR 6 = 1`.

Given an array `nums`, return *the **sum** of all **XOR totals** for every **subset** of *`nums`. 

**Note:** Subsets with the **same** elements should be counted **multiple** times.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`.

 
Example 1:

```

**Input:** nums = [1,3]
**Output:** 6
**Explanation: **The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6

```

Example 2:

```

**Input:** nums = [5,1,6]
**Output:** 28
**Explanation: **The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

```

Example 3:

```

**Input:** nums = [3,4,5,6,7,8]
**Output:** 480
**Explanation:** The sum of all XOR totals for every subset is 480.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        # Initialize 'or_all_nums' to 0. This variable will store the bitwise OR
        # of all elements in the 'nums' array.
        # A bit at position 'k' in 'or_all_nums' will be 1 if and only if
        # at least one number in 'nums' has its k-th bit set.
        or_all_nums = 0
        
        # Iterate through each number in the input array.
        for num in nums:
            # Perform a bitwise OR operation with the current number.
            # This accumulates all set bits from all numbers into 'or_all_nums'.
            or_all_nums |= num
        
        # Get the number of elements in the input array.
        # According to the problem constraints (1 <= nums.length <= 12),
        # 'n' will always be at least 1.
        n = len(nums)
        
        # The core mathematical property:
        # The sum of all subset XOR totals for an array 'nums' is equal to
        # (bitwise OR of all elements in 'nums') * (2^(n-1)).
        #
        # Intuition for this property:
        # Consider any specific bit position 'k'.
        # 1. If the k-th bit is 0 in ALL numbers in 'nums':
        #    Then, for any subset, its XOR total will also have its k-th bit as 0.
        #    So, this bit position contributes 0 to the total sum.
        #    This corresponds to the k-th bit of 'or_all_nums' being 0.
        #
        # 2. If the k-th bit is 1 in AT LEAST ONE number in 'nums':
        #    Let 'x' be an element in 'nums' that has its k-th bit set.
        #    We can pair up all 2^n subsets: for every subset 'A' that does NOT
        #    contain 'x', there's a corresponding subset 'A U {x}' that DOES
        #    contain 'x'.
        #    If the XOR total of 'A' has its k-th bit as 'b', then the XOR total
        #    of 'A U {x}' (which is XOR_total(A) ^ x) will have its k-th bit as 'b ^ 1'.
        #    This means that exactly half of the 2^n subsets will have their
        #    XOR total with the k-th bit set to 1, and the other half will have it as 0.
        #    So, 2^(n-1) subsets will contribute 2^k to the total sum for this bit position.
        #    This corresponds to the k-th bit of 'or_all_nums' being 1.
        #
        # Therefore, the total sum is equivalent to summing (2^(n-1) * 2^k) for
        # every bit position 'k' where the k-th bit of 'or_all_nums' is 1.
        # This simplifies to 'or_all_nums * 2^(n-1)'.
        
        # Calculate 2^(n-1) using a left bit shift for efficiency.
        # (1 << (n - 1)) is equivalent to 2 raised to the power of (n - 1).
        power_of_two_n_minus_1 = 1 << (n - 1)
        
        # Return the product as the final sum.
        return or_all_nums * power_of_two_n_minus_1
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to calculate the sum of XOR totals for all possible subsets of a given array `nums`. An empty subset has an XOR total of 0.

Let's consider a small example: `nums = [1, 3]`.
The subsets and their XOR totals are:
- `[]`: XOR total = 0
- `[1]`: XOR total = 1
- `[3]`: XOR total = 3
- `[1, 3]`: XOR total = 1 ^ 3 = 2
The sum of these XOR totals is `0 + 1 + 3 + 2 = 6`.

**Initial Approach (Brute Force - Backtracking):**
A straightforward way to solve this is to generate all `2^n` subsets using a recursive backtracking approach. For each element in `nums`, we have two choices: either include it in the current subset or exclude it. We maintain a running XOR total for the current subset being built. Once all elements have been considered, we add the `current_xor_total` to a global sum.
This approach would have a time complexity of `O(2^n)` because there are `2^n` subsets, and for each, we perform constant work. The space complexity would be `O(n)` for the recursion stack. Given `n <= 12`, `2^12 = 4096`, which is small enough for this approach to pass.

**Optimized Approach (Mathematical Property):**
While the brute-force approach works, competitive programming often rewards finding more efficient mathematical properties. Let's analyze the problem from a bitwise perspective.

Instead of summing the XOR totals directly, let's consider the contribution of each bit position to the final sum. The total sum `S` can be expressed as `S = Σ (C_k * 2^k)`, where `C_k` is the count of subsets whose XOR total has the `k`-th bit set to 1.

Let's determine `C_k` for any given bit position `k`:

1.  **Case 1: The `k`-th bit is 0 in ALL numbers in `nums`.**
    If no number in `nums` has its `k`-th bit set, then any XOR combination of these numbers will also have its `k`-th bit as 0. Therefore, `C_k = 0`.

2.  **Case 2: The `k`-th bit is 1 in AT LEAST ONE number in `nums`.**
    Let `x` be an element in `nums` that has its `k`-th bit set. We can partition all `2^n` subsets into two equal halves:
    *   Subsets that *do not* contain `x`. There are `2^(n-1)` such subsets.
    *   Subsets that *do* contain `x`. These are formed by taking each subset `A'` from the first group and adding `x` to it (`A' U {x}`). There are also `2^(n-1)` such subsets.

    Consider a subset `A'` from the first group. Let its XOR total be `X(A')`, and let the `k`-th bit of `X(A')` be `b`.
    Now consider the corresponding subset `A'' = A' U {x}`. Its XOR total is `X(A') ^ x`. Since `x` has its `k`-th bit set to 1, the `k`-th bit of `X(A'')` will be `b ^ 1`.
    This means that for every subset `A'` whose XOR total has its `k`-th bit as `b`, there is a corresponding subset `A''` whose XOR total has its `k`-th bit as `1-b`. This creates a perfect pairing where one has the `k`-th bit 0 and the other has it 1.
    Therefore, exactly half of the `2^n` subsets will have their XOR total with the `k`-th bit set to 1. So, `C_k = 2^n / 2 = 2^(n-1)`.

**Combining these cases:**
The `k`-th bit of the total sum will be `2^(n-1) * 2^k` if at least one number in `nums` has its `k`-th bit set, and `0` otherwise.
The condition "at least one number in `nums` has its `k`-th bit set" is equivalent to checking if the `k`-th bit of the bitwise OR of all numbers in `nums` (`OR_all_nums = nums[0] | nums[1] | ... | nums[n-1]`) is 1.

So, the total sum `S` can be written as:
`S = Σ_{k=0}^{MAX_BITS} ( ( (OR_all_nums >> k) & 1 ) * 2^(n-1) * 2^k )`
We can factor out `2^(n-1)`:
`S = 2^(n-1) * Σ_{k=0}^{MAX_BITS} ( ( (OR_all_nums >> k) & 1 ) * 2^k )`
The summation `Σ_{k=0}^{MAX_BITS} ( ( (OR_all_nums >> k) & 1 ) * 2^k )` is precisely the definition of `OR_all_nums` itself.
Therefore, the final formula is: `Total Sum = OR_all_nums * 2^(n-1)`.

This elegant mathematical property allows for a highly efficient solution.

## Step-by-Step Approach

1.  **Calculate `OR_all_nums`**: Initialize a variable `or_all_nums = 0`. Iterate through each number `num` in the input array `nums` and update `or_all_nums = or_all_nums | num`. After the loop, `or_all_nums` will contain the bitwise OR of all elements in `nums`.
2.  **Get `n`**: Determine the length of the `nums` array, `n = len(nums)`.
3.  **Calculate `2^(n-1)`**: Compute `2` raised to the power of `(n-1)`. This can be done efficiently using a left bit shift: `1 << (n - 1)`.
    *   Note: The problem constraints `1 <= nums.length <= 12` ensure `n >= 1`, so `n-1 >= 0`. `1 << 0` correctly evaluates to `1`.
4.  **Compute Result**: Multiply `or_all_nums` by `2^(n-1)`. This product is the final answer.

## Complexity Analysis

*   **Time Complexity**: `O(N)`
    *   We iterate through the `nums` array once to compute `or_all_nums`. This takes `O(N)` time, where `N` is the length of `nums`.
    *   The remaining operations (getting length, bit shift, multiplication) are `O(1)`.
    *   Therefore, the dominant factor is the single pass through the array, resulting in `O(N)` time complexity.

*   **Space Complexity**: `O(1)`
    *   We only use a few constant-size variables (`or_all_nums`, `n`, `power_of_two_n_minus_1`). No additional data structures are used that scale with input size.

## Common Pitfalls / Mistakes

1.  **Brute-force for large N**: While `O(2^N)` is acceptable for `N=12`, candidates might default to it without realizing a more optimal `O(N)` solution exists. For larger `N` (e.g., `N=20` or `N=30`), the `O(2^N)` approach would time out.
2.  **Off-by-one in `2^(n-1)`**: Forgetting to subtract 1 from `n` when calculating the power of 2, or incorrectly handling `n=1` (where `n-1=0` and `2^0=1`). The bit shift `1 << (n-1)` correctly handles `n-1=0`.
3.  **Misunderstanding XOR properties**: Not recognizing how XOR behaves with respect to individual bits and how it interacts with subset generation. The key insight is that if a bit is present in at least one number, it will be present in exactly half of the subset XOR sums.
4.  **Integer Overflow**: For `N` up to 12 and `nums[i]` up to 1000, the maximum `OR_all_nums` is `2^10 - 1 = 1023` (if all bits up to 9 are set). The maximum `2^(N-1)` is `2^(12-1) = 2^11 = 2048`. The product `1023 * 2048` is approximately `2 * 10^6`, which fits comfortably within standard 32-bit or 64-bit integer types in most languages. However, for larger constraints, this could be a concern.

## Real Interview Follow-Up Questions

1.  **What if `nums` could contain duplicate elements? Does your solution still work?**
    *   **Answer**: Yes, the solution still works. The mathematical property relies on `n` being the count of elements in the array and `OR_all_nums` being the bitwise OR of all elements. When we consider subsets, we treat elements at different indices as distinct, even if their values are the same. For example, if `nums = [1, 1]`, `n=2`, `OR_all_nums = 1 | 1 = 1`. The result is `1 * (1 << (2-1)) = 1 * 2 = 2`. The subsets are `[]` (XOR 0), `[nums[0]]` (XOR 1), `[nums[1]]` (XOR 1), `[nums[0], nums[1]]` (XOR 1^1 = 0). Sum = `0 + 1 + 1 + 0 = 2`. The formula holds.

2.  **What if `nums` could be empty? (i.e., `n=0`)**
    *   **Answer**: The current problem constraints state `1 <= nums.length`, so `nums` is never empty. If it could be empty:
        *   `or_all_nums` would remain `0`.
        *   `n` would be `0`.
        *   `1 << (n-1)` would be `1 << -1`, which is undefined or an error in some languages.
        *   The sum of XOR totals for an empty array should be `0` (only one subset, `[]`, with XOR total `0`).
        *   To handle this, we would add a check: `if n == 0: return 0`. Otherwise, proceed with the formula.

3.  **How would you approach this problem if `N` was much larger, say `N = 10^5`, but `nums[i]` values were still small (e.g., `nums[i] < 1024`)?**
    *   **Answer**: My `O(N)` solution is already optimal for `N = 10^5` as it iterates through `nums` once. The constraint on `nums[i]` values (less than 1024 means they fit in 10 bits) is implicitly handled by the bitwise OR operation, which correctly aggregates the bit information regardless of the magnitude of `nums[i]` (as long as they fit in standard integer types). The formula `OR_all_nums * 2^(N-1)` remains valid and efficient.

4.  **What if `N` was small (e.g., `N <= 20`), but `nums[i]` could be very large (e.g., `10^18`)?**
    *   **Answer**: The `O(N)` solution would still work. `OR_all_nums` would simply be a larger integer (e.g., a 64-bit integer in Python, or `long long` in C++). The bitwise OR operation and multiplication would still be efficient. The number of bits in `OR_all_nums` would be at most 60-64, but the logic remains the same. The `2^(N-1)` factor would also be calculated correctly. The only potential issue would be if the final product exceeds the maximum representable integer type, but for `N=20`, `2^19` is still manageable.

5.  **Can this problem be solved using dynamic programming?**
    *   **Answer**: Yes, the brute-force recursive approach can be thought of as a form of dynamic programming if memoization is applied, though it's not strictly necessary here due to the nature of subset generation.
    *   A DP approach could be `dp[i][xor_val]` representing whether `xor_val` can be formed using a subset of `nums[0...i-1]`. This would be `O(N * MAX_XOR_VALUE)`. `MAX_XOR_VALUE` can be up to `2^10 = 1024` for `nums[i] < 1024`. So `12 * 1024` states.
    *   A more direct DP approach to calculate the sum:
        `dp[i]` could be a list of all possible XOR sums achievable using elements up to index `i-1`.
        `dp[0] = [0]` (for the empty set)
        For `num` in `nums`:
            `new_dp = list(dp)`
            For `prev_xor` in `dp`:
                `new_dp.append(prev_xor ^ num)`
            `dp = new_dp`
        Finally, `sum(dp)` would be the answer.
    *   This DP approach would generate all `2^N` XOR sums and then sum them. Its time complexity would be `O(N * 2^N)` (due to list copying/extending) or `O(2^N)` if managed carefully (e.g., using sets to avoid duplicates if needed, though not strictly required here). Space would be `O(2^N)`. This is less efficient than the `O(N)` mathematical solution.
