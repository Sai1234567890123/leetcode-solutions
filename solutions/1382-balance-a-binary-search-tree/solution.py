# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        """
        Balances an unbalanced Binary Search Tree (BST).
        
        Strategy:
        1. Perform an in-order traversal to extract nodes in sorted order.
           We can collect the node references directly to reuse them.
        2. Recursively construct a height-balanced BST from the sorted list
           by choosing the median element as the subtree root.
        """
        sorted_nodes = []
        
        def inorder(node: TreeNode | None) -> None:
            if not node:
                return
            inorder(node.left)
            sorted_nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        def build_balanced_bst(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            
            mid = (left + right) // 2
            curr = sorted_nodes[mid]
            
            # Recursively build left and right subtrees
            curr.left = build_balanced_bst(left, mid - 1)
            curr.right = build_balanced_bst(mid + 1, right)
            
            return curr
        
        return build_balanced_bst(0, len(sorted_nodes) - 1)
