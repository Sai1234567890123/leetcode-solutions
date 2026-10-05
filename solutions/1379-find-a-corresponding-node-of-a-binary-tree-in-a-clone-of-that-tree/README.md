# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)  
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

## 📝 Problem Statement

Given two binary trees `original` and `cloned` and given a reference to a node `target` in the original tree.

The `cloned` tree is a **copy of** the `original` tree.

Return *a reference to the same node* in the `cloned` tree.

**Note** that you are **not allowed** to change any of the two trees or the `target` node and the answer **must be** a reference to a node in the `cloned` tree.

 
Example 1:

```

**Input:** tree = [7,4,3,null,null,6,19], target = 3
**Output:** 3
**Explanation:** In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

```

Example 2:

```

**Input:** tree = [7], target =  7
**Output:** 7

```

Example 3:

```

**Input:** tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
**Output:** 4

```

 
**Constraints:**

	- The number of nodes in the `tree` is in the range `[1, 104]`.

	- The values of the nodes of the `tree` are unique.

	- `target` node is a node from the `original` tree and is not `null`.

 
**Follow up:** Could you solve the problem if repeated values on the tree are allowed?

---

## 💻 Implementation (python3)

```py
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        Traverses both trees simultaneously to find the target node by reference.
        Using BFS ensures we avoid recursion depth limits in Python (since N <= 10^4).
        Comparing node references (original_node is target) directly answers both
        the base problem and the follow-up where node values can be duplicated.
        """
        if not original or not cloned:
            return None
        
        # Queue stores pairs of (original_node, cloned_node)
        queue = deque([(original, cloned)])
        
        while queue:
            orig_node, clone_node = queue.popleft()
            
            # Check reference identity, not value equality
            if orig_node is target:
                return clone_node
            
            if orig_node.left:
                queue.append((orig_node.left, clone_node.left))
            if orig_node.right:
                queue.append((orig_node.right, clone_node.right))
                
        return None
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires finding the clone of a specific `target` node in an identical copy of a binary tree. 

Key observations:
1. **Reference vs. Value**: We are given a direct reference to `target` in `original`. While the problem notes that node values are unique, the interview follow-up specifically asks: *what if values are not unique?* By comparing the memory identity (`orig_node is target`) rather than `orig_node.val == target.val`, our solution natively handles both unique and non-unique values.
2. **Parallel Traversal**: Both trees have the exact same structure. If we traverse both trees synchronously (e.g., visiting the left child of `original` and the left child of `cloned` simultaneously), whenever we encounter `target` in `original`, the node at the exact same position in `cloned` is our answer.
3. **Recursion vs. Iteration in Python**: The tree can have up to $10^4$ nodes. In a skewed tree, recursive DFS would exceed Python's default recursion depth limit of $1000$ (`RecursionError`). An iterative approach (BFS with a queue or DFS with a stack) is production-grade and immune to stack overflow.

### Step-by-Step Approach

1. Initialize a queue with a tuple of roots: `(original, cloned)`.
2. While the queue is not empty:
   - Pop `(orig_node, clone_node)`.
   - If `orig_node is target`, return `clone_node`.
   - If `orig_node.left` exists, push `(orig_node.left, clone_node.left)` onto the queue.
   - If `orig_node.right` exists, push `(orig_node.right, clone_node.right)` onto the queue.
3. If no match is found, return `None`.

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$ in the worst case (e.g., target is at the last visited leaf node or absent), where $N$ is the number of nodes in the tree. We visit each node at most once and perform $\mathcal{O}(1)$ operations per node.
- **Space Complexity**: $\mathcal{O}(W)$ where $W$ is the maximum width of the tree. In a balanced binary tree, the maximum width is at most $\lceil N / 2 \rceil$, which gives $\mathcal{O}(N)$ space complexity in the worst-case queue size. If an iterative DFS stack is used, space complexity would be $\mathcal{O}(H)$ where $H$ is the height of the tree ($\mathcal{O}(\log N)$ for balanced, $\mathcal{O}(N)$ for skewed).

### Common Pitfalls & Mistakes

1. **Comparing Values Instead of Node References**: Checking `orig_node.val == target.val` fails immediately if node values are duplicated (the follow-up question). Always compare references (`orig_node is target`).
2. **Recursion Limit Exceeded**: Submitting a naive recursive DFS in Python can result in a `RecursionError` on degenerate, line-shaped trees (constraints state $N \le 10^4$).
3. **Searching Only the Cloned Tree**: Without unique values, you cannot simply traverse `cloned` looking for a value. Parallel traversal is the most direct way to resolve identity.

### Real Interview Follow-Up Questions & Answers

1. **Follow-Up: What if repeated values on the tree are allowed?**
   - *Answer*: Traversal by reference identity (`orig_node is target`) handles duplicate values transparently. No value comparisons are performed.

2. **Follow-Up: Can we solve this if we only have access to `target` (and parents) and cannot traverse from the root?**
   - *Answer*: If tree nodes have a `.parent` pointer, we can trace a path from `target` up to `original` root, recording the sequence of moves (e.g., `['left', 'right', 'left']`). Then, starting from `cloned` root, replay the path downward in reverse. This takes $\mathcal{O}(H)$ time and $\mathcal{O}(H)$ space, without exploring the rest of the tree.

3. **Follow-Up: What if the tree is distributed across multiple machines / huge (cannot fit in memory)?**
   - *Answer*: The path-recording approach above works well: traverse upward from `target` to get the path coordinates (or depth-first path), then only stream the specific path down the cloned tree rather than loading the whole tree.
