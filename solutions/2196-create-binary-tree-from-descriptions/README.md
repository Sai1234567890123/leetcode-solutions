# 2196. Create Binary Tree From Descriptions

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/create-binary-tree-from-descriptions/](https://leetcode.com/problems/create-binary-tree-from-descriptions/)  
**Topics:** Array, Hash Table, Tree, Binary Tree

---

## 📝 Problem Statement

You are given a 2D integer array `descriptions` where `descriptions[i] = [parenti, childi, isLefti]` indicates that `parenti` is the **parent** of `childi` in a **binary** tree of **unique** values. Furthermore,

	- If `isLefti == 1`, then `childi` is the left child of `parenti`.

	- If `isLefti == 0`, then `childi` is the right child of `parenti`.

Construct the binary tree described by `descriptions` and return *its **root***.

The test cases will be generated such that the binary tree is **valid**.

 
Example 1:

```

**Input:** descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
**Output:** [50,20,80,15,17,19]
**Explanation:** The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

```

Example 2:

```

**Input:** descriptions = [[1,2,1],[2,3,0],[3,4,1]]
**Output:** [1,2,null,null,3,4]
**Explanation:** The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.

```

 
**Constraints:**

	- `1 4`

	- `descriptions[i].length == 3`

	- `1 i, childi 5`

	- `0 i

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
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        nodes: dict[int, TreeNode] = {}
        children: set[int] = set()

        for parent_val, child_val, is_left in descriptions:
            # Retrieve or create parent node
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            parent_node = nodes[parent_val]

            # Retrieve or create child node
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            child_node = nodes[child_val]

            # Connect parent to child based on is_left flag
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            # Record child to identify the root later
            children.add(child_val)

        # The root is the only node that never appears as a child
        for parent_val, _, _ in descriptions:
            if parent_val not in children:
                return nodes[parent_val]

        return None
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to reconstruct a binary tree given parent-child directional edges. All node values are guaranteed to be unique, and the tree structure is guaranteed to be a valid binary tree.

Two primary challenges exist:
1. **Node Instantiation and Edge Linking**: We must instantiate each `TreeNode` exactly once and link left/right pointers accurately. A hash map mapping node values to their corresponding `TreeNode` references allows $O(1)$ lookup and instantiation.
2. **Identifying the Root**: In any valid tree/DAG, the root node has an in-degree of 0 (it is never a child of any node). By maintaining a set of all values that appear as children, the root will simply be the node that appears as a parent but never as a child.

### Step-by-Step Approach

1. Initialize a hash map `nodes` mapping `val -> TreeNode(val)`.
2. Initialize a hash set `children` to keep track of every `child_val`.
3. Iterate through each `[parent_val, child_val, is_left]` in `descriptions`:
   - If `parent_val` is not in `nodes`, create a new `TreeNode(parent_val)`.
   - If `child_val` is not in `nodes`, create a new `TreeNode(child_val)`.
   - Assign the child node to `parent_node.left` if `is_left == 1`, otherwise to `parent_node.right`.
   - Add `child_val` to the `children` set.
4. Iterate over the descriptions again (or over the keys in `nodes`). The first node value that is not present in `children` is the root of the tree.
5. Return the `TreeNode` reference corresponding to that root value.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the number of descriptions.
  - We iterate through `descriptions` of length $N$ once to build the tree and record children. Dictionary and set operations run in average $\mathcal{O}(1)$ time.
  - Finding the root takes at most $\mathcal{O}(N)$ checks.
  - Total time complexity: $\mathcal{O}(N)$.

- **Space Complexity**: $\mathcal{O}(N)$
  - The `nodes` hash map stores at most $N + 1$ unique tree nodes.
  - The `children` hash set stores at most $N$ unique child values.
  - Total auxiliary space: $\mathcal{O}(N)$.

### Common Pitfalls / Mistakes

1. **Re-instantiating Nodes**: Instantiating a new `TreeNode` every time a value appears creates disconnected components rather than a unified tree. Using a hash map guarantees singletons for each unique value.
2. **Finding the Root Incorrectly**: Searching for the root by traversing child-to-parent pointers backwards is unnecessary and requires extra space or overhead. A simple set of child nodes resolves root identification in $\mathcal{O}(1)$ per lookup.
3. **Assuming 1-indexed / Contiguous Values**: Node values can be any integer up to $10^5$. Using an array instead of a hash map can waste memory or lead to index out-of-bounds errors if constraints change.

### Real Interview Follow-Up Questions

#### 1. What if the input stream is massive and does not fit in memory? (External Memory / Streaming)
**Answer**: 
- We can write descriptions to an external distributed key-value store or use a two-pass MapReduce approach:
  - First pass: Emit `(child, 1)` to count in-degrees. Filter for keys with 0 in-degree to find the root.
  - Second pass: Adjacency list stored in an on-disk database (e.g., RocksDB) where nodes are fetched on demand when traversing the tree.

#### 2. What if the input can contain cycles or invalid tree structures? How would you validate?
**Answer**:
- Validate three properties:
  1. Exactly one node has an in-degree of 0 (the root).
  2. Every other node has an in-degree of exactly 1.
  3. No parent has multiple left or multiple right children.
  4. Perform a DFS/BFS starting from the candidate root to ensure all $V$ nodes are reachable and visited exactly once (acyclic and fully connected).

#### 3. What if values are not unique?
**Answer**:
- If values are not unique, node values alone cannot serve as node identifiers. Each description must either use explicit unique IDs (like memory addresses or UUIDs) alongside node values, or the input representation must be structured hierarchically (e.g., serialized preorder/inorder traversal).
