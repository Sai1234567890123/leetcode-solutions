# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        """
        Calculates the sum of values of the deepest leaves in the binary tree
        using a single-pass Depth-First Search (DFS).
        """
        max_depth = -1
        deepest_sum = 0

        def dfs(node: TreeNode | None, depth: int) -> None:
            nonlocal max_depth, deepest_sum
            if not node:
                return

            # Found a node at a strictly greater depth: reset sum and update max_depth
            if depth > max_depth:
                max_depth = depth
                deepest_sum = node.val
            # Found another node at the current maximum depth: accumulate value
            elif depth == max_depth:
                deepest_sum += node.val

            # Recurse down left and right subtrees
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return deepest_sum
