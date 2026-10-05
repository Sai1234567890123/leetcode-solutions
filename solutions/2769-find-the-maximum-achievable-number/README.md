# 2769. Find the Maximum Achievable Number

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-the-maximum-achievable-number/](https://leetcode.com/problems/find-the-maximum-achievable-number/)  
**Topics:** Math

---

## 📝 Problem Statement

Given two integers, `num` and `t`. A **number **`x`** **is** achievable** if it can become equal to `num` after applying the following operation **at most** `t` times:

	- Increase or decrease `x` by `1`, and *simultaneously* increase or decrease `num` by `1`.

Return the **maximum **possible value of `x`.

 
Example 1:

**Input:** num = 4, t = 1

**Output:** 6

**Explanation:**

Apply the following operation once to make the maximum achievable number equal to `num`:

	- Decrease the maximum achievable number by 1, and increase `num` by 1.

Example 2:

**Input:** num = 3, t = 2

**Output:** 7

**Explanation:**

Apply the following operation twice to make the maximum achievable number equal to `num`:

	- Decrease the maximum achievable number by 1, and increase `num` by 1.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # The problem asks for the maximum possible initial value 'x' such that 'x' can become equal to
        # the given 'num' after applying a specific operation at most 't' times.

        # Let the initial value we are looking for be `x_initial`.
        # Let the given number be `num_initial`.
        # After some operations, `x_initial` becomes `x_final` and `num_initial` becomes `num_final`.
        # We want `x_final = num_final`.

        # Let's analyze the effect of the operation on the difference `x - num`.
        # The operation is: "Increase or decrease `x` by `1`, and *simultaneously* increase or decrease `num` by `1`."
        # There are four possible ways to apply this operation:

        # 1. `x` increases by 1, `num` increases by 1:
        #    - `x` becomes `x + 1`
        #    - `num` becomes `num + 1`
        #    - Effect on `x - num`: `(x + 1) - (num + 1) = x - num`. The difference remains unchanged.

        # 2. `x` decreases by 1, `num` decreases by 1:
        #    - `x` becomes `x - 1`
        #    - `num` becomes `num - 1`
        #    - Effect on `x - num`: `(x - 1) - (num - 1) = x - num`. The difference remains unchanged.

        # 3. `x` increases by 1, `num` decreases by 1:
        #    - `x` becomes `x + 1`
        #    - `num` becomes `num - 1`
        #    - Effect on `x - num`: `(x + 1) - (num - 1) = x - num + 2`. The difference increases by 2.

        # 4. `x` decreases by 1, `num` increases by 1:
        #    - `x` becomes `x - 1`
        #    - `num` becomes `num + 1`
        #    - Effect on `x - num`: `(x - 1) - (num + 1) = x - num - 2`. The difference decreases by 2.

        # Our goal is to make `x_final = num_final`, which means `x_final - num_final = 0`.
        # Let the initial difference be `D = x_initial - num_initial`.
        # We want to change this difference `D` to `0` using at most `t` operations.

        # To find the *maximum* possible `x_initial`, we want `x_initial` to be as large as possible
        # relative to `num_initial`. This implies `x_initial - num_initial` (i.e., `D`) should be
        # a positive value that we then reduce to zero.

        # If `D > 0`, we need to decrease the difference by `D`.
        # The most efficient way to decrease the difference is using operation type 4, which reduces `x - num` by 2.
        # Each such operation counts as one of the `t` allowed operations.
        # To reduce the difference `D` to `0`, we need `D / 2` operations of type 4.
        # (Note: `D` must be an even number for this to be possible, as each operation changes the difference by an even amount.
        # If `x_initial - num_initial` is odd, it can never become 0. However, our final answer will always result in an even difference.)

        # The number of operations used must be at most `t`.
        # So, `D / 2 <= t`.
        # This implies `D <= 2 * t`.

        # To maximize `x_initial`, we should choose the maximum possible value for `D`.
        # The maximum `D` is `2 * t`.
        # Substituting `D = x_initial - num_initial`:
        # `x_initial - num_initial = 2 * t`
        # `x_initial = num_initial + 2 * t`

        # Let's verify this with an example: `num = 4, t = 1`.
        # According to the formula, `x_initial = 4 + 2 * 1 = 6`.
        # Initial state: `x = 6`, `num = 4`. Difference `x - num = 2`.
        # We need to reduce the difference by 2. This requires `2/2 = 1` operation of type 4.
        # Apply operation type 4 once:
        # `x` becomes `6 - 1 = 5`
        # `num` becomes `4 + 1 = 5`
        # Now `x = 5` and `num = 5`. They are equal.
        # We used 1 operation, which is `<= t` (1 <= 1). This works.

        # The maximum achievable `x` is `num + 2 * t`.
        return num + 2 * t
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The core of this problem lies in understanding how the given operation affects the relationship between `x` and `num`. Specifically, we should look at the difference `x - num`.

Let's analyze the four possible outcomes of the operation: "Increase or decrease `x` by `1`, and *simultaneously* increase or decrease `num` by `1`."

1.  **`x` increases by 1, `num` increases by 1:**
    *   New `x`: `x + 1`
    *   New `num`: `num + 1`
    *   New difference `(x + 1) - (num + 1) = x - num`. The difference remains **unchanged**.

2.  **`x` decreases by 1, `num` decreases by 1:**
    *   New `x`: `x - 1`
    *   New `num`: `num - 1`
    *   New difference `(x - 1) - (num - 1) = x - num`. The difference remains **unchanged**.

3.  **`x` increases by 1, `num` decreases by 1:**
    *   New `x`: `x + 1`
    *   New `num`: `num - 1`
    *   New difference `(x + 1) - (num - 1) = x - num + 2`. The difference **increases by 2**.

4.  **`x` decreases by 1, `num` increases by 1:**
    *   New `x`: `x - 1`
    *   New `num`: `num + 1`
    *   New difference `(x - 1) - (num + 1) = x - num - 2`. The difference **decreases by 2**.

Our goal is to find the maximum initial `x` (let's call it `x_initial`) such that it can become equal to the given `num` (let's call it `num_initial`) after at most `t` operations. This means we want `x_final = num_final`, or `x_final - num_final = 0`.

To maximize `x_initial`, we want `x_initial` to be as large as possible relative to `num_initial`. This implies that `x_initial - num_initial` should be a positive value. Let `D = x_initial - num_initial`. We need to reduce this positive difference `D` to `0`.

The operations that change the difference are types 3 and 4. Since we want to reduce a positive difference `D`, we should use operation type 4, which decreases the difference by 2. Each application of operation type 4 counts as one operation.

If we need to reduce the difference by `D`, and each operation reduces it by 2, we will need `D / 2` operations.
The problem states we can use "at most `t` times" these operations.
Therefore, `D / 2 <= t`.
Multiplying by 2, we get `D <= 2 * t`.

To find the *maximum* `x_initial`, we should choose the maximum possible value for `D`, which is `2 * t`.
Substituting `D = x_initial - num_initial`:
`x_initial - num_initial = 2 * t`
Solving for `x_initial`:
`x_initial = num_initial + 2 * t`

This `x_initial` is achievable:
Start with `x = num_initial + 2 * t` and `num = num_initial`.
Apply operation type 4 (`x` decreases by 1, `num` increases by 1) exactly `t` times.
After `t` operations:
*   `x` becomes `(num_initial + 2 * t) - t = num_initial + t`
*   `num` becomes `num_initial + t`
At this point, `x` and `num` are equal (`num_initial + t`), and we have used exactly `t` operations, satisfying the "at most `t` times" condition.

Thus, the maximum achievable `x` is `num + 2 * t`.

## Step-by-Step Approach

1.  Understand the problem: Find the maximum `x` that can become equal to `num` using at most `t` operations.
2.  Analyze the operation's effect on the difference `x - num`.
    *   Operations (`x+1, num+1`) and (`x-1, num-1`) leave `x - num` unchanged.
    *   Operation (`x+1, num-1`) increases `x - num` by 2.
    *   Operation (`x-1, num+1`) decreases `x - num` by 2.
3.  To make `x` equal to `num`, the final difference `x - num` must be 0.
4.  To maximize the initial `x`, we want `x_initial` to be as large as possible relative to `num_initial`. This means `x_initial - num_initial` should be a positive value.
5.  Let `D = x_initial - num_initial`. We need to reduce this difference `D` to 0.
6.  The most efficient way to reduce a positive difference is by using the operation that decreases `x - num` by 2 (i.e., `x` decreases by 1, `num` increases by 1).
7.  Each such operation reduces the difference by 2. To reduce `D` to 0, we need `D / 2` operations.
8.  The total number of operations must be at most `t`. So, `D / 2 <= t`.
9.  This implies `D <= 2 * t`.
10. To maximize `x_initial`, we choose the maximum possible `D`, which is `2 * t`.
11. Substitute `D = x_initial - num_initial` back: `x_initial - num_initial = 2 * t`.
12. Solve for `x_initial`: `x_initial = num_initial + 2 * t`.
13. Return `num + 2 * t`.

## Complexity Analysis

*   **Time Complexity:** O(1)
    The solution involves a single arithmetic calculation (`num + 2 * t`). This takes constant time regardless of the input values.

*   **Space Complexity:** O(1)
    The solution uses a constant amount of memory to store `num`, `t`, and the result. No additional data structures are allocated.

## Common Pitfalls / Mistakes

1.  **Misinterpreting the "simultaneously" clause:** Some candidates might incorrectly assume that `x` and `num` can be increased/decreased independently. The problem explicitly states they change *simultaneously*, meaning one operation affects both.
2.  **Not focusing on the difference `x - num`:** The key insight is how the difference between `x` and `num` changes. Without this, one might try to track `x` and `num` separately, leading to a more complex and potentially incorrect approach.
3.  **Trying to simulate:** For small `t`, one might be tempted to simulate the operations. However, this is inefficient and unnecessary. The algebraic approach based on the difference is much more robust and optimal.
4.  **Incorrectly maximizing `x`:** A candidate might think to maximize `x` by always increasing it (e.g., using `x+1, num-1` operations). However, this also changes `num`, and the goal is for `x` to *equal* `num`, not just to make `x` as large as possible in isolation. The maximum `x_initial` is achieved by setting it as far above `num_initial` as possible while still being able to close the gap within `t` operations.

## Real Interview Follow-Up Questions

1.  **What if we wanted to find the *minimum* achievable `x`?**
    *   **Answer:** To find the minimum `x_initial`, we would want `x_initial - num_initial` (our `D`) to be as negative as possible. This means `x_initial` should be as far *below* `num_initial` as possible.
    *   If `D < 0`, we need to increase the difference to 0. The most efficient way to increase the difference is using operation type 3 (`x` increases by 1, `num` decreases by 1), which increases `x - num` by 2.
    *   To increase the difference by `|D|` (since `D` is negative, `|D| = -D`), we need `|D| / 2` operations.
    *   So, `|D| / 2 <= t`, which means `-D / 2 <= t`, or `-D <= 2t`.
    *   To minimize `x_initial`, we choose the most negative `D`, which is `-2t`.
    *   Therefore, `x_initial - num_initial = -2t`, leading to `x_initial = num_initial - 2t`.

2.  **What if the operation was "increase `x` by 1 OR increase `num` by 1 (but not both), and decrease the other by 1"?**
    *   **Answer:** This changes the problem significantly. If it's "increase `x` by 1 and decrease `num` by 1" OR "increase `num` by 1 and decrease `x` by 1", then it's the same as our types 3 and 4.
    *   If it means we can choose to change *only one* of them, say `x` by `+1` or `-1`, and `num` by `+1` or `-1` independently, then the problem becomes different. For example, if we can just change `x` by `+1` and `num` stays the same, then `x - num` changes by `+1`. If we can change `x` by `+1` and `num` by `+1`, then `x - num` is unchanged. The problem statement's "simultaneously" is crucial. If it were independent, the problem would be about minimizing `|x_initial - num_initial|` by `t` operations, where each operation can change `x` or `num` by 1. This would be `num + t` or `num - t` depending on the goal. But the original problem is clear about simultaneous change.

3.  **What if `t` could be very large (e.g., `10^18`)? Would your solution still work?**
    *   **Answer:** Yes, the solution `num + 2 * t` is O(1) and involves basic arithmetic. Python integers handle arbitrary size, so `num + 2 * t` would work even for `t = 10^18` without overflow, assuming `num` also fits. This highlights the robustness of the algebraic approach over simulation.

4.  **Could there be any floating-point numbers involved, or are `num` and `t` always integers?**
    *   **Answer:** The problem constraints specify `num` and `t` are integers. The operations also involve changes by `1`, so all values of `x` and `num` will remain integers. Our analysis of `D/2` implicitly assumes `D` is even, which is consistent because `2*t` is always even. If `x_initial - num_initial` were odd, it would be impossible to make it 0 using operations that change the difference by 2. However, since we are constructing the maximum `x_initial`, and `num + 2t - num = 2t` (an even number), this is not an issue.

5.  **What if `num` could be negative?**
    *   **Answer:** The problem constraints state `1 <= num, t <= 100`, so `num` is always positive. If `num` could be negative, the logic `num + 2 * t` would still hold. The difference `x - num` would still be an integer, and the operations would affect it in the same way. The maximum achievable `x` would simply be `num + 2 * t`, which could be positive or negative depending on `num` and `t`.
