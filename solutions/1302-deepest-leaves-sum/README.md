# 1302. Deepest Leaves Sum

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/deepest-leaves-sum/](https://leetcode.com/problems/deepest-leaves-sum/)  
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

## 📝 Problem Statement

Given the `root` of a binary tree, return *the sum of values of its deepest leaves*.
 
Example 1:

```

**Input:** root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
**Output:** 15

```

Example 2:

```

**Input:** root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
**Output:** 19

```

 
**Constraints:**

	- The number of nodes in the tree is in the range `[1, 104]`.

	- `1

---

## 💻 Implementation (python3)

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        """
        Calculates the sum of values of the deepest leaves in the binary tree
        using a single-pass Depth-First Search (DFS).
        """
        max_depth = -1
        deepest_sum = 0

        def dfs(node: TreeNode | None, depth: int) -> None:
            nonlocal max_depth, deepest_sum
            if not node:
                return

            # Found a node at a strictly greater depth: reset sum and update max_depth
            if depth > max_depth:
                max_depth = depth
                deepest_sum = node.val
            # Found another node at the current maximum depth: accumulate value
            elif depth == max_depth:
                deepest_sum += node.val

            # Recurse down left and right subtrees
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return deepest_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The objective is to compute the sum of values of all nodes located at the maximum depth of the binary tree. 

There are two primary paradigms to approach this:
1. **Breadth-First Search (BFS) / Level-Order Traversal**: Traverse the tree level by level. In each iteration, reset the sum to the sum of nodes at the current level. Once traversal finishes, the last calculated level sum represents the deepest leaves.
2. **Depth-First Search (DFS) Traversal**: Traverse the tree while passing down the current `depth`. Maintain two state variables: `max_depth` (the deepest level encountered so far) and `deepest_sum`.
   - When encountering a `depth > max_depth`, we have found a new deepest level: reset `deepest_sum` to `node.val` and update `max_depth = depth`.
   - When encountering a `depth == max_depth`, add `node.val` to `deepest_sum`.
   - Any node encountered at `depth < max_depth` is ignored.

**Why choose DFS over BFS?**
While both achieve $O(N)$ time complexity, DFS is strictly superior in terms of auxiliary space for balanced trees:
- BFS stores an entire level in memory, which requires $O(W)$ space where $W$ is the maximum width of the tree (up to $\approx N/2$ in a balanced binary tree, i.e., $O(N)$ space).
- DFS utilizes call stack frames bounded by the height of the tree $H$. In a balanced tree, $H = O(\log N)$.

Note: We do not need an explicit `node.left is None and node.right is None` check because any node at the global maximum depth cannot have children (otherwise, its children would reach a greater depth).

---

### Step-by-Step Approach

1. Initialize `max_depth = -1` and `deepest_sum = 0`.
2. Define a helper function `dfs(node, depth)`:
   - Base case: If `node` is `None`, return immediately.
   - If `depth > max_depth`: We reached a new deepest level. Update `max_depth = depth` and reset `deepest_sum = node.val`.
   - Else if `depth == max_depth`: We found another node at the current deepest level. Add `node.val` to `deepest_sum`.
   - Recursively call `dfs(node.left, depth + 1)` and `dfs(node.right, depth + 1)`.
3. Invoke `dfs(root, 0)`.
4. Return `deepest_sum`.

---

### Complexity Analysis

- **Time Complexity:** $O(N)$
  - Every node in the binary tree is visited exactly once. At each node, we perform $O(1)$ constant-time operations.
- **Space Complexity:** $O(H)$
  - Governed by the call stack recursion depth.
  - **Best/Average Case (balanced tree):** $O(\log N)$
  - **Worst Case (skewed tree):** $O(N)$

---

### Common Pitfalls / Mistakes Candidates Make

1. **Two-Pass Overhead**: First computing the tree's maximum depth in one full pass, then doing a second pass to sum nodes at that depth. While still $O(N)$, doing it in a single pass is cleaner and preferred.
2. **Unnecessary Leaf Checks**: Writing verbose conditional logic to verify `if not node.left and not node.right`. Any node at `max_depth` is guaranteed to be a leaf.
3. **Queue Sizing in BFS**: In BFS, forgetting to capture the level size (`len(queue)`) or overwriting the queue prematurely, causing nodes from different levels to mix into the same sum.
4. **Integer Overflow Considerations**: In languages like C++ or Java, if node values or counts were large, standard 32-bit signed integers could overflow (though within LeetCode's constraints of $N \le 10^4$ and $val \le 100$, maximum sum is $10^6$, fitting comfortably in a 32-bit integer).

---

### Real Interview Follow-Up Questions & Solutions

#### 1. How would you solve this if memory is extremely constrained (e.g., embedded devices where $O(H)$ stack space is unacceptable)?
**Answer:** Use **Morris Traversal** (threaded binary tree).
- By modifying the right pointers of in-order predecessors to point back to the current node, we can traverse the tree without recursion or explicit queues.
- Since standard Morris Traversal doesn't easily maintain depth during backward leaps, we can run a two-pass Morris traversal:
  1. Pass 1: Find maximum depth.
  2. Pass 2: Sum nodes at that depth.
- This achieves $O(N)$ time with strictly $O(1)$ auxiliary space.

#### 2. What if the tree is distributed across multiple machines / too large to fit in single-machine memory?
**Answer:** 
- Represent the tree as an adjacency list or key-value store partitioned across machines (e.g., using MapReduce / Apache Spark).
- **Map phase:** Emit key-value pairs `(depth, node.val)` by propagating depths downward from the root.
- **Reduce phase:** Aggregate sums by `depth` to get `(depth, sum_at_depth)`.
- Finally, take the record with the maximum key `depth`.

#### 3. How would you handle concurrent reads and mutations (e.g., subtrees being dynamically inserted/deleted)?
**Answer:**
- Standard traversals require snapshot isolation or subtree-level locking.
- If using locks, Read-Write locks (RWLock) or hand-over-hand locking (lock coupling) can be used, though locking top-down creates bottlenecks near the root.
- A preferred pattern is an immutable/persistent tree data structure (like Clojure's or functional trees) where updates create a new root with path copying, allowing concurrent traversals to run against consistent immutable snapshots without locking.
