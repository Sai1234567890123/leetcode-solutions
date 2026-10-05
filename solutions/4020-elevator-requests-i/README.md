# 4020. Elevator Requests I

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/elevator-requests-i/](https://leetcode.com/problems/elevator-requests-i/)  
**Topics:** Array, Simulation

---

## 📝 Problem Statement

You are given an integer `n` denoting the number of floors in a building, where the floors are numbered from 0 to `n - 1`.

You are also given an integer array `requests`, where `requests` represents the sequence of floor requests.

An elevator starts at floor 0 and follows these rules:

	- The elevator moves one floor per second.

	- The elevator serves requests in the given order.

	- If the elevator is already on the requested floor, no movement is needed.

	- After serving a request, the elevator immediately starts moving toward the next request.

Return the **total time** in seconds required to serve all requests.

 
Example 1:

**Input:** n = 5, requests = [2,1,4,3]

**Output:** 7

**Explanation:**

	- `requests[0] = 2`: Moving from floor 0 to floor 2 takes 2 seconds.

	- `requests[1] = 1`: Moving from floor 2 to floor 1 takes 1 second.

	- `requests[2] = 4`: Moving from floor 1 to floor 4 takes 3 seconds.

	- `requests[3] = 3`: Moving from floor 4 to floor 3 takes 1 second.

The total time required is `2 + 1 + 3 + 1 = 7` seconds.

Example 2:

**Input:** n = 3, requests = [2,0,0]

**Output:** 4

**Explanation:**

	- `requests[0] = 2`: Moving from floor 0 to floor 2 takes 2 seconds.

	- `requests[1] = 0`: Moving from floor 2 to floor 0 takes 2 seconds.

	- `requests[2] = 0`: No movement is needed.

The total time required is `2 + 2 + 0 = 4` seconds.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total_time = 0
        current_floor = 0
        
        # Traverse each requested floor in order
        for target_floor in requests:
            # Add time required to travel to the next floor
            total_time += abs(target_floor - current_floor)
            # Update current floor to the new position
            current_floor = target_floor
            
        return total_time
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks us to simulate the movement of an elevator that starts at floor `0` and services floor requests sequentially in the order given by the array `requests`.

Since:
1. The elevator moves at a rate of 1 floor per second, the time taken to move from floor $A$ to floor $B$ is simply the Manhattan distance on a 1D line: $|A - B|$ seconds.
2. The elevator serves requests strictly sequentially.

All we need to do is keep track of the elevator's `current_floor` (initialized to `0`), and for each target floor in `requests`, add `abs(target_floor - current_floor)` to our running total time, and then set `current_floor = target_floor`.

### Step-by-Step Approach
1. Initialize `total_time = 0` and `current_floor = 0`.
2. Iterate through each `target_floor` in the `requests` list:
   - Compute the travel duration: `abs(target_floor - current_floor)`.
   - Add this duration to `total_time`.
   - Update `current_floor` to `target_floor`.
3. Return `total_time`.

### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(m)$, where $m$ is the length of `requests`. We perform a single pass through the array, doing constant-time $\mathcal{O}(1)$ operations per request.
- **Space Complexity:** $\mathcal{O}(1)$, as we only use a couple of scalar variables (`total_time`, `current_floor`).

---

### Common Pitfalls / Mistakes Candidates Make
- **Off-by-one / Initial position error:** Forgetting that the elevator starts at floor `0` rather than at `requests[0]`.
- **Negative time / Directional errors:** Forgetting to use the absolute value `abs(target_floor - current_floor)` when the elevator moves down.
- **Unnecessary state tracking:** Overcomplicating the solution with queue or time simulation tick-by-tick instead of directly accumulating the delta distance.

---

### Real Interview Follow-Up Questions

1. **What if the elevator can batch requests (SCAN / LOOK / Elevator algorithm) instead of serving strictly First-Come, First-Served (FCFS)?**
   - *Answer:* FCFS is often inefficient. In a real operating system or elevator controller, we use algorithms like SCAN (the elevator sweeps all the way in one direction serving requests, then reverses) or LOOK (sweeps until the last request in that direction, then reverses). If we are asked to minimize total time or wait time dynamically, we can use a min-heap or balanced BST to process requests in directional order.

2. **What if requests arrive dynamically with timestamps `(arrival_time, floor)`?**
   - *Answer:* The elevator can idle between requests. If `current_time < arrival_time`, the elevator advances its internal clock to `arrival_time`. The time taken to serve would then be: `current_time = max(current_time, arrival_time) + abs(target_floor - current_floor)`.

3. **What if multiple elevators are available?**
   - *Answer:* This becomes a variant of the multi-agent pathfinding / dispatch problem (often framed as an online scheduling or dynamic programming problem). A greedy heuristic often assigns the request to the elevator that minimizes the incremental arrival/wait time, or uses linear programming for global optimization.
