# 1382. Balance a Binary Search Tree

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/balance-a-binary-search-tree/](https://leetcode.com/problems/balance-a-binary-search-tree/)  
**Topics:** Divide and Conquer, Greedy, Tree, Depth-First Search, Binary Search Tree, Binary Tree

---

## 📝 Problem Statement

Given the `root` of a binary search tree, return *a **balanced** binary search tree with the same node values*. If there is more than one answer, return **any of them**.

A binary search tree is **balanced** if the depth of the two subtrees of every node never differs by more than `1`.

 
Example 1:

```

**Input:** root = [1,null,2,null,3,null,4,null,null]
**Output:** [2,1,3,null,null,null,4]
**Explanation:** This is not the only correct answer, [3,1,4,null,2] is also correct.

```

Example 2:

```

**Input:** root = [2,1,3]
**Output:** [2,1,3]

```

 
**Constraints:**

	- The number of nodes in the tree is in the range `[1, 104]`.

	- `1 5`

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
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        """
        Balances an unbalanced Binary Search Tree (BST).
        
        Strategy:
        1. Perform an in-order traversal to extract nodes in sorted order.
           We can collect the node references directly to reuse them.
        2. Recursively construct a height-balanced BST from the sorted list
           by choosing the median element as the subtree root.
        """
        sorted_nodes = []
        
        def inorder(node: TreeNode | None) -> None:
            if not node:
                return
            inorder(node.left)
            sorted_nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        def build_balanced_bst(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            
            mid = (left + right) // 2
            curr = sorted_nodes[mid]
            
            # Recursively build left and right subtrees
            curr.left = build_balanced_bst(left, mid - 1)
            curr.right = build_balanced_bst(mid + 1, right)
            
            return curr
        
        return build_balanced_bst(0, len(sorted_nodes) - 1)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A Binary Search Tree has the fundamental property that its **in-order traversal** visits nodes in strictly increasing (sorted) order. 

If we have a sorted sequence of values, constructing a height-balanced BST is equivalent to LeetCode #108 (*Convert Sorted Array to Binary Search Tree*):
1. Choose the middle element as the current subtree root.
2. Recursively build the left subtree from the left half of the subarray.
3. Recursively build the right subtree from the right half of the subarray.

By picking the middle element at every step, we ensure that the number of elements in the left and right subtrees differs by at most 1, guaranteeing an optimal height of $\lfloor \log_2 N \rfloor$ and strictly adhering to the balanced BST criteria ($\lvert \text{depth}(\text{left}) - \text{depth}(\text{right}) \rvert \le 1$).

We can optimize memory allocations by storing the `TreeNode` references directly in the list and rewiring their pointers (`left` and `right`) during the build phase.

---

### Step-by-Step Approach

1. **In-Order Traversal**: Traverse the original BST in-order (`left -> root -> right`) and collect node references in a Python list `sorted_nodes`.
2. **Divide and Conquer Construction**:
   - Define a helper function `build_balanced_bst(left, right)`.
   - Base case: If `left > right`, return `None`.
   - Midpoint selection: `mid = (left + right) // 2`.
   - Assign `curr = sorted_nodes[mid]`.
   - Recursively assign `curr.left = build_balanced_bst(left, mid - 1)` and `curr.right = build_balanced_bst(mid + 1, right)`.
   - Return `curr`.
3. Call `build_balanced_bst(0, len(sorted_nodes) - 1)` and return the new root.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
  - In-order traversal visits each node exactly once: $\mathcal{O}(N)$.
  - Constructing the balanced tree visits each index in the sorted array once and sets pointers in $\mathcal{O}(1)$ per node: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N)$, which is asymptotically optimal since we must inspect all nodes.

- **Space Complexity:** $\mathcal{O}(N)$
  - `sorted_nodes` holds $N$ node references: $\mathcal{O}(N)$ space.
  - The recursion stack for `inorder` takes $\mathcal{O}(H)$ space, which can be $\mathcal{O}(N)$ in the worst case (a completely skewed tree).
  - The recursion stack for `build_balanced_bst` is bounded by the height of the balanced tree: $\mathcal{O}(\log N)$.
  - Total Auxiliary Space: $\mathcal{O}(N)$.

---

### Common Pitfalls / Mistakes

1. **Allocating New Nodes Unnecessarily**: Creating new `TreeNode(val)` instances increases garbage collection pressure and memory usage. Reusing existing node pointers is cleaner and faster.
2. **Integer Overflow on Mid Calculation**: In languages like C++/Java, `(left + right) / 2` can overflow if indices are large; using `left + (right - left) / 2` is standard practice (though Python handles arbitrarily large integers automatically).
3. **Off-by-One in Array Boundaries**: Passing `mid` instead of `mid - 1` or `mid + 1` causes infinite recursion.

---

### Real Interview Follow-Up Questions

#### 1. Can you do this in $\mathcal{O}(1)$ auxiliary space?
**Answer:** Yes, using the **Day-Stout-Warren (DSW) Algorithm**:
- **Phase 1 (Vine Creation):** Flatten the BST into a linked list-like structure (a "vine" or degenerate right-skewed tree) using right rotations at the root/nodes whenever a left child exists. This takes $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.
- **Phase 2 (Balancing):** Perform a calculated series of left rotations on alternating nodes along the vine to iteratively compress the vine into a balanced BST.
- Both phases operate completely in-place using tree rotations without storing node references or recursion stack frames, achieving **$\mathcal{O}(N)$ time and $\mathcal{O}(1)$ auxiliary space**.

#### 2. What if the tree is too large to fit in memory? (External Memory / Streaming)
**Answer:**
- Perform an external merge sort or write the in-order traversal into an on-disk sequential file.
- Read sequentially from the file using a bottom-up construction (similar to constructing a complete binary tree from a stream by building subtrees of size $2^k - 1$).
