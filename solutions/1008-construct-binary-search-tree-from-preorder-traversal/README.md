# 1008. Construct Binary Search Tree from Preorder Traversal

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)  
**Topics:** Array, Stack, Tree, Binary Search Tree, Monotonic Stack, Binary Tree

---

## 📝 Problem Statement

Given an array of integers preorder, which represents the **preorder traversal** of a BST (i.e., **binary search tree**), construct the tree and return *its root*.

It is **guaranteed** that there is always possible to find a binary search tree with the given requirements for the given test cases.

A **binary search tree** is a binary tree where for every node, any descendant of `Node.left` has a value **strictly less than** `Node.val`, and any descendant of `Node.right` has a value **strictly greater than** `Node.val`.

A **preorder traversal** of a binary tree displays the value of the node first, then traverses `Node.left`, then traverses `Node.right`.

 
Example 1:

```

**Input:** preorder = [8,5,1,7,10,12]
**Output:** [8,5,10,1,7,null,12]

```

Example 2:

```

**Input:** preorder = [1,3]
**Output:** [1,null,3]

```

 
**Constraints:**

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
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        idx = 0
        n = len(preorder)

        def build(upper_bound: float) -> TreeNode | None:
            nonlocal idx
            # Base case: exhausted array or current value exceeds the allowed upper bound
            if idx == n or preorder[idx] > upper_bound:
                return None

            # The current element becomes the root of this subtree
            val = preorder[idx]
            idx += 1
            root = TreeNode(val)

            # Left child's values must be strictly less than the current node's value
            root.left = build(val)
            # Right child's values must be strictly less than the inherited upper bound
            root.right = build(upper_bound)

            return root

        return build(float('inf'))
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A preorder traversal visits nodes in the order: **Root $\to$ Left Subtree $\to$ Right Subtree**.
In a Binary Search Tree (BST):
1. All elements in the left subtree are strictly less than `root.val`.
2. All elements in the right subtree are strictly greater than `root.val` and strictly bounded by the parent's upper bound.

A naive approach would locate the split point between elements smaller and larger than the root using linear scan or binary search, leading to an $O(N^2)$ or $O(N \log N)$ solution.

An optimal $O(N)$ approach mimics tree construction with a single scan over `preorder` by carrying an `upper_bound` constraint down the recursion:
- If the current element exceeds `upper_bound`, it cannot belong to the current subtree; return `None`.
- Otherwise, consume the element, create a node, and:
  - Recursively build the left child with `upper_bound = node.val`.
  - Recursively build the right child with `upper_bound` inherited from the caller.

Notice that a lower bound is not strictly necessary for standard preorder traversal. Because we greedily build left subtrees first, when the recursion falls back to construct the right child, any value seen will already be greater than the current node's value (otherwise, it would have been consumed in the left subtree).

---

### Step-by-Step Approach

1. **Pointer Maintenance**: Maintain an index `idx` pointing to the next unplaced value in `preorder`.
2. **Recursive Function `build(upper_bound)`**:
   - Check if `idx == len(preorder)` or `preorder[idx] > upper_bound`. If so, backtrack (`return None`).
   - Create a new `TreeNode` with `val = preorder[idx]`.
   - Increment `idx`.
   - Set `root.left = build(root.val)`.
   - Set `root.right = build(upper_bound)`.
   - Return `root`.
3. **Initial Call**: Invoke `build(float('inf'))` to start with no upper limit.

---

### Complexity Analysis

- **Time Complexity:** $O(N)$
  - Each element in the array `preorder` is processed at most once when creating a node, and checked at most a constant number of times against `upper_bound` during backtracks. Thus, the total time is strictly linear.
- **Space Complexity:** $O(H)$ auxiliary space
  - $H$ is the height of the resulting BST.
  - In the worst case (skewed tree), $H = O(N)$.
  - In the average/best case (balanced tree), $H = O(\log N)$.
  - This space is utilized solely by the recursive call stack.

---

### Common Pitfalls / Mistakes

1. **Re-sorting to get Inorder traversal**: Sorting `preorder` to obtain `inorder` and then building a tree using preorder + inorder works, but it takes $O(N \log N)$ time and $O(N)$ additional memory for hash maps.
2. **Slicing arrays at each recursion**: Passing array slices (e.g., `preorder[1:i]` and `preorder[i:]`) creates copies at each step, degrading time and space complexity to $O(N^2)$.
3. **Overcomplicating bounds**: Introducing both `lower_bound` and `upper_bound` is redundant for preorder traversal. Only `upper_bound` is required.

---

### Real Interview Follow-Up Questions

#### 1. How would you solve this iteratively without recursion?
**Answer:** Use an explicit stack.
- The root is `TreeNode(preorder[0])`. Push it onto the stack.
- For each subsequent value:
  - If `val < stack[-1].val`, it is the left child of `stack[-1]`. Attach it and push to stack.
  - If `val > stack[-1].val`, pop nodes while `stack` is not empty and `stack[-1].val < val`. The last popped node will have `val` as its right child. Attach it and push the new node to stack.
- This also runs in $O(N)$ time and $O(H)$ space.

#### 2. What if the input stream is endless (streaming data)?
**Answer:**
If tokens arrive one-by-one from a stream where the end is unknown, an iterative stack-based approach works seamlessly: process each node as it arrives, popping ancestors until finding the parent.

#### 3. What if there are duplicate values allowed in the BST?
**Answer:**
We must clarify the BST definition for duplicates (e.g., duplicates go to the left or right). If duplicates go to the left, the bound condition changes to `preorder[idx] >= upper_bound`.
