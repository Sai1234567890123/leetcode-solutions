# 2391. Minimum Amount of Time to Collect Garbage

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/)  
**Topics:** Array, String, Prefix Sum

---

## 📝 Problem Statement

You are given a **0-indexed** array of strings `garbage` where `garbage[i]` represents the assortment of garbage at the `ith` house. `garbage[i]` consists only of the characters `'M'`, `'P'` and `'G'` representing one unit of metal, paper and glass garbage respectively. Picking up **one** unit of any type of garbage takes `1` minute.

You are also given a **0-indexed** integer array `travel` where `travel[i]` is the number of minutes needed to go from house `i` to house `i + 1`.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house `0` and must visit each house **in order**; however, they do **not** need to visit every house.

Only **one** garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks **cannot** do anything.

Return* the **minimum** number of minutes needed to pick up all the garbage.*

 
Example 1:

```

**Input:** garbage = ["G","P","GP","GG"], travel = [2,4,3]
**Output:** 21
**Explanation:**
The paper garbage truck:
1. Travels from house 0 to house 1
2. Collects the paper garbage at house 1
3. Travels from house 1 to house 2
4. Collects the paper garbage at house 2
Altogether, it takes 8 minutes to pick up all the paper garbage.
The glass garbage truck:
1. Collects the glass garbage at house 0
2. Travels from house 0 to house 1
3. Travels from house 1 to house 2
4. Collects the glass garbage at house 2
5. Travels from house 2 to house 3
6. Collects the glass garbage at house 3
Altogether, it takes 13 minutes to pick up all the glass garbage.
Since there is no metal garbage, we do not need to consider the metal garbage truck.
Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.

```

Example 2:

```

**Input:** garbage = ["MMM","PGM","GP"], travel = [3,10]
**Output:** 37
**Explanation:**
The metal garbage truck takes 7 minutes to pick up all the metal garbage.
The paper garbage truck takes 15 minutes to pick up all the paper garbage.
The glass garbage truck takes 15 minutes to pick up all the glass garbage.
It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.

```

 
**Constraints:**

	- `2 5`

	- `garbage[i]` consists of only the letters `'M'`, `'P'`, and `'G'`.

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        total_time = 0
        last_m = last_p = last_g = 0
        
        # 1. Total pickup time is simply the total length of all strings in garbage.
        # 2. Track the farthest house index that contains each type of garbage.
        for i, g in enumerate(garbage):
            total_time += len(g)
            if 'M' in g:
                last_m = i
            if 'P' in g:
                last_p = i
            if 'G' in g:
                last_g = i
                
        # Compute prefix sums of travel times to quickly get travel cost to any house.
        # travel_prefix[i] stores the travel time from house 0 to house i.
        prefix_sum = 0
        travel_prefix = [0] * len(garbage)
        for i in range(len(travel)):
            prefix_sum += travel[i]
            travel_prefix[i + 1] = prefix_sum
            
        # Add travel times for each truck up to its respective last house.
        total_time += travel_prefix[last_m]
        total_time += travel_prefix[last_p]
        total_time += travel_prefix[last_g]
        
        return total_time
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the minimum total time taken by three trucks (Metal, Paper, Glass) to collect all corresponding garbage. Each truck starts at house `0`, travels sequentially house-by-house, and stops once all garbage of its specific type has been collected. Crucially, trucks operate independently in terms of their travel paths, but since only one truck can move at a time, the total time is simply the sum of times spent by each individual truck.

The total time consists of two independent parts:
1. **Garbage Collection Time**: Every single character `'M'`, `'P'`, and `'G'` across all houses takes exactly 1 minute to collect. Thus, the total collection time is simply the sum of lengths of all strings in `garbage`.
2. **Travel Time**: A truck for garbage type $X \in \{'M', 'P', 'G'\}$ must travel from house `0` up to the last house containing garbage of type $X$. It does not need to travel any further. Hence, the travel time for truck $X$ is the sum of travel times from house `0` to house `last_index(X)`.

### Step-by-Step Approach

1. Iterate through `garbage` once:
   - Add the length of `garbage[i]` to `total_time`.
   - Update the last seen index for `'M'`, `'P'`, and `'G'`.
2. Compute a prefix sum array for `travel`. `travel_prefix[i]` will represent the travel time from house `0` to house `i`.
3. Add `travel_prefix[last_m]`, `travel_prefix[last_p]`, and `travel_prefix[last_g]` to `total_time`.
4. Return `total_time`.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N + L)$, where $N$ is the number of houses (`len(garbage)`) and $L$ is the total number of characters across all strings in `garbage` ($\sum |garbage[i]|$). We do a single pass over `garbage` and a single pass over `travel` ($N - 1$ elements).
- **Space Complexity**: $\mathcal{O}(N)$ for the `travel_prefix` array. This can easily be optimized to $\mathcal{O}(1)$ auxiliary space if we accumulate travel times on the fly or mutate in-place, but $\mathcal{O}(N)$ is negligible given constraints ($N \le 10^5$).

### Common Pitfalls / Mistakes Candidates Make

1. **Simulating truck movements step-by-step**: Simulating the movement of trucks house-by-house with conditional logic is overly complex, error-prone, and slow.
2. **Double counting travel**: Candidates often travel back to house `0` after collecting garbage. The problem states trucks do not need to return.
3. **Misinterpreting serialization**: Candidates might overcomplicate the constraint "Only one garbage truck may be used at any given moment." Since time simply accumulates linearly, the order of truck operations does not affect the total duration at all.

### Real Interview Follow-Up Questions

#### 1. What if trucks could operate in parallel?
**Answer**: If all 3 trucks can move simultaneously, the total time would be the completion time of the slowest truck:
$$\max_{T \in \{M, P, G\}} (\text{travel\_time}(T) + \text{pickup\_time}(T))$$
Each truck's time would be computed independently and we would take the maximum instead of the sum.

#### 2. What if houses and roads form an arbitrary tree or graph instead of a straight line?
**Answer**: If the houses form a general tree (e.g., roads form a spanning tree) and trucks must return to house 0:
- This becomes finding the weight of the minimal subtree containing the root (house 0) and all houses with garbage type $X$, multiplied by 2 (for round-trip).
- If trucks do not need to return to house 0, it reduces to $2 \times (\text{subtree weight}) - \text{max path from root to any target node in the subtree}$.

#### 3. How to handle streaming data / very large $N$ where arrays don't fit in memory?
**Answer**: We can solve this with a single pass in reverse or two passes:
- In a forward pass, write travel times to a memory-mapped file or stream.
- Since we only need the total length of all strings and the prefix sums up to the last occurrence of each character, we can maintain the total character count and use a rolling sum of `travel` while updating the running travel cost for each garbage type when encountered.
