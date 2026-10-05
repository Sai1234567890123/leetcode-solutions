# 1038. Binary Search Tree to Greater Sum Tree

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)  
**Topics:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

---

## 📝 Problem Statement

Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a *binary search tree* is a tree that satisfies these constraints:

	- The left subtree of a node contains only nodes with keys **less than** the node's key.

	- The right subtree of a node contains only nodes with keys **greater than** the node's key.

	- Both the left and right subtrees must also be binary search trees.

 
Example 1:

```

**Input:** root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
**Output:** [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

```

Example 2:

```

**Input:** root = [0,null,1]
**Output:** [1,null,1]

```

 
**Constraints:**

	- The number of nodes in the tree is in the range `[1, 100]`.

	- `0 

 
**Note:** This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

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
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        """
        Converts a Binary Search Tree to a Greater Sum Tree using
        reverse in-order traversal (Right -> Node -> Left).
        """
        running_sum = 0
        
        def reverse_inorder(node: TreeNode | None) -> None:
            nonlocal running_sum
            if not node:
                return
            
            # 1. Visit right subtree first (larger values)
            reverse_inorder(node.right)
            
            # 2. Process current node
            running_sum += node.val
            node.val = running_sum
            
            # 3. Visit left subtree (smaller values)
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

In a Binary Search Tree (BST):
- Standard in-order traversal (`Left` $\to$ `Node` $\to$ `Right`) visits values in strictly **ascending** order.
- Reverse in-order traversal (`Right` $\to$ `Node` $\to$ `Left`) visits values in strictly **descending** order.

The problem requires us to add to each node the sum of all keys greater than or equal to its own key. By traversing the tree in descending order:
1. The first node visited is the maximum value in the BST. Its new value is just its current value.
2. The second node visited is the second largest, so its new value is its value plus the largest value.
3. Every subsequent node visited should simply absorb the cumulative sum of all nodes visited before it.

By keeping a cumulative `running_sum`, we can update each node in-place in a single pass.

---

### Step-by-Step Approach

1. Initialize `running_sum = 0`.
2. Define a recursive helper function `reverse_inorder(node)`:
   - **Base Case:** If `node` is `None`, return immediately.
   - **Traverse Right:** Call `reverse_inorder(node.right)`. All keys in the right subtree are greater than `node.val` and must be accumulated first.
   - **Process Root:** Add `node.val` to `running_sum` and update `node.val = running_sum`.
   - **Traverse Left:** Call `reverse_inorder(node.left)`. Keys in the left subtree are smaller, so they will inherit this node's updated accumulated sum.
3. Call `reverse_inorder(root)` and return `root`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of nodes in the BST. Each node is visited exactly once.
- **Space Complexity:** $\mathcal{O}(H)$, where $H$ is the height of the tree, representing the recursion call stack.
  - In the worst case (skewed tree), $H = N \implies \mathcal{O}(N)$ space.
  - In the best/balanced case, $H = \log N \implies \mathcal{O}(\log N)$ space.

*(Note: If strictly $\mathcal{O}(1)$ auxiliary space is required, Reverse Morris In-Order Traversal can be used.)*

---

### Common Pitfalls / Mistakes Candidates Make

1. **Calculating Subtree Sums Repeatedly:** Traversing the right subtree for each node from scratch leads to an inefficient $\mathcal{O}(N^2)$ or $\mathcal{O}(N \log N)$ algorithm.
2. **Mutating Node Values Before Visiting Left Subtree:** If a candidate attempts to pass sums downwards without doing a strict reverse in-order traversal, the BST invariant might be misinterpreted.
3. **Global/Class State Leakage:** Forgetting to reset the running accumulator between multiple test invocations if using a class-level variable. Using a closure or instance method variable avoids this issue.

---

### Real Interview Follow-Up Questions & Answers

#### 1. Can we do this in $\mathcal{O}(1)$ auxiliary space without recursion or an explicit stack?
**Answer:** Yes, using **Reverse Morris In-Order Traversal**:
- For the current node, check if it has a right child:
  - If no right child, add `node.val` to `running_sum`, update `node.val`, and move to `node.left`.
  - If a right child exists, find the inorder successor (the leftmost node in the right subtree).
  - If the successor's left pointer is `None`, create a temporary thread pointing to `node` (`successor.left = node`) and move to `node.right`.
  - If the successor's left pointer already points to `node`, remove the thread (`successor.left = None`), add `node.val` to `running_sum`, update `node.val`, and move to `node.left`.
- This achieves $\mathcal{O}(N)$ time and true $\mathcal{O}(1)$ space.

#### 2. What if the tree has duplicate keys?
**Answer:** The standard BST definition either disallows duplicates or puts duplicates strictly on one side (e.g., right subtree for $\ge$). The reverse in-order traversal still works seamlessly with duplicates because the relative order of ties does not change the correctness of the prefix sum: ties will simply be accumulated one after another.

#### 3. How would you handle this tree if it is too massive to fit into memory on a single machine?
**Answer:** If the tree is stored distributed across machines (e.g., partitioned by key ranges such as $[0-1000)$, $[1000-2000)$):
1. **Pass 1:** Query each partition to get the sum of keys within its range.
2. Calculate the prefix sums of the partition totals from the highest range down to the lowest range.
3. **Pass 2:** Pass the offset to each partition and run local reverse in-order traversals in parallel.
