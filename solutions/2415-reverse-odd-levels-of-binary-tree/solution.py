# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        def dfs(node1: TreeNode | None, node2: TreeNode | None, level: int) -> None:
            # Base case: Since it's a perfect binary tree, if node1 is None, node2 is also None
            if not node1 or not node2:
                return

            # If the current level is odd, swap the values of the mirrored nodes
            if level % 2 == 1:
                node1.val, node2.val = node2.val, node1.val

            # Recurse symmetrically:
            # Pair the leftmost child of the left subtree with the rightmost child of the right subtree
            dfs(node1.left, node2.right, level + 1)
            # Pair the rightmost child of the left subtree with the leftmost child of the right subtree
            dfs(node1.right, node2.left, level + 1)

        # Start recursion with the children of the root at level 1
        dfs(root.left, root.right, 1)
        return root
