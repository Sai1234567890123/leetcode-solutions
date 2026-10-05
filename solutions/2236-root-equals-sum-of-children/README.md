# 2236. Root Equals Sum of Children

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/root-equals-sum-of-children/](https://leetcode.com/problems/root-equals-sum-of-children/)  
**Topics:** Tree, Binary Tree

---

## 📝 Problem Statement

You are given the `root` of a **binary tree** that consists of exactly `3` nodes: the root, its left child, and its right child.

Return `true` *if the value of the root is equal to the **sum** of the values of its two children, or *`false`* otherwise*.

 
Example 1:

```

**Input:** root = [10,4,6]
**Output:** true
**Explanation:** The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.

```

Example 2:

```

**Input:** root = [5,3,1]
**Output:** false
**Explanation:** The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.

```

 
**Constraints:**

	- The tree consists only of the root, its left child, and its right child.

	- `-100

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
    def checkTree(self, root: TreeNode | None) -> bool:
        # Per problem constraints, the tree contains exactly 3 nodes:
        # the root, its left child, and its right child.
        # Direct check if root's value equals the sum of left and right child values.
        return root.val == root.left.val + root.right.val
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem explicitly constrains the binary tree to contain exactly three nodes:
1. The `root`
2. The `root.left` child
3. The `root.right` child

Because both children are guaranteed to exist, this is a direct conditional check comparing the root's value against the sum of its two children's values. There is no traversal, recursion, or dynamic data structure required.

### Step-by-Step Approach

1. Access `root.val`.
2. Access `root.left.val` and `root.right.val`.
3. Compute `root.left.val + root.right.val`.
4. Return `True` if `root.val == root.left.val + root.right.val`, otherwise return `False`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$. The algorithm executes a single addition and comparison operation regardless of any external input variables.
- **Space Complexity:** $\mathcal{O}(1)$. No additional memory or recursion call stack is utilized.

---

### Common Pitfalls / Mistakes

1. **Over-engineering:** Attempting tree traversals (e.g., DFS or BFS) or recursive solutions when the constraints explicitly guarantee exactly 3 nodes.
2. **Defensive Programming Oversights:** In real-world code, blindly accessing `root.left.val` without checking `root is not None` and `root.left is not None` can lead to `AttributeError` / `NullPointerException`. Even though LeetCode guarantees the tree structure here, mentioning null checks to the interviewer demonstrates senior engineering instincts.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if this property needs to hold for an arbitrary binary tree (every node equals the sum of its children)?
* **Answer:** We can solve this with a post-order traversal (DFS). For each node:
  - If it is a leaf node, its property vacuously holds (or it contributes its value to its parent).
  - For an internal node, recursively verify both children, then verify `node.val == (node.left.val if node.left else 0) + (node.right.val if node.right else 0)`.
  - Time Complexity: $\mathcal{O}(N)$, Space Complexity: $\mathcal{O}(H)$ where $H$ is the tree height.

#### 2. What if node values can be arbitrarily large integers (overflow concerns)?
* **Answer:** 
  - In Python 3, integers have arbitrary precision, so overflow is not an issue.
  - In languages like C++, Java, or Go, summing two 32-bit signed integers (`INT_MAX`) can cause integer overflow. We would cast operands to 64-bit integers (`long long` in C++, `long` in Java) before adding: `(long)root.left.val + root.right.val == root.val`.

#### 3. How would you handle a concurrent environment where nodes might be updated dynamically?
* **Answer:** 
  - To ensure a consistent read across parent and children, we need read locks on the parent and both children simultaneously, or use optimistic concurrency control (e.g., version tagging on nodes). If nodes can be modified or restructured concurrently, lock ordering (e.g., parent first, then left child, then right child) must be strictly enforced to avoid deadlocks.
