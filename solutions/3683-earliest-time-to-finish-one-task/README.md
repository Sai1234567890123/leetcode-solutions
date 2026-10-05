# 3683. Earliest Time to Finish One Task

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/earliest-time-to-finish-one-task/](https://leetcode.com/problems/earliest-time-to-finish-one-task/)  
**Topics:** Array

---

## 📝 Problem Statement

You are given a 2D integer array `tasks` where `tasks[i] = [si, ti]`.

Each `[si, ti]` in `tasks` represents a task with start time `si` that takes `ti` units of time to finish.

Return the earliest time at which at least one task is finished.

 
Example 1:

**Input:** tasks = [[1,6],[2,3]]

**Output:** 5

**Explanation:**

The first task starts at time `t = 1` and finishes at time `1 + 6 = 7`. The second task finishes at time `2 + 3 = 5`. You can finish one task at time 5.

Example 2:

**Input:** tasks = [[100,100],[100,100],[100,100]]

**Output:** 200

**Explanation:**

All three tasks finish at time `100 + 100 = 200`.

 
**Constraints:**

	- `1 i, ti]`

	- `1 i, ti

---

## 💻 Implementation (python3)

```py
class Solution:
    def earliestTime(self, tasks: list[list[int]]) -> int:
        """
        Calculates the earliest completion time among all given tasks.
        
        Each task is represented by [start_time, duration].
        The completion time for a task is start_time + duration.
        """
        # Find the minimum completion time across all tasks
        return min(start + duration for start, duration in tasks)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

For each task $i$, we are given:
- Start time: $s_i$
- Duration: $t_i$

The task finishes when its duration is completed after its start time, meaning the finish time is simply:
$$\text{finish\_time}_i = s_i + t_i$$

To find the earliest time at which *at least one* task is finished, we need to determine the minimum finish time among all tasks in the collection:
$$\text{ans} = \min_{i} (s_i + t_i)$$

### Step-by-Step Approach

1. Iterate over each pair `[start, duration]` in `tasks`.
2. Compute the end time for each: `start + duration`.
3. Track and return the minimum end time found across all tasks.
4. In Python, this can be concisely and idiomatically written using a generator expression inside `min(...)`, which consumes $O(1)$ auxiliary space.

### Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the number of tasks in `tasks`. We iterate through the list of tasks once, doing constant $O(1)$ work per task.
- **Space Complexity:** $O(1)$ auxiliary space. We do not allocate any additional data structures; the generator expression evaluates lazily in place.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Confusing Duration with End Time:** Misinterpreting $t_i$ as the completion timestamp rather than the duration, leading to taking $\min(t_i)$ instead of $\min(s_i + t_i)$.
2. **Sorting Overhead:** Sorting the array by $s_i + t_i$, which results in $O(N \log N)$ time complexity when a linear scan $O(N)$ is optimal.
3. **Integer Overflow (in languages like C++ / Java):** While $s_i, t_i$ fit in 32-bit signed integers in standard constraints, in competitive programming or large-scale systems, $s_i + t_i$ might exceed $2^{31} - 1$ if values are up to $2 \times 10^9$. In Python, integers have arbitrary precision, avoiding overflow automatically.

---

### Real Interview Follow-Up Questions

#### 1. What if tasks are streamed (infinite data stream)?
- **Answer:** Maintain a running minimum integer (`earliest_finish = float('inf')`). As each task `(s, t)` arrives, update `earliest_finish = min(earliest_finish, s + t)`. This handles streaming data in $O(1)$ time per event and $O(1)$ total memory.

#### 2. What if tasks can only be executed on a single worker (sequential execution with no overlap)?
- **Answer:** If tasks must be processed one at a time on a single machine, this transforms into a CPU scheduling problem. Depending on whether tasks can be preempted or not:
  - If non-preemptive and we want earliest single completion, the worker would immediately pick the task with the minimum $s_i + t_i$ (or shortest job first at the earliest available time).
  - If scheduling all tasks, Shortest Remaining Time First (SRTF) or Earliest Deadline First (EDF) with a priority queue would be considered.

#### 3. What if we want to find the earliest time when $K$ tasks are finished?
- **Answer:** 
  - Instead of finding the absolute minimum, we need the $k$-th smallest finish time.
  - For small $k$ or streaming, use a max-heap of size $k$ with $O(N \log k)$ time.
  - In an offline batch setting, use QuickSelect (e.g., `introselect` / `std::nth_element`) to find the $k$-th smallest value in $O(N)$ average time and $O(1)$ auxiliary space.
