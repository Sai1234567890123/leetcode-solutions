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
