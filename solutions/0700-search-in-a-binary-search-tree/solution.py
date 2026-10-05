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
