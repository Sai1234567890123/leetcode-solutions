# 0654. Maximum Binary Tree

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/maximum-binary-tree/](https://leetcode.com/problems/maximum-binary-tree/)  
**Topics:** Array, Divide and Conquer, Stack, Tree, Monotonic Stack, Binary Tree, Cartesian Tree

---

## 📝 Problem Statement

You are given an integer array `nums` with no duplicates. A **maximum binary tree** can be built recursively from `nums` using the following algorithm:

	- Create a root node whose value is the maximum value in `nums`.

	- Recursively build the left subtree on the **subarray prefix** to the **left** of the maximum value.

	- Recursively build the right subtree on the **subarray suffix** to the **right** of the maximum value.

Return *the **maximum binary tree** built from *`nums`.

 
Example 1:

```

**Input:** nums = [3,2,1,6,0,5]
**Output:** [6,3,5,null,2,0,null,null,1]
**Explanation:** The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

```

Example 2:

```

**Input:** nums = [3,2,1]
**Output:** [3,null,2,null,1]

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
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        """
        Constructs the Maximum Binary Tree (Cartesian Tree) in O(N) time
        using a monotonic decreasing stack.
        """
        stack: list[TreeNode] = []

        for num in nums:
            curr = TreeNode(num)
            
            # Maintain a monotonic decreasing stack.
            # Any node smaller than `curr` must be in `curr`'s left subtree,
            # because it appeared before `curr` and `curr` is greater.
            # The last popped node will directly become `curr.left`.
            while stack and stack[-1].val < num:
                curr.left = stack.pop()
            
            # If the stack is not empty, the node at stack[-1] is greater than `curr`
            # and appeared before `curr`. Therefore, `curr` must be in stack[-1]'s right subtree.
            if stack:
                stack[-1].right = curr
            
            # Push the current node onto the stack.
            stack.append(curr)

        # The bottom of the stack holds the maximum element of the entire array,
        # which is the root of the Cartesian Tree.
        return stack[0] if stack else None
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem defines a **Cartesian Tree** where:
1. An **in-order traversal** of the tree yields the original array sequence.
2. The tree obeys the **max-heap property** (every parent's value is greater than its children's values).

#### The Naive Recursive Approach ($O(N^2)$)
A direct translation of the problem description finds the maximum element in the current range $[L, R]$, sets it as the root, and recursively calls itself on $[L, \text{max\_idx} - 1]$ and $[\text{max\_idx} + 1, R]$. In the worst case (e.g., strictly ascending or descending arrays), finding the maximum takes $O(N)$ per level with depth $O(N)$, resulting in $O(N^2)$ time.

#### The Optimal Monotonic Stack Approach ($O(N)$)
We can process elements iteratively from left to right while maintaining a **monotonic decreasing stack** of tree nodes:
- When a new element `num` arrives, it must be to the right of all previous elements.
- Any elements currently on the stack that are **smaller** than `num` cannot be parents of `curr`. Since they appeared before `num`, they must reside in `curr`'s **left subtree**. Specifically, as we pop them, the most recently popped element becomes the direct left child of `curr`.
- After removing all smaller elements, if the stack still has an element, that element is **larger** than `num` and appeared before it. Thus, `curr` belongs to its **right subtree**.
- Finally, `curr` is pushed onto the stack.

By the end of the iteration, the bottom of the stack (`stack[0]`) is the global maximum and the root of the tree.

---

### Step-by-Step Approach

1. Initialize an empty list `stack`.
2. Iterate through each `num` in `nums`:
   - Instantiate `curr = TreeNode(num)`.
   - While `stack` is not empty and `stack[-1].val < num`:
     - Pop `node = stack.pop()`.
     - Assign `curr.left = node`. (Each popped node was smaller than the subsequent one popped, so setting `curr.left` repeatedly correctly leaves the largest among the smaller elements as the direct left child).
   - If `stack` is non-empty, assign `stack[-1].right = curr`.
   - Push `curr` to `stack`.
3. Return `stack[0]` (the root).

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$. Each element is pushed onto the stack exactly once and popped at most once. Tree node child assignments take $\mathcal{O}(1)$ time. Thus, the total time is strictly linear.
- **Space Complexity:** $\mathcal{O}(N)$. In the worst case (a strictly decreasing array), all $N$ nodes will be on the stack at the same time. The tree itself also occupies $\mathcal{O}(N)$ memory.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Settling for $O(N^2)$ recursion:** Many candidates immediately implement the divide-and-conquer approach. While simple, top tech companies expect candidates to recognize the Cartesian tree pattern and optimize to $O(N)$.
2. **Incorrect Left Child Assignment:** Forgetting that when popping multiple elements from the stack, only the *last* popped element (which is the largest among the smaller elements popped) should be the direct left child of `curr`. The loop `curr.left = stack.pop()` naturally accomplishes this.
3. **Array Slicing Overhead:** In the recursive approach, doing `nums[:max_idx]` and `nums[max_idx+1:]` incurs heavy memory allocation and copy overhead ($\mathcal{O}(N)$ per slice), causing Time Limit Exceeded (TLE) or Memory Limit Exceeded (MLE). Always pass indices $[L, R]$ if using recursion.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if `nums` can contain duplicate values?
- **Answer:** The definition of Cartesian trees assumes distinct keys to guarantee uniqueness of the tree structure. If duplicates exist, we must break ties deterministically:
  - We can define the "maximum" as either the *first* occurrence or the *last* occurrence.
  - In the monotonic stack, changing the condition from `stack[-1].val < num` to `<` vs `<=` determines whether the earlier or later duplicate becomes the parent.

#### 2. Can we build this tree online from a data stream?
- **Answer:** Yes! The monotonic stack algorithm processes elements in an **online, streaming fashion**. We do not need the full array in advance. As each number arrives from the stream, we perform the while-pop, link, and push operations. The current root of the tree is always `stack[0]`.

#### 3. What if memory is constrained (e.g., $N = 10^9$) and the tree cannot fit in RAM?
- **Answer:** If storing node pointers in memory is impossible:
  - We can compute the parent array on disk or write out nodes directly.
  - The stack only needs to store indices/values of the "right spine" of the tree. The maximum depth of the right spine in practice is often much smaller than $N$, drastically reducing the working memory required during stream processing.
