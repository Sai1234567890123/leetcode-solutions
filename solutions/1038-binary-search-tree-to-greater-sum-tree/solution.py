# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        """
        Converts a Binary Search Tree to a Greater Sum Tree using
        reverse in-order traversal (Right -> Node -> Left).
        """
        running_sum = 0
        
        def reverse_inorder(node: TreeNode | None) -> None:
            nonlocal running_sum
            if not node:
                return
            
            # 1. Visit right subtree first (larger values)
            reverse_inorder(node.right)
            
            # 2. Process current node
            running_sum += node.val
            node.val = running_sum
            
            # 3. Visit left subtree (smaller values)
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
