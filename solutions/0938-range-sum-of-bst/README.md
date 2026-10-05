# 0938. Range Sum of BST

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/range-sum-of-bst/](https://leetcode.com/problems/range-sum-of-bst/)  
**Topics:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

---

## 📝 Problem Statement

Given the `root` node of a binary search tree and two integers `low` and `high`, return *the sum of values of all nodes with a value in the **inclusive** range *`[low, high]`.

 
Example 1:

```

**Input:** root = [10,5,15,3,7,null,18], low = 7, high = 15
**Output:** 32
**Explanation:** Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

```

Example 2:

```

**Input:** root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
**Output:** 23
**Explanation:** Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

```

 
**Constraints:**

	- The number of nodes in the tree is in the range `[1, 2 * 104]`.

	- `1 5`

	- `1 5`

	- All `Node.val` are **unique**.

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
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        """
        Calculates the sum of all node values in a BST within [low, high].
        Uses iterative DFS with BST pruning to avoid Python recursion depth limits.
        """
        if not root:
            return 0

        total_sum = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue

            # If node's value is within range, add to total
            if low <= node.val <= high:
                total_sum += node.val

            # Pruning logic based on BST properties:
            # Only traverse left child if current value > low,
            # otherwise all left descendants are strictly less than low.
            if node.val > low and node.left:
                stack.append(node.left)

            # Only traverse right child if current value < high,
            # otherwise all right descendants are strictly greater than high.
            if node.val < high and node.right:
                stack.append(node.right)

        return total_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A naive approach would traverse every node in the tree (e.g., standard pre-order/in-order traversal) and sum the values falling within `[low, high]`. However, this fails to leverage the Binary Search Tree (BST) invariants.

In a BST:
- All nodes in `node.left` have values strictly less than `node.val`.
- All nodes in `node.right` have values strictly greater than `node.val`.

We can prune subtrees that cannot possibly contain values in `[low, high]`:
1. If `node.val < low`, every node in `node.left` will also be `< low`. Thus, we prune `node.left` and only traverse `node.right`.
2. If `node.val > high`, every node in `node.right` will also be `> high`. Thus, we prune `node.right` and only traverse `node.left`.
3. If `low <= node.val <= high`, `node.val` is in the range. We accumulate `node.val` and must search both `node.left` and `node.right`.

While a recursive DFS is elegant, Python's default recursion depth limit is 1,000. With up to $20,000$ nodes in a potentially skewed tree, recursion can trigger a `RecursionError`. Hence, an **iterative DFS** using an explicit stack is the robust, production-grade choice.

---

### Step-by-Step Approach

1. **Edge Case Handling**: If `root` is `None`, return `0`.
2. **Initialize Data Structures**:
   - `total_sum = 0` to accumulate the result.
   - `stack = [root]` to manage nodes to visit.
3. **Iterative Traversal**:
   - Pop a node from `stack`.
   - If `low <= node.val <= high`, add `node.val` to `total_sum`.
   - If `node.val > low`, push `node.left` onto the stack (if it exists).
   - If `node.val < high`, push `node.right` onto the stack (if it exists).
4. **Return Result**: Once the stack is empty, return `total_sum`.

---

### Complexity Analysis

- **Time Complexity:** 
  - **Worst Case:** $\mathcal{O}(N)$ where $N$ is the number of nodes in the tree. This occurs when all nodes fall within `[low, high]` or when the tree is unbalanced and every branch must be explored.
  - **Average Case:** $\mathcal{O}(K + H)$, where $K$ is the number of nodes in `[low, high]` and $H$ is the tree height. We only visit the valid nodes and the boundary search paths leading to them.
- **Space Complexity:** 
  - $\mathcal{O}(H)$, where $H$ is the height of the tree, representing the maximum number of nodes stored in the stack at any time.
  - In a balanced BST, $H = \mathcal{O}(\log N)$. In the worst-case (completely skewed tree), $H = \mathcal{O}(N)$.

---

### Common Pitfalls / Mistakes

1. **Ignoring BST Properties:** Visiting every node unconditionally (standard $\mathcal{O}(N)$ traversal) works, but signals to the interviewer that you aren't optimizing or utilizing data structure properties.
2. **Recursion Stack Overflow:** In Python, a skewed tree with $20,000$ nodes exceeds the default recursion limit ($1,000$). Iterative solutions avoid this pitfall.
3. **Inclusive Range Boundary Mistakes:** Using strict inequalities (`node.val > low` or `node.val < high`) for the value check rather than inclusive (`low <= node.val <= high`).
4. **Incorrect Pruning Conditions:** Forgetting that if `node.val == low`, you can still skip the left subtree, but if `node.val > low`, the left subtree might contain valid values.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if queries are frequent (e.g., millions of range sum queries on an immutable BST)?
**Answer:** Precomputing subtree sums and node counts or augmenting the BST into an Order Statistic Tree / Fenwick tree variant allows answering range sums in $\mathcal{O}(H)$ or $\mathcal{O}(\log N)$ without visiting every node in the range:
- Store at each node `node.subtree_sum` (sum of all nodes in its subtree).
- A helper function `sum_less_than_or_equal(x)` can compute the prefix sum in $\mathcal{O}(H)$ time by accumulating `left.subtree_sum + curr.val` whenever turning right.
- Then, `range_sum(low, high) = sum_less_than_or_equal(high) - sum_less_than_or_equal(low - 1)`.

#### 2. What if memory is strictly $\mathcal{O}(1)$ beyond the tree itself?
**Answer:** We can use **Morris In-Order Traversal**, which uses temporary threading (modifying right pointers of predecessors) to traverse the BST without a call stack or auxiliary data structures in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ extra space.

#### 3. What if the tree is distributed across multiple machines (large scale)?
**Answer:** Partition the BST across machines based on key ranges. Given a range $[low, high]$, route the query only to the machines holding key partitions that overlap with $[low, high]$, perform local range sums, and aggregate the results via a map-reduce / scatter-gather pattern.
