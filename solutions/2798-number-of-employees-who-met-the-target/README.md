# 2798. Number of Employees Who Met the Target

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/number-of-employees-who-met-the-target/](https://leetcode.com/problems/number-of-employees-who-met-the-target/)  
**Topics:** Array

---

## 📝 Problem Statement

There are `n` employees in a company, numbered from `0` to `n - 1`. Each employee `i` has worked for `hours[i]` hours in the company.

The company requires each employee to work for **at least** `target` hours.

You are given a **0-indexed** array of non-negative integers `hours` of length `n` and a non-negative integer `target`.

Return *the integer denoting the number of employees who worked at least* `target` *hours*.

 
Example 1:

```

**Input:** hours = [0,1,2,3,4], target = 2
**Output:** 3
**Explanation:** The company wants each employee to work for at least 2 hours.
- Employee 0 worked for 0 hours and didn't meet the target.
- Employee 1 worked for 1 hours and didn't meet the target.
- Employee 2 worked for 2 hours and met the target.
- Employee 3 worked for 3 hours and met the target.
- Employee 4 worked for 4 hours and met the target.
There are 3 employees who met the target.

```

Example 2:

```

**Input:** hours = [5,1,4,2,2], target = 6
**Output:** 0
**Explanation:** The company wants each employee to work for at least 6 hours.
There are 0 employees who met the target.

```

 
**Constraints:**

	- `1 5`

---

## 💻 Implementation (python3)

```py
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        """
        Counts the number of employees who worked at least `target` hours.
        
        Uses a generator expression with sum() to achieve O(n) time and O(1) auxiliary space.
        """
        return sum(1 for h in hours if h >= target)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the count of employees whose logged hours meet or exceed a specific threshold (`target`). 

Since the array `hours` is unsorted and each element can independently satisfy or fail the condition, every element must be inspected at least once. A linear scan counting elements where `hours[i] >= target` is theoretically optimal.

### Step-by-Step Approach

1. Iterate through each employee's worked hours `h` in the `hours` array.
2. Check whether `h >= target`.
3. Increment our count by `1` for every employee that satisfies this condition.
4. Using Python's `sum(1 for h in hours if h >= target)` streams elements through a generator expression, keeping memory overhead strictly $O(1)$ without allocating intermediate lists.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the number of employees (length of `hours`). We make a single pass through the array.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. No additional data structures are created; elements are processed via an iterator.

---

### Common Pitfalls / Mistakes

1. **Strict Inequality vs. Inclusive Inequality:** The problem specifies "at least `target` hours", which means `hours[i] >= target`, not `hours[i] > target`.
2. **Unnecessary Memory Allocation:** Using list comprehensions like `len([h for h in hours if h >= target])` or `sum([h >= target for h in hours])` allocates an $\mathcal{O}(n)$ intermediate list in memory. Using a generator expression or a simple `for` loop avoids this.
3. **Sorting Overhead:** Sorting the array first takes $\mathcal{O}(n \log n)$ time, which is suboptimal compared to a direct linear scan $\mathcal{O}(n)$.

---

### Real Interview Follow-Up Questions

#### 1. What if the `hours` array is already sorted?
- **Answer:** If `hours` is sorted in ascending order, we can use binary search (`bisect_left` in Python) to find the first index where `hours[i] >= target`.
- **Complexity:** Reduces time complexity to $\mathcal{O}(\log n)$ and auxiliary space remains $\mathcal{O}(1)$.
- **Code snippet:**
  ```python
  import bisect

  idx = bisect.bisect_left(hours, target)
  return len(hours) - idx
```

#### 2. How would you handle this in a real-time streaming context (e.g., millions of events per second)?
- **Answer:** 
  - If the query is dynamic (different `target` values requested frequently), we can maintain an approximate data structure like a **t-digest** or a **Count-Min Sketch / Histogram** of hour buckets (since hours are bounded, e.g., 0 to 168 hours/week).
  - If `target` is static, we can simply maintain a running counter that increments whenever an incoming stream item $\ge target$.

#### 3. How would you scale this for distributed datasets (e.g., billions of records across multiple machines)?
- **Answer:** Use a MapReduce paradigm:
  - **Map:** Each worker partition processes a chunk of `hours` and counts local matches (`count_local = sum(1 for h in chunk if h >= target)`).
  - **Reduce:** The master node aggregates the partial counts by summing them up.
