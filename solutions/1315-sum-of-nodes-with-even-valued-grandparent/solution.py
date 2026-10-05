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
