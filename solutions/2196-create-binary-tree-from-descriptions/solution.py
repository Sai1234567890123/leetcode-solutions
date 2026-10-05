# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        nodes: dict[int, TreeNode] = {}
        children: set[int] = set()

        for parent_val, child_val, is_left in descriptions:
            # Retrieve or create parent node
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            parent_node = nodes[parent_val]

            # Retrieve or create child node
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            child_node = nodes[child_val]

            # Connect parent to child based on is_left flag
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            # Record child to identify the root later
            children.add(child_val)

        # The root is the only node that never appears as a child
        for parent_val, _, _ in descriptions:
            if parent_val not in children:
                return nodes[parent_val]

        return None
