# 1315. Sum of Nodes with Even-Valued Grandparent

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/)  
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

## 📝 Problem Statement

Given the `root` of a binary tree, return *the sum of values of nodes with an **even-valued grandparent***. If there are no nodes with an **even-valued grandparent**, return `0`.

A **grandparent** of a node is the parent of its parent if it exists.

 
Example 1:

```

**Input:** root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
**Output:** 18
**Explanation:** The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

```

Example 2:

```

**Input:** root = [1]
**Output:** 0

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
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        """
        Calculates the sum of values of all nodes with an even-valued grandparent.
        Utilizes DFS passing down whether the parent and grandparent are even.
        """
        def dfs(node: TreeNode | None, is_parent_even: bool, is_grandparent_even: bool) -> int:
            if not node:
                return 0
            
            # If the grandparent is even, this node's value contributes to the sum
            total = node.val if is_grandparent_even else 0
            
            # Determine if current node is even for its children and grandchildren
            current_is_even = (node.val % 2 == 0)
            
            # Recurse down to left and right subtrees:
            # - The child's parent status is `current_is_even`
            # - The child's grandparent status is `is_parent_even`
            total += dfs(node.left, current_is_even, is_parent_even)
            total += dfs(node.right, current_is_even, is_parent_even)
            
            return total
        
        # At the root, neither parent nor grandparent exists
        return dfs(root, is_parent_even=False, is_grandparent_even=False)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A node $X$ contributes to the total sum if its grandparent is even. There are two standard approaches:
1. **Lookahead (Top-down sum addition):** Whenever we encounter an even node, we look 2 levels ahead to its grandchildren (`node.left.left`, `node.left.right`, `node.right.left`, `node.right.right`) and sum their values if they exist. While functional, this leads to excessive `None` checking (`node.left is not None`, etc.) and cluttered code.
2. **Context Passing (State propagation):** Instead of peering into the future, we pass contextual history down the recursion tree. Each recursive call receives two boolean flags:
   - `is_parent_even`: Is the immediate parent node even?
   - `is_grandparent_even`: Is the grandparent node even?

When visiting any node `u`:
- If `is_grandparent_even` is `True`, add `u.val` to the running sum.
- When recursing into `u`'s children, the new parent becomes `u` (i.e., `u.val % 2 == 0`), and the new grandparent becomes `is_parent_even`.

This keeps the code concise, robust against `None` references, and completely decoupled from looking ahead.

---

### Step-by-Step Approach

1. **Base Case:** If `node` is `None`, return `0`.
2. **Value Accumulation:** Initialize `total = node.val` if `is_grandparent_even` is `True`, else `0`.
3. **State Transition:** Compute `current_is_even = (node.val % 2 == 0)`.
4. **Recurse:**
   - Left subtree: `dfs(node.left, current_is_even, is_parent_even)`
   - Right subtree: `dfs(node.right, current_is_even, is_parent_even)`
5. **Return:** Sum the current contribution and the results from both subtrees.
6. **Initialization:** Start at `root` with `is_parent_even = False` and `is_grandparent_even = False`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of nodes in the binary tree. Every node is visited exactly once.
- **Space Complexity:** $\mathcal{O}(H)$, where $H$ is the height of the tree, representing the recursion stack. In the worst case (skewed tree), $H = N \implies \mathcal{O}(N)$. In the best/average case (balanced tree), $H = \log N \implies \mathcal{O}(\log N)$. No additional dynamic heap allocations are made.

---

### Common Pitfalls / Mistakes Candidates Make

1. **AttributeError / Null Pointer Dereferences:** When using the "lookahead" approach, candidates often write `if node.val % 2 == 0: total += node.left.left.val` without checking whether `node.left` exists first.
2. **Double Counting:** Attempting to do both top-down grandchild collection and bottom-up aggregation without clear separation.
3. **State Propagation Errors:** Mixing up the arguments when passing down the state (e.g., passing `current_is_even` as the grandparent instead of the parent).

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the tree is extremely deep and causes a recursion stack overflow?
*Answer:* We can implement an iterative traversal using either BFS (queue) or DFS (explicit stack). With BFS, we store tuples of `(node, parent_is_even, grandparent_is_even)`. This avoids recursion stack overflow and bounds memory usage to the maximum width of the tree ($\mathcal{O}(W)$ where $W \le N/2$).

#### 2. What if $k$-th ancestor condition is required instead of just grandparent ($k = 2$)?
*Answer:* 
- If $k$ is small/constant, we can pass a fixed-size bitmask or a circular buffer/tuple of size $k$ representing the parity of the last $k$ ancestors.
- If $k$ is large, we can maintain an active path list or stack during DFS: `path_parities.append(node.val % 2 == 0)`. When visiting a node, check `path_parities[-k-1]` in $\mathcal{O}(1)$ time, and pop when backtracking.

#### 3. How would you solve this with $\mathcal{O}(1)$ auxiliary space?
*Answer:* We can use **Morris Traversal**. By establishing temporary threads from the in-order predecessor to the current node, we can traverse the tree without a recursion stack or queue. To track ancestors with $\mathcal{O}(1)$ space, we can maintain the path length or look ahead to grandchildren when at an even node, using standard pointer validation.
