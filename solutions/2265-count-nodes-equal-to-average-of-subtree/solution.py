# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        Calculates the number of nodes where the node's value equals
        the integer average of its subtree.
        """
        matching_node_count = 0

        def post_order(node: TreeNode) -> tuple[int, int]:
            nonlocal matching_node_count
            if not node:
                # (subtree_sum, subtree_node_count)
                return 0, 0
            
            # Post-order traversal: process left and right subtrees first
            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)
            
            # Aggregate values for the current subtree rooted at `node`
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check condition: integer division represents floor rounding
            if current_sum // current_count == node.val:
                matching_node_count += 1
                
            return current_sum, current_count

        post_order(root)
        return matching_node_count
