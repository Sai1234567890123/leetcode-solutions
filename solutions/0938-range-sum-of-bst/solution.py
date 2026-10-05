# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        """
        Calculates the sum of all node values in a BST within [low, high].
        Uses iterative DFS with BST pruning to avoid Python recursion depth limits.
        """
        if not root:
            return 0

        total_sum = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue

            # If node's value is within range, add to total
            if low <= node.val <= high:
                total_sum += node.val

            # Pruning logic based on BST properties:
            # Only traverse left child if current value > low,
            # otherwise all left descendants are strictly less than low.
            if node.val > low and node.left:
                stack.append(node.left)

            # Only traverse right child if current value < high,
            # otherwise all right descendants are strictly greater than high.
            if node.val < high and node.right:
                stack.append(node.right)

        return total_sum
