# 1877. Minimize Maximum Pair Sum in Array

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/)  
**Topics:** Array, Two Pointers, Greedy, Sorting

---

## 📝 Problem Statement

The **pair sum** of a pair `(a,b)` is equal to `a + b`. The **maximum pair sum** is the largest **pair sum** in a list of pairs.

	- For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the **maximum pair sum** would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.

Given an array `nums` of **even** length `n`, pair up the elements of `nums` into `n / 2` pairs such that:

	- Each element of `nums` is in **exactly one** pair, and

	- The **maximum pair sum **is **minimized**.

Return *the minimized **maximum pair sum** after optimally pairing up the elements*.

 
Example 1:

```

**Input:** nums = [3,5,2,3]
**Output:** 7
**Explanation:** The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

```

Example 2:

```

**Input:** nums = [3,5,4,2,4,6]
**Output:** 8
**Explanation:** The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.

```

 
**Constraints:**

	- `n == nums.length`

	- `2 5`

	- `n` is **even**.

	- `1 5`

---

## 💻 Implementation (python3)

```py
class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        """
        Minimizes the maximum pair sum by sorting the array and pairing 
        the i-th smallest element with the i-th largest element.
        """
        nums.sort()
        
        n = len(nums)
        max_pair_sum = 0
        
        # Pair elements from the outer ends towards the center
        for i in range(n // 2):
            current_pair_sum = nums[i] + nums[n - 1 - i]
            if current_pair_sum > max_pair_sum:
                max_pair_sum = current_pair_sum
                
        return max_pair_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

To minimize the maximum pair sum, we want to balance out the values in each pair as much as possible. If we pair a large element with another large element, their sum will be excessively large. Conversely, pairing a small element with another small element leaves the remaining large elements to be paired together, worsening the maximum sum.

The optimal greedy strategy is:
1. Sort the array in non-decreasing order.
2. Pair the smallest element with the largest element, the second-smallest with the second-largest, and so on: $(nums[i], nums[n - 1 - i])$.
3. Track the maximum sum among all these pairs.

**Why does this greedy choice work? (Exchange Argument)**
Consider four sorted elements: $a \le b \le c \le d$.
The possible pairings are:
1. $(a, d)$ and $(b, c) \rightarrow \text{max sum} = \max(a+d, b+c)$
2. $(a, c)$ and $(b, d) \rightarrow \text{max sum} = \max(a+c, b+d) = b+d$ (since $b+d \ge a+c$)
3. $(a, b)$ and $(c, d) \rightarrow \text{max sum} = \max(a+b, c+d) = c+d$ (since $c+d \ge a+b$)

Notice that $b + d \ge a + d$ and $b + d \ge b + c$. Thus, $\max(a+d, b+c) \le b+d$.
Similarly, $c + d \ge a + d$ and $c + d \ge b + c$.
Therefore, pairing $(a, d)$ and $(b, c)$ is guaranteed to produce a maximum pair sum that is less than or equal to any other pairing. By extending this via induction across all $n$ elements, the greedy pairing is strictly optimal.

---

### Step-by-Step Approach

1. **Sort `nums`** in-place in ascending order.
2. **Iterate** with a pointer $i$ from $0$ up to $n / 2 - 1$.
3. At each step, compute the pair sum `nums[i] + nums[n - 1 - i]`.
4. Maintain a running maximum `max_pair_sum`.
5. Return `max_pair_sum`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n \log n)$
  - Sorting $n$ elements takes $\mathcal{O}(n \log n)$ time using Python's Timsort.
  - The subsequent two-pointer scan takes $\mathcal{O}(n)$ time.
  - Overall time complexity is dominated by sorting: $\mathcal{O}(n \log n)$.
  *(Note: If $nums[i]$ is tightly bounded, e.g., $nums[i] \le 10^5$, we can achieve $\mathcal{O}(n + \max(nums))$ using Counting Sort).*

- **Space Complexity:** $\mathcal{O}(n)$ or $\mathcal{O}(1)$
  - In Python, `list.sort()` is implemented using Timsort, which requires up to $\mathcal{O}(n)$ auxiliary space in the worst case.
  - No additional data structures are created, so auxiliary space is $\mathcal{O}(1)$ beyond the sorting overhead.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Trying Dynamic Programming or Backtracking:** Candidates sometimes overcomplicate this problem thinking it is a partition problem (like NP-hard subset-sum variants). Realizing it is an unconstrained pairing problem allows a simple greedy proof.
2. **Off-by-one errors:** Stopping at `n // 2` properly handles all pairs because $n$ is guaranteed to be even. Be careful when indexing `n - 1 - i`.
3. **Overlooking Counting Sort:** When interviewers mention small integer ranges (e.g., $nums[i] \le 10^5$), failure to mention the $\mathcal{O}(n + K)$ counting sort alternative misses a high-signal optimization point.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if $n$ and the values in `nums` are bounded such that $nums[i] \le 10^5$? Can we do better than $\mathcal{O}(n \log n)$?
**Answer:** Yes. We can use **Counting Sort** (or Bucket Sort). We create a frequency array of size $\max(nums) + 1$, count occurrences in $\mathcal{O}(n)$, and use two pointers (`left` and `right`) traversing inward across the frequency buckets to form pairs. This reduces the time complexity to $\mathcal{O}(n + M)$ where $M = \max(nums)$, requiring $\mathcal{O}(M)$ space.

#### 2. How would you handle a massive dataset that cannot fit into memory (External Sorting / Scale)?
**Answer:** If the array is stored across multiple disk blocks or distributed across machines:
- Use **External Merge Sort** to sort the chunks on disk and merge them.
- Once sorted, read from both the beginning (head) and end (tail) of the sorted external file in parallel chunks/streams using two cursors and compute the maximum pair sum in a single streaming pass.

#### 3. What if $n$ is odd and we must leave one element unpaired to minimize the maximum pair sum of the remaining elements?
**Answer:** If one element must be discarded, the problem becomes finding which element $nums[k]$ to drop. Binary searching over the answer or using prefix and suffix paired maximums allows finding the optimal element in $\mathcal{O}(n \log(\max - \min))$ or $\mathcal{O}(n)$ after sorting.
