# 1475. Final Prices With a Special Discount in a Shop

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)  
**Topics:** Array, Stack, Monotonic Stack

---

## 📝 Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of the `ith` item in a shop.

There is a special discount for items in the shop. If you buy the `ith` item, then you will receive a discount equivalent to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] 

Return an integer array `answer` where `answer[i]` is the final price you will pay for the `ith` item of the shop, considering the special discount.

 
Example 1:

```

**Input:** prices = [8,4,6,2,3]
**Output:** [4,2,4,2,3]
**Explanation:** 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.

```

Example 2:

```

**Input:** prices = [1,2,3,4,5]
**Output:** [1,2,3,4,5]
**Explanation:** In this case, for all items, you will not receive any discount at all.

```

Example 3:

```

**Input:** prices = [10,1,1,6]
**Output:** [9,0,1,6]

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # Using a monotonic increasing stack to track indices of items
        # waiting for their next smaller or equal discount element.
        stack = []
        ans = prices[:]
        
        for i, price in enumerate(prices):
            # Resolve discounts for all pending items in the stack that are >= current price
            while stack and prices[stack[-1]] >= price:
                prev_idx = stack.pop()
                ans[prev_idx] -= price
            
            stack.append(i)
            
        return ans
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to find the first element to the right of index `i` that is less than or equal to `prices[i]`. This is the classic **"Next Smaller (or Equal) Element"** pattern.

While an $O(n^2)$ nested loop approach passes given the small constraints ($n \le 500$), an interviewer at Google or Meta expects the optimal $O(n)$ solution using a **Monotonic Stack**.

By maintaining a stack of indices whose prices are strictly increasing:
1. When we encounter a new price `prices[i]`, we check if it can serve as a discount for any unresolved indices currently in the stack.
2. If `prices[stack[-1]] >= prices[i]`, then index `i` is the closest and first valid discount for `stack[-1]`. We pop `stack[-1]` and apply the discount: `ans[prev_idx] -= prices[i]`.
3. We repeat this check until the condition is no longer met, maintaining the monotonic property, and then push the current index `i` onto the stack.

### Step-by-Step Approach

1. Create a copy of `prices` named `ans` to store the result without mutating the input directly (best practice in production).
2. Initialize an empty stack `stack` to store indices.
3. Iterate through `prices` with index `i` and value `price`:
   - While `stack` is non-empty and `prices[stack[-1]] >= price`:
     - Pop `prev_idx = stack.pop()`.
     - Update `ans[prev_idx] = ans[prev_idx] - price`.
   - Push current index `i` onto `stack`.
4. Return `ans`. Any elements left in the stack have no valid discount, so their initial values remain unchanged.

### Complexity Analysis

- **Time Complexity:** $O(n)$
  Each index is pushed onto the stack exactly once and popped at most once. The `while` loop runs at most $n$ times across the entire execution of the algorithm.
- **Space Complexity:** $O(n)$
  In the worst-case scenario (e.g., strictly increasing array `[1, 2, 3, 4, 5]`), no elements are popped until the end, and the stack will hold $n$ elements. If modifying the input in-place is allowed, auxiliary space is $O(n)$ for the stack.

### Common Pitfalls / Mistakes

1. **Incorrect Monotonicity Condition:** Using `>` instead of `>=`. The problem states the discount applies if `prices[j] <= prices[i]`, meaning equal prices also trigger the discount.
2. **Storing Values Instead of Indices:** Storing values in the stack makes it difficult to update the correct index in the output array, especially when duplicate prices exist. Always store indices.
3. **Overwriting Values Mid-Iteration:** If modifying in-place, updating `prices[prev_idx]` directly could interfere if you are comparing against `prices[stack[-1]]` after modification. Using an independent output array or comparing with an unchanged original reference avoids bugs.

### Real Interview Follow-Up Questions

#### 1. What if the array represents a circular shop (i.e., you can loop around to index 0)?
- **Answer:** We can iterate through the array twice (from index `0` to `2n - 1`), using modulo `i % n` for indexing, but only pushing indices during the first pass (`i < n`) to avoid infinite loops and duplicate processing.

#### 2. How to handle a real-time data stream where prices arrive continuously?
- **Answer:** We cannot determine the discount immediately upon an item's arrival because the discount occurs in the future. We would keep unresolved items in memory (stack) with an expiration timeout/window constraint. When a new transaction arrives, it evaluates and clears applicable items in the stack.

#### 3. How do you scale this for massive data that doesn't fit in memory?
- **Answer:** If partitioned by time/chunks, each chunk can compute discounts locally. Items left unresolved in a chunk's stack can be passed to subsequent chunks as boundary state, processing chunks sequentially or via a map-reduce pipeline.
