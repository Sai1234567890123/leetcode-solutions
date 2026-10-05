# 1769. Minimum Number of Operations to Move All Balls to Each Box

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/)  
**Topics:** Array, String, Prefix Sum

---

## 📝 Problem Statement

You have `n` boxes. You are given a binary string `boxes` of length `n`, where `boxes[i]` is `'0'` if the `ith` box is **empty**, and `'1'` if it contains **one** ball.

In one operation, you can move **one** ball from a box to an adjacent box. Box `i` is adjacent to box `j` if `abs(i - j) == 1`. Note that after doing so, there may be more than one ball in some boxes.

Return an array `answer` of size `n`, where `answer[i]` is the **minimum** number of operations needed to move all the balls to the `ith` box.

Each `answer[i]` is calculated considering the **initial** state of the boxes.

 
Example 1:

```

**Input:** boxes = "110"
**Output:** [1,1,3]
**Explanation:** The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

```

Example 2:

```

**Input:** boxes = "001011"
**Output:** [11,8,5,4,3,4]
```

 
**Constraints:**

	- `n == boxes.length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        ans = [0] * n
        
        # Pass 1: Left to right
        # Accumulate operations needed to bring all balls to the left of i into box i
        balls_count = 0
        running_ops = 0
        for i in range(n):
            ans[i] += running_ops
            balls_count += int(boxes[i])
            running_ops += balls_count
            
        # Pass 2: Right to left
        # Accumulate operations needed to bring all balls to the right of i into box i
        balls_count = 0
        running_ops = 0
        for i in range(n - 1, -1, -1):
            ans[i] += running_ops
            balls_count += int(boxes[i])
            running_ops += balls_count
            
        return ans
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for each index `i` to compute:
$$\text{answer}[i] = \sum_{j=0, \text{boxes}[j] == '1'}^{n-1} |i - j|$$

A brute-force solution checks every pair $(i, j)$, resulting in an $O(n^2)$ time complexity. While $n \le 2000$ permits $O(n^2)$, this is suboptimal and will not pass interview standards for scalability.

To optimize to $O(n)$, we decompose $|i - j|$ into:
1. Balls to the left of $i$ ($j < i$): contribution is $(i - j)$.
2. Balls to the right of $i$ ($j > i$): contribution is $(j - i)$.

Notice that as we transition from index $i - 1$ to $i$:
- Every ball located at index $< i$ must now travel $1$ additional step.
- If we have seen `balls_count` balls to the left of index $i$, the operations required increase by `balls_count`.

Thus, we can compute the total distance in two linear passes:
1. **Left-to-Right pass**: Compute the cost of moving all balls to the left of $i$ into $i$.
2. **Right-to-Left pass**: Compute the cost of moving all balls to the right of $i$ into $i$ and add it to `ans[i]`.

### Step-by-Step Approach

1. Initialize an array `ans` of length $n$ with zeros.
2. Initialize `balls_count = 0` and `running_ops = 0`.
3. Iterate from $i = 0$ to $n - 1$:
   - Add `running_ops` to `ans[i]`.
   - If `boxes[i] == '1'`, increment `balls_count`.
   - Increment `running_ops += balls_count` for the next position.
4. Reset `balls_count = 0` and `running_ops = 0`.
5. Iterate backward from $i = n - 1$ down to $0$:
   - Add `running_ops` to `ans[i]`.
   - If `boxes[i] == '1'`, increment `balls_count`.
   - Increment `running_ops += balls_count` for the next position.
6. Return `ans`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$. We perform exactly two linear sweeps across the string of length $n$. Each step performs $\mathcal{O}(1)$ arithmetic operations.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. Excluding the output array `ans` of size $n$ required by the problem specification, we only use a few integer variables (`balls_count`, `running_ops`, `n`).

---

### Common Pitfalls / Mistakes Candidates Make

1. **Settling for $O(n^2)$:** Candidates frequently see the constraint $n \le 2000$ and submit a nested loop, failing to recognize the prefix/suffix cumulative nature of the problem.
2. **Off-by-One Accumulation:** Adding the current ball into `running_ops` before adding `running_ops` to `ans[i]`. A ball at index $i$ requires $0$ operations to move to index $i$; its distance only increases when moving to index $i + 1$.
3. **Extra Memory Allocations:** Creating separate `left_ops` and `right_ops` arrays of size $n$, using $\mathcal{O}(n)$ auxiliary space when the computation can be performed in-place directly on the return array.

---

### Real Interview Follow-Up Questions

#### 1. What if each box can contain multiple balls (e.g., an array of integers `boxes` where `boxes[i] >= 0`)?
**Answer:** The exact same algorithm applies! Instead of `balls_count += int(boxes[i])`, we do `balls_count += boxes[i]`. The time complexity remains $\mathcal{O}(n)$ and space complexity $\mathcal{O}(1)$.

#### 2. What if the array is circular (i.e., box $0$ and box $n-1$ are adjacent)?
**Answer:** In a circular array, distance between $i$ and $j$ is $\min(|i - j|, n - |i - j|)$.
- Compute the total number of operations for index $0$ initially.
- As the target shifts from $i$ to $(i + 1) \pmod n$, balls in the "closer via right" half shift by $-1$, while balls in the "closer via left" half shift by $+1$.
- We can maintain a sliding window of size $\lfloor n / 2 \rfloor$ containing the balls that become closer/further and update the answer in $\mathcal{O}(1)$ per box, yielding an overall $\mathcal{O}(n)$ solution.

#### 3. How would you handle a sparse input where $n = 10^9$, but there are only $k \le 10^5$ balls?
**Answer:** 
- Instead of iterating through all $n$ coordinates, store the sorted positions of the $k$ balls $p_0, p_1, \dots, p_{k-1}$ and prefix sums of positions.
- For any query box $x$, use binary search (`bisect`) to find the number of balls to the left and right.
- With prefix sums, evaluate $\sum_{p_j < x} (x - p_j) + \sum_{p_j \ge x} (p_j - x)$ in $\mathcal{O}(1)$ per query after an $\mathcal{O}(k \log k)$ initial sort.
