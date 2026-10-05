# 1282. Group the People Given the Group Size They Belong To

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/)  
**Topics:** Array, Hash Table, Greedy

---

## 📝 Problem Statement

There are `n` people that are split into some unknown number of groups. Each person is labeled with a **unique ID** from `0` to `n - 1`.

You are given an integer array `groupSizes`, where `groupSizes[i]` is the size of the group that person `i` is in. For example, if `groupSizes[1] = 3`, then person `1` must be in a group of size `3`.

Return *a list of groups such that each person `i` is in a group of size `groupSizes[i]`*.

Each person should appear in **exactly one group**, and every person must be in a group. If there are multiple answers, **return any of them**. It is **guaranteed** that there will be **at least one** valid solution for the given input.

 
Example 1:

```

**Input:** groupSizes = [3,3,3,3,3,1,3]
**Output:** [[5],[0,1,2],[3,4,6]]
**Explanation:** 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

```

Example 2:

```

**Input:** groupSizes = [2,1,3,3,3,2]
**Output:** [[1],[0,5],[2,3,4]]

```

 
**Constraints:**

	- `groupSizes.length == n`

	- `1

---

## 💻 Implementation (python3)

```py
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        result = []
        # Maps group_size -> list of candidate person IDs currently accumulating
        buckets = defaultdict(list)
        
        for person_id, size in enumerate(groupSizes):
            buckets[size].append(person_id)
            # Once the bucket reaches its required capacity, flush it into result
            if len(buckets[size]) == size:
                result.append(buckets[size])
                buckets[size] = []
                
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires us to assemble groups of specific sizes such that every person $i$ is placed into a group of size `groupSizes[i]`. We are guaranteed that a valid partition always exists.

Because the identity of the people within the same group size does not matter, a greedy approach works optimally:
1. Whenever we encounter a person who needs a group of size $S$, we place them in a staging area (bucket) reserved for groups of size $S$.
2. As soon as the staging bucket reaches size $S$, we know this group is complete.
3. We move this completed group into our final answer and reset the staging bucket for future people who also require size $S$.

### Step-by-Step Approach

1. Initialize an empty list `result` to hold the completed groups.
2. Use a hash map (`defaultdict(list)`) named `buckets` where each key is a `size` and the value is a list of person IDs currently waiting for a group of that size.
3. Iterate through `groupSizes` using `enumerate` to track both the `person_id` and the required `size`.
4. Append `person_id` to `buckets[size]`.
5. Check if `len(buckets[size]) == size`:
   - If true, append the full group to `result`.
   - Reset `buckets[size] = []` to start accumulating for the next group of the same size.
6. Return `result`.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is the length of `groupSizes`. Each person is added to a bucket once and moved to the final output list once. List append and lookup in the hash map take $O(1)$ amortized time.
- **Space Complexity:** $O(n)$ auxiliary space (excluding the output list). At any given moment, each person ID is stored in either a temporary bucket in `buckets` or directly transferred to `result`. The dictionary stores at most $n$ elements across all buckets at any point.

### Common Pitfalls / Mistakes

1. **Overcomplicating with Sorting:** Sorting the input array takes $O(n \log n)$ time and loses the original indices, requiring extra storage to pair `(size, index)`. Using a hash map achieves $O(n)$ time directly.
2. **Delayed Chunking:** Collecting all IDs for each size first and then slicing them (e.g., `[arr[i:i+s] for i in range(0, len(arr), s)]`) creates unnecessary intermediate lists and passes over the data multiple times, whereas flushing on-the-fly is more memory-efficient.

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input arrives as an infinite stream of `(person_id, group_size)` tuples?
*Answer:* The on-the-fly flushing approach translates directly to streaming. We can maintain the hash map state and emit/yield completed groups as a generator whenever a bucket reaches capacity:
```python
def stream_groups(stream):
    buckets = defaultdict(list)
    for person_id, size in stream:
        buckets[size].append(person_id)
        if len(buckets[size]) == size:
            yield buckets[size]
            buckets[size] = []
```

#### 2. What if memory is constrained and $n$ does not fit in RAM?
*Answer:* We can use an array of fixed-size ring buffers or write directly to an external store or disk partition keyed by `group_size`. Since elements are only flushed in chunks of size $S \le n$, intermediate memory can be kept strictly within $O(\max(S))$ bounded buffer per distinct size.

#### 3. What if a valid solution is NOT guaranteed?
*Answer:* If input validation is needed:
- After processing all elements, check if any bucket in `buckets` is non-empty. If `any(buckets[s] for s in buckets)`, it is impossible to form complete groups, and we should raise an exception or return an empty list / `None`.
- Additionally, ensure that $1 \le \text{groupSize}[i] \le n$ for all $i$.
