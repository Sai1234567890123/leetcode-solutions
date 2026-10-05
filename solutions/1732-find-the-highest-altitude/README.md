# 1732. Find the Highest Altitude

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-the-highest-altitude/](https://leetcode.com/problems/find-the-highest-altitude/)  
**Topics:** Array, Prefix Sum

---

## 📝 Problem Statement

There is a biker going on a road trip. The road trip consists of `n + 1` points at various altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the **net gain in altitude** between points `i`​​​​​​ and `i + 1` for all (`0 

 
Example 1:

```

**Input:** gain = [-5,1,5,0,-7]
**Output:** 1
**Explanation:** The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

```

Example 2:

```

**Input:** gain = [-4,-3,-2,-1,4,3,2]
**Output:** 0
**Explanation:** The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

```

 
**Constraints:**

	- `n == gain.length`

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """
        Finds the highest altitude reached during the trip.
        The trip starts at altitude 0.
        """
        current_altitude = 0
        max_altitude = 0

        for net_change in gain:
            current_altitude += net_change
            if current_altitude > max_altitude:
                max_altitude = current_altitude

        return max_altitude
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the peak altitude reached on a journey that starts at altitude $0$. We are given an array of differences between consecutive altitudes (gains/drops). 

Mathematically:
- $\text{Altitude}_0 = 0$
- $\text{Altitude}_i = \text{Altitude}_{i-1} + \text{gain}[i-1] = \sum_{j=0}^{i-1} \text{gain}[j]$

This translates directly to finding the maximum prefix sum of the `gain` array, with the initial sum being $0$. Rather than constructing an explicit prefix sum array, which takes $O(n)$ extra memory, we can maintain a running sum of the current altitude and track the maximum altitude encountered so far.

### Step-by-Step Approach

1. Initialize `current_altitude = 0` to represent the starting point (point 0).
2. Initialize `max_altitude = 0` because point 0 is a valid point and its altitude is 0. If all gains are negative, the highest altitude remains 0.
3. Iterate through each `net_change` in `gain`:
   - Add `net_change` to `current_altitude`.
   - Update `max_altitude = max(max_altitude, current_altitude)`.
4. Return `max_altitude`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `gain`. We perform a single linear scan over the array with constant time $\mathcal{O}(1)$ operations at each step.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. We only use two scalar variables (`current_altitude` and `max_altitude`) regardless of the input size.

### Common Pitfalls / Mistakes Candidates Make

1. **Forgetting the Starting Altitude (0):**
   Initializing `max_altitude` to `gain[0]` or `float('-inf')` instead of `0`. If all altitude gains are negative (e.g., `gain = [-4, -3, -2]`), the maximum altitude is $0$ at the starting position, not $-4$.
2. **Unnecessary Memory Allocation:**
   Constructing the entire prefix sum array or using `itertools.accumulate` and materializing a full list. While still asymptotically optimal in time, it consumes unnecessary $\mathcal{O}(n)$ memory.

### Real Interview Follow-Up Questions

#### 1. What if the input is a continuous data stream that does not fit in memory?
**Answer:** The current approach already processes the data as a single-pass stream. We only need the current altitude and the max altitude in memory. We can easily adapt this to process chunks from an iterator/generator or network socket with $\mathcal{O}(1)$ memory.

#### 2. What if values are extremely large and could cause integer overflow?
**Answer:** In Python 3, integers have arbitrary precision and do not overflow natively. In lower-level languages like C++ or Java:
- If `gain[i]` fits in a 32-bit integer, summing $n$ elements could exceed `INT_MAX` (e.g., $10^5$ elements each equal to $10^9$).
- We would need to use 64-bit integers (`long long` in C++, `long` in Java) or BigInteger primitives if the constraints exceed $2^{63} - 1$.

#### 3. How would you solve this concurrently / on multiple machines (MapReduce / Parallel Prefix Sum)?
**Answer:** This can be parallelized using the parallel prefix sum (scan) algorithm:
1. Divide the array into $P$ chunks across $P$ workers.
2. Each worker computes the total sum of its chunk and the maximum prefix sum within its chunk.
3. A master coordinator collects the total sums, computes global offset bases for each chunk, and determines the global maximum by adjusting each chunk's local maximum with the offset.
