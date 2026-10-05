# 1791. Find Center of Star Graph

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-center-of-star-graph/](https://leetcode.com/problems/find-center-of-star-graph/)  
**Topics:** Graph Theory

---

## 📝 Problem Statement

There is an undirected **star** graph consisting of `n` nodes labeled from `1` to `n`. A star graph is a graph where there is one **center** node and **exactly** `n - 1` edges that connect the center node with every other node.

You are given a 2D integer array `edges` where each `edges[i] = [ui, vi]` indicates that there is an edge between the nodes `ui` and `vi`. Return the center of the given star graph.

 
Example 1:

```

**Input:** edges = [[1,2],[2,3],[4,2]]
**Output:** 2
**Explanation:** As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

```

Example 2:

```

**Input:** edges = [[1,2],[5,1],[1,3],[1,4]]
**Output:** 1

```

 
**Constraints:**

	- `3 5`

	- `edges.length == n - 1`

	- `edges[i].length == 2`

	- `1 i, vi i != vi`

	- The given `edges` represent a valid star graph.

---

## 💻 Implementation (python3)

```py
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        """
        Finds the center node of a valid star graph.
        
        Since a star graph's center node must be connected to every other node,
        it must appear in every edge, including the first two edges.
        """
        u1, v1 = edges[0]
        u2, v2 = edges[1]
        
        # The center node must be common to both edges[0] and edges[1].
        if u1 == u2 or u1 == v2:
            return u1
        return v1
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A star graph with $n$ nodes has a single central node with degree $n - 1$, and all other $n - 1$ outer nodes have degree $1$. 

Because the problem guarantees that the input is a valid star graph, the central node must be an endpoint of **every single edge** in the graph. Therefore:
1. We do not need to construct an adjacency list.
2. We do not need to calculate the degree of all nodes.
3. We only need to inspect the first two edges: `edges[0]` and `edges[1]`.

The center node is simply the node that appears in both `edges[0]` and `edges[1]`.

### Step-by-Step Approach

1. Unpack the first edge into endpoints `u1, v1`.
2. Unpack the second edge into endpoints `u2, v2`.
3. Check if `u1` is present in the second edge (i.e., `u1 == u2` or `u1 == v2`):
   - If `True`, `u1` is the center node.
   - If `False`, `v1` must be the center node.
4. Return the identified center node in $O(1)$ time and $O(1)$ auxiliary space.

### Complexity Analysis

- **Time Complexity:** $O(1)$ — Only the first two edges are accessed and compared with constant-time equality checks. We do not even need to read the rest of the array.
- **Space Complexity:** $O(1)$ — Only a few primitive variables are used; no additional data structures are allocated.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Over-engineering with Adjacency Lists or Degree Counting:** Building a hash map or an array to count degrees of all $n$ nodes takes $O(n)$ time and $O(n)$ space. While this is acceptable in some contexts, top-tier interviewers look for candidates who immediately exploit the star graph's topological invariant to achieve $O(1)$.
2. **Missing Input Guarantees:** Assuming edges might not form a valid star graph and prematurely adding validation logic when the problem states that the graph is guaranteed to be a valid star graph. (Always clarify this with your interviewer before optimizing to $O(1)$).

---

### Real Interview Follow-Up Questions

#### 1. What if the input is NOT guaranteed to be a valid star graph?
**Answer:** 
We would need to validate two conditions:
1. `edges.length == n - 1` (tree condition).
2. Exactly one node has degree $n - 1$, and all other $n - 1$ nodes have degree $1$.
We can do this in $O(n)$ time and $O(n)$ space by counting node degrees. If an edge contains an invalid node label or forms a self-loop, return `-1`.

#### 2. What if edges are arriving as an infinite stream?
**Answer:**
If edges are streamed and guaranteed to be a valid star graph, we only need to inspect the first two distinct edges to output the center immediately. 
If we must continuously validate that the stream maintains the star graph property, we maintain the candidate center from the first two edges and verify that every subsequent streamed edge $(u, v)$ contains this center. If any edge does not, we flag the graph as invalid. Space remains $O(1)$.

#### 3. What if $n$ is massive (e.g., billions of edges distributed across multiple machines in MapReduce/Spark)?
**Answer:**
If the graph is partitioned, each partition can emit candidate centers (nodes with local degree $> 1$). The master node / reducer can intersect candidate sets or verify if a global center node has degree $n - 1$. Alternatively, any worker reading the first two edges can broadcast the candidate center, and a distributed map job can verify that all edges contain that vertex.
