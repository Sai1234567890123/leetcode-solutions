# 0700. Search in a Binary Search Tree

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/search-in-a-binary-search-tree/](https://leetcode.com/problems/search-in-a-binary-search-tree/)  
**Topics:** Tree, Binary Search Tree, Binary Tree

---

## 📝 Problem Statement

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

 
Example 1:

```

**Input:** root = [4,2,7,1,3], val = 2
**Output:** [2,1,3]

```

Example 2:

```

**Input:** root = [4,2,7,1,3], val = 5
**Output:** []

```

 
**Constraints:**

	- The number of nodes in the tree is in the range `[1, 5000]`.

	- `1 7`

	- `root` is a binary search tree.

	- `1 7`

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
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        Iteratively search for a node with value `val` in a Binary Search Tree.
        
        Using an iterative approach guarantees O(1) auxiliary space, avoiding
        the call stack overhead of recursive traversal.
        """
        curr = root
        
        while curr is not None and curr.val != val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
                
        # Returns the node if found, or None if the subtree doesn't contain val
        return curr
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A Binary Search Tree (BST) possesses an invariant property:
- For any given node `curr`, all values in its left subtree are strictly less than `curr.val`, and all values in its right subtree are strictly greater than `curr.val`.

This property allows us to discard half of the remaining search space at each step, analogous to binary search in a sorted array:
1. If `val == curr.val`, we have found the target node and can return it immediately.
2. If `val < curr.val`, the target value can only exist in the left subtree.
3. If `val > curr.val`, the target value can only exist in the right subtree.

While recursion is straightforward, an **iterative solution** is strictly superior in production environments because it uses $O(1)$ auxiliary memory and eliminates the risk of call stack overflow on skewed trees (where depth $H \approx N$).

---

### Step-by-Step Approach

1. Initialize a pointer `curr = root`.
2. Loop while `curr` is not `None` and `curr.val != val`:
   - If `val < curr.val`, update `curr = curr.left`.
   - Otherwise (`val > curr.val`), update `curr = curr.right`.
3. When the loop terminates:
   - If the node was found, `curr` points to it.
   - If the value does not exist in the BST, `curr` will be `None`.
4. Return `curr`.

---

### Complexity Analysis

- **Time Complexity:** 
  - **Average Case:** $O(\log N)$, where $N$ is the number of nodes in a balanced BST.
  - **Worst Case:** $O(H) = O(N)$, where $H$ is the height of the tree. This occurs when the tree degrades into a linked list (skewed BST).
- **Space Complexity:** 
  - $O(1)$ auxiliary space. Unlike the recursive solution which uses $O(H)$ stack space, the iterative approach maintains only a single pointer.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Choosing Recursion Without Justification:** Recursive code is concise, but in an interview setting, failing to recognize that the recursion can be converted to an $O(1)$ space iteration signals a lack of memory awareness.
2. **Treating it as a General Binary Tree:** Performing a full traversal (e.g., BFS or DFS traversing both left and right children) wastes the BST ordering property, resulting in unnecessary $O(N)$ time on balanced trees instead of $O(\log N)$.
3. **Null Pointer Exceptions:** Forgetting to check if `root` is `None` before dereferencing `root.val`. The `while curr is not None` condition handles empty trees and missing values gracefully.

---

### Real Interview Follow-Up Questions

#### 1. What if the BST allows duplicate keys?
- **Answer:** We need to clarify requirements with the interviewer: should we return the *first* encountered matching node, the *shallowest*, or *all* matching nodes? 
  - If BST property defines duplicates as $\le$ going to the left (or $\ge$ going to the right), we may need to continue traversing in that specific direction even after finding a match if all instances need to be collected.

#### 2. How would you handle concurrent reads and writes to this BST?
- **Answer:** 
  - **Coarse-grained locking:** Place a Read-Write Lock (`shared_mutex`) on the entire tree. Readers can run concurrently, while mutations (insert/delete) require exclusive access.
  - **Fine-grained locking (Hand-over-hand locking):** Acquire read locks on nodes as you traverse down. Lock child, then release parent.
  - **Lock-Free BSTs / Copy-on-Write:** Use immutable BST structures (persistent data structures) or lock-free BST algorithms based on Compare-And-Swap (CAS) pointers (e.g., Ellen et al.'s non-blocking BST).

#### 3. What if the tree is too large to fit in memory (External Memory / Disk-based)?
- **Answer:** Standard BSTs have high tree height, causing too many random disk I/O operations (one I/O per node accessed). We would transition to a **B-Tree** or **B+ Tree**, which has high fan-out (thousands of keys per node) designed to match disk block/page sizes, minimizing disk read operations to $O(\log_B N)$ where $B$ is the page size.
