# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        idx = 0
        n = len(preorder)

        def build(upper_bound: float) -> TreeNode | None:
            nonlocal idx
            # Base case: exhausted array or current value exceeds the allowed upper bound
            if idx == n or preorder[idx] > upper_bound:
                return None

            # The current element becomes the root of this subtree
            val = preorder[idx]
            idx += 1
            root = TreeNode(val)

            # Left child's values must be strictly less than the current node's value
            root.left = build(val)
            # Right child's values must be strictly less than the inherited upper bound
            root.right = build(upper_bound)

            return root

        return build(float('inf'))
