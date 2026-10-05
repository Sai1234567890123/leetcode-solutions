# 2415. Reverse Odd Levels of Binary Tree

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/)  
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

## 📝 Problem Statement

Given the `root` of a **perfect** binary tree, reverse the node values at each **odd** level of the tree.

	- For example, suppose the node values at level 3 are `[2,1,3,4,7,11,29,18]`, then it should become `[18,29,11,7,4,3,1,2]`.

Return *the root of the reversed tree*.

A binary tree is **perfect** if all parent nodes have two children and all leaves are on the same level.

The **level** of a node is the number of edges along the path between it and the root node.

 
Example 1:

```

**Input:** root = [2,3,5,8,13,21,34]
**Output:** [2,5,3,8,13,21,34]
**Explanation:** 
The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.

```

Example 2:

```

**Input:** root = [7,13,11]
**Output:** [7,11,13]
**Explanation:** 
The nodes at level 1 are 13, 11, which are reversed and become 11, 13.

```

Example 3:

```

**Input:** root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
**Output:** [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
**Explanation:** 
The odd levels have non-zero values.
The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.

```

 
**Constraints:**

	- The number of nodes in the tree is in the range `[1, 214]`.

	- `0 5`

	- `root` is a **perfect** binary tree.

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
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        def dfs(node1: TreeNode | None, node2: TreeNode | None, level: int) -> None:
            # Base case: Since it's a perfect binary tree, if node1 is None, node2 is also None
            if not node1 or not node2:
                return

            # If the current level is odd, swap the values of the mirrored nodes
            if level % 2 == 1:
                node1.val, node2.val = node2.val, node1.val

            # Recurse symmetrically:
            # Pair the leftmost child of the left subtree with the rightmost child of the right subtree
            dfs(node1.left, node2.right, level + 1)
            # Pair the rightmost child of the left subtree with the leftmost child of the right subtree
            dfs(node1.right, node2.left, level + 1)

        # Start recursion with the children of the root at level 1
        dfs(root.left, root.right, 1)
        return root
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires reversing the values of nodes at every odd level in a **perfect binary tree**. 

A standard level-order traversal (BFS) can achieve this by collecting all nodes at a given level and using a two-pointer approach to reverse their values when the level is odd. However, BFS requires storing the entire width of the tree at the deepest level, which consumes $O(N)$ auxiliary space (where $N/2$ nodes exist at the bottom layer).

Since the tree is guaranteed to be a **perfect binary tree**, we can leverage its inherent structural symmetry using a Depth-First Search (DFS) approach:
- To reverse values at an odd level, the $i$-th node from the left must swap its value with the $i$-th node from the right.
- We can traverse the tree using two pointers (`node1` and `node2`) representing symmetric counterpart nodes across the tree's vertical axis.
- When traversing deeper:
  - Pair `node1.left` with `node2.right` (outer pair).
  - Pair `node1.right` with `node2.left` (inner pair).
- This recursive pairing mirrors the exact symmetric swap required, operating in $O(\log N)$ auxiliary call stack space instead of $O(N)$.

### Step-by-Step Approach

1. **Edge Case**: If the `root` is `None`, return `None`.
2. **Recursive Helper Function (`dfs(node1, node2, level)`)**:
   - **Base Case**: If either node is `None`, return immediately.
   - **Value Swap**: If `level % 2 == 1`, swap `node1.val` and `node2.val`.
   - **Divide & Conquer**:
     - Call `dfs(node1.left, node2.right, level + 1)` to handle the outer mirror.
     - Call `dfs(node1.right, node2.left, level + 1)` to handle the inner mirror.
3. **Execution**: Invoke `dfs(root.left, root.right, 1)` and return `root`.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$
  Every node in the tree is visited exactly once, performing $\mathcal{O}(1)$ operations per node.
- **Space Complexity**: $\mathcal{O}(\log N)$
  Because the tree is a perfect binary tree, its height is strictly $h = \log_2(N + 1)$. The maximum call stack depth is $\mathcal{O}(\log N)$, which evaluates to at most $14$ stack frames for $N = 2^{14}$. This is strictly optimal compared to BFS $\mathcal{O}(N)$.

---

### Common Pitfalls / Mistakes

1. **Re-linking Pointers Instead of Swapping Values**:
   - The problem statement asks to reverse the node *values*. Attempting to mutate child pointers (`left` and `right`) instead of swapping values is significantly more error-prone, particularly when maintaining the tree's structure for subsequent levels.
2. **Incorrect Recursive Pairings**:
   - A common bug is pairing `node1.left` with `node1.right` and `node2.left` with `node2.right`. This only swaps locally within subtrees instead of reversing across the entire level horizontally.
3. **Overlooking the "Perfect Binary Tree" Property**:
   - Writing code that over-complicates null checks. In a perfect binary tree, if `node.left` exists, `node.right` is guaranteed to exist.

---

### Real Interview Follow-Up Questions

#### 1. What if the tree is NOT a perfect binary tree (i.e., arbitrary shape)?
- **Answer**: The symmetric DFS approach breaks down because corresponding mirror nodes may not exist at matching depths. 
- In this case, standard **BFS (Level-Order Traversal)** is the preferred solution:
  1. Traverse level by level using a queue.
  2. For odd levels, extract all node values into an array, reverse the array, and reassign the values back to the nodes in the queue.
  3. Time Complexity remains $\mathcal{O}(N)$, and Space Complexity is $\mathcal{O}(W)$ where $W$ is the maximum width of the tree ($\le N/2$).

#### 2. What if modifying `node.val` is disallowed (nodes are immutable)?
- **Answer**: If nodes cannot be mutated in place, we must reconstruct the tree or swap pointers directly:
  - If we rebuild: perform DFS to create new `TreeNode` instances with reversed values.
  - If swapping pointers: at even levels, we can swap `node.left` and `node.right` pointers of each node at level $L-1$, but doing so will invert the child subtrees, which requires unwinding or careful mirrored traversal for deeper levels.

#### 3. How would you handle this tree if it is too massive to fit into memory?
- **Answer**: 
  - If nodes are serialized on disk (e.g., in array/heap layout: node at index $i$ has children at $2i+1$ and $2i+2$):
    - Level $L$ spans indices from $2^L - 1$ to $2^{L+1} - 2$.
    - We can perform memory-mapped file access (mmap) or chunked two-pointer disk reads to swap symmetric pairs $A[2^L - 1 + k]$ and $A[2^{L+1} - 2 - k]$ strictly on disk without loading the entire tree into RAM.
