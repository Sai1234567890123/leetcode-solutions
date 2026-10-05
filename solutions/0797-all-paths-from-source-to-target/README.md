# 0797. All Paths From Source to Target

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/all-paths-from-source-to-target/](https://leetcode.com/problems/all-paths-from-source-to-target/)  
**Topics:** Backtracking, Depth-First Search, Breadth-First Search, Graph Theory, Directed Acyclic Graph

---

## 📝 Problem Statement

Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in **any order**.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

 
Example 1:

```

**Input:** graph = [[1,2],[3],[3],[]]
**Output:** [[0,1,3],[0,2,3]]
**Explanation:** There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

```

Example 2:

```

**Input:** graph = [[4,3,1],[3,2,4],[3],[4],[]]
**Output:** [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

```

 
**Constraints:**

	- `n == graph.length`

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        """
        Finds all paths from node 0 to node n - 1 in a directed acyclic graph (DAG).
        Uses backtracking / DFS traversal.
        """
        target = len(graph) - 1
        result: list[list[int]] = []
        path: list[int] = [0]

        def dfs(curr: int) -> None:
            # Base case: reached the destination node
            if curr == target:
                # Append a shallow copy of the current valid path
                result.append(list(path))
                return

            # Explore all outgoing edges from the current node
            for neighbor in graph[curr]:
                path.append(neighbor)
                dfs(neighbor)
                # Backtrack to explore alternative branches
                path.pop()

        dfs(0)
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for **all** paths from node `0` to node `n - 1` in a **Directed Acyclic Graph (DAG)**. 

Key observations:
1. **No Cycles:** Because the graph is strictly acyclic (a DAG), we do not need a `visited` set to prevent infinite loops. Every path exploration will naturally terminate.
2. **Exhaustive Enumeration:** The problem explicitly demands all paths, which means we must enumerate every valid route from source to destination.
3. **Backtracking / Depth-First Search (DFS):** DFS is optimal for path enumeration. We maintain a running path stack:
   - When we hit the target node `n - 1`, we record a snapshot of our current path.
   - We recursively visit all neighbors, appending them to our path, and backtrack (pop) upon returning from the recursion.

### Step-by-Step Approach

1. Initialize `target = len(graph) - 1`, `result = []`, and `path = [0]`.
2. Define `dfs(curr)`:
   - If `curr == target`, append a copy of `path` (`list(path)`) to `result`.
   - Iterate over each `neighbor` in `graph[curr]`:
     - Push `neighbor` to `path`.
     - Recurse via `dfs(neighbor)`.
     - Pop `neighbor` from `path` (backtrack).
3. Start the traversal from node `0`: `dfs(0)`.
4. Return `result`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(2^{n - 1} \cdot n)$
  - In the worst case (a dense DAG where each node $i$ has edges to all nodes $j > i$), the number of paths between node $0$ and node $n - 1$ is $2^{n - 2}$.
  - Each path can have length up to $n$. Copying a path of length up to $n$ into the result list takes $\mathcal{O}(n)$ time.
  - Overall time complexity is bounded by $\mathcal{O}(2^n \cdot n)$. Given $n \le 15$, $2^{13} \times 15 \approx 122,880$ operations, which executes in a few milliseconds.
- **Space Complexity:** $\mathcal{O}(n)$ auxiliary space (excluding the output list)
  - The recursion stack depth is at most $n$.
  - The backtracking list `path` holds at most $n$ nodes at any time.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Unnecessary Visited Set:** Many candidates reflexively use a global `visited` set as they would in general graph traversals. In a DAG path-finding problem, a node can—and often must—be visited multiple times across different paths. Maintaining a global visited set produces incomplete results.
2. **Mutating the Path in Results:** Forgetting to clone the path when appending to `result` (e.g., doing `result.append(path)` instead of `result.append(list(path))` or `result.append(path[:])`). This leads to a list of empty lists or references to the final state of `path`.
3. **Memoization / DP Pitfall:** While memoization (e.g., caching all subpaths from node $u$ to $n-1$) is possible, in the worst case where every path is unique, memoization does not reduce the asymptotic complexity and adds overhead due to path concatenation and memory consumption. Simple DFS with backtracking is more memory-efficient.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the graph contains cycles (not a DAG)?
- **Answer:** We would need cycle detection. We can maintain a local `visited` set (or pass a set representing nodes in the current path). When visiting `neighbor`, if `neighbor` is already in the current recursion stack / set, we prune that branch to avoid infinite loops. We remove `neighbor` from the set when backtracking.

#### 2. What if $n$ is very large (e.g., $n = 10^5$), but we only need to count the number of paths instead of listing them?
- **Answer:** If we only need the *count* of paths, we can use **Dynamic Programming with Topological Sort**:
  $$\text{dp}[u] = \sum_{v \in \text{graph}[u]} \text{dp}[v]$$
  with base case $\text{dp}[n - 1] = 1$. This reduces the time complexity from exponential $\mathcal{O}(2^n \cdot n)$ to linear $\mathcal{O}(V + E)$.

#### 3. What if the output cannot fit in memory (e.g., millions of paths)?
- **Answer:** Instead of accumulating all paths in a list and returning them all at once, implement a Python generator using the `yield` statement. This streams paths one by one to the consumer in $\mathcal{O}(n)$ auxiliary memory.
