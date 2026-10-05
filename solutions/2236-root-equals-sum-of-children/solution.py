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
