# 1979. Find Greatest Common Divisor of Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-greatest-common-divisor-of-array/](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)  
**Topics:** Array, Math, Number Theory, Euclidean Algorithm, Greatest Common Divisor

---

## 📝 Problem Statement

Given an integer array `nums`, return** ***the **greatest common divisor** of the smallest number and largest number in *`nums`.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

 
Example 1:

```

**Input:** nums = [2,5,6,9,10]
**Output:** 2
**Explanation:**
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

```

Example 2:

```

**Input:** nums = [7,5,6,8,3]
**Output:** 1
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

```

Example 3:

```

**Input:** nums = [3,3]
**Output:** 3
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

```

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
import math

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        """
        Finds the GCD of the smallest and largest number in the array.
        Time Complexity: O(N + log(min_val))
        Space Complexity: O(1)
        """
        # Single pass to find the minimum and maximum values
        min_val = float('inf')
        max_val = float('-inf')
        
        for num in nums:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
                
        # Euclidean algorithm to compute gcd(min_val, max_val)
        # We can implement it iteratively to ensure O(1) auxiliary space
        a, b = min_val, max_val
        while b:
            a, b = b, a % b
            
        return a
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the greatest common divisor (GCD) of the smallest and largest numbers present in `nums`. 

This breaks down into two distinct sub-problems:
1. **Find Extrema**: Identify $\min(\text{nums})$ and $\max(\text{nums})$.
2. **Compute GCD**: Calculate $\gcd(\min(\text{nums}), \max(\text{nums}))$.

Finding both the minimum and maximum requires examining each element in `nums` at least once, giving a lower bound of $O(n)$ time. Once the two numbers are identified, the Euclidean algorithm is the gold standard for finding the GCD efficiently in logarithmic time.

### Step-by-Step Approach

1. **Initialize Extrema**: Set `min_val` to $\infty$ and `max_val` to $-\infty$.
2. **Traverse the Array**: In a single pass, update `min_val` and `max_val` for each element in `nums`.
3. **Apply the Euclidean Algorithm**:
   - The Euclidean algorithm is based on the principle that the greatest common divisor of two integers $a$ and $b$ ($a > b$) is the same as the greatest common divisor of $b$ and $a \pmod b$.
   - Iteratively replace $(a, b)$ with $(b, a \pmod b)$ until $b = 0$.
   - When $b = 0$, $a$ is the GCD.

### Complexity Analysis

- **Time Complexity**: $O(n + \log(\min(\text{nums})))$
  - Scanning the array of length $n$ to find the minimum and maximum takes $O(n)$ time.
  - Computing the GCD of two numbers $a$ and $b$ using the Euclidean algorithm takes $O(\log(\min(a, b)))$ steps (by Lamé's Theorem, the number of steps is at most $5 \times \log_{10}(\min(a, b))$).
  - Since $M = \max(\text{nums}) \le 1000$, $\log(M)$ is negligible ($\approx 10$ operations), making the total runtime strictly $O(n)$.
- **Space Complexity**: $O(1)$
  - Only a few variables (`min_val`, `max_val`, `a`, `b`) are used. The iterative Euclidean algorithm does not use call stack memory.

### Common Pitfalls / Mistakes

1. **Sorting the Array**: Running `nums.sort()` to get `nums[0]` and `nums[-1]` takes $O(n \log n)$ time, which is suboptimal compared to a single $O(n)$ pass.
2. **Brute-Force GCD**: Iterating from $\min(\text{nums})$ down to 1 checking for divisibility takes $O(\min(\text{nums}))$ time. While it passes for small constraints ($\le 1000$), it degrades significantly if numbers are large ($10^9$ or $10^{18}$).
3. **Recursion Limit / Stack Overflow**: Implementing the Euclidean algorithm recursively without tail-call optimization could theoretically consume $O(\log(\min(a, b)))$ call stack space. The iterative approach guarantees true $O(1)$ auxiliary space.

### Real Interview Follow-Up Questions

1. **What if the data is a continuous stream and cannot fit in memory?**
   - **Answer**: Maintain two variables `stream_min` and `stream_max`. As each element arrives, update `stream_min = min(stream_min, x)` and `stream_max = max(stream_max, x)`. When the query is requested, compute the GCD of the two tracked variables in $O(\log(\text{stream\_min}))$ time.

2. **Can we optimize the number of comparisons when finding both min and max?**
   - **Answer**: Yes. Comparing elements in pairs reduces the total number of comparisons from $2(n - 1)$ to approximately $3n/2$:
     - Compare `nums[i]` and `nums[i+1]`.
     - Compare the smaller of the two with current `min_val`.
     - Compare the larger of the two with current `max_val`.

3. **What if the numbers can be negative or zero?**
   - **Answer**: 
     - If numbers can be negative, take the absolute value since $\gcd(a, b) = \gcd(|a|, |b|)$.
     - If both are $0$, $\gcd(0, 0)$ is technically undefined (or $0$ depending on conventions). If one is $0$ and the other is non-zero, $\gcd(a, 0) = |a|$. The Euclidean loop `while b: a, b = b, a % b` naturally handles one of them being $0$ if initialized appropriately.
