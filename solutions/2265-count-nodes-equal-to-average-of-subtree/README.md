# 2265. Count Nodes Equal to Average of Subtree

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/)  
**Topics:** Tree, Depth-First Search, Binary Tree

---

## 📝 Problem Statement

Given the `root` of a binary tree, return *the number of nodes where the value of the node is equal to the **average** of the values in its **subtree***.

**Note:**

	- The **average** of `n` elements is the **sum** of the `n` elements divided by `n` and **rounded down** to the nearest integer.

	- A **subtree** of `root` is a tree consisting of `root` and all of its descendants.

 
Example 1:

```

**Input:** root = [4,8,5,0,1,null,6]
**Output:** 5
**Explanation:** 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

```

Example 2:

```

**Input:** root = [1]
**Output:** 1
**Explanation:** For the node with value 1: The average of its subtree is 1 / 1 = 1.

```

 
**Constraints:**

	- The number of nodes in the tree is in the range `[1, 1000]`.

	- `0

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
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        Calculates the number of nodes where the node's value equals
        the integer average of its subtree.
        """
        matching_node_count = 0

        def post_order(node: TreeNode) -> tuple[int, int]:
            nonlocal matching_node_count
            if not node:
                # (subtree_sum, subtree_node_count)
                return 0, 0
            
            # Post-order traversal: process left and right subtrees first
            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)
            
            # Aggregate values for the current subtree rooted at `node`
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check condition: integer division represents floor rounding
            if current_sum // current_count == node.val:
                matching_node_count += 1
                
            return current_sum, current_count

        post_order(root)
        return matching_node_count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

To determine if a node's value equals the average of its subtree, we must know two pieces of information about the subtree rooted at that node:
1. The sum of all node values in the subtree (`subtree_sum`).
2. The total number of nodes in the subtree (`subtree_count`).

Computing this top-down for every node would require recalculating subtree sums and counts repeatedly, leading to a suboptimal $O(N^2)$ time complexity. 

Instead, notice that the information for any subtree can be directly composed from the information of its left and right subtrees:
- $\text{subtree\_sum} = \text{left\_sum} + \text{right\_sum} + \text{node.val}$
- $\text{subtree\_count} = \text{left\_count} + \text{right\_count} + 1$

This natural dependency structure points directly to a **post-order depth-first search (DFS)**. By computing metrics bottom-up, each node is visited exactly once, yielding an optimal $O(N)$ solution.

---

### Step-by-Step Approach

1. **Maintain a Global Counter**: Initialize `matching_node_count = 0`.
2. **Post-Order Helper Function (`post_order(node)`)**:
   - **Base Case**: If `node` is `None`, return `(0, 0)` representing a sum of `0` and a count of `0`.
   - **Recursive Step**:
     - Recurse on `node.left` to get `(left_sum, left_count)`.
     - Recurse on `node.right` to get `(right_sum, right_count)`.
   - **Aggregation**:
     - `current_sum = left_sum + right_sum + node.val`
     - `current_count = left_count + right_count + 1`
   - **Evaluation**:
     - Calculate the subtree average using integer division: `current_sum // current_count`.
     - If the result equals `node.val`, increment `matching_node_count`.
   - **Return**:
     - Return `(current_sum, current_count)` up to the parent.
3. **Execution**: Invoke `post_order(root)` and return `matching_node_count`.

---

### Complexity Analysis

- **Time Complexity:** $O(N)$
  - Each of the $N$ nodes is visited exactly once in the post-order traversal. At each node, constant-time $O(1)$ arithmetic operations and checks are performed.
- **Space Complexity:** $O(H)$
  - $H$ is the height of the binary tree, corresponding to the maximum depth of the call stack.
  - In the worst case (a completely skewed tree/linked-list structure), $H = O(N)$.
  - In the best/balanced case, $H = O(\log N)$.

---

### Common Pitfalls / Mistakes

1. **Incorrect Division / Rounding**:
   - The problem explicitly specifies: *rounded down to the nearest integer*. Using standard integer division (`//` in Python) automatically floors the result. Be careful in languages like C++/Java if negative values were possible, as integer division truncates toward zero rather than flooring. (In this problem, values are $\ge 0$).
2. **Top-Down Inefficiency ($O(N^2)$)**:
   - Calculating `sum` and `count` via separate recursive calls from each node instead of passing the results upward.
3. **Zero Division**:
   - Attempting to divide by `current_count` when `current_count == 0`. Handling the `node is None` base case cleanly ensures that when evaluating a valid node, `current_count` is at least $1$.

---

### Real Interview Follow-Up Questions

#### 1. What if the tree is extremely deep (e.g., $N = 10^6$) and causes a stack overflow?
- **Answer**: Recursion can exceed the call stack limit. We can rewrite the solution iteratively using a post-order traversal via an explicit stack. To simulate post-order iteratively, use a stack to push nodes and keep track of visited status (e.g., using a hash map or modifying pointers) to compute values after both subtrees are evaluated. Alternatively, Morris Traversal can be adapted for $O(1)$ auxiliary space, though it is more complex.

#### 2. What if node values can be negative?
- **Answer**: In Python, `//` computes floor division (`-7 // 2 == -4`), which adheres strictly to "rounded down to nearest integer". In C++/Java, `/` truncates toward zero (`-7 / 2 == -3`). If negative values were permitted, you would need `std::floor((double)sum / count)` in C++ / Java to correctly floor negative averages.

#### 3. What if the tree data is too large to fit in memory on a single machine?
- **Answer**: We can represent the tree across distributed partitions (e.g., in MapReduce or Apache Spark GraphX). Subtree aggregations become a generalized map-reduce tree aggregation (gather-apply-scatter / Pregel model) where messages containing `(sum, count)` are passed along directed edges from leaves to parents.
